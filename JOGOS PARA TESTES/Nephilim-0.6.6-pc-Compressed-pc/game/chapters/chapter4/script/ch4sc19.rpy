label ch4sc19:

    window hide dissolve
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (2.0)
    scene ch4sc19_000 with Dissolve(2.0)
    $ renpy.pause()
    scene ch4sc19_001 with Dissolve(1.5)
    ki "Surely you’re kidding?!"
    ki "You can’t be serious..."
    scene ch4sc19_002 with dissolve
    pl "Absolutely, I’m serious."
    pl "It’s the only way to make sure it doesn’t happen again!"
    scene ch4sc19_003 with dissolve
    ki "We can’t just destroy something like that."
    ki "There’s no telling what'll happen!"
    scene ch4sc19_002 with dissolve
    pl "Did you already forget what happened to father?! He went mad because of that thing!"
    pl "Are you willing to risk the same thing happening again? To [mc]?"
    scene ch4sc19_003 with dissolve
    ki "Of course not!"
    ki "I'd never risk [mc]’s wellbeing!"
    scene ch4sc19_002 with dissolve
    pl "Then it’s settled..."
    pl "We destroy the ring."
    scene black with Dissolve(1.5)
    "The two argue back and forth for the better part of an hour..."
    scene ch4sc19_004 with Dissolve(1.5)
    ki "It’s up to [mc], he is the one who has it."
    ki "What do you think we should do with it? Do you feel any different after taking it?"
    scene ch4sc19_005 with dissolve
    pl "What my sister is trying to say is... have you felt like murdering us yet?"
    mct "Kira isn’t usually this timid."
    mct "She’s clearly still affected by how severely the ring influenced their father."
    scene ch4sc19_006 with dissolve
    mc "Girls... look at me."
    mc "First off... No, Pearl. I haven’t felt like murdering you."
    mc "I’ve been trying to be aware if the ring was trying to influence me, even subtly."
    mc "But I haven’t felt anything from it, other than it has a potent magical aura."
    mc "I suspect it can only affect someone if they wear it on their finger."
    scene ch4sc19_007 with dissolve
    ki "So... you’re not in danger of becoming like Father?"
    scene ch4sc19_006 with dissolve
    mc "No."
    mc "And if I do, then I’m counting on you girls to bring me back."
    scene ch4sc19_008 with dissolve
    pl "Don’t worry!"
    pl "We’ll whoop your ass until you come to your senses!"
    ###Choice###
    menu:
        "Inform the girls of what's to be done. {color=#ffee54}Leadership{/color}":
            scene ch4sc19_006 with dissolve
            mc "I’m keeping the ring."
            mc "I work for the adventurer’s guild, as you know."
            mc "They know more than any of us about investigating artifacts and keeping them safely."
            scene black with Dissolve(1.5)
            $ renpy.pause(1)
            scene ch2sc23_22 with Dissolve(1.5)
            mc "I have another ring, similar to this back home. It doesn’t have the same darkness but..."
            mc "Its magic is just as potent."
            mc "I suspect they were both amongst the ten rings of power used to defeat a tyrant named Balthazar, 500 years ago."
            scene ch4sc19_006 with Dissolve(1.5)
            mc "Your father already admitted that his ring was one of them."
            mc "And now that I've felt its magic for myself... I believe they are connected."
            $ leadership += 1
            mc "But I won’t know for sure until I return to the guild and show them this one."
            "Your successfully swayed the girls opinion, {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

        "Convince the girls to keep the ring. {color=#2bff8b}Persuasion{/color}":
            scene ch4sc19_006 with dissolve
            mc "I believe it's in our best interest to keep it."
            mc "We have more to learn about the effects it has, but we'll be cautious."
            scene black with Dissolve(1.5)
            $ renpy.pause(1)
            scene ch2sc23_22 with Dissolve(1.5)
            mc "I have another ring, similar to this back home. It doesn’t have the same darkness but..."
            mc "Its magic is just as potent."
            mc "I suspect they were both amongst the ten rings of power used to defeat a tyrant named Balthazar, 500 years ago."
            scene ch4sc19_006 with Dissolve(1.5)
            mc "Your father already admitted that his ring was one of them."
            mc "And now that I've felt its magic for myself... I believe they are connected."
            $ persuasion += 1
            mc "But I won’t know for sure until I return to the guild and show them this one."
            mc "I know you girls don't like it, but put your faith in me, I won't succumb to its effects."
            "Your successfully convinced the girls to trust your decision, {b}{color=#2bff8b}Persuasion{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."


    scene ch4sc19_008 with dissolve
    pl "Okay..."
    pl "I still think we should destroy it, but if this is your decision, I will respect it."
    scene ch4sc19_006 with dissolve
    mc "Noted. Don’t worry, I’ll be very careful with it."
    scene ch4sc19_007 with dissolve
    ki "I guess that settles it, then. Just... be careful."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch4sc19_009 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc19_010 with Dissolve(1.5)
    $ renpy.pause()
    ki "*Drawn out sigh* ..."
    mc "Okay, let it out."
    scene ch4sc16_164 with dissolve
    ki "..."
    mc "Out with it. You’ve been sitting here in silence for the last hour."
    scene ch4sc16_163 with dissolve
    ki "What? Can’t I just be enjoying the view?"
    scene ch4sc16_164 with dissolve
    mc "With your eyes closed?"
    ki "..."
    scene ch4sc16_163 with dissolve
    ki "Aren’t you going to miss this?"
    ki "The fresh sea-breeze? The sound of the waves as the ship sails toward a destination?"
    ki "The noises of the seagulls when Kelly has been snacking on deck..."
    ki "Pedro yelling at you for peeling his potatoes wrong?"
    scene ch4sc16_164 with dissolve
    ki "..."
    mc "Kira... Are you trying to ask me if I’ll miss... {b}YOU?{/b}"
    scene ch4sc16_163 with dissolve
    ki "No!"
    scene ch4sc16_164 with dissolve
    $ renpy.pause(1)
    scene ch4sc16_163 with dissolve
    ki "Maybe?"
    ki "Will you?"
    scene ch4sc19_011 with dissolve
    mc "I’ll miss the heck out of you."
    mc "I’m going to miss the way you make up stuff for Flynn to do, so he has a purpose out here."
    mc "I’ll miss the way you care about the crew, even when you try to hide it."
    scene ch4sc19_012 with dissolve
    mc "I’ll miss seeing you at the helm of the Banshee, steering us towards a new horizon."
    mc "I’ll miss the way your fiery red hair catches the rays of the sun."
    scene ch4sc19_011 with dissolve
    mc "I’ll miss the way you threaten to end me, every time I tease you."
    scene ch4sc19_012 with dissolve
    mc "I’ll miss those emerald eyes of yours that always give away your intentions."
    mc "I'll miss you, Kira... Captain of the Bloody Banshee... Princess of Looter’s bay."
    scene ch4sc19_013 with dissolve
    ki "You..."
    ki "You really noticed all those things about me?"
    scene ch4sc19_012 with dissolve
    mc "Of course. You’re amazing and I’m glad to have you in my life."
    scene ch4sc19_013 with dissolve
    ki "You..."
    ki "You still want me in your life after we reach Luxenford?"
    scene ch4sc19_011 with dissolve
    mc "Of course. Kira..."
    mc "We didn’t just go through all this together just to leave each other behind."
    scene ch4sc19_014 with dissolve
    ki "Good! ... good."
    ki "I want that as well... to be in each other’s lives moving forward."
    scene ch4sc19_013 with dissolve
    ki "I was afraid you'd want to forget about me once you got back to land."
    scene ch4sc19_012 with dissolve
    mc "Not possible."
    mc "You’ve left quite the impression... *Chuckles*"
    scene ch4sc19_014 with dissolve
    ki "*Smirks* Idiot..."
    scene ch4sc16_164 with dissolve
    ki "..."
    scene ch4sc16_163 with dissolve
    ki "After we drop you and Flynn off at the port in Luxenford, Pearl, the crew, and I will head back to Looter’s Bay."
    scene ch4sc16_164 with dissolve
    mc "Really?"
    mc "I didn’t think you’d want to return there anytime soon."
    scene ch4sc16_163 with dissolve
    ki "We have to... we left the place without a leader."
    ki "It'll soon be complete chaos... cutthroats and scoundrels..."
    ki "All of them trying to gain control of the bay."
    ki "Pearl and I will have to sort out the mess and regain control."
    scene ch4sc16_164 with dissolve
    mc "I see, for what it's worth, I can think of none better than the two of you to take control of Looter's Bay."
    mc "Then it'll likely be a while until we cross paths again?"
    scene ch4sc16_163 with dissolve
    ki "*Sigh* Yeah..."
    scene ch4sc19_011 with dissolve
    mc "Promise me that you will come visit as soon as you’re done in Looter’s bay."
    scene ch4sc19_014 with dissolve
    ki "Y-You want that?"
    ki "*Excitedly* I... I would love to!!"
    ki "Then you could show me around Luxenford! I’ve only really seen the port..."
    scene ch4sc19_013 with dissolve
    ki "I mean, only if you want to..."
    scene ch4sc19_015 with dissolve
    mc "You bet."

    if kira_relationship == True:
        scene ch4sc19_015 with dissolve
        mc "We’ll go on a date."
        mc "Just the two of us... like Inmortui, but without the lightning storms... risen undead... and necromancers."
        scene ch4sc19_014 with dissolve
        ki "*Snickers* Inmortui had it's moments but yes, I'd much prefer a date that does not include any of that!"
        ki "Mmm... I’ve never been on a date!"
        scene ch4sc19_015 with dissolve
        mc "It seems you’re doing a lot of ‘firsts’ with me."
        scene ch4sc19_014 with dissolve
        ki "I wouldn’t have it any other way."
        ki "I can’t think of anyone else I would trust with my first times and... only times."
        ki "I should’ve said this earlier, but I’m going to miss you too! So much!"
        scene ch4sc19_016 with dissolve
        with vpunch
        ki "Mwaaah!"
        "Before you could react, this little redhead has planted her soft lips on yours."
        "She isn’t settling for a quick peck either..."
        "She continues to hold her lips against yours, feeling the warmth between them."
        "It’s easy to tell that she doesn’t wish to stop, but she finally pulls away."
        scene ch4sc19_014 with dissolve
        ki "We’re almost there, let’s get you home so you can help your friend!"
        mc "Alright, I'll go make sure Flynn has our stuff ready."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(2)

    else:
        scene ch4sc19_014 with dissolve
        ki "We’re almost there, let’s get you and Flynn home so you can finally help your friend!"
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(2)

    scene ch4sc19_017 with Dissolve(2)
    $ renpy.pause()
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_018 with Dissolve(2)
    $ renpy.pause()
    kl "Buuuuh! I don’t want to say goodbye..."
    mc "This isn’t goodbye. We’ll see each other again."
    kl "Promise?"
    mc "I promise."
    scene ch4sc19_019 with dissolve
    with vpunch
    kl "*Hugs tightly*"
    mct "This little girl really knows how to give a hug... she’s squishing herself against me."

    if kelly_relationship == True:
        scene ch4sc19_020 with dissolve
        kl "*Whispers*{size=-10}{b} Next time we see each other...{/b}{/size}"
        kl "*Whispers*{size=-10}{b} I will use your beautiful cock as my own personal sugarcane!{/b}{/size}"
        scene ch4sc19_019 with dissolve
        mc "Fuck... you’re going to make me hard."
        scene ch4sc19_020 with dissolve
        kl "*Whispers* {size=-10}{b}That’s how I prefer you. Hard and ready to satisfy me... *Giggles* Take care!{/b}{/size}"
        scene black with Dissolve(2)


    else:
        scene ch4sc19_019 with dissolve
        mc "Take care, Kelly."
        scene ch4sc19_020 with dissolve
        kl "You too!"
        kl "I look forward to our next adventure together!"
        scene black with Dissolve(2)

    scene ch4sc19_021 with Dissolve(2)
    $ renpy.pause()
    scene ch4sc19_022 with dissolve
    mc "Hey, you two."
    scene ch4sc19_023 with dissolve
    pl "[mc]!"
    pl "Kira was just telling me how handsome she thinks you are!"
    scene ch4sc19_024 with dissolve
    ki "Don’t let her fool you."
    ki "She was the one who was singing your praises..."
    scene ch4sc19_024 with dissolve
    pl "Oh? So you weren’t just saying how you wanted him to wrap his ‘strong, manly arms around you’?"
    pl "How you wanted to-"
    scene ch4sc19_025 with dissolve
    with vpunch
    ki "{b}ZIP IT!!{/b} Or you will be swimming back to Looter’s Bay!"
    ki "You can get real friendly with those fishes you love so much!"
    pl "*Mumbling* {b}Mhhh!! Mhmn!{/b}"
    scene ch4sc19_026 with dissolve
    mc "*Laughs*"
    bth "..."
    scene ch4sc19_027 with dissolve
    with vpunch
    evr "{b}HahahaH! HahH! HaHAhAhH!{/b}"
    scene ch4sc19_028 with dissolve
    mc "I’m going to miss you girls..."
    bth "..."
    scene ch4sc19_029 with dissolve
    pl "Group hug!"
    scene ch4sc19_030 with dissolve
    with vpunch
    pl "*Laughs* Yes! Get him, Kira!"
    mc "Girls! We’re gonna fall!"
    scene ch4sc19_031 with dissolve
    with vpunch
    pl "Show him no mercy! {b}Squish him!{/b}"
    scene ch4sc19_031 with dissolve
    ki "I’m squishing! Are you?!"
    pl "Trust me, he’s feeling both my squishies right now!"
    pl "And he looks like he’s enjoying them!"
    mct "Fuck... they really are soft."
    scene ch4sc19_032 with dissolve
    with vpunch
    ki "Yours? Pfft! He’s enjoying mine! {b}*Squishes breasts into you*{/b}"
    mc "Girls!!"
    scene ch4sc19_033 with dissolve
    with vpunch
    evr "*Laughs* Aaahh!"
    ki "*Laughs* Pearl, you dummy!"
    pl "*Laughs* You’re the one who weighs too much for him!"
    ki "*Laughs* As if! Your ass has way too much volume!"
    pl "*Laughs* That’s not even an insult, you... carrot-top!!"
    mc "*Groans* G-Girls..."
    "They release you and everyone gets back on their feet."
    scene black with Dissolve(1.5)
    scene ch4sc19_028 with Dissolve(1.5)
    mc "That’s a hug I won’t soon forget."
    mc "I'd better get going. Go show Looter’s Bay who their new Queens are."
    scene ch4sc19_034 with dissolve
    pl "Queens... It does have a nice ring to it. What do you say, sis?"
    scene ch4sc19_035 with dissolve
    ki "I say we go take back what’s ours, and show them what happens when you stand against us."
    scene ch4sc19_028 with dissolve
    mc "I look forward to hearing all about your conquests the next time you’re in the capital."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch4sc19_036 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    evr "Byeee! Take care [mc]! See you soon! We miss you already! Handsome! Nice ass!"
    scene ch4sc19_037 with dissolve
    fy "Are you heading to the adventurer’s guild?"
    mc "Mh-hm. There’s a certain someone I’m... eager to see."
    fy "I think I know exactly who you’re referring to."
    scene ch4sc19_038 with dissolve
    mc "What about you?"
    fy "I’m stopping by the Seafarer’s guild to give them my report, and then I’m getting some shut-eye!"
    scene ch4sc19_039 with dissolve
    mc "I’ll see you around, then. And Flynn, it was great having you along."
    fy "Count on it, cus! It was just like old times, but with hot women!"
    bth "*Chuckles*"
    scene black with Dissolve(2)
    scene ch4sc19_040 with Dissolve(1.5)
    sy "Pheeew! What a day huh?"
    el "Tell me about it ... I never thought I'd finish all those reports!"
    sy "I knoooow! *Sigh* That’s part of managing the guild, though."
    scene ch4sc19_041 with dissolve
    sy "But now we’re all caught-"
    el "What is it? You look like you’ve seen a ghost..."
    scene ch4sc19_042 with dissolve
    sy "Ooohh... nothing of the sort! Urrhh... I’ve gotta go see Dalen! Yup!"
    sy "Bye!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch4sc19_043 with Dissolve(1.5)
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    #####ANIMATION#####
    show mcel_re with fade
    $ renpy.pause(4, hard=True)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    scene ch4sc19_044 with Dissolve(1.5)
    mct "Fuck... I actually feel nervous."
    mct "She’s still as beautiful as I remember her..."
    mct "Huh? She’s... crying?"
    scene ch4sc19_045 with dissolve
    elt "He’s here... {b}HE’S ACTUALLY HERE!!{/b}"
    scene ch4sc19_046 with dissolve
    elt "*Sobs happily* He’s actually here!"
    elt "[mc] is finally back! {b}OH NO{/b}... I’m a total mess!"
    scene ch4sc19_047 with dissolve
    elt "Uh-Oh!"
    elt "It’s the first time we see each other in months, and I’m ugly crying!!"
    scene ch4sc19_048 with dissolve
    elt "I was supposed to be ready for this moment!"
    elt "My hair is a mess! My-"
    scene ch4sc19_049 with dissolve
    elt "This feeling... I'd recognize it anywhere. It’s his hand!"
    elt "*Purrs softly* Nnhh... I’ve missed him so much! His touch is so... soothing."
    mc "Care to tell me why the most beautiful girl in all of Midomir is crying?"
    elt "*Purrs* Mhnnwhh! He thinks I’m the most beautiful... even when I’m crying?!"
    scene ch4sc19_050 with dissolve
    el "S-Stop trying to make me blush, and give me the biggest hug of all time... like you promised!"
    scene ch4sc19_049 with dissolve
    mc "The biggest hug of all time, huh?"
    scene ch4sc19_050 with dissolve
    el "Yes! The biggest of them all!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mc "We'd better get started then."
    mc "Come here, you little kitten!"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_051 with dissolve
    #####ANIMATION#####
    show mcel_hug1 with fade
    $ renpy.pause(5, hard=True)
    #$ renpy.pause()
    scene ch4sc19_052 with dissolve
    with vpunch
    el "*Squeals* {b}Aiiihhh!{/b} *Laughs* I forgot how much of a brute you are!"
    scene ch4sc19_053 with dissolve
    mc "Oh? Sounds like someone wants me to put her down again?"
    scene ch4sc19_052 with dissolve
    el "{b}I SAID NO SUCH THING!!{/b}"
    el "You better not put me down for the next hour! Mh-hm!"
    scene ch4sc19_054 with dissolve
    $ renpy.pause(2)
    scene ch4sc19_055 with dissolve
    el "Hi..."
    scene ch4sc19_054 with dissolve
    mc "Hey you..."

    if eliza_path == True:
        scene ch4sc19_055 with dissolve
        el "Am I still your kitten?"
        scene ch4sc19_054 with dissolve
        mc "You’ll always be my kitten."
        scene ch4sc19_055 with dissolve
        el "You’re my lion."
        el "Now and always."
        scene ch4sc19_054 with dissolve
        mc "Now and always."
        scene ch4sc19_055 with dissolve
        el "I’m going to kiss you now..."
        scene ch4sc19_056 with dissolve
        $ renpy.pause()
        el "*Kiss* Mwaaah!"
        mct "I’ve missed her lips... Soft and tender, warm and inviting..."
        mct "I better pull back, otherwise I’m going to throw on her on the desk and show her just how much I’ve missed her."
        scene ch4sc19_057 with dissolve
        elt "Oh? H-He pulled away?"
        elt "Did I do something wrong?"
        scene ch4sc19_058 with dissolve
        mc "Sorry, I had to..."
        scene ch4sc19_059 with dissolve
        el "*Nervous* I-I understand. Y-You don’t feel the same anymore..."
        el "I thought this might happen when we were apart for so long..."
        scene ch4sc19_058 with dissolve
        mc "You’re right... I don’t."
        scene ch4sc19_057 with dissolve
        elt "I knew it... He never pulled away from a kiss before..."
        scene ch4sc19_058 with dissolve
        mc "I don’t feel the same... What I feel for you, Eliza. It has matured-"
        mc "Grown into something much more potent. Now that I know what it feels like to be apart from you..."
        mc "I don't like it. Not one bit."
        scene ch4sc19_057 with dissolve
        elt "Oh? His feelings are stronger?"
        elt "I feel the same. Just the thought of being apart from him again gives me stomache-aches!"
        scene ch4sc19_059 with dissolve
        el "Then why did you... break the kiss?"
        scene ch4sc19_058 with dissolve
        mc "I had to. If we kept kissing, I wouldn’t have been able to hold back."
        mc "I was about to throw you down on the desk and tear your clothes off..."
        scene ch4sc19_057 with dissolve
        elt "Heavens!! Please do!"
        elt "*Sigh* Sylph and Dalen are still here. Maybe it’s for the best he held back."
        scene ch4sc19_058 with dissolve
        mc "Erase any doubts from your mind. Kissing you and holding you? It’s the best feeling in the world."
        scene ch4sc19_060 with dissolve
        el "*Soft whisper* Then ... we should probably do it again."
        scene ch4sc19_061 with dissolve
        el "*Soft whisper* Wouldn’t you like to feel my soft cherry-lips merge with yours?"
        mc "Yes..."
        el "*Soft whisper* And feel my breasts press against you as passion overtakes us?"
        mc "Eliza... I do..."
        el "Mnnhh..."
        "You feel her warm, tantalizing breath on your lips."
        scene ch4sc19_062 with dissolve
        el "Nuh-uh!"
        el "You said it yourself. We won’t be able to hold back. And Sylph and Dalen are both still here."
        mct "*Heavy sigh* She’s right... I hate it when she’s right."
        el "Don’t look so defeated. I’ve saved up lots of kisses... among other things in my vault."
        el "And I intend to cash in... soon."
        mct "This girl. Innocent and cute, but also a little she-devil."
        mct "She enjoys teasing me far too much..."
        scene ch4sc19_058 with dissolve
        mc "Alright, alright. We’ll wait."
        mc "You said Dalen was still here? I need to talk to him about the artifact."
        scene ch4sc19_059 with dissolve
        el "Oh! Right! The artifact! You really found it, then?"
        scene ch4sc19_058 with dissolve
        mc "We both know I wouldn’t have returned without it."
        scene ch4sc19_059 with dissolve
        el "Can I come too?"
        scene ch4sc19_058 with dissolve
        mc "Of course. There’s a lot to know about it and it'll be your choice to use it, or not."
        mc "Let’s go see him."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(1.5)

    else:
        scene ch4sc19_058 with dissolve
        mc "Is Dalen still here? I need to talk to him about the artifact."
        scene ch4sc19_059 with dissolve
        el "Yeah, I think so. Oh, right! The artifact! You really found it, then?"
        scene ch4sc19_058 with dissolve
        mc "We both know I wouldn’t have returned without it."
        scene ch4sc19_059 with dissolve
        el "Can I come too?"
        scene ch4sc19_058 with dissolve
        mc "Of course. There’s a lot to know about it and it'll be your choice to use it or not."
        mc "Let’s go see him."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(1.5)

    scene ch4sc19_063 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    da "Ah, there you are."
    da "I was starting to wonder why Eliza was still here. Now I see why."
    scene ch4sc19_064 with dissolve
    el "Dalen! Look who I found!"
    scene ch4sc19_065 with dissolve
    da "Eliza... didn’t I tell you to stop bringing every guy you stumble across back here?"
    el "*Laughs* But this one is reeeaally handsome! And I heard he's a great adventurer!"
    el "Can I please keep this one?"
    da "*Chuckles* Just this one, then."
    scene ch4sc19_066 with dissolve
    mc "Alright, alright, you two... Dalen we need to discuss something."
    da "I suspected this wasn’t just a social call... Come, take a seat."
    scene black with dissolve
    scene ch4sc19_067 with dissolve
    da "So this is it, huh?"
    da "The Chalice of Vitality?"
    scene ch4sc19_068 with dissolve
    da "It does look ancient..."
    mc "Yeah. I'm thinking it's at least a few thousand years old."
    scene ch4sc19_069 with dissolve
    el "What does it do? How can this cure my legs?"
    mc "You will have to drink from it."
    scene ch4sc19_070 with dissolve
    el "Drink from it? That doesn’t seem so bad. Let’s get some water!"
    scene ch4sc19_068 with dissolve
    da "Not so fast. We don’t even know if there’s any side effects we should be aware of."
    scene ch4sc19_069 with dissolve
    el "Side effects? Like what?"
    scene ch4sc19_068 with dissolve
    da "Well it’s an artifact created by the divines themselves. They are ancient relics of the past."
    da "While they hold tremendous power, they usually also have some sort of a draw back."
    da "To ensure mortals can't just abuse them."
    scene ch4sc19_069 with dissolve
    el "Oh... Well, do we know what it does?"
    scene ch4sc19_071 with dissolve
    mc "Yeah. I do."
    "Both of them attentively look at you."
    mc "I met her... Lucid."
    scene ch4sc19_072 with dissolve
    da "Lucid... Mother of the Damned? She's one of the Seven Divines, according to legend."
    scene ch4sc19_071 with dissolve
    mc "She's the one who created this artifact. When I picked it up in the chamber on Inmortui..."
    mc "I was transported to her realm."
    mc "Apparently it's an enchantment she has cast on it, so she could guide whoever found it."
    scene ch4sc19_072 with dissolve
    da "To meet one of the Divines... remarkable. Did she tell you about its effects?"
    scene ch4sc19_071 with dissolve
    mc "She did. We didn’t have much time to talk, though, as the enchantment was short lived. But she did tell me quite a bit."
    scene ch4sc19_073 with dissolve
    mc "Eliza, this will not just cure your legs."
    mc "It will change you... permanently."
    scene ch4sc19_074 with dissolve
    el "Change me? How?"
    scene ch4sc19_073 with dissolve
    mc "When you drink from it, you will undergo a transformation of sorts, you will become-"
    mc "A vampire."
    scene ch4sc19_074 with dissolve
    with vpunch
    el "{b}WHAT?!{/b} V-Vampire?!"
    el "I-I can’t be a vampire?! Aren’t they just scary creatures from my mother’s books?"
    scene ch4sc19_075 with dissolve
    mc "I'm afraid not. You will become a pureblooded vampire. A direct descendant from Lucid’s own blood."
    mc "You will become immortal, Eliza. You won’t age, you won’t get sick, any injury you get will mend itself."
    mc "You'll become faster than any elf, stronger than any orc, you'll gain more abilities as you grow in power."
    mc "You won’t have to be afraid ever again."
    elt "..."
    elt "I can’t become a vampire... can I? Just saying that sounds ridiculous!"
    elt "But if I don’t, I’ll never walk again? I’ll be bound to become a burden to all my friends... to [mc]."
    scene ch4sc19_074 with dissolve
    el "What are the drawbacks?"
    el "I assume drinking blood is one of them? Uck!"
    scene ch4sc19_073 with dissolve
    mc "Yeah. You can still eat and drink normally, but it won’t give you any nourishment."
    mc "Only blood will satiate you."
    scene ch4sc19_074 with dissolve
    el "What else? I want to know everything."
    scene ch4sc19_073 with dissolve
    mc "Your emotions will be hard to control at first. Lucid said everything will feel ‘heightened’"
    mc "All emotions will be intensified, all your senses will be at their peak."
    mc "Happiness becomes bliss, sadness can turn to despair, anger becomes rage..."
    mc "Lucid warned me that emotions, or lack of control of them, is what makes most vampires turn feral."
    mc "They lose themselves in these heavy emotions until they can’t take it anymore, and snap."
    scene ch4sc19_074 with dissolve
    el "[mc], I don’t want that! What if I can’t handle it?!"
    el "I can't become some feral bloodsucker!"
    scene ch4sc19_073 with dissolve
    mc "I wouldn’t have brought this back and presented it to you-"
    mc "If there was even the slightest doubt in my mind that you couldn’t handle it."
    mc "Eliza, you’re the strongest person I’ve ever met."
    mc "Remember all the times you helped me through my rage?"
    mc "I will see you through this, if you choose it."
    mc "You won’t be alone, we have each other's backs."
    mc "Another drawback as you mentioned is the blood."
    mc "You will crave it, thirst for it... your body will scream for it."
    scene ch4sc19_076 with dissolve
    el "Ugh... I suspected as much..."
    scene ch4sc19_075 with dissolve
    elt "If I do this..."
    elt "I'll be able to keep up with [mc]... I will walk again, run again, jump again."
    scene ch4sc19_078 with dissolve
    elt "I believe him when he says I can do this. He believes in me."
    elt "*Sigh* There really isn't a choice."
    elt "If this is what fate has in store for me, I'll grab fate by it's balls and take control."
    scene ch4sc19_079 with dissolve
    el "This is crazy... But, okay."
    el "I’ll do it."
    el "I’m already set on doing whatever it takes to walk again."
    el "And if you really believe I can handle this? Then I’m all in."
    scene ch4sc19_080 with dissolve
    el "Now and always?"
    mc "Now and always."
    "She squeezes your hand and takes a deep breath."
    scene ch4sc19_070 with dissolve
    el "So... how do we do this?"
    scene ch4sc19_071 with dissolve
    mc "You will have to drink blood from the chalice."
    scene ch4sc19_073 with dissolve
    mc "Human blood, or at the very least, blood from a mortal race."
    scene ch4sc19_074 with dissolve
    el "Oh. Great... Wonderrrrful..."
    scene ch4sc19_076 with dissolve
    el "Wait... Human blood? Eeuuuw..."
    scene ch4sc19_074 with dissolve
    el "Where are we even supposed to get human blood?"
    scene ch4sc19_067 with dissolve
    da "Use mine."
    scene ch4sc19_069 with dissolve
    el "No way!"
    el "I can’t ask you to do that. Not after everything."
    scene ch4sc19_081 with dissolve
    da "You aren’t asking me... I’m offering."
    da "I want to help you."
    scene ch4sc19_082 with dissolve
    el "I don’t know, you’ve already done so much for me, Dalen. I feel like I’m becoming a burden."
    da "That’s nonsense."
    da "You’re the closest thing I have to family, helping you isn’t a chore, Eliza. It’s a privilege."
    scene ch4sc19_081 with dissolve
    da "Besides, do you see any other humans around here?"
    scene ch4sc19_083 with dissolve
    el "*Sigh* Fair point."
    el "So how do we do this?"
    scene ch4sc19_084 with dissolve
    da "Like this."
    el "Dalen!"
    scene ch4sc19_085 with dissolve
    with vpunch
    da "*Grunts* Hrngh..."
    scene ch4sc19_086 with dissolve
    el "Dalen! Stop! That’s enough already!"
    da "We're not taking any chances."
    "Dalen keeps squeezing his hand until the chalice is full."
    scene ch4sc19_087 with dissolve
    da "There you go..."
    scene ch4sc19_088 with dissolve
    $ renpy.pause()
    elt "..."
    elt "If I drink this... Everything changes."
    elt "I will change. Will [mc] still look at me the same?"
    elt "*Sigh* A vampire. A bloodsucking monster..."
    scene ch4sc19_089 with dissolve
    elt "Speed... strength... reflexes... bloodthirst... predator..."
    elt "Hearing... sight... emotions... killing..."
    elt "I don’t think I’ve ever read a vampire book where the vampire wasn’t a killer."
    scene ch4sc19_088 with dissolve
    elt "Will I really be able to handle this?"
    scene ch4sc19_090 with dissolve
    elt "I have to. I’ve been a burden long enough!"
    elt "With this... I will be able to protect [mc]."
    scene ch4sc19_091 with dissolve
    mc "Eliza... We can sleep on it."
    mc "You don’t have to make the choice right now."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    el "..."
    play music feels_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_092 with dissolve
    el "*Mouthing* I. Love. You."
    scene ch4sc19_093 with dissolve
    $ renpy.pause(1)
    scene ch4sc19_094 with dissolve
    $ renpy.pause(1)
    scene ch4sc19_093 with dissolve
    $ renpy.pause(2)
    scene ch4sc19_095 with Dissolve(1.5)
    el "*Gulp* *Gulp*"
    scene ch4sc19_096 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    "She completely empties the cup without any hesitation."
    scene ch4sc19_097 with dissolve
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    el "*Groans* Urrh... I... I don’t feel so good..."
    "You notice her eyes starting to glaze over."
    scene ch4sc19_098 with dissolve
    with vpunch
    mc "Eliza!!"
    scene ch4sc19_099 with dissolve
    mc "I've got you..."
    da "She might remain unconscious while she undergoes her transition."
    scene ch4sc19_100 with dissolve
    mc "I’ll stay here with her and watch over her."
    scene ch4sc19_101 with dissolve
    da "Take her to your room at the Drunken Rooster."
    da "It’s probably best she has a bed. We don’t know how long this will take."
    scene ch4sc19_100 with dissolve
    mc "Alright. I’ll do that. Will you be fine here?"
    scene ch4sc19_101 with dissolve
    da "Yeah, I’ll just have to get some bandages for my hand, I guess I cut it a little deeper than I intended."
    da "Afterwards I’ll begin studying anything we have on vampirism. I haven’t dealt with vampires before-"
    da "The more we can learn, the better off she will be."
    scene ch4sc19_100 with dissolve
    mc "Sure, that's probably a good idea. Before I go-"
    mc "Let me see your hand."
    scene ch4sc19_102 with dissolve
    $ renpy.pause(1)
    da "What are you-"
    mc "I’ve grown in power since I left."
    mc "I managed to absorb magical essence from the rejuvenation crystals on Inmortui."
    mc "With a little bit of focus... I should be able to heal surface wounds."
    scene ch4sc19_103 with dissolve
    da "*Grunts* That’s... beyond anything I imagined you'd be capable of."
    "As you concentrate a cloud of rejuvenating mist forms around Dalen's hand."
    da "It's already healing? ... Thank you."
    scene ch4sc19_104 with dissolve
    mc "Don’t mention it... We’ll talk tomorrow."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc15_005 with Dissolve(2)
    play music dark_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc15_067 with dissolve
    $ renpy.pause()
    scene ch4sc15_068 with dissolve
    $ renpy.pause()
    scene ch4sc15_069 with dissolve
    ta "Status."
    scene ch4sc15_070 with dissolve
    lu "I haven’t been able to-"
    scene ch4sc15_069 with dissolve
    ta "Silence."
    ta "Useless girl. Your worth is diminishing by the hour."
    scene ch4sc15_071 with dissolve
    lu "..."
    ta "Do I really have to remind you again what will happen to mommy-dearest if you can’t deliver?"
    scene ch4sc15_072 with dissolve
    lu "Don’t touch her!"
    scene ch4sc15_069 with dissolve
    ta "I think it’s time for a family reunion!"
    scene ch4sc19_105 with dissolve
    with vpunch
    lu "Argh! Let go! You’re hurting me!"
    ta "Look! Look at your sad excuse of a mother!"
    lu "M-Mom!"
    scene ch4sc19_106 with dissolve
    lum "Leave her alone! Get your filthy hands off her!"
    scene ch4sc19_105 with dissolve
    ta "{b}LOOK AT HER, LUNA!{/b} Look at your poor mother! You know this is all your doing, right?"
    ta "She could be free, if only you would break that curse."
    ta "Every minute she spends in here is because of {b}your{/b} incompetence!"
    scene ch4sc19_106 with dissolve
    lum "Don’t listen to him, Luna!"
    lum "Don’t give him what he wants!"
    with vpunch
    ta "{b}SILENCE WITCH!!{/b}"
    scene ch4sc19_107 with dissolve
    ta "She will give me exactly what I want, 'cause that’s the only way she can help her pathetic mother."
    lu "Mommy! I’m sorry! I will do whatever it takes to get you out!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc19_108 with Dissolve(2)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    mct "Don't worry. This will work. It has to."
    mct "It feels good to be back. To be by your side again."
    mct "Something about you just... calms me."
    scene ch4sc19_109 with dissolve
    mct "At first, I just expected to find her and watch over her. Like Oren asked me to."
    mct "Make sure she didn't get into trouble... that she had a decent life."
    mct "But almost immediately upon meeting her... I knew."
    mct "She is so genuine... kind... caring... fierce... loyal... passionate."
    mct "Eliza... He will pay for this. For everything he has put you through."
    scene ch4sc19_110 with dissolve
    mct "I guess she'll be out for a while... I'd better get some rest as well."
    mct "I have a feeling this transition will be rough on her."
    mct "Her compassion for others will work against her when she has to feed..."
    scene ch4sc19_111 with dissolve
    mct "I love you... Goodnight."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc19_112 with dissolve
    "It doesn’t take long for sleep to claim you as you’re finally back in your own bed after two moons..."
    scene black with Dissolve(2)
    play music feels_3 fadein 1.0
    #stop music fadeout 1.0
    #$ renpy.pause(2)
    scene ch4sc19_113 with Dissolve(2)
    $ renpy.pause(1)
    #####ANIMATION#####
    show el_sleep1 with fade
    $ renpy.pause(4, hard=True)
    $ renpy.pause()
    scene black with Dissolve(2)
    scene ch4sc19_115 with Dissolve(2)
    el "*Groans* Hnngh..."
    scene ch4sc19_116 with dissolve
    el "..."
    scene ch4sc19_117 with dissolve
    el "Did it work? Am I a vampire now? ..."
    el "I’ve got fangs... I’m... So... Thirsty..."
    scene ch4sc19_118 with dissolve
    el "Huh? [mc] is here?"
    el "Oh, right! He came home! He finally came home to me..."
    scene ch4sc19_119 with dissolve
    el "He’s so cute when he’s sleeping... I’ve missed sharing a bed with him..."
    el "But he’s sleeping so far away ... Is he scared I’ll break or something?"
    scene ch4sc19_120 with dissolve
    el "I want to be closer..."
    el "His neck looks so... Enticing..."
    scene ch4sc19_121 with dissolve
    el "*Soft whisper* {size=-10}{b}I’ve missed you... I’ve missed you so much that it hurts.{/b}{/size}"
    el "*Soft whisper* {size=-10}{b}Your blue eyes... Your strong hands... Your warm body... Your fuzzy hair... Your beautiful neck...{/b}{/size}"
    scene ch4sc19_122 with dissolve
    el "*Soft whisper* {size=-10}{b}Warm... Delicious neck, I really want to kiss it...{/b}{/size}"
    el "*Soft whisper* {size=-10}{b}Yeah... Just a little kiss.{/b}{/size}"
    scene ch4sc19_123 with dissolve
    el "*Soft whisper* {size=-10}{b}Nnnghh... He smells so good!{/b}{/size}"
    scene ch4sc19_124 with dissolve
    el "*Kiss* MnnnHh... *Kiss* Nnngh... *Kiss* MhHhmm..."
    el "I want to taste him so badly! I... I need to!"
    scene ch4sc19_125 with dissolve
    $ renpy.pause()
    scene ch4sc19_126 with dissolve
    $ renpy.pause()
    "Just as her soft bottom lip touches your neck and her fangs are about to pierce your skin she suddenly stops."
    scene ch4sc19_127 with dissolve
    with vpunch
    el "{b}NO!!{/b}"
    scene ch4sc19_128 with dissolve
    elt "*Groans* Hnngh! What am I doing?! I almost bit [mc]!"
    elt "*Groans* Argh! My head hurts! It’s like a hangover times ten!"
    scene ch4sc19_129 with dissolve
    with vpunch
    elt "*Groans* I-I have to get out of here!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch4sc19_130 with Dissolve(1.5)
    $ renpy.pause()
    play music dark_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_131 with dissolve
    $ renpy.pause()
    scene ch4sc19_132 with dissolve
    $ renpy.pause()
    scene ch4sc19_133 with dissolve
    $ renpy.pause()
    scene ch4sc19_134 with dissolve
    elt "Seems like my legs are back to normal... No, better than normal."
    elt "I feel light as a feather!"
    scene ch4sc19_135 with dissolve
    uk "Excuse me, miss? Are you alright? I saw you jump from the stairs..."
    el "..."
    scene ch4sc19_136 with dissolve
    el "No... I’m not alright, I’m so thirsty..."
    el "So... unbelievably thirsty..."
    el "You wouldn’t happen to have something to drink?"
    scene ch4sc19_137 with dissolve
    uk "Afraid not miss, I work in the tavern behind you, I could ask if they have some water for you-"
    scene ch4sc19_138 with dissolve
    with vpunch
    uk "Arrrgh! What are you doing!? Release me!"
    el "Liar... You have something to drink right here!"
    scene ch4sc19_139 with dissolve
    el "Something really delicious..."
    uk "Let me go! You’re scaring me!"
    el "I just need a little bite... Just... A sip..."
    scene ch4sc19_140 with dissolve
    $ renpy.pause()
    scene ch4sc19_141 with dissolve
    with vpunch
    uk "Argh!!"
    elt "Mnnnghh... *Suck* She’s... Delicious! *Sucks harder*"
    "With each drop of blood Eliza consumes, her intentions of a small taste diminishes..."
    scene ch4sc19_142 with dissolve
    elt "Mmnngh! *Suck* Just give me a little more! *Sucks harder* More!"
    #### Choice ####
    menu:
        "Eliza holds back.":
            "As Eliza is about to lose herself to the overwhelming need to feed she comes suddenly stops."
            scene ch4sc19_143 with dissolve
            el "AaHh! That'll do..."
            scene ch4sc19_144 with dissolve
            el "Thank you! I really needed that!"
            el "Don't worry I'll be sure to leave a nice tip next time I stop by the tavern."
            #play music dark_3 fadein 1.0
            stop music fadeout 1.0
            scene ch4sc19_145 with dissolve
            elt "Huh? No... No! N-No, no, no, NO!"
            play music feels_3 fadein 1.0
            #stop music fadeout 1.0
            scene ch4sc19_146 with dissolve
            $ renpy.pause()
            scene ch4sc19_147 with dissolve
            elt "She’s... Dead? {b}NO!{/b}"
            elt "Please wake up! I-I just had a little bit?! No-... I... I had a lot?!"
            elt "But... I-I stopped?"
            scene ch4sc19_148 with dissolve
            el "*Shaky voice* I... I killed someone?!"
            el "*Shaky voice* {b}NO!{/b} No! no, no, no, no! I can’t have killed someone... I-I didn’t mean to!"
            scene ch4sc19_149 with dissolve
            el "*Shaky voice* I... I just bit her? And now she's dead?"
            el "*Shaky voice* I’m so sorry! What have I done?!"
            el "*Shaky voice* Huh? Wh-What's that sound?"
            scene ch4sc19_150 with dissolve
            mc "That's the sound of her heart beating."
            scene ch4sc19_151 with dissolve
            elt "Huh?? She-she's alive?!"
            elt "I-I was just so thirsty... And now she’s hurt? A woman is hurt because of me!!"
            scene ch4sc19_151 with dissolve
            $ renpy.pause()
            scene ch4sc19_152 with dissolve
            el "*Shaky voice* [mc]... I did this... I hurt her!"
            el "*Shaky voice* S-She wanted to help me! And I took adventage!"
            scene ch4sc19_151 with dissolve
            mc "Listen. This could have been a hell of a lot worse. But you somehow stopped yourself."
            mc "I should've been awake, to help you with this."
            scene ch4sc19_152 with dissolve
            el "B-But what are we going to do? We can't just leave her here?"
            scene ch4sc19_151 with dissolve
            mct "I have to get her out of here."
            mct "It doesn't look good if someone were to see us like this."
            mc "Come."
            scene ch4sc19_152 with dissolve
            el "W-What? We can’t just leave her?"
            scene ch4sc19_151 with dissolve
            mc "That’s exactly what we’re going to do. We need to get out of here before someone sees you."
            mc "She'll be alright, her pulse is steady and she'll probably wake up with one giant headache."
            mc "But there's nothing more for us to do, right now at least."
            mc "Come with me."
            scene ch4sc19_153 with dissolve
            el "W-wait up!"
            el "[mc]!"
            #play music dark_3 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(2)
            $ renpy.pause(1)
            scene ch4sc19_154 with Dissolve(1.5)
            play music forest_1 fadein 1.0
            #stop music fadeout 1.0
            el "H-How are you walking this calmly?! We’re up so high!"
            mc "When you’re not afraid of falling, remaining calm isn’t much of an issue."
            el "You’re not afraid?"
            mc "No. And neither should you be... You’re a vampire now. You know immortality is part of the package?"
            scene black with dissolve
            scene ch4sc19_155 with dissolve
            el "*Sigh* I didn’t even think of that... Vampire, huh?"
            scene ch4sc19_156 with dissolve
            el "I... Hurt that woman. I... I attacked her for her blood."
            el "I’m... I’m a monster, [mc]."
            scene ch4sc19_157 with dissolve
            el "Please don’t look at me like that..."
            scene ch4sc19_158 with dissolve
            mc "How am I looking at you?"
            scene ch4sc19_157 with dissolve
            el "Like it’s okay... Like you’re about to tell me it wasn’t my fault."
            el "It was my fault! I sucked her blood and... I enjoyed it!"
            scene ch4sc19_159 with dissolve
            el "I’m... I’m a monster! A hideous, blood-sucking monster!"
            el "Don’t look at me!"
            mc "Come here..."
            el "N-No!"
            "You grab her and despite her reluctance, she doesn’t put up a fight as you place her in your arms."
            scene ch4sc19_160 with dissolve
            el "You can’t do this... You can’t reward me for hurting an innocent."

        "Eliza gives in to the blood. ({color=#fc584c}Eliza Dark{/color})":
            "Only when there is no more blood flowing through the barmaid's veins does she stop."
            scene ch4sc19_143 with dissolve
            el "AaHh! Incredible!"
            $ eldark += 1
            "Having fully fed, taken the life of an innocent, Eliza has taken a step into darkness, {color=#f00}Dark Morality{/color} increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch4sc19_144 with dissolve
            el "Thank you! I really needed that!"
            el "Don't worry I'll be sure to leave a nice tip next time I stop by the tavern."
            #play music dark_3 fadein 1.0
            stop music fadeout 1.0
            scene ch4sc19_145 with dissolve
            "After a few moments of reveling in the bloodlust, Eliza realises what she has done."
            elt "Huh? No... No! N-No, no, no, NO!"
            play music feels_3 fadein 1.0
            #stop music fadeout 1.0
            scene ch4sc19_146 with dissolve
            $ renpy.pause()
            scene ch4sc19_147 with dissolve
            elt "She’s... Dead? NO!"
            elt "Please wake up! I-I just had a little bit?! No-... I... I had a lot?!"
            scene ch4sc19_148 with dissolve
            el "*Shaky voice* I... I killed someone?!"
            el "*Shaky voice* NO! No! no, no, no, no! I can’t have killed someone... I-I didn’t mean to!"
            scene ch4sc19_149 with dissolve
            el "*Shaky voice* I... I just bit her? And now she's dead..."
            el "*Shaky voice* I’m so sorry! What have I done?!"
            scene ch4sc19_150 with dissolve
            elt "I’ve killed someone! I’ve killed an innocent person!"
            elt "I-I was just so thirsty... And now she’s dead. A woman is dead because of me!!"
            scene ch4sc19_151 with dissolve
            $ renpy.pause()
            scene ch4sc19_152 with dissolve
            el "*Shaky voice* [mc]... I did this... I killed her!"
            el "*Shaky voice* S-She wanted to help me! And I took her life!"
            scene ch4sc19_151 with dissolve
            mct "I have to get her out of here."
            mc "Come."
            scene ch4sc19_152 with dissolve
            el "W-What? We can’t just leave her?"
            scene ch4sc19_151 with dissolve
            mc "That’s exactly what we’re going to do. We need to get out of here before someone sees you."
            mc "Come with me."
            scene ch4sc19_153 with dissolve
            el "W-wait up!"
            el "[mc]!"
            #play music dark_3 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(2)
            $ renpy.pause(1)
            scene ch4sc19_154 with Dissolve(1.5)
            play music forest_1 fadein 1.0
            #stop music fadeout 1.0
            el "H-How are you walking this calmly?! We’re up so high!"
            mc "When you’re not afraid of falling, remaining calm isn’t much of an issue."
            el "You’re not afraid?"
            mc "No. And neither should you be... You’re a vampire now. You know immortality is part of the package?"
            scene black with Dissolve(1.5)
            scene ch4sc19_155 with Dissolve(1.5)
            el "*Sigh* I didn’t even think of that... Vampire, huh?"
            scene ch4sc19_156 with dissolve
            el "I... Killed that woman."
            el "I’m... I’m a murderer [mc]."
            scene ch4sc19_157 with dissolve
            el "Please don’t look at me like that..."
            scene ch4sc19_158 with dissolve
            mc "How am I looking at you?"
            scene ch4sc19_157 with dissolve
            el "Like it’s okay... Like you’re about to tell me it wasn’t my fault."
            el "It was my fault! I drained every last bit of her blood and... I enjoyed it!"
            scene ch4sc19_159 with dissolve
            el "I’m... I’m a monster! A hideous, blood-sucking monster!"
            el "Don’t look at me!"
            mc "Come here..."
            el "N-No!"
            "You grab her and despite her reluctance, she doesn’t put up a fight as you place her in your arms."
            scene ch4sc19_160 with dissolve
            el "You can’t do this..."
            el "You can’t reward me for killing an innocent."



    scene ch4sc19_161 with dissolve
    mc "Eliza... I’m not rewarding you."
    mc "I’m comforting you..."
    scene ch4sc19_162 with dissolve
    el "But... I don’t deserve comfort."
    scene ch4sc19_161 with dissolve
    mc "Sure you do. I don’t know anyone who is more deserving of comfort than you."
    mc "The things you’ve had to endure over the last two moons..."
    mc "Being crippled... Being left behind... Managing to climb out of your own despair."
    scene ch4sc19_162 with dissolve
    el "[mc]..."
    scene ch4sc19_161 with dissolve
    mc "Having to accept vampirism to walk again... Cut yourself some slack, okay?"
    mc "You lost control for a moment and..."
    if eldark >= 1:
        mc "You killed someone, I'll be honest with you."
        mc "I expected this might happen, as you said yourself, no stories mentions a vampire that hasn't killed."
        mc "You will most likely kill again, this is a part of who you are now."
        scene ch4sc19_162 with dissolve
        el "But... I feel terrible... I couldn't control it, it felt... so good."
        scene ch4sc19_161 with dissolve
        mc "You'll learn to control your feedings, but you also don't have to feel bad about your instincts."
        mc "A lion does not feel pity for the zebra, nor does a cat for a mouse."

    else:
        mc "You attacked her in desperation, but you didn’t intend for that."
        scene ch4sc19_162 with dissolve
        el "Still, I don't want to lose control like that..."
        el "I can't be a vampire if I end up killng a bunch a people, at least not innocent people."


    mc "You won’t learn how to be a vampire overnight..."
    scene ch4sc19_162 with dissolve
    el "I suppose..."
    el "It still hurts me so much that I did that..."
    scene ch4sc19_161 with dissolve
    mc "You’ve always cared a great deal about others. Vampirism has magnified your emotions, remember?"
    mc "You feel everything more intensely now, which is why it’s all the more important you remind yourself who you are."
    scene ch4sc19_162 with dissolve
    el "[mc]... I’m scared..."
    scene ch4sc19_161 with dissolve
    mc "We’ll get you through this. I’ll personally see to it."
    mc "Starting at first light tomorrow, we’ll begin practicing your new abilities. How does that sound?"
    scene ch4sc19_162 with dissolve
    el "I... I’d like that."
    scene ch4sc19_163 with dissolve
    el "Just the two of us?"
    scene ch4sc19_164 with dissolve
    mc "You bet."
    mc "I’m not letting you out of my sight."
    scene ch4sc19_163 with dissolve
    el "Careful what you say-... Now you will have to spend the entire day with me tomorrow!"
    scene ch4sc19_164 with dissolve
    mc "I’ve missed you."
    scene ch4sc19_163 with dissolve
    el "I’ve missed you too!"
    scene ch4sc19_165 with dissolve
    $ renpy.pause()
    el "..."
    mct "Her heartbeat has relaxed."
    scene ch4sc19_166 with dissolve
    el "This is nice... Thank you."
    scene ch4sc19_165 with dissolve
    mc "You’ve calmed me down plenty of times, returning the favor is the least I can do."
    scene ch4sc19_166 with dissolve
    el "Oh, so you’re just returning the favor?"
    scene ch4sc19_165 with dissolve
    mc "No. Not just."
    scene ch4sc19_166 with dissolve
    el "Good!"
    scene ch4sc19_167 with dissolve
    el "I didn’t like it when I woke up and you slept on the other side of the bed..."
    scene ch4sc19_165 with dissolve
    mc "I didn’t want to disturb you. I wasn’t sure how the transition works..."
    scene ch4sc19_167 with dissolve
    el "We’ve had enough distance between us... I don’t like it."
    el "Not one bit."
    scene ch4sc19_168 with dissolve
    mc "I agree. I didn’t like it either."
    scene ch4sc19_167 with dissolve
    el "Promise you won’t leave again?"
    scene ch4sc19_165 with dissolve
    mc "I promise."
    scene ch4sc19_166 with dissolve
    el "*Giggles* Otherwise I’m going to kick your butt! I might even be able to do it now!"
    scene ch4sc19_164 with dissolve
    mc "*Chuckles* We’ll see. I’ve never met a vampire before, so I’m not really sure how strong you will be."
    mc "But from what Lucid told me, you're going to be powerful."
    scene ch4sc19_168 with dissolve
    mc "As a pureblood, directly from her bloodline you will be stronger than the average vampire."
    mc "Although if a normal vampire has a significant age advantage over you, they might be stronger."
    scene ch4sc19_167 with dissolve
    el "I think something like this was mentioned in mother’s books... Vampires gain strength as they age."
    scene ch4sc19_168 with dissolve
    mc "That’s one of the ways yeah."
    scene ch4sc19_167 with dissolve
    el "So... I basically have to become an old lady to be strong... *Sigh*"
    scene ch4sc19_165 with dissolve
    mc "*Chuckles* At least you won’t age physically. It must be nice knowing you’ll remain beautiful."
    scene ch4sc19_166 with dissolve
    el "Oh? I bet you think that’s quite the perk! Don’t you?"
    scene ch4sc19_164 with dissolve
    mc "I can’t deny that."
    mc "The thought of you living forever does appeal to me."
    scene ch4sc19_167 with dissolve
    el "[mc], Do you still look at me the same?"
    scene ch4sc19_168 with dissolve
    mc "Yes. Nothing has changed for me."
    mc "Did you abandon me when you learned who or what I was?"
    scene ch4sc19_167 with dissolve
    el "No... I would never."
    scene ch4sc19_168 with dissolve
    mc "Exactly, when you care about someone and you love them, you stick by them."
    mc "I firmly believe that, hell you're the one who made me come to hold that belief."
    scene ch4sc19_166 with dissolve
    el "You really mean that?"
    scene ch4sc19_164 with dissolve
    "You nod."
    ####Choice####
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc19_164 with dissolve
            mc "Come here, Kitten."
            $ eliza_path = True
            scene ch4sc19_169 with dissolve
            $ renpy.pause()
            scene ch4sc19_170 with dissolve
            $ renpy.pause()
            el "Mmnh-Hmh..."
            scene ch4sc19_171 with dissolve
            $ renpy.pause()
            el "Anhn-Nngh..."
            scene ch4sc19_172 with dissolve
            $ renpy.pause()
            mct "I love how delicately she moves her tongue, licking mine and inviting me into her mouth."
            elt "Mmmmm..."
            elt "He tastes so good..."
            "She licks your tongue gently while keeping your mouths closely together."
            "As your tongues play she moans softly between your kisses."
            scene ch4sc19_171 with dissolve
            el "*Moans* Mmnnh-MMnnnH! MmmmmMmm..."
            $ renpy.pause(1)
            scene ch4sc19_170 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_171 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_172 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_171 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_170 with dissolve
            el "*Mwah* Mmnnhh... Just what I needed. *Mwah* My lion."
            mc "My beautiful kitten."
            $ eliza_trust += 2
            "Eliza's trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch4sc19_166 with dissolve
            el "You know... I almost bit you when I woke up earlier..."
            scene ch4sc19_165 with dissolve
            mc "Oh? What stopped you?"
            scene ch4sc19_167 with dissolve
            el "I thought it might hurt you... That seemed to snap me out of it."
            scene ch4sc19_168 with dissolve
            mc "It wouldn’t hurt me."
            mc "It might sting a little but I acquired a new ability on Inmortui. I was able to absorb the essence of rejuvenation crystals."
            mc "It boosted my healing abilities quite a bit."
            scene ch4sc19_166 with dissolve
            el "Oh? So I can bite you?!"
            scene ch4sc19_165 with dissolve
            mc "Not so fast..."
            mc "We can try it tomorrow, if you’re up for it."
            scene ch4sc19_166 with dissolve
            with vpunch
            el "{b}REALLY!!?{/b}"
            el "Yes! Yes, yes, {b}YES!!{/b}"
            scene ch4sc19_167 with dissolve
            el "I mean... Sure, okay... If you want to."
            scene ch4sc19_169 with dissolve
            mc "Come here, you little kitten!"
            scene ch4sc19_170 with dissolve
            el "*Mwwaah!*"
            el "Take me to bed?"
            scene ch4sc19_169 with dissolve
            mc "Mhm-Hm, let's go."
            scene black with Dissolve(2)
            $ renpy.pause(1)


        "Don’t kiss her. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc19_164 with dissolve
            mc "We've been up here a while, I think it’s time we get back to bed."
            mc "If we’re going to be figuring out more about your vampirism tomorrow, we better be well rested."
            scene ch4sc19_166 with dissolve
            el "Yeah, I'm ready for bed! Thank you for this..."
            scene black with Dissolve(2)
            $ renpy.pause(1)

    scene ch4sc19_173 with dissolve
    $ renpy.pause()
    scene ch4sc19_174 with dissolve
    $ renpy.pause(1)
    el "How much longer? We’ve been walking for an hour..."
    scene ch4sc19_175 with dissolve
    mc "Are you trying to convince me that your legs can’t handle a little walk?"
    el "Don’t get me wrong! I love that I’m able to walk again! But-..."
    el "They are still a little weak from months of being idle..."
    scene ch4sc19_176 with dissolve
    mc "Uh-huh... Your powerful vampire legs feel weak?"
    mc "You wouldn’t happen to be fishing for a pity lift?"
    scene ch4sc19_177 with dissolve
    el "I-I would never!"
    el "I mean... Now that you mentioned it... A lift would be nice!"
    scene ch4sc19_178 with dissolve
    mc "*Sigh* Get on... You little schemer."
    scene ch4sc19_178 with dissolve
    elt "Heh-heh-heh!"
    scene ch4sc19_179 with Dissolve(1.5)
    mc "Happy?"
    el "Mh-hm!"
    mc "We should be there soon, Borri said it was just past the forest clearing."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch4sc19_180 with Dissolve(1)
    $ renpy.pause()
    scene ch4sc19_181 with dissolve
    mc "Here we are."
    el "What is this place? It looks... Barren."
    mc "It’s the Timah highlands. A vast area that stretches as far as the eastern sen’ju forests."
    mc "Borri recommended it to me a while back, if I needed a place to train my abilities without being seen."
    el "Ah that makes sense! So this will be our training ground?"
    mc "Yeah, we don’t know what you are capable of yet, we don’t want to give people a show... Do we?"
    el "Definitely not! I prefer it when it's just the two of us..."
    scene ch4sc19_182 with dissolve
    mc "See that structure over there? That will be our spot for combat training today."
    el "Uh! That looks cool! And... Ancient?"
    el "I wonder who made it?"
    mc "Could have been people that lived in the area once upon a time or it could be some kind of religious structure."
    scene ch4sc19_181 with dissolve
    el "OH! Like a sacrificial altar?"
    mc "*Chuckles* Not what I was thinking... C’mon let’s go."
    scene black with dissolve
    scene ch4sc19_183 with dissolve
    el "I knew it! It totally is a sacrificial altar!"
    mc "Have you ever seen a sacrificial altar?"
    el "No... But this is what I imagine one would look like!"
    scene ch4sc19_184 with dissolve
    mc "*Sigh*"
    mct "I almost forgot how perky her ass is..."
    mc "What are you doing?"
    scene ch4sc19_185 with dissolve
    el "Stretching! I don’t want to pull anything while I’m kicking your butt!"
    el "You should try it!"
    scene ch4sc19_186 with dissolve
    mc "Pass."
    el "*Stretching* Hnngh! Are you sure you don’t want to join me for a little stretching? It will be good for you."
    mct "She’s doing this on purpose..."
    scene ch4sc19_187 with dissolve
    $ renpy.pause()
    scene ch4sc19_188 with dissolve
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    el "*Whispers* Here I come!"
    scene ch4sc19_186 with dissolve
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch4sc19_189 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch4sc19_190 with dissolve
    with vpunch
    $ renpy.pause()
    mct "That was close... Her speed is far beyond what anyone human is capable of."
    mct "She even managed to block my grapple attempt... Impressive."
    mct "It’s good to see her smile... Huh?!"
    scene ch4sc19_191 with dissolve
    $ renpy.pause()
    scene ch4sc19_192 with dissolve
    with vpunch
    $ renpy.pause()
    mc "*Grunts* Hhrh!"
    scene ch4sc19_193 with dissolve
    mct "Damn... I guess I should pay attention."
    mct "She’s strong... Stronger than I anticipated."
    scene ch4sc19_194 with dissolve
    mc "You’re right behind me, aren’t you...?"
    scene ch4sc19_195 with dissolve
    el "Right behind you."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    el "I want to taste you... I want... Your blood."
    scene ch4sc19_196 with dissolve
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    el "*Hissing*"
    scene ch4sc19_197 with dissolve
    with vpunch
    "Overcome with thirst, she leaps ontop of you."
    mc "Eliza! Knock it off!"
    mc "Snap out of it! Don’t let the hunger control you!"
    scene ch4sc19_198 with dissolve
    el "Just... Just a small taste!! *Hissing* HrraahH!!"
    scene ch4sc19_199 with dissolve
    with vpunch
    el "*Groans* ARrrhHnngh!"
    mc "{b}*Shouts*{/b} I said knock it off!"
    scene ch4sc19_200 with dissolve
    el "*Hissing* HssshH!"
    mct "I’m going to have to get serious. She’s lost control... Probably angry with herself for hurting that girl last night."
    mct "Now that anger is fueling her bloodlust... I need to snap her out of it and fast."
    scene ch4sc19_201 with dissolve
    with vpunch
    mct "Here she comes!"
    scene ch4sc19_202 with dissolve
    $ renpy.pause()
    scene ch4sc19_203 with dissolve
    mc "{b}*Shouts*{/b} Eliza... Stop!"
    scene ch4sc19_204 with dissolve
    with vpunch
    mct "She dodged!"
    scene ch4sc19_205 with dissolve
    $ renpy.pause()
    scene ch4sc19_206 with dissolve
    $ renpy.pause()
    scene ch4sc19_207 with dissolve
    with vpunch
    mc "{b}*Shouts* ENOUGH!!{/b}"
    scene ch4sc19_208 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    el "*Whimpers* S-Sorry!!"
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    mct "That seems to have done it..."
    mct "Huh, she’s shaking?"
    scene ch4sc19_209 with dissolve
    mc "Hey... Come here."
    el "*Shaky voice* N-No... I almost hurt you!"
    scene ch4sc19_210 with dissolve
    el "*Shaky voice* I wanted to bite you really badly! And-And I was just so angry!"
    el "*Shaky voice* And you smell really good! I just wanted to be close to you! And... Bite you!"
    mc "*Chuckles* Heh."
    scene ch4sc19_211 with dissolve
    el "Why are you laughing?! This isn’t funny!"
    scene ch4sc19_212 with dissolve
    mc "It’s a little funny ..."
    mc "Your emotions are heightened as a vampire, if you’re not careful they will take over and turn into bloodlust."
    mc "Even when you feel happy, it can make you want to bite someone and drink their blood. Sort of a survival mechanism."
    scene ch4sc19_211 with dissolve
    el "Well I think it’s stupid!! This could have ended really badly if you weren’t stronger than me."
    el "What if you aren’t around and I lose control? I might hurt someone or worse!"
    el "I can't live with that. I-I just can't!"
    scene ch4sc19_212 with dissolve
    mc "We won’t let it come to that."
    scene ch4sc19_213 with dissolve
    mc "We’ll practice your self control until you’re able to win a trophy for self-moderation."
    el "..."
    scene ch4sc19_214 with dissolve
    el "Trophy for self-moderation? You’re such a dummy..."
    scene ch4sc19_215 with dissolve
    with vpunch
    el "Big dummy!"
    el "..."
    el "Sorry for trying to bite you..."
    mc "Sorry for scaring you."
    with vpunch
    el "Mmpfh!! *Hugs tightly* I didn’t like it!"
    scene ch4sc19_216 with dissolve
    el "But this hug is making up for it!"
    el "I’ve decided I’ll forgive you for scaring me... If... You squeeze me!"
    scene ch4sc19_215 with dissolve
    mc "I have to squeeze you?"
    with vpunch
    el "Yes! Firmly!"
    el "*Whimpers* NNngh!"
    scene ch4sc19_216 with dissolve
    el "Thank you..."
    scene ch4sc19_217 with dissolve
    el "*Sigh* We should probably head back... I have desk duty at the guild."
    scene ch4sc19_215 with dissolve
    mc "Sure, I have to talk with Dalen anyway. He stayed up last night combing through anything related to vampirism."
    el "Think he found something?"
    mc "Being the leader of a guild, adventuring guild no less, I’m sure he has a lot of books about this stuff."
    mc "Or maybe Sylph knows something? She didn't seem thrilled to see me last night."
    scene ch4sc19_217 with dissolve
    el "Y-Yeah... I told her about you... Being a Nephilim. She wasn’t too excited about that."
    scene ch4sc19_215 with dissolve
    mc "Oh? I guess I’ll give her some space and let her come to me when she’s ready."
    scene ch4sc19_217 with dissolve
    el "That’s probably for the best, I don’t think she dislikes you or anything, it just has something to do with her past."
    scene ch4sc19_215 with dissolve
    mc "Don’t worry, I’m sure she will come around... Let’s head back."
    el "Okay!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_218 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    evr "Eliza! You’re on your feet!"
    scene ch4sc19_219 with dissolve
    br "I can’t believe me eyes! Ye on yer feet lass! The artifact really worked?!"
    scene ch4sc19_220 with dissolve
    ml "Miss Eliza! It’s good to see you’re feeling better!"
    scene ch4sc19_221 with dissolve
    sy "..."
    mct "Looks like she isn’t too happy to see me still..."
    scene ch4sc19_222 with dissolve
    el "Hey everyone! Look who I found!"
    br "By Malpheon’s hammer! [mc]! Yer back? {b}HA! ALES TONIGHT!{/b}"
    scene ch4sc19_223 with dissolve
    mc "Hey Borri. Good to see you and thanks for keeping an eye on Eliza."
    br "Bah! Of course lad! She's like me own kin!"
    scene ch4sc19_224 with dissolve
    el "Milton! You’re here early, good! Let’s get you sorted with your first proper quest!"
    scene ch4sc19_220 with dissolve
    ml "Sure thing miss Eliza! I'm excited to get started!"
    scene ch4sc19_223 with dissolve
    mc "I’ve got to talk to Dalen, is he around?"
    scene ch4sc19_225 with dissolve
    sy "I-In his office..."
    scene ch4sc19_226 with dissolve
    mc "Sylph can we talk?"
    scene ch4sc19_225 with dissolve
    sy "N-Now isn’t really a good time, I’ve got a lot of papers to work through today..."
    scene ch4sc19_226 with dissolve
    mc "I know you’re upset with me... So just come to me whenever you’re ready, okay?"
    scene ch4sc19_225 with dissolve
    sy "O-Okay... Will do..."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch4sc19_227 with dissolve
    play music home_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Hey Dalen, found anything?"
    scene ch4sc19_228 with dissolve
    da "Oh, hey [mc]. Just bits and pieces of vampire lore but nothing too concrete yet..."
    da "At first I wanted to look for anything mentioning or referring to a cure... But that only lead to dead ends."
    scene ch4sc19_229 with dissolve
    mc "Yeah, I suspected as much, Lucid did emphasize that vampirism is permanent."
    da "Hmm."
    scene ch4sc19_228 with dissolve
    da "Vampire lore is hard to come by... They are experts at blending in and they are few and far between."
    da "I’ve never even heard of one during my years as an adventurer..."
    scene ch4sc19_229 with dissolve
    mc "Yeah me neither..."
    scene ch4sc19_228 with dissolve
    da "Until we get more information we have to be careful with how we deal with the situation."
    scene ch4sc19_230 with dissolve
    da "If people find out about her condition... Could cause a panic amongst citizens."
    da "They won’t hesitate to call for her execution."
    scene ch4sc19_231 with dissolve
    mc "That won’t be easy..."
    mc "She is struggling with her emotions and the hunger."
    scene ch4sc19_230 with dissolve
    da "That’s to be expected."
    da "Her whole existence has just been turned upside down..."
    scene ch4sc19_228 with dissolve
    da "This is her first day as a vampire..."
    da "I think it’s important for her to be surrounded by people she cares about."
    scene ch4sc19_230 with dissolve
    da "You. You need to remind her of all the good things life has to offer her."
    da "Otherwise we could risk losing her to the bloodlust."
    scene ch4sc19_229 with dissolve
    mc "That is not an option."
    mc "I don’t think she can go much longer without feeding..."
    mc "She fed last night, but already this morning she lost control as we were training."
    mc "If I hadn’t overpowered her, she would’ve fed on me."
    scene ch4sc19_228 with dissolve
    da "Hmh... As much as I hate to say it. She needs to feed... And the longer she goes without doing so..."
    da "It will probably get easier and easier for her to lose control. You somehow have to teach her how to feed."
    scene ch4sc19_230 with dissolve
    da "Without hurting someone in the process."
    da "Yes... I heard about the girl last night, a woman who was attacked in an alley, bite marks on her neck?"
    scene ch4sc19_231 with dissolve
    mc "She didn’t mean to-"
    scene ch4sc19_230 with dissolve
    da "I’ve taken care of it. I spoke to the guards that was on the case, told them it might be linked to the one who has been kidnapping girls."
    da "But if more people gets attacked, they will start to investigate."
    scene ch4sc19_231 with dissolve
    mc "But how do we practice feeding? I suppose I could let her feed on me? I can regenerate."
    scene ch4sc19_230 with dissolve
    da "I don’t think that’s an option... While that is a safe solution for now... The moment you aren’t with her-"
    da "And her hunger sets in? She would be likely to feed and kill someone..."
    scene ch4sc19_228 with dissolve
    da "She would only have known feeding from you in a controlled setting, feeding from a human? Out of desperation?"
    da "She wouldn’t know how to handle it."
    da "Besides... We don't know if your blood will do more harm than good."
    scene ch4sc19_229 with dissolve
    mc "Then what are you suggesting?"
    scene ch4sc19_230 with dissolve
    da "I think she needs to learn how to feed on humans and learn how to restrain herself."
    da "That is the only way we can guarantee that she will be able to control it when we aren’t around."
    scene ch4sc19_231 with dissolve
    mc "We can’t just go up to someone and have her feed on them..."
    scene ch4sc19_228 with dissolve
    da "Well, obviously not. I would suggest dark areas, preferably at night. Maybe pick someone who is drunk?"
    da "That way you can better explain it off or have them think they just imagined it..."
    scene ch4sc19_229 with dissolve
    mc "*Sigh* Okay. I’ll take her out tonight and attempt it."
    mc "There is something else I wanted to talk to you about."
    scene ch4sc19_228 with dissolve
    da "Oh? What is it?"
    scene ch4sc19_232 with dissolve
    mc "This..."
    "You toss the ring you acquired from Blackheart on the table."
    mc "It’s an enchanted ring, just like the one Borri had."
    da "Highly curious..."
    mc "I acquired it from Blackheart when I defeated him in Looter’s Bay."
    da "I don’t imagine he just handed it to you?"
    scene ch4sc19_233 with dissolve
    mc "Not quite... I was hoping you and Sylph could investigate it."
    scene ch4sc19_228 with dissolve
    da "I’ll put Sylph on it. She's good with magical artifacts."
    scene ch4sc19_229 with dissolve
    mc "I have a theory that the rings are connected and that they aren’t the only ones out there..."
    scene ch4sc19_228 with dissolve
    da "Connected? Why is that?"
    scene ch4sc19_233 with dissolve
    mc "As I said, it has the same potency of magic that I felt with Borri’s ring... And..."
    mc "When I faced Taron... I felt the same type of magic. I didn’t think much of it at the time as I was focused on Eliza."
    mc "But there is no doubt about it. I definitely felt it."
    scene ch4sc19_228 with dissolve
    da "Do you think he has one of these rings as well?"
    scene ch4sc19_229 with dissolve
    mc "I do... I want to go back to the cells and see if I can find anything."
    scene ch4sc19_233 with dissolve
    mc "Can you keep an eye on Eliza while I’m gone?"
    scene ch4sc19_230 with dissolve
    da "Sure, we’ll keep her busy with desk work."
    scene ch4sc19_231 with dissolve
    mc "Thank you, I’ll try to be quick ..."
    scene ch4sc19_233 with dissolve
    mc "Oh and whatever you do, don’t wear the ring."
    mc "It has some sort of corruption effect on whoever wields it."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_234 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    el "You’re back! How did it go?"
    mc "He wasn’t able to find much yet, but he will continue looking into it."
    scene ch4sc19_235 with dissolve
    mc "How do you feel about me taking you out tonight?"
    scene ch4sc19_236 with dissolve
    el "*Excited* Take me out? Like a date?!"
    scene ch4sc19_237 with dissolve
    mc "Not a date. Dalen and I both think you should learn how to feed properly, to avoid future repeats of last night."

    if eliza_relationship == True:
        scene ch4sc19_237 with dissolve
        elt "Oh... I was really hoping we could finally go on our date..."
        elt "Just some alone time the two of us... Having fun and making out!"
        elt "Lot's of making out, definitely!"
        elt "But he’s right. I need to learn how to control this... Hunger. The sooner the better."

    else:
        scene ch4sc19_237 with dissolve
        elt "Oh... I was really hoping we could finally go out."
        elt "I know it's just a friendly date but I've really been looking forward to it."
        elt "Just have some fun together, now that [mc] is finally back."

    scene ch4sc19_238 with dissolve
    el "Okay! We’ll practice feeding tonight!"
    el "Prepare to be amazed! After tonight I’ll put other vampires to shame!"
    scene ch4sc19_239 with dissolve
    mc "*Chuckles* You don’t lack enthusiasm, I’ll give you that."
    mc "I know I said I wouldn’t take my eyes off you today... But I need to head out for a while, will you be okay?"
    scene ch4sc19_240 with dissolve
    el "No problem, I’ll be busy with assigning new contracts today. Just pick me up later?"
    mc "Will do. Oh, and try not to eat anyone while I’m out..."
    el "No promises! So you better hurry back..."

    if eliza_relationship == True:
        scene ch4sc19_236 with dissolve
        el "Aren’t you forgetting something?"
        scene ch4sc19_241 with dissolve
        "Eliza puckers her lips waiting for you."
        mct "Heh... Such a cutie."
        el "Mhmh..."
        scene ch4sc19_242 with dissolve
        elt "*Kiss* MmmMmm..."
        scene ch4sc19_243 with dissolve
        mc "Bye..."
        scene ch4sc19_242 with dissolve
        elt "*Mwah* I love kissing him..."
        scene ch4sc19_243 with dissolve
        mc "Eliza..."
        scene ch4sc19_242 with dissolve
        elt "*Kiss* NNngh... As soon as we get this dumb hunger under control..."
        elt "I’m going to make out with him all day!"
        scene ch4sc19_243 with dissolve
        el "Bye bye... My Lion."
        mc "Bye my little kitten."
        scene black with Dissolve(2)

    else:
        scene ch4sc19_240 with dissolve
        el "Bye! See you later!"
        mc "Count on it, see you."
        scene black with Dissolve(2)

    scene black with Dissolve(1)
    $ renpy.pause(1)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc15_005 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc19_244 with dissolve
    mct "..."
    mct "That was easy... Only two guards? Taron is getting lax."
    mct "Being back here feels... Odd."
    mct "But there's a chance I could learn something..."
    scene ch4sc19_245 with dissolve
    mct "I don’t detect any traces of magic like the rings... However, I do sense something up ahead."
    mct "It's definitely a potent magic but somewhat subdued?"
    scene ch4sc19_246 with dissolve
    with vpunch
    uk "*Coughing*"
    scene ch4sc19_247 with dissolve
    mct "Huh? Somebody is in this cell..."
    scene ch4sc19_248 with dissolve
    uk "*Coughs* Great... Another of Taron’s goons here to gloat?"
    mct "She wasn’t here last time... He has been keeping busy..."
    scene ch4sc19_249 with dissolve
    mc "Who are you? How do you know Taron?"
    scene ch4sc19_248 with dissolve
    uk "You're not one of Taron's lackeys?"
    mc "No."
    cas "Cassandra. Head of the mage’s guild here in Luxenford."
    cas "You?"
    ####Choice####
    menu:
        "Reveal who you are.":
            scene ch4sc19_249 with dissolve
            mc "[mc], of Riverside, Member of the Adventurers guild."
            $ cas_trust += 2
            "Cassandra appreciates you being upfront with her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Not important.":
            scene ch4sc19_249 with dissolve
            mc "Who I am doesn’t matter."
            mc "All you have to know is that I’m no friend of Taron."

    scene ch4sc19_250 with dissolve
    cas "Good, then you’re an ally."
    scene ch4sc19_249 with dissolve
    mc "Hold on, I’ll get you out."
    scene ch4sc19_251 with dissolve
    with vpunch
    cas "No! Don’t touch it!"
    cas "I can’t leave this cell... Taron had one of his mages put a hex on me!"
    cas "If I leave it will activate and my own magic will tear me apart from the inside... Besides..."
    scene ch4sc19_253 with dissolve
    mc "Leave it to Taron to be a sadistic fuck... Anything else I should know?"
    scene ch4sc19_252 with dissolve
    cas "He has my daughter... Luna."
    cas "I can’t risk him hurting her..."
    scene ch4sc19_253 with dissolve
    mc "Luna, hmh... Okay, so I can’t break you out? What does he want with you?"
    mc "He’s surely not just doing this on a whim."
    scene ch4sc19_252 with dissolve
    cas "He has been pestering me for months to lift a curse from an ancient relic he acquired..."
    cas "I kept refusing... That curse is dark magic... Ancient magic."
    cas "And it’s obvious he is not a person who should have access to such power."
    scene ch4sc19_253 with dissolve
    mc "On that we agree. What is this curse?"
    scene ch4sc19_254 with dissolve
    cas "Even I don't know, I didn't study it for long before I declined his request."
    scene ch4sc19_253 with dissolve
    mc "Damn, would've been good to know what I'm up against."
    mc "You said he has your daughter?"
    scene ch4sc19_252 with dissolve
    cas "Yes. Luna... He is using me as a hostage to make her lift the curse."
    scene ch4sc19_254 with dissolve
    cas "She’s not strong enough... Not yet. But that doesn’t stop him from pressuring her!"
    scene ch4sc19_252 with dissolve
    with vpunch
    cas "She’s just a girl! She only turned 18 this summer! She shouldn’t be doing dark magic!"
    scene ch4sc19_253 with dissolve
    mc "You’re right. She shouldn’t... How do I find her?"
    scene ch4sc19_254 with dissolve
    cas "You’ll help her?"
    scene ch4sc19_253 with dissolve
    mc "Taron should never get what he wants. He’s a psychopath."
    mc "He's hurt my loved ones on several occassions... So Yes, I will help your daughter."
    scene ch4sc19_254 with dissolve
    cas "Thank you! I can’t begin to express how much of a relief this is..."
    scene ch4sc19_252 with dissolve
    cas "I was starting to fear I’d have to give in and do what he wants."
    scene ch4sc19_253 with dissolve
    mc "How do I find her?"
    scene ch4sc19_254 with dissolve
    cas "She attends the Academy of learning and also works at the mages guild."
    mct "Academy of learning, that's where Alice studies alchemy and herbology."
    cas "She has blonde-silverish hair, dresses in black and wears my big goofy witches hat."
    scene ch4sc19_253 with dissolve
    mc "Got it. And her name is Luna?"
    scene ch4sc19_254 with dissolve
    cas "Yes. Please find her and help her!"
    scene ch4sc19_253 with dissolve
    mc "I have a friend who studies at the Academy, maybe she knows your daughter."
    mc "Cassandra, I won’t let Taron get his hands on whatever this relic is."
    scene ch4sc19_254 with dissolve
    cas "Help her and I will owe you a debt of gratitude I won't soon forget."
    scene ch4sc19_253 with dissolve
    mc "I'll do what I can, meanwhile stay strong."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc19_255 with dissolve
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc19_256 with dissolve
    al "*Sigh* I wonder if I’ll have that some day ... With [mc]."
    scene ch4sc19_257 with Dissolve(1.3)
    $ renpy.pause()
    scene ch4sc19_257 with dissolve
    mc "Miss me?"
    scene ch4sc19_257 with dissolve
    al "You have no idea-"
    scene ch4sc19_258 with dissolve
    with vpunch
    al "[mc]?! Y-Y-You’re here?!"
    al "I can’t believe it! You’re back!"
    scene ch4sc19_260 with dissolve
    al "Prepare yourself!"
    mc "Alice what are you-"
    scene ch4sc19_261 with dissolve
    with vpunch
    al "{b}HUG-ATTACK!!{/b}"
    mc "*Grunts* Alice... People are staring."
    al "*Laughs* Let em! I want my hug!"
    scene ch4sc19_262 with dissolve
    al "..."
    scene ch4sc19_263 with dissolve
    al "*Shy* You’re touching my ass..."
    scene ch4sc19_264 with dissolve
    mc "You surprised me... I had to grab onto something with decent volume."
    scene ch4sc19_263 with dissolve
    al "I-... I don't mind."
    ####Choice####
    menu:
        "Keep grabbing her ass. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc19_263 with dissolve
            al "You’re not letting go?"
            $ alice_path = True
            scene ch4sc19_264 with dissolve
            mc "No, I’m not."
            "Alice likes that you grabbed her ass, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            $ alice_trust += 5
            scene ch4sc19_263 with dissolve
            al "[mc]... We’re in public..."
            al "What will people think?"
            scene ch4sc19_264 with dissolve
            mc "I don’t care. You have a cute little ass and I like having you in my hands."
            scene ch4sc19_265 with dissolve
            al "Good riddance! If you’re going to corrupt me in public you should at least kiss me..."
            scene ch4sc19_266 with dissolve
            al "*Whispers* {size=-10}{b}I’ve been waiting months for this...{/b}{/size}"
            al "*Whispers* {size=-10}{b}Now kiss me like I’m the only girl in the world.{/b}{/size}"
            scene ch4sc19_267 with dissolve
            $ renpy.pause()
            "The two of you merge lips and you feel her big soft lips latching onto yours repeatedly."
            scene ch4sc19_268 with dissolve
            mct "It’s like her lips are made for this... They’re incredibly soft."
            scene ch4sc19_267 with dissolve
            al "*Moans softly* MMmmmMMmm ..."
            scene ch4sc19_268 with dissolve
            al_t "He’s back... And we’re kissing! Mmmmhh... And I’m in his hands..."
            scene ch4sc19_267 with dissolve
            al_t "His lips are amazing! I don’t even care if people are watching..."
            scene ch4sc19_268 with dissolve
            al "*Soft moan* NNngh! He’s grabbing my ass so firmly... We have to stop... Otherwise I need to change panties..."
            scene ch4sc19_266 with dissolve
            al "*heavy breathing* We need to stop..."
            mc "Sure."
            scene ch4sc19_267 with dissolve
            al "MMmHHh! AahhHh..."
            scene ch4sc19_266 with dissolve
            al "*Heavy breathing* J-Jerk! Stop..."
            scene ch4sc19_267 with dissolve
            mct "Heh... She’s telling me to stop but she keeps kissing me? This girl..."
            scene ch4sc19_268 with dissolve
            al_t "*Sigh* I’ve missed him so much!"
            scene ch4sc19_269 with dissolve
            $ renpy.pause()
            al_t "NNngh! It’s like we’re communicating our feelings with each kiss."
            al_t "I... No! We need to stop... Before I ask him to pull me into an empty class-room and take me right there"
            scene ch4sc19_268 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_267 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_266 with dissolve
            $ renpy.pause(1)
            al "*Panting* S-Stop... We need to stop."
            scene ch4sc19_263 with dissolve
            al "Please put me down..."
            scene ch4sc19_270 with dissolve
            al "Sorry ... It’s not that I wanted to stop... It’s just-"
            mc "Don’t worry, this isn’t the time or place."
            al "Yeah... We were being... Indecent."
            scene black with dissolve
            "The two of you take a moment to calm down."


        "Put her down. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc19_264 with dissolve
            mc "Okay I think that’s enough hugging for now..."
            scene ch4sc19_265 with dissolve
            al "Y-Yeah... It was nice."

    scene ch4sc19_270 with dissolve
    al "I can tell something is on your mind."
    al "You’re not just here to see me, are you?"
    scene ch4sc19_271 with dissolve
    mc "Not just to see you, no."
    scene ch4sc19_272 with dissolve
    al "Let’s hear it..."
    al "Maybe I can help?"
    scene ch4sc19_273 with dissolve
    mc "I need to find a girl, Luna."
    mc "She supposedly attends the Academy here."
    al_t "He’s looking for Luna? Maybe it has something to do with her sword?"
    al_t "Or maybe it has to do with her mother? But how is [mc] involved in this?"
    mc "Alice?"
    scene ch4sc19_274 with dissolve
    al "Huh? Sorry! Yes I know Luna, she’s a friend actually."
    al "Is this about her mother?"
    scene ch4sc19_275 with dissolve
    mc "Yes. I went back to the prison where Taron kept Eliza, I wanted to look for clues."
    mc "But instead I found a woman, Luna’s mother. Being kept in one of the cells..."
    scene ch4sc19_276 with dissolve
    al "Oh? You rescued her mom? That’s amazing! Then Luna won’t have to work on that cursed sword anymore!"
    al "I was worried she would end up getting herself into something bad..."
    scene ch4sc19_277 with dissolve
    mc "Not so hasty... I couldn’t free her mother."
    mc "Taron has managed to put some sort of ‘Hex’ on her."
    mc "Her mother can’t leave the prison without dying. She pleaded with me to help Luna."
    scene ch4sc19_278 with dissolve
    al "That’s horrible... So helping Luna with the artifact is the play?"
    mct "Alice knows about the cursed artifact?"
    al "Luna should be in the east wing, there’s an unused room at the top of the stairs, she usually works in there"
    al "While you deal with Luna, I’ll ask my professor about the hex, she could know something."
    scene ch4sc19_279 with dissolve
    mct "Is it just me or has Alice really grown up after I saw her in Riverside?"
    mct "She’s not afraid to get involved and she’s even taking charge."
    mc "Okay. We’ll work it from both angles. But don’t reveal too much to the professor..."
    mc "The less people who knows about it the safer it is."
    mc "Be careful Alice... Good luck."
    scene ch4sc19_280 with dissolve
    al "You’re the one who’s going to need luck! Luna has been working on the sword for almost two months!"
    al "Just... Do what you can to help her... She’s really sweet."
    scene ch4sc19_281 with dissolve
    al "My classes are about to begin! Catch you later!"
    mct "I better get to it... East wing, room at the top of the stairs."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc16_182 with dissolve
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    lu "C’mon... Just break already you stupid! Idiot! Curse!"
    scene ch4sc16_183 with dissolve
    lu "*Chanting* Azha... Lir... Lazi’ahi... Luh!"
    scene ch4sc16_184 with dissolve
    with vpunch
    lu "*Groans* {b}NO!!{/b}"
    lu "At this rate I’ll never break the curse! And I’m running out of time!"
    scene ch4sc16_185 with dissolve
    lu "He will hurt mother..."
    lu "None of my magic is effective on this thing..."
    scene ch4sc19_283 with dissolve
    mct "There she is... Silverish hair, black clothes, big quirky hat."
    mc "Hey, need some help with that?"
    scene ch4sc19_284 with dissolve
    with vpunch
    lu "*Startled* Who are you?!"
    lu "Stay put! Unless you wish to be incinerated!"
    scene ch4sc19_285 with dissolve
    mc "Woah, woah! No need to set the place on fire..."
    lu "Speak! Before I set you ablaze!"
    mc "Cassandra asked me to find you. To help you with the cursed relic."
    lu "Lies! You don’t know her! You’re one of Tarons lackeys sent to scare me!"
    scene ch4sc19_286 with Dissolve(1.3)
    mc "..."
    scene ch4sc19_287 with dissolve
    mc "Don’t... Ever... Associate me with that cockroach!"
    scene ch4sc19_287b with dissolve
    mc "We clear?"
    lu "Okay! Okay..."
    lu "So you’re not one of his lackeys? Then who are you?"
    scene ch4sc19_287 with dissolve
    mc "I’m [mc], I'm a member of the Adventurer's guild."
    mc "I was investigating an area Taron had kept one of my friends..."
    scene ch4sc19_288 with dissolve
    lu "That’s where you met my mom. In Taron’s dungeon..."
    scene ch4sc19_289 with dissolve
    mc "Yeah, she didn't look to be in pristine condition."
    scene ch4sc19_290 with dissolve
    lu "He’s been keeping her locked up for months... Caged up like an animal!"
    with vpunch
    lu "I have to free her! *Frustrated sigh* But I haven’t been able to make any progress..."
    scene ch4sc19_289 with dissolve
    mc "Cassandra asked me to find you. To help you."
    scene ch4sc19_291 with dissolve
    lu "Curious..."
    lu "Why? Why would you put yourself in danger to help me?"
    scene ch4sc19_287 with dissolve
    mc "I'll be honest with you, helping you is not out of the goodness in my heart."
    mc "I have my own motivations for wanting Taron to suffer... Helping you serves that purpose."
    scene ch4sc19_292 with dissolve
    lu "Hmh."
    mct "She’s smiling?"
    scene ch4sc19_293 with dissolve
    lu "An alliance... I like it."
    lu "Shake on it?"
    scene ch4sc19_294 with dissolve
    mc "Sure."
    scene ch4sc19_295 with dissolve
    $ renpy.pause()
    mct "Her hands are so delicate..."
    lu "We'll work together, to free my mother and bring Taron to justice."
    mc "We'll work together."
    scene ch4sc19_296 with dissolve
    lu "..."
    mct "She’s kind of cute... If you look past her almost incinerating me earlier..."
    scene ch4sc19_297 with dissolve
    lu "Okay! Let’s get to it!"
    mc "After you."
    scene ch4sc19_298 with dissolve
    lu "This is what we’re working with. A black blade of unknown origin..."
    lu "It’s believed to be from the ancient world."
    scene ch4sc19_299 with dissolve
    mc "Ancient world? As in the world before Balthazar’s rampage?"
    scene ch4sc19_300 with dissolve
    lu "Exactly... You do know some of our history. Curious."
    scene ch4sc19_299 with dissolve
    mc "That means this relic is well over 500 years old, probably more."
    mc "I'm guessing it's from the 1st Era."
    scene ch4sc19_300 with dissolve
    lu "Uh-Huh, it's highly likely to be way older."
    lu "I haven't been able to determine it's origin."
    scene ch4sc19_301 with dissolve
    mc "It looks like it’s still in pristine condition... What material is it made of?"
    lu "I don’t know... It’s pitch-black all over, even the hilt and handle... Like onyx or obsidian."
    mct "Strange... It definitely has potent magic infused into it. Ancient... Dark magic."
    scene ch4sc19_299 with dissolve
    mc "Luna, this blade is cursed, correct?"
    scene ch4sc19_298 with dissolve
    lu "Yes. I’ve been trying to break the curse by infusing my magic into it, hoping to overwhelm it."
    lu "But it seems to be protected by some sort of barrier that repels my magic..."
    scene ch4sc19_301 with dissolve
    mc "Mind if I take a look at it?"
    lu "Go ahead... I’m at a loss as what to do about it."
    scene ch4sc19_302 with dissolve
    lu "What are you doing?"
    mc "Checking its balance... It’s incredibly light for a sword this size, but perfectly balanced."
    mc "Stand back a bit, I’m going to try to infuse some of my magic into it..."
    scene ch4sc19_303 with dissolve
    lu "Your magic? You’re a mage?!"
    lu "Why didn't you tell me?"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc19_304 with dissolve
    mc "No, not like a mage. I’m something else entirely..."
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_304a with dissolve
    with vpunch
    lu "It’s responding to you?! How?"
    scene ch4sc19_304aa with dissolve
    mc "I’m channeling it with my magic just like you said, to overwhelm it."
    scene ch4sc19_304b with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    with vpunch
    lu "By the arcane arts! It’s working?!"
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    mc "*Grunts* Ahrrh! Let’s find out!"
    scene ch4sc19_304c with dissolve
    with vpunch
    lu "{b}*Screams*{/b} AAiiiyh!"
    with vpunch
    mc "I can’t hold it much longer! Get down!"
    lu "{b}*Shouting*{/b} [mc]! Aiihh!"
    with vpunch
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    scene ch4sc19_305 with Dissolve(1.3)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    mc "You okay?"
    lu "*Shaking* Y-Yes... I... I think so."
    scene ch4sc19_306 with dissolve
    lu "By the Arcane! What was that?! Did it work?"
    lu "Is the curse finally broken?"
    scene ch4sc19_307 with dissolve
    mc "Not yet... I felt it giving way but I might have to do it over several attempts."
    mc "Do you mind if I stay here and continue working on it?"
    scene ch4sc19_308 with dissolve
    lu "Not at all! But... What should I do? My magic won’t work on it."
    lu "I can’t just sit still while my mother is imprisoned..."
    scene ch4sc19_309 with dissolve
    mc "Your mother mentioned a hex put on her? Preventing her from leaving, my friend Alice is working on it."
    mc "She isn’t magically gifted though and could probably use your help in finding a way to break the hex."
    scene ch4sc19_310 with dissolve
    lu "Oh, you know Alice? She’s really sweet!"
    scene ch4sc19_311 with dissolve
    lu "*Mumbles* She’s... My only friend..."
    lu "..."
    lu "I really appreciate you doing this..."
    lu "I know you aren't doing it for me... But-... Thank you."
    scene ch4sc19_309 with dissolve
    mc "You don't have to thank me, as you said, I have my own reasons for helping."
    scene ch4sc19_308 with dissolve
    lu "Just one thing before I go to help her..."
    scene ch4sc19_312 with dissolve
    $ renpy.pause()
    mc "Oh?"
    scene ch4sc19_313 with dissolve
    $ renpy.pause()
    lu "Regardless of intentions, your help is valuable to me. So-"
    scene ch4sc19_314 with dissolve
    lu "*Mwah*"
    mct "That was unexpected... I guess she really appreciates someone trying to help her mom."
    mct "Can’t have been easy dealing with all this on her own as an 18 year old..."
    mct "Her scent... Vanilla and Orchids."
    "Luna's warm, soft lips lingers for a few moments before stepping back."
    scene ch4sc19_308 with dissolve
    lu "Sorry! I-I'm just grateful!"
    lu "A-And your super cute! And dark! Tall and dark! Um-Hh!"
    scene ch4sc19_316 with dissolve
    lu "Aaaand I’m rambling like a total mess..."
    lu "Byee!"
    scene ch4sc19_317 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch4sc19_318 with dissolve
    mct "*Sigh* She seems sweet and trustworthy... And Alice likes her."
    mct "But after Selena, I don’t want to take any chances when it comes to Taron."
    mct "It’s better if nobody knows I actually broke the curse..."
    scene ch4sc19_319 with dissolve
    mct "But why would a sword from the ancient world be of value to Taron?"
    mct "And why would it have that strong of a curse placed on it?"
    scene ch4sc19_320 with dissolve
    mct "Since Sylph and I aren’t on speaking terms right now..."
    mct "I guess there's only one way to figure this out... I’ll have to disenchant it myself."
    scene ch4sc19_321 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    with vpunch
    mc "{b}W-WHAT THE?!{/b}"
    scene ch4sc19_322 with Dissolve(1.5)
    play music forestnight_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc19_323 with Dissolve(1.5)
    $ renpy.pause()
    scene ch4sc19_324 with dissolve
    $ renpy.pause()
    mct "Five hells... What is going on? The sword is transforming into a..."
    scene ch4sc19_325 with dissolve
    $ renpy.pause()
    scene ch4sc19_326 with dissolve
    mct "Woman?"
    scene ch4sc19_327 with dissolve
    uk "You."
    uk "You freed me."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch4sc19_326 with dissolve
    mc "What... Are you?"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "I broke a curse placed on the blade... Which you emerged from?"
    scene ch4sc19_327 with dissolve
    uk "You don’t know what I am?"
    scene ch4sc19_326 with dissolve
    mc "No? I’ve never seen anything like you."
    scene ch4sc19_327 with dissolve
    uk "Tell me, What year is this?"
    scene ch4sc19_326 with dissolve
    mc "Year 562 of the 2nd Era."
    scene ch4sc19_328 with dissolve
    with vpunch
    uk "{b}WHAT?!{/b} Has it really been that long..."
    scene ch4sc19_329 with dissolve
    mc "You still haven’t told me what you are."
    scene ch4sc19_330 with dissolve
    uk "I’m a Symbiote! Silly!"
    scene ch4sc19_328 with dissolve
    uk "You know... Like a Slime or Oozeling just... Cooler!"
    scene ch4sc19_329 with dissolve
    mc "What’s the difference?"
    scene ch4sc19_330 with dissolve
    uk "I’ll pretend you didn’t just say that!"
    scene ch4sc19_329 with dissolve
    uk "There’s too many differences to go over them all right now... But I suppose the main difference is-"
    scene ch4sc19_328 with dissolve
    uk "How we survive, slimes has to devour bio-organisms to survive."
    scene ch4sc19_329 with dissolve
    uk "Oozelings survive by feeding on in-animate objects and materials. Disgusting I know! Blegh!"
    scene ch4sc19_330 with dissolve
    uk "And Symbiotes, like myself survive by forming a symbiosis with a living being!"
    scene ch4sc19_326 with dissolve
    mc "Symbiosis? Like a give and take between the host and you?"
    scene ch4sc19_331 with dissolve
    uk "Exactly! You’re brilliant! Catching on quickly."
    scene ch4sc19_329 with dissolve
    uk "As a Symbiote, I need essence from a living host to survive."
    scene ch4sc19_326 with dissolve
    mc "Won’t that kill the host?"
    scene ch4sc19_327 with dissolve
    uk "In most cases yes. We usually seek a host with a high amount of essence or life-force."
    scene ch4sc19_328 with dissolve
    uk "That way we can survive for longer and benefit from symbiosis."
    scene ch4sc19_329 with dissolve
    mc "What does the host gain from the symbiosis?"
    scene ch4sc19_330 with dissolve
    uk "Lots of benefits! A telepathic connection between host and symbiote is established."
    scene ch4sc19_331 with dissolve
    uk "And the host will benefit from increased physical power! Symbiotes are very powerful!"
    mct "Hmh... This is not what I expected... Is that why Taron wants this creature? To increase his power?"
    scene ch4sc19_326 with dissolve
    mct "What if I were to enter this symbiosis it’s talking about? I have vast amounts of essence and I am able to regenerate."
    scene ch4sc19_327 with dissolve
    ox "I’m Onyx btw!"
    scene ch4sc19_329 with dissolve
    mc "Nice to meet you Onyx, I’m [mc]."
    scene ch4sc19_330 with dissolve
    ox "[mc], Hmh! I like it!"
    scene ch4sc19_329 with dissolve
    mc "Onyx, why were you under that curse?"
    scene ch4sc19_328 with dissolve
    ox "Ugh! That stupid witch cursed me!"
    ox "She forced me into the shape of a blade and put an immobiluz curse on me."
    scene ch4sc19_331 with dissolve
    ox "It’s basically like a stasis spell, only permanent until broken by sheer force of power."
    scene ch4sc19_330 with dissolve
    ox "You... You must be very powerful to break such a curse."
    scene ch4sc19_329 with dissolve
    mc "I suppose... So you need a host to survive now that the curse is broken?"
    scene ch4sc19_327 with dissolve
    ox "Yes... Afraid I won’t be able to manifest for long without a host and their essence."
    scene ch4sc19_326 with dissolve
    mc "A man named Taron wants you for himself, do you know him?"
    scene ch4sc19_329 with dissolve
    ox "Taron... No. I’ve been asleep for well over 500 years if what you told me earlier is true."
    scene ch4sc19_330 with dissolve
    ox "Last I remember some warlord named Balthazar wanted to acquire me during the age of the rebellion wars."
    scene ch4sc19_329 with dissolve
    mc "You knew Balthazar?"
    scene ch4sc19_330 with dissolve
    ox "Not personally... I knew ‘of’ him. He had quite the reputation! You didn’t want to stand in his way."
    scene ch4sc19_331 with dissolve
    ox "Lord of Embers they often referred to him as. He would torment those who stood against him by burning them alive..."
    scene ch4sc19_329 with dissolve
    mc "Balthazar is gone, has been for 500 years."
    scene ch4sc19_330 with dissolve
    ox "Good! I don’t care much for world destruction and all that. I’m a simple symbiote... I like to be alive!"
    scene ch4sc19_328 with dissolve
    ox "And thanks to you... I finally feel alive again."
    scene ch4sc19_326 with dissolve
    ox "So this... ‘Taron’ wants to enter symbiosis with me?"
    scene ch4sc19_331 with dissolve
    ox "However... He didn’t free me."
    scene ch4sc19_332 with dissolve
    ox "You did."
    ox "You removed the shackles on me, Mhm..."
    scene ch4sc19_333 with dissolve
    ox "Would you be open to me?"
    ox "To... Bond with me? To... Have me?"
    scene ch4sc19_334 with dissolve
    ox "You freed me... You deserve me. I could be yours if you want it..."
    ox "With you as my host... I wouldn’t just be feeding to survive... You would make my life... Exciting."
    scene ch4sc19_335 with dissolve
    $ renpy.pause()
    ox "Something I crave desperately... Being stuck as a cursed object for 500 years... Not very thrilling."
    ox "Just sensing the magic within you ... Sends tingles throughout my body."
    scene ch4sc19_336 with dissolve
    mc "How would it work?"
    mc "You would become part of me?"
    ox "Yes, as we enter symbiosis, we will merge into one."
    scene ch4sc19_335 with dissolve
    ox "We will be able to communicate through your mind. You will be able to call upon me if you need me."
    ox "You could use me as a weapon in battle. Or I could shield you from harm."
    scene ch4sc19_336 with dissolve
    mc "What about the whole you feeding on my essence situation?"
    ox "You’ve got more magic within you than I’ve ever seen... It would take years if not decades for me to drain you ..."
    mc "Encouraging..."
    scene ch4sc19_334 with dissolve
    mct "She doesn’t know about my regenerative powers..."
    mct "They could potentially recover and off-set the magic she needs to survive."
    scene ch4sc19_338 with dissolve
    $ renpy.pause()
    mct "I can't let Taron have her... If what she claims is true, she will be a tremendous asset."
    mct "Even Balthazar sought her... If I'm to do this, we better do it right, I'll be honest with her."
    scene ch4sc19_336 with dissolve
    mc "Onyx, I have the ability to passively regenerate. Would that affect anything?"
    ox "Yes! Yes it would! How exciting this is!"
    scene ch4sc19_335 with dissolve
    ox "This means we could maintain symbiosis... As long as we want! Years... Decades... Centuries!"
    ox "*Moans* I'm quivering at the thought!"
    ox "There’s essentially two ways for maintaining our symbiosis."
    scene ch4sc19_337 with dissolve
    ox "One. I feed passively from you as I’ve done with my past hosts..."
    ox "Boring, but it does the trick."
    scene ch4sc19_335 with dissolve
    ox "Or... Two. I feed actively from you... Much more exciting!"
    scene ch4sc19_336 with dissolve
    mc "Actively?"
    scene ch4sc19_337 with dissolve
    ox "*Sensual tone* Actively... Very actively..."
    scene ch4sc19_335 with dissolve
    mc "You mean..."
    scene ch4sc19_338 with dissolve
    ox "Why don’t I show you..."
    ####Choice####
    menu:
        "Allow her to feed actively. ({color=#ff8cdd}Onyx scene{/color})":
            scene ch4sc19_338 with dissolve
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            mct "This could be interesting."
            $ ox_path = True
            mc "Go ahead. Show me how you would like to be fed."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            ox "Exciting! Thrilling! Mmnn... You will have to lose these!"
            scene ch4sc19_339 with dissolve
            ox "Mnnh... What a fine specimen you are."
            ox "Such a warm and well built body. Mhm..."
            ox "I’m very excited for you to be my host..."
            mct "Her breasts are surprisingly warm..."
            ox "You like them, don’t you?"
            scene ch4sc19_340 with dissolve
            ox "The feeling of them wrapping around your powerful arm... How soft and squishy they become against your skin."
            mc "They feel amazing... Different to normal breasts..."
            scene ch4sc19_339 with dissolve
            ox "Mhm-hm. That's because my body can materialize and liquify at will."
            ox "So I can match them perfectly to your needs."
            scene ch4sc19_340 with dissolve
            ox "Once we enter symbiosis they will be yours whenever you want."
            ox "I'll be yours."
            scene ch4sc19_339 with dissolve
            ox "As your Symbiote... My only purpose in life will be to protect you and make you happy."
            scene ch4sc19_341 with dissolve
            ox "Would you like that?"
            mc "Yes."
            scene ch4sc19_339 with dissolve
            ox "Then let’s get these pesky pants off! I need to feed directly from the source!"
            scene black with dissolve
            scene ch4sc19_342 with dissolve
            ox "{b}MH-HM!{/b} You’re already erect! And... Much bigger than I suspected!"
            ox "You must be really excited about me satisfying you until you feed me..."
            mc "I guess it would be foolish to try and deny it at this point..."
            scene ch4sc19_343 with dissolve
            ox "*Gasps* {b}OH!{/b} It’s... It’s like a rod of steel!"
            ox "So warm and... Firm! I absolutely need a taste!"
            scene ch4sc19_344 with dissolve
            ox "*Kiss*"
            mc "Aahh... Onyx... Keep doing that."
            scene ch4sc19_345 with dissolve
            $ renpy.pause()
            ox "*Suck* Mnnghh..."
            scene ch4sc19_346 with dissolve
            ox "*Kiss* Sowwh... Mnnhh! {b}Ghood!{/b}"
            scene ch4sc19_347 with dissolve
            ox "*Suck* MnnhhH... *Suck* {b}Mnnh-Mhh!{/b}"
            mc "*Groans* Hnnh... Just like that... Fuck."
            "Her liquidy lips merging with your cock is a surreal feeling you've never experienced before."
            scene ch4sc19_346 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_345 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_346 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_347 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_346 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_345 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_346 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_347 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_348 with dissolve
            $ renpy.pause()
            ox "*Lick* Mmnhh! Oh? You already got a little present for me? Let me just get that..."
            scene ch4sc19_349 with dissolve
            ox "*Licks* {b}Yumhhmm!{/b} Mnnhh..."
            ox "I'll be a good Symbiote for you... Mhm!"
            scene ch4sc19_350 with dissolve
            mc "*Moans* F-Fuck Onyx... That’s AhhH... Something else... AhHh..."
            ox "I will Mhnngh... Satisfy you in NnnhH... Ways you can’t imagine master..."
            scene ch4sc19_351 with dissolve
            ox "Please... Master... Feed me!"
            mct "Her tongue is amazing... Fuck. The way she’s begging me... Let’s complete this symbiosis."
            scene ch4sc19_352 with dissolve
            with vpunch
            ox "{b}OHHmMm!!{/b} OOhm! *Suck* MMhmmhh! *Lick*"
            "You push yourself inside her warm mouth, catching her by surprise. She doesn’t have time to retract her tongue."
            show ox_ani1 with fade
            $ renpy.pause(1, hard=True)
            $ renpy.pause()
            ox "*Moans* {b}OOhhMmm!! MMnh!! Mhppff!{/b}"
            mct "Damn... She’s taking my cock well... It’s like her mouth is morphing to fit me perfectly..."
            mc "That’s a good symbiote... Ahh."
            ox "{b}*Moans* OOhhMmm!! *Licks* MMnh!! *Sucks* Mhppff!{/b}"
            show ox_ani2 with fade
            $ renpy.pause(1, hard=True)
            $ renpy.pause()
            mc "*Grunts* That’s right... Take all of it."
            ox "*Muffled* {b}MNHH!!{/b} OmhHh! *Sucks thoroughly* {b}Mmffh!{/b}"
            mc "Your mouth is amazing Onyx... If you keep doing this well, you will be fed often."
            ox "*Sucks harder* {b}MmmhhH!{/b}"
            show ox_ani3 with fade
            $ renpy.pause(1, hard=True)
            $ renpy.pause()
            mc "*Grunts* Ahh... You want to be fed huh? Then show me. Show me just how much you desire it."
            "Onyx tightens her mouth around your cock firmly, squishing her tongue against you."
            ox "*Sucks eagerly* {b}MMH! MMffh!{/b}"
            "Each time she pushes you inside her mouth she licks your shaft and squeezes you with her lips."
            with vpunch
            mc "That’s it... I’m- {b}I’m coming!{/b}"
            with vpunch
            ox "{b}*Sucking harder* !!!{/b}"
            with vpunch
            scene ch4sc19_352 with dissolve
            mc "*Moans* {b}AhHh!{/b} Fuck..."
            "Even though you just came down her throat she hasn't stopped sucking."
            scene ch4sc19_353 with dissolve
            ox "*Suck* {b}Mmhh!{/b} *Suck* NNngh!"
            with vpunch
            scene ch4sc19_354 with dissolve
            ox "*Sucks gently* Mnnnh..."
            mc "Damn... You really just pulled out every last drop..."
            mc "Make sure you get it all... You deserve it."
            scene ch4sc19_355 with dissolve
            ox "*Sucks* MnHhhhH... *Licks* MmmmMmm..."
            "Onyx continues to lick every inch of your hard throbbing cock until it’s completely clean."
            scene ch4sc19_353 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_355 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_353 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_355 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_356 with dissolve
            ox "Mmmhh! Thank you master!"
            ox "Who knew feeding could be so... Exciting!"
            scene ch4sc19_353 with dissolve
            ox "*Sucks gently* Mmhm... Mh-mh-mnnnh..."
            scene ch4sc19_356 with dissolve
            ox "Yum!"
            mc "Feeding you was an experience... That was incredible."
            ox "I’m happy you chose this method! I’m already getting hungry just thinking about the next time you will feed me!"
            scene ch4sc19_357 with dissolve
            mc "You and me both..."
            mc "So... We’re in symbiosis now?"
            ox "Not quite! We’ll have to merge into one."
            scene ch4sc19_358 with dissolve
            ox "Do you accept me? Do you wish to bond with me? To become as one?"
            ox "For me to be yours? To use me as your desires see fit?"
            scene ch4sc19_359 with dissolve
            mc "I do."
            scene ch4sc19_358 with dissolve
            ox "No hesitation? A man after my own tastes."
            ox "Your conviction is unwavering... Hot."
            scene ch4sc19_360 with dissolve
            ox "Merge with me [mc]! Let’s become one..."
            mct "I can feel her essence entering my body..."
            mct "It feels... Strange? It’s like my body is absorbing her."
            scene ch4sc19_361 with dissolve
            $ renpy.pause()
            mct "Strange is too mild a word..."
            scene black with Dissolve(2)
            scene ox_unlock with dissolve
            $ renpy.pause()
            scene black with Dissolve(2)


        "Refuse her. (Passive feeding)":
            scene ch4sc19_336 with dissolve
            mc "Stop. If we are to do this symbiosis thing... You will feed passively."
            ox "Shame... As you wish... We’ll do it your way."
            scene black with dissolve
            scene ch4sc19_358a with dissolve
            ox "We’ll become as one... Symbiosis will benefit us both greatly. Are you willing to accept me?"
            scene ch4sc19_359a with dissolve
            mc "I understand the terms. You will survive by feeding passively on my essence, in return I’ll become stronger."
            mc "I accept you, Onyx..."
            scene ch4sc19_358a with dissolve
            ox "A man of conviction... Delicious!"
            ox "Merge with me [mc]! Let’s become one!"
            scene ch4sc19_360a with dissolve
            ox "*Moans*"
            "You feel Onyx beginning to merge with you."
            scene ch4sc19_361a with dissolve
            "Your body absorbs her as and the two of you become one."
            scene black with Dissolve(2)
            scene ox_unlock with dissolve
            $ renpy.pause()
            scene black with Dissolve(2)

    scene ch4sc19_362 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    ox "We did it! We are one!"
    show ox_ani4 with fade
    $ renpy.pause(1, hard=True)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    ox "OooOuuohHh! Do you realize how thrilling your magic feels?!"
    ox "And you didn’t even vomit! That’s a first..."
    mc "It felt strange but... Also good?"
    ox "I did go easy on you... I wanted it to be pleasant."
    mc "So... How does this work? Can anyone hear us?"
    ox "No. We’re communicating via our symbiosis, sort of like a... Mind-link?"
    mc "You can read my mind?"
    ox "Wouldn’t that be thrilling?! But no... It’s more akin to having a conversation only with our thoughts."
    ox "Also I won’t just be able to talk to you out of nowhere, you will have to focus on me to establish our connection."
    mc "Are you able to see what I see?"
    ox "Not exactly. When you activate me, it’s more like I can ‘sense’ what your eyes see?"
    ox "It’s a little odd to explain-..."
    ox "but essentially I can see when you choose to activate me otherwise I just rest dormant inside you."
    mc "Let’s talk combat. What can I expect?"
    ox "You already know my blade form. You can channel me into that if you need to slice somebody in half..."
    ox "I’ve basically granted you the ability to manipulate my symbiote slime into whatever you wish."
    ox "To do so, just activate me by channeling me with your magic and thinking about what you wish to shape me as."
    ox "I’m very durable, so don’t worry about hurting me."
    ox "I'm basically immortal as long as my host is alive, which is why a symbiote-"
    ox "-Will do anything to protect her host. Your life is my life. We are one."
    mc "That’s incredible... And pretty handy."
    ox "I told you! Symbiosis is awesome! Why do you think Balthazar wanted me?"
    ox "He wouldn’t just have been a powerful warlord, with me he could have dominated the five kingdoms."
    mc "He was much more than just a warlord... He almost tore the world as we know it apart."
    mc "He caused the 1st era to end with his imprisonment... Thus started the 2nd era, 562 years ago now."
    ox "Wooooh... A lot must have happened after I was cursed then. Being in stasis without a host..."
    ox "I wasn’t able to perceive the world... It was all empty... Dark... Silent."
    mc "Good thing I freed you then?"
    ox "The best! I feel so alive again! More so than ever actually, thanks to your amazing essence!"
    mc "You said that a symbiote usually kills its host passively by feeding, however since my regeneration off-sets it."
    mc "Are we in permanent symbiosis?"
    ox "Yes. We are bonded permanently now... Unless... You expel me."
    mc "Expel you?"
    ox "Yes. If a host is exceptionally powerful... e.g you. They could expel a symbiote which would kill the symbiote."
    mc "Oh... Why tell me? You could easily have lied."
    ox "I... I’ve finally got a chance at life again. And with a host that’s actually worthwhile."
    ox "Our bond is permanent. I want it to be pure... Not tainted by lies. Anything you ask me I will answer truthfully."
    ox "You were honest with me from the beginning, I will grant you the same."
    ox "Even if you won’t like the answers."
    mc "I appreciate that Onyx."
    mc "Then I will ask you this... Did you want to be bonded with Balthazar?"
    ox "Yes."
    mc "Damn... You really weren’t kidding about being truthful."
    ox "You have to understand... In my time. He was the most renowned warlord."
    ox "A powerful host like him would mean a longer life-span for me."
    ox "That is my purpose as a symbiote, to form the best symbiosis I can and live through that."
    mc "Balthazar was evil though?"
    ox "Was he? He was known to be brutal to his enemies, but in my time he wasn’t known as ‘evil’."
    ox "Either way it wouldn’t matter. I don’t bind myself to the morals of my host..."
    ox "You could be the holiest saint of the high heavens or the darkest demon from the abyss."
    ox "None of that matters to me."
    mc "So basically, I shouldn’t count on you to steer me in a moral direction?"
    ox "You get it! Good! You can always ask for my advice whenever you need it without being judged."
    mc "I think we’ve covered all the basics for now."
    ox "Great! Then you don’t mind if I take a nap? It's so warm and cozy in here..."
    ox "Just call on me whenever you need me."
    ox "By the way... You probably shouldn’t go telling people about me."
    ox "You said this ‘Taron’ was after me? Others could be as well."
    mct "She's right, telling anyone won't do any good for now."
    scene ch4sc19_362 with dissolve
    mc "Sure. I won’t tell anyone, go ahead and get some rest."
    scene ch4sc19_363 with dissolve
    mct "*Sigh* That was certainly ... Unexpected. I thought the sword might be a powerful weapon."
    mct "But it was much more than just a weapon ... A whole being? From the ancient world..."
    mct "I did kind of rush into this ... But I wasn’t about to let Taron have her."
    scene ch4sc19_364 with dissolve
    mct "Onyx will be a valuable asset going forward."
    mct "I better go pick-up Eliza, she should almost be done at the guild."
    #play music explore_1 fadein 1.0
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_365 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    el "Here you go, Milton. A compass and a healing elixir, just in case you run into trouble."
    el "I doubt you will, though. It should be a simple delivery quest."
    scene ch4sc19_366 with dissolve
    ml "Thank you, miss Eliza."
    ml "You’re always so thoughtful. I just hope I can live up to your expectations."
    scene ch4sc19_367 with dissolve
    el "Please... There are no expectations here other than you do your best!"
    scene ch4sc19_366 with dissolve
    ml "That's nice to hear. I've always felt a lot of pressure from the higher-ups at the garrison."
    scene ch4sc19_367 with dissolve
    el "I’m just happy that I was able to get you back on your feet after we caused you to be dismissed."
    scene ch4sc19_366 with dissolve
    ml "Water under the bridge! I’m happier here than I ever was as a guard..."
    scene ch4sc19_367 with dissolve
    el "I like the sound of that! You seem to be enjoying the book I found for you?"
    scene ch4sc19_366 with dissolve
    ml "Very much! I almost can’t believe most of what's in here..."
    scene ch4sc19_367 with dissolve
    el "It all true! It’s a bestiary, it has information on different creatures that guild members have encountered."
    scene ch4sc19_366 with dissolve
    ml "Cool! Have you seen any of these creatures?"
    scene ch4sc19_367 with dissolve
    el "I have. Goblins and a mean-looking goblin berserker too. And you know Sylph, obviously."
    scene ch4sc19_366 with dissolve
    ml "That... sounds rough. Wait, Sylph is in this?"
    scene ch4sc19_367 with dissolve
    el "Well, not her specifically. But there’s faes, fairies, nymphs, pixies and all sorts."
    el "I believe Sylph falls under the subspecies known as forest fae."
    scene ch4sc19_366 with dissolve
    ml "Mind if I keep this for tonight? I wouldn’t mind finishing it."
    scene ch4sc19_367 with dissolve
    el "By all means! Just bring it back tomorrow before you leave for your quest."
    el "Sylph can get a little overbearing if things aren't in order. *Giggles*"
    scene ch4sc19_368 with dissolve
    ml "Will do! Thank you, miss Eliza!"
    el "Don’t mention it-"
    scene ch4sc19_369 with dissolve
    el "*Excitedly* [mc]!! Incoming!"
    scene ch4sc19_370 with dissolve
    with vpunch
    el "Finally! Finally, finally!!"
    scene ch4sc19_371 with dissolve
    el "I’ve been waiting all day!"
    mc "*Whispers* {size=-10}{b}I love that you’re this excited but...{/b}{/size}"
    mc "Try to keep calm while we’re here. We don’t want you to lose control."

    if eliza_path == True:
        scene ch4sc19_372 with dissolve
        el "*Whispers* {size=-10}{b}I’m not letting go until you give me a kiss! I haven’t seen you all day.{/b}{/size}"
        scene ch4sc19_373 with dissolve
        el "*Kiss* Mmmh."
        mct "I love that she isn’t afraid to show everyone that she’s mine."
        mct "And she’s squeezing me so tightly... I suppose she still feels some trauma from being left alone."
        scene ch4sc19_374 with dissolve
        el "*Licks* Nnnghh ..."
        mct "Fuck... She's such a tease. The way she moves her tongue so gently across my lips."
        el "*Licks* MmMmmmmm ..."
        scene ch4sc19_373 with dissolve
        mct "Her heart is pounding... she's completely forgotten that anyone else is here."
        scene ch4sc19_372 with dissolve
        el "*Whispers* {size=-10}{b}Yum.{/b}{/size}"
        mc "*Whispers* {size=-10}{b}Yum indeed. I’ll need some more of that later...{/b}{/size}"
        el "*Whispers* {size=-10}{b}Mh-Hm! Definitely... just... a little appetizer! *Giggles*{/b}{/size}"
        scene ch4sc19_373 with dissolve
        el "*Kiss* Mhmh... Mmhhh."
        scene ch4sc19_372 with dissolve
        el "Okay! Okay... Phew! I'd better climb down. *Snickers*"
        scene black with Dissolve(1.5)


    else:
        scene ch4sc19_371 with dissolve
        el "Boooooo! *Sigh* Okay, I'll have my hug another time then."
        scene ch4sc19_375 with dissolve
        el "*Exhales* Okay ... I’m calm."

    scene ch4sc19_375 with dissolve
    mc "Ready to get out of here?"
    el "Yes!!"
    scene ch4sc19_376 with dissolve
    ml "Oh, hey. Welcome back [mc]."
    mc "Hey. Are you settling in alright?"
    ml "I sure am! Miss Eliza has been showing me the ropes and making sure I get appropriate quests for my skill level."
    scene ch4sc19_377 with dissolve
    mc "You’re in good hands with this one."
    mc "She’s the most incredible and hardworking girl I know."
    scene ch4sc19_378 with dissolve
    el "*Whispers* {size=-10}{b}Shush you!{/b}{/size}"
    scene ch4sc19_379 with dissolve
    el "Bye Milton! If I don’t see you tomorrow before your quest, best of luck and remember to stick to the roads!"
    scene ch4sc19_380 with dissolve
    mc "*Whispers* {size=-10}{b}Milton? Since when are you on first name basis? Why can't he just be... guard?{/b}{/size}"
    el "*Whispers* {size=-10}{b}You’re terrible! ... Don’t tell me you’re jealous?!{/b}{/size}"
    mc "*Whispers*{size=-10}{b} No...{/b}{/size}"
    el "*Whispers* {size=-10}{b}You totally are!{/b}{/size}"
    mc "*Sigh* ..."
    el "Good... It means you care."
    mc "Yeah, yeah. C’mon, let’s get out of here."
    scene black with Dissolve(1.5)
    scene ch4sc19_381 with dissolve
    el "I’m... hungry..."
    mc "I know. Not giving in to the hunger as soon as it presents itself is what you need to learn."
    scene ch4sc19_382 with dissolve
    el "*Sigh* I know... But it’s not like being hungry was before. It’s like my entire body is screaming at me."
    el "It feels like I’m burning up everywhere under my skin..."
    scene ch4sc19_383 with dissolve
    el "Every time we've passed a person since we left the guild, I've wanted to sink my teeth into their necks..."
    el "I can hear their hearts beating, pumping warm, delicious blood through their veins..."
    scene ch4sc19_384 with dissolve
    mc "Soon. I promise... You’re doing well keeping it at bay so far."
    mc "Let’s head up to the roof behind the tavern."
    scene ch4sc19_385 with dissolve
    el "The roof sounds kinda nice... I like it there."
    el "Can I... bite you up there?"
    scene ch4sc19_381 with dissolve
    mc "No."
    el "Booo! You’re being mean..."
    mc "We already talked about this. You need to learn how to feed properly if you want to control this."
    scene ch4sc19_385 with dissolve
    el "But you smell way better than everyone else."
    el "I bet your blood tastes... angelic!"
    scene ch4sc19_384 with dissolve
    mc "That’s the thing... we're worried there might be side-effects if you drink my blood."
    mc "Vampires feed on mortals. There are too many unknowns... what if my blood burns you from the inside out?"
    mc "Until we know for certain... I won’t let you anywhere near mine."
    scene ch4sc19_385 with dissolve
    el "I understand... I hate it, but I understand."
    scene ch4sc19_386 with dissolve
    el "Isn’t this the roof we sat on last night?"
    mc "Yeah, it is. It should be a good vantage point. It's off the main streets and drunks will walk through the alley."
    scene ch4sc19_387 with dissolve
    el "Eeuw! I don’t want to bite some filthy drunk!"
    mc "Picking a target who’s drunk will make it easier ..."
    mc "And if they try to tell anyone, people will just put it down to them being too drunk."
    scene ch4sc19_388 with dissolve
    el "Mhhm... Makes sense. *Sigh* Fine."

    if eliza_path == True:
        scene ch4sc19_389 with dissolve
        el "I already have a target in my sights..."
        scene ch4sc19_390 with dissolve
        el "You see... there’s this guy. He just recently came back to me... and everything’s changed again."
        mc "Everything?"
        scene ch4sc19_391 with dissolve
        el "Everything... except the way I feel about him."
        scene ch4sc19_392 with dissolve
        mc "I wonder who that could be."
        scene ch4sc19_391 with dissolve
        el "I’ll show you. Close your eyes."
        scene ch4sc19_393 with dissolve
        mc "Closed."
        el "Mh-Hm..."
        scene ch4sc19_395 with dissolve
        "You feel her warm breath against your lips, and her scent surrounds you like a warm blanket."
        el "Tell me. What do I smell like?"
        scene ch4sc19_394 with dissolve
        mc "Your scent is delicate..."
        mc "*Inhales* Dreamveil... Sunroot... with a subtle hint of citrus."
        scene ch4sc19_395 with dissolve
        el "Your nose is as sharp as ever. You like it?"
        mc "It’s intoxicating... not very different from your usual scent, though."
        scene ch4sc19_394 with dissolve
        el "It’s a new perfume I bought recently..."
        scene ch4sc19_395 with dissolve
        el "I tried a few different ones, but then I remembered how you complimented my scent..."
        scene ch4sc19_394 with dissolve
        el "The lady in the shop showed me this one, she called it an enhancer. It's supposed to enhance your own natural scent."
        scene ch4sc19_395 with dissolve
        el "I wanted to wear it for your return..."
        el "But you surprised me at the guild so I didn’t have a chance to wear it until now..."
        scene ch4sc19_394 with dissolve
        mc "It’s definitely having an... effect on me."
        mc "Your natural scent was already alluring as it was..."
        scene ch4sc19_396 with dissolve
        el "*Sensual whisper* Taste me..."
        "Her soft lips rest against yours, and you answer in kind."
        scene ch4sc19_397 with dissolve
        mct "There it is... her signature lip-sucking. She really is amazing."
        scene ch4sc19_398 with dissolve
        el "*Moans softly* Mmmmhh..."
        mct "She really has the best lips in all the known realms..."
        scene ch4sc19_397 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_398 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_399 with dissolve
        $ renpy.pause()
        #####ANIMATION#####
        show el_kiss10 with fade
        $ renpy.pause(1, hard=True)
        $ renpy.pause()
        el "Nnnghh... Mmmmmmm..."
        mct "Her tongue movements are unmatched... She’s massaging mine, covering it with her saliva."
        mct "It’s like each kiss is telling me how much she cares about me."
        elt "I don’t want to stop kissing him... Mhhh! We've got so many kisses to catch up on... *Licks*"
        scene ch4sc19_399 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_398 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_397 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_396 with dissolve
        el "*Heavy breathing * That was..."
        mc "Hot."
        scene ch4sc19_395 with dissolve
        el "Scorching..."
        mc "Blazing..."
        scene ch4sc19_394 with dissolve
        el "Searing..."
        mc "*Chuckles* You win."
        scene ch4sc19_396 with dissolve
        el "I want my prize now."
        scene ch4sc19_397 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_398 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_399 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_398 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_397 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_396 with dissolve
        mc "I've always hated losing. But with you, it’s like I win either way."
        scene ch4sc19_397 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_396 with dissolve
        $ renpy.pause(1.3)
        scene ch4sc19_393 with dissolve
        el "*Giggles* For such a brute... you really know how to melt me with your words."
        el "I need to sit... My knees feel funny."
        scene ch4sc19_391 with dissolve
        el "I might tumble and fall off the roof."
        scene ch4sc19_392 with dissolve
        mc "I’d catch you."
        scene ch4sc19_391 with dissolve
        el "Don’t say that... I might just test it."
        scene black with dissolve
        scene ch4sc19_400 with dissolve
        "The two of you sit closely together, looking up at the moon."
        scene ch4sc19_401 with dissolve
        el "I love you."
        scene ch4sc19_402 with dissolve
        mc "I love you too."
        scene ch4sc19_401 with dissolve
        el "To the moon and back?"
        scene ch4sc19_402 with dissolve
        mc "Mh-Hm. To the moon and back."

    else:
        scene ch4sc19_400 with dissolve

    scene ch4sc19_401 with dissolve
    el "It really is beautiful tonight. Big and bright... like a million fireflies swarmed together in the sky."
    scene ch4sc19_402 with dissolve
    mc "Imagine if that was true..."
    scene ch4sc19_403 with dissolve
    $ renpy.pause()
    scene ch4sc19_404 with dissolve
    el "I feel so tiny when I look up there..."
    scene ch4sc19_403 with dissolve
    mct "She's right... I wonder what else is out there?"
    scene ch4sc19_404 with dissolve
    el "Do you ever wonder what’s out there?"
    scene ch4sc19_403 with dissolve
    $ renpy.pause(1)
    scene ch4sc19_405 with dissolve
    mc "I used to quite often."
    mc "After your father took me away, I suffered from nightmares... about my parents."
    scene ch4sc19_406 with dissolve
    mc "I'd have these vivid dreams about finding them that night... and I'd wake up shaking."
    mc "When that happened, I'd find somewhere I could look at the moon."
    scene ch4sc19_405 with dissolve
    mc "And it might sound dumb... but I'd talk to it."
    mc "I'd tell it about everything I'd been through."
    scene ch4sc19_406 with dissolve
    mc "I'd complain about how things weren't fair... and the things that annoyed me."
    mc "And after a while, I always managed to calm down."
    "You feel her hand run up your back, then her fingers caressing your hair."
    scene ch4sc19_407 with dissolve
    el "[mc]... that’s not dumb. Not at all."
    el "You probably needed to talk to someone about it all, and I don’t imagine my father being a good listener."
    scene ch4sc19_408 with dissolve
    mc "Yeah, I could never talk to him. Not like I’m able to talk with you."
    scene ch4sc19_407 with dissolve
    el "I’m here for you... always."

    if eliza_path == True:
        scene ch4sc19_409 with dissolve
        el "I’ll be your moon."
        scene ch4sc19_410 with dissolve
        mc "My moon... I like that."
        scene ch4sc19_409 with dissolve
        el "You'd better! It’s a permanent position."
        el "And I offer no take-backs!"
        scene ch4sc19_410 with dissolve
        mc "I'd do anything for you. You know that, right?"
        scene ch4sc19_407 with dissolve
        el "I do."
        el "And the feeling is mutual. If you ended up in one of the five hells-"
        scene ch4sc19_409 with dissolve
        el "I'd barge in there and break you out myself!"
        scene ch4sc19_410 with dissolve
        mc "My own little hellraiser. *Chuckles*"

    else:
        scene ch4sc19_408 with dissolve
        mc "Thank you. It means a lot."

    scene black with Dissolve(1.5)
    scene ch4sc19_411 with dissolve
    "The two of you sit in companionable silence for a while, just observing the streets below."
    "Eliza gently runs her fingers through your hair while she rests against you."
    el "..."
    scene ch4sc19_412 with dissolve
    el "*Sigh* Hunger’s back..."
    scene ch4sc19_413 with dissolve
    mc "Luckily for you... it’s dinner time. See that girl?"
    scene ch4sc19_416 with dissolve
    el "Mh-Hm."
    el "I’m surprised you didn’t pick some stinky old man."
    scene ch4sc19_414 with dissolve
    mc "I think it’s important we make this a positive experience for you."
    scene ch4sc19_413 with dissolve
    mc "Anyway... she’s your meal for tonight."
    mc "I’ll observe and step in if needed."
    scene ch4sc19_414 with dissolve
    el "Mhhm..."
    el "I'm so hungry..."
    scene ch4sc19_415 with dissolve
    el "I can't believe I'm saying this... but she looks delicious."
    scene ch4sc19_416 with dissolve
    $ renpy.pause()
    scene ch4sc19_417 with dissolve
    $ renpy.pause()
    scene ch4sc19_418 with dissolve
    $ renpy.pause()
    scene ch4sc19_419 with dissolve
    $ renpy.pause(1.3)
    uk "Huh? Anyone there?"
    scene ch4sc19_420 with dissolve
    uk "Weird... I thought I heard something."
    uk "I must be imagining things. *Sigh* Serves me right for letting the girls get me tipsy."
    scene ch4sc19_421 with dissolve
    uk "I'd better get home before Father discovers I’m out past curfew... well past."
    stop music fadeout 2.0
    uk "Last time it happened, I had to do all the chores by myself for a week..."
    #stop music fadeout 2.0
    play music darknight_4 fadein 2.0
    scene ch4sc19_422 with dissolve
    with vpunch
    uk "*Muffled* Mhhhhh!! Mmmhpfff!"
    el "I’m really sorry... I just need a quick bite."
    scene ch4sc19_423 with dissolve
    with vpunch
    $ renpy.pause()
    uk "Muffled* Hhnnghhh! Hhhmmh!"
    scene ch4sc19_424 with dissolve
    $ renpy.pause()
    elt "Mhm... Sho ghood... Mmhm! M-More..."
    scene ch4sc19_425 with dissolve

    ##### CHOICE #####
    menu:
        "Guide her to control. ({color=#87e1fa}Light Path{/color})":
            scene ch4sc19_425 with dissolve
            mc "Eliza... You’ve had enough. If you continue, you'll kill her."
            mc "Remember, the goal is to control your feed and stop before the bloodlust sets in."
            mct "I have to be cautious here, a woman's life is at stake."
            mct "If I try to pull her off, she might snap the girl's neck in the process. The last thing she needs is an innocent life on her conscience."
            mct "I have to get through to her. Make her stop of her own accord... It’s the only way for her to learn control."
            scene ch4sc19_426 with dissolve
            mc "Eliza, I know you’re probably drowning in emotions right now, and the blood is making you forget everything else."
            mc "But you'll lose yourself like that. So just... focus on my voice. I’m right here with you."
            mc "Think of your favorite memory, the happiest one you can remember... and focus on that."
            scene ch4sc19_427 with dissolve
            el "..."
            el "[mc]..."
            scene ch4sc19_428 with dissolve
            el "Hhhaaaa..."
            scene ch4sc19_429 with dissolve
            el "I heard you. I actually heard you through the blood."
            el "I... I found you in the darkness."
            el "Did I do it? Did I stop in time?"
            scene ch4sc19_430 with dissolve
            mc "Yes. You did better than I expected. She's still breathing fine."
            el "What are you doing? Will she be okay?!"
            scene ch4sc19_431 with dissolve
            mc "It’s a new ability I learned when I was on Inmortui. I can mend fresh wounds."
            mc "I used it on Dalen after he cut himself to fill the chalice with his blood."
            el "Woah! [mc]... This is incredible! You’re healing her!"
            el "Then... I... I didn’t kill her?!"
            stop music fadeout 2.0
            #play music darknight_4 fadein 2.0
            scene black with Dissolve(1.5)
            scene ch4sc19_432 with dissolve
            #stop music fadeout 2.0
            play music forest_1 fadein 2.0
            mc "She’ll be fine. She just need to sleep it off."
            mc "She might wake up with one hell of a headache, though."
            el "Maybe... Maybe I really can do this? Be a vampire who doesn’t have to kill?"
            mc "As long as you maintain focus when you feed, and not give in to the bloodlust-"
            mc "Then... Yeah, I think it's possible."
            scene ch4sc19_433 with dissolve
            with vpunch
            el "*Squeals excitedly* Mhiyaah!"
            el "Thank you! Thank you so much for helping me!"
            el "This- This means I won't have to kill anyone!"
            mc "Of course. I’ll be with you every step of the way. We’re in this together."
            mc "I failed you the night you were turning... I should've been more attentive."
            $ light += 2
            "{color=#87e1fa}Light Morality{/color} increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            $ renpy.pause(1)

        "Encourage her to revel in it. ({color=#f00}Dark Path{/color})":
            scene ch4sc19_425 with dissolve
            $ el_blood = True
            mct "She'll never survive being a vampire if she doesn’t enjoy it."
            mct "She’s an apex predator now..."
            $ eldark += 1
            mct "Why should she feel bad for surviving? Does the wolf feel bad for the sheep?"
            mct "Does the lion apologize to the zebra? Does the eagle pity the hare? No. She should enjoy this."
            scene ch4sc19_426 with dissolve
            mc "I’m here with you. Just relax and drink up..."
            with vpunch
            el "*Bites harder* Hrrhhmm..."
            scene ch4sc19_427 with dissolve
            mc "Good girl... Take as much as you need."
            mc "Savor the taste..."
            scene ch4sc19_428 with dissolve
            el "More... So good... I want more..."
            scene ch4sc19_427 with dissolve
            with vpunch
            mc "Drink as much as you need... Empty her veins if need be."
            el "*Moans* Mmnhh! Mhmmm..."
            scene ch4sc19_428 with dissolve
            el "Haaahh... Delicious!"
            scene ch4sc19_429 with dissolve
            el "Do you want some?"
            mc "Pass."
            scene ch4sc19_428 with dissolve
            el "More for me then."
            scene ch4sc19_427 with dissolve
            el "Mmnhhh... Nnngh..."
            "She continues sucking on the girl’s neck until there’s nothing left."
            stop music fadeout 2.0
            #play music explore_2 fadein 2.0
            scene black with Dissolve(1.5)
            scene ch4sc19_430 with dissolve
            #stop music fadeout 2.0
            play music forest_1 fadein 1.0
            el "Is she dead?"
            mc "It seems so. Do you feel satisfied?"
            el "Mh-Hm. She was tasty..."
            scene ch4sc19_432 with dissolve
            mc "Good. I’m proud of you."
            el "R-Really? I did good?"
            mc "Yes. You’re top of the food chain... She is prey."
            el "Is it really okay that I killed her?"
            mc "Eliza, you're not human any more. Binding yourself to human morals will only bring you suffering."
            mc "Besides, humans kill each other constantly. Why should you be upset about it when you literally need to feed to survive?"
            el "When you put it like that... it seems, okay?"
            scene ch4sc19_433 with dissolve
            with vpunch
            el "I’m so happy! Yaay!"
            el "I couldn’t have done this without you! Thank you for guiding me through it!"
            $ dark += 2
            mc "I’ll be with you every step of the way, I promise."
            "{color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)
            $ renpy.pause(1)

    scene ch4sc19_434 with Dissolve(1.5)
    el "With you by my side... I feel like I can overcome this whole vampire thing."
    el "I thought I might not be any good at it... It seemed like such an insurmountable mountain to climb."
    scene ch4sc19_435 with dissolve
    mc "Luckily, you seem to be a good climber."
    scene ch4sc19_434 with dissolve
    el "I can’t take all the credit... I have a great climbing partner."
    scene ch4sc19_436 with dissolve
    el "..."
    scene ch4sc19_437 with dissolve
    el "What?"
    scene ch4sc19_436 with dissolve
    mc "Nothing... Just..."

    #### Choice ####
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc19_436 with dissolve
            mc "Come here, you little cutie."
            scene ch4sc19_438 with dissolve
            $ eliza_trust += 3
            "As your lips touch gently, you can taste the metallic traces of the blood on her lips."
            scene ch4sc19_439 with dissolve
            "But that doesn't stop either of you from enjoying each others lips."
            scene ch4sc19_440 with dissolve
            $ eliza_path = True
            el "MmpphH! Mmhhh..."
            "The taste of blood is quickly washed away by your co-mingled saliva."
            mct "She kisses me with such intimacy... It’s hard not to get addicted."
            scene ch4sc19_441 with dissolve
            mct "Who am I kidding? I am already addicted."
            elt "Nngh! I love how he grabs on to me when we kiss... It makes me feel so safe."
            scene ch4sc19_437 with dissolve
            el "Yum..."
            el "Take me home? Our bed is waiting for us."
            scene ch4sc19_436 with dissolve
            mc "That does sound inviting... Let's go."
            stop music fadeout 2.0
            #play music explore_2 fadein 2.0
            scene black with Dissolve(1.5)

        "Let’s get out of here. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc19_436 with dissolve
            $ eliza_path = False
            mc "Let’s get out of here before anyone comes by."
            scene ch4sc19_437 with dissolve
            el "Yeah... It’s been a long day. I can practically hear our bed screaming for us."
            stop music fadeout 2.0
            #play music explore_2 fadein 2.0
            scene black with Dissolve(1.5)

    scene black with dissolve
    $ renpy.pause(1)
    #stop music fadeout 2.0
    play music explore_1 fadein 2.0
    scene ch4sc19_442 with Dissolve(1.5)
    el "*Stretching* Finally. This bed has been calling me all day!"
    mc "You and me both... It’s been quite the day."
    scene ch4sc19_443 with dissolve
    el "I need to get out of these clothes... Tell me about your day?"
    scene ch4sc19_444 with dissolve
    mc "After I left the guild, I went to search the cells where Taron kept you."
    mc "I had to fight off a few of his thugs, but nothing major."
    el "Ugh! I still have nightmares about that place..."
    scene ch4sc19_443 with dissolve
    el "Did you encounter the old man that was in the cell with me?"
    mc "No. Are you sure you didn’t just imagine him because of the trauma?"
    scene ch4sc19_445 with dissolve
    el "I’m positive... He was there."
    el "He kept mumbling variations of the word 'wibble' ..."
    el "He might've been traumatized by something."
    scene ch4sc19_446 with dissolve
    el "*Continues undressing*"
    mc "Sounds like he was off his meds... Anyway, he wasn’t there."
    el "Shame... I'd like to help that old man, he must've been there for a reason..."
    mc "Maybe... somebody else was in the cells though."
    el "Oh? Another prisoner? Or one of his guards?"
    scene ch4sc19_447 with dissolve
    mc "Prisoner. A woman named Cassandra."
    el "Cassandra... Doesn’t ring a bell. I don’t think she was there at the same time as me."
    el "He really has a thing for locking up women, huh? *Angrily* Bastard..."
    mc "She's the leader of the mage’s guild here in Luxenford."
    scene ch4sc19_448 with dissolve
    with vpunch
    el "{b}WHAT?!{/b} A leader of a guild? Isn’t that insanely risky, even for him?"
    mc "Yes. He’s gotten careless... Something or someone must have him under a lot of pressure."
    scene ch4sc19_449 with dissolve
    mc "Which means he's bound to make mistakes. Eventually, that'll lead us to him."
    mc "Holding a guild leader prisoner is bound to get noticed. She'll be able to identify him easily."
    mc "I can only assume that means he doesn’t intend to let her live."
    scene ch4sc19_450 with dissolve
    el "Good thing you got her out of there then!"
    scene ch4sc19_451 with dissolve
    mc "About that... I didn’t free her."
    scene ch4sc19_452 with dissolve
    el "What?! Why would you just leave her there to rot? Do you have any idea how it feels to be kept in that place?"
    mc "Eliza..."
    el "Those cold, murky cells... They’re disgusting! Inhumane! We need to go get her right now!"
    scene ch4sc19_451 with dissolve
    with vpunch
    mc "{b}ELIZA!!{/b} Listen for a second."
    mc "If I could’ve gotten her out, I would have. But Taron had a mage cast a hex on her."
    mc "Apparently, if she leaves, it'll use her own mana as a bomb and destroy her from the inside."
    scene ch4sc19_453 with dissolve
    el "W-What?? That’s horrible... We have to do something."
    mc "I am. Cassandra asked me to find her daughter, Luna."
    scene ch4sc19_454 with dissolve
    el "Luna... Luna... Hmh."
    el "Alice has a friend at the academy with that name."
    mc "That would be the one."
    scene ch4sc19_455 with dissolve
    el "You already found her?"
    scene ch4sc19_456 with dissolve
    mc "I did. Taron has been forcing her to try to lift a curse from a blade of ancient origin..."
    mc "He's using her mother as leverage to keep her obedient."
    mc "Clearly, Taron values it highly enough that he's willing to go to extremes for it."
    scene ch4sc19_455 with dissolve
    el "Geez! You weren't kidding about having had a busy day..."
    scene ch4sc19_456 with dissolve
    mct "Telling her about Onyx could be risky. If the wrong person gets wind of it... everyone involved is at risk."
    mct "She already has a lot on her plate right now. Do I really want to add more on top of it?"
    scene ch4sc19_458 with dissolve
    el "Spill it. Whatever it is you're thinking so hard about... just tell me."
    scene ch4sc19_456 with dissolve
    mct "Heh... Observant as ever."
    mct "We agreed we'd never keep each other in the dark... I don’t intend to start now."
    mct "Eliza is the one person I'd trust with anything."
    scene ch4sc19_457 with dissolve
    mc "I offered to help Luna lift the curse while she and Alice search for a way to break the hex on Cassandra."
    mc "But after Luna left... I managed to break the curse on the blade without her."
    mc "And it turned out not to be a blade at all. The curse was a seal to lock Onyx in stasis in her blade form."
    scene ch4sc19_458 with dissolve
    el "Onyx?"
    scene ch4sc19_457 with dissolve
    mc "Onyx is the blade- Well, actually, she's something called a 'Symbiote'."
    mc "She has the ability to change shapes."
    scene ch4sc19_458 with dissolve
    el "What’s a sym... symbiote?"
    scene ch4sc19_457 with dissolve
    mc "A symbiote is one of three subspecies of morphlings. The other two kinds are slimes and oozelings."
    mc "They each have their own characteristics and abilities, but I don’t know too much about them."
    scene ch4sc19_455 with dissolve
    el "What did you do with it?"
    el "I haven’t seen you carrying around a sword or anything?"
    scene ch4sc19_457 with dissolve
    mc "Symbiotes need a host to survive."
    mc "So... I offered-"
    scene ch4sc19_459 with dissolve
    with vpunch
    el "You didn’t!"
    el "Please tell me you didn’t do something so reckless?!"
    scene ch4sc19_460 with dissolve
    mc "*Heavy sigh* I did... Just hear me out."
    el "*Groans in protest* Hrrrhnh..."
    mc "Taron wants Onyx... very badly. Obviously that filth should never be allowed to get anything he wants."
    mc "A symbiote like Onyx is both incredibly rare and very powerful."
    mc "I couldn’t risk Taron somehow getting his hands on her."
    mc "The only way to ensure that he'd never be able to possess her was to bond with her."
    scene ch4sc19_461 with dissolve
    el "Bond...? What does that mean?"
    scene ch4sc19_460 with dissolve
    mc "As I said earlier, a symbiote needs a host to survive. She's basically feeding on my mana."
    mc "Normally the constant drain kills the host over time. But since I can regenerate my mana, I can counteract the effects of her feeding."
    mc "Which means we'll be able to maintain the state of symbiosis permanently. Thus, she's now out of Taron’s reach."
    scene ch4sc19_461 with dissolve
    el "I don’t fully understand. Is she... part of you? Can she hear us right now?"
    scene ch4sc19_462 with dissolve
    mc "She is part of me. We merged... I absorbed her. But she can’t hear or see anything."
    mc "She's lying dormant inside me. I have to choose to activate her by infusing her with some of my mana."
    scene ch4sc19_461 with dissolve
    el "I... I understand. I don’t particularly like it... But I understand why it had to be done."
    scene ch4sc19_460 with dissolve
    mc "This has to stay between us. Anyone who knows will be in danger."
    scene ch4sc19_461 with dissolve
    el "My lips are sealed."
    scene ch4sc19_463 with dissolve
    elt "It really shows how much he trusts me. He could’ve easily kept quiet, thinking that he was ‘protecting’ me."
    elt "Instead, he told me the truth. He actually respects me."
    scene ch4sc19_464 with dissolve
    el "Hnnngh!"
    el "..."
    el "Hnnghhghh!!"
    mct "*Chuckles* Now that’s cute. She’s pretending to have trouble with her shirt..."
    scene ch4sc19_465 with dissolve
    mct "I’ll never understand how that old man Oren could've created something so beautiful..."
    mct "Her mother’s genes must be the dominant ones."
    scene ch4sc19_466 with dissolve
    el "*Ahem* Could you...?"
    mc "Right..."
    "You walk up close behind her."
    scene ch4sc19_467 with dissolve
    $ renpy.pause()
    mc "Let’s get this thing off you."
    mc "Lift up your arms."
    scene ch4sc19_468 with dissolve
    el "Like this?"
    mct "I can feel her ass pressing against me. As long as she doesn’t move..."
    mc "Just like that, yeah. It should come right off."
    scene ch4sc19_469 with dissolve
    el "I feel vulnerable like this... Yet safe with you this close..."
    scene ch4sc19_468 with dissolve
    mct "She’s moving her ass slightly. Brushing against my..."
    scene ch4sc19_469 with dissolve
    elt "Is that his...? Oh! It definitely is!"
    "You grab the hem of her shirt and gently pull it off her."
    scene ch4sc19_470 with dissolve
    el "Thank you..."
    el "..."
    scene ch4sc19_471 with dissolve
    elt "Oh? He’s still holding on to me?"
    scene ch4sc19_470 with dissolve
    el "Your hands... They’re warm as usual..."
    scene ch4sc19_471 with dissolve
    mc "Your skin is delicate. Just like I remember. Smooth like the finest silk sheets in a royal palace..."
    scene ch4sc19_470 with dissolve
    el "*Giggles* Been visiting the royal bedroom, have you?"
    scene ch4sc19_471 with dissolve
    mc "Not exactly... But I’ve got a good imagination."
    scene ch4sc19_470 with dissolve
    el "I certainly appreciate the compliment, but I don’t think my skin is a match for expensive silk sheets..."
    scene ch4sc19_472 with dissolve
    mc "You have no idea how wrong you are. Your skin is perfection."
    el "*Sighs heavily* [mc]... I..."
    scene ch4sc19_473 with dissolve
    mc "Your full, shapely hips... Your tight, smooth stomach..."
    el "Ohh... [mc]... Hnnh..."
    scene ch4sc19_474 with dissolve
    el "My body feels overly sensitive in your hands... Like every fiber of my being is ignited..."
    #### Choice ####
    menu:
        "Kiss her shoulder. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc19_475 with dissolve
            stop music fadeout 1.0
            #play music explore_2 fadein 2.0
            $ eliza_path = True
            $ renpy.pause()
            #stop music fadeout 2.0
            play music lewd_1 fadein 2.0
            el "*Whimpers* MnnHh!"
            scene ch4sc19_477 with dissolve
            elt "His lips feel amazing..."
            mct "Her scent really is something else... I can even taste it."
            scene ch4sc19_478 with dissolve
            elt "H-Holy fuck!! He’s sucking on my neck..."
            elt "I-... I-I thought I was the vampire. Nnnghh!"
            scene ch4sc19_479 with dissolve
            "Eliza grabs her breast instinctively, gently rubbing her nipple with her thumb as you enjoy the taste of her neck."
            scene ch4sc19_478 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_479 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_478 with dissolve
            elt "Mmmmm. If he keeps this up... Nnnghh..."
            scene ch4sc19_479 with dissolve
            mct "I can’t get enough of this girl. She’s everything I could ever want in a woman."
            mct "Leaving her on her own for two months... I'd love to go back and smack myself across my noggin."
            el "*Moans* Mmhhmm..."
            scene ch4sc19_478 with dissolve
            mct "She’s been grinding her ass against my crotch more intensely since I started kissing her neck."
            scene ch4sc19_479 with dissolve
            el "*Moans* NnghhH... Nnh! Mmmmm!"
            scene ch4sc19_480 with dissolve
            with vpunch
            $ renpy.pause()
            el "Mnnhh..."
            mct "Damn... The way she just grabbed my neck so powerfully. If I were a human, I'd be dead."
            scene ch4sc19_481 with dissolve
            el "*Kissing intensely* Ahhhhmm... Mnnghhh..."
            scene ch4sc19_480 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_481 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_480 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_481 with dissolve
            mct "Her kisses feel different suddenly. She feels more... raw. Untamed. Her lust is taking over."
            mct "Her vampirism magnifies her emotions and she's having trouble containing herself."
            scene ch4sc19_480 with dissolve
            mct "I can’t believe I’m thinking this... but I have to stop her. If we keep going..."
            mct "She'll lose her virginity right now, while she's caught up in the moment."
            mct "I know her well enough to know that she'd regret losing her virginity that way."
            scene ch4sc19_482 with dissolve
            mc "Eliza... We need to stop."
            el "{b}NO!!{/b}"
            scene ch4sc19_481 with dissolve
            with vpunch
            el "*Kiss* Mhhnm..."
            scene ch4sc19_482 with dissolve
            mc "Stop it. If we keep going, we’ll make a mistake that we can’t undo."
            el "I don’t care... Let’s make a mistake! Let’s make lots of them... Just kiss me!"
            scene ch4sc19_481 with dissolve
            el "*Grip tightens* Mmnhhh ... Nnnghh!"
            scene ch4sc19_482 with dissolve
            mc "Eliza... enough."
            el "Don’t you want me? Aren’t you attracted to me? Why do we need to hold back?"
            scene ch4sc19_481 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_480 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_481 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_482 with dissolve
            mc "Stop-"
            stop music fadeout 1.0
            #play music explore_2 fadein 2.0
            scene ch4sc19_483 with dissolve
            with vpunch
            #stop music fadeout 1.0
            play music darknight_1 fadein 2.0
            mc "I said stop!"
            mc "We are not doing this. Not now."
            el "Y-You... don’t like me?"
            "She soon realizes what she is attempting and abruptly comes to her senses."
            scene ch4sc19_484 with dissolve
            el "*Shaky voice* W-What am I doing? No... No! I’ve ruined everything..."
            el "What was I thinking?! This can’t be me! [mc]! Why am I like this?"
            scene ch4sc19_485 with dissolve
            mc "Hey, it's okay. Nothing bad happened. You just lost control for a moment."
            mc "I don’t blame you, we both knew this would take some serious adjusting to."
            scene ch4sc19_484 with dissolve
            el "No! It’s not okay... I’m disgusting! I forced myself on you. L-Let go of me!"
            scene ch4sc19_486 with dissolve
            with vpunch
            "She breaks free of your arms, grabs her shirt and rushes towards the door."
            mc "Eliza!"
            scene ch4sc19_487 with dissolve
            mct "She can’t run away from this. It's part of her now. She needs to be able to take control of her emotions."
            scene ch4sc19_488 with dissolve
            with vpunch
            el "W-What are you doing? ... Let me go!"
            mc "No."
            mc "You’re not leaving the room in this state."
            scene ch4sc19_489 with dissolve
            mc "Especially not dressed like that."
            scene ch4sc19_490 with dissolve
            el "Urgh! You’re such a jerk!"
            scene ch4sc19_491 with dissolve
            el "A big dummy jerk!"
            scene ch4sc19_490 with dissolve
            mc "Go on, let it all out."
            scene ch4sc19_491 with dissolve
            with vpunch
            el "*Sobs* Y-You! {b}YOU LEFT ME!!{/b}"
            mct "I had a feeling this was something she'd been keeping suppressed."
            mct "She needs to let it all out."
            scene ch4sc19_490 with dissolve
            el "You left me all alone! And now... Now, I’m like this! Ruining the moments I’ve been longing for so deeply!"
            mc "You’re not ruining anything."
            scene ch4sc19_491 with dissolve
            el "Jerk!"
            el "I was sick for an entire week when you left! I couldn’t keep any food down!"
            mct "Woah... I didn't realize that my leaving had taken such a big toll on her. I’m such an idiot."
            scene ch4sc19_490 with dissolve
            el "*Sobs* Both of them! Mother... Father... They both left me... their child!"
            el "And then you-"
            scene ch4sc19_492 with dissolve
            "You know exactly what she is about to say and you don’t let her finish, instead you hug her firmly."
            stop music fadeout 1.0
            #play music darknight_1 fadein 2.0
            mc "I’m sorry."
            mc "I shouldn’t have left... I was just so angry... and ashamed."
            #stop music fadeout 1.0
            play music relax_2 fadein 2.0
            el "Why...?"
            mc "I failed you. I failed Oren. I’m supposed to protect you, but you got badly hurt."
            scene ch4sc19_493 with dissolve
            mc "I had to act."
            mc "I had to focus on doing... something. Helping you walk again was all I could latch onto."
            scene ch4sc19_492 with dissolve
            mc "I didn’t think, Eliza. I didn’t realize how much it would affect you."
            el "You really are a dummy. Don’t you know how much I-... I love you."
            scene ch4sc19_494 with dissolve
            mc "I love you too."
            scene ch4sc19_495 with dissolve
            el "To the moon and back, right?"
            scene ch4sc19_494 with dissolve
            mc "To all the moons and back."
            scene ch4sc19_495 with dissolve
            el "*Giggles* All the moons?"
            scene ch4sc19_494 with dissolve
            mc "Yeah... Just to be sure."
            scene ch4sc19_495 with dissolve
            el "Mnnh... I like that."
            el "[mc]?"
            scene ch4sc19_494 with dissolve
            mc "Mh?"
            scene ch4sc19_495 with dissolve
            el "Thank you. I needed this."
            el "I don’t know what got into me... but you've managed to calm me."
            scene ch4sc19_494 with dissolve
            mc "You lost control of your emotions and you were holding back some pent-up feelings."
            mc "I'd never hold that against you. Besides, I caused them."
            el "Mh-Hm..."
            scene ch4sc19_496 with dissolve
            with vpunch
            el "*Laughs* Aiiiih!! H-Hey! What are you doing?!"
            mc "I’m taking my moonkitten to bed."
            scene ch4sc19_497 with dissolve
            el "*Giggles* Moonkitten? P-Put me down right now you... you brute!"
            mc "Oh? You want to be put down?"
            scene ch4sc19_498 with dissolve
            with vpunch
            el "{b}*Squeals*{/b} Aiihh!!"
            el "This is not what I meant!"
            mc "We’re almost there."
            scene ch4sc19_499 with dissolve
            el "If you drop me, I’m not forgiving you for... at least two days!"
            el "You hear me?! {b}TWO DAYS!{/b}"
            mc "Two days? We can’t have that."
            scene ch4sc19_500 with dissolve
            mc "Would you look at that. We’ve arrived at our destination."
            el "[mc]! Don’t you dare!"
            mc "I wouldn’t dream of doing- Oh you mean this!"
            scene ch4sc19_501 with dissolve
            with vpunch
            el "{b}*Squeals*{/b} Aiiiyhh!"
            el "{b}OH!{/b} It’s on!"
            mct "By all the gods... I’ve missed seeing her like this. Playful and... naked."
            scene ch4sc19_502 with dissolve
            mct "Her mesmerizing breasts... Perky... Supple... Soft... Mh."
            scene ch4sc19_503 with dissolve
            mct "Her smooth, toned stomach... Leading the way from her breasts down to her legs."
            scene ch4sc19_504 with dissolve
            mct "And what legs she has... Soft, warm, shapely thighs..."
            scene ch4sc19_505 with dissolve
            mct "Her cute little feet... She’s always been playful with them, brushing them against mine under the covers."
            scene ch4sc19_506 with dissolve
            mct "And there we have it... Her curvy, peachy ass... Enough to fill both my hands and then some."
            mct "There’s not a single doubt in my mind that the divines themselves have blessed her."
            scene ch4sc19_507 with dissolve
            el "*Giggles*"
            stop music fadeout 1.0
            #play music relax_2 fadein 2.0
            scene ch4sc19_508 with dissolve
            #stop music fadeout 1.0
            play music lewd_1 fadein 2.0
            el "Seeing something you like?"
            scene ch4sc19_507 with dissolve
            mc "You have no idea..."
            scene ch4sc19_508 with dissolve
            el "Then why don’t you... come get it?"
            scene ch4sc19_507 with dissolve
            mct "I'd almost forgotten what a little temptress she can be..."
            mct "It'd be a sin to decline her invitation."
            scene ch4sc19_509 with dissolve
            elt "Gods... I love when he takes his shirt off."
            mc "Do you have any idea how beautiful you are?"
            elt "I love when he compliments me... I feel all giddy inside..."
            scene ch4sc19_510 with dissolve
            "As you approach the bed, she shifts and places her foot on your abs."
            el "Uh-Uh. Not so fast."
            mc "*Chuckles* What? I can’t get in our bed?"
            el "You can... But it requires a sacrifice!"
            scene ch4sc19_511 with dissolve
            mc "A sacrifice?"
            scene ch4sc19_512 with dissolve
            el "Uh-huh! A sacrifice of the highest value!"
            scene ch4sc19_511 with dissolve
            mc "Alright... I’ll play along. What must I sacrifice?"
            el "..."
            scene ch4sc19_513 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_511 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_513 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_512 with dissolve
            el "Your pants."
            scene ch4sc19_511 with dissolve
            mc "I knew you’d say that."
            scene ch4sc19_512 with dissolve
            el "How so?"
            scene ch4sc19_513 with dissolve
            el "..."
            scene ch4sc19_514 with dissolve
            with vpunch
            mc "Cause I know what a naughty little thing you are!"
            el "*Laughing* Ahiiyh!! It tickles!"
            el "*Soft moan* Mnnh! [mc]... You’re squishing my breast... Ahhnngh..."
            mc "Sounds to me like you’re enjoying having your perky breasts squished against me."
            el "Mmhph... No... I don’t- Ahhh... Enjoy thi- Ohhh... at all."
            scene ch4sc19_515 with dissolve
            mc "So you’re not loving how it feels when my lips nuzzle your neck? *Kiss*"
            el "*Moans* Oohmhmmhh... N-No ..."
            mct "Heh... She’s so cute when she’s trying to play hard to get..."
            mct "Let’s see how long she can keep it up."
            scene ch4sc19_516 with dissolve
            mc "So, you’re saying... lying together naked... pressing against each other like this... it doesn't effect you?"
            el "*Moans* Nhho... Nhot at ahll... *Moans* I’m ahh... sweet girl... Mmhh!"
            el "You’re bad for Ahh... trying to corrupt my innocence... MMhh."
            scene ch4sc19_517 with dissolve
            mc "So, me whispering in your ear... it doesn’t quicken your pulse?"
            mc "*Whispers* Me telling you how many nights I’ve lain awake thinking about this moment..."
            scene ch4sc19_518 with dissolve
            el "*Moans* Mmnhhh..."
            scene ch4sc19_517 with dissolve
            mc "*Whispers* How much I’ve longed to be in this bed with you again..."
            mc "*Whispers* How it just takes one whiff of your scent to make me rock hard..."
            scene ch4sc19_518 with dissolve
            el "*Moans* Nnngh! Ahh... [mc]..."
            scene ch4sc19_517 with dissolve
            mc "*Whispers* How seeing you naked stirs untamed emotions inside me..."
            scene ch4sc19_518 with dissolve
            el "*Moans* Ohhh [mc] ... Mmnhh!"
            scene ch4sc19_517 with dissolve
            mc "*Whispers* Every inch of your naked body isn’t tingling? Craving to be touched by me, your lion."
            scene ch4sc19_518 with dissolve
            el "*Pleading moan* [mc]... Nnhhh..."
            el "*Moans* Mmnhh! N-No more... Nngh... Kiss me!"
            scene ch4sc19_519 with dissolve
            el "*Mwah* Mnnhh..."
            "Her resistance completely melts away as your lips touch."
            "The sound of her whimpering moans fill your room as you keep her sensitive breasts squished together."
            #####ANIMATION#####
            show el_kiss11 with fade
            $ renpy.pause(1, hard=True)
            $ renpy.pause()
            el "*Soft moan* Mnnhh... Hhnn..."
            mct "I can feel her heartbeat through her breast... Her pulse is wild..."
            mct "I must’ve really turned her on... Hell, it even turned me on..."
            mct "I’ve been instinctively pressing my cock against her leg this entire time."
            el "*Kiss* Mnhhh... *Lick* Nnnhh... Mnhh!"
            scene ch4sc19_519 with dissolve
            elt "*Mwaah* He’s so hard! *Muah* I love feeling him close against me."
            scene ch4sc19_518 with dissolve
            mc "*Whispers* I knew you wouldn’t last long."
            scene ch4sc19_517 with dissolve
            el "*Whimpers* Nnghh... Not fair... You’re Ahhnn..."
            scene ch4sc19_518 with dissolve
            mc "*Whispers* I’m...? Say it."
            scene ch4sc19_517 with dissolve
            el "*Heavy breathing* Y-You’re Mmhh... my lion."
            scene ch4sc19_519 with dissolve
            el "*Kiss* Mh ..."
            scene ch4sc19_520 with dissolve
            el "*Lick* Hhnnh..."
            mct "Gods... grant me strength. Her tongue is definitely my greatest weakness..."
            scene ch4sc19_521 with dissolve
            el "*Licks passionately* NNhh... Mh-Mh! *Lick*"
            scene ch4sc19_520 with dissolve
            mct "I’m inhaling her scent with every breath... Tasting her with the slightest movement of our tongues..."
            scene ch4sc19_521 with dissolve
            el "*Licks* Mhh..."
            scene ch4sc19_520 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_519 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_520 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_521 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_520 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_519 with dissolve
            $ renpy.pause(1)
            scene ch4sc19_518 with dissolve
            el "[mc]... If you don’t stop... I’ll lose control again."
            scene ch4sc19_516 with dissolve
            el "Please... I... I can’t take it much longer... Feeling you press against me is torture right now..."
            scene ch4sc19_515 with dissolve
            mc "*Whispers* Torture, huh?"
            el "*Soft moan* Hnnghh... You know- Mmhh... what I mean."
            mct "As much as I want to continue this... I don’t want to push her over the edge."
            mct "She’s already been through a rollercoaster of emotions today."
            scene ch4sc19_517 with dissolve
            mc "*Whispers* You’re off the hook... for now."
            scene ch4sc19_519 with dissolve
            "She turns her head and locks lips with you, sucking gently a few times before she moves out from under you."
            stop music fadeout 1.0
            #play music relax_2 fadein 2.0
            scene black with Dissolve(1.5)

        "Snap out of it. ({color=#2bff8b}Friendship{/color})":
            scene ch4sc19_474 with dissolve
            $ eliza_path = False
            mc "Sorry. I got caught up in the moment... Let’s get into bed."
            el "............"
            el "*Sighs heavily* Okay..."
            stop music fadeout 1.0
            #play music relax_2 fadein 2.0
            scene black with Dissolve(1.5)

    scene ch4sc19_522 with Dissolve(1.5)
    el "This!"
    #stop music fadeout 1.0
    play music forest_1 fadein 2.0
    mc "Hmm?"
    el "I’ve been looking forward to this all day."
    scene ch4sc19_523 with dissolve
    mc "I’m spoiling you too much... I should be whipping you into shape."
    scene ch4sc19_522 with dissolve
    el "Luckily, I'm already in shape. So... spoil away!"
    scene ch4sc19_523 with dissolve
    mc "*Chuckles*"
    mc "Hey, what's that scroll on your nightstand?"
    scene ch4sc19_524 with dissolve
    el "Oh, that? It’s... a surprise!"
    mc "Now I’m curious... Tell me?"
    scene ch4sc19_522 with dissolve
    el "Too bad! You’ll have to wait!"
    scene ch4sc19_523 with dissolve
    mc "I hate waiting... makes me anxious."
    scene ch4sc19_522 with dissolve
    el "Nice try! My lips are sealed! It’s a surprise for you... Telling you would make it less exciting!"
    el "There’s absolutely no way that you’ll get it out of me- {b}Eeeeeeee!!{/b}"
    scene ch4sc19_525 with dissolve
    with vpunch
    mc "Sorry, what were you saying? I didn’t quite catch that!"
    el "{b}*Laughing* Hahahah! N-No! Stop!!{/b}"
    scene ch4sc19_526 with dissolve
    mc "All you have to do is tell me what the scroll is."
    scene ch4sc19_525 with dissolve
    el "{b}*Laughing* NhooO! Hahahh! Hands off my butt! It tickles!{/b}"
    scene ch4sc19_526 with dissolve
    mc "You mean this perky little thing is ticklish?"
    scene ch4sc19_525 with dissolve
    with vpunch
    el "{b}*Squeals* Aiyyeee! SHTOOPP! Mercy! Hahahhhhaha!{/b}"
    el "I’ll tell you everything! I promise!"
    scene ch4sc19_526 with dissolve
    mc "That’s more like it."
    "You grab her by the hips and pull her back into the bed."
    scene ch4sc19_527 with dissolve
    el "You’re very hands-on today."
    scene ch4sc19_528 with dissolve
    mc "Sorry, I got a little carried away."
    scene ch4sc19_527 with dissolve
    el "If you ever apologize for touching me again, I’ll... I’ll be really mad! No! Furious even!"
    scene ch4sc19_528 with dissolve
    mct "Heh... This little cutie."
    mc "Noted. So what’s that scroll about?"
    scene ch4sc19_529 with dissolve
    el "*Sigh* I promised, didn't I?"
    mc "Yes, and there’s no take-backs."
    scene ch4sc19_530 with dissolve
    el "Okay. So, the scroll used to belong to Dalen. He got it as a reward when he graduated with honors from the academy."
    el "You remember when we talked before you left? About having a dream that goes beyond our revenge?"
    scene ch4sc19_531 with dissolve
    mc "I do. Finding a place to call... home."
    scene ch4sc19_532 with dissolve
    el "That’s what that scroll is. Home... our home."
    scene ch4sc19_530 with dissolve
    el "Dalen wanted me to have it. He says I’ve earned it and that he doesn’t have a need for it..."
    el "But that’s a cover... I think he feels guilty about drifting apart from Father after they graduated."
    scene ch4sc19_532 with dissolve
    el "And that he wasn’t there for me when Father left. Or when Mother left..."
    scene ch4sc19_530 with dissolve
    el "Even though he doesn’t have to feel guilty about something that was out of his control."
    el "He couldn’t have known about any of that. *Sigh* But he looked happy when I accepted it."
    scene ch4sc19_531 with dissolve
    mc "What is it? You call it home, but it’s just a scroll."
    scene ch4sc19_533 with dissolve
    el "It isn’t just a scroll! It’s the deed to a piece of land not far from here."
    el "Dalen said it doesn’t have any buildings yet. It's completely untouched."
    scene ch4sc19_531 with dissolve
    mc "No buildings?"
    scene ch4sc19_533 with dissolve
    el "Yeah, so it will be up to the two of us to gather materials and make something out of it."
    el "Make it ours."
    scene ch4sc19_531 with dissolve
    mc "Eliza... that’s amazing. You really keep surprising me."
    mc "Dalen mentioned how hard you’ve been working, managing the guild with Sylph."
    scene ch4sc19_533 with dissolve
    el "Oh, I didn’t do much. They give me too much credit."
    scene ch4sc19_531 with dissolve
    mc "I don’t believe that for even a second..."
    mc "I’m proud of you."
    scene ch4sc19_534 with dissolve
    el "..."
    elt "I did it all for you..."
    scene ch4sc19_535 with dissolve
    elt "I love you so much."
    scene ch4sc19_536 with dissolve
    el "*Sighs heavily* We'd better get some rest."
    "After a quick shuffle, Eliza makes herself comfortable."
    scene black with Dissolve(1.5)
    scene ch4sc19_537 with Dissolve(1.5)
    el "Ahhhh... Yes! I’ve been looking forward to this! *Giggles*"
    el "My favorite heated pillow and head-scratches!"
    scene ch4sc19_538 with dissolve
    mc "*Chuckles* You know this is a two-person bed?"
    scene ch4sc19_537 with dissolve
    el "Mh-Hm. I fail to see your point."
    scene ch4sc19_538 with dissolve
    mc "My point is, maybe you could-"
    scene ch4sc19_537 with dissolve
    el "If you finish that sentence, I’ll have an extra large bucket of cold water waiting for you in the morning."
    mct "*Sigh* I guess I’ll take the sleeping arm then... Women!"
    scene ch4sc19_538 with dissolve
    mc "My side of the bed it is..."
    scene ch4sc19_537 with dissolve
    el "Wise choice! Mhhh..."
    el "Your side is so much more comfortable! It’s warm... and somehow smells like... timber?"
    el "Why do you smell like that? I’ve never seen you chop wood!"
    scene ch4sc19_538 with dissolve
    mc "*Chuckles* How should I know? It’s just my scent."
    scene ch4sc19_537 with dissolve
    el "*Giggles* I like it! And I especially like your head scratches, Mhhhh..."
    el "Mhhh! Night, night!"
    mct "Heh. She sure loves her cuddle time..."
    scene ch4sc19_538 with dissolve
    stop music fadeout 1.0
    #play music forest_1 fadein 2.0
    mc "Goodnight."
    scene black with Dissolve(2)
    $ renpy.pause(0.5)
    scene ss39 with Dissolve(2)
    $ renpy.pause()
    scene ch4sc19_539 with Dissolve(2)
    $ renpy.pause(1)
    #stop music fadeout 1.0
    play music explore_2 fadein 2.0
    scene ch4sc19_540 with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_539 with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_540 with Dissolve(2)
    mc "*Groggy* Hnngh... Eliza?"
    scene ch4sc19_541 with dissolve
    el "Wakey, wakey, eggs and bakey!"
    scene ch4sc19_539 with dissolve
    mc "Urhh... Is the sun even up yet...?"
    scene ch4sc19_541 with dissolve
    el "It will be soon! Time to look alive!"
    scene ch4sc19_540 with dissolve
    mc "Wake me when it’s dawn, you little morning monster."

    if eliza_path == True:
        scene ch4sc19_541 with dissolve
        el "Morning monster? Would a monster do this?!"
        scene ch4sc19_542 with dissolve
        $ renpy.pause()
        scene ch4sc19_543 with dissolve
        el "*Muah* And this..."
        scene ch4sc19_542 with dissolve
        el "*Muah* Nnhhgh... *Mwah*"
        scene ch4sc19_543 with dissolve
        mc "*Laughing* H-Hey! Attacking an unsuspecting victim is exactly what a monster would do!"
        scene ch4sc19_542 with dissolve
        el "*Kiss* Nhooo! *Mwah* This is totally different! *Muah*"
        scene ch4sc19_543 with dissolve
        el "*Mwaahh* These are- *Kiss* attacks of- Hnnghhh... affection!"
        mct "Waking up with her is never boring... She’s grinding against me."
        scene ch4sc19_542 with dissolve
        mc "Okay, okay! I’m awake..."
        scene ch4sc19_541 with dissolve
        el "Better be! You can’t sleep all day, you big ol’ sleepyhead!"

    else:
        scene ch4sc19_541 with dissolve
        el "C’mon! We have to get up, sleepyhead!"

    scene ch4sc19_540 with dissolve
    mc "Ugh... What's the rush? I could use a day where we sleep til at least noon..."
    scene ch4sc19_541 with dissolve
    el "We’re going training! You always say I have to practice."
    scene ch4sc19_540 with dissolve
    mc "Sure... But does it have to be this early?"
    scene ch4sc19_541 with dissolve
    el "Yes. I’m excited!"
    scene ch4sc19_540 with dissolve
    mc "*Sigh* I couldn’t tell..."
    scene ch4sc19_541 with dissolve
    el "Let’s gooooo! Up and at 'em! *Giggles*"
    stop music fadeout 1.0
    #play music forest_1 fadein 2.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    #stop music fadeout 1.0
    play music forest_1 fadein 2.0
    scene ch4sc19_177 with Dissolve(2)
    el "*Nervous* How do you feel?"
    scene ch4sc19_178 with dissolve
    mc "Tired..."
    scene ch4sc19_176 with dissolve
    el "Nooo. Not what I was referring to, you snoozebean!"
    scene ch4sc19_177 with dissolve
    el "I meant... How do you feel about our deed? I know you said you're proud of me."
    el "But what do you think about the deed? Do you think we'll actually be able to make it happen?"
    scene ch4sc19_178 with dissolve
    mc "Eliza... You’re one of the strongest people I’ve ever met..."
    mc "There’s no obstacle that you won’t be able to overcome if you set your mind to it."
    mc "If it were just me? I wouldn’t bother with it... But for us? Creating a home together?"
    scene ch4sc19_176 with dissolve
    mc "I’m already looking forward to starting that project with you."
    el "Me too!"
    el "I feel like I’m going to burst whenever I think about it..."
    scene ch4sc19_177 with dissolve
    el "I’ve decided I’ll keep working with Sylph to manage the guild so we can save up for the materials."
    el "As much as I'd love to go exploring every day, face new challenges and such..."
    scene ch4sc19_175 with dissolve
    el "*Sigh* Sometimes you have to make sacrifices to make a dream come true."
    mc "That’s... very mature of you."
    mc "Did you somehow age ten years while I was away?"
    scene ch4sc19_176 with dissolve
    el "Silly... I just want to make this happen, very badly."
    mc "We will."
    scene ch4sc19_178 with dissolve
    mc "How about I promise to take you out on quests once in a while?"
    scene ch4sc19_178a with dissolve
    el "Mhm! I'd like that very much!"
    scene ch4sc19_178 with dissolve
    mc "*Sigh* Can’t believe I’m saying this... Get on."
    scene ch4sc19_178a with dissolve
    el "Y-You mean? {size=+10}{b}ACTUALLY?!{/b}{/size}"
    scene ch4sc19_179 with dissolve
    el "Before you have a chance to confirm, she jumps onto your back."
    mc "I’m going to start taking on more lucrative quests."
    mc "I won’t let you be the only one working on your-... on our dream."
    elt "He has no idea how happy it makes me to hear him say that. Our dream."
    scene ch4sc19_181 with dissolve
    mc "Okay, we’re here... Time to get off, you little monkey."
    el "*Sigh* Aww... I wish I could stay here all day!"
    mc "Right... Not happening."
    with vpunch
    el "Not even if I do this?"
    "She presses her breasts into your back and tightens her legs around your waist."
    mc "Nice try. But no."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.5
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    play music outdoors_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc19_183 with Dissolve(1)
    el "I kind of like this spot, actually. The highlands seem like such a peaceful landscape."
    mc "I know what you mean! I think I spotted some wild horses grazing last time we were here."
    el "I’m just going to stretch, then we can begin!"
    scene ch4sc19_184 with dissolve
    mct "Always with her stretching..."
    mct "Does it actually have any benefit?"
    scene ch4sc19_185 with dissolve
    el "Aren’t you going to join me?"
    scene ch4sc19_184 with dissolve
    mc "Pass."
    scene ch4sc19_185 with dissolve
    el "You know, one of these days I’ll convince you to!"
    scene ch4sc19_186 with dissolve
    el "Stretching is super healthy! It loosens up your limbs and joints and gets them ready for activity."
    mc "Is that how you've always been so nimble? Even when you were purely human."
    el "I'd like to think so!"
    scene ch4sc19_187 with dissolve
    mc "I won’t lie..."
    mc "It does seem to have certain... perks."
    scene ch4sc19_188 with dissolve
    el "These perks you’re talking about... Wouldn’t happen to be my breasts, would they?"
    scene ch4sc19_186 with dissolve
    mc "*Chuckles* No... Not ‘just’ your breasts."
    mc "Your cheeks are included in the perk package."
    el "*Giggles* Is that so? I guess they come as a bundle..."
    scene ch4sc19_188 with dissolve
    el "So, you’ll join me next time?"
    scene ch4sc19_187 with dissolve
    mc "Deal."
    scene ch4sc19_185 with dissolve
    el "Hnnngh! I’m done."
    scene ch4sc19_184 with dissolve
    mc "I’m surprised you didn’t attempt to sneak attack me this time."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.5
    scene ch4sc19_544 with dissolve
    el "Not today... I wanted to try something else."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.5
    el "You know how knights salute each other before they fight in tournaments?"
    mc "Yeah, I’ve heard they do it as a sign of respect for their opponent."
    scene ch4sc19_545 with dissolve
    el "I'd like us to have our own ‘salute’."
    scene ch4sc19_546 with dissolve
    mct "She’s stunning... The way her blue eyes light up..."
    mct "How her fair skin is enhanced by the morning sunlight ... How her hair is caught by the wind..."
    mct "If this is another attempt to sneak attack me... it'll work."
    scene ch4sc19_547 with dissolve
    mc "So, what did you have in mind? Knights usually bow, don’t they?"
    scene ch4sc19_548 with dissolve
    el "They do. But I have something better in mind for us."
    "You fully expect a surprise attack of sorts as she leans in towards you."

    if eliza_path == True:
        scene ch4sc19_549 with dissolve
        "*Mwah* She plants her soft lips onto yours for a gentle kiss."
        mct "I love how she tastes... Her lips are unbelievably soft."

    else:
        scene ch4sc19_549 with dissolve
        "She plants her lips on your cheek. *Muah*"

    scene ch4sc19_550 with dissolve
    el "How’s that for a salute?"
    scene ch4sc19_551 with dissolve
    mc "I think we’ll have to incorporate salutes for everything we do..."
    el "*Giggles* Maybe we should!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch4sc19_183 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "Let’s begin! No holding back. I want to push myself today."
    mc "You've got it."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.5
    mct "This could be a good opportunity to test out some of Onyx’s capabilities."
    scene ch4sc19_189 with dissolve
    with vpunch
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.5
    mct "Here she comes!"
    scene ch4sc19_190 with dissolve
    with vpunch
    mct "Damn!"
    mct "I almost didn’t block in time... She’s scarily quick."
    scene ch4sc19_191 with dissolve
    mct "Fuck! I’m wide open!"
    "Eliza doesn't hesitate to seize her oppotunity, she jumps up and twists mid-air."
    scene ch4sc19_192 with dissolve
    with vpunch
    mc "*Grunts* Hrrh! Onyx!"
    scene ch4sc19_552 with dissolve
    "As soon as you channel her, she cushions your landing."
    scene ch4sc19_553 with dissolve
    ox "Master! Are you okay?"
    mct "Yeah, thanks for the save."
    ox "If you die... I’ll lose my favorite host."
    scene ch4sc19_554 with dissolve
    mct "Right... Shit, here she comes again! Onyx be ready!"
    ox "Activating kill mode."
    scene ch4sc19_555 with dissolve
    with vpunch
    mct "What?! She’s not a real enemy, Onyx! Deactivate now!"
    ox "Loosen up, it was a joke Master! ... Sorta... {b}DODGE!{/b}"
    scene ch4sc19_556 with dissolve
    with vpunch
    "You barely manage to dodge her sweep."
    scene ch4sc19_557 with dissolve
    mct "Okay, Onyx... Let’s see what you’re capable of."
    ox "Anything Master! Just imagine it and I'll know what you need!"
    mct "I want her to be on the offense... Be ready to shield me."
    scene ch4sc19_190 with dissolve
    with vpunch
    $ renpy.pause(1.5)
    scene ch4sc19_558 with dissolve
    el "So you’re using Onyx? I saw that black goo that caught your landing."
    el "I won’t be holding back then."
    scene ch4sc19_559 with dissolve
    mc "Let’s see what you’ve got."
    scene ch4sc19_560 with dissolve
    with vpunch
    "She swiftly drops down into a low-kick."
    mc "*Grunts* Sneaky..."
    scene ch4sc19_561 with dissolve
    el "Ha! You’re done!"
    mct "Onyx, now!"
    scene ch4sc19_562 with dissolve
    with vpunch
    "Just as Eliza's fist is about to connect, Onyx erupts outwards and grasps Eliza tightly."
    el "*Grunts* Hnngh! {b}Euuuew!!{/b}"
    scene ch4sc19_563 with dissolve
    el "*Squeals* Aaayieeh! Get it off! {b}Euw! Eeeww!!{/b}"
    mct "Good work, Onyx. Let’s take her down!"
    scene ch4sc19_564 with dissolve
    with vpunch
    el "{b}*Screams*{/b} Aiiiyyhhh!!"
    #play music forest_1 fadein 1.0
    stop music fadeout 1.5
    scene ch4sc19_565 with dissolve
    with vpunch
    mc "Got you."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.5
    el "*Smirking* Oh yeah? Are you sure about that?"
    with vpunch
    "She squeezes you between her legs which are wrapped tightly around your waist."
    mc "Looks like we have a tie..."
    el "Nuh-uh. You’re at my mercy!"
    scene ch4sc19_566 with dissolve
    with vpunch
    "She swiftly rolls the two of you over."
    mc "*Laughing* Really?"
    el "Admit defeat!"
    with vpunch
    el "I’ve got you in my monkey death-grip! Your impending doom is near! *Squeeze*"
    mc "Is that so?"
    scene ch4sc19_567 with dissolve
    with vpunch
    mc "You manage to wiggle free from her grip and swiftly hold her up by her hips."
    el "Aiiiyh!! Meanie!"
    el "*Giggling* You’re not supposed to escape the death grip!"
    scene ch4sc19_568 with dissolve
    mc "I like this position better... Now you’re in my grip."
    el "*Giggling* This was my plan all along! I've got you exactly where I want you!"
    el "Now I can do this!"

    if eliza_path == True:
        scene ch4sc19_569 with dissolve
        "You feel the soft, wet sensation of her lips, a sensation you’ve become very familiar with."
        mct "She really loves kissing... She’s managed to make me look forward to each and every one of them."
        "She doesn't just settle for your cheek, she has a different target in mind."
        scene ch4sc19_570 with dissolve
        el "*Muah* Mnnhh... Shuurrender? *Kiss*"
        mc "Hnnh... *Kiss* Tempting... But no. *Kiss*"
        scene ch4sc19_571 with dissolve
        el "*Mwah* You’re- Mmhhh... So- *Kiss* Annhhoying!"
        scene ch4sc19_570 with dissolve
        el "*Mwah* Not to- Mmhhh... mention so-... *Kiss* Stubborn!"
        scene ch4sc19_571 with dissolve
        mc "*Kiss* You’ll have to- Mhhh... Try harder."


    else:
        scene ch4sc19_569 with dissolve
        "She plants her soft lips onto your cheek."
        el "*Mwaaah!*"


    scene ch4sc19_572 with dissolve
    el "She wiggles free from your grasp and lies on top of you."
    el "Surrender."
    mc "No."
    scene ch4sc19_573 with dissolve
    el "Then you leave me no choice... I’ll have to keep doing this!"

    if eliza_path == True:
        scene ch4sc19_574 with dissolve
        el "*Mwaah!*"
        scene ch4sc19_575 with dissolve
        "She swiftly moves further up and grabs the back of your head gently but firmly."
        with vpunch
        "Then pushes your face between her soft perky breasts."
        scene ch4sc19_576 with dissolve
        el "*Soft moan* Nnngh!! H-How you like that?"
        scene ch4sc19_575 with dissolve
        mc "*Muffled* Mmnhh! Mmhmmmm..."
        mct "So soft... So warm... They’re like perfectly cushioned pillows."
        scene ch4sc19_576 with dissolve
        el "*Soft moan* Ohhh... Mmhh! S-Surrender! Ahhnghh..."
        scene ch4sc19_575 with dissolve
        mct "F-Fuck... I can barely breathe, and what little air I can get is potent with her scent..."
        scene ch4sc19_576 with dissolve
        mct "I’m rock hard... The way she’s wiggling on top of me isn't helping."
        scene ch4sc19_575 with dissolve
        elt "Heavens! My-My breasts are so sensitive... I {b}love{/b} having him between them!"
        scene ch4sc19_576 with dissolve
        $ renpy.pause(1)
        scene ch4sc19_575 with dissolve
        $ renpy.pause(1)
        scene ch4sc19_576 with dissolve
        $ renpy.pause(1)
        scene ch4sc19_577 with dissolve
        el "*Soft moan* {b}NNghh! L-Last chance!{/b} AAhhh... D-Do... You... Want... To... Tap... Out."
        "You squeeze her peachy ass firmly, while she keeps you lodged between her breasts."
        with vpunch
        elt "Ahh! I love feeling his hands on me! Mmnhhh... If I keeps this up, I’ll be the one tapping out..."
        mct "I guess I’ll let her have this one..."
        "You gently tap her ass."
        scene ch4sc19_578 with dissolve
        $ renpy.pause(0.7)
        scene ch4sc19_577 with dissolve
        $ renpy.pause(0.7)
        scene ch4sc19_578 with dissolve
        $ renpy.pause(0.7)
        scene ch4sc19_577 with dissolve
        $ renpy.pause(0.7)
        scene ch4sc19_573 with dissolve
        el "*Giggling* I knew I’d win! Never even doubted it for a second!"
        scene ch4sc19_579 with dissolve
        mc "Yeah, right. Even if you'd kept your moans silent, which they weren't..."
        mc "I could feel them vibrating through your breasts."
        scene ch4sc19_580 with dissolve
        el "I couldn’t help it... You know how sensitive they are..."
        scene ch4sc19_579 with dissolve
        mc "Mh. That I do..."
        scene ch4sc19_580 with dissolve
        el "Did you enjoy it?"
        scene ch4sc19_579 with dissolve
        mc "I think we both know the answer to that..."
        scene ch4sc19_580 with dissolve
        el "Yeah... The answer is literally poking me right now..."
        scene ch4sc19_581 with dissolve
        el "I... *Sigh* I really want to do something about that, but you know..."
        scene ch4sc19_582 with dissolve
        mc "I know... You have desk duty at the guild."
        el "..."
        scene ch4sc19_581 with dissolve
        el "*Mumbles* Stuuupid desk duty..."
        el "You’re not mad at me?"
        scene ch4sc19_582 with dissolve
        mc "Mad at you? Don’t talk crazy..."
        scene ch4sc19_581 with dissolve
        el "But... I made you hard? And now we don’t even have time to do anything..."
        scene ch4sc19_582 with dissolve
        mct "Look at this little kitten... She’s upset that she can’t play with me."
        scene ch4sc19_579 with dissolve
        mc "Don’t worry, I’m not mad... I could never be mad at my moonkitten."
        scene ch4sc19_580 with dissolve
        el "*Happy* Uh-Uh! I-I’ll make it up to you later! I promise!"
        scene ch4sc19_583 with dissolve
        $ renpy.pause()
        el "*Kiss* Nnnghh... Mmmmmmmm... *Mwah*"
        scene black with Dissolve(1.5)

    else:
        scene ch4sc19_574 with dissolve
        "She continues kissing your cheeks."
        mc "*Chuckles* Alright, alright! You win!"
        scene black with Dissolve(1.5)

    scene black with dissolve
    "The two of you get yourself sorted and head back towards Luxenford."
    scene ch4sc19_176 with Dissolve(1.5)
    el "I feel like I’m getting the hang of my improved speed and strength."
    mc "You’re certainly putting up quite a fight... You’re actually managing to land some hits."
    scene ch4sc19_177 with dissolve
    el "You’re not just letting me?"
    scene ch4sc19_178 with dissolve
    mc "No. I have to actually try, otherwise you'd flatten me in a second."
    mc "You’re incredibly strong, a lot more than I anticipated at first."
    scene ch4sc19_175 with dissolve
    mc "Which is why you need to be cautious when you interact with others."
    el "Yeah. I could easily end up hurting someone... if I don’t pay attention-"
    el "Even a simple handshake, I could accidentally crush someone's hand. An excited hug could break their ribs..."
    scene ch4sc19_178 with dissolve
    mc "Exactly... So just be aware of it, and ease into those things until you get the hang of it."
    mc "You've already done a lot better today. You didn’t lose control during training."
    scene ch4sc19_178a with dissolve
    el "I did what you told me. Whenever I felt overwhelmed, I focused on my happiest memory."
    el "And luckily, I don’t have to worry about hurting you!"
    scene ch4sc19_178 with dissolve
    mc "Yeah... I can handle your excitement."
    scene ch4sc19_178b with dissolve
    with vpunch
    el "Praise the heavens for that!"
    el "'Cause I often feel excited when you’re around! *Giggles*"
    scene ch4sc19_178c with dissolve
    mc "*Grunts* Hnngh... Really? I couldn’t tell..."
    el "I’m good at hiding it!"
    "The two of you break out into laughter."
    scene ch4sc19_178d with dissolve
    with vpunch
    bth "*Laughing* Hhahhhhahah! Hahah-Hhaha!"
    #play music forest_1 fadein 1.0
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc19_224 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    el "Morning, Sylph! Morning, Milton!"
    scene ch4sc19_584 with dissolve
    ml "Good morning, miss Eliza!"
    sy "Morniiiing! Just in time, we’re about to open for the day!"
    scene ch4sc19_585 with dissolve
    el "Where’s Borri? Don’t tell me he’s still snoozing?"
    sy "Borri is already out on his quest. We’ve had a lot of smaller tasks and assignments, as you know."
    sy "Come help me back here Eliza, we have a bunch of stuff piled up!"
    scene ch4sc19_586 with dissolve
    ml "Hey, [mc]. It’s good to have you back."
    mc "Hey guar- Milton."
    mc "I’m glad we were able to help you out after that whole mess with your dismissal."
    scene ch4sc19_587 with dissolve
    sy "Come, come! I have many contracts for you to sort through!"
    mct "Is he checking them out?"
    mc "*Firmly* {b}HEY!{/b} Eyes up here buddy."
    scene ch4sc19_586 with dissolve
    ml "S-Sorry!!"
    ml "I-I didn’t mean anything by it!"
    scene ch4sc19_588 with dissolve
    el "Hmh? What are you guys up to?"
    scene ch4sc19_589 with dissolve
    mc "Just a little friendly banter, right Milton?"
    ml "R-Right! Just banter! It’s a guy thing."
    scene ch4sc19_588 with dissolve
    el "Okaaay... I’ll go help Sylph."
    el "You guys behave!"
    scene ch4sc19_589 with dissolve
    mc "Milton, Milton, Milton..."
    #### Choice ####
    menu:
        "Threaten him. ({color=#fc584c}Intimidation{/color})":
            scene ch4sc19_589 with dissolve
            mc "Stare at her ass again and even the gravekeeper won't know what happened to your body... We clear?"
            ml "Y-Yes! C-C-Crystal sir!"
            mc "Good. It’s been a while since I killed someone. Better not give me an excuse to scratch that itch."
            ml "I-I won’t! I-I-I’ll be on my best behavior!"
            mc "Good talk... Run along now."
            $ intimidation += 2
            "Milton took your threat seriously, your {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(1.5)

        "Convince him. ({color=#2bff8b}Persuasion{/color})":
            scene ch4sc19_589 with dissolve
            mc "Milton..."
            ml "S-Sorry... I just... She’s very beautiful."
            mc "I know... But she’s family. Do you understand me?"
            ml "Yes, I really didn’t mean to offend!"
            mc "Just think about how good she’s been to you, and how bad she will feel if you objectify her like that."
            ml "No! I didn’t! I mean, I don’t want miss Eliza to feel that way! I swear I'll avert my eyes!"
            $ persuasion += 2
            "You convinced Milton it was wrong to look at Eliza like that, your {b}{color=#2bff8b}Persuasion{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(1.5)

        "Teach him. ({color=#ffee54}Leadership{/color})":
            scene ch4sc19_589 with dissolve
            mc "Milton..."
            ml "S-Sorry..."
            ml "I just... She’s very beautiful."
            mc "*Scoffs* She is, but Eliza and Sylph are women of the adventurer's guild."
            mc "And what are we, Milton?"
            ml "M-Men of the adventurer's guild?"
            mc "And what is our role when it comes to our women?"
            ml "Protect them at all costs? Be it on adventures or right here in the city."
            ml "*Sighs* Oh... I see your point, I can't believe I looked at them like that!"
            $ leadership += 2
            mc "*Chuckles* It's alright, we men have simple minds, easily distracted at times..."
            "You taught Milton how to handle himself when it comes to guild members, your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."


    scene ch4sc19_590 with Dissolve(1.5)
    sy "Milton, don’t forget to visit the stables!"
    ml "Will do Sylph!"
    mct "Stables...? Selena?"
    scene ch4sc19_591 with dissolve
    mc "What’s going on at the stables, Sylph?"
    scene ch4sc19_592 with dissolve
    sy "We got word that the stablekeeper is missing, so we’re sending Milton to check it out."
    sy "It’ll be his first quest outside the city."
    mc "No it won’t. I’ll handle it..."
    scene ch4sc19_593 with dissolve
    sy "Uhh... sure? Just send Milton back for a new quest, then."
    mct "She looks worried..."
    scene ch4sc19_594 with dissolve
    el "I’ll go with you!"
    mc "No, I’m going alone. Besides you have desk-duty here."
    scene ch4sc19_595 with dissolve
    sy "Yuuup! He’s right, you can’t leave."
    el "I don’t like this. What if she’s there? Ugghh..."
    scene ch4sc19_591 with dissolve
    mc "If Selena is there, I'll handle it. I won’t be long."
    sy "[mc], can we talk later?"
    mc "Sure, we’ll talk later."
    scene ch4sc19_594 with dissolve
    el "I don’t like this... *Sigh* But okay. She’s definitely not a threat to you..."
    scene ch4sc19_596 with dissolve
    mc "Milton, hold up! Change of plans, you're not going to the stables now."
    ml "Oh? Alright!"

    if eliza_path == True:
        scene ch4sc19_240 with dissolve
        el "Not so fast! Aren’t you forgetting something..."
        scene ch4sc19_241 with dissolve
        el "MMmmmMMm..."
        mct "Heh this girl... Better give her what she wants."
        scene ch4sc19_242 with dissolve
        el "*Muuah!*"
        el "*Mwah* Nnnhh..."
        scene ch4sc19_243 with dissolve
        mc "One more..."
        scene ch4sc19_242 with dissolve
        el "*Muah* MMmmMm!"
        scene ch4sc19_243 with dissolve
        mc "A third for good measure..."
        scene ch4sc19_242 with dissolve
        el "*Mwaah* Mnnhh..."
        scene ch4sc19_243 with dissolve
        el "Hurry back and be safe..."
        scene ch4sc19_236 with dissolve
        mc "Keep a kiss ready for me when I return."
        el "*Blushing* I’ll have a few ready for you!"
        scene ch4sc19_237 with dissolve
        elt "Heavens... I can’t believe the butterflies I feel when he kisses me!"
        scene black with Dissolve(1.5)
        $ renpy.pause(1)


    else:
        scene ch4sc19_240 with dissolve
        el "Please, be careful and hurry back."
        scene ch4sc19_239 with dissolve
        mc "Will do. Make sure you have a proper quest for me when I return. We've gotta earn that coin."
        scene ch4sc19_238 with dissolve
        el "You got it! I’ll pick the most lucrative one!"
        scene black with Dissolve(1.5)
        $ renpy.pause(1)

    scene black with dissolve
    scene ch4sc7b with Dissolve(1.5)
    $ renpy.pause()
    scene ch4sc19_597 with Dissolve(2)
    mct "So she's back..."

    if samarah_alive == True:
        scene ch4sc19_597 with dissolve
        mct "She’s humming?"
        mct "Doesn’t seem too worried about her missing boss."
        scene ch4sc19_598 with dissolve
        mc "*Clears throat*"
        sl "Go away. We’re closed, and I’m expecting someone!"
        mc "Now is that any way to greet someone you stabbed in the back?"
        mc "Guess I'll be on my way then."
        scene ch4sc19_599 with dissolve
        sl "[mc]?! [mc]!! You’re here!"
        sl "Stop! Don’t go!"
        scene ch4sc19_600 with dissolve
        with vpunch
        "Selena wraps her arms around you, holding firmly."
        sl "You’re the one I was expecting... I’m really glad you made it."
        scene ch4sc19_601 with dissolve
        mc "Where’s the stablekeeper, Selena?"
        scene ch4sc19_600 with dissolve
        sl "He's taken the week off, and returned to his home village to procure some more horses."
        scene ch4sc19_601 with dissolve
        mc "So he’s not missing?"
        scene ch4sc19_600 with dissolve
        sl "*Snickers* No. I just made that report and sent it to the guild..."
        sl "hoping you'd show up."
        scene ch4sc19_602 with dissolve
        mct "She’s holding on to me tightly..."
        mct "I can feel every inch of her breasts pressing against my back."
        mc "You’re squeezing me awfully tight..."
        scene ch4sc19_603 with dissolve
        sl "Duh! I’ve missed you!"
        sl "You don’t mind a little hug, do you?"
        scene ch4sc19_602 with dissolve
        mc "*Sigh* I suppose not..."
        mc "Did you get your sister to safety?"
        scene ch4sc19_603 with dissolve
        sl "Uh-Huh! Samarah is staying at a little cottage in the mountains, near the Ravenwood plateau."
        sl "It's just a couple of hours on foot from Folkstead, so it's a pretty cozy location."
        scene ch4sc19_602 with dissolve
        mc "I’m glad she’s okay."
        mc "How did you manage to secure a cottage?"
        scene ch4sc19_603 with dissolve
        sl "I used all my savings from working here at the stables."
        sl "It’s not a fancy cottage... it was actually abandoned."
        sl "So I was able to strike a good deal for it. Samarah will stay there and work in the village of Folkstead nearby."
        scene ch4sc19_602 with dissolve
        mc "Makes sense, you’re a good sister."
        scene ch4sc19_603 with dissolve
        sl "She deserves the best..."
        sl "She’s been through so much."
        scene ch4sc19_602 with dissolve
        mc "What about you?"
        mc "What are you doing here?"
        scene ch4sc19_603 with dissolve
        sl "What does it look like I’m doing? I’m hugging you!"
        sl "I had to come see you..."
        scene ch4sc19_604 with dissolve
        sl "I wanted to thank you... I know I wronged you, and you could’ve easily taken it out on Samarah."
        sl "But you didn’t..."
        sl "Instead, you allowed us to leave and have a new chance at life."
        sl "I've spent so many nights lying awake thinking about how stupid I was for not trusting you."
        sl "If I'd just told you everything from the beginning... maybe we could have rescued Samarah ourselves."
        scene ch4sc19_601 with dissolve
        mc "Glad you finally seem to realize it..."
        scene ch4sc19_600 with dissolve
        sl "I have so much to make up for... I want to make it right."
        sl "I want to thank you properly."
        scene ch4sc19_605 with dissolve
        mc "How do you plan on doing that?"
        sl "Apologizing to everyone. Proving that you can depend on me again... Earning back your trust."
        sl "And... this..."
        scene ch4sc19_606 with dissolve
        mc "Selena..."
        sl "Please... Let me show how much I appreciate you..."
        sl "How... thankful I am."

        #### Choice ####
        menu:
            "Accept her. ({color=#ff8cdd}Romance{/color})":
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene ch4sc19_606 with dissolve
                mc "We shouldn’t... Not this soon..."
                sl "Yes we should... Don't you want me? Am I imagining the outrageous connect between us?"
                play music lewd_1 fadein 1.0
                #stop music fadeout 1.0
                scene ch4sc19_607 with dissolve
                $ selena_path = True
                mc "No... you're not imagining it."
                sl "Mmhh... You're long overdue being rewarded for everything."
                sl "There have been sparks igniting between us every time we've been close."
                mc "*Sigh* A reward does sound good..."
                $ selena_bj = True
                scene ch4sc19_608 with dissolve
                sl "It does, doesn’t it? And I have a feeling this reward will leave you very... satisfied."
                sl "Just let me take care of you. Let me thank you..."
                mc "*Groans* Fuck..."
                $ selena_sex = True
                "Selena begins to undo your trousers."
                scene ch4sc19_609 with dissolve
                sl "Oh, my... You really seem to like the idea of having me on my knees, thanking you."
                mc "Hnnhgh... That’s certainly an alluring thought."
                sl "I'd better stop wasting time and get on my knees then..."
                scene ch4sc19_610 with dissolve
                sl "Mh-Mh... Now that’s what I call a proper cock!"
                sl "*Snickers* No wonder you walk around so confidently... Or should I say, cockily?"
                mc "Why don’t you put that little mouth of yours to good use?"
                scene ch4sc19_611 with dissolve
                sl "*Bites lip* You want me to put your beautiful cock in my mouth?"
                sl "Make it nice and wet with my spit? Rub my tender tongue all over it?"
                scene ch4sc19_612 with dissolve
                mc "Yes... Show me just how badly you want to be forgiven."
                sl "You must’ve been blessed by the gods to have such a nice cock..."
                scene ch4sc19_613 with dissolve
                sl "*Mwah* Mmmhh... Tasty."
                #####ANIMATION#####
                show sl_fuck1 with fade
                $ renpy.pause(1, hard=True)
                $ renpy.pause()
                sl "*Sucking* Ghhah... HHnghh!"
                mct "Fuck... She’s sucking really hard... HnnHh..."
                sl "*Sucking* NNngh! MMhh! *Sucking firmly* Ghhagh! HHggrh!"
                scene ch4sc19_612 with dissolve
                "After thoroughly covering your cock in her warm saliva, she pauses."
                sl "I think I’m a little overdressed for the occasion... Why don’t you lie down over there."
                scene black with dissolve
                scene ch4sc19_614 with dissolve
                sl "Enjoying the view?"
                mc "It’s gorgeous..."
                sl "Have you ever had a chocolate woman before? Our pussies have quite the flavor I've been told."
                mc "No... but by your scent, I am inclined to believe what you've been told is the truth, you smell delicious."
                scene ch4sc19_615 with dissolve
                sl "Then allow me to give you a little taste..."
                "She wiggles further onto you, presenting you with her plump ass."
                scene ch4sc19_616 with dissolve
                mc "You certainly smell delicious.... earthy with a hint of orange? MMh..."
                mc "You're already dripping wet, you're leaking onto my chest..."
                sl "Mmh... I can feel your hot breath between my cheeks... Taste me! My pussy needs you!"
                scene ch4sc19_617 with dissolve
                with vpunch
                "She presses herself fully against you, forcing your face between her shapely cheeks."
                #####ANIMATION#####
                show sl_fuck2 with fade
                $ renpy.pause(1, hard=True)
                $ renpy.pause()
                with vpunch
                sl "{b}*Moans* OOHHH!! [mc]! MMnhh!{/b}"
                sl "F-Fuck!! Just like that! Ahhhh! Smell me! Taste me! AhhHnngh!"
                sl "D-Dig your tongue in me! Ahh... Mmmhh!"
                mct "I can barely breathe... But fuck... She does taste incredible."
                sl "{b}*Moans Louder* OOhhH! [mc]!!{/b} I love how you’re using your tongue! {b}MMHH!!{/b}"
                with vpunch
                sl "{b}*Shaking* AHHH! I’M CUMMING!! KEEP LICKING ME!! AH-AH-OHHH!{/b}"
                with vpunch
                $ renpy.pause(1)
                with vpunch
                scene ch4sc19_617 with dissolve
                sl "*Heavy breathing* Whhoooh... I didn’t expect you to devour me like that..."
                sl "You’ve got me trembling from pleasure..."
                mc "*Muffled* Mnhm-Mhh-Nnh..."
                scene ch4sc19_618 with dissolve
                sl "Moans* OOhhh... I like how it vibrates when you try to talk between my ass cheeks..."
                mc "Mmhhh! Mmh-mhm..."
                sl "*Snickers* Let me adjust..."
                scene ch4sc19_616 with dissolve
                sl "See? You've got me dripping... All just with your tongue."
                mc "You didn't give me much of a choice..."
                sl "I couldn't help myself. I wanted you to get a proper taste."
                scene ch4sc19_615 with dissolve
                sl "There we go..."
                sl "So... What’s your verdict? Have I swayed you to like chocolate?"
                scene ch4sc19_614 with dissolve
                mc "You’re fucking delicious... I’ll give you that."
                sl "That was just the appetizer... I hope you’re ready for the main course."
                scene ch4sc19_619 with dissolve
                with vpunch
                sl "Just gotta get this big cock of yours inside- Hnnnghh!"
                "Selena doesn't care about taking it slow, she wants you inside, and pushes further down onto you."
                #####ANIMATION#####
                show sl_fuck3 with fade
                $ renpy.pause(1, hard=True)
                $ renpy.pause()
                sl "{b}*Moans* OHHH!{/b} I can barely fit you! {b}AH! AHH!{/b}"
                sl "*Moans* Do you- Ahhnngh! Feel how tight I am for you?! Oohh!"
                mc "You feel amazing wrapped around my cock."
                sl "*Moans* Ah-Ahh! You like having me ride you? Pressing down onto your beautiful cock? {b}MMH!{/b}"
                sl "Heavens you're big!! {b}AHhh!{/b}"
                sl "*Moans louder* Oohhh! You’re hitting all the right spots! Oh! {b}AH! YES!!{/b}"
                sl "*Moans* I’m not sthhopping! Not until you give me a big nice load of your cum!"
                sl "*Moans loudly* I’m- AHH! Ohhngh! I’m going to milk it out of you with my wet little pussy!"
                mct "Fuck... She’s going wild for my dick... She’s so fucking tight..."
                with vpunch
                sl "*Moans* That’s it! Ahhh! [mc]! I feel you throbbing inside me!"
                sl "*Moans* Please! Please give it to me! I need your forgiveness! {b}AH! YEES!!{/b}"
                with vpunch
                sl "{b}*Moans* [mc]!!{/b} Do you feel me?! Do you feel how thankful I am?? {b}AH! MMH!!{/b}"
                mct "F-Fuck she’s cumming! And she’s gripping me so tightly!"
                with vpunch
                sl "{b}*Moans Loudly* AH!-AH!!{/b} Yes! Fuck you’re deep! {b}MMH!{/b} Cum with Mheeeeeee!"
                with vpunch
                $ renpy.pause(1.5)
                with vpunch
                scene ch4sc19_615 with dissolve
                sl "*Panting* Pheewh... Now that’s what I call a proper ride."
                mc "You'd be the one to know... You’re the one working at the stables."
                scene ch4sc19_614 with dissolve
                sl "*Snickers* I’ll definitely be riding you more often!"
                mc "Is that so?"
                sl "Mh-Hmh. I still have a lot of gratitude left... Let’s get dressed."
                scene black with dissolve
                "The two of you put your clothes back on and you immediately feel Selena’s arms wrap around you."
                scene ch4sc19_620 with dissolve
                sl "*Relieved sigh* Thank you... Thank you so much! For allowing my sister a chance at life."
                sl "For forgiving me... Thank you, [mc]. I know I still have a lot of making up ahead of me."
                sl "But this was... perfect. The chance I needed."
                scene ch4sc19_621 with dissolve
                mc "You've taken the first step, and I acknowledge that."
                mc "But the road to redeem yourself is still long..."
                mc "Starting with Eliza... I’m not the one whose forgiveness you need the most. She is."
                scene ch4sc19_620 with dissolve
                sl "I know... I just needed to see you first."
                scene ch4sc19_621 with dissolve
                mc "I’m heading back."
                mc "How you handle your apology is up to you."
                scene ch4sc19_620 with dissolve
                sl "Will you... come visit me and Samarah in Folkstead?"
                sl "Will you come see me?"
                scene ch4sc19_621 with dissolve
                mc "If you're able to make up with Eliza and she decides to forgive you... then yes."
                mc "If she can't find it in herself to forgive you, then this is goodbye."
                scene ch4sc19_620 with dissolve
                sl "*Sigh* I-... I understand."
                "Selena realises she has a mountain to climb still, but she's on the right path."
                $ selena_trust += 5
                "Having shared this moment of intimacy with you, Selena feels ready for the hardships ahead, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene black with Dissolve(2)

            "Reject her. ({color=#f00}Reject Selena{/color})":
                scene ch4sc19_607 with dissolve
                mc "Selena... Stop."
                mc "I’m not interested... Have you even apologized to Eliza yet?"
                scene ch4sc19_609 with dissolve
                sl "Not yet..."
                sl "I only just arrived yesterday and I wanted to see you first."
                scene ch4sc19_601 with dissolve
                $ selena_path = False
                mc "Eliza is the one who your betrayal hurt the most. IF she decides to forgive you-"
                mc "Then, and only then, will I consider trying to trust you again."
                scene ch4sc19_600 with dissolve
                sl "That’s all I needed to know..."
                sl "That you would at least consider it. I’ll apologize to her!"
                scene ch4sc19_601 with dissolve
                mc "Good, I’m heading back now..."
                mc "Try not to report anyone else missing."
                scene ch4sc19_603 with dissolve
                sl "*Snickers* No promises!"
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene black with Dissolve(2)

        scene black with dissolve
        stop music fadeout 1.0
        jump ch5sc1



    else:
        scene ch4sc19_598 with dissolve
        sl "*Hums*"
        mc "Selena."
        scene ch4sc19_599 with dissolve
        play music darknight_4 fadein 1.0
        #stop music fadeout 1.0
        with vpunch
        sl "Huh?! [mc]!"
        sl "You’re here! Good to-"
        scene ch4sc19_622 with dissolve
        with vpunch
        sl "*Struggling for breath* Hhrhh! Hhhrhh!"
        scene ch4sc19_623 with dissolve
        mc "I told you what would happen if I ever saw you again. *Squeezing tightly*"
        with vpunch
        mc "{b}WHY ARE YOU HERE?!{/b}"
        scene ch4sc19_622 with dissolve
        "*Loosens grip* She can’t answer while you’re choking her."
        "You put her down and grab her firmly."
        scene ch4sc19_624 with dissolve
        with vpunch
        sl "*Groans* Aahrh!"
        mc "If you don’t want me to snap your neck like I did with your sister, you'd better start talking."
        sl "You! I’m here to find you!"
        scene ch4sc19_625 with dissolve
        mc "*Grip tightens* What the fuck do you want?"
        sl "I- Hhrrhh! I need your help!"
        sl "It’s... It’s my sister! Hhhrhh! I found a way to bring her back!"
        scene ch4sc19_624 with dissolve
        mc "Your sister? I killed her with my own hands. She’s dead... You’ve clearly lost it."
        sl "It’s possible! I’ve come across an object... a soulgem."
        scene ch4sc19_625 with dissolve
        sl "*Groans* It can contain the soul of any being and it will allow me to talk to her!"
        with vpunch
        mc "Bullshit! I’ve never heard of such a thing."
        scene ch4sc19_626 with dissolve
        sl "They’re incredibly rare... I’ve spent the last two months with my head buried in books in several libraries."
        sl "I finally discovered what could be the potential location of a soulgem..."
        mc "So what? What makes you think I'd help you? I couldn’t care less."
        scene ch4sc19_625 with dissolve
        sl "Please... I just- need you to activate the soulgem once I’ve gotten my hands on it."
        sl "I know I’ve hurt you... I’m not asking for me. I’m asking for my sister! Samarah! She was innocent!"
        scene ch4sc19_624 with dissolve
        sl "I don’t believe you're so coldblooded that you're really okay with her being dead!"
        sl "You were angry... I get it. But now? Now that we might have a chance to bring her back!"
        sl "To make it right!"
        scene ch4sc19_626 with dissolve
        sl "She was just a kid! She didn’t even get to experience life! Please, [mc]!"
        sl "I know I fucking messed up, okay?! I’m not asking for forgiveness, I’m asking you to give my sister a chance!"
        scene ch4sc19_627 with dissolve
        sl "*Sobbing* Please! You’re my only hope! I’ll... I’ll do anything you want!"
        scene ch4sc19_628 with dissolve
        "Selena presses her plump ass back into your crotch."
        scene ch4sc19_627 with dissolve
        sl "Anything..."
        scene ch4sc19_628 with dissolve
        sl "[mc]... Please! Help me with this and I’ll be in your debt!"
        scene ch4sc19_627 with dissolve
        mc "Anything I want, huh?"
        scene ch4sc19_628 with dissolve
        sl "Anything... you... want."
        #### Choice ####
        menu:
            "Agree to help her. ({color=#ff8cdd}Fuck Selena{/color})":
                scene ch4sc19_627 with dissolve
                mct "I don't really care about what she wants..."
                mct "But this soulgem she is talking about does sound interesting, I'll play along."
                mc "Okay... I’ll help. You’re right... Samarah was a spur of the moment decision."
                mc "If you find this ‘soulgem’ I’ll help."
                scene ch4sc19_628 with dissolve
                sl "Really?! YES! [mc]!! I owe you!"
                mc "You can begin paying off your debt by kneeling."
                scene black with Dissolve(1.5)
                "As you release Selena, she undresses you and kneels before you."
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene ch4sc19_611 with Dissolve(1.5)
                sl "Like this? Is this how you want me?"
                play music lewd_1 fadein 1.0
                #stop music fadeout 1.0
                scene ch4sc19_610 with dissolve
                mc "Stop talking and start sucking."
                sl "Heavens you’re big! I don’t think you can fit inside my mouth..."
                scene ch4sc19_612 with dissolve
                mc "You'd better make it fit. Time to show how badly you want my help."
                scene ch4sc19_629 with dissolve
                with vpunch
                "You grab the back of her head and press your cock through her lips."
                mc "Now put that mouth of yours to good use."
                #####ANIMATION#####
                show sl_fuck4 with fade
                $ renpy.pause(1, hard=True)
                $ renpy.pause()
                with vpunch
                sl "*Gagging* Mmhhhr!! Hhhggaahh!"
                "After the initial surprise of you shoving your cock in her mouth, she adjusts and begins sucking."
                mc "Fuck that’s good... You do know how to use that little mouth of yours."
                sl "*Suck* *Suck* MmhhH! *Lick* Nngghh!"
                mc "You’re a good little slut. Hnngh... Keep taking my dick like that."
                sl "MMHH! Gahrgh! Hnnh! *Sucking harder*"
                mc "You love being force-fed my cock, huh? How I’m reaching the back of your tiny throat?"
                sl "*Muffled gagging* Hhgarrhh! Hhhnnrhh! MNNGH!"
                scene ch4sc19_630 with dissolve
                sl "*heavy breathing* Hhnnaahh... Hnnahhh..."
                mc "You’re good with your mouth, but what about your pussy? Will it be as good?"
                "Her eyes are watering from having your cock so deep in her throat."
                scene ch4sc19_631 with dissolve
                sl "*Coughing* Hhrnnh! Yhess! I’ll show you... You'll enjoy it!"
                sl "I’ll be the best little slut for you."
                scene ch4sc19_632 with dissolve
                "She undresses and gets down on all fours."
                sl "Is this pleasing you? Are you going to fuck my slutty little pussy with that big cock of yours?"
                sl "I bet you’ve never had a chocolate pussy before..."
                mc "Looks good... There’s just one thing missing."
                scene ch4sc19_633 with dissolve
                with vpunch
                sl "{b}*Moans* AAHHH! HHARRH!{/b}"
                "You press her firmly down into the hay, grabbing her wrists while plunging your cock deep inside her."
                scene ch4sc19_634 with dissolve
                mc "Damn Selena, you’re soaking wet! My cock is drenched in a mix of your spit and juices..."
                mc "You must enjoy being my little slut."
                sl "*Moans* NnngghH!! {b}Y-YES!!{/b} Fuck me, [mc]!! Give me your cock!"
                #####ANIMATION#####
                show sl_fuck5 with fade
                $ renpy.pause(1, hard=True)
                $ renpy.pause()
                with vpunch
                sl "*Moans* Hhnrhh! YES!! Please fuck my tight, slutty pussy! Make it yours!"
                sl "*Moans* AH-AH-MMH! [mc]! FUCK!! You’re {b}HUGE!!{/b}"
                sl "*Moans loudly* This is- AH! AH! Nothing like my- OH!! OMMH! My fingers!"
                mc "Your little pussy belongs to me now. And I'll fill it out whenever I want."
                with vpunch
                sl "Moans* FUCK!! YES!! Wheneverrrr you- OHHHH! want!"
                sl "*Moans* I’m yours to fuck whenever! Fuck me right here in the hay like the dirty stable-maiden I am!"
                with vpunch
                sl "{b}*Moans* AHHH! F-FUCK!! YOURRE SOOOH DEEP! AHHH!{/b}"
                mc "*Grunts* That’s Hnngh! Right! Orgasm with me deep inside you! Force me to cum!"
                sl "{b}*Moans* AHH! YES!! [mc]!! GIVE ME EVERYTHING!!{/b} I’m your slut! I want all of you!"
                with vpunch
                $ renpy.pause(1)
                with vpunch
                scene ch4sc19_633 with dissolve
                $ renpy.pause(1.5)
                scene ch4sc19_635 with dissolve
                with vpunch
                sl "{b}*Screaming* OOHHH FUCK!! AHIIIIYHH!!!{/b}"
                "You pump her soaking pussy full of your cum while her moans carry through the forest."
                with vpunch
                sl "{b}*Moans* AIIIYEEH!! Aiiiiyh! AHHH!{/b}"
                scene black with Dissolve(1.5)
                "The two of you get dressed after you catch your breath."
                scene ch4sc19_609 with dissolve
                sl "*Hugs* Whauh... That was amazing!"
                sl "Thank you for agreeing to help!"
                scene ch4sc19_606 with dissolve
                mc "You were... convincing."
                scene ch4sc19_603 with dissolve
                sl "I’ve wanted that cock of yours since we first met..."
                mc "Is that so?"
                sl "Mh-Hm! And you being so rough with me... pushed all the right buttons! I’ve never had an orgasm like that!"
                scene ch4sc19_609 with dissolve
                sl "I look forward to being your slut again..."
                scene ch4sc19_601 with dissolve
                mc "Mh. Go find that soulgem and I’ll happily feed you my cock again..."
                scene ch4sc19_600 with dissolve
                sl "I will! Thank you! I’m so excited to bring her back!"
                sl "You have no idea how much this means to me!"
                scene ch4sc19_601 with dissolve
                mc "I can tell. The sooner the better. You know where to find me."
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene black with Dissolve(1.5)

            "Refuse to help her. ({color=#f00}Reject Selena{/color})":
                scene ch4sc19_626 with dissolve
                mc "Not interested. Go find someone else to help you."
                scene ch4sc19_625 with dissolve
                sl "[mc]! Please! I need you!"
                scene ch4sc19_624 with dissolve
                mc "Fuck off, Selena. You’re not even worth the energy it'd take to kill you."
                mct "Besides, killing her would be too merciful... Her suffering would be over too quickly."
                mct "I’d rather wait til she latches onto some semblance of hope..."
                mct "And destroy her all over again."
                "You release her and walk away."
                scene ch4sc19_599 with dissolve
                sl "[mc]! Don’t go! Please!"
                sl "I need you!!"
                #play music forest_1 fadein 1.0
                stop music fadeout 1.0
                scene black with Dissolve(1.5)


        scene black with dissolve
        $ renpy.pause()
        stop music fadeout 1.0
        jump ch5sc1

label ch4sc9:

    window hide dissolve
    play music home_2 fadein 1.0
    scene black with Dissolve (1.0)
    scene ch4sc9_001 with Dissolve(2.0)
    $ renpy.pause()
    scene ch4sc9_002 with dissolve
    $ renpy.pause()
    scene ch4sc9_003 with dissolve
    mct "According to that sleazeball back on the ship, Kelly was last seen in this alley."
    mct "He probably got fed up with rejection and decided to act on his... urges."
    scene ch4sc9_004 with dissolve
    mct "Looks like there’s been some kind of a struggle here."
    mct "Could’ve been a couple of drunks settling a dispute. It’s the alley of a tavern after all ..."
    mct "Hmm. A set of small footprints, most likely female. Criss-crossing with several larger ones …"
    scene ch4sc9_005 with dissolve
    mct "Huh?"
    scene ch4sc9_006 with dissolve
    mct "Looks like her attackers were well-armed."
    mct "She didn’t give up without a fight... good."
    mct "She might still be alive then."
    scene ch4sc9_007 with dissolve
    with vpunch
    uk "*Muffled noises* Let me out!"
    mct "There’s shouting coming from that door."
    scene ch4sc9_008 with dissolve
    uk "Don’t let Kelly out of your sight."
    uk "If anyone tries to enter, stop them immediately!"
    scene ch4sc9_009 with dissolve
    uk "I'll be back soon. I have some business to attend to."
    scene ch4sc9_010 with dissolve
    uk "Yes sir!"
    scene ch4sc9_007 with dissolve
    mct "Well, that was easy."
    mct "I could just take care of that guy and break her out..."
    mct "But I’m curious about that man... he knows Kelly’s name."
    mct "How does he know her? Has he been targeting her?"
    scene ch4sc9_011 with dissolve
    stop music fadeout 1.0
    mct "Could he be the one behind the kidnappings here in Luxenford?"
    play music sneak_1 fadein 1.0
    mct "I'd better shadow him and learn more."
    scene black with Dissolve(2)
    scene ch4sc9_012 with Dissolve(2)
    mct "I haven’t been to this area of the capital before. Looks expensive."
    mct "He doesn’t dress like a noble, though."
    scene ch4sc9_013 with dissolve
    mct "Who are you meeting in a fancy place like this?"
    scene ch4sc9_014 with dissolve
    mct "And what do you want with a random girl from a crew of pirates?"
    scene ch4sc9_014 with dissolve
    with vpunch
    uk "Where the heavens have you been?!"
    uk "You’ve been out all night! Up to who knows what?!"
    uk "Honey... please listen to me for just a moment."
    mct "Sounds like he's arguing with a woman?"
    stop music fadeout 1.0
    scene ch4sc9_015 with dissolve
    play music home_2 fadein 1.0
    uk "I’m tired of your excuses, Edward!"
    uk "How many whores did you fuck last night??"
    scene ch4sc9_016 with dissolve
    ed "None! I swear I didn’t bed anyone this time!"
    ed "Honey... I found her! I found our baby girl!"
    scene ch4sc9_015 with dissolve
    uk "You'd sink so low as to use her as an excuse?"
    uk "You disgust me!"
    scene ch4sc9_016 with dissolve
    ed "Maggie... please listen!"
    ed "It’s really her! Our little Kelly has come home!"
    scene ch4sc9_014 with dissolve
    mct "Huh? Kelly is their daughter? Why did he kidnap her then?"
    scene ch4sc9_017 with dissolve
    mg "O-Our Kelly is back? I... I never thought I'd see my baby again."
    scene ch4sc9_015 with dissolve
    mg "Why isn’t she with you then? Where is she, Edward?"
    scene ch4sc9_016 with dissolve
    ed "Now, don’t freak out..."
    ed "I had to lock her up."
    scene ch4sc9_015 with dissolve
    with vpunch
    mg "{b}YOU DID WHAT?!{/b}"
    mg "{b}OUR LITTLE KELLY?!{/b} I’m going to kill you!"
    scene ch4sc9_016 with dissolve
    ed "Maggie! Please listen! All these years she’s spent with those... filthy pirates."
    ed "Let’s just say that when I ran into her, she wasn’t very eager to be reunited with us."
    scene ch4sc9_018 with dissolve
    with vpunch
    mg "So you thought... {b}KIDNAPPING OUR OWN DAUGHTER{/b}... would make her happy to come back?!!!"
    mg "May the heavens have mercy on you after I get done with you!"
    scene ch4sc9_015 with dissolve
    mg "Take me to her, right now!"
    scene ch4sc9_016 with dissolve
    ed "Maggie... no. Not until Kelly calms down."
    ed "I have one of my guys watching her and bringing her meals. She’s well taken care of."
    ed "Maybe tonight we can go see her together."
    scene ch4sc9_019 with dissolve
    ed "Now, I have some important business to attend to at the docks. Please, just be patient, Maggie."
    scene ch4sc9_020 with dissolve
    mg "*Mumbles* That bastard! How dare he keep me from my baby girl. She needs me!"
    mg "*Mumbles* It's been so many years since I last held my baby girl! B-Bastard!"
    scene ch4sc9_014 with dissolve
    mct "This is a good chance to get some more information."
    mct "She seems very unhappy with her husband. I could use that to my advantage."
    scene ch4sc9_021 with dissolve
    mc "Excuse me, Maggie is it?"
    scene ch4sc9_022 with dissolve
    mg "What is it now, you jerk? I don’t want anymore bad news, Edwar-"
    scene ch4sc9_023 with dissolve
    mg "Oh! You’re not my husband."
    scene ch4sc9_024 with dissolve
    mg "My apologies for the outburst."
    mg "My husband he- Arrgh! It doesn’t matter."
    scene ch4sc9_025 with dissolve
    mg "Please. State your business, young man."
    mg "This is private property, if you weren’t aware."
    #####Choice######
    menu:
        "I work for your husband, Edward. (Lie)":
            scene ch4sc9_027 with dissolve
            mc "I work for Lord Edward. I was supposed to meet him here to receive instructions about a ‘Kelly’?"
            scene ch4sc9_026 with dissolve
            mg "Oh! You know about our daughter?! Hmmm..."
            scene ch4sc9_025 with dissolve
            mg "Yes! That could work. Young man, I want you to find out where she is and bring her to me!"
            scene ch4sc9_027 with dissolve
            mc "I don’t know, Miss. Wouldn’t that upset your husband?"
            scene ch4sc9_026 with dissolve
            mg "*Mumbles* Looks like he needs some added incentive."
            scene ch4sc9_028 with dissolve
            mg "Perhaps, but it would make me..."
            mg "Very, appreciative."
            scene ch4sc9_029 with dissolve
            mc "How could I deny a mother’s request to reunite with her daughter?"
            scene ch4sc9_028 with dissolve
            mg "Mhm. I will make it worth your while... believe me."
            mg "Now go, bring my sweet Kelly home."
            scene black with Dissolve(2)

        "I’m looking for your daughter, Kelly. (Honest)":
            scene ch4sc9_027 with dissolve
            mc "I followed your husband here, from a building where I believe he's keeping Kelly captive."
            mc "My instructions are to bring her safely back to her crew."
            mc "But I didn't expect her kidnappers to be... her own parents."
            scene ch4sc9_025 with dissolve
            mg "You know where she is?? Please! Bring her back to me!"
            mg "I miss her terribly. My little Kelly."
            scene ch4sc9_027 with dissolve
            mc "Maggie, she has to return to her crew. She was taken against her will."
            scene ch4sc9_028 with dissolve
            mg "Please, young man. Please bring her home!"
            scene ch4sc9_028 with dissolve
            mg "I would be... immensely grateful."
            mg "There's nothing a mother wouldn't do... for the man who brings her child home."
            scene ch4sc9_029 with dissolve
            mc "I’ll see what I can do. You should have a chance to talk, at least."
            mc "But Kelly is likely leaving tonight, with our crew, just be aware of that."
            scene ch4sc9_028 with dissolve
            mg "Thank you! I'll make it worth your while."
            mg "I promise you will not regret this young man, thank you..."
            mg "Now go, bring my little Kelly home."
            scene black with Dissolve(2)

    scene ch4sc9_030 with Dissolve(2)
    mct "This is where her father exited from earlier."
    mct "Let’s take a look inside."
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc9_031 with Dissolve(2)
    play music explore_1 fadein 1.0
    kl "*Annoyed* Urrrh! Why can’t I leave?"
    kl "If you work for my father, then let me go right now!"
    scene ch4sc9_032 with dissolve
    kl "I want to leave. Now! My crew is waiting for me!"
    scene ch4sc9_033 with dissolve
    with vpunch
    kl "*Gasps* Uaaahh?! Holy smokes!!"
    kl "Who are you?? What are you doing!"
    scene ch4sc9_034 with dissolve
    $ renpy.pause()
    scene ch4sc9_034b with dissolve
    mc "Oh, hey Kelly."
    scene ch4sc9_034 with dissolve
    $ renpy.pause(1)
    scene ch4sc9_034b with dissolve
    mc "This isn’t what it looks like."
    scene ch4sc9_035 with dissolve
    kl "It looks like you’re killing him!"
    ####Choice####
    menu:
        "Incapacitate him. ({color=#87e1fa}Light Path{/color})":
            scene ch4sc9_034b with dissolve
            mc "Don’t worry, Kelly. He'll wake up in time for supper."
            scene ch4sc9_034c with dissolve
            with vpunch
            $ renpy.pause(1)
            $ light += 2
            "You chose to spare the man... {color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)

        "Kill him. ({color=#f00}Dark Path{/color})":
            scene ch4sc9_034b with dissolve
            mc "Okay... So, it’s exactly what it looks like."
            scene ch4sc9_034c with dissolve
            with vpunch
            $ renpy.pause(1)
            $ dark += 2
            "You chose to execute the man in cold blood... {color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)


    scene ch4sc9_036 with Dissolve(2)
    mc "Are you ready to get the hell out of here?"
    scene ch4sc9_037 with dissolve
    kl "Who are you? You’re clearly not working for my father."
    scene ch4sc9_038 with dissolve
    kl "Hmmm."
    scene ch4sc9_038b with dissolve
    kl "Kira sent you! Didn’t she?"
    scene ch4sc9_039 with dissolve
    mc "She did. But your mother has also requested to see you."
    mc "She was against your father's plan to keep you here."
    scene ch4sc9_038 with dissolve
    $ renpy.pause(1.3)
    scene ch4sc9_038b with dissolve
    kl "I don’t know... I didn’t expect to be in this situation... or to see her again."
    kl "It's been years... she really didn't have a hand in my kidnapping?"
    scene ch4sc9_038 with dissolve
    $ renpy.pause(1.3)
    "Kelly seems to ponder the situation but seemingly has trouble making a decision."
    scene ch4sc9_038b with dissolve
    kl "What do you think I should do?"
    ####Choice####
    menu:
        "Take her to her mother. (Reward)":
            scene ch4sc9_039 with dissolve
            mc "Alright then... we should stop to see your mother before we return."
            mc "She seemed really distraught about the whole situation, she longs for a reunion."
            scene ch4sc9_038 with dissolve
            $ renpy.pause(1.3)
            scene ch4sc9_038b with dissolve
            kl "*Sigh* I won’t lie... I’m not really jumping with joy at the prospect."
            kl "I haven’t seen her since I was five."
            scene ch4sc9_038 with dissolve
            mc "Since you were five? That's a long time... how come?"
            scene ch4sc9_038b with dissolve
            kl "I-... I'm something called a 'Sea-born' which is when a child is birthed at sea."
            kl "The captain of the ship has a claim to the child when they turn five..."
            scene ch4sc9_037 with dissolve
            kl "It's an ironclad rule, this is done to ensure that there is enough crew and sailors in the kingdom."
            kl "Not all captains come to make the claim, but in my case... they did."
            scene ch4sc9_038 with dissolve
            mc "Kira and Pearl claimed you? But they don't look much older than their early twenties?"
            "Kelly shakes her head."
            scene ch4sc9_038b with dissolve
            kl "No, they aren't the ones that claimed me, some other captain did."
            kl "He was... not a kind man, so when Pearl and Kira happened upon us and shipwrecked us, they... found me."
            kl "They decided to take me on as a steward and in return for my service, I'd be under their protection."
            scene ch4sc9_037 with dissolve
            kl "Life at sea is not exactly... welcoming to a woman, so I eagerly accepted their offer."
            kl "I'd have access to hot meals, my own bed, and best of all, no men getting handsy with me..."
            scene ch4sc9_038b with dissolve
            kl "I owe them my life, so I'll happily scrub the deck, cook our meals and wash our clothes."
            kl "Seeing my mother again... I don't know... what if it causes issues?"
            scene ch4sc9_039 with dissolve
            mc "I’m sure it won’t be as bad as you think."
            mc "At the very least, it might give her some closure."
            mc "I can't imagine it's been easy for her, losing her daughter all those years ago."
            scene ch4sc9_038b with dissolve
            kl "Even if I'm not the daughter she wants me to be?"
            kl "What if she's disappointed with how I turned out?"
            scene ch4sc9_039 with dissolve
            mc "The impression I got is that she just wants to be reunited with you."
            mc "I don't think she expects you to be anyone other than the women you've grown up to be."
            scene ch4sc9_038 with dissolve
            mc "So, what do you say?"
            kl "..."
            scene ch4sc9_038b with dissolve
            kl "Okay, I'll go meet her."
            kl "On the condition that you escort me! If you're with me I'll be safe."
            scene ch4sc9_039 with dissolve
            mc "Deal. I'll not let anyone touch you."
            mc "Let's go see your mother."
            scene black with Dissolve(1.5)
            scene ch4sc9_040 with Dissolve(1.5)
            mc "Maggie. Look who I found"
            scene ch4sc9_041 with dissolve
            with vpunch
            mg "{b}KELLY!{/b}"
            mg "Oh my sweet baby is finally home!"
            scene ch4sc9_042 with dissolve
            kl "H-Hi... Mom?"
            scene ch4sc9_043 with dissolve
            with vpunch
            $ renpy.pause(1.3)
            mg "Oh, sweetheart! I’m so thrilled to have you back!"
            scene ch4sc9_044 with dissolve
            kl "I-I’m happy to see you too, Mom."
            kl "After father locked me up, I didn’t know what to think about either of you."
            scene ch4sc9_043 with dissolve
            mg "Oh, sweetie! You'd better believe he has been, and will continue to be, scolded for that!"
            mg "You have nothing to fear here. I promise!"
            scene ch4sc9_044 with dissolve
            kl "Thank you."
            scene ch4sc9_045 with dissolve
            kl "Mom... I’m not staying. We’re setting sail in a few hours."
            kl "My crew has been waiting for me since last night. They must be worried."
            scene ch4sc9_046 with dissolve
            mg "Oh, sweetie. What are you saying? Why do you want to go back to them?"
            mg "You can have a good, safe, and prosperous life here. Where you belong."
            mg "Your father and I, we're nobles... you'll want for nothing, I promise."
            mg "You’re finally back and alive! Won’t you consider staying?"
            scene ch4sc9_047 with dissolve
            kl "Mom, I can’t."
            kl "My crew are my family now."
            kl "That's what it means to be {b}Sea-born{/b}."
            scene ch4sc9_048 with dissolve
            kl "You and father gave me up when I was five..."
            kl "I spent so many years wondering... why?"
            scene ch4sc9_047 with dissolve
            kl "But when I turned fifteen, my old crew was conquered by Kira and Pearl, captains of the Bloody Banshee."
            scene ch4sc9_046 with dissolve
            mg "Kelly... sweetheart."
            mg "Bloody banshu? I'm not following what you're saying?"
            scene ch4sc9_047 with dissolve
            kl "Bloody Banshee, Mom. It’s the name of our ship."
            kl "They treat me well."
            kl "Sure, it’s hard work being at sea all the time... but it’s all I’ve ever known."
            scene ch4sc9_048 with dissolve
            kl "If I stayed here with you and father, I'd be letting them down."
            kl "And I would grow to resent you for it."
            scene ch4sc9_047 with dissolve
            kl "I don’t want that. I don't want to resent you."
            scene ch4sc9_046 with dissolve
            mg "Oh, sweetie... I-I understand."
            mg "You have a strong sense of obligation, I can tell."
            mg "Would you be willing to visit us when you're docked here in Luxenford at least?"
            scene ch4sc9_049 with dissolve
            kl "Yes! I'd love to visit whenever possible!"
            kl "As long as father won’t try kidnapping me again!"
            scene ch4sc9_043 with dissolve
            with vpunch
            mg "You have nothing to worry about! Leave your father to me!"
            scene ch4sc9_044 with dissolve
            kl "Mother! Y-You’re embarrassing me in front of [mc]..."
            scene ch4sc9_045 with dissolve
            kl "I’m sorry, Mom. But I need to get back to the ship and help them prepare."
            scene ch4sc9_044 with dissolve
            kl "[mc], I’ll see you back at the ship?"
            scene ch4sc9_a with dissolve
            mc "I’ll walk you back. Just wait for me at the entrance, I need to discuss something with your mom."
            scene ch4sc9_043 with dissolve
            mg "*Hugs tightly* Bye, sweetie. Please be safe!"
            scene black with Dissolve(1.5)
            scene ch4sc9_050 with Dissolve(1.5)
            mc "Maggie, are you sure your husband won’t be a problem?"
            mc "He didn't strike me as someone who is used to accepting defeat."
            scene ch4sc9_051 with dissolve
            mg "Hummh? Oh, my husband?"
            mg "Yes, I'll make sure he accepts the situation."
            mg "He is a stubborn fool, but he must see reason, he has acted poorly in this matter."
            scene ch4sc9_052 with dissolve
            mg "Now, I believe I promised you a reward for bringing my daughter home safely."
            mg "Would you like to see just how grateful a mother can be? Or would you prefer coin?"
            ###Choice###
            menu:
                "Coin will do just fine.":
                    scene ch4sc9_053 with dissolve
                    mc "I’ll take the coins."
                    $ mg_reward_coin = True
                    scene ch4sc9_052 with dissolve
                    mg "*Sigh* I won’t lie... I was hoping you’d pick the other option."
                    mg "It’s been a while..."
                    scene ch4sc9_054 with dissolve
                    mg "Oh well, here’s your coin."
                    mg "Please, look after Kelly out there."
                    scene ch4sc9_053 with dissolve
                    mc "I will. Goodbye, Maggie."
                    stop music fadeout 1.0
                    scene black with Dissolve(2)

                "Show me how grateful you can be. ({color=#ff8cdd}Lewd{/color})":
                    scene ch4sc9_053 with dissolve
                    $ mg_reward_lewd = True
                    stop music fadeout 1.0
                    mc "How about you show me just how grateful you can be."
                    play music lewd_1 fadein 1.0
                    scene ch4sc9_052 with dissolve
                    mg "Mhhh! I was hoping you’d pick this option! I haven't been touched in years..."
                    mg "My husband is always away at sea and when he isn't... he lays with whores..."
                    mg "Which means..."
                    scene ch4sc9_055 with dissolve
                    mc "Which means you're craving a good fuck and your husband isn't doing his duty as a man."
                    mg "*Snickers* Words young man! But I can't deny it..."
                    mg "Why don’t you lose your clothes and join me back here?"
                    scene ch4sc9_056 with dissolve
                    mg "Hurry up, handsome!"
                    mg "We don’t want my husband coming back to interrupt us."
                    scene ch4sc9_053 with dissolve
                    mc "Fuck me. How can her husband neglect an ass like that?"
                    scene black with Dissolve(2)
                    scene ch4sc9_057 with Dissolve(2)
                    "As you turn the corner you see Maggie, standing near the wall, displaying herself for you."
                    mg "Come closer young man... I can feel your gaze but not your touch."
                    scene ch4sc9_058 with dissolve
                    "You walk up behind Maggie, sliding your hand between her perky cheeks."
                    mg "*Moans softly* Ohh... there you are. Is this how you want me?"
                    mc "Mmmh. Now lean against the wall and let me feel you."
                    mg "*Moans* Mnhh! You're naughty, touching a married woman like this..."
                    scene ch4sc9_059 with dissolve
                    mc "You're about to get what you've been waiting for. Brace yourself against the wall."
                    mc "I’m going to make you feel like a woman again."
                    scene ch4sc9_060 with dissolve
                    mg "Y-Yes! Please! I want to feel desired again!"
                    mg "Heavens! Feeling your strong young hands on my waist... Mnhh!"
                    mg "D-Don’t bother with foreplay! I’m already dripping wet for you!"
                    scene ch4sc9_061 with dissolve
                    mg "You've earned this... you reunited me with my sweet Kelly, you deserve this."
                    mg "*Moans* Hhnnn! I-I feel you! Please, {b}fuck me! Claim your prize!{/b}"
                    scene ch4sc9_062 with dissolve
                    with vpunch
                    "You push inside her wet and surprisingly tight pussy. She really hasn’t been fucked in a while."
                    mg "{b}OH! OHhh! Yes!!{/b}"
                    show maggie_f1 with fade
                    $ renpy.pause(2, hard=True)
                    mg "{b}YES! AhhH! FUCK ME!! SHOW ME WHAT A LUSTFUL YOUNG MAN YOU ARE! AIIHHH!!{/b}"
                    with vpunch
                    mg "{b}*Loud moans* AHH! You’re filling me UP! Annhhh!{/b}"
                    mg "Keep ravaging me like this! {b}YESSSS!{/b}"
                    $ renpy.pause()
                    scene ch4sc9_063 with dissolve
                    "You feel her pushing herself against you, matching the pace of each thrust."
                    show maggie_f2 with fade
                    $ renpy.pause(2, hard=True)
                    $ renpy.pause()
                    mg "{b}OH! [mc]!{/b} Hhnngh! You’re so deep!"
                    mg "T-Take your time sweetie... enjoy the warmth and tightness of my pussy- Ahhh..."
                    mc "Fuck Maggie... I can't believe how juicy you are... I need more."
                    mg "D-Do it... fuck me harder! Show me what it means to be fucked by a young stud! AHhH!"
                    show maggie_f3 with fade
                    $ renpy.pause(2, hard=True)
                    $ renpy.pause()
                    "I love feeling your waist clap my cheeks! {b}Ahh!{/b}"
                    mg "D-Don't Stop! {b}DO NOT MnnHh! STOP!{/b}"
                    mg "{b}I’m COMING! Mnhhnh!!! YESS!!{/b}"
                    with vpunch
                    $ renpy.pause(0.5)
                    with vpunch
                    mg "{b}AiiiaahHHh!! I can't stop! I can't stop cumming all over you!!{/b}"
                    with vpunch
                    scene ch4sc9_064 with dissolve
                    mg "*Panting heavily* Ahhh... thank you."
                    mg "*Panting* Hnnh... mmh... I feel like a young woman again."
                    mc "Damn... I knew you were wet... but you completely soaked my cock in your juices. *Chuckles*"
                    scene ch4sc9_065 with dissolve
                    "Maggie reaches behind and you feel her fingers strafe along your cock, as she feels how wet it is."
                    mg "*Giggling* It's your fault for ravaging me like that! A young cock like this... mmh."
                    mg "You filled me up so good! It’s already dripping out..."
                    mc "What can I say? You didn't leave me much choice, given how tightly you squeezed me when you came."
                    scene ch4sc9_066 with dissolve
                    mg "I suppose I did get a little carried away with how good it felt."
                    mg "*Giggles happily* I can't believe how good it felt when you entered me..."
                    mg "I practically lost my mind to the pleasure and thought of having a young man inside me, taking me..."
                    mg "I need a moment... you shouldn't keep Kelly waiting any longer..."
                    mg "And please, promise me you'll keep an eye out for Kelly?"
                    mc "I won't let anything happen to her, Maggie, I give you my word."
                    scene ch4sc9_065 with dissolve
                    mg "*Scoffs happily* I don't know if it's the effect of your warm cum still being deep inside of me..."
                    mg "But... I believe you, [mc], I believe you will keep her safe."
                    mg "*Moans softly* Protect my sweet girl at all cost, and this will be..."
                    mg "One of many rewards I'll bestow upon you... mmh... now go, you have my blessing."
                    scene black with Dissolve(2)

            scene ch4sc9_a1 with dissolve
            play music relax_2 fadein 1.0
            mct "There she is, looking carefree and happy."
            mct "It must've been good for her to see her mother."
            if mg_reward_lewd == True:
                mct "Speaking of her mother... I probably shouldn't tell her what I just did to her."
                mct "*Chuckles* That was quite the reward... I wouldn't mind another next time I see her."

            else:
                mct "It was nice to earn a bit of coin for reuniting them, I guess it pays off to be a decent person."

            scene ch4sc9_a2 with dissolve
            mc "Hey Kelly."
            mc "You ready to head back to the crew?"
            scene ch4sc9_a3 with dissolve
            kl "You bet! Hopefully Pedro isn't too cross with me..."
            kl "I was supposed to help him in the kitchen today."
            scene ch4sc9_a4 with dissolve
            mc "I'm sure he'll understand."
            mc "It's not every day you get kidnapped, is it?"
            scene ch4sc9_a5 with dissolve
            kl "*Giggles* No, no it isn't! Thank the seas for that!"
            kl "But if it were to happen again, I know who will rescue me! *Giggling*"
            scene ch4sc9_a6 with dissolve
            mc "*Chuckles* Oh yeah?"
            mc "What makes you think I'd save your ass again?"
            scene ch4sc9_a7 with dissolve
            kl "Hmnnhh... cause I have a cute ass!"
            scene ch4sc9_a8 with dissolve
            kl "*Giggles*"
            mc "*Chuckles* I mean... I wasn't going to say it like that... but yeah, you do."
            kl "I knew you had taken notice!"
            scene ch4sc9_a7 with dissolve
            kl "And because... you have a good heart."
            scene ch4sc9_a8 with dissolve
            $ renpy.pause(1)
            scene ch4sc9_a9 with dissolve
            kl "Is this okay?"
            "You feel a soft and delicate touch embrace your hand."
            scene ch4sc9_a10 with dissolve
            $ renpy.pause()
            menu:
                "Yeah, I don't mind. ({color=#ff8cdd}Romance{/color})":
                    scene ch4sc9_a7 with dissolve
                    kl "*Giggles* Great!"
                    kl "I've always wanted to hold hands with someone!"
                    $ kelly_trust += 3
                    "Kelly's trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

                "If you must...":
                    scene ch4sc9_a7 with dissolve
                    kl "I must!"

                "No, I'm with someone else.":
                    scene ch4sc9_a7 with dissolve
                    kl "Oh ... I see."

            scene ch4sc9_a9 with dissolve
            kl "[mc]... thank you, Not just for freeing me."
            kl "But for convincing me to see my mother again."
            scene ch4sc9_a11 with dissolve
            kl "I never thought I would see my parents again..."
            kl "I don't remember much from before I was given away... only bits and pieces..."
            scene ch4sc9_a12 with dissolve
            kl "But going forward, I want to visit them..."
            kl "Whenever we're docked here in the capital, I'll visit them."
            scene ch4sc9_a13 with dissolve
            mc "I think that's a good idea."
            mc "My parents, they... they're gone."
            scene ch4sc9_a13 with dissolve
            mc "If I had the chance to see them again, nothing could stop me."
            scene ch4sc9_a14 with dissolve
            kl "Oh? I'm sorry."
            kl "I guess I'm lucky I still can... thank you."
            kl "Sharing that couldn't have been easy. It means a lot to me."
            scene ch4sc9_a15 with dissolve
            kl "If you ever want to talk about it... or anything, really, I'd be happy to listen."
            scene ch4sc9_a16 with dissolve
            mc "Thank you, Kelly. I... I'll remember that."
            kl "..."
            scene ch4sc9_a17 with dissolve
            kl "Enough mushiness! *Giggles* Let's race back to the ship!"
            scene ch4sc9_a18 with dissolve
            kl "Loser has to wash winner's dirty laundry for a week!"
            mc "H-Hey! That's cheating!"
            kl "*Laughs* Afraid a little girl is going to beat you?"
            kl "You better hurry! I have quite the stack of used panties that need a thorough wash! *Snickers*"
            mc "*Chuckles* Oh it's on little lady!"
            scene black with Dissolve(2)

    $ renpy.pause(1)
    "You and Kelly sprint back to the docks and board the Banshee with the setting sun on the horizon."
    scene ch4sc08_061 with Dissolve(2)
    play music summon_3 fadein 1.0
    $ renpy.pause(1)
    mc "Hey Ki- sorry, Captain."
    mc "Kelly is back, safe and sound... she's helping Pedro prepare dinner."
    scene ch4sc08_065 with dissolve
    ki "..."
    ki "Took you long enough."
    scene ch4sc08_066 with dissolve
    ki "Did you get lost or something?"
    ki "Don't tell me you expect a medal?"
    scene ch4sc08_067 with dissolve
    mc "Whatever. I didn’t do it for you."
    scene ch4sc08_068 with dissolve
    mc "Now, I have an overdue appointment with my bed."
    mc "If there’s any more trouble before dawn. Don’t bother waking me."
    scene ch4sc08_065 with dissolve
    ki "..."
    ki "Kira."
    mc "Hmh?"
    scene ch4sc08_066 with dissolve
    ki "Call me Kira."
    ki "Captain is for the crew and you're no-"
    scene ch4sc08_068 with dissolve
    mc "I’m not part of your crew."
    mc "I’m well aware… as you keep reminding me."
    mc "Next time you need a stranger to sort out your messes, don't come to me."
    scene ch4sc08_069 with dissolve
    kit "Arrh! Bloody-waters! W-why did I say that?!"
    kit "'Call me Kira'?"
    kit "What am I? Some weak landlubber?! S-Some little teenage girl!? Ugh!"
    kit "I should’ve cut out his tongue for talking back to me!"
    scene ch4sc08_070 with dissolve
    kit "*Deep sigh* He brought Kelly back, unharmed."
    kit "He hasn't even asked for a reward for his service? What is his deal?!"
    kit "Hnngh..."
    scene ch4sc08_071 with dissolve
    kit "Maybe he isn't so terrible?"
    kit "He doesn't act like other men I've encountered..."
    scene ch4sc08_072 with dissolve
    kit "[mc]..."
    kit "You're a mystery..."
    kit "*Giggles softly* ..."
    scene black with Dissolve(2)
    stop music fadeout 1.0
    scene ch4sc9_067 with Dissolve(2)
    play music relax_2 fadein 1.0
    mct "I don’t imagine the beds are going to be comfortable."
    mct "But at this point, I don’t give a goblin-shit. I need this day to be over."
    scene ch4sc9_068 with dissolve
    mct "*Sigh* Hmm. Bed seems more accommodating than I thought."
    mct "Not that it matters. I’m going to sleep like a log either way."
    scene ch4sc9_069 with dissolve
    fy "Hey cuz! You’re finally back."
    fy "I was starting to wonder if you'd make it in time!"
    scene ch4sc9_070 with dissolve
    mc "Hey Flynn. You've got us all set up?"
    scene ch4sc9_071 with dissolve
    fy "You know it! And Kira only threatened to cut my privates off twice since you left!"
    fy "I’m definitely making progress with her!"
    scene ch4sc9_070 with dissolve
    mc "I’m sure she is dropping onto her bed as we speak, swooning over having you onboard her ship…"
    scene ch4sc9_071 with dissolve
    fy "You really think so?!"
    fy "Bah! I know you’re messing with me, cuz!"
    scene ch4sc9_072 with dissolve
    fy "But could you imagine... a woman like her... desiring you?"
    fy "She probably has hundreds of kills under her belt. But when her soft touch reaches your skin..."
    fy "Everything else melts away! Ahh."
    scene ch4sc9_070 with dissolve
    mc "Getting a little carried away, aren’t you? Just get some sleep, Flynn."
    mc "Tomorrow is a new day, and you should probably avoid Kira for a while."
    mc "Maybe stick to socializing with some of the other crew. Kelly, the girl I brought back, seems friendly."
    scene ch4sc9_071 with dissolve
    fy "She definitely is! I met her when she came back aboard earlier! What a beauty, cuz!"
    scene ch4sc9_072 with dissolve
    fy "I think I’m in love!"
    scene ch4sc9_073 with dissolve
    fy "She isn’t as fiery as Kira, but she has that innocent girl-next-door thing going on."
    scene ch4sc9_074 with dissolve
    fy "And her breasts! Oh my! How does a little thing like her achieve such... volume?"
    fy "Imagine how soft they must be! Like giant pillows!"
    fy "Could you imagine sleeping on those puppies? Oh what dreams I'd hav-"
    kl "*Clears throat* Ahrrem!"
    scene ch4sc9_075 with dissolve
    $ renpy.pause()
    fy "She’s behind me, isn’t she?"
    mc "*Laughs* Yup!"
    scene ch4sc9_076 with dissolve
    kl "*Giggles* Hiiii Flynn!"
    kl "I know I didn’t just hear you talking about my 'volume', right?"
    kl "That wouldn’t be in keeping with the fine gentleman I met earlier."
    scene ch4sc9_075 with dissolve
    with vpunch
    mc "*Laughs*"
    fy "K-Kelly!! No I-I wasn’t saying anything bad!"
    fy "Just-... {b}GOODNIGHT!{/b}"
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc9_077 with Dissolve(2)
    kl "Hi [mc]..."
    kl "I guess it's just the two of us left..."
    scene ch4sc9_078 with dissolve
    mc "Hey, Kelly."
    mc "It would seem so..."
    scene ch4sc9_077 with Dissolve(1)
    kl "Have you... settled in yet?"
    mc "Yeah, sort of, it's my first time on a ship, it's honestly better than I expected."
    kl "Good... that's good, I'm glad..."
    mct "I can't tell if she's fishing for a connection or if she just wants to go to bed and be done with today."
    ####Choice####
    menu:
        "Ask how she’s doing. ({color=#ff8cdd}Romance{/color} / {color=#2bff8b}Friendship{/color})":
            scene ch4sc9_078 with dissolve
            mc "Sorry about Flynn… He is a little over the top... but he means well, he's not a creeper."
            mc "How are you holding up after everything with your parents?"
            scene ch4sc9_079 with dissolve
            kl "It’s sweet of you to ask."
            kl "Most of the men I deal with... being part of a crew and all..."
            kl "Well, let’s just say they don’t bother to ask how I’m feeling. Ever."
            scene ch4sc9_080 with dissolve
            mc "They should."
            kl "..."
            "A slight smile appears on Kelly, she clearly appreciates you showing interest in her life."
            scene ch4sc9_081 with dissolve
            kl "S-So…"
            kl "Uhhm…"
            kl "It looks like we’re bunkmates."
            scene ch4sc9_082 with dissolve
            mc "Yeah, it looks like it."
            mc "I hope you don’t snore…"
            scene ch4sc9_083 with dissolve
            kl "Fat chance!"
            kl "If anyone snores it would be you! Definitely so! And you better not or else... I'll pillow-smack you!"
            mc "*Chuckles* ..."
            scene ch4sc9_082 with dissolve
            kl "*Giggles* ..."
            scene ch4sc9_084 with dissolve
            kl "Uhhh, [mc]?"
            kl "I-I’m actually happy you’re here."
            kl "Not just on this ship, but knowing you'll be right next to me while I sleep. I feel a bit safer."
            scene ch4sc9_082 with dissolve
            kl "Lately I've felt like I'm being watched... it's creeping me out."
            kl "I think it might be Louie, he's always been a bit... strange, but I can't prove anything."
            scene ch4sc9_084 with dissolve
            kl "So... I'm glad you'll be sleeping with me for the foreseeable future."
            kl "I'd hate to be on my own... especially after the kidnapping as well."
            scene ch4sc9_081 with dissolve
            kl "Does that sound weird?"
            scene ch4sc9_080 with dissolve
            mc "No, not really."
            mc "It sounds completely normal after what you’ve been through today."
            mc "You’ve held it together surprisingly well... I suppose life at sea has toughened you up."
            scene ch4sc9_081 with dissolve
            kl "I’d like to think so!"
            kl "But I don’t always feel so tough... honestly, I’ve felt alone for most of my life."
            scene ch4sc9_079 with dissolve
            kl "I only joined Kira and Pearl’s crew three years ago, when I was fifteen."
            kl "Up until then, it was very lonely."
            scene ch4sc9_080 with dissolve
            "A forced smile surfaces on Kelly’s face…"
            scene ch4sc9_085 with dissolve
            kl "Ah! Listen to me babbling on about my sob-story, I’m sure you don’t want to be bothered with that."
            scene ch4sc9_078 with dissolve
            mc "I don’t mind it. If we’re going to be bunkmates for the next couple of moons..."
            mc "It wouldn't hurt to get to know each other better."
            scene ch4sc9_082 with dissolve
            $ renpy.pause()
            scene ch4sc9_083 with dissolve
            kl "*Excitedly* Yes! Brilliant!!"
            scene ch4sc9_084 with dissolve
            kl "Let’s get comfy first, though! *Giggles*"
            scene ch4sc9_080 with dissolve
            kl "..."
            scene ch4sc9_081 with dissolve
            kl "R-Right! We should probably undress!"
            scene ch4sc9_086 with dissolve
            $ renpy.pause(1)
            "You begin undressing, not paying much attention to Kelly."
            "Although seeing you undress right in front of her is clearly drawing her attention."
            scene ch4sc9_087 with dissolve
            $ renpy.pause()
            scene ch4sc9_088 with dissolve
            $ renpy.pause()
            scene ch4sc9_089 with dissolve
            $ renpy.pause()
            mc "Kelly?"
            kl "."
            kl ".."
            kl "..."
            scene ch4sc9_090 with dissolve
            kl "Huh! Whhah?"
            kl "I-I... {b}!!!{/b}"
            scene ch4sc9_091 with dissolve
            kl "I promise I wasn’t staring!!"
            scene ch4sc9_089 with dissolve
            kl "..."
            scene ch4sc9_091 with dissolve
            kl "O-Okay, I was! But-but it’s because of all those scars!"
            scene ch4sc9_092 with dissolve
            kl "Uh-huh... Not because of how incredibly handsome you are."
            scene ch4sc9_091 with dissolve
            with vpunch
            kl "{b}Urrh!{/b} Not that you aren’t handsome!"
            kl "{b}Arrh!{/b} I mean- You are! Very, very, very much so!!"
            scene ch4sc9_084 with dissolve
            $ renpy.pause()
            mc "Kelly... take a deep breath."
            scene ch4sc9_082 with dissolve
            kl "R-Right! *Inhales deeply*"
            scene ch4sc9_084 with dissolve
            kl "*Exhales* Haahhh... sorry about that."
            mct "*Chuckles* She's cute, getting all flustered seeing me undress?"
            mc "It's quite alright. I suppose I should’ve warned you about my scars."
            scene ch4sc9_082 with dissolve
            kl "It’s O-Okay! Just don’t let it happen again! *Giggles*"
            kl "I suppose I should undress as well now."
            scene ch4sc9_084 with dissolve
            mc "Unless you plan on sleeping in that attire, I suppose you should."
            mc "Want me to turn around?"
            scene ch4sc9_092 with dissolve
            kl "N-No..."
            kl "*Mumbles* It’s alright, I-I want you to see me."
            scene ch4sc9_084 with dissolve
            "Kelly nervously unties her straps. Once loose, she lets her shirt drop to the floor."
            scene ch4sc9_093 with dissolve
            $ renpy.pause()
            scene ch4sc9_094 with dissolve
            $ renpy.pause()
            kl "I-I..."
            scene ch4sc9_095 with dissolve
            kl "[mc], What do you think? A-Am I pretty?"
            kl "I know I’m a little out of proportion for my body size..."
            kl "Flynn was making comments... but I didn't hear you say anything? Did you not find me attractive?"
            ####Choice####
            menu:
                "You’re beautiful. ({color=#ff8cdd}Romance{/color})":
                    scene ch4sc9_095 with dissolve
                    mc "Kelly. There’s nothing wrong with you."
                    mc "Not in the slightest... you’re immensely beautiful…"
                    scene ch4sc9_094 with dissolve
                    mc "Yes, your breasts have a little more... magnitude, than most girls your size."
                    scene ch4sc9_095 with dissolve
                    mc "But I think that only adds to you being uniquely breathtaking."
                    scene ch4sc9_096 with dissolve
                    kl "Breathtaking?"
                    kl "That’s so sweet! You really like them then!"
                    mc "*Chuckles* Yes, Kelly... I really like your gorgeous breasts."
                    scene ch4sc9_097 with dissolve
                    kl "Thank you! *Giggles softly* Oh that's such a relief!"
                    kl "I’m going to sleep so much better now!"
                    $ kelly_trust += 2
                    "Kelly is happy that you find her attractive, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                    scene black with Dissolve(2)
                    $ renpy.pause(1)
                    scene ch4sc9_098 with Dissolve(2)
                    $ renpy.pause()
                    scene ch4sc9_099b with dissolve
                    kl "*Whispers* {size=-10}{b}Psst! [mc], you awake?{/b}{/size}"
                    scene black with Dissolve(2)
                    $ renpy.pause(1)
                    scene ch4sc9_099b with Dissolve(2)
                    kl "*Whispers* {size=-10}{b}[mc]?{/b}{/size}"
                    scene ch4sc9_099 with dissolve
                    $ renpy.pause(1.3)
                    scene ch4sc9_0100 with dissolve
                    mc "Kelly? Can’t sleep?"
                    scene ch4sc9_099 with dissolve
                    kl "Y-Yeah... I had a bad dream."
                    kl "Would you mind if I... Uhh..."
                    scene ch4sc9_0101 with dissolve
                    kl "You know... uhh... I wanted to ask you something..."
                    kl "Maybe it's a little inappropriate, but... mhh... uhh..."
                    scene ch4sc9_0100 with dissolve
                    mc "You want to sleep in my bunk, don’t you?"
                    scene ch4sc9_099 with dissolve
                    kl "*Excitedly* {b}Yes!!{/b}"
                    kl "I-I mean, if you don’t mind?"
                    scene ch4sc9_0101 with dissolve
                    kl "I want to fall asleep in the safety of my rescuer's arms."
                    kl "You’re the only man I’ve ever felt safe with."
                    ####Choice####
                    menu:
                        "Accept. (Kelly {color=#ff8cdd}Romance{/color})":
                            scene ch4sc9_0100 with dissolve
                            $ kelly_sex = True
                            mc "Of course you can."
                            mc "If I ever say no to you while you’re asking me, naked, feel free to punch me."
                            scene ch4sc9_0102 with dissolve
                            kl "*Giggles* Oh my! I completely forgot I'm butt naked!"
                            "Kelly likes knowing seeing her naked has an effect on you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                            $ kelly_trust += 2
                            kl "Hopefully you don’t mind?"
                            scene ch4sc9_0100 with dissolve
                            mc "No. I definitely don’t."
                            scene ch4sc9_0103 with dissolve
                            $ kelly_path = True
                            kl "In that case! Make some room for your favorite crewmate!"
                            kl "I might be tiny but my breasts require... substantial space!"
                            scene black with Dissolve(2)
                            "She climbs into your bunk effortlessly and cuddles herself tightly against you."
                            scene ch4sc9_0104 with Dissolve(2)
                            kl "Ahhhh! This is quite an improvement from my own bunk."
                            kl "I feel immensely better already! So... warm."
                            mct "*Chuckles* I'd have to agree... having her cuddle up to me, pressing her naked body against me, definitely an improvement."
                            scene ch4sc9_0105 with dissolve
                            kl "I haven’t felt this relaxed since... well, ever!"
                            kl "You know, I’ve never been naked with a man before."
                            kl "Kira says men only want bad things."
                            scene ch4sc9_0106 with dissolve
                            kl "But you make me feel safe. I even liked when you looked at my breasts…"
                            scene ch4sc9_0105 with dissolve
                            kl "It was exciting, to be honest!"
                            scene ch4sc9_0107 with dissolve
                            mc "They are very appealing, just like the rest of you."
                            mc "You’re a beautiful girl. You'll make any man you choose incredibly happy."
                            scene ch4sc9_0106 with dissolve
                            kl "Mhmm... I want to make you happy, [mc]."
                            scene ch4sc9_0105 with dissolve
                            kl "I want to thank you. Not just for saving me..."
                            scene ch4sc9_0106 with dissolve
                            kl "But for being so kind and warm to me."
                            kl "For being a real man, who respects me and haven't forced himself onto me."
                            scene ch4sc9_0107 with dissolve
                            mc "Kelly. You don’t need to thank-"
                            scene ch4sc9_0108 with dissolve
                            kl "*Kiss* Mhhm..."
                            "Before you can finish your sentence, she gently rubs her soft thigh against your crotch..."
                            scene ch4sc9_0109 with dissolve
                            $ renpy.pause()
                            "And her warm wet lips move down to trail kisses across your chest as her thumb playfully toys with your nipple."
                            $ kelly_bj = True
                            scene ch4sc9_0108 with dissolve
                            $ renpy.pause(1.3)
                            scene ch4sc9_0109 with dissolve
                            $ renpy.pause(1.3)
                            kl "*Moans softly* Nhhhh… *Kisses* Mwaah. Mwh."
                            scene ch4sc9_0108 with dissolve
                            mc "Kelly... *Grunts* Mhhm…"
                            scene ch4sc9_0110 with dissolve
                            kl "You were saying?"
                            mc "I... I was just saying how much I- enjoy the way you express your gratitude."
                            scene ch4sc9_0108 with dissolve
                            "She rubs her thigh against your crotch once again."
                            scene ch4sc9_0109 with dissolve
                            kl "Thennn... I'd better, mmhh... Thannkhh... you properly."
                            scene ch4sc9_0110 with dissolve
                            kl "What is that rubbing against my thigh, I wonder?"
                            kl "I'd better take a look... Let me get you out of these uncomfortable pants."
                            scene black with Dissolve(2)
                            stop music fadeout 1.0
                            scene ch4sc9_0111 with Dissolve(2)
                            play music lewd_1 fadein 1.0
                            kl "{b}Oh!{/b} My goodness! It’s throbbing against my thigh!!"
                            kl "I didn’t expect it to be so warm... or this thick!"
                            scene ch4sc9_0112 with dissolve
                            kl "Is that supposed to all fit inside me? I’m-... {b}tiny!{/b}"
                            kl "My breasts might be large, but down there... I'm little."
                            scene ch4sc9_0111 with dissolve
                            kl "I can barely fit two of my own fingers, and they are small..."
                            scene ch4sc9_0113 with dissolve
                            mc "It gets bigger..."
                            scene ch4sc9_0112 with dissolve
                            kl "Yeah, right!"
                            scene ch4sc9_0113 with dissolve
                            mc "You'll see soon enough."
                            scene ch4sc9_0114 with dissolve
                            kl "{b}No way!!?{/b}"
                            kl "Nuh-uh! Don’t believe it! How?!"
                            scene ch4sc9_0113 with dissolve
                            mc "Well, you can find out if you touch it. Or put it in your mouth..."
                            scene ch4sc9_0114 with dissolve
                            kl "M-My mouth? But... it’s huge!"
                            scene ch4sc9_0112 with dissolve
                            kl "Would it make you happy if I... did that?"
                            scene ch4sc9_0115 with dissolve
                            $ renpy.pause ()
                            "Before you answer, she has already begun wrapping her little hand around your cock."
                            kl "Like this? Does this feel good, [mc]?"
                            mc "F-Fuck... Yes... Kelly, that's amazing."
                            scene ch4sc9_0116 with dissolve
                            $ renpy.pause ()
                            kl "{b}*Gasps* It’s growing!!{/b}"
                            with vpunch
                            kl "*Grabs tightly* I can’t believe it! You were right!"
                            mc "*Grunts* Aahhh..."
                            kl "It feels so firm and strong... Is it okay if I take a closer look?"
                            mc "By all means... I’m literally in your hands."
                            scene ch4sc9_0117 with dissolve
                            $ renpy.pause ()
                            kl "Woah..."
                            scene ch4sc9_0118 with dissolve
                            kl "Seriously! Look how big it is compared to my fingers."
                            kl "I can barely grip it!"
                            scene ch4sc9_0119 with dissolve
                            kl "*Giggles* I wonder what it tastes like?"
                            kl "Could I?"
                            scene ch4sc9_0118 with dissolve
                            kl "Heavens! I couldn’t! Right?"
                            kl "It would be so naughty..."
                            kl "I suppose I already am. Touching you like this ... naked."
                            mc "If you want to, I’m okay with it. Just remember it’s sensitive."
                            scene ch4sc9_0117 with dissolve
                            "Squished against you like this, you can feel her heartbeat increasing rapidly."
                            scene ch4sc9_0119 with dissolve
                            kl "O-Okay! I’m doing it!"
                            kl "I’m going to... put you in my mouth!"
                            kl "Please tell me if I’m doing it right, I haven’t done anything like this before."
                            mc "Go on."
                            scene black with Dissolve(2)
                            "She swiftly repositions herself."
                            scene ch4sc9_0120 with Dissolve(2)
                            $ renpy.pause ()
                            kl "Whau! It’s a little scary up close."
                            kl "But also... oddly enticing?"
                            kl "This will make you happy, right?"
                            scene ch4sc9_0121 with dissolve
                            mc "It’s one of the best feelings a man can experience. So yes... you would make me happy."
                            klt "Good... I really want to make him happy."
                            klt "He saved me from my father."
                            klt "And he's been a perfect gentleman the entire time... he even reunited me with my mom."
                            klt "He hasn't asked anything of me... he hasn't even been inappropriate."
                            scene ch4sc9_0122 with dissolve
                            klt "Not one sleazy remark or attempt to grope me."
                            klt "He isn’t like the other men I've encountered... he's better."
                            scene ch4sc9_0123 with dissolve
                            $ renpy.pause ()
                            kl "*Blows air*"
                            mc "Ahh..."
                            scene ch4sc9_0124 with dissolve
                            $ renpy.pause ()
                            kl "*Kiss* Mhww…"
                            ######ANIMATION######
                            show kelly_bj1 with fade
                            $ renpy.pause(2, hard=True)
                            $ renpy.pause ()
                            kl "{b}*Moans* MhHhmM!!{/b}"
                            klt "Fuck! He Mhhmh! So Hnhh! {b}BIG!!{/b}"
                            klt "He tastes Nhhn… So delicious! Mhm!"
                            klt "I want to do this- {b}MhMH!{/b} For him every Hnhhmm! {b}NIGHT!{/b}"
                            klt "{b}Yes!!{/b} Mnnhh! That would- Nnhnh... Make him- Happy mnnh..."
                            scene ch4sc9_0125 with dissolve
                            kl "{b}*Muffled moans* Mnhh! NhhnHh!{/b}"
                            ######ANIMATION######
                            show kelly_bj2 with fade
                            $ renpy.pause(2, hard=True)
                            $ renpy.pause ()
                            mc "*Grunts* Fuck… Kelly- AhHh... You’re a natural."
                            klt "He likes it! He really likes it! {b}MmNNh!{/b}"
                            klt "*Sucks harder* I’m Hnhnghh! I’m going to make you, Mmnhh... {b}Really happy!{/b}"
                            "Kelly tightens her young, wet, lips around your cock while she begins swirling her warm tongue around your tip."
                            klt "He’s throbbing inside my mouth! {b}NhnHHn!{/b}"
                            klt "{b}Cum for me [mc]!!{/b} Show me how much you enjoy being inside my mouth!"
                            kl "{b}*Moans & Sucks* MHmmHH! NhHHnnngh!{/b}"
                            mc "{b}F-Fuck Kelly!{/b} I’m going to-"
                            with vpunch
                            $ renpy.pause (0.7)
                            with vpunch
                            $ renpy.pause (0.7)
                            with vpunch
                            $ renpy.pause (0.7)
                            "You fill her mouth with cum but she doesn't stop immediately. You can feel her thoroughly licking your cock clean."
                            scene ch4sc9_0125 with dissolve
                            "After she’s done, she snuggles up to you once more."
                            scene black with Dissolve(2)
                            scene ch4sc9_0126 with Dissolve(2)
                            kl "That was..."
                            scene ch4sc9_0127 with dissolve
                            mc "Incredible."
                            scene ch4sc9_0126 with dissolve
                            kl "{b}YES!{/b} It was so much better than I thought it would be."
                            kl "*Giggles* Kira always yappers on and on about how nasty men are..."
                            kl "But you weren't nasty... you were yummy!"
                            scene ch4sc9_0127 with dissolve
                            mc "*Chuckles* Good to hear..."
                            scene ch4sc9_0126 with dissolve
                            kl "At first I just wanted to make you happy."
                            kl "But once I had you in my mouth… I couldn’t stop myself *Giggles*"
                            scene ch4sc9_0127 with dissolve
                            mc "No complaints here."
                            scene ch4sc9_0126 with dissolve
                            kl "*Sleepy yawn* Ahhhh… Happy… G-Goodnight."
                            scene ch4sc9_0127 with dissolve
                            mc "Goodnight, Kelly."
                            "Kelly feels closer to you, she's happy you decided to accept her, her trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                            $ kelly_trust += 2
                            stop music fadeout 1.0
                            scene black with Dissolve(2)

                        "Decline. ({color=#2bff8b}Friendship{/color})":
                            scene ch4sc9_0100 with dissolve
                            mc "I don’t think that’s a good idea Kelly…"
                            mc "We barely know each other and I don’t want to take advantage of you."
                            mc "Besides, if Kira found out I messed around with her crew, she'd probably have me fed to the sharks."
                            scene ch4sc9_0101 with dissolve
                            kl "O-Okay... I get it."
                            kl "I’ll try to get some sleep then."
                            stop music fadeout 1.0
                            scene black with Dissolve(2)

                "Not my type.":
                    scene ch4sc9_095 with dissolve
                    mc "Of course you're pretty. And there's certainly nothing wrong with being gifted so generously."
                    mc "But... I'm sorry. I can't let myself be distracted right now. I'm not here on a pleasure cruise."
                    scene ch4sc9_096 with dissolve
                    kl "T-That’s okay... I had a feeling. Let’s get some sleep!"
                    scene ch4sc9_097 with dissolve
                    kl "I hope we won't have to get up early... I really want to sleep in!"
                    scene black with Dissolve(2)


        "Let her be. (Neutral)":
            scene ch4sc9_078 with dissolve
            mc "I don’t know about you but I’m about to pass out."
            mc "I'll see you tomorrow, Kelly."
            scene ch4sc9_077 with dissolve
            kl "Totally! Nighty night."
            scene black with Dissolve(2)



    scene ch4sc9_0129b with Dissolve(2)
    $ renpy.pause ()
    scene ch4sc9_0129 with dissolve
    mct "Ugh... I can’t sleep."
    mct "Some fresh air might do the trick."
    scene ch4sc9_0130 with dissolve
    $ renpy.pause ()
    scene ch4sc9_0131 with dissolve
    $ renpy.pause (1.3)
    mct "Huh. Is that... ?"
    scene ch4sc9_0132 with dissolve
    play music relax_1 fadein 1.0
    $ renpy.pause ()
    scene ch4sc9_0133 with dissolve
    $ renpy.pause (0.5)
    #####ANIMATION#####
    scene pearl_moonlight with dissolve
    $ renpy.pause(2, hard=True)
    mct "It’s definitely Pearl."
    mct "Damn..."
    mct "Flynn wasn’t exaggerating when he raved on about Pearl and Kira's beauty."
    mct "The way the moonlight highlights her tan skin against the darkened skies..."
    mct "Not to mention her curves... the way she carries herself... she’s beautiful and she knows it."
    mct "According to Flynn, she's reputed to be a skilled fighter just like her sister."
    mct "It’s hard to imagine someone so mesmerizing being that deadly."
    mct "Guess it’s time I head back below deck and get some rest."
    scene ch4sc9_0133 with dissolve
    $ renpy.pause (1.3)
    stop music fadeout 1.0
    scene ch4sc9_0134 with dissolve
    pl "Aren't you going to join me?"
    mct "She noticed me? She's got a strong sense of her surroundings."
    play music summon_2 fadein 1.0
    mc "Sure, if you don't mind."
    scene ch4sc9_0135 with dissolve
    $ renpy.pause (1.3)
    pl "I like to come out here at night."
    scene ch4sc9_0136 with dissolve
    mc "I can see why."
    mc "It’s... serene."
    scene ch4sc9_0135 with dissolve
    pl "*Giggles* Serene? Is that your way of saying it’s beautiful?"
    scene ch4sc9_0136 with dissolve
    mc "No. It means calming. Or soothing…"
    scene ch4sc9_0135 with dissolve
    pl "Oh! I see."
    pl "Yeah, I suppose it is soothing."
    pl "Serene... *Giggles softly* Yes, serene."
    scene ch4sc9_0136 with dissolve
    pl "I come here for the sounds mostly. The gentle lapping of the sea against the ship..."
    pl "The sighing of the wind as it flows across the sails."
    scene ch4sc9_0135 with dissolve
    pl "It’s like my senses are... magnified somehow."
    pl "There's just something about being out at night..."
    pl "It makes me feel-"
    scene ch4sc9_0136 with dissolve
    mc "Alive?"
    pl "Alive, yes."
    pl "Hmm, you're a curious one."
    mc "*Chuckles* As are you..."
    scene ch4sc9_0137 with dissolve
    $ renpy.pause (1.3)
    scene ch4sc9_0138 with dissolve
    pl "A pearl for your thoughts?"
    scene ch4sc9_0137 with dissolve
    mc "*Chuckles* Clever..."
    scene ch4sc9_0138 with dissolve
    pl "Something keeping you up?"
    pl "Maybe... the reason you’re on our ship?"
    mct "She comes off as aloof, but she's much more perceptive than I initially anticipated."
    scene ch4sc9_0137 with dissolve
    mc "You’re observant."
    scene ch4sc9_0138 with dissolve
    pl "Call it intuition."
    scene ch4sc9_0137 with dissolve
    mc "Well... you've pretty much guessed it."
    mc "The reason I'm aboard the Bloody Banshee and heading to Inmortui..."
    scene ch4sc9_0138 with dissolve
    pl "It’s to help someone? Someone you care about?"
    scene ch4sc9_0137 with dissolve
    mc "Yeah, how did you-"
    mc "Intuition. Right."
    scene ch4sc9_0138 with dissolve
    pl "You helped Kelly without a second thought, very... masculine."
    pl "You're a protector, a provider, that's why you're out here as well, to provide and protect."
    scene ch4sc9_0137 with dissolve
    mc "*Chuckles* I guess you've got me all figured out, huh?"
    scene ch4sc9_0139 with dissolve
    $ renpy.pause (1)
    "Pearl turns and looks directly at you."
    scene ch4sc9_0140 with dissolve
    pl "You’re interesting."
    pl "On first impression, you don't seem like someone who'd go out of his way to help people."
    pl "And yet, you’re here to help someone you care about."
    scene ch4sc9_0139 with dissolve
    pl "..."
    scene ch4sc9_0140 with dissolve
    pl "I like that you helped Kira recover Kelly, you didn't know Kelly, and Kira... well-"
    pl "Kira has been... less than friendly to you."
    scene ch4sc9_0137 with dissolve
    pl "..."
    scene ch4sc9_0140 with dissolve
    pl "You have layers…"
    scene ch4sc9_0139 with dissolve
    mc "Layers?"
    scene ch4sc9_0140 with dissolve
    pl "Like an onion!"
    scene ch4sc9_0141 with dissolve
    pl "*Giggles*"
    mc "Great. I’ve always dreamed of being an onion."
    scene ch4sc9_0140 with dissolve
    pl "A cute onion!"
    scene ch4sc9_0139 with dissolve
    pl "..."
    scene ch4sc9_0140 with dissolve
    pl "[mc], What's your story?"
    scene ch4sc9_0137 with dissolve
    mc "*Sigh* ..."
    mc "We’re really doing this?"
    scene ch4sc9_0138 with dissolve
    pl "Kira says the voyage to Inmortui will take somewhere between one to two moons."
    pl "We might as well get to know each other? The ship isn't that big."
    scene ch4sc9_0139 with dissolve
    mct "She’s got a point. And she’s certainly friendlier than her sister."
    mc "Alright. I’ll start from the beginning."
    scene ch4sc9_0140b with dissolve
    $ renpy.pause ()
    scene ch4sc9_0142 with dissolve
    pl "Woah! No way. He killed your parents AND he crippled Eliza?"
    pl "You’ve had to endure so much. Ever since you were a boy..."
    scene ch4sc9_0143 with dissolve
    pl "All these scars..."
    pl "They carry such painful memories."
    scene ch4sc9_0144 with dissolve
    $ renpy.pause ()
    scene ch4sc9_0140 with dissolve
    pl "But they are also signs that you are a survivor."
    pl "A brave soul who will do anything for those he cares about."
    scene ch4sc9_0137 with dissolve
    mc "You’re giving me too much credit. I’ve hurt people too."
    mc "Most of them were bad, but some of them weren't. Innocents."
    scene ch4sc9_0138 with dissolve
    pl "Sounds like you’re carrying around a lot of guilt."
    scene ch4sc9_0136 with dissolve
    pl "I've hurt a lot of bad people too. And like you..."
    pl "Some innocents have also been caught in the crossfire."
    scene ch4sc9_0135 with dissolve
    pl "It's something we'll carry with us for the rest of our lives."
    mc "Rest of our lives, huh?"
    scene ch4sc9_0136 with dissolve
    pl "Yeah. Unless you’re a cold blooded killer with no sign of remorse."
    pl "But then, you wouldn’t be lugging around all the guilt, would you? Besides…"
    scene ch4sc9_0138 with dissolve
    pl "When I touched your chest just now, I could tell it's definitely not cold blood in your veins..."
    pl "You were surprisingly warm to the touch."
    scene ch4sc9_0137 with dissolve
    pl "..."
    mc "You know, you might have everyone else fooled..."
    scene ch4sc9_0139 with dissolve
    mc "But this flirty and dumbed-down version of yourself is clearly a front."
    pl "..."
    scene ch4sc9_0140 with dissolve
    pl "Got me all figured out, have you?"
    scene ch4sc9_0139 with dissolve
    mc "No, far from it."
    mc "You’re an onion too."
    scene ch4sc9_0140 with dissolve
    pl "*Giggles softly* Am I... a cute onion?"
    scene ch4sc9_0139 with dissolve
    mc "Very."
    scene ch4sc9_0137 with dissolve
    mc "There’s more to you than meets the eye."
    scene ch4sc9_0139 with dissolve
    mc "You're wickedly smart, and cunning too."
    mc "You mask it very well, so I’m not surprised others don’t catch on."
    scene ch4sc9_0144 with dissolve
    mc "Obviously, you’re incredibly beautiful."
    mc "I suspect you'd give most princesses a run for their money."
    pl "..."
    plt "He needs to stop saying these things!"
    scene ch4sc9_0139 with dissolve
    mc "I suppose that’s why you’re so flirty? You can leverage your looks against males."
    mc "And since the world of pirates and sailors is dominated by men, any edge you can find against them is useful."
    scene ch4sc9_0138 with dissolve
    pl "Hmh. Perceptive…"
    scene ch4sc9_0137 with dissolve
    mc "One thing I haven’t figured out, though."
    mc "Why are you flirting with me? You have nothing to gain."
    pl "..."
    scene ch4sc9_0140 with dissolve
    pl "I flirt with you 'cause it’s fun! Obviously!"
    pl "How am I supposed to resist a cute onion?"
    pl "*Giggles* Peeling layers is fun! Mh-hm!"
    scene ch4sc9_0144 with dissolve
    plt "He’s wrong."
    plt "I do have something to gain..."
    scene ch4sc9_0139 with dissolve
    plt "Him."
    scene ch4sc9_0136 with dissolve
    pl "It’s going to be dawn soon."
    mc "Damn. Time really flies, huh?"
    scene ch4sc9_0135 with dissolve
    pl "Yeah. Sure does, thank you for keeping me company."
    pl "It was... pleasant."
    scene ch4sc9_0136 with dissolve
    mc "Yeah, thanks for the chat. It felt good to have someone to talk to."
    pl "Same time tomorrow then?"
    mc "*Chuckles* Sounds good."
    scene black with dissolve
    "You get up and begin to head back"
    scene ch4sc9_0134 with dissolve
    pl "Night night, Onion!"
    scene ch4sc9_0133 with dissolve
    mc "Goodnight, Pearl."
    scene ch4sc9_0132 with dissolve
    mct "Interesting girl."
    mct "I enjoyed getting to know her, cute little onion... *Chuckles*"
    scene ch4sc9_0145 with dissolve
    $ renpy.pause ()
    plt "H-He really sees me."
    "Pearl felt seen by you, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
    $ pearl_trust += 3
    plt "I know Kira likes him..."
    scene ch4sc9_0146 with dissolve
    plt "But so do I... I really like him."
    plt "I have a feeling about him... I can't quite put my finger on it, but I like him!"
    plt "Neither of us has ever liked a guy... and now we fancy the same guy? Being twins is complicated!"
    plt "I only touched his chest with the tip of my finger, but he was so warm? Almost radiating heat..."
    scene ch4sc9_0147 with dissolve
    plt "I wonder..."
    plt "How would it feel if he touched me?"
    plt "Taking me in his arms…"
    plt "I’ve never let anyone touch me. Kira would definitely kill him, if he did."
    scene ch4sc9_0146 with dissolve
    plt "I'm 23... never had a boyfriend... never known a man's touch... nor a man's love."
    plt "*Whimpers* {size=-10}{b}Nnnhh! I need to cool off!{/b}{/size}"
    plt "Maybe a swim?"
    scene ch4sc9_0148 with Dissolve(2)
    $ renpy.pause ()
    plt "This should do the trick!"
    scene ch4sc9_0149 with dissolve
    $ renpy.pause ()
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc9_0150 with Dissolve(2)
    play music dark_1 fadein 1.0
    lll "*Grunts* Hhhrrrhh... That’s right Pearl! Show me your naked body!"
    lll "*Grunts* hhhrrhh... You love teasing me, don’t you? You’re a dirty little tease!"
    lll "*Grunts* HHRrhhhr… I know you want me, you whore! Just look at how you..."
    scene ch4sc9_0151 with dissolve
    lll "Walk around in your skimpy outfits."
    lll "Flirting with men to get what you want."
    scene ch4sc9_0152 with dissolve
    lll "*Grunts* Hhhrhh… Don’t worry, you little skank! I'll give you exactly what you need."
    scene ch4sc9_0151 with dissolve
    lll "*Grunts louder* HHRrhhhr... You and that big-titted cow, Kelly, will be my own personal whores!"
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause (1)
    jump ch4sc10

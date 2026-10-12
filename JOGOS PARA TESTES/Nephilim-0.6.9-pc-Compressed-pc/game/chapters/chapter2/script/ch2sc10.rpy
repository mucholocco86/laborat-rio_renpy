#Start Chaper
label ch2sc10:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music outdoors_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc10_01 with Dissolve(2.0)
        $ renpy.pause()
        window show dissolve
        scene ch2sc10_01 with dissolve
        mct "I should see if old man Gibbs is home while there’s still some daylight left."
        scene ch2sc10_02 with dissolve
        mct "I wonder what he has been up to all these years?"
        mct "Probably still  making tools for the village, and getting drunk at the tavern."
        scene ch2sc10_03 with dissolve
        mct "Come to think of it, though, we didn’t run into him at the tavern last night."
        mct "He and father often had a couple of ales there after they were done with work for the day."
        scene ch2sc10_04 with dissolve
        fy "Hey Sabby!"
        scene ch2sc10_05 with dissolve
        sa "Urrh, Flynn. I’ve told you a million times not to call me that."
        scene ch2sc10_06 with dissolve
        fy "Isn’t that... ?"
        scene ch2sc10_07 with dissolve
        sa "It could be... Alice mentioned he was back."
        scene ch2sc10_08 with dissolve
        with vpunch
        fy "{b}HEY! [mc]!{/b}"
        scene ch2sc10_09 with dissolve
        $ renpy.pause()
        scene ch2sc10_10 with dissolve
        fy "Well, well, well. If it isn’t our favorite cousin!"
        scene ch2sc10_11 with dissolve
        sa "Don’t mind Flynn. His manners are terrible as always. Hi [mc]."
        scene ch2sc10_16 with dissolve
        mc "I’m your only cousin, Flynn..."
        mc "Hi Sabrina."
        scene ch2sc10_13 with dissolve
        sa "It’s good to see you!"
        sa "You're looking... good, real good."
        scene ch2sc10_16 with dissolve
        mc "You don’t seem all that surprised to see me."
        scene ch2sc10_14 with dissolve
        fy "Alice already told us you were back when we ran into her earlier."
        fy "She had a very... angry expression."
        scene ch2sc10_15 with dissolve
        fy "I didn't dare ask what was upsetting her."
        fy "As I’m sure you remember, her gut-punch is quite something."
        scene ch2sc10_16 with dissolve
        mc "I already smoothed things over with her."
        mc "She was upset when she first saw me after thinking I had been dead for ten years."
        scene ch2sc10_17 with dissolve
        sa "Yeah, I can imagine. You’re okay, though? We haven’t heard from you in all these years."
        sa "I'm honestly feeling like giving you a good slap as well!"
        scene ch2sc10_18 with dissolve
        fy "What’s up with that, hmm?"
        fy "Your parents die and you just vanish off the face of the earth?"
        scene ch2sc10_19 with dissolve
        with vpunch
        sa "{b}Flynn!{/b}"
        sa "Shut your piehole! You're so insensitive!"
        scene ch2sc10_20 with dissolve
        mc "It’s alright, Sabrina. It wasn’t safe for me to be here."
        mc "It still isn’t. I’m just passing through the area on my way to Luxenford."
        scene ch2sc10_18 with dissolve
        fy "You’re headed to the capital?"
        fy "What for?"
        scene ch2sc10_20 with dissolve
        mc "Yes, it holds answers that I need."
        scene ch2sc10_17 with dissolve
        sa "We’re actually headed there ourselves in about two weeks."
        scene ch2sc10_22 with dissolve
        sa "Why don’t you stay with us until then?"
        sa "We could travel to Luxenford together!"
        sa "I’m positive Mom and Dad would love to have you over, You’re their nephew too, after all."
        scene ch2sc10_23 with dissolve
        mc "I’m leaving tomorrow at first light, with Eliza. I’ve waited ten years..."
        scene ch2sc10_24 with dissolve
        mc "And I’m done waiting."
        scene ch2sc10_25 with dissolve
        fy "Eliza huh? Is she hot?"
        scene ch2sc10_26 with dissolve
        mc "*Exhales* ..."
        scene ch2sc10_27 with dissolve
        sa "Flynn! How about you keep it in your pants for once?"
        scene ch2sc10_28 with dissolve
        fy "What? I was just curious..."
        scene ch2sc10_29 with dissolve
        sa "You’re hopeless."
        scene ch2sc10_30 with dissolve
        fy "Hopeless romantic!"
        scene ch2sc10_29 with dissolve
        sa "No. Just hopeless!"
        scene ch2sc10_28 with dissolve
        fy "[mc] traveling alone with a young maiden. You can’t blame me for assuming..."
        fy "They're probably dating! I think that's safe to assume?"
        scene ch2sc10_31 with dissolve
        mc "She’s..."
        #CHOICE
        menu:
            "Someone I care about.":
                $ eliza_trust += 1
                scene ch2sc10_32 with dissolve
                fy "Okay, okay. I won’t make any inappropriate jokes."
                scene ch2sc10_26 with dissolve
                mc "..."
                scene ch2sc10_25 with dissolve
                fy "So, when can we meet this lovely maiden you've found?"
                scene ch2sc10_33 with dissolve
                mc "How about... never?"
                scene ch2sc10_34 with dissolve
                fy "Oh, come on! If you care about her, she is obviously something special..."
                scene ch2sc10_35 with dissolve
                fy "I have a duty to make sure my dear cousin doesn’t get played for a fool by some lady and her feminine charms."
                fy "Or get lured into devil worship by a succubus!"
                scene ch2sc10_29 with dissolve
                sa "Oh lord, Flynn! As if you'd know anything about ladies or their charms."
                scene ch2sc10_36 with dissolve
                mc "Yeah... I’m with Sabrina on this one."
                scene ch2sc10_37 with dissolve
                fy "You two are really teaming up on me, huh?"
                scene ch2sc10_29 with dissolve
                sa "Just like when we were little!"
                scene ch2sc10_26 with dissolve
                mc "..."
                scene ch2sc10_33 with dissolve
                mc "We’ll be at the tavern later if you want to say hello."
                scene ch2sc10_30 with dissolve
                fy "Yes! We’ll be there! Right Sabby?"
                scene ch2sc10_42 with dissolve
                sa "Ugh! Don’t call me that."
                scene ch2sc10_43 with dissolve
                sa "Yes, we’ll be there."
                scene ch2sc10_38 with dissolve
                mc "Word of caution, Flynn. If you insult her..."
                scene ch2sc10_44 with dissolve
                fy "Yeah, yeah. You’ll feed me to the pigs."
                scene ch2sc10_36 with dissolve
                mc "No. Eliza will whoop your ass herself. She’s tougher than she looks."
                scene ch2sc10_45 with dissolve
                fy "As if a girl could scare me!"
                scene ch2sc10_39 with dissolve
                $ renpy.pause(1)
                "You share a look with Sabrina, the two of you chuckling at Flynn."
                scene ch2sc10_40 with dissolve
                $ renpy.pause(1)
                sa "*Giggles* ..."
                scene ch2sc10_46 with dissolve
                sa "Well, we've gotta get to Arnstead's farm to buy some flour."
                sa "We promised to help Mom prepare the bread for tomorrow’s market day."
                scene ch2sc10_47 with dissolve
                fy "Do we really have to? I’m sure they can handle it without us."
                scene ch2sc10_48 with dissolve
                with vpunch
                sa "Flynn!"
                scene ch2sc10_49 with dissolve
                fy "Coming! See ya, cus!"
                fy "Oh, you should stop by our house cus! Mom and dad would love to know that you're... well, alive?"
                scene ch2sc10_33 with dissolve
                mc "Sure... I guess I could pay them a visit."

            "Just a friend.":
                scene ch2sc10_32 with dissolve
                fy "Boring."
                scene ch2sc10_26 with dissolve
                mc "..."
                scene ch2sc10_25 with dissolve
                fy "So, when can we meet her?"
                scene ch2sc10_33 with dissolve
                mc "Never?"
                scene ch2sc10_34 with dissolve
                fy "Oh, come on! If you’re just friends, you won’t mind if I meet her."
                scene ch2sc10_35 with dissolve
                fy "I have a duty to make sure my cousin keeps good company."
                scene ch2sc10_29 with dissolve
                sa "Pfft Flynn... you wouldn’t know good company if it landed on your face and her name was Aphrodite."
                scene ch2sc10_36 with dissolve
                mc "Yeah. I’m with Sabrina on this one."
                scene ch2sc10_37 with dissolve
                fy "You two are really teaming up on me, huh?"
                scene ch2sc10_29 with dissolve
                sa "Just like when we were younger!"
                scene ch2sc10_33 with dissolve
                mc "We’ll be at the tavern later if you want to say hello."
                scene ch2sc10_30 with dissolve
                fy "Yes! We’ll be there! Right Sabby?"
                scene ch2sc10_42 with dissolve
                sa "Ugh! Don’t call me that."
                scene ch2sc10_43 with dissolve
                sa "Yes, we’ll be there."
                scene ch2sc10_38 with dissolve
                mc "Word of caution, Flynn. If you get on her bad side..."
                scene ch2sc10_44 with dissolve
                fy "Yeah, yeah, You’ll hang me upside down a tree and let the birds shit on me."
                scene ch2sc10_36 with dissolve
                mc "No. Eliza will handle you herself. She enjoys making a fool out of idiots."
                scene ch2sc10_45 with dissolve
                fy "As if a girl could scare me!"
                scene ch2sc10_39 with dissolve
                $ renpy.pause()
                scene ch2sc10_40 with dissolve
                $ renpy.pause()
                scene ch2sc10_46 with dissolve
                sa "Well, we've gotta get to Arnstead's farm to buy some flour. We promised to help Mom and Dad prepare the bread for tomorrow’s market day."
                scene ch2sc10_47 with dissolve
                fy "Do we really have to? I’m sure they can handle it without us."
                scene ch2sc10_48 with dissolve
                with vpunch
                sa "Flynn!"
                scene ch2sc10_49 with dissolve
                fy "Coming! See ya, cus!"
                fy "Oh, you should stop by our house cus! Mom and dad would love to know that you're... well, alive?"
                scene ch2sc10_33 with dissolve
                mc "Sure... I guess I could pay them a visit."

        scene ch2sc10_50 with dissolve
        mct "I was going to pay Gibson a visit, but he should be closing up for the day."
        mct "I guess I might as well pay a visit to uncle Shane and aunt Maya."
        mct "It feels weird calling them aunt and uncle, when I know they aren't really..."
        mct "As for Gibson... I’ll visit you tomorrow before we leave, old bear."
        stop music fadeout 2.0
        scene black with Dissolve(2)
        $ renpy.pause(0.5)
        scene ss88 with Dissolve(1)
        $ renpy.pause()
        scene ch2sc10_51 with Dissolve(2)
        play music forest_1 fadein 1.0
        $ renpy.pause(0.5)
        sh "What's this? I thought you'd be halfway done with making the bread for tomorrow?"
        my "*Scoffs* I would've been if you had bought the flour yesterday as I asked you... instead you went for ales."
        scene ch2sc10_52 with dissolve
        my "So, I'm setting the table while Flynn and Sabrina are heading to Arnstead for some freshly milled flour."
        scene ch2sc10_53 with dissolve
        sh "Ugh... why do you always give me attitude about grabbing a few ales at the tavern?"
        sh "I work hard to put meals on our table at the lumbermill... I need to unwind after a days work."
        scene ch2sc10_52 with dissolve
        my "You're the one nagging me, expecting me to work miracles when you've not held up your end..."
        my "A little attitude is well earned."
        scene ch2sc10_53 with dissolve
        sh "You should work on showing me some respect... I'm the damn best husband a woman like you will find."
        scene ch2sc10_52 with dissolve
        my "Ugh... stop pestering me already and go make yourself useful somewhere... I need to prepare for when they return with the flour."
        scene ch2sc10_53 with dissolve
        sh "Fine... whatever, I'll grab an ale at the tavern."
        scene ch2sc10_54 with dissolve
        my "Of course... another ale..."
        sh "I bust my ass for an ungrateful wife, who refuses to be intimate with me for years... I am owed as many ales as I want."
        my "*Mumbles sarcastically* I wonder why I'm not attracted to you."
        scene ch2sc10_55 with dissolve
        my "*Groans* Ugh! Why do I let him get to me... can't he just be grateful for once?"
        my "No... that would be far too much to ask..."
        scene ch2sc10_56 with dissolve
        my "I need a bath... I won't have time later if I'm to make all the bread before tomorrow's market day."
        my "Mmh, yes... a bath is just what I need, it should be a good hour before the kids return with the flour."
        scene black with Dissolve(2)
        $ renpy.pause(0.5)
        "Half an hour passes..."
        scene ch2sc10_57 with Dissolve(2)
        $ renpy.pause(0.5)
        mct "*Chuckles* Their house looks just like I remember it, they always had this unique wall made of clay."
        mct "Papa and uncle Shane built it together, they always praised each other about it when they were hanging out."
        scene ch2sc10_58 with dissolve
        "*Soft noises* Nh... nhh..."
        scene ch2sc10_60 with dissolve
        my "*Moans softly* Ohh..."
        my "I'm so sensitive after a bath... nngh... oh yes..."
        scene ch2sc10_61 with dissolve
        my "Ohh..."
        scene my_lewd1 with dissolve
        $ renpy.pause()
        my "Years... mmh... years since I've had a man touch me... mmh..."
        my "I can't believe how much I crave a man's affection... aahh..."
        my "I haven't had sex with Shane in almost two decades... he's not a man... mmh..."
        my "I put on a good front for Sabrina and Flynn... mmh... but how much longer do I have to?"
        my "Aahh... they're both adults now... mmh..."
        my "I've caught Shane getting his dick wet at the tavern multiple times..."
        my "It's not fair... as a woman I'm bound to him but he can... enjoy life's pleasures without repercussions..."
        scene ch2sc10_58 with dissolve
        "*Soft noises* Nh... nhh..."
        mct "Hmm? I guess somebody's home... it almost sounds like..."
        scene ch2sc10_59 with dissolve
        mc "Uncle Shane? Aunt Maya? You guys home?"
        scene ch2sc10_61 with dissolve
        my "Ugh! What now Shane?! I told you to leave!"
        scene ch2sc10_62 with dissolve
        with vpunch
        my "*Gasps* B-Burgler! Somebody! {b}HELP!!{/b}"
        with vpunch
        my "{b}GET OUT YOU SCOUNDREL!{/b}"
        scene ch2sc10_63 with dissolve
        mc "Woah! Woah!"
        mc "Aunt Maya, it's me! {b}[mc]!{/b}"
        my "[mc]?! *Gasps* W-Wait! {b}T-Turn around!{/b}"
        scene ch2sc10_64 with dissolve
        mc "Right... my bad."
        my "*Quietly* {size=-10}{b}Heavens! I... I just gave him a full display!{/b}{/size}"
        my "Close the door while I get my towel."
        scene ch2sc10_65 with dissolve
        my "Thank you..."
        mc "Of course... my bad for barging in like this..."
        my "Don't be silly... if anything, this proves it's really you... you've never knocked once when you've come to visit."
        mc "*Chuckles* I suppose I never did... although I never ran into you like... this."
        mc "This was... quite the greeting..."
        my "*Quietly* {size=-10}{b}I hope you enjoyed it...{/b}{/size}"
        scene ch2sc10_66 with dissolve
        my "Come here you! I need my hug!"
        mc "What are you... aren't you still naked?"
        scene ch2sc10_67 with dissolve
        my "Who cares! You're alive! *Giggling happily*"
        my "I knew you would be... deep down, I knew it."
        my "I knew when they found your mother and father... with no reports of your body... I knew you would be out there."
        scene ch2sc10_68 with dissolve
        my "Goodness honey! You're taller than me now! How you've grown..."
        my "You're a man now... mmh... who would've thought..."
        my "Turn around sweetie, let me have a proper look at you."
        scene ch2sc10_69 with dissolve
        my "Mmh... yes... you certainly have grown into quite the man."
        mc "*Chuckles* What makes you say that?"
        scene ch2sc10_70 with dissolve
        my "Oh I don't know... maybe it's the fact you have a naked women in front of you and your instinct was to grab her by her hips..."
        mc "I'm just happy to see you, Maya."
        my "*Giggles* Yes... I can certainly tell, the feeling is mutual... otherwise I'd have removed your hand already."
        scene ch2sc10_69 with dissolve
        my "It seems this isn't your first time having a naked woman in your arms?"
        my "Shame... *Quietly* {size=-10}{b}I always imagined I'd be the first...{/b}{/size}"
        mc "Hmm?"
        scene ch2sc10_70 with dissolve
        my "*Giggles* Nothing honey... come, sit with me."
        scene ch2sc10_71 with dissolve
        my "Hnngh... I'll just... mmh... grab the towel before we go, you don't mind, do you honey?"
        mc "That's probably a good idea."
        mct "Is she intentionally pressing herself against me? Nah... it's just a coincidence."
        scene ch2sc10_72 with dissolve
        my "There we go... thank you for not making a big deal out of seeing your aunt naked sweetie."
        my "Most young men would've made a fuss about it... but not you, you're... mature."
        mct "Technically she isn't even my aunt, her husband Shane is the brother of my human 'dad'"
        mct "And I'm not even related to him... the only human I have a bloodtie with was my mother... obviously Maya doesn't know this."
        scene ch2sc10_73 with dissolve
        mct "This is neither the time or place to dive into that topic with her... for now I'm just happy to see she's doing well."
        mct "She has the same warmth as I remember... always welcomed me with a hug and open arms each time I visited."
        mct "She never made any issue of having to cook extra dinner because I played too long with Flynn and Sabrina, she's always treated me as her own."
        my "*Giggles* Sweetie? Aren't you joining me? It's rude to keep a halfnaked woman waiting you know?"
        mc "*Chuckles* Right, I'm right behind you."
        scene ch2sc10_74 with dissolve
        my "*Snickers* Phrasing honey! That's a bold thing to tell a woman who's naked."
        mc "I said nothing that wasn't truthful."
        my "*Scoffs lightly* Sit... you little rascal."
        scene ch2sc10_75 with dissolve
        mc "You look good... better than I remember."
        my "*Snickers* I'm a decade older than you remember... but then again, back then you wouldn't have appreciated my looks."
        my "I'll take the compliment, thank you."
        scene ch2sc10_76 with dissolve
        my "It's lovely to be complimented by a man..."
        my "Especially after all these years."
        scene ch2sc10_77 with dissolve
        mc "What are you talking about? A woman like you isn't being showered in compliments by your husband daily?"
        "Maya shakes her head"
        scene ch2sc10_76 with dissolve
        my "You've given me more compliments in the short time you've been back than Shane has in the last decade..."
        scene ch2sc10_78 with dissolve
        my "Our marriage has never been one of love, it was arranged by our parents, his lineage as a lumberjack and mine as a farmer..."
        my "They thought it would be a prosperous marriage, and on paper... it is."
        scene ch2sc10_79 with dissolve
        my "But a marriage void of love..."
        my "Only held together by duty and parenthood, it will show it's cracks over time, especially when the children grow up."
        scene ch2sc10_77 with dissolve
        mc "I didn't know..."
        scene ch2sc10_76 with dissolve
        my "How could you? You were only ten summers when you disappeared sweetie..."
        my "Far too young to understand the complications of a mature relationship."
        scene ch2sc10_77 with dissolve
        mc "I suppose... still, I can't help but feel you should be treated better, I don't much like the idea of you being neglected."
        scene ch2sc10_80 with dissolve
        my "My sweet boy... you're as kind and thoughtful as you were back then..."
        my "I'm glad to see that hasn't changed."
        scene ch2sc10_81 with dissolve
        my "Enough about my sad marriage, tell me everything about you... what happened? Where... did you go?"
        my "When I heard how they found your parents... I dreaded what would've happened to you..."
        scene ch2sc10_82 with dissolve
        my "I found hope in the fact you weren't there... I knew it meant you might've escaped their fate, but how?"
        my "How could you make it on your own at the age of ten?"
        scene ch2sc10_83 with dissolve
        "Maya inches herself closer to you, caressing your cheek with her delicate fingers and soft, warm palm."
        mc "*Exhales* It's quite a long story... I found them that night you know?"
        scene ch2sc10_84 with dissolve
        my "*Gasps* Oh no... oh sweetie... I prayed that you wouldn't have seen them like that."
        my "I'm so sorry... that is not something you should've seen at that age. It was difficult even for the adults to handle."
        scene ch2sc10_83 with dissolve
        mc "Mmh... it's okay... I'm-... okay."
        scene ch2sc10_84 with dissolve
        my "You don't have to act strong with me... I'm here for you honey, I always will be."
        "You nod"
        scene ch2sc10_83 with dissolve
        mc "I know Maya. I know..."
        mc "A man found me shortly after I found out what happened to mama and papa, he took me away and protected me from our pursuers."
        mc "He taught me how to survive, but we couldn't risk going back here, it would've lead them to you."
        scene ch2sc10_84 with dissolve
        my "That sounds... awful, you're here now... does that mean you're safe?"
        my "Please make it so."
        scene ch2sc10_83 with dissolve
        mc "Somewhat, I lost their trail, I'm on my way to Luxenford, but I couldn't pass through Riverside without knowing you were okay."
        scene ch2sc10_84 with dissolve
        my "Oh [mc]... it means the world to me to know you're alright... that you came to see me... thank you honey."
        my "Thank you for putting my greatest worry to bed... the amount of nightmares and sleepless night's I've had not knowing your fate..."
        scene ch2sc10_83 with dissolve
        mc "I apologize for making you worry... this was the earliest I could come visit."
        scene ch2sc10_84 with dissolve
        my "It matters not... what matters is that you did, I'm so relieved to see you alive... to see what a man you've grown to be."
        scene ch2sc10_85 with dissolve
        my "Mmh... so muscular... you're strong..."
        "You feel her hand run down and across your chest, clearly intrigued by your muscular physique."
        my "Oh my... what am I saying? Oh my towel!"
        scene ch2sc10_84 with dissolve
        my "*Giggles* Your aunt is feeling lightheaded by this pleasant surprise, forgive me."
        scene ch2sc10_83 with dissolve
        mc "*Chuckles* There's nothing to forgive, I imagine it must be quite the reveal."
        scene ch2sc10_84 with dissolve
        my "It certainly was... but I wouldn't have it any other way."
        scene ch2sc10_86 with dissolve
        my "Stay here honey... I'll be right back, I better get dressed before Flynn and Sabrina return with the flour I sent them to get."
        mc "Sure... I guess it would be a little awkward to explain why you're only wearing a towel."
        my "It definitely would be... I'll be right back, and don't stare at my ass like that! *Snickers*"
        mc "You've got the wrong idea aunt Maya, I'm just admiring the scenery..."
        scene ch2sc10_87 with dissolve
        my "Uh-huh... the scenery... of my house?"
        mc "Mmh... it's a... beautiful house, aunt Maya."
        my "*Giggling* Stop it... you're going to make me blush honey!"
        scene black with Dissolve(1.5)
        "Within a couple of minutes Maya returns to you, wearing more apropriate attire."
        scene ch2sc10_88 with Dissolve(1.5)
        my "What do you think? Can I pull off this dress?"
        mc "*Chuckles* Asking me questions you already know the answer to? Yes... you look beautiful."
        scene ch2sc10_89 with dissolve
        my "*Giggles* You can't blame a woman for wanting a compliment."
        mc "I certainly can't."
        my "Now come here... let your aunt give you a hug!"
        scene ch2sc10_90 with dissolve
        mc "Mmmfhh... Mfffh... Maya..."
        my "Shush you... let your aunt give you a little bit of affection..."
        mct "Mmffh... so soft... her scent... just as natural as always, slight hint of hazelnut and tea-leaves..."
        scene ch2sc10_91 with dissolve
        my "Goodness... I find out you're alive and here I am... almost suffocating you! *Giggling*"
        scene my_lewd2 with dissolve
        mc "Mmffh... it's okay... I'll die happy."
        my "*Giggles* Such a charmer you've grown up to be... mmhh... I always knew you would become a ladies man."
        my "You've always had that look in your eyes, a look that could get a woman to do anything for you."
        mc "Mmffhh... is that so? Mmhh..."
        my "Oh believe me... no woman in her right mind would deny such a lovely man... you can have anything you want sweetie..."
        my "Mmhh... anything in the whole world."
        my "I'm so happy that you're alive honey... so... incredibly... happy- Mmhh..."
        my "You'll be a good boy and stay for dinner, won't you sweetie?"
        mc "MffhhH... Mmh... I really can't- Mmffh..."
        my "You'd really deny your aunt this request? Knowing how happy it would make her?"
        mct "Damnit... she had to play that card..."
        mc "Mmm... alright... mmhh, I can't refuse you aunt Maya... mmhh..."
        my "That's my good boy! Mmhh... such a good boy..."
        my "Come sweetie... you can help me prepare in the kitchen."
        my "I've already set the table, Shane won't be home tonight, he's drinking at the tavern."
        my "You'll take his place at the table... mmhh... *Quietly* {size=-10}{b}Where you belong.{/b}{/size}"
        scene ch2sc10_92 with dissolve
        "Maya takes your arm and leads you over to the kitchen, keeping your arm squished between her large, soft breasts."
        my "Okay sweetie, I'd like you to chop vegetables for me, while I handle your meat- the meat!"
        mc "Sure, shouldn't be a problem."
        scene ch2sc10_93 with dissolve
        my "I knew you would be up for the task, only a real man isn't afraid of working a kitchen with his woman."
        mc "Being on my own, I've had to do my share of cooking if I wanted to survive."
        scene ch2sc10_94 with dissolve
        my "I can imagine... tonight won't be for survival though, it'll be your welcome home meal."
        my "Perfect! I left the beef to simmer on low heat for a couple of hours, my mouth is already watering..."
        scene ch2sc10_95 with dissolve
        mc "I can't wait to taste it, as I remember your cooking is outstanding."
        my "You're too kind honey... you were just a little glutton last time I cooked for you."
        scene ch2sc10_96 with dissolve
        mc "*Chuckles* I still am, ravenous even."
        scene my_lewd3 with dissolve
        my "*Giggles* Ravenous huh? I guess those muscles of yours needs nourishment."
        mc "*Chuckles* ..."
        my "Don't you worry, I'll make sure to always have a meal for you whenever you need it sweetie."
        my "As your aunt, it's my duty to ensure you're taken care of."
        my "Especially with your mother gon-... I'm sorry."
        mc "It's okay... I've had ten years to adjust, you mentioning them is not an issue."
        scene my_lewd4 with dissolve
        my "Okay... I want you to know that you can talk to me about them."
        my "I will never judge your feelings sweetie, or belittle them."
        mc "Thank you Maya, I know."
        my "Do you know why... why they were killed?"
        mc "Mmh, I do."
        mc "A man has been after me ever since that night, he killed them... because of me."
        my "No honey... do not say that, let alone think it... he is clearly a deranged individual with no morals."
        scene my_lewd3 with dissolve
        my "Do not let him make you feel as if this was your fault... you were ten years old."
        my "He is at fault and he alone, he chose to do something unspeakable... he is the one you should direct your blame at."
        mc "Yeah... trust me, I am."
        mc "It's just when something happens because of you, even if you didn't make it happen, it can still make you believe it's your fault."
        my "I can see how such a line of thought could be made... but know that it wasn't your fault."
        scene my_lewd4 with dissolve
        my "Let's change the subject, I don't like thinking about what happened that night..."
        mc "Yeah... I agree."
        my "So..."
        my "Since you've grown up to be quite the looker and charmer... and we've established you can handle yourself around a woman."
        my "Any girlfriend? Or should I say... girlfriendS? *Snickers*"
        mc "*Chuckles* Really? You just had to emphasize the plural?"
        my "Absolutely... I imagine a young stud like you to have at least three girlfriends by now? You're twenty after all."
        mc "Sorry to disappoint, but I'm currently single."
        scene my_lewd3 with dissolve
        my "Single, huh? Hmm... interesting."
        my "Must be by choice? A man like you could easily have his pick of the town and settle down."
        mc "It is by choice yeah, I'm constantly on the move and... I'm not fit to settle down until I've avenged mama and papa."
        my "Avenged... is that why you're heading to Luxenford?"
        mc "Intuitive as always I see, yeah... the man responsible lives in Luxenford."
        my "I want to tell you to think about this and not do something foolish, but I know you well enough to know that would be a waste of words."
        mc "You're right, I wouldn't listen to common sense when it comes to this."
        scene my_lewd4 with dissolve
        my "Just... promise me that you'll come visit? And not after a decade this time."
        mc "Mh, I promise aunt Maya."
        my "Good! It warms my heart to have been granted this promise sweetie."
        my "You always kept your promises, I suspect that hasn't changed."
        mc "I try to at least."
        my "That's enough for me... now I have something to look forward to."
        scene ch2sc10_97 with dissolve
        my "How's the carrots looking? Did you finish yet sweetie?"
        mc "I'll let you be the judge, do you have a particular cutting-size in mind?"
        my "Mhm, I do... for this dish I'm wanting finely cut little pieces of carrots, these large chunks won't do."
        scene ch2sc10_98 with dissolve
        my "Here... I'll guide you."
        "You feel her soft hand run along your arm and onto your hand, guiding the blade as you hold it, while pressing herself into your back."
        scene ch2sc10_99 with dissolve
        my "*Giggling* You're lucky I came over here to check on you honey... otherwise we'd have to hear Flynn complain about carrot chunks."
        mc "*Chuckles* We wouldn't want that."
        my "No, we wouldn't."
        scene my_lewd5 with dissolve
        my "Mmh... that's it sweetie, follow my lead, as your aunt, it's my duty to teach you these things."
        my "These big carrot chunks simply won't do... cutting vegetables is an art, you need precise, clean cuts."
        mc "I see... I never really thought about it."
        my "Don't worry... with me teaching you, you'll be doing it without thinking soon enough."
        my "Flynn is hopeless in a kitchen and Sabrina refuses to learn... she's focused on gaining experience as a seamstress."
        my "I'm glad she has found something to latch onto, I just wish she would see the benefit of being versatile."
        my "She can't rightly expect to find a husband if she can't cook..."
        mc "It's definitely not the norm but I'm sure she'll land herself a decent husband even without cooking."
        my "Mmh... I hope so, I don't want her to end up like me... old and unloved."
        mc "You're neither of those things aunt Maya... you're both loved and you're certainly not old... you're in your prime."
        my "Oh stop it... you really believe so sweetie?"
        "You feel her breasts squishing further into your back, she's enjoying the intimacy of this moment between you."
        mc "Mh-hm, I stand by what I said."
        my "You're doing so well... mmhh... you're a great student honey."
        my "If only I could convince you to stay... we could make this a daily thing... mmh."
        mc "As tempting as you make this, I can't-"
        my "Sshh... I know... I was just thinking wishfully, out loud."
        my "I would love to have a man like you around... doing things with me... *Whispers softly* {size=-10}{b}and to me...{/b}{/size}"
        mc "Aunt Maya-"
        scene ch2sc10_100 with dissolve
        my "Shh..."
        my "I know... I know I'm not really your aunt."
        scene ch2sc10_101 with dissolve
        mc "You... know?"
        scene ch2sc10_100 with dissolve
        my "Mhh... I know that your father wasn't your real father... which means my children aren't your cousins... and I'm not your aunt."
        scene ch2sc10_101 with dissolve
        mc "How? How did you find out?"
        scene ch2sc10_100 with dissolve
        my "Your mother told me, you were nine at the time."
        my "She had been arguing with your dad about how to raise you, they had some minor difference in opinions about the matter."
        scene ch2sc10_102 with dissolve
        my "So she came to me one night, we ended up sharing a bottle of wine and she spilled the beans."
        my "She claimed your father to be an angel, of course I dismissed this as the wine talking."
        scene ch2sc10_103 with dissolve
        my "But then she showed me she was able to do magic... seeing her making the bottle of wine levitate right before my eyes..."
        my "Suddenly her claim became believable..."
        scene ch2sc10_101 with dissolve
        mc "You've never told anyone?"
        scene ch2sc10_103 with dissolve
        my "Of course not..."
        my "I promised your mother to take it to my grave, besides... what good would it do to share this information with others?"
        scene ch2sc10_102 with dissolve
        my "I just wanted you to know that I..."
        scene ch2sc10_103 with dissolve
        my "That I love you very much sweetie, and you'll always be family, even if we aren't by blood."
        my "I'll always be your aunt... no matter what anyone says, okay?"
        ####Choice####
        menu:
            "Agree to Aunt & Nephew roleplay":
                scene ch2sc10_101 with dissolve
                mc "You'll always be my beautiful aunt."
                "Maya loves that you're on the same page as her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene ch2sc10_103 with dissolve
                $ maya_rp = True
                my "Oh honey... my sweet and handsome nephew... you make auntie really happy."
                my "We'll roleplay as aunt and nephew from now on, okay sweetie?"
                $ maya_trust += 2

            "Agree to keep up the charade for Flynn and Sabrina":
                scene ch2sc10_101 with dissolve
                mc "I don't mind that we keep pretending for Flynn and Sabrina's sake."
                scene ch2sc10_103 with dissolve
                my "Thank you sweetie... I don't want to destroy their world."
                my "We'll just keep pretending to be aunt and nephew, at least for the time being, okay?"

        scene ch2sc10_101 with dissolve
        mc "Mhh, okay. I'd like that."
        scene ch2sc10_104 with dissolve
        my "My sweet boy... Mwaah!"
        mc "*Chuckles* H-Hey! Stop it... you're embarrasing me."
        my "*Giggling* What? You're embarresed being given affection by your beautiful aunt?"
        my "Show me how much you love me with a kiss! *Giggling*"
        scene ch2sc10_105 with dissolve
        fy "I'm baaack! Is dinner ready yet? I'm famished!"
        "Maya quickly adjusts herself, as the door open and Flynn announces himself."
        mc "*Chuckles* Hey cus..."
        scene ch2sc10_106 with dissolve
        fy "Oooh! Cus! Did I walk in on something indecent?"
        my "Flynn! What are you saying?!"
        fy "*Chuckles* Are you putting the moves on my mother cus? After just having her to yourself for one hour?"
        scene ch2sc10_107 with dissolve
        my "Flynn! Don't be proposterous, [mc] has been the perfect gentleman, he's helped me prepare dinner."
        my "You're doing the dishes tonight for having such lewd thoughts!"
        fy "But mom! I was jesting... you know my humor!"
        my "I do, which is exactly why you're doing the dishes! It's about time you grow out of such commentary!"
        scene ch2sc10_108 with dissolve
        fy "Mother! You can't be serious..."
        fy "It's not like I made a joke about catching the two of you naked, accidentally falling onto each other and such!"
        my "Oh I'm serious young man!"
        scene ch2sc10_109 with dissolve
        "You feel Maya leaning back into you, and you instictively grab her hips."
        my "In fact you'll be doing the dishes for a week since you felt the need to elaborate on that subject."
        my "Now go sit, dinner is ready... and pay attention to your cousin, you could learn some proper manners from him."
        fy "*Exhales* Yes mother..."
        scene ch2sc10_110 with dissolve
        my "Where's your sister?"
        fy "She went to visit Alice, said she'd be having dinner at her place."
        my "Oh... that's a shame."
        scene ch2sc10_111 with dissolve
        my "I'd have hoped we'd be able to have dinner as a family."
        scene ch2sc10_112 with dissolve
        fy "Wouldn't we need dad here for it to be considered a family dinner?"
        scene ch2sc10_111 with dissolve
        my "Ugh, no... not with [mc] here. We'd be a family, a proper family."
        my "Everything would be perfect."
        scene ch2sc10_112 with dissolve
        fy "Mother please... you almost make it sound like you want [mc] to be your husband."
        scene ch2sc10_113 with dissolve
        my "At least he would be a proper man and look after his family!"
        scene ch2sc10_114 with dissolve
        mc "*Chuckles* You can call me dad from now on."
        scene ch2sc10_115 with dissolve
        fy "That isn't funny! I have a dad!"
        scene ch2sc10_111 with dissolve
        my "I don't know darling... it's a little funny. *Giggles*"
        my "Imagine if [mc] was your daddy."
        scene ch2sc10_112 with dissolve
        fy "Okay, okay... you two have had your fun... please change the subject!"
        "Maya giggles, she clearly enjoys turning Flynn's indecency against him."
        scene ch2sc10_113 with dissolve
        my "Alright, I think we've had our fun, now dig in boys, eat your fill."
        scene ch2sc10_111 with dissolve
        my "Especially you sweetie, you've had a long journey I'm sure, don't hold back."
        mc "Thank you aunt Maya, I'll make sure there won't be any leftovers."
        my "That's my boy. *Giggles*"
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "The three of you enjoy dinner until everything has been devoured, and you begin to take your leave."
        scene ch2sc10_116 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mc "Alright, thank you for dinner aunt Maya, it was lovely."
        mc "I guess I'll see you at the tavern later Flynn, once you've cleaned all the dishes and kitchen."
        scene ch2sc10_117 with dissolve
        my "Wait up sweetie!"
        mc "Aunt Maya? Did I forget something?"
        my "Yes silly! You forgot the most important part..."
        scene ch2sc10_118 with dissolve
        my "A proper goodbye hug! Mmh."
        my "You've become so tall... so handsome..."
        my "You didn't think you'd escape without embracing me properly, did you?"
        scene ch2sc10_119 with dissolve
        mc "How could I forget... Flynn's mannerism must've rubbed off on me during dinner."
        scene ch2sc10_120 with dissolve
        my "Gods let it not be so... I much prefer your mannerism sweetie."
        my "Especially your hand placement... you know how to hold a woman in your embrace."
        scene ch2sc10_119 with dissolve
        mc "Holding a woman isn't complicated, you just need to follow your instincts."
        scene ch2sc10_120 with dissolve
        my "*Snickers* So it's your instinct to grab my ass?"
        my "I like the sound of that..."
        scene ch2sc10_121 with dissolve
        my "Remember what you promised me, okay sweetie?"
        my "That you'll come visit me... that you won't let me feel lonely for much longer."
        scene ch2sc10_119 with dissolve
        mc "I have no intentions of letting my aunt feel like this..."
        scene ch2sc10_121 with dissolve
        my "Even though I'm not your real aunt?"
        mc "Even so... as you said, we're family."
        my "And family takes care of each other, no matter what."
        scene ch2sc10_119 with dissolve
        mc "Exactly."
        scene ch2sc10_120 with dissolve
        my "My sweet [mc], you remind me of her... your mother, she has instilled some great values in you."
        scene ch2sc10_122 with dissolve
        my "Come here sweetie..."
        my "As your aunt, it's my duty to ensure you're leaving with something to remember me by."
        my "*Soft whisper* Allow me to give you something sweet to look forward to upon returning to me."
        scene ch2sc10_123 with dissolve
        "You feel the soft sensation of Maya's warm, delicate lips make contact with your cheek."
        "She purposefully lands her kiss halfway onto your lips, lingering for quite a while."
        "Her scent of Hazelnut cream and Tea-leaves is overpowering as you feel her large breasts squished against your chest."
        my "Be safe out there sweetie... I'll have another embrace awaiting you when you return to me."
        scene ch2sc10_122 with dissolve
        mc "You know how to keep a man on his toes... Shane is a lucky guy."
        my "No... he isn't... he could have been if he had manned up instead of spending a decade at the bottom of a bottle."
        my "He has lost his chance, for good."
        scene ch2sc10_120 with dissolve
        my "But his loss... might be your gain, take care honey."
        scene ch2sc10_119 with dissolve
        mc "You too, Aunt Maya, I'll return some day."
        scene ch2sc10_120 with dissolve
        my "I know you will, just like I knew you were alive... I feel it in my heart."
        my "Goodbye sweetie."
        scene ch2sc10_119 with dissolve
        mc "Goodbye Maya."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        jump ch2sc11

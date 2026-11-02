label ch7sc5:

    window hide dissolve
    scene ss31 with Dissolve(1.5)
    $ renpy.pause()
    scene ch7sc03_057 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.8)
    el "*Giggling happily* I’m going to miss you too Sundancer!"
    el "You were a mighty steed! Thanks for being my first!"
    mon "*Giggles* He’s really taken to you, Eliza. When horses bond with a person it’s for life."
    scene ch7sc03_058 with dissolve
    mon "Thank you for taking such great care of Sundancer, he seems to be in good health."
    el "How could we not? *Giggles* He’s such a cutiepie!"
    scene ch7sc03_060 with dissolve
    mc "You’re welcome Monica, he was just like you described, gentle which allowed Eliza ample opportunity to learn how to ride."
    scene ch7sc03_059 with dissolve
    mon "He’s the perfect beginner horse! He doesn’t go as fast as some of the others but I enjoy that about him."
    scene ch7sc03_057 with dissolve
    mon "Eliza, since the two of you are such great friends, do you want to be the one who feeds him and puts him in his stall?"
    el "Can I? I’d love that! *Giggles* Sundancer! C’mon you rascal!"
    scene ch7sc04_001 with dissolve
    mon "*Giggling* It’s so nice to see how they’ve bonded already."
    mon "A horse can easily judge a person’s character, she must have a pure heart."
    scene ch7sc04_002 with dissolve
    mc "She has the purest heart of anyone I know."
    mc "I was wondering, how did you end up as a stablemaiden?"
    scene ch7sc04_003 with dissolve
    mon "My parents had horses on the farm I grew up at."
    mon "I came to Luxenford to study at the academy, but when I saw the position for a stablemaiden had opened up-"
    scene ch7sc04_004 with dissolve
    mon "-I felt it calling to me, I suddenly missed everything I had been raised with, the connection I had with the horses back home."
    mon "I instantly knew I had to jump on the opportunity."
    scene ch7sc04_003 with dissolve
    mon "And with my experience handling horses, the stablekeeper was happy to give me the position."
    scene ch7sc04_002 with dissolve
    mc "You definitely seem to be in your element here at the stables, I’m sure you made the right call."
    scene ch7sc04_003 with dissolve
    mon "Thank you, [mc]."
    scene ch7sc04_004 with dissolve
    mon "I was honestly a little nervous initially, as the academy would have put me into some more ‘esteemed’ career paths."
    mon "But at the end of the day, finding joy in what I do every day meant more to me than some perceived social standing."
    scene ch7sc04_005 with dissolve
    mon "Enough about me, how did your journey to Loboten go?"
    mon "I assume it went well? Given that you’ve both returned in good health."
    scene ch7sc04_002 with dissolve
    mc "Yeah, it went about as well as one could expect."
    mc "Although we did run into trouble, turns out Loboten was being targeted by outlaws, a group of bandits."
    scene ch7sc04_006 with dissolve
    mon "Ugh! I hate filth like that…"
    mon "It’s rarely enough for them to just rob people… no, they enjoy tormenting and hurting others… I hope you put an end to them."
    scene ch7sc04_007 with dissolve
    mc "We killed every last one of them."
    scene ch7sc04_005 with dissolve
    mon "Good, Loboten is a little too close to Luxenford for bandits to be getting comfortable."
    mon "I’ve never ran into any personally, but I’ve heard plenty of travelers tell… stories."
    scene ch7sc04_004 with dissolve
    mon "So I’ll definitely be happy to avoid any run-ins with such people…"
    scene ch7sc04_002 with dissolve
    mc "I think you’re safe, I doubt they would ever come this close to the city, the city-guards would crush them swiftly if they did."
    scene ch7sc04_003 with dissolve
    mon "*Giggles* If they don’t, I now know who to rely upon for vermin extermination."
    scene ch7sc04_002 with dissolve
    mc "*Chuckles* Vermin exterminator? That’s certainly a title…"
    scene ch7sc04_003 with dissolve
    mon "I guess I could also refer to you as, Hero of Loboten? *Giggles*"
    scene ch7sc04_002 with dissolve
    mc "I’ll take both."
    scene ch7sc04_004 with dissolve
    mon "My, my! Such a greedy man! *Snickers*"
    scene ch7sc04_008 with dissolve
    el "Sundancer is fed and resting in his stall!"
    el "Thank you for letting me do this Monica! He’s so cute!"
    scene ch7sc04_009 with dissolve
    mon "You’re welcome! I’m just happy to see someone enjoying horses as much as I do."
    el "You bet! Spending time with Sundancer has convinced me that we need a stable with horses at our homestead!"
    mon "That is a great idea! If you’re interested, I can probably get you a discount on Sundancer if you decide you want to go through with it."
    el "Great! Although it’s a ways off… we’re starting construction of our house in the coming days."
    scene ch7sc04_010 with dissolve
    el "Ready to head back? You have that sparring with Diana?"
    el "She didn’t strike me as the type of woman who likes to be kept waiting."
    scene ch7sc04_011 with dissolve
    mc "Right, let’s head out then."
    mc "It was nice chatting with you Monica, take care. I’m sure we’ll see you again."
    scene ch7sc04_012 with dissolve
    mon "*Giggles* I hope so! It was lovely to see the two of you again!"
    mon "Be safe and don’t be strangers!"
    scene black with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "You and Eliza head back to Luxenford."

    if irene_alive == True:
        scene ss29 with Dissolve(1.5)
        $ renpy.pause()
        scene ss89 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ir34 with Dissolve(1.5)
        play music summon_3 fadein 1.0
        $ renpy.pause()
        scene ir127 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ir "*Panting heavily* Hnngh… hnhh…"
        ir "How much more… how much must I endure? How long must I wait? Hnnghh…"
        scene ir128 with dissolve
        vi "Well, well, well…"
        vi "Last one standing amongst four Shadow-brothers in a free-for-all?"
        ir "*Panting* Viperia… I’m ready."
        scene ir129 with dissolve
        vi "Ready you say?"
        ir "Yes! I’m ready to take down Rin… you’ve had me training day and night for months."
        vi "You’ve certainly improved…"
        scene ir130 with dissolve
        vi "The only thing you’re ready for is… a bath."
        vi "Look at yourself… all exhausted and covered in blood from a lightweight free-for-all?"
        scene ir131 with dissolve
        ir "Tsk! I’m ready and you know it! Just let me go avenge Alana already!"
        vi "We’ve talked about this sweetie… you’re still too emotional, which will only get you killed."
        vi "We will send you after Rin, once we have determined you have acquired the skills AND determination to do so."
        scene ir132 with dissolve
        ir "Ugh! You have no idea what you’re talking about… whatever…"
        ir "Weren’t you going to draw me a bath?"
        vi "*Scoffs* So bossy… very well, I’ll draw you a bath."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        scene ir133 with Dissolve(1.5)
        play music feels_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause()
        vi "Make sure you get all the blood off… we have a guild dinner tonight to attend."
        ir "I don’t care about guild dinners… I don’t need any of that, not until Alana has been avenged."
        scene ir134 with dissolve
        vi "You will be there… and you will be spotless."
        vi "You were my initiate, that means you are a reflection of me… make sure you’re cleaned and ready in an hour."
        ir "*Groans* Just leave already!"
        scene ir135 with dissolve
        irt "Alana…"
        irt "I will avenge you… I swear it by all the gods."
        scene ir136 with dissolve
        irt "Viperia wants me to go to stupid dinners when… when Rin is still out there… alive and breathing!?"
        irt "While Alana is six feet deep and never will see the light of day again!? Urgh!"
        scene ir137 with dissolve
        irt "*Sighs* They don’t realise how ready I am… every moment I waste here is a moment Alana suffers in the afterlife."
        scene ir138 with dissolve
        $ renpy.pause()
        "Irene begins to rub her breast, trying to get the dried blood off…"
        irt "Every moment Alana isn’t avenged, she will wander the afterlife in despair…"
        irt "She won’t be able to rest in peace knowing the reason her best friend killed her was because of… Rin."
        irt "If I had managed to take down Rin prior to my initiation… Alana would still be alive…"
        irt "But now she’s dead… I… I killed her…"
        irt "No… not me… Rin… Rin killed her…"
        irt "Viperia… she keeps holding me back… she keeps telling me to not get emotionally invested…"
        irt "Yet, she’s the one acting like she’s afraid to lose me? *Scoffs*"
        irt "Viperia has been a solid mentor… I even care about her a tiny smidge… but if she stands in my way…"
        irt "If she tries to stop my vengeance… I’ll kill her."
        irt "Alana died by my hands… the least I can do is to ensure she finds peace."
        scene ir139 with dissolve
        irt "*Sighs* Looks like I managed to wash all the blood off…"
        irt "I don’t even feel the slightest tingle when rubbing my breast any longer…"
        irt "I’ve become numb to everything since she passed… since I killed her."
        scene ir86 with dissolve
        irt "I better get dressed… I don’t much feel like hearing Viperia nag me all evening for being late…"
        irt "Once I avenge Alana… her spirit will live on in me…"
        scene ir140 with dissolve
        $ renpy.pause()
        irt "She’ll get to be a Shadow-sister, through me."
        irt "We’ll travel the world together… assassinate rich, filthy, noble pricks… live lavishly."
        irt "*Sighs* But first… dinner and more training…"
        scene black with Dissolve(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)


    else:
        pass


    scene ss65 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_013 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    $ renpy.pause(0.5)
    mct "Looks like I made it here before Diana."
    mct "Guess I could warm up a bit on the target dummies."
    scene ch7sc04_014 with dissolve
    $ renpy.pause()
    mc "Hmmh?"
    scene ch7sc04_015 with dissolve
    play music battle_3 fadein 1.0
    mc "Di-"
    scene ch7sc04_016 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    mct "As expected… she’s not pulling any punches, a kick with this amount of force would’ve taken the head clean off an average human."
    scene ch7sc04_017 with dissolve
    mc "Sneaky, is that how you want to greet me? *Chuckles*"
    scene ch7sc04_018 with dissolve
    di "If you want a more pleasant greeting, you’ll have to earn it."
    di "I’m impressed you could sense me, when I mask my presence with icefoil I’m near untraceable."
    scene ch7sc04_017 with dissolve
    mc "Your scent gave you away."
    scene ch7sc04_019 with dissolve
    di "My… scent?"
    scene ch7sc04_020 with dissolve
    mc "Mhh. Vanilla-extract and Oceanic-rose powder."
    di "..."
    dit "He… he familiarised himself with my… scent?"
    scene ch7sc04_019 with dissolve
    di "If  you think you being sweet is going to make me go easy on you…"
    scene ch7sc04_017 with dissolve
    mc "*Chuckles* I wouldn’t dare think such a thing."
    scene ch7sc04_016 with dissolve
    di "Good, let us talk with our bodies. No magic, just hand to hand."
    scene ch7sc04_017 with dissolve
    mc "Bring it, Lord Admiral."
    scene ch7sc04_021 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    scene ch7sc04_022 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    scene ch7sc04_023 with dissolve
    $ renpy.pause(0.3)
    mct "I’d almost forgotten how agile she is… she’d give Eliza a run for her money."
    scene ch7sc04_024 with dissolve
    di "*Giggles* …"
    scene ch7sc04_025 with dissolve
    with vpunch
    mc "*Groans* Urh!"
    scene ch7sc04_026 with dissolve
    mct "If I’m not careful she’s going to knock me out, her being so nimble and quick makes me forget just how much power she has."
    scene ch7sc04_027 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    scene ch7sc04_028 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "You manage to block a rib-shattering kick in the last second."
    dit "He's blocking well..."
    dit "But there's something I've wanted to try... since our first clash."
    scene ch7sc04_029 with dissolve
    with vpunch
    di "*Giggles* Hey…"
    di "You look handsome today-"
    scene ch7sc04_030 with dissolve
    with vpunch
    mc "What the-"
    "Diana locks her legs firmly around you as she swiftly pulls back with all her might, sending you flying forwards."
    scene ch7sc04_031 with dissolve
    $ renpy.pause(1)
    scene ch7sc04_032 with dissolve
    $ renpy.pause(1)
    dit "Impressive, he managed to stick the landing after being sent with full force."
    scene ch7sc04_033 with dissolve
    $ renpy.pause(0.5)
    mct "Here she comes!"
    scene ch7sc04_034 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    di "*Gasps* Aah!"
    scene ch7sc04_035 with dissolve
    di "Seems like your grappling skills have been honed well."
    dit "The way he’s grabbing me… he’s man-handling me so easily… *Giggling*"
    scene ch7sc04_036 with dissolve
    with vpunch
    di "*Squeals* Aiih!"
    scene ch7sc04_038 with dissolve
    mc "Did you just squeal?"
    scene ch7sc04_036 with dissolve
    di "Nngh-no! You’re just heavy!"
    scene ch7sc04_038 with dissolve
    mc "*Chuckles* You definitely squealed."
    scene ch7sc04_036 with dissolve
    di "I was surprised."
    scene ch7sc04_039 with dissolve
    di "You’ve gotten stronger… by quite a bit."
    scene ch7sc04_040 with dissolve
    mc "Is that why you’ve been giggling as we traded blows?"
    scene ch7sc04_039 with dissolve
    di "I’ve never met someone who could keep up with me, blow to blow."
    di "It’s invigorating being able to go all out and not worry about killing my sparring partner-"
    scene ch7sc04_041 with dissolve
    with vpunch
    di "*Squeals* Aiih-ah!"
    mc "You’re right, it’s refreshing being able to let loose, now speak with your body, Lord Admiral."
    scene ch7sc04_042 with dissolve
    with vpunch
    di "*Snickers* Let’s speak!"
    scene ch7sc04_043 with dissolve
    $ renpy.pause(0.5)
    scene ch7sc04_044 with dissolve
    $ renpy.pause(0.5)
    scene ch7sc04_045 with dissolve
    with vpunch
    mc "*Groans* Ugh!"
    mc "*Groans* Hngh!"
    scene ch7sc04_046 with dissolve
    mc "Five hells… she took the wind out of me."
    scene ch7sc04_047 with dissolve
    mc "*Chuckles* Still smiling I see… you’re having fun."
    scene ch7sc04_048 with dissolve
    $ renpy.pause(0.5)
    scene ch7sc04_049 with dissolve
    with vpunch
    di "*Whimpers* Nngh!"
    scene ch7sc04_050 with dissolve
    with vpunch
    di "*Gasps* Ah!"
    scene ch7sc04_051 with dissolve
    di "*Panting* You got me- Hnngh… you got me good."
    scene ch7sc04_052 with dissolve
    di "That combo had both power and speed."
    di "Your hand to hand almost rivals my own."
    scene ch7sc04_053 with dissolve
    with vpunch
    di "Let’s continue the conversation! *Snickers*"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ss4 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_054 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    $ renpy.pause(0.5)
    di "*Giggles happily* …"
    scene ch7sc04_055 with dissolve
    mc "*Chuckles* What?"
    scene ch7sc04_054 with dissolve
    di "That’s what I call a workout."
    di "You kept me on my toes."
    scene ch7sc04_055 with dissolve
    mc "I didn’t have much of a choice, every time I let off the offensive, you were pressing the attack."
    mc "You’ve been trained well."
    scene ch7sc04_056 with dissolve
    di "As have you."
    di "As I said earlier, I’ve never been able to spar with anyone without them being hospitalized… this was… refreshing."
    di "At least... not since I stopped sparring with my mentor."
    scene ch7sc04_055 with dissolve
    mc "*Chuckles* I agree, being able to put full force into exercise just makes it feel different."
    di "*Giggles* Yeah… very… different."
    scene ch7sc04_056 with dissolve
    di "So…"
    scene ch7sc04_057 with dissolve
    di "Will you miss me?"
    scene ch7sc04_058 with dissolve
    mc "Hmh?"
    scene ch7sc04_057 with dissolve
    di "You know… when I set sail tomorrow?"
    scene ch7sc04_059 with dissolve
    mc "Miss you? *Chuckles* Not one bit."
    scene ch7sc04_060 with dissolve
    di "Liar."
    scene ch7sc04_059 with dissolve
    mc "Alright, alright… maybe I’ll miss you a teeny tiny bit."
    mc "I could get used to having you as my sparring partner."
    scene ch7sc04_060 with dissolve
    di "Mhm-hm… me too."
    di "Let’s have another sparring session next time I’m in town?"
    scene ch7sc04_059 with dissolve
    mc "You bet."
    scene ch7sc04_061 with dissolve
    di "Your mentor… he was one of the legendary trinity, wasn’t he?"
    di "Just like your guildmaster Dalen."
    scene ch7sc04_062 with dissolve
    mc "Mh, he was. Oren."
    mc "He taught me everything I know, from basic survival, to various fighting styles."
    scene ch7sc04_063 with dissolve
    mc "My parents were killed because of what… I am."
    mc "Oren found me that very night and took me under his wing from that very moment, at the cost of his own family."
    scene ch7sc04_062 with dissolve
    mc "He abandoned everything he loved, to protect me…"
    mc "And he died before he could reveal to me why."
    scene ch7sc04_063 with dissolve
    mc "He always said, 'One day, when you’re ready… I’ll share everything I know'"
    scene ch7sc04_064 with dissolve
    di "[mc]... I’m sorry."
    di "I wish I could tell you something about him… but I only know of his academy records."
    di "He became a blank canvas after he left the capital to start a family."
    scene ch7sc04_063 with dissolve
    mc "It’s alright, it’s not on you… this is my burden to deal with."
    mc "I'll figure it out some day…"
    scene ch7sc04_062 with dissolve
    mc "Now, why don’t you tell me about your mentor?"
    scene ch7sc04_064 with dissolve
    di "You know the story of what happened to my father…"
    scene ch7sc04_065 with dissolve
    di "My father had pleaded with Blackheart to spare me, and he did… he sent me to an orphanage in Luxenford."
    di "Once I hit puberty, I began to display magical abilities… the others were freaked out, scared of me."
    scene ch7sc04_066 with dissolve
    di "The guildmaster of the knight’s guild, caught wind of my powers and took me under his wing when I was 11."
    di "I’m sure you’ve heard of him."
    scene ch7sc04_067 with dissolve
    $ renpy.pause(0.5)
    di "General Geskir."
    di "He’s one of the most powerful men in Luxeron."
    scene ch7sc04_068 with dissolve
    di "At my current level, he still makes me look like a toddler just learning how to walk."
    mct "Damn… if he’s that much stronger than Diana… can he even be human?"
    di "He’s a no-nonsense man, he was tough on me and had me training day and night."
    scene ch7sc04_066 with dissolve
    di "If I wanted anything to eat, I’d have to train relentlessly."
    di "The only way I was allowed to sleep was when I passed out from exhaustion."
    scene ch7sc04_065 with dissolve
    di "But I never complained… because he-... he didn’t treat me like a freak."
    di "He saw potential in me, he gave me a way to work towards my purpose… my vengeance."
    scene ch7sc04_068 with dissolve
    di "For that… I will owe him a debt I can never repay."
    scene ch7sc04_063 with dissolve
    mc "I understand how you feel…"
    mc "While I haven’t attained my vengeance yet…"
    scene ch7sc04_062 with dissolve
    mc "I’m already grateful that Oren has taught me to the point of being able to avenge my parents."
    scene ch7sc04_069 with dissolve
    di "[mc]... I-..."
    di "I truly believe you will avenge them, and when you do… you’ll know all your struggles have been worth it."
    scene ch7sc04_070 with dissolve
    mc "Thank you Diana… I appreciate that."
    "Diana nods at you with a warm smile."
    scene ch7sc04_071 with dissolve
    di "Phew… sparring for hours with you has left me feeling kind of hot…"
    di "The sun has been baking us thoroughly today."
    scene ch7sc04_072 with dissolve
    di "I’m drenched! I guess I’ll have to pick a more suitable outfit for hour-long sessions with you."
    di "I hate it when my breasts get all sweaty like this…"
    scene ch7sc04_073 with dissolve
    di "*Exhales* Aahh… get some air, girls."
    di "Mmmh… breathe in the fresh air. This is perfect."
    mc "Perfect… yeah… they definitely deserve to breathe."
    scene ch7sc04_074 with dissolve
    di "*Giggles* I know… I shouldn’t be so hard on them, I’m going to spend the rest of my life with them, so I better treat them well."
    di "By the seas! This breeze is hitting all the right spots!"
    scene ch7sc04_073 with dissolve
    di "You should consider yourself happy you don’t have to deal with this as a man."
    di "Breasts are high maintenance, you know?"
    scene ch7sc04_074 with dissolve
    mc "Yeah… I can’t imagine the horror you must have to endure."
    di "*Giggles* I know you’re making fun of me… but as a man, you only get the fun part of breasts… not the struggles."
    scene ch7sc04_075 with dissolve
    di "Mmmh… thank you for today though. I really enjoyed spending time with you."
    mc "Me too, I’m looking forward to our next match."
    scene ch7sc04_076 with dissolve
    di "I’m not going to go easy on you."
    di "If anything, our match today showed you can handle me going all out, so I will continue to do so."
    di "I better get going… as much as this breeze is making the girls feel better, I’m in need of a proper bath."
    scene ch7sc04_077 with dissolve
    mc "*Chuckles* Yeah, I’m heading to the royal palace now. Guess I better have a bath as well."
    di "*Giggling* …"
    scene ch7sc04_076 with dissolve
    di "Getting used to the idea of having maids drawing a bath for you? Lord [mc]."
    scene ch7sc04_077 with dissolve
    mc "It certainly isn’t something I’ll complain about. *Chuckles*"
    di "Mmh-hmm."
    scene ch7sc04_076 with dissolve
    di "I’m setting sail tomorrow at first light…"
    scene ch7sc04_078 with dissolve
    di "You could… visit me, later tonight?"
    di "I have an incredibly expensive bottle of exotic wine I’d love to taste… with you."
    scene ch7sc04_079 with dissolve
    di "Ugh! What am I saying… *Quietly* {size=-10}{b}Get a grip Diana!{/b}{/size}"
    scene ch7sc04_080 with dissolve
    di "I’ll see you when I return, have fun at the palace!"
    mct "*Chuckles* She’s cute when she gets all flustered."
    mct "It was nice spending a bit of time with her before she departs, we’re becoming friends."
    mct "She mentioned visiting her tonight…"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene major_choice with Dissolve(1.5)
    $ renpy.pause(0.5)
    ###major_choice###
    menu:
        "Visit Diana later tonight. ({color=#ff8cdd}Romance lock-in{/color})":
            scene ch7sc04_080 with Dissolve(1.5)
            $ renpy.pause(0.5)
            $ di_path = True
            mct "The tension between us has been increasing with each encounter… I have no desire to stay away from her any longer…"
            $ di_relationship = True

        "I’ve got plenty on my plate as of now. ({color=#2bff8b}Friendship lock-in{/color})":
            scene ch7sc04_080 with Dissolve(1.5)
            $ renpy.pause(0.5)
            $ di_path = False
            mct "*Sighs* As much as I enjoy her company, sharing a bottle of wine with her tonight will definitely lead things down a path I’m not interested in."
            $ di_relationship = False

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_081 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "That must’ve been quite the workout! Diana was drenched in sweat just now when she passed through."
    scene ch7sc04_082 with dissolve
    mc "Yeah, she went all out."
    mc "I suppose it felt great for her to be able to let loose and actually push herself for once."
    scene ch7sc04_081 with dissolve
    el "You’ve been at it for hours, I even managed to go to the market with Alice for some supplies for tomorrow."
    el "And I still beat you back here. *Giggles*"
    scene ch7sc04_083 with dissolve
    mc "Great thinking, if we’re going to spend a few days there, we’d want to avoid having to come back to Luxenford for the basics."
    scene ch7sc04_084 with dissolve
    el "I mostly got food and such since we already have our camping supplies there."
    scene ch7sc04_083 with dissolve
    mc "Oh, are you cooking for me?"
    scene ch7sc04_084 with dissolve
    el "Of course! *Giggles*"

    if eliza_relationship == True:
        el "I’m your girlfriend after all! Cooking comes with the title. *Giggles*"
        scene ch7sc04_083 with dissolve
        mc "*Chuckles* Lucky me."

    else:
        pass

    scene ch7sc04_084 with dissolve
    el "Are you heading to Palace Valois now?"
    scene ch7sc04_083 with dissolve
    mc "Yeah, that was my plan."
    mc "Unless you need me for something here?"
    scene ch7sc04_084 with dissolve
    el "Nuh! I think Sylph and I can handle the rest for today."
    el "Dalen is meeting some acquaintances and Borri is out on a quest with Milton and Flynn."
    scene ch7sc04_083 with dissolve
    mc "Flynn on a quest? *Chuckles*"
    scene ch7sc04_084 with dissolve
    el "I know! *Snickers* But Dalen thinks it’ll be good for him and Borri doesn’t put up with his nonsense."

    if eliza_relationship == True:
        el "Before you go…"
        scene ch7sc04_085 with dissolve
        "Eliza gently strokes your cheek as she moves in closer with her lips puckered."
        scene ch7sc04_086 with dissolve
        el "Mmmh… *Kisses side of lips* I love you."
        scene ch7sc04_087 with dissolve
        mc "I love you too Kitten."
        el "You give me butterflies when you tell me that…"
        scene ch7sc04_086 with dissolve
        "She plants another soft kiss on the side of your lips, intentionally not going for the makeout as she knows she can’t hold back if she does."
        el "Mmhh… say hi to Amelia or Frida for me if you run into them."
        scene ch7sc04_087 with dissolve
        mc "I will, have a good night Kitten, I’ll pick you up in the morning."
        el "Okay… goodnight, my Lion."

    else:
        scene ch7sc04_084 with dissolve
        el "have fun at the palace! And say hi to Amelia or Frida is you encounter them!"
        scene ch7sc04_083 with dissolve
        mc "Will do, I’ll see you tomorrow at dawn."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ss13 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_088 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    $ renpy.pause(0.5)
    mct "There she is, Gina I think her name was?"
    mct "I hope she’s doing alright after what… she endured."
    scene ch7sc04_089 with dissolve
    mc "Hey, how are you holding up-"
    scene ch7sc04_090 with dissolve
    with vpunch
    gin "{b}*Screams* Aiiyh!! NO!!{/b} Don’t touch me!!"
    with vpunch
    mc "H-Hey! It’s me! I’m not here to hurt you!"
    scene ch7sc04_091 with dissolve
    gin "You’re-... it’s you! You’re the man who rescued me!"
    gin "Oh heavens! I just smacked you! I’m so sorry sir! I-I didn’t mean to!"
    scene ch7sc04_092 with dissolve
    mc "Hey… it’s alright, I wasn’t thinking… I shouldn’t have put my hand on you after what you’ve been through recently."
    scene ch7sc04_091 with dissolve
    gin "I-I’ve ruined everything!"
    gin "Now you won’t want to take me in… I can’t believe I struck you like that."
    scene ch7sc04_092 with dissolve
    mc "Hey… relax, you haven’t ruined anything."
    mc "Your name is Gina, right?"
    scene ch7sc04_093 with dissolve
    gin "Yes… Georgina actually, but my loved ones and friends call me Gina."
    gin "Please… do so as well, after what you did for me."
    scene ch7sc04_094 with dissolve
    mc "I’d be honored to call you Gina."
    "She smiles kindly at you, slightly surprised at how pleasant you are."
    scene ch7sc04_095 with dissolve
    gin "You are a good man… a kind man… a man who protects."
    gin "That is worth something… unlike the man whom I married… the man who left me to-..."
    scene ch7sc04_096 with dissolve
    gin "-Suffer the horrors of those mongrels…"
    scene ch7sc04_097 with dissolve
    mc "I wasn't about to let an innocent woman be tormented… I’m sorry I couldn’t have prevented what was done to you-"
    scene ch7sc04_095 with dissolve
    gin "Don’t you apologize for even a second!"
    gin "I’m alive and in good health, thanks to you. I owe you everything, I owe you my life."
    scene ch7sc04_098 with dissolve
    gin "Please… accept my gratitude? It’s all I have to offer you."
    "Gina gently touches your hand, caresses it carefully with her delicate fingers."
    scene ch7sc04_099 with dissolve
    mc "I-... I’m glad I was able to get you to safety."
    scene ch7sc04_098 with dissolve
    gin "Queen Merida told me… your name is [mc]?"
    gin "That you’re a heroic man who’s also saved her daughter? Princess Amelia."
    scene ch7sc04_099 with dissolve
    mc "Mmh, I can’t take all the credit for that, my friends really did most of the heavy-lifting."
    scene ch7sc04_098 with dissolve
    gin "[mc]... the queen told me something… something I almost couldn’t believe if it hadn’t been words from her own mouth."
    gin "That-... I could potentially serve under you? That she could have my marriage dissolved due to neglect of my husband’s duties."
    scene ch7sc04_099 with dissolve
    mc "Mmh, this is true. I’ve discussed it with her as well, but we want it to be your decision… is this something you’d want?"
    scene ch7sc04_098 with dissolve
    gin "*Nods* Yes… it’s something I’d want."
    gin "As I said… I owe you my life. I will happily serve under you, repaying that debt, moon after moon, season after season…"
    scene ch7sc04_099 with dissolve
    mc "You’re being trained here at the palace for the time being, right?"
    scene ch7sc04_100 with dissolve
    gin "Correct, the queen said that it could be a while before I can live with you and apply my services to you?"
    scene ch7sc04_101 with dissolve
    mc "Yeah, it will be a while before I can house you, but as soon as I’m able to, I’ll bring you a new life."
    scene ch7sc04_100 with dissolve
    gin "*Giggling* A new life? Sounds like a dream come true."
    gin "The gods know my life hasn’t been very… fulfilling, but I feel it… standing here with you."
    scene ch7sc04_102 with dissolve
    gin "You will change my life in ways I couldn’t have imagined."
    gin "I will serve you faithfully, I will give my life to you… you will become my purpose."
    scene ch7sc04_101 with dissolve
    mc "*Chuckles* I love the sound of that."
    mc "But for now, just focus on getting better, okay? Rest as much as you can and learn what you can from the maids here."
    scene ch7sc04_100 with dissolve
    gin "Okay!"
    scene ch7sc04_102 with dissolve
    gin "I’ll do my best to be as ready as I can be, for when you decide it’s time for me to join you."
    gin "Thank you for coming to see me!"
    scene ch7sc04_101 with dissolve
    mc "I tend to spend some time here at the palace, so I’ll stop by and check on you every now and then."
    scene ch7sc04_100 with dissolve
    gin "I’d like that! I’d-... really like that."
    scene ch7sc04_098 with dissolve
    gin "Please stop by and see me whenever you want."
    scene ch7sc04_099 with dissolve
    mc "*Chuckles* I will, take care Gina."
    scene ch7sc04_098 with dissolve
    gin "Lord [mc]... take care!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ss59 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc01_308 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    $ renpy.pause(0.5)
    bn "[mc], good. I was going to have sent for you if you hadn’t arrived."
    scene ch7sc01_312 with dissolve
    mc "You were?"
    mc "Did something happen?"
    scene ch7sc01_309 with dissolve
    bn "You tell me, I heard about the Loboten business?"
    scene ch7sc01_310 with dissolve
    mc "Oh? What about it?"
    scene ch7sc01_311 with dissolve
    bn "I received a raven earlier, I almost couldn’t believe what was written…"
    bn "That a woman has been appointed as head of the village?"
    bn "Even more surprising, it wrote that it had been supported by you? A lord."
    scene ch7sc01_312 with dissolve
    mc "Your majesty, I know it isn’t common practice to have women fulfill such roles, but I didn’t give her my support on a whim."
    mc "She is by far the most qualified for the task, as she had worked with the previous village elder for years."
    scene ch7sc01_311 with dissolve
    bn "Be that as it may… this weakens our position."
    bn "A woman doesn’t have the resilience to lead… they just don’t have the head for it."
    scene ch7sc01_310 with dissolve
    mc "Your Grace, I stand by my decision."
    mc "Christa does have a mind for leading the village, she will do well as head of Loboten."
    bn "*Chuckles* …"
    scene ch7sc01_309 with dissolve
    bn "Very well then, you’re the one who supported this so it’ll be on you if she can’t follow through."
    scene ch7sc01_312 with dissolve
    mc "Trust me, Christa will follow through."
    mc "She cares deeply for Loboten, which will ensure she will work day and night to ensure its prosperity."
    scene ch7sc01_313 with dissolve
    bn "Alright, alright. We’ll see how she does."
    scene ch7sc01_311 with dissolve
    bn "It’s slightly concerning though, how close that group of thugs were willing to come to Luxenford."
    bn "This has Lord Alaric’s foul stench all over it… he is pushing and prodding to find weak spots."
    scene ch7sc01_312 with dissolve
    mc "That was my initial conclusion as well."
    mc "It’s a bold power-play on his part, most likely to see how far he can push you as well as distress your people."
    scene ch7sc01_311 with dissolve
    bn "*Sighs* It's working too, reports from nearby villages claim growing discontent, that bandits threaten the area."
    scene ch7sc01_309 with dissolve
    bn "I’ve called upon my generals for an assembly, we need to form a strategic plan of attack."
    scene ch7sc01_310 with dissolve
    mc "Probably a good idea… if that’s all, I’ll be on my way, your Majesty."
    scene ch7sc01_309 with dissolve
    bn "That’ll be all, Lord [mc]."
    bn "Oh, you should stop by the royal library, Amelia is currently studying there and she’s been eager to see you."
    scene ch7sc01_313 with dissolve
    mc "*Chuckles* …"
    scene ch7sc01_312 with dissolve
    mc "Royal Library it is then."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch7sc01_293 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    $ renpy.pause(0.5)
    $ renpy.pause()
    scene ch7sc04_103 with dissolve
    mct "Damn… he’s huge."
    mct "Probably one of the generals Bennen has called in."
    scene ch7sc04_104 with dissolve
    mct "His aura is absurd… he’s strong…"
    scene ch7sc04_105 with dissolve
    mc "Hmh?"
    uk "You."
    uk "You’re the one who’s been distracting Diana."
    scene ch7sc04_106 with dissolve
    mc "General Geskir, I presume?"
    "The man doesn’t answer."
    scene ch7sc04_107 with dissolve
    ges "There’s a war brewing kid, the last thing Diana needs is for you to distract her."
    ges "Especially… distractions of the heart."
    scene ch7sc04_108 with dissolve
    mc "Diana is a grown woman, she can make her own decisions."
    scene ch7sc04_109 with dissolve
    mc "Put your hands on me again, and it’ll be the last time you have hands… General Geskir."
    scene ch7sc04_110 with dissolve
    ges "*Chuckles* I guess I can see why she’d be gravitating towards you… you’ve got a lotta fight in you."
    ges "My warning stands, steer clear of Diana. She is important to the war we’ve got coming our way."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "You leave without any further exchange."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ss83 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_111 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    $ renpy.pause(0.5)
    mct "Damn… this place is huge, it even has several floors."
    mct "It’ll take a while to find Amelia between all these bookshelves…"
    scene ch7sc04_112 with dissolve
    wo "Hold on."
    scene ch7sc04_113 with dissolve
    mc "Hmmh?"
    scene ch7sc04_112 with dissolve
    wo "One moment."
    scene ch7sc04_114 with dissolve
    wo "Nnh…"
    scene ch7sc04_115 with dissolve
    wo "Okay…"
    wo "Let’s have a look at you."
    scene ch7sc04_113 with dissolve
    mc "What are you talking about? I’m here to see-"
    scene ch7sc04_116 with dissolve
    wo "You’re here to see me."
    wo "Until you’ve been given my seal of approval, I’m the only person in this library that matters to you."
    scene ch7sc04_117 with dissolve
    mc "And who are you?"
    wo "..."
    scene ch7sc04_118 with dissolve
    lz "Liz."
    lz "The librarian of Palace Valois. I’m the authority within these walls, act out of order and your ass is out of here."
    mct "*Chuckles* She’s spicy."
    scene ch7sc04_119 with dissolve
    lz "Got it? I don’t take any shit from prickly little noblesons such as you."
    lz "I’ve seen enough of your kind to know you’re up to no good, let me guess… you’re here to bother a woman?"
    scene ch7sc04_120 with dissolve
    mc "First of all, I’m not here to cause trouble…"
    mc "Secondly, don’t associate me with prickly noblesons, I’m a commoner- or… at least I was, until recently."
    scene ch7sc04_119 with dissolve
    lz "*Scoffs* A commoner?"
    scene ch7sc04_121 with dissolve
    lz "You’re a fool if you think I’ll buy that… I’ve never known a commoner to wear elven fabric and visit the royal library."
    lz "I know a noble when I see one."
    scene ch7sc04_120 with dissolve
    mc "You're right, I am a noble."
    mc "I was recently granted Lordship by King Bennen for my deeds."
    mc "But don’t mistake that for me being born into wealth… I was born a commoner and has lived as one my entire life."
    scene ch7sc04_122 with dissolve
    lz "Then you’re-... him."
    lz "You’re Lord [mc]."
    scene ch7sc04_120 with dissolve
    mc "You’ve heard of me?"
    scene ch7sc04_119 with dissolve
    lz "Obviously."
    lz "I spend my days with my nose in books of state."
    scene ch7sc04_121 with dissolve
    lz "Of course I’ve heard about the commoner turned royal bodyguard, then elevated to Lordship."
    lz "It’s not exactly every day such events befall someone of your origins."
    scene ch7sc04_120 with dissolve
    mc "As long as we’re clear on the matter."
    scene ch7sc04_122 with dissolve
    lz "We are, I apologize for my earlier assumption, Lord [mc]."
    lz "I meant no offense, but as I said, I’ve had to deal with a great many prickly noblesons, and you’re dressed the part."
    scene ch7sc04_123 with dissolve
    mc "Apology accepted."
    mc "I’m no stranger to how obnoxious those types can be, so I won’t hold it against you."
    scene ch7sc04_124 with dissolve
    lz "As long as you follow the rules and remain respectful of the people here, and the books..."
    lz "Then you're free to visit the library as you like."
    lz "Now, what brings you here today? I’m not occupied at the moment, so perhaps I could assist you in finding a book?"
    scene ch7sc04_125 with dissolve
    mc "I appreciate it, although I’m not here for a book today."
    mc "I’m actually looking for Amelia, her father said she’d be here studying today?"
    scene ch7sc04_124 with dissolve
    lz "Princess Amelia, huh?"
    lz "She isn’t fond of being disturbed during her studies… but given your position as her bodyguard, I doubt she would mind."
    scene ch7sc04_126 with dissolve
    lz "She likes to study in the back of the library, near the grand windows."
    lz "I believe that’s where you’ll find her."
    scene ch7sc04_127 with dissolve
    mc "Thank you, Liz."
    mc "I appreciate your help."
    "Liz nods at you in approval while visibly surprised at your gratefulness, probably not used to being thanked for her assistance."
    scene ch7sc04_128 with dissolve
    lz "As I said, you’re welcome to stop by anytime… preferably for books and not women."

    ####Choice####
    menu:
        "Be bold and flirt. ({color=#87e1fa}Charisma{/color})":
            mc "What if you’re the woman I came to see next time?"
            lz "Careful, Lord [mc]."
            $ charisma += 1
            scene ch7sc04_129 with dissolve
            lz "You certainly don’t lack confidence… but I fear I’m too much of a woman for a young man such as yourself."
            mc "*Chuckles* We’ll see, Liz."
            "Liz enjoys your cockiness despite brushing off your remark, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ lz_trust += 2

        "Honor her wishes. ({color=#ffee54}Leadership{/color})":
            mc "I'll do my best to not cause a disturbance."
            lz "Good, then you are most welcome here at the library."
            scene ch7sc04_129 with dissolve
            lz "I'll admit, it's lovely to see a young man such as you seek out Princess Amelia."
            $ leadership += 1
            lz "I've only ever seen her hang out with her handmaiden or her cousin, Princess Gwen."
            mc "The princess is great company, I rather enjoy being around her."
            "Liz likes that you appreciate Amelia, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ lz_trust += 2


        "Don't flirt with the librarian. (Neutral)":
            scene ch7sc04_118 with dissolve
            mc "Noted, I appreciate your help."

    scene ch7sc04_130 with dissolve
    mct "There she is."
    mct "I can see why she favors this spot for studying."
    scene ch7sc04_131 with dissolve
    mct "Being able to enjoy the afternoon sun while being comfortable on a cushioned bench."
    mct "With a grand window overlooking the palace gardens."
    scene ch7sc04_132 with dissolve
    mct "She has mentioned before how she has to study quite a bit to be prepared for when she inherits the crown one day."
    mct "Studying politics must be a rather dry subject… but at least she gets a nice view while doing it."
    scene ch7sc04_133 with dissolve
    mct "She looks focused."
    mct "She’s probably been at it hours already…"
    scene ch7sc04_134 with dissolve
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    mc "Hey you."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Mind if I join you for a bit?"
    scene ch7sc04_135 with dissolve
    am "[mc], please… sit with me."
    am "I could use a little distraction before I lose my mind. *Giggles*"
    scene ch7sc04_136 with dissolve
    mc "I gotta admit, this is a pretty cool library, especially with a spot like this. Do you always study here?"
    am "Most of the time, sometimes I do some reading out in the palace gardens or in my room."
    scene ch7sc04_137 with dissolve
    am "But I definitely prefer the library, it’s like… hmm…"
    am "It’s like I’m more focused here? Like being in the ‘correct’ environment helps me immerse myself in whatever I’m doing."
    scene ch7sc04_138 with dissolve
    mc "Yeah, I know what you mean."
    mc "Kind of like training for me, sure I can do exercises in my room but… it just  doesn’t feel the same."
    scene ch7sc04_139 with dissolve
    am "I’d love to watch you workout sometime."
    am "Get all worked up and drenched in sweat-"
    scene ch7sc04_140 with dissolve
    with vpunch
    am "*Gasps* AhH! I-I mean…"
    am "I’ve never seen a man training his body before- Ugh! I… I just mean I find it interesting!"
    mc "*Chuckles* Calm down Amelia…"
    scene ch7sc04_141 with dissolve
    am "That probably made me sound like a total weirdo… *Sighs*"
    scene ch7sc04_142 with dissolve
    am "*Gasps* Ah! [mc]... w-what are you doing?!"
    am "We’re in a library! *Giggles*"
    scene ch7sc04_143 with dissolve
    mc "Oh don’t mind me…"
    mc "I’m just… distracting you from your studies."
    scene ch7sc04_144 with dissolve
    am "*Gasps softly* Aah… [mc]-... someone could see you… touching me."
    scene ch7sc04_143 with dissolve
    mc "Tell me to stop."
    scene ch7sc04_144 with dissolve
    am "Nnngh… no… I’m not going to do that."
    scene ch7sc04_143 with dissolve
    am "But this is highly inappropriate to do… mmgh… in such a public place…"
    scene ch7sc04_144 with dissolve
    mc "I don’t see anything inappropriate about a bodyguard giving the woman he’s assigned to protect a massage to ensure her health."
    am "Oh gosh… mmh… don’t-... don’t make it sound so logical… oh [mc]..."
    scene ch7sc04_143 with dissolve
    am "I really needed this… Nngh… I had no idea… you’re applying the perfect amount of pressure."
    scene ch7sc04_145 with dissolve
    am "*Giggles softly* This is sooooooo much better than studying! Nnnghh…"
    mct "*Chuckles* She’s in total bliss… she must’ve been all tensed up from studying hours on end."
    scene ch7sc04_146 with dissolve
    am "W-Why did you stop?"
    am "Was touching me unpleasant for you?"
    mc "*Chuckles* We both know that isn’t the case."
    mc "But this is all you’re getting for today, Princess."
    scene ch7sc04_147 with dissolve
    am "So mean… did you come here just to tease me?"
    am "I really enjoyed that… your touch."
    scene ch7sc04_148 with dissolve
    mc "Your future will contain more foot rubs, I promise."
    mc "How’s your studies going? What topic are you dealing with today?"
    scene ch7sc04_149 with dissolve
    am "This recent week has been mostly about military strategy and warfare."
    am "Father thinks it’s silly that I’ve chosen this as a topic but with everything going on at the moment…"
    scene ch7sc04_150 with dissolve
    am "I don’t want to be caught with my panties down and not understand how to approach the situation."
    am "I know it’s not usually a woman’s subject to study about warfare…"
    scene ch7sc04_151 with dissolve
    mc "I think it’s a great choice of subject."
    mc "Besides, you’ll be Queen some day. You could be dealing with war in your lifetime, being prepared is wise."
    scene ch7sc04_152 with dissolve
    am "Exactly! You always understand my point of view!"
    am "I’m really glad I have you… you seem to be the only man in all of Midomir who doesn’t judge me for being born with a vagina."
    scene ch7sc04_153 with dissolve
    mc "I have met plenty of women who are more than capable… and plenty of men who are less than."
    mc "I think you’re capable of whatever you set your mind to, Princess."
    scene ch7sc04_152 with dissolve
    am "[mc]... thank you."
    am "Knowing you believe in me… it… it means the world to me."
    scene ch7sc04_153 with dissolve
    mc "*Chuckles* Well then, I better say it louder."
    mc "{b}I BELIEVE IN YOU AMELIA, YOU’RE AN INCREDIBLE WOMAN-{/b}"
    scene ch7sc04_154 with dissolve
    with vpunch
    am "*Giggling* Hush you! We’re in a library!"
    "Amelia rushes to cover your mouth with her hand."
    am "You better be quiet or you’re going to be in big trouble mister! *Snickers*"
    mc "*Muffled* {size=-10}{b}Princess Amelia- Mmffhh… is not only beautiful but incredibly willful- mmffh!{/b}{/size}"
    scene ch7sc04_155 with dissolve
    with vpunch
    am "*Giggling* Oh you’re in {b}DEEP{/b} trouble now buddy!"
    mc "*Muffled chuckling* {size=-10}{b}Mmffhh! Amelia the strongest woman I know- Mmffhh!{/b}{/size}"
    with vpunch
    am "*Snickers* You better be quiet! Or else-"
    scene ch7sc04_156 with dissolve
    "Amelia presses you down, by pushing her waist down onto yours, ensuring you can’t escape her."
    mc "*Chuckles* Or else what? What are you going to do, Princess?"
    am "You’re about to find out-"
    scene ch7sc04_157 with dissolve
    lz "*Clears throat* …"
    lz "I could hear the two of you all the way up at the front desk… what in the world are you doing?!"
    scene ch7sc04_158 with dissolve
    am "Hi Liz… we’re sorry."
    am "Aren’t we [mc]?? *Nudges you*"
    with vpunch
    mc "Yeah… *Clears throat* we apologize for the disturbance Liz."
    scene ch7sc04_159 with dissolve
    lz "Mhm-hm."
    mc "*Whispers* {size=-10}{b}She’s not buying our apology.{/b}{/size}"
    am "*Whispers* {size=-10}{b}I had a feeling she wouldn’t… she’s too smart for a half assed apology.{/b}{/size}"
    scene ch7sc04_160 with dissolve
    lz "I expected this of the new guy, but you Amelia?"
    lz "You’ve always been a role model to the others studying here, showing them how one should behave in a library."
    scene ch7sc04_159 with dissolve
    am "*Sighs heavily* Liz, I’m honestly sorry… okay? We got caught up in some banter and one thing led to-"
    scene ch7sc04_160 with dissolve
    lz "One thing led to another… yes, that much is certainly clear."
    lz "You're mounting him... in public."
    scene ch7sc04_161 with dissolve
    lz "*Sighs* You should probably dismount Lord [mc] and return to your studies, Princess."
    am "R-Right… I’ll get off him!"
    scene ch7sc04_162 with dissolve
    lz "Lord [mc], I think it’s best that you leave for today."
    lz "You’re new and it’s your first offense, so I’ll not ban you from the library… but for today, you should let Amelia resume her studies."
    scene ch7sc04_163 with dissolve
    am "*Whispers* {size=-10}{b}See you later… thank you for the distraction.{/b}{/size}"
    am "*Whispers* {size=-10}{b}I appreciate you coming to see me... it was... a pleasant surprise.{/b}{/size}"
    mc "*Whispers* {size=-10}{b}You’re welcome… I’ll see you around.{/b}{/size}"
    scene ch7sc04_164 with dissolve
    mc "Again… I apologize for disrupting your library, Liz."
    mc "I’ll be on my best behavior next time I visit."
    scene ch7sc04_165 with dissolve
    lz "Hold it."
    mc "Hmmh?"
    scene ch7sc04_166 with dissolve
    lz "If you’re serious about your apology and you’d like to earn your way back into my good graces."
    lz "Then I could use an extra pair of hands around the library sometime."
    scene ch7sc04_167 with dissolve
    lz "There’s a lot of manual labor that is rather exhausting to do all by myself here…"
    lz "If you’re up for a little hard work and want to put your money where your mouth is… then stop by sometime."
    scene ch7sc04_166 with dissolve
    lz "Then I’ll forget this incident ever happened."
    lz "I know this isn’t a typical task for a lord such as yourself… but you claim to be different."

    ####Choice####
    menu:
        "Earn your way back into Liz’s good graces. ({color=#87e1fa}Charisma{/color})":
            scene ch7sc04_168 with dissolve
            mc "I’m not about to refuse a woman in need of my help."
            mc "Especially if it means getting back into her good graces."
            lz "*Scoffs lightly* …"
            scene ch7sc04_167 with dissolve
            lz "I had a feeling you’d not be deterred by a little hard work…"
            $ lz_help = True
            "Liz appreciates that you're willing to make amends, your {color=#87e1fa}Charisma{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch7sc04_169 with dissolve
            lz "After all… you do have a figure that suggests…"
            lz "That you’ve seen quite a bit of hard labour in your life."
            scene ch7sc04_168 with dissolve
            mc "A man doesn’t get a toned physique by sitting around all day."
            $ charisma += 1
            scene ch7sc04_169 with dissolve
            lz "Exactly… I can tell I don’t have to be shy about… putting you to work."
            lz "The library closes at sunset, stop by one of these days and I’ll… have found plenty for you to get your hands on."
            scene ch7sc04_170 with dissolve
            lz "You better leave for today though…"
            lz "I wouldn’t want others thinking it’s okay to cause a disturbance and not get kicked out for it."
            scene ch7sc04_171 with dissolve
            mc "*Chuckles* I’ll see you soon, Liz."
            mc "For a… sunset work session."
            lz "*Giggling* …"
            $ lz_trust += 2
            "Liz enjoys your suggestive banter, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Claim you're no stranger to hard work. ({color=#ffee54}Leadership{/color})":
            scene ch7sc04_168 with dissolve
            mc "You're right, it's not exactly something a lord would do."
            mc "Luckily I'm more of an adventurer than a lord, I'm no stranger to assisting those in need."
            lz "*Scoffs lightly* Mhm-hm."
            scene ch7sc04_167 with dissolve
            lz "Adventurer over lordship? Curious... you're full of surprises."
            $ lz_help = True
            scene ch7sc04_168 with dissolve
            mc "You have no idea... so give me the chance, and I'll happily lend you my hands."
            mc "Having to work my way through the ranks at the guild, I'm no stranger to hard work."
            scene ch7sc04_167 with dissolve
            lz "I'm sure I can find something... for your hands."
            "Liz likes that you have your feet on the ground compared to other lords, your {color=#ffee54}Leadership{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ leadership += 1
            scene ch7sc04_169 with dissolve
            lz "You seem like the type of man who isn't afraid to take charge..."
            lz "The type of man who... gets things done... mhh."
            mc "I'll rise to the occassion, a beautiful maiden is counting on it."
            scene ch7sc04_170 with dissolve
            lz "*Snickers* Such a cocky young man... we'll see how much of that cockiness is left once I've..."
            lz "Worked you... thoroughly."
            lz "You better leave for today though…"
            lz "I wouldn’t want others thinking it’s okay to cause a disturbance and not get kicked out for it."
            scene ch7sc04_171 with dissolve
            mc "*Chuckles* Of course, I’ll see you soon, Liz."
            mc "For a… private work session with Luxeron's best Librarian."
            lz "*Giggling* …"
            $ lz_trust += 2
            "Liz enjoys your suggestive banter, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."


        "Refuse assisting her at the library. (Neutral)":
            scene ch7sc04_166 with dissolve
            mc "Sorry Liz."
            mc "I can’t afford to spend time working here, I’ve got too much going on at the moment."
            scene ch7sc04_167 with dissolve
            lz "That’s fine… I just thought I’d ask, as long as you act civil and according to the library rules, you’re still allowed here."
            lz "But as I said, I think you should leave for today."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss63 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc04_172 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    $ renpy.pause(1)
    scene ch7sc04_173 with dissolve
    $ renpy.pause(1.5)
    scene ch7sc04_174 with dissolve
    $ renpy.pause(1.5)
    scene ch7sc04_175 with dissolve
    $ renpy.pause(1)
    qm "*Giggling softly* ..."
    scene ch7sc04_176 with dissolve
    qm "Hello little guy, aren’t you a beautiful fella?"
    qm "Do you also long for a partner to talk to? *Sighs* To… share your life with?"
    scene ch7sc04_177 with dissolve
    qm "Oh! You do have someone! *Giggles*"
    qm "Go on you two, the sun is setting soon… you should head back to your nest and take cover for the night."
    scene ch7sc04_178 with dissolve
    qm "*Exhales* Maybe one day… I’ll have someone to share my nights with as well…"
    qm "Someone to share my life with…"
    scene ch7sc04_179 with dissolve
    qm "Someone who will provide me with what I’ve always found lacking in my life…"
    qm "A… genuine connection, unwavering… never to be broken."
    scene ch7sc04_180 with dissolve
    mct "Sounds like Merida could use a little pick-me-up."
    qm "*Sighs defeatedly* Hhh… what am I even saying?"
    qm "I should really lay off on the romance novels I’ve been diving into as of late."
    scene ch7sc04_181 with dissolve
    with vpunch
    qm "{b}*Gasps* Aiiyh!{/b}"
    mc "Guess who?"
    scene ch7sc04_182 with dissolve
    qm "I only know one man with such a warm touch…"
    qm "Not to mention he’s the only one who’d be brazen enough to grab me like this…"
    mc "*Chuckles* Oh yeah? And what would his name be?"
    scene ch7sc04_183 with dissolve
    qm "He has quite a heroic name… [mc]! *Giggles*"
    qm "Please… let me look upon you."
    scene ch7sc04_184 with dissolve
    qm "Mmmh… looks like I was right! *Giggles softly*"
    qm "The man I longed to see… hi."
    scene ch7sc04_185 with dissolve
    mc "Hey. *Chuckles*"

    ####Choice####
    menu:
        "Tell Merida she looks gorgeous today. ({color=#87e1fa}Charisma{/color})":
            mc "You look gorgeous today, my Queen."
            qm "*Giggling* …"
            scene ch7sc04_184 with dissolve
            qm "Oh stop it…"
            scene ch7sc04_186 with dissolve
            qm "You really think so?"
            scene ch7sc04_185 with dissolve
            mc "Mmh-hm."
            mc "I’ve been all over the palace today and none have come close to taking my breath away… until now."
            scene ch7sc04_184 with dissolve
            $ charisma += 1
            qm "Oh [mc]... you know how to make a woman feel special."
            "Your lighthearted compliment landed well with Merida, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ queen_trust += 2
            scene ch7sc04_186 with dissolve
            qm "I’m glad you surprised me."
            scene ch7sc04_185 with dissolve
            mc "*Chuckles* Missed me?"

        "Don’t compliment her. (Neutral)":
            mc "Missed me?"

    scene ch7sc04_186 with dissolve
    qm "More so than you could possibly imagine…"
    scene ch7sc04_184 with dissolve
    qm "Won’t you sit with me sweetie?"
    scene ch7sc04_185 with dissolve
    mc "Not yet… first, I want to do this."
    scene ch7sc04_187 with dissolve
    qm "*Gasps softly* Ohh! Oh honey…"
    qm "What… what have I done to earn a massage like this?"
    scene ch7sc04_188 with dissolve
    mc "You’ve been nothing but welcoming towards me, nothing but warm and kind."
    mc "Taking in Gina and sheltering her, rather than sending her back to her deadbeat husband."
    scene ch7sc04_189 with dissolve
    mc "You’re a woman who has a genuine heart, you care deeply for others and their wellbeing."
    mc "I believe such a woman… deserves to be taken care of."
    scene ch7sc04_187 with dissolve
    qm "Any decent woman would’ve done the same if she was in my position… mmmgh."
    qm "I’m nothing special sweetie…"
    scene ch7sc04_188 with dissolve
    mc "You’re wrong Merida."
    mc "There are countless noblewomen throughout the kingdom who never bother to look below themselves in the social hierarchy."
    scene ch7sc04_189 with dissolve
    mc "You’re at the top of the social hierarchy and yet, you’ve managed to maintain who you are… your kindness and warmth."
    qm "*Giggling softly* Mmh…"
    scene ch7sc04_191 with dissolve
    qm "Oh [mc]... you really know how to make me feel… seen."
    qm "Nnhh… oh that’s good… keep applying pressure there."
    mc "You mean right…"
    scene ch7sc04_192 with dissolve
    mc "Here? *Applies pressure to neck*"
    qm "Oh- Mmfhh… honey… you do realise touching a woman like this… makes her feel a very specific type of way?"
    scene ch7sc04_191 with dissolve
    mc "Oh yeah? I couldn’t tell. *Chuckles*"
    scene ch7sc04_190 with dissolve
    qm "Have you been to see Gina yet? She has been asking about you since the moment she woke up."
    scene ch7sc04_188 with dissolve
    mc "Yeah, I saw her earlier when I arrived."
    mc "She seems to be in good health all things considering."
    scene ch7sc04_187 with dissolve
    qm "She is a strong woman… to endure what she… endured. And find the will to keep living? I don’t know if I could…"
    scene ch7sc04_188 with dissolve
    mc "You could."
    scene ch7sc04_189 with dissolve
    mc "But I agree, she has a lot of strength."
    scene ch7sc04_190 with dissolve
    qm "We should still make sure to not rush her into anything… a traumatic event like that could easily re-surface out of nowhere."
    scene ch7sc04_191 with dissolve
    mc "Mhm, we’ll give her all the time she needs to find her footing."
    mc "She was keen on the idea of gathering herself and being trained here at the palace until she can move to my homestead."
    scene ch7sc04_192 with dissolve
    qm "Yes… mmmh… that was my impression as well, when I informed her she could be free of her husband and serve you."
    scene ch7sc04_191 with dissolve
    qm "Oh sweetie… you’re so good to me… mmh… she was eager to see you and make sure you knew how thankful she was."
    scene ch7sc04_188 with dissolve
    mc "Yeah… she made that pretty clear."
    scene ch7sc04_189 with dissolve
    mc "I told her she didn’t owe me anything but she feels indebted to me."
    scene ch7sc04_187 with dissolve
    qm "Of course she does… how often does a kind and strong man save you from the most horrific fate you can imagine?"
    scene ch7sc04_191 with dissolve
    qm "She will feel indebted to you for the rest of her life… make sure you appreciate her and don’t end up taking her for granted."
    scene ch7sc04_192 with dissolve
    mc "I have no intentions of doing that. I just hope she will find enough purpose in serving me?"
    scene ch7sc04_191 with dissolve
    qm "Oh you needn’t worry about that… I can personally speak from experience of being involved in your life…"
    scene ch7sc04_192 with dissolve
    qm "You have a way of… filling women with purpose."
    scene ch7sc04_190 with dissolve
    qm "Just like how you’ve inspired Amelia…"
    qm "She’s changed so much since you came into our lives… she actually smiles now."
    scene ch7sc04_191 with dissolve
    qm "She gets excited about things she used to dread... mmh... oh that's good honey."
    qm "She has found a purpose, she no longer dreads her future, in fact she is studying much harder now."
    scene ch7sc04_192 with dissolve
    qm "She wants to be the best she can be."
    qm "She wants to be a queen who inspires her people."
    scene ch7sc04_191 with dissolve
    mc "I know one such queen already."
    mc "Amelia will become a magnificient queen, she has a great role model in her mother."
    scene ch7sc04_186 with dissolve
    qm "Oh honey… do you… really mean that?"
    scene ch7sc04_185 with dissolve
    mc "You know I do."
    mc "You’re a great mother Merida, you lead by example and want the best for your daughter."
    scene ch7sc04_186 with dissolve
    qm "Gosh… are you trying to make my belly burst with butterflies? *Giggles*"
    scene ch7sc04_184 with dissolve
    qm "Because if you keep this up… massaging me while complimenting me… I’ll melt right here."
    scene ch7sc04_185 with dissolve
    mc "*Chuckles* …"
    scene ch7sc04_187 with dissolve
    qm "*Gasps* Aahh! Oh my…"
    qm "My shoulders love your touch… mmh."
    scene ch7sc04_193 with dissolve
    mc "I can tell. *Chuckles*"
    mc "I’ll have to rub them more often."
    qm "Yes… oh that would be much appreciated…"
    scene ch7sc04_194 with dissolve
    qm "Goodness… you’re reading my body like an open book."
    mc "I do have quite a bit of experience in the matter."

    if qm_relationship == True:
        scene ch7sc04_186 with dissolve
        qm "*Giggles* I bet you do! A handsome young man such as yourself won’t have any issues with the opposite sex."
        scene ch7sc04_184 with dissolve
        qm "You’ve got me curious… about this ‘experience’ you claim to have. *Giggling*"
        scene ch7sc04_185 with dissolve
        mc "Oh yeah?"
        scene ch7sc04_186 with dissolve
        qm "Mhm-hm… in fact, I think you should take me to my room… and show me."
        scene ch7sc04_184 with dissolve
        qm "You know… a little hands-on experience, to show me you aren’t just boasting to impress me."
        scene ch7sc04_185 with dissolve
        mc "*Chuckles* You know… I think you’re on to something."
        mc "You’re the type of woman who won’t just settle for words, you need… action."
        scene ch7sc04_186 with dissolve
        qm "Mmh… [mc], escort me to my room… now."
        scene ch7sc04_185 with dissolve
        mc "As you wish, my beautiful queen."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ss60 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "The two of you sneak past several guards on the way to Merida’s personal bedchamber so as to not raise suspicion."
        scene black with Dissolve(1.5)
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        scene ch7sc04_195 with dissolve
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        qm "*Giggling* Did you remember to lock the door behind us sweetie?"
        mc "I’m pretty sure the entire palace heard the door locking with the eagerness I did that. *Chuckles*"
        scene ch7sc04_196 with dissolve
        qm "Luckily for us, I slam the door shut on occasion whenever I’m upset with Bennen’s lack of effort."
        scene ch7sc04_197 with dissolve
        mc "So you’re saying nobody will disturb us, despite what… sounds can be heard from here and down the hall?"
        "Merida locks eyes with you and giggles warmly, that was exactly what she meant, despite not wanting to admit it."
        scene ch7sc04_196 with dissolve
        qm "What I’m saying is… you were talking a big game out in my gardens… about knowing a woman’s body."
        qm "I think it’s time you prove yourself… show me what-"
        scene ch7sc04_198 with dissolve
        with vpunch
        qm "{b}*Squeals loudly* Aiiyh!{/b} Honey!? *Giggling* W-What are you up to?"
        qm "Am… am I not too heavy for you?"
        scene ch7sc04_199 with dissolve
        mc "*Chuckles* Too heavy? Don’t be ridiculous… you’re light as a feather, Merida."
        mc "As for what I’m doing? I vaguely remember you mentioning your husband never carried you? Not even on your wedding night."
        qm "*Giggles softly* …"
        scene ch7sc04_200 with dissolve
        qm "[mc]... this feels much more like the wedding night I always wanted… instead of the one I actually got."
        qm "If only I had met you first…"
        scene ch7sc04_201 with dissolve
        mc "You’ve met me now."
        qm "*Giggles softly* Mh-hm…"
        scene ch7sc04_202 with dissolve
        qm "You’re right… I’ve met you now. That’s what matters."
        qm "Will you put me down by the fireplace? I’ve always wanted to experience such a thing."
        scene ch7sc04_203 with Dissolve(1.5)
        $ renpy.pause(0.5)
        qm "*Giggling happily* Sweetie… it feels just like I imagined it would… with you."
        qm "You didn’t even tremble or flinch in the slightest… you’re… strong."
        scene ch7sc04_204 with dissolve
        mc "Benefit of having been physically active for my entire life."
        mc "*Chuckles* You’re simply reaping the benefits."
        scene ch7sc04_205 with dissolve
        qm "I refuse to only reap benefits from you and not… provide you with any of my own."
        qm "Please, make yourself comfortable honey."
        scene ch7sc04_206 with dissolve
        qm "*Moans softly* Oh goodness! Mmh… there’s that warm touch I’ve grown so familiar with."
        qm "Am I being blessed with another of your legendary foot massages?"
        mc "Mhm, you are. I vividly remember how much you enjoyed the last one."
        scene ch7sc04_207 with dissolve
        qm "*Moans softly* Oh [mc]... you’re so sweet to me…"
        scene ch7sc04_208 with dissolve
        qm "I doubt a woman has ever lived to be treated with such care by a man- mmhh…"
        scene ch7sc04_207 with dissolve
        mc "I know my audience tonight, what she needs… what she deserves."
        scene ch7sc04_208 with dissolve
        qm "Oh sweetie… your touch is mmmagical! Ahh…"
        scene ch7sc04_209 with dissolve
        qm "*Whimpers softly* Mmgh… that… that feels incredible…"
        qm "You’re doing so well… mmgh… at proving you know a woman’s body- aahh…"
        scene ch7sc04_207 with dissolve
        mc "I have an incredible woman in my hands…"
        scene ch7sc04_208 with dissolve
        mc "Even if I had no experience, my instincts would guide me in your presence."
        scene ch7sc04_209 with dissolve
        qm "Oh honey… I-... I believe you… mmh."
        mct "The way she’s squeezing her thighs together, she's squirming at every touch, she’s really feeling it."
        mct "It’s time to take this further… she is more open to it tonight than ever before."
        scene ch7sc04_210 with dissolve
        mc "I believe you’re ready for a deeper massage."
        qm "*Giggling* …"
        scene ch7sc04_211 with dissolve
        qm "A deeper massage? Are you sure honey?"
        scene ch7sc04_210 with dissolve
        mc "I’m sure."
        scene ch7sc04_211 with dissolve
        qm "Okay… you’re the one with the experience, I’d be wise to follow your guidance."
        qm "What do you need me to do?"
        scene ch7sc04_210 with dissolve
        mc "Lie down on your stomach for me."
        scene ch7sc04_212 with dissolve
        qm "*Giggles* This is quite… exhilarating."
        qm "Being told what to do by… you."
        scene ch7sc04_213 with dissolve
        qm "Like this sweetie? Am I doing it right?"
        mc "That’s perfect… you’re perfect."
        qm "[mc]... please begin your massage, I’m feeling a little exposed here. *Giggles*"
        scene ch7sc04_214 with dissolve
        qm "*Moans* Oh my! Mmh… somehow it always surprises me when you grab me… you’re so firm with me, yet attentive."
        mc "Being neglected and untouched for over 20 years… you’ve got a lot to catch up on, and I will be the one to lead you."
        qm "*Whimpers* Mmh… yes, I… I’d like that."
        scene ch7sc04_215 with dissolve
        mc "Tell me if I’m applying too much pressure, I know how sensitive a woman’s thighs can be."
        qm "Goodness… don’t-... don’t worry about that honey… whatever you’re doing… it’s incredible."
        scene ch7sc04_216 with dissolve
        mc "You’re in good hands, I promise."
        qm "[mc]... I feel you… mmh."
        scene ch7sc04_215 with dissolve
        mc "I can’t believe Bennen has neglected you for twenty plus years…"
        mc "I wouldn’t be able to keep my hands off a woman such as you…"
        scene ch7sc04_216 with dissolve
        qm "*Moans softly* Our evidence is rubbing my thighs as we speak… mmgh… k-keep doing that."
        qm "Do you know how good it feels to be seen finally? To be… touched. Mmmh-mmh…"
        scene ch7sc04_217 with dissolve
        qm "*Moans* Oh sweetie… c-careful…"
        qm "You’re getting a little close there… mmmh…"
        qm "You know… mmh… we can’t go there… it’s… too complicated-"
        scene ch7sc04_218 with dissolve
        qm "*Gasps* Aahh… [mc]!"
        mc "Tell me to stop and I will."
        qm "*Moans* St… mmh… o-okay… just a little bit."
        scene ch7sc04_219 with dissolve
        mc "Red panties Merida? You knew I was coming to see you today."
        qm "*Whimpers* No… but when I heard you were at the castle… mmh… I put them on in hope of seeing you."
        scene ch7sc04_218 with dissolve
        mc "Mmh… you wearing them just in the hopes of seeing me… you know how to make me smile."
        scene ch7sc04_219 with dissolve
        qm "You like them then? I bought them while you were away… Aahh… hoping to one day show them off to you."
        scene ch7sc04_220 with dissolve
        mc "I love them… they look gorgeous on your thick and shapely ass, Merida."
        qm "*Moans* Oh my… the way you’re touching it… I don’t think I need to question if your compliment is genuine… ahh."
        scene ch7sc04_219 with dissolve
        mc "If there are any doubts… I’ll dispel them with this massage."
        scene ch7sc04_220 with dissolve
        qm "You’re good at this… mmgh… being massaged by you is an incredible experience."
        scene ch7sc04_219 with dissolve
        qm "You make me feel like I’m the only woman in all of Midomir… Mmh!"
        scene ch7sc04_220 with dissolve
        mc "You are Merida… there’s none that rivals you."
        mc "I’m going to remove your dress now."
        scene ch7sc04_221 with dissolve
        qm "My dress? I… don’t you think that is a little too far sweetie?"
        qm "You’ve already rubbed my ass rather extensively… but being fully naked… that’s… incredibly indecent."
        scene ch7sc04_222 with dissolve
        mc "I’m going to move upwards to your back, your dress will be in the way."
        scene ch7sc04_221 with dissolve
        qm "Oh… if… if it’s for the massage, then I-... I suppose it would be alright to remove my dress, sweetie."
        scene ch7sc04_222 with dissolve
        mc "You only get to experience your first full-body massage once Merida, I want to ensure you have the best experience."
        qm "*Giggles happily* Mhm-hmm!"
        scene ch7sc04_223 with dissolve
        "You remove her dress and move further up until your waist is pushing against her bubbly ass."
        qm "Oh this feels… oh my… I’ve never been exposed like this with a man before… mmh."
        scene ch7sc04_224 with dissolve
        mc "This is your first time being naked with a man?"
        scene ch7sc04_223 with dissolve
        qm "*Gasps softly* Aahh… yes."
        scene ch7sc04_224 with dissolve
        mc "You know how to make me feel truly blessed…"
        mc "Mmhh, you’re pretty tense here, I’ll have to work this area for a while."
        scene ch7sc04_223 with dissolve
        qm "*Moans softly* Oh honey- Mmhh…"
        qm "I’ve been a little stressed as of late… mmgh… you’re making all of it disappear in this moment."
        scene ch7sc04_224 with dissolve
        mc "Don’t worry… I have no intention of stopping until you feel like you’re in the high-heavens."
        scene ch7sc04_225 with dissolve
        mc "So, if you’ve never been naked with Bennen… how did you? Amelia?"
        scene ch7sc04_226 with dissolve
        qm "Ugh… I hate just thinking about it… it makes me feel so small."
        qm "As you know, I’ve only been with him once, which was on our wedding night… he asked me to keep my dress on."
        scene ch7sc04_227 with dissolve
        mc "He did? He wasn’t tearing it off you as fast as humanly possible?"
        qm "No… quite the opposite, I had begun to undress but he swiftly asked me to keep my dress on."
        qm "*Imitates Bennen* ‘Honey, you look beautiful in this dress, please… you must keep it on’"
        scene ch7sc04_226 with dissolve
        qm "I thought it to be an odd request, but didn’t question it… so we proceeded to the bed…"
        qm "He only pulled the dress up to the bare minimum and he didn’t look at me once, he kept his eyes closed during the act."
        scene ch7sc04_227 with dissolve
        qm "Luckily it was short-lived, I was about to fall asleep from the lack of stimulus and intimacy."
        mc "Bennen is a fool... there's nothing I desire more than to undress you and reveal your gorgeous body."
        scene ch7sc04_223 with dissolve
        qm "*Moans softly* Aahh… sweetie… mmh… you really know what to say... mmh."
        qm "See… this is how you stimulate a woman… mmh… this is how you should be intimate with her."
        scene ch7sc04_224 with dissolve
        mc "I don’t have any intentions of following Bennen's way of handling a woman… he’s clueless in this matter."
        scene ch7sc04_225 with dissolve
        qm "*Giggling happily* Mmmh…"
        scene ch7sc04_223 with dissolve
        qm "You're definitely not clueless... your touch proves it."
        scene ch7sc04_228 with dissolve
        qm "*Moans softly* Oh [mc]... I feel so seen and appreciated when I’m with you…"
        qm "How you speak to me… care for me… touch me… mmh."
        scene ch7sc04_225 with dissolve
        mc "You deserve the best Merida… I intend to provide that."
        scene ch7sc04_229 with dissolve
        qm "{b}*Gasps* Aiyh! [mc]!{/b} *Giggling* W-What are you doing young man?"
        "You push down gently but firmly, pressing her down against the soft carpet, squishing her large and shapely breast to stimulate them as well."
        mc "This is all part of the massage, Merida… mmh… allow me to give you a proper massage."
        scene ch7sc04_230 with dissolve
        stop music fadeout 2.0
        qm "*Moans softly* It is? Oh… ohh… I… I guess it’s alright then… please, keep going."
        play music lewd_1 fadein 1.5
        #stop music fadeout 1.0
        scene qm_lewd3 with dissolve
        $ renpy.pause()
        qm "I’m in your hands sweetie… I’m at your mercy… mmh… I trust in your guidance."
        mct "Five hells… I’m already rock hard from touching her for well over an hour at this point…"
        "Merida doesn’t point it out, but she clearly feels your cock through your pants as you press against her."
        "She instinctively begins to push her plump ass back against you while you continue the massage."
        qm "*Moans softly* This is highly inappropriate you know… ahh… pressing yourself onto your queen like this… mmh."
        mc "Is that so? It feels entirely appropriate to me… ahh… ffhh… your body is incredible Merida."
        with vpunch
        qm "*Giggles softly* You really like an old body like mine? It’s not as tight and firm as it used to be-"
        mc "*Applies pressure* You know better than to compare yourself to the youth, you are in your prime."
        mc "You’re not old… you’re mature… you’re incredibly firm and tight all over, while being perfectly supple and shapely.”"
        qm "*Moans softly* Ahh- [mc]... you say such outrageous things… mmmh… I feel… I feel your- *Gasps*"
        scene ch7sc04_231 with dissolve
        qm "Honey! Y-Your cock is out!"
        mc "Fuck… mmh… us rubbing together must’ve pushed my pants down enough to release it."
        scene ch7sc04_232 with dissolve
        qm "Ohh… I see… your pants are in the way sweetie?"
        qm "Then… if we are to continue this massage… I think it’s best if you take off your pants fully, so they aren’t in the way."
        scene ch7sc04_233 with dissolve
        mc "I think you’re right… they’ll only be in the way."
        scene ch7sc04_232 with dissolve
        qm "Besides… it’s not fair I’m the only one who’s exposed… *Giggling softly*"
        scene ch7sc04_233 with dissolve
        mc "You’re absolutely right, my queen… where are my manners."
        scene ch7sc04_232 with dissolve
        qm "*Giggles* It seems I will have to teach you proper etiquette when dealing with a nude queen."
        qm "Begin by removing your pants sweetie."
        scene ch7sc04_234 with dissolve
        "You get to your feet and begin undoing your pants."
        qm "You’re staring at my ass… aren’t you?"
        mc "*Chuckles* There isn’t a world where my eyes wouldn’t gravitate towards your plump ass."
        scene ch7sc04_235 with dissolve
        qm "*Giggling* I’m happy to provide such a view… only for you."
        qm "Please honey… come back down to your queen… she craves your hands… your massage."
        "As you’re about to take your first step towards what would an undeniably unforgettable night with Merida, you hear knocking at the door."
        scene ch7sc04_236 with dissolve
        bn "Honey? Why’s your door locked?"
        with vpunch
        qm "*Startled* B-Bennen?! H-Hi honey! What are you doing here?!"
        bn "It’s half an hour past dinner time? Amelia and I have been waiting for you at the dining hall."
        qm "Oh gosh! I completely forgot! I’ll join you in a moment!"
        bn "Honey, are you okay in there? You sound a little out of it? I’m coming in, just let me find the keys."
        scene ch7sc04_237 with dissolve
        "Merida swiftly gets to her feet and rushes to you, grabbing your cock firmly."
        qm "*Whispers* {size=-10}{b}Honey, come with me! He can’t know you’re in here!{/b}{/size}"
        mc "Fff… okay, where?"
        qm "Over here, behind my room divider."
        scene ch7sc04_238 with dissolve
        "As she rushes you behind the divider you the hear the door to the room unlock, yet she maintains her firm grip on your cock."
        qm "*Whispers* {size=-10}{b}Sshh sweetie… you’ve got to be quiet, mmh… you’re so hard for me.{/b}{/size}"
        scene ch7sc04_239 with dissolve
        bn "Honey is everything alright with you?"
        bn "You usually never miss dinner? Hell, you’re the one who always calls me out for being busy."
        qm "*Whispers* {size=-10}{b}That’s it sweetie… you’ve treated me so well tonight… let me do this for you.{/b}{/size}"
        scene ch7sc04_240 with dissolve
        qm "*Whispers* {size=-10}{b}You’re such a good boy… mmh… letting your queen touch you like this… you like it honey?{/b}{/size}"
        mc "Ffhh… yeah… mmmh… your touch is divine."
        scene qm_lewd4 with dissolve
        $ renpy.pause()
        bn "Honey? Did you say something?"
        qm "N-No… just that you should leave… I’d prefer to be alone at the moment."
        mc "*Quietly* {size=-10}{b}Mmmgh… fuck that’s good Merida…{/b}{/size}"
        bn "Honey don’t be silly… you need to have dinner, Amelia and I haven’t had any either as we are waiting for you."
        qm "*Quietly* {size=-10}{b}This man just can’t take a hint? He doesn’t even know his wife is touching another man right this moment…{/b}{/size}"
        qm "Bennen, just leave! I’ll be down in a little bit- Mmmh… once I’m done handling things here."
        bn "Honey… I know I’ve neglected you as of late… more so than usual, but I’ve just been busy as you know."
        qm "*Quietly* {size=-10}{b}Mmh... you're such a good boy... keep rubbing my ass while you look at my breasts.{/b}{/size}"
        qm "*Quietly* {size=-10}{b}Just feel me... mmh... let me touch you... let my hand satisfy you.{/b}{/size}"
        scene qm_lewd5 with dissolve
        $ renpy.pause()
        qm "Ugh… this isn’t about that Bennen!"
        qm "I’ve just been trying on some new clothes and simply forgot the time!"
        bn "Oh! *Chuckles* My bad, I should’ve known!"
        bn "Those black pants near the fireplace, did you buy them? You’ve never wanted to wear black previously?"
        qm "The pants? Oh… yes… I wanted to try something different… mmh… it’s time for a change in my life."
        "Merida tightens her grip as she feels your cock starting to throb."
        qm "*Quietly* {size=-10}{b}That’s my sweet boy… let your queen take care of you… mmh…{/b}{/size}"
        qm "*Quietly* {size=-10}{b}Be a good boy and cum for me… show me that you enjoy my touch, [mc].{/b}{/size}"
        with vpunch
        mc "Ffhh… Merida… I… I can’t hold it much longer."
        bn "Honey? What was that sound? You okay back there?"
        qm "Oh! Yes… I’m fine! Better than fine actually… mmh… I just stubbed my toe on the dresser."
        qm "*Quietly* {size=-10}{b}Cum for me sweetie… cum for your queen.{/b}{/size}"
        bn "Okay honey, I can tell you don’t want to be disturbed at the moment… we’ll wait for you in the dining hall, please don’t take too long."
        with vpunch
        qm "*Moans softly* I’ll-... I’ll be right there! Mmmh… *Quietly* {size=-10}{b}You’re so hard! Mmgh… throbbing like crazy for me…{/b}{/size}"
        with vpunch
        "As soon as you hear the door close behind Bennen, you can no longer hold your orgasm back with Merida’s passionate stroking."
        scene ch7sc04_241 with dissolve
        with vpunch
        mc "*Moans* Aah! Merida- Mmmgh!!"
        qm "*Moans happily* That’s it sweetie! You’re such a good boy! Mmmh! Cum for me!"
        with vpunch
        scene ch7sc04_242 with dissolve
        mc "Fffhh… that was insane… you really squeezed it out of me."
        stop music fadeout 1.0
        qm "Mmh… you were such a good boy."
        play music relax_2 fadein 1.0
        qm "Your cock really is something special… beautiful, powerful and filled with what I desire."
        scene ch7sc04_243 with dissolve
        qm "*Sighs* This was too risky… we allowed ourselves to once again be overtaken by our feelings for each other…"
        qm "We cannot be doing things like this… we need to control ourselves."
        scene ch7sc04_244 with dissolve
        mc "Merida…"
        scene ch7sc04_243 with dissolve
        qm "No, sweetie just do as I say…"
        qm "Thank you for the massage, I don’t regret it… I enjoyed it as you’re well aware… but this is too dangerous."
        scene ch7sc04_244 with dissolve
        mc "Merida-"
        scene ch7sc04_245 with dissolve
        qm "Please leave for tonight and forget this happened… I have to get dressed and join Bennen and Amelia for dinner."
        mct "Five hells… tonight we took a huge step forward, she was even willing to make love, I could sense it on her pheromones."
        mct "But Bennen’s interruption not only stopped it from happening but also set our progress back."
        mc "Merida, I’ll leave… but only after doing this."
        scene ch7sc04_246 with dissolve
        qm "Doing what-"
        mc "This."
        scene ch7sc04_247 with dissolve
        with vpunch
        "You grab Merida and pull her closely into your arms."
        qm "Mmmhfh! Mmhfh… Nnh-nhm… oh honey…"
        qm "Kiss me."
        scene ch7sc04_248 with dissolve
        qm "Mmfhh… mmh… *Kisses gently* [mc]... mmh…"
        mc "If you want to hide our feelings for the time being… so be it, but we both know they are real… genuine… mmh."
        scene ch7sc04_249 with dissolve
        qm "*Kisses intimately* Ohh-mmh… I know sweetie… I’ve never felt emotions with a man as I do with you… mmh."
        qm "If it weren’t for the danger I’m putting you in… I wouldn’t hold back… I would give myself to you… mmh… right now."
        scene ch7sc04_248 with dissolve
        mc "I can handle the danger… I’m more worried about the fallout on your end… which is why I won’t push you on the matter."
        mc "Despite my heart and body craving you."
        scene ch7sc04_249 with dissolve
        qm "Oh sweetie… please know my heart and body feels the same… *Kisses intimately* I feel the same."
        scene ch7sc04_247 with dissolve
        qm "*Heavy breaths* O-Okay… enough sweetie… we’ve risked enough for one night, please take your leave."
        mc "Mmh… I’ll see you around, Merida."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        "You take your leave, ensuring to remain unseen, allowing Merida to get dressed and join her family for dinner."


    else:
        scene ch7sc04_186 with dissolve
        qm "*Giggles* I bet you do! You should probably take your leave for today before someone sees you touching the queen."
        scene ch7sc04_184 with dissolve
        qm "Thank you for checking on me and… for the massage. I really needed this."
        scene ch7sc04_185 with dissolve
        mc "You’re welcome Merida. I wasn’t about to visit the palace and not check in on my favorite queen."
        scene ch7sc04_186 with dissolve
        qm "Always the charmer! *Giggles*"
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0

    scene ss46 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc04_250 with Dissolve(1.5)
    $ renpy.pause(0.5)
    ri "..."
    scene ch7sc04_251 with dissolve
    $ renpy.pause()
    scene ch7sc04_252 with dissolve
    uk "We need to talk."
    ri "Hm."
    scene ch7sc04_253 with dissolve
    uk "It’s about your poison dosage…"
    uk "You can’t keep doing this… especially if you up the dosages this often… your body doesn’t have time to adapt."
    scene ch7sc04_254 with dissolve
    uk "Last time I found you passed out, right here on the floor… if any of them had located you while you were alone…"
    scene ch7sc04_255 with dissolve
    ri "I know."
    scene ch7sc04_254 with dissolve
    uk "You would be dead."
    scene ch7sc04_255 with dissolve
    ri "I know."
    scene ch7sc04_254 with dissolve
    uk "Why are you pushing this matter? You were caught offguard, sure… but this is extreme."
    scene ch7sc04_255 with dissolve
    ri "Caught offguard, never again."
    ri "Need to build resistance… to defeat her."
    scene ch7sc04_254 with dissolve
    uk "That woman from the society? Viperia? You already defeated her."
    scene ch7sc04_255 with dissolve
    ri "Nnh-nh. Body gone… still alive."
    scene ch7sc04_256 with dissolve
    uk "*Sighs* Rin, you’re a great partner in our line of work, skilled and direct… but this?"
    uk "The Society of Shadows has been on our tail for a while, their attacks on you have increased… why?"
    scene ch7sc04_257 with dissolve
    ri "Unknown."
    ri "Must… find out. Upping dosage, important."
    scene ch7sc04_256 with dissolve
    uk "*Sighs* You’re preparing for war with them… you can’t take on the Society on your own, you know this."
    uk "You need allies."
    scene ch7sc04_257 with dissolve
    ri "Only need one."
    scene ch7sc04_256 with dissolve
    uk "*Sighs* That guy again? C’mon…"
    uk "Isn't about time you forgot about him-"
    scene ch7sc04_258 with dissolve
    with vpunch
    uk "*Groans* Hnngh!"
    ri "Mention him again… I dare you."
    uk "Hnngh… fine, but at least tell me why you won’t contact him?"
    scene ch7sc04_259 with dissolve
    ri "Refuse to… burden him."
    ri "Now, leave it be."
    scene ch7sc04_260 with dissolve
    ri "Mention him again…"
    ri "Will be, last thing… you do."
    scene ch7sc04_259 with dissolve
    ri "Clear?"
    uk "Hnngh… clear."
    scene ch7sc04_260 with dissolve
    ri "Hm."
    scene ch7sc04_261 with dissolve
    ri "Come, we have contract."
    uk "At least I won’t have to ask if you’re up for killing some cultists."
    ri "Need the exercise, otherwise… body can’t handle next dosage."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss52 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc04_262 with Dissolve(1.5)
    $ renpy.pause(0.5)
    bth "*Giggling*"
    scene ch7sc04_263 with dissolve
    al "These robes are great Luna! I’ve never worn silk before… it’s so smooth."
    al "And it feels perfect on my skin after we just had our bath, it doesn’t stick to my damp skin."
    scene ch7sc04_264 with dissolve
    al "I usually only wear a towel for at least half an hour after bathing, until my body has dried off properly."
    al "But with robes like these… mmh! *Giggles*"
    scene ch7sc04_265 with dissolve
    lu "I’m glad you like them! I thought they were fitting since we’re having a sleepover!"
    lu "You’ve really never had anything made of silk?"
    scene ch7sc04_266 with dissolve
    lu "Not even panties or a bra?"
    lu "Or a blanket? Bed sheet? Scarf?"
    scene ch7sc04_267 with dissolve
    al "Never had any of such luxuries, being from a small village like Riverside, very few people had such privilege."
    al "Pretty much just the village elder and his family."
    scene ch7sc04_268 with dissolve
    al "One time I was lucky enough to be allowed to touch a bit of silk fabric from a traveling merchant that passed through Riverside."
    al "I remember how my mother rushed me away from it, said not to touch anything as she was scared I would get it dirty."
    scene ch7sc04_267 with dissolve
    al "[mc] was at the market with his parents as well that day, apparently he had seen how much I liked the silk fabric…"
    scene ch7sc04_269 with dissolve
    al "Later that day, when we met up to play at the apple orchards, he presented me with a small piece of silk!"
    scene ch7sc04_268 with dissolve
    al "I was awestruck… he had followed the merchant around the market, and eventually a piece of fabric fell off the wagon."
    scene ch7sc04_269 with dissolve
    al "So [mc] got hold of it without anyone noticing and ran for the hills. *Giggles*"
    scene ch7sc04_267 with dissolve
    al "He got quite the scolding upon his parents learning of what had happened and my mother promptly returned the silk."
    scene ch7sc04_269 with dissolve
    al "But for a few hours… I had my very own piece of silk, because of him."
    scene ch7sc04_266 with dissolve
    lu "*Snickers* That definitely sounds like [mc]!"
    lu "He has this quality where if he notices someone he cares about wanting something… he’ll do his best to provide it."
    scene ch7sc04_270 with dissolve
    lu "I really admire that about him…"
    lu "He’s a provider."
    scene ch7sc04_266 with dissolve
    lu "He’ll do anything to take care of us, protect us and provide for us."
    lu "We should do the same for him!"
    scene ch7sc04_268 with dissolve
    al "I agree. We should all strive to take care of him as best we can, just as he does for us."
    scene ch7sc04_267 with dissolve
    al "He is different from the kid I grew up with, a lot has changed in his life…"
    scene ch7sc04_269 with dissolve
    al "But at his core, he still has a genuine heart."
    scene ch7sc04_266 with dissolve
    lu "Mhm-hm! I can attest to that! *Giggles*"
    scene ch7sc04_271 with dissolve
    lu "We need to be ready to fuck up Taron the very moment we get the chance!"
    with vpunch
    lu "After everything he’s put [mc] through, heck… all of us through, he needs to be stopped… permanently!"
    scene ch7sc04_272 with dissolve
    with vpunch
    lu "I swear Alice! If that bastard shows his face again or attempts to harm [mc], I’ll incinerate him!"
    al "L-Luna calm down! I’m with you on all of it but don’t incinerate us prematurely!"
    scene ch7sc04_273 with dissolve
    lu "*Sighs* Sorry… I didn’t mean to scare you, I just get so worked up when I think about that bastard."
    lu "Hurting my mom… blackmailing me… turning Rose against us… injuring Eliza… toying with [mc]... Ugh!"
    scene ch7sc04_274 with dissolve
    al "Uhh… Luna, your robe…"
    lu "Hmh?"
    scene ch7sc04_275 with dissolve
    with vpunch
    lu "*Squeals* A-Alice! Why didn’t you say so!"
    al "*Snickers* I did? What’s the big deal, we’ve seen each other naked plenty of times when bathing?"

    if luna_relationship == True:
        scene ch7sc04_265 with dissolve
        lu "*Sighs* I-... I know, but..."
        scene ch7sc04_264 with dissolve
        al "But it’s different now that you’ve fallen in love with [mc] and he’s made you his."
        lu "*Nods* Mhm-hm."
        scene ch7sc04_265 with dissolve
        lu "Bathing is one thing… but in other situations, I-... I only want him to see me."
        scene ch7sc04_268 with dissolve
        al "I get it, which is why I pointed it out so you could fix the robe."
        al "Trust me… I have no desire to sit and stare at your perfect breasts all night and feel insecure about my own."
        scene ch7sc04_266 with dissolve
        lu "Don’t be silly! Yours are perfect too! I wish mine were more like yours!"
        lu "Yours are perky and they sit perfectly!"
        scene ch7sc04_268 with dissolve
        al "As if yours doesn’t? And you have size! Something most men seem very focused on!"
        scene ch7sc04_267 with dissolve
        al "Trust me… having small breasts like me, makes you practically invisible to men!"
        scene ch7sc04_265 with dissolve
        lu "*Giggling* As if, we’ve both seen several guys at the academy eyeing you!"
        scene ch7sc04_264 with dissolve
        al "C-Changing topics! I heard the two of you rescued a woman from a goblin attack?"

    else:
        scene ch7sc04_266 with dissolve
        lu "*Giggles* I suppose you’re right… still, it’s different when bathing."
        scene ch7sc04_268 with dissolve
        al "I know, which is why I pointed it out so you could fix it."
        al "Trust me… I have no desire to sit and stare at your perfect breasts all night and feel insecure about my own."
        scene ch7sc04_265 with dissolve
        lu "Don’t be silly! Yours are perfect too! I wish mine were more like yours!"

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music mmm_elven_forest fadein 1.0
    stop music fadeout 1.0
    if di_relationship == True:
        scene ss84 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.5
        scene ch7sc04_276 with Dissolve(1.5)
        $ renpy.pause()
        scene ch7sc04_277 with dissolve
        $ renpy.pause()
        scene ch7sc04_278 with dissolve
        $ renpy.pause()
        scene ch7sc04_279 with dissolve
        $ renpy.pause()
        scene ch7sc04_280 with dissolve
        $ renpy.pause(1)
        di "*Whimpers softly* Mmh! What a great way to end my time here in Luxenford this time around."
        di "He provided me with something no man has ever managed… my vengeance."
        di "Even Geskir couldn't bring me that... but [mc], he delivered... like he promised."
        scene ch7sc04_281 with dissolve
        di "Not to mention… how he elevated my heartrate during our sparring today… I’ve never felt so excited… such a surge of emotions."
        di "I can’t believe I almost invited him to join me tonight… what was I thinking…"
        di "*Sighs* He’s already shared my bed with me once… would it really be so horrible if we… shared it again?"
        scene ch7sc04_282 with dissolve
        "*Knocking on cabin door*"
        di "Huh?! My crew knows not to seek me out past lights out."
        scene ch7sc04_283 with dissolve
        "*Knocking on cabin door*"
        di "Whoever it is…"
        scene ch7sc04_284 with dissolve
        di "They’ll come to regret trespassing on my ship."
        di "I can feel their presence… they’re strong."
        scene ch7sc04_285 with dissolve
        di "*Gasps quietly* {size=-10}{b}What a powerful aura… I can feel it through the door… it feels familiar but I can't risk it.{/b}{/size}"
        di "*Quietly* {size=-10}{b}I’ll need to strike swift and true, I’m at a disadvantage within these close-quarters.{/b}{/size}"
        scene ch7sc04_286 with dissolve
        with vpunch
        di "{b}*Shouts* You’re going to regret trespassing on a royal vessel!{/b}"
        scene ch7sc04_287 with dissolve
        with vpunch
        di "You’ve chosen the wrong woman to sneak up on!"
        scene ch7sc04_288 with dissolve
        di "*Gasps* H-Huh?"
        di "You… you’re here?"
        scene ch7sc04_289 with dissolve
        di "I-..."
        scene ch7sc04_290 with dissolve
        di "W-What are you doing here?"
        scene ch7sc04_291 with dissolve
        di "I-... I thought I wouldn’t see you until I return?"
        di "W-Why are you here?"
        scene ch7sc04_292 with dissolve
        with vpunch
        di "*Gasps* Aahh!"
        scene ch7sc04_293 with dissolve
        mc "You."
        scene ch7sc04_294 with dissolve
        di "What… what do you mean?"
        scene ch7sc04_293 with dissolve
        mc "I came to see you… I wanted to… see you, Diana."
        scene ch7sc04_294 with dissolve
        di "Oh? Why? What did you want to see me for?"
        di "Did you… need to tell me something?"
        scene ch7sc04_293 with dissolve
        mc "Yes… this."
        #play music mmm_elven_forest fadein 1.0
        stop music fadeout 1.0
        scene ch7sc04_295 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mc "I can’t stay away from you any longer…"
        di "Then… don’t."
        di "I don’t want you to stay away from me either…"
        scene ch7sc04_296 with dissolve
        "Your lips graces Diana’s and her delicate wet lips intimately brushes against yours as well."
        di "*Whispers softly* {size=-10}{b}If you kiss me now… there’s no going back…{/b}{/size}"
        scene ch7sc04_297 with dissolve
        di "Mmfhh… mnnh-nhh…"
        "Her warning does little to deter you, in fact it only makes you kiss her even more passionately."
        scene ch7sc04_298 with dissolve
        "Diana traces her wet tongue across your bottom lip, gently teasing you."
        di "I know I-... retracted my invitation earlier… I’m glad you chose to ignore it, mmh…"
        scene ch7sc04_297 with dissolve
        mc "Mmmh… I want you… Diana."
        di "Nnh-mmh… I want you [mc]... share my bed with me tonight?"
        scene ch7sc04_299 with dissolve
        di "*Squeals while licking* Aiiyh-mmh! Mmhh…"
        di "[mc]-... mmh… make love to me."
        scene ch7sc04_300 with dissolve
        "With Diana wrapped tightly around you and her tongue passionately caressing yours, you carry her towards her bed."
        mct "Mmh… damn she tastes good… I can’t wait to taste the rest of her."
        scene ch7sc04_301 with dissolve
        "The two of you continue to let your tongues do the talking as you inch your way closer to the bed."
        "With Diana’s large and supple breasts resting on top of your chest, and her legs tightly wrapped around your waist."
        scene ch7sc04_302 with dissolve
        "Diana whimpers between licking your tongue and sucking your lips as you press her against the bedpost."
        di "Mmmh-Mmh! What about… the exotic wine I offered? Mmgh-Mmghhhh…"
        scene ch7sc04_303 with dissolve
        "You put her down and pull her close, your tongues immediately reconnect as if they were magnetic."
        mc "*Caresses tongue* Mmgh… we’ll save it until after… mmh… there’s something else I crave at the moment."
        scene ch7sc04_304 with dissolve
        di "Mmh! Whatever it is- *Kisses* you’re craving… you’ll have it tonight… mmgh!"
        mct "I love how she caresses the back of my neck while pressing her plump ass against me… mmh."
        di "Nnnh… I love how you’re touching me… mmh… please… expose them."
        scene ch7sc04_305 with dissolve
        di "*Licks intimately* Please… show my girls how much you desire them… mmh…"
        mc "You’re about to know what it feels like to be desired from tip to top."
        scene ch7sc04_306 with dissolve
        "You pull open her bra, forcing her breasts to spill out and revealing her aroused nipples."
        di "*Shares saliva* Nnh! Mmh! Oh [mc]... mmh… touch them… touch me."
        scene ch7sc04_307 with dissolve
        "Diana whimpers as your warm hand makes contact with her naked breast."
        scene di_lewd1 with dissolve
        $ renpy.pause()
        di "*Moans while licking* Ohh… mmh… what a strange feeling- Aahh… k-keep touching me…"
        mc "Your breasts are incredible… nngh… I’ve been wanting to get my hands on them for a while now…"
        di "Me… mmh… me too… every time we’ve embraced… I’ve felt them squish against you… it’s all led us here… tonight."
        di "[mc]... you’re making them tingle with your touch… mmgh… your tongue does it as well… with every lick- Nngh…"
        mc "You’re reacting to the magic coursing through me, since you’re magically adept yourself, it feels even more intense."
        scene ch7sc04_307 with dissolve
        di "Please… mmgh… lick them? Nnnh-mhh… I want you to… taste my breasts."
        scene ch7sc04_308 with dissolve
        "You grab her by the hips and pull her to the bed."
        di "This feels… so intimate."
        mc "What you’re about to feel will bring a whole new meaning to the word intimate for you."
        di "Please… suck my breast?"
        scene ch7sc04_309 with dissolve
        di "*Moans* Aahh! It-... it tingles! Mmgh! OH!! Ohhh…"
        scene di_lewd2 with dissolve
        $ renpy.pause()
        di "[mc]- Mmh… j-just like that… caress my nipple with your tongue… mmmh…"
        di "I-... ahh… I can’t believe you’re sucking my breast right now… mmgh… please tell me this isn’t a dream?"
        "You assure her by nibbling her sensitive nipple gently."
        di "*Moans* Aahh! Oh! It’s not a dream- Mmh! Definitely not!"
        mc "It’s a shame you’ve already bathed… Mmh… would’ve loved to lick your sweat off them."
        di "You… would’ve liked that? Aahh… I wish I knew… mmh… they were drenched… it would’ve taken you a while to clean them up."
        mc "Exactly… mmh… not to mention your sweat during our sparring was filled with pheromones… your scent was enticing."
        di "I-... mmh… I have something to confess… I saw you enjoying the view when I aired them after the sparring."
        mc "That’s not much of a secret… *Sucks intimately* I couldn’t keep my eyes focused on anything else."
        di "Aahh… I know… that's not my confession… my confession is… I did that on purpose… I… wanted you to look."
        scene ch7sc04_308 with dissolve
        #play music mmm_elven_forest fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        di "*Moans* W-Why did you stop? I… I really enjoyed you sucking them."
        mc "Lay down on the bed… I want to taste all of you."
        di "A-All of me? Okay… Okay. Should we… undress?"
        mct "She’s cute when she’s all nervous like this, usually she’s so headstrong and confident, but tonight… she’s vulnerable."
        mc "Yes, but keep your panties on, I want to remove them myself in a bit."
        scene ch7sc04_310 with dissolve
        di "Will you not take off your pants? I-... I felt how hard you were when I sat on you…"
        di "*Whispers softly* {size=-10}{b}I… I really want to see you… all of you.{/b}{/size}"
        mc "*Chuckles* Patience… this is your first time, and right now… it’s all about you."
        di "*Nods* O-Okay… [mc], I trust you."
        scene ch7sc04_311 with dissolve
        mc "Don’t worry… you’re in good hands tonight."
        di "Mmh… [mc]... can we kiss once more before you… continue?"
        scene ch7sc04_312 with dissolve
        mc "Come here gorgeous."
        mc "*Whispers* {size=-10}{b}You can always have one more kiss… always.{/b}{/size}"
        di "*Whispers softly* {size=-10}{b}If that’s the case… I’d like two.{/b}{/size}"
        scene ch7sc04_313 with dissolve
        di "Mmgh-mmhh… mffhh…"
        "Diana moans softly as your arm presses against her breast while your lips merge in a very intimate and soft kiss."
        scene ch7sc04_314 with dissolve
        di "Nngh… your lips… your touch… your presence… mmgh… you somehow turn my nervousness into excitement."
        scene ch7sc04_313 with dissolve
        mc "It’s because your body feels it’s safe- mmgh… this is why your body relaxes in my embrace."
        scene ch7sc04_314 with dissolve
        di "Mmgh-mh… I really enjoy your embrace… *Sucks gently* It’s the purest emotion I’ve ever… felt."
        scene ch7sc04_312 with dissolve
        mc "Mmh… you’re ready for me to continue, aren’t you? My little admiral."
        di "*Panting softly* I… I’d like that."
        scene ch7sc04_315 with dissolve
        "As you move a little ways down to her collarbone, you plant your lips gently, tasting her smooth velvet skin while she moans."
        di "Ohh… by the seas… d-don’t stop…"
        mct "All this foreplay and teasing… her body is already trembling with anticipation… mmh…"
        scene ch7sc04_316 with dissolve
        di "*Moans softly* Ohh [mc]... caressing my nipple again? Aahh…"
        di "You’re reading my body like it’s… mmh… like it’s your favorite book."
        scene ch7sc04_317 with dissolve
        "Diana’s moans fill her cabin as you gently suck her flavorful nipple."
        #play music mmm_elven_forest fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        scene di_lewd3 with dissolve
        $ renpy.pause()
        "Meanwhile your hand runs down onto hers which was resting between her legs…"
        "You push down slightly on her hand so that the two of you begin rubbing her together on the outside of her soaked panties."
        di "*Moans* Nnhh! I-... I can’t believe you’re sucking my nipple again… while you… ahhh! While you touch me down there…"
        di "It’s like… mmh… you know exactly what I need… what I desire… better than myself."
        mct "Mmmh… *Sucks intimately* Her breasts are incredible… her skin has a perfectly smooth texture."
        mct "Not to mention how flavorful and bathed in pheromones they are… mmh… I can’t get enough."
        with vpunch
        di "{b}*Moans* Aiih-AHhh! [mc]! I- Ahhh!! I’m going to- AHH!{/b}"
        with vpunch
        scene ch7sc04_318 with dissolve
        with vpunch
        di "{b}*Squeals loudly* Aiiiyh!! {size=+5}SEAS!! [mc]! AHH!{/b}{/size}"
        with vpunch
        "Diana’s entire body spasms as she begins to orgasm to the pleasure of your sucking of her nipple and intimate rubbing of her pussy."
        "She tightens her legs around your arm, keeping your hand locked in place pressing against her wet panties and she bites her hand in pleasure."
        with vpunch
        di "Mmmfh! MMh! {b}AHH!!{/b}"
        mct "Five hells… she just had that big of an orgasm just from rubbing and sucking of her nipple? She’s going to explode when I get down there."
        scene ch7sc04_319 with dissolve
        di "Seas! H-How did you do that?! How did you make me orgasm like that??"
        mc "*Chuckles* Since we're both Demi-gods, our bodies feel everything we do together more intensely."
        di "[mc]... please… I need you… down there… between my thighs."
        di "What you just did to my nipple… I-... mmh… I really want you to do that… down there."
        mc "Say it."
        scene ch7sc04_320 with dissolve
        di "You’re so mean…"
        di "[mc]... please… make out with my pussy?"
        scene ch7sc04_321 with dissolve
        mc "Now that’s a request I’ll never deny from you… brace yourself, you’re going to come even more intensely this time."
        "Diana giggles softly as she opens her legs, she is clearly enticed by what you just said."
        scene ch7sc04_322 with dissolve
        with vpunch
        "You grab her legs and shift her onto the pillows, then you get into position and spread her legs while your taste her inner thigh."
        di "{b}*Squeals* AahH!{/b}"
        di "*Moans* Nnhh… your lips on my skin feels so… so… right. Mmmh!"
        scene ch7sc04_323 with dissolve
        mc "Mmh… the amount of pheromones that’s coming from your soaked panties… I’m not going to be able to hold back."
        di "Aahhh… I’m-... I’m ready… I want you to see me… and taste me."
        scene ch7sc04_324 with dissolve
        "You begin to pull down her panties, taking your time, enjoying the view of the fabric unveiling her most intimate self."
        mc "I’ve been thinking about you all day…"
        di "[mc]... as have I… you find your way into my mind… even at times you have no business being there… mmh."
        scene ch7sc04_325 with dissolve
        mc "Damn… I love how wet you are for me."
        di "*Nervous* Do you… like it? My pussy… appeals to you?"
        scene ch7sc04_326 with dissolve
        mc "You’re kidding? It’s gorgeous… you’re beautiful Diana."
        di "*Gasps softly* Oh my… oh [mc]... g-gently… I’m really sensitive- Mmmh…"
        scene ch7sc04_327 with dissolve
        di "*Moans* Aahh! I feel you! I feel your tongue- Mmh!"
        scene di_lewd4 with dissolve
        $ renpy.pause()
        mc "Mmmh… mffh… fuck you’re just as tasty as your scent suggested… mmh…"
        di "*Moans softly* [mc]- Aahh… I can’t believe you’re making out with my pussy… ahh… in my bed… mmh!"
        with vpunch
        "You rub your tongue from the very buttom of her vagina and all the way up between her wet lips and onto her clitoris."
        "You keep a constant pressure, listening to her moans like a sweet melody of pleasure."
        with vpunch
        di "{b}*Moans* AhH-MhH! [mc]!{/b} That feels… oh-OH k-keep doing that! Don’t… don’t stop! {b}AH!!{/b}"
        with vpunch
        di "{b}*Squeals in pleasure* AHh-aiiyh! I’m coming! {size=+5}AHH!!{/size}{/b}"
        scene ch7sc04_328 with dissolve
        with vpunch
        mc "Mmmfh! Fffh!"
        "The sensation of your tongue caressing her pussy and your lips pressing against hers sends her fully over the edge, squirting intensely."
        scene ch7sc04_329 with dissolve
        with vpunch
        "You grab her juicy thighs and swiftly adjust her so that you can drink all of her juices as her orgasm rages on."
        with vpunch
        di "{b}*Squeals and moans* Aiiyh! [mc]!! Ahh! I-I can’t stop coming!! AiiiyhHH!{/b}"
        scene ch7sc04_330 with dissolve
        with vpunch
        di "{b}*Moans* Seas!!{/b} I’ve never felt anything like thiiiis-aiiyhh!! {b}Y-Your’re melting my mind!! AhH!{/b}"
        "Hearing how much pleasure she’s having from being eaten by you, you continue to slurp her warm and tasty juices for a while longer."
        scene ch7sc04_331 with dissolve
        mc "*Licks lips* Damn Diana… that was fucking delicious… you’re delicious."
        di "*Panting* Let me taste!"
        scene ch7sc04_332 with dissolve
        with vpunch
        "She eagerly leans up and grabs hold of you so that she can taste her own juices on your lips."
        di "Mmh! Mmgh… Nnghh! So good… Mmgh!! I can see why you were licking me so intensely… mmghh!"
        "She continues to caress your tongue with hers for a few minutes, just enjoying being wrapped naked around each other."
        di "Mmh… take off your pants… I want to taste you as well. I-... I want to suck your cock."
        scene ch7sc04_333 with Dissolve(2.5)
        $ renpy.pause(0.5)
        "As soon as your pants are off and she sees how hard you are, she doesn’t hesitate to grab your cock and begins to make out with it."
        scene di_lewd5 with dissolve
        $ renpy.pause()
        mc "*Moans* Ffhh… that feels incredible…"
        mc "You know just how to tighten your mouth enough while still leaving room to maneuver your naughty tongue."
        di "*Sucks gently and licks* Nnngh…. mmmhhh… soohh… gooodhh… mmgh…"
        di "I should’ve sucked your cock straight after our sparring today… mmgh… I was so horny…"
        di "Every time we wrestled… I wanted to get naked... mffh... I felt you pressing against me... nnffhh... I liked it."
        with vpunch
        mc "Fffuck… keep sucking like that… you’re about to get a mouthful- aahhH…"
        with vpunch
        "Feeling your cock throb with pleasure, she sucks even more intimately."
        "Making sure to swirl her tongue around your tip each time she sucks, covering you in her warm saliva."
        with vpunch
        mc "Fuck Diana! I’m going to cum- {b}AAhhH!{/b}"
        with vpunch
        di "{b}*Sucks harder*{/b} I’m not stoppinghh! Mmgh!! Fill my throat with your warm cum! Mmh!"
        scene ch7sc04_334 with dissolve
        with vpunch
        "You grab her hair tightly and hold her head in place while she continues to suck passionately-"
        "Allowing you to unleash load after load down her throat."
        scene ch7sc04_335 with dissolve
        with vpunch
        mc "{b}*Moans*{/b} Ahh! Fuck! Fuck that little tongue of yours is out of this world- {b}Ffhh!!{/b}"
        with vpunch
        di "{b}*Choking and swallowing* Nnfhh! Ghhffh!! Mmgh-hhgghh!!{/b}"
        mc "That’s it! Mmgh! Take all of it like a good little lord admiral… mmgh!"
        scene ch7sc04_336 with dissolve
        with vpunch
        di "{b}*Coughs and gasps for air* Hnngh! Aaahh! MmH!{/b}"
        mc "Fuck Diana… that was incredible… especially for your first time having a cock in your mouth."
        scene ch7sc04_337 with dissolve
        di "[mc]... I’m sorry… in the end I couldn’t handle the full load."
        di "You’re… disappointed in me, aren’t you?"
        scene ch7sc04_338 with dissolve
        mc "Say that again and I’m kicking you out of your own bed."
        "Diana whimpers softly as you wipe away her tears from choking on your cock."
        scene ch7sc04_339 with dissolve
        mc "There we go, beautiful as ever."
        di "*Giggles softly* …"
        scene ch7sc04_340 with dissolve
        di "Thank you… I really tried my best."
        di "Your cock is rather big you know? And that amount of cum… I had no idea what to expect or how to handle it."
        scene ch7sc04_339 with dissolve
        mc "Don’t worry… you realise that making me cum that hard is a telltale sign that you did everything to perfection?"
        scene ch7sc04_340 with dissolve
        di "Oh! I guess I should have taken that as a sign… *Giggles*"
        di "Still, I’d like to practice with you until I can handle you with ease."
        scene ch7sc04_339 with dissolve
        mc "*Chuckles* We can practice as much as you want next time you’re in Luxenford, but for now…"
        mc "I believe my Lord Admiral begged me to make love to her?"
        scene ch7sc04_340 with dissolve
        di "She did… I want you to be my first… *Quietly* {size=-10}{b}and my only.{/b}{/size}"
        scene ch7sc04_341 with dissolve
        "Diana moans softly as you shift the two of you into position and she feels the tip of your cock resting at her entrance."
        di "Aahh… [mc]... I’m ready… I want you."
        scene ch7sc04_342 with dissolve
        di "*Whimpers* Oh! Ohh! Mmh… I feel you [mc]... I feel you inside me."
        mc "Mmgh… soaking wet and perfectly tight… mmh… you’re amazing."
        di "*Whimpers* G-Gently please… mmgh… I want to feel everything with you."
        scene di_lewd6 with dissolve
        $ renpy.pause()
        di "Aahh… yes- Ahh… oh this feels… Mmh… so intimate…"
        mc "Yeah… mmh… slow and deep like this makes both of us feel- Mmgh… every little pleasurable movement."
        di "I love it- Aahh… I know how strong you are… mmgh… and yet you’re able to be this incredibly gentle with me? Mmhh…"
        scene ch7sc04_342 with dissolve
        di "I… I want more… mmgh… I’m ready."
        scene ch7sc04_343 with dissolve
        "You push even further inside the juicy warmth of her tight pussy, and Diana wraps both her legs and arms around you in pleasure."
        scene di_lewd7 with dissolve
        $ renpy.pause()
        di "*Whimpers* O-Owh! Mmgh! Ffffhh you’re so deep! Ah-AhH!"
        with vpunch
        "Your increased thrusting fully penetrates the depths of Diana’s tight little pussy-"
        "-While her juicy ass is elevated from the bed, giving you the perfect angle."
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        di "Aiiyh-Ah! [mc]! I-I can’t hold it!! AhH!! {b}I’m coming!!{/b}"
        scene ch7sc04_343 with dissolve
        di "*Moans intimately* Aaahh! We’re one! Mmghh… we’re finally one… making love…"
        di "*Giggles happily* I came while you made love to me."
        mc "*Whispers* {size=-10}{b}Fuck Diana… you feel incredible when I’m this deep inside of you… mmh.{/b}{/size}"
        di "*Giggles* You didn’t cum… you’ll have to keep making love to me until you do-"
        scene ch7sc04_344 with dissolve
        with vpunch
        di "{b}*Gasps* Aiiyh! [mc]!!{/b} L-Like this?"
        mc "Think you can handle being taken like this?"
        di "*Moans softly* Nngh… I love how you’re stretching me… d-do it... take me [mc]."
        scene di_lewd8 with dissolve
        $ renpy.pause()
        di "{b}*Moans*{/b} Oh fuuuck! Mmh!! Oh!! {b}You’re going even deeper! AiiyhH!{/b}"
        with vpunch
        di "{b}*Moans*{/b} I love this! Mmgh! {b}Take me [mc]!{/b}"
        di "Make me your woman- Ahh! Cum inside me!"
        di "I love seeing you enter me… mmgh!"
        di "I love seeing your hard cock become one with my wet pussy… Ohhh!"
        scene di_lewd9 with dissolve
        $ renpy.pause()
        with vpunch
        mc "Fuck Diana! Mm… I can’t hold back much longer with how tight and juicy you are…"
        with vpunch
        di "D-Don’t hold back! I want you to fill my pussy just like you did my mouth!"
        di "{b}Aiiyh! Yes!!{/b} I feel you throbbing!"
        scene ch7sc04_345 with dissolve
        with vpunch
        "As you’re about to unleash inside of her, Diana shifts the two of you around in a swift motion."
        di "{b}*Moans* AhH!{/b} If I’m going to be your woman… I’m going to be the one to claim your cum tonight! Mmhghh…"
        mct "*Chuckles* Fuck… she doesn't just want me to cum inside of her, she wants to be in control of my orgasm… mmh."
        di "[mc]... I’m going to make you feel really good now… and I won’t stop until I feel your warm cum."
        scene di_lewd10 with dissolve
        $ renpy.pause()
        "Diana begins to slowly and carefully press herself back down onto your cock, fully submerging you in her pussy."
        di "*Moans softly* Ohh… mmh… this feels so intimate… you like it when I make love to you? Mmmhh…"
        mc "Fuck… yeah… this is incredible… you know exactly how to move your hips- Aahh…"
        mc "Not to mention the feeling of your large and soft breasts caressing my chest as you ride me… mmh…"
        with vpunch
        di "[mc]... they’re yours… I’m yours… mmh… please claim me by filling me with your cum… mmh…"
        with vpunch
        "Upon hearing Diana’s soft moans begging to be made yours, you can’t withhold it any longer, and you begin filling her."
        with vpunch
        di "{b}*Gasps* AahH!{/b} I-I feel it! Mmgh! I feel myself becoming yours! M-More!"
        scene ch7sc04_345 with dissolve
        with vpunch
        mc "Fuck! Mmgh! Fuck you’re tight!!"
        scene ch7sc04_346 with dissolve
        with vpunch
        di "*Giggling* Nngh! Oh this feels so much different than I thought it would… I love it."
        mc "Does it tingle? Mmmh… fuck, your pussy is something else… you made me cum even though you went slow and intimate."
        #play music mmm_elven_forest fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        scene ch7sc04_348 with dissolve
        di "*Whispers softly* {size=-10}{b}Mmh-hm… it does tingle… I can’t tell if it's your cock or cum… but it feels really good.{/b}{/size}"
        di "[mc]... do you realise how happy you’ve made me tonight?"
        scene ch7sc04_349 with dissolve
        mc "Mmh… I do, your heartbeat gives it away… I feel the same."
        di "*Giggling happily* Mmhh..."
        scene ch7sc04_348 with dissolve
        di "I love feeling your heart beating like this... through your chest and into my breasts."
        di "I never thought… I would have this… I never thought I could be happy with a man."
        di "But then you came into my life… little by little chipping away at my walls, proving to me that maybe… maybe I am allowed to feel happy."
        scene ch7sc04_349 with dissolve
        mc "I used to feel the same way… that being happy would make me weak…"
        mc "But I’ve found strength in feeling happy, or at least allowing myself to be happy when I’m with my loved ones."
        mc "When you care about something and it makes you happy, you’ll do anything to protect it."
        mc "You’ll elevate yourself beyond what you thought possible for the sake of the people you love."
        scene ch7sc04_348 with dissolve
        di "Mmh… I agree… I feel like that at this moment… *Whispers* {size=-10}{b}I’ll do anything for you.{/b}{/size}"
        di "Kiss me… please."
        scene ch7sc04_350 with dissolve
        "You embrace Diana’s wet lips while she rests on top of you with your cock still plunged in the depths of her pussy."
        di "Mmgh-nnh… I-... I love you [mc]."
        scene ch7sc04_351 with dissolve
        $ renpy.pause(0.5)
        with vpunch
        di "*Gasps* I-... I-..."
        "Realising what she just confessed to you, she swiftly puts her palm to your mouth and leans up."
        di "I’m sorry! I shouldn’t have said that… I-... I’m going to go clean up!"
        scene ch7sc04_352 with dissolve
        di "A-And I’ll get that bottle of wine… mhm, we need that… I need that."
        di "I’ll be right back… make yourself comfortable."
        mct "*Chuckles* So she loves me huh?"
        mct "I guess I already knew that… a woman doesn’t make love like she just did without having feelings."
        scene ch7sc04_347 with dissolve
        di "Seas… we should’ve prepared better… your cum is leaking out of me and I don’t have any washcloths in here."
        mc "*Chuckles* I’d say I’m sorry… but I’m really not. You earned it and you look incredible like this."
        di "*Snickers* It does feel nice, but I’d prefer to wipe it off before we stain my sheets too heavily-"
        scene ch7sc04_353 with dissolve
        with vpunch
        di "{b}*Squeals*{/b} UuaaiiihHh!!"
        scene ch7sc04_354 with dissolve
        with vpunch
        "Out of pure instinct you react, instantly rushing to catch her in her fall."
        di "*Gasps* Y-You… caught me?"
        scene ch7sc04_355 with dissolve
        di "*Soft spoken* Thank you…"
        scene ch7sc04_356 with dissolve
        mc "You should be careful, you just lost your virginity and we’ve been making love for hours."
        mc "Not to mention our sparring earlier, no wonder you're a little wobbly. *Chuckles*"
        scene ch7sc04_355 with dissolve
        di "*Giggles* You’re right…"
        di "I was told it would hurt, but I barely felt any discomfort when we made love?"
        scene ch7sc04_356 with dissolve
        mc "Probably due to how aroused we were…"
        mc "Not to mention our sensitivity to each other’s magic, made it feel more pleasurable."
        scene ch7sc04_355 with dissolve
        di "It felt incredible… just like now, when our skin is in contact with each other… everything is heightened."
        di "I guess I lost balance due to my body finally reacting to the exhaustion and discomfort of going through this."
        scene ch7sc04_357 with dissolve
        mc "Let’s get your little butt back in bed."
        di "H-Hey! It’s not little! Take that back… you may have rescued me from a fall, but I’ll still kick your ass!"
        mc "*Chuckles* You and your cute little butt will rest up in bed."
        scene ch7sc04_358 with dissolve
        di "You’re one to talk about cute butts!"
        di "Yours is totally cute as well! *Giggles*"
        scene ch7sc04_359 with dissolve
        di "[mc], you’re not leaving… right?"
        di "I-... I’d like it if you would stay with me for the night."
        scene ch7sc04_360 with dissolve
        mc "Don’t worry… I’m staying the night."
        mc "I’ll just go grab you that washcloth and fetch that wine you spoke of."
        scene ch7sc04_359 with dissolve
        di "Oh! That’s so sweet… you can probably find both the washcloth and the wine below deck in storage."
        di "The wine should be on the top left shelf in the cooling area."
        scene ch7sc04_360 with dissolve
        mc "Great, you just remain here and rest while you look beautiful, I’ll be right back."
        di "*Giggles happily* Mhh-hmm!"
        scene black with Dissolve(1.5)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        scene ch7sc04_361 with Dissolve(1.5)
        play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(1)
        mct "Mmh… the sound of the water and the fresh air when you’re near the ocean…"
        mct "It feels perfect after making love to a woman."
        scene ch7sc04_362 with dissolve
        mct "She’s leaving tomorrow, I’ll make sure tonight will be a memory she’ll cherish while she’s away."
        scene ch7sc04_363 with dissolve
        mct "Huh?!"
        scene ch7sc04_364 with dissolve
        with vpunch
        "Even with your instincts alerting you to incoming danger, you’re struck before you can react with enough force to knock you out."
        scene ch7sc04_365 with dissolve
        mc "*Groans* Hnngh… Ges-... Geskir…"
        scene ch7sc04_366 with dissolve
        mc "Hngghh… Bastard…"
        scene black with Dissolve(1.5)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause()



    else:
        scene black with Dissolve(1.5)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause()






    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    #"{color=#00ff00}End of v0.6.4 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    #"{color=#00ff00}End of v0.6.4 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    scene black with dissolve
    $ renpy.pause(0.1)
    stop music fadeout 1.0
    #jump endofversion
    jump ch7sc6

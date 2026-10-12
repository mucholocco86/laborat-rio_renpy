label ch5sc1:

    window hide dissolve
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (2.0)
    $ renpy.pause(1)
    scene ch5sc01_000 with Dissolve(2.5)
    $ renpy.pause()
    scene ch5sc01_001 with Dissolve (2.0)
    $ renpy.pause(1)
    am "Are these the ones Mother likes?"
    scene ch5sc01_002 with dissolve
    md2 "I think so!"
    am "You aren’t sure?"
    am "We’ve walked around the market for an hour!"
    scene ch5sc01_003 with dissolve
    md2 "Uhmm... I think these are the ones!"
    md2 "They have to be!"
    am "Ugh, let’s just get them."
    am "We have to get back before they notice we’re gone."
    scene ch5sc01_004 with dissolve
    md2 "O-Okay! I’ll just pay for them."
    am "Don’t take too long."
    am "You know how my father gets when I leave the castle."
    scene ch5sc01_005 with dissolve
    md2 "I’ll be quick, Your Highness!"
    scene ch5sc01_006 with dissolve
    am "Mh-Hm... I’ll see you back at the castle."
    am "Oh, and do try to pick the best ones."
    scene ch5sc01_005 with dissolve
    md2 "Y-Yes, Your Highness-"
    scene ch5sc01_006 with dissolve
    am "What did I tell you about calling me that in public?"
    scene ch5sc01_007 with dissolve
    md2 "S-Sorry, Your High-... Amelia."
    am "Just hurry up."
    am "We have to be ready for Mother’s event tonight."
    scene black with Dissolve(1.5)
    scene ch5sc01_008 with Dissolve(1.5)
    $ renpy.pause(1.5)
    scene ch5sc01_009 with dissolve
    $ renpy.pause(1)
    scene ch5sc01_008 with dissolve
    amt "How many times do I have to remind her not to call me 'Highness' in public?"
    scene ch5sc01_009 with dissolve
    mct "The city is crowded today."
    mct "*Sigh* I hate crowds..."
    scene ch5sc01_008 with dissolve
    amt "She knows that it’s risky sneaking out of the castle without an escort..."
    scene ch5sc01_009 with dissolve
    mct "I hope Alice and Luna have made some progress on breaking the Hex."
    scene ch5sc01_010 with dissolve
    amt "It's nice out here. I wish my parents weren't so hellbent on keeping me inside the castle."
    mct "Maybe I could help them break the hex?"
    scene ch5sc01_011 with dissolve
    amt "*Sigh* I know they're just trying to keep me safe... but being confined to the castle isn't living."
    mct "I don't know anything about breaking hexes, but maybe my abilities will surprise me again?"
    scene black with dissolve
    with vpunch
    am "Owwh!"
    mc "*Grunts* Hmh?"
    scene ch5sc01_012 with dissolve
    am "Urrh... Watch where you’re going, will you?!"
    mc "Me? You’re the one who walked into me..."
    scene ch5sc01_013 with dissolve
    am "How dare you talk back to me?! Do you even know who I am?"
    mct "A bitch that’s for sure..."
    am "I could’ve gotten hurt!"
    am "Scraped my knee or hurt my wrist... your head would've been on a spike you know?"
    scene ch5sc01_014 with dissolve
    mc "Did you... get hurt?"
    am "..."
    scene ch5sc01_015 with dissolve
    am "No."
    am "I-..."
    am "I suppose I didn't."
    scene ch5sc01_016 with dissolve
    mc "Here..."
    mc "let me help you up."
    am "..."
    scene ch5sc01_017 with dissolve
    mct "Why does she seem so surprised that I’m offering her my hand?"
    "She carefully places her fingers in your hand and allows you to pull her up."
    scene ch5sc01_018 with dissolve
    am "........"
    amt "W-Why did he do that?! Why did he offer me his hand? Doesn't he know??"
    scene ch5sc01_019 with dissolve
    am "You shouldn’t have done that."
    am "Peasants aren’t allowed to touch nobles, you'd lose a hand if anyone saw you..."
    scene ch5sc01_020 with dissolve
    mc "It’ll be our secret."
    am "*Scoffs lightly* ..."
    amt "Why is he just staring at me? Doesn't he know who I am?"
    scene ch5sc01_021 with dissolve
    mct "Her ring... could it be?"
    mct "I can definitely sense magic flowing within it."
    scene ch5sc01_019 with dissolve
    am "If you’re done leering at me..."
    am "I need to get home."

    if charisma >= 6:
        scene ch5sc01_020 with dissolve
        mc "*Scoffs* Is looking upon a beautiful woman considered leering now?"
        amt "B-Beautiful?"
        scene ch5sc01_019 with dissolve
        am "W-What are you saying?"
        scene ch5sc01_018 with dissolve
        mc "I'm saying that I find you beautiful."
        am "..."
        "Your compliment is but one of many this woman receives on the daily... Yet yours stood out to her"
        "You had enough charisma to make an impression, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
        scene ch5sc01_020 with dissolve
        $ charisma += 1
        mc "If that somehow offended you-"
        scene ch5sc01_019 with dissolve
        am "You didn't offend me! Hmph!"
        am "If that's all, I bid you farewell."
        scene ch5sc01_020 with dissolve
        mc "Sure? Farewell to you too."
        mc "It was nice meeting you?"
        scene ch5sc01_019 with dissolve
        $ amelia_trust += 1
        am "I suppose it wasn't... terrible."
        "Amelia's trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

    else:
        scene ch5sc01_018 with dissolve
        "Your {color=#87e1fa}Charisma{/color} was too low to leave an impression."
        mc "I wasn’t-"

    scene ch5sc01_022 with dissolve
    am "Goodbye, peasant boy."
    am "Do try not to knock over any more noblewomen, next one might not be as pleasant as me."
    scene ch5sc01_023 with dissolve
    mct "Peasant boy? And she considers herself... pleasant? Sheesh..."
    mct "She could’ve at least said thanks."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc01_024 with Dissolve(1.5)
    al "Two logs should be enough to heat the room for a while."
    scene ch5sc01_025 with dissolve
    mc "There she is."
    mc "I was starting to wonder if I was in the right place."

    if alice_path == True:
        scene ch5sc01_026 with dissolve
        with vpunch
        al "Aiiiyh!"
        mc "*Whispers* {size=-10}{b}What’s a lovely girl like you doing all alone in a place like this?{/b}{/size}"
        scene ch5sc01_027 with dissolve
        al "*Giggling* She was getting logs for the fire until she was so rudely interrupted!"
        mc "Rudely, huh? ... Maybe I should let you go then?"
        scene ch5sc01_028 with dissolve
        al "N-No! That would be inadvisable..."
        al "A proper gentleman should apologize to a lady when he causes her distress."
        mc "Distress? Hmm... And what kind of apology would the lady prefer?"
        scene ch5sc01_029 with dissolve
        al "*Mwah* This should suffice!"
        scene ch5sc01_030 with dissolve
        al "*Moans softly* Mmhh..."
        scene ch5sc01_029 with dissolve
        mct "I’ve missed her full lips... they’re perfect for kissing."
        scene ch5sc01_030 with dissolve
        al_t "*Licks* Nnhh... I hope he likes my tongue... Mmmmmm..."
        mct "She enjoys teasing me with her tongue. Licking just the tip of it until I enter her mouth."
        scene ch5sc01_029 with dissolve
        al_t "Heavens! I love how firmly he’s holding on to my waist..."
        scene ch5sc01_031 with dissolve
        "She instinctively begins rubbing herself back against you."
        al "*Moans* HHnnghh! MMmhh... [mc]...*Kiss*"
        al "*Moans* Y-You’re poking my-... my ass... Mmhh *Kiss*"
        scene ch5sc01_032 with dissolve
        mc "You’re the one rubbing into me..."
        al "*Moans* Nnnh... Can’t... Can’t help it. It feels so good..."
        al "*Soft moan* [mc]... keep... keep pressing against me *Kiss*"
        scene ch5sc01_031 with dissolve
        mct "She’s already gotten me rock hard... If she keeps this up..."
        scene ch5sc01_030 with dissolve
        mct "I’ll take her virginity right here..."
        "The sound of a door opening snaps the two of you out of your tantric kiss."
        with vpunch
        scene black with Dissolve(1.5)


    else:
        scene ch5sc01_033 with dissolve
        mc "Hey Alice."
        al "[mc]! Hi! You’re here!"
        mc "Yeah, I wanted to check to see how you and Luna are progressing with the hex."
        scene ch5sc01_034 with dissolve
        al "And here I thought you'd come to visit your childhood friend..."
        mc "Sweet Alice... you should know by now that your pouty face never works on me."
        scene ch5sc01_035 with dissolve
        al "*Puckers lips* Hnnngh..."
        al "............"
        mc "*Sigh* Okay, fine. The hex check-up is obviously just a cover."
        mc "I’m really here to visit my sweet and dear childhood friend whom I’ve missed so, so much!"
        scene ch5sc01_036 with dissolve
        al "I knew it! You really missed me?"
        scene ch5sc01_033 with dissolve
        mc "Sure did!"
        al "Awwwh! I missed you too! Lots!"
        scene black with Dissolve(1.5)


    $ renpy.pause(1)
    scene ch5sc01_037 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    lu "Alice! There you are. I thought you still had classes going on?"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    al "I had a short break so I thought I'd quickly get things setup for you."
    scene ch5sc01_038 with dissolve
    lu "Thank you, Alice. I appreciate it."
    lu "And I see you brought [mc] with you... perfect!"
    scene ch5sc01_039 with dissolve
    al "Perfect?"
    lu "Yup! Perfect! I need him."
    scene ch5sc01_040 with dissolve
    mc "What do you need me for?"
    lu "It's a secret! *Laughs lightly*"
    lu "You’ll see! Soon."
    scene ch5sc01_041 with dissolve
    al "Don’t worry, [mc]. You’re in good hands with her! She's really good with magic."
    al "I’ve gotta go. My class is about to resume and the professor is already on my ass..."
    scene ch5sc01_042 with dissolve
    al "Catch you later?"
    mc "Mh-Hm."
    if alice_path == True:
        al "*Whispering* {size=-10}{b}Keep those handsome lips ready...{/b}{/size}"
        al "*Whispering* {size=-10}{b}That was the type of kiss which... needs to be finished.{/b}{/size}"
        mc "*Whispering* {size=-10}{b}You're right, that kiss deserves a proper ending.{/b}{/size}"

    else:
        al "Take care!"


    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch5sc01_043 with Dissolve(1.5)
    lu "She is totally crushing on you."
    mc "I’m aware..."
    scene ch5sc01_044 with dissolve
    lu "So... why aren’t you doing something about it?"
    lu "All the boys at the academy are fawning over her."
    lu "And yet, you're the only guy she gives any thought? It only makes sense to claim her as yours, no?"
    scene ch5sc01_045 with dissolve
    mc "Me and Alice... it’s complicated."
    lu "She told me you’ve been friends since childhood?"
    lu "You're afraid you might ruin the friendship or?"
    scene ch5sc01_046 with dissolve
    mc "Yeah... it's definitely crossed my mind."
    lu "I’m sorry."
    lu "It’s none of my business... Mother always tells me I’m too nosy."
    mc "It’s okay. I can understand being curious..."
    scene ch5sc01_047 with dissolve
    mc "I used to be curious about everything when I was younger."
    lu "Really? I’d like to hear about that."
    lu "Let’s go sit by the window?"
    mc "Sure."
    scene ch5sc01_048 with dissolve
    lu "*Excitedly* Awesome! Fantastic! Magnificent! Splendid! Grand! There's so much I want to know!"
    mc "Great... what did I just get myself into?"
    lu "*Snickers* Nothing you can’t handle, I’m sure."
    scene ch5sc01_049 with dissolve
    "Luna observes you carefully as you sit down beside her."
    mct "She seems a little nervous."
    scene ch5sc01_050 with dissolve
    mc "Are you alright?"
    scene ch5sc01_051 with dissolve
    lu "Hmh? Oh, me? Yup! I’m good!"
    lu "Splendid actually!"
    scene ch5sc01_052 with dissolve
    lu "..."
    scene ch5sc01_051 with dissolve
    lu "It’s just..."
    lu "It's the first time I’ve been alone with a boy."
    scene ch5sc01_053 with dissolve
    lu "I mean- We’ve been alone before... When we first met."
    lu "You know- when I almost fireballed you?"
    lu "But that was totally different! It wasn’t intentional!"
    scene ch5sc01_054 with dissolve
    mc "And this is... intentional?"
    scene ch5sc01_053 with dissolve
    lu "Uh-huh!"
    lu "I mean... I chose to sit here with you."
    scene ch5sc01_054 with dissolve
    mc "*Chuckles* Does that mean you like me?"
    scene ch5sc01_055 with dissolve
    lu "L-Like you?"
    lu "{b}UH!{/b} Don’t be silly! I barely know you..."
    mc "You can still feel a connection with someone based upon initial impression."
    lu "True! I felt it too! Uh, I mean... *Sighs*"
    scene ch5sc01_053 with dissolve
    lu "I just- I just really like that you are trying to help free my mom."
    lu "That’s all! It’s pretty admirable."
    lu "And Alice vouches for you."
    lu "Which means you're great! Uh-huh!"
    scene ch5sc01_054 with dissolve
    mct "It’s not as admirable as she thinks... I just can’t allow Taron to have anything he wants."
    mct "Although... it could be handy to have a witch as an ally. And she has connections to the Mages Guild."
    mct "Alice really seems to trust her, and she’s always been a great judge of character. She was best friends with me, after all."
    mct "Not to mention, my gut feeling about Luna is that she is genuine to the core."
    mc "I’m happy to help, Luna."
    mc "Nobody should have to go through what Taron is doing to you and your mother."
    scene ch5sc01_053 with dissolve
    lu "Thank you. It- It means a lot."
    scene ch5sc01_056 with dissolve
    lu "There's something I wanted to ask you..."
    lu "Did you manage to break the curse on the sword?"
    scene ch5sc01_057 with dissolve
    mct "Right, Onyx... I wasn't sure if or when I should tell her."
    mct "Alice is a good judge of character and she trusts Luna."
    mct "If I want to make an ally out of her, I need to try trusting her..."
    scene ch5sc01_056 with dissolve
    lu "You okay?"
    lu "It's okay if you couldn't break the curse-"
    scene ch5sc01_054 with dissolve
    mc "I broke the curse."
    mc "But it wasn't a sword at all. It was a being from the ancient world, a symbiote."
    scene ch5sc01_055 with dissolve
    with vpunch
    lu "{b}WHAT?!{/b} A S-Symbiote?!"
    lu "Don't tell me you already bonded with it?"
    mc "I did."
    scene ch5sc01_051 with dissolve
    lu "Good grief... You just rushed into it like that?"
    lu "By all that's arcane, what compelled you to do such a thing?"
    mc "It may have been a little impulsive... but I couldn't risk Taron getting his hands on Onyx."
    scene ch5sc01_053 with dissolve
    lu "Onyx, huh? You do realize bonding with a symbiote is permanent, right?"
    scene ch5sc01_054 with dissolve
    mc "Onyx mentioned that, yes."
    mc "She basically gave me the full rundown about symbiosis before I accepted her."
    scene ch5sc01_056 with dissolve
    lu "You'll die, though... A symbiote feeds on their hosts energy! She'll consume your life force."
    lu "It may take a long time, but in the end their hosts always die."
    scene ch5sc01_057 with dissolve
    mc "I've got that covered..."
    scene ch5sc01_056 with dissolve
    lu "Okay? Color me intrigued."
    lu "I'm a little disappointed I didn't get a say in this..."
    scene ch5sc01_053 with dissolve
    lu "But knowing that this Onyx is out of Taron's reach helps make up for it."
    lu "That bastard doesn't deserve to get anything he wants."
    scene ch5sc01_054 with dissolve
    mc "Thank you for taking it so well."
    mc "I was half-expecting you to go off on me."
    scene ch5sc01_053 with dissolve
    lu "And what exactly would either of us get out of that?"
    lu "I want us to be allies, if that wasn't clear."
    scene ch5sc01_056 with dissolve
    lu "Maybe I'm desperate... Maybe it's Alice's high opinion of you?"
    lu "Or maybe I'm just naive..."
    scene ch5sc01_053 with dissolve
    lu "But I feel like I can trust you."
    lu "So no, I'm not mad."
    scene ch5sc01_056 with dissolve
    lu "Just promise me you'll use Onyx, or whatever other mean's you have, to help my mom."
    lu "She needs our help."
    scene ch5sc01_054 with dissolve
    mc "You can count on it."
    lu "..."
    scene ch5sc01_056 with dissolve
    lu "Good! Good, good... goody-good!"
    lu "Now, tell me something about yourself!"
    scene ch5sc01_054 with dissolve
    mc "Mhm... Well, I left home at the age of ten."
    scene ch5sc01_055 with dissolve
    with vpunch
    lu "{size=+5}{b}Ten?!{/b}{/size}"
    lu "By the sage’s balls! What were you thinking?!"
    lu "Did your parents... beat you? Is that why you ran away?"
    scene ch5sc01_056 with dissolve
    lu "I could fireball them for you, if you want?"
    scene ch5sc01_057 with dissolve
    mc "Settle down, Luna. I appreciate you being willing to fireball someone on my behalf."
    mc "But that won’t be necessary. And no, they didn’t beat me. Nor did I run away."
    scene ch5sc01_054 with dissolve
    mc "They were the best parents I could have wished for... My father was always pushing me to learn things."
    mc "And my mother showered me with warmth and love."
    mc "I left home because... *Sighs heavily*"
    scene ch5sc01_058 with dissolve
    "Luna noticed the despair in your tone and she moves closer, sliding one of her legs across yours."
    "You hesitate and swallow a lump in your throat as you try to explain."
    "Apparently it hasn’t gotten any easier to share your past with people..."
    scene ch5sc01_059 with dissolve
    lu "It’s okay, [mc]. You can tell me."
    scene ch5sc01_060 with dissolve
    lu "It’s just the two of us here."
    scene ch5sc01_059 with dissolve
    lu "I’m not going anywhere."
    scene ch5sc01_060 with dissolve
    mct "Her hand, it’s so... delicate and warm."
    scene ch5sc01_059 with dissolve
    mc "*Sigh* The day I left home... I spent the day playing with Alice."
    scene ch5sc01_060 with dissolve
    mc "We went exploring in the woods like we'd done many times before. Playing at being adventurers..."
    scene ch5sc01_059 with dissolve
    mc "We ended up falling asleep in the woods and when we woke up it was already dark."
    scene black with Dissolve(1)
    scene ch1sc8_07 with Dissolve(1)
    mc "When I finally got home... I realized I couldn’t smell Mother’s stew..."
    scene black with Dissolve(1)
    scene ch5sc01_060 with Dissolve(1)
    mc "And I didn’t hear Father complaining about setting the table... or chopping firewood."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mc "I'd never heard my home be so silent before."
    scene ch5sc01_060 with dissolve
    play music forestnight_3 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch1sc8_14 with Dissolve(2)
    mc "When I went inside... everything was a mess."
    scene ch1sc8_18 with dissolve
    mc "I started searching the house and-..."
    mc "As I entered our bedroom, that’s when I saw them..."
    scene ch1sc8_20_1 with dissolve
    mc "That was the instant when my entire life was vaporized."
    scene ch1sc8_20_2 with dissolve
    mc "*Memory* Mama..."
    scene ch1sc8_20_3 with dissolve
    mc "*Memory* Papa..."
    scene ch1sc8_20_6 with dissolve
    mc "No matter how loudly I screamed for them to wake up... they didn’t respond."
    scene ch1sc8_20_8 with dissolve
    mc "They were... dead. Murdered. Their bodies were covered in blood and bruises."
    scene ch1sc8_24 with dissolve
    mc "I couldn’t believe my own eyes... My parents... dead? Right in front of me?"
    scene ch1sc8_30 with dissolve
    mc "As I was screaming my lungs out, something happened..."
    scene ch1sc8_35 with dissolve
    mc "A seal between my mother and me broke."
    scene ch1sc8_40 with dissolve
    mc "And that’s when I discovered I wasn’t human."
    scene ch1sc8_45 with dissolve
    mc "I didn’t comprehend it at first. It would be years until I really understood what... I am."
    scene ch1sc8_52 with dissolve
    mc "And that’s when ‘He’ appeared..."
    scene ch5sc01_060 with dissolve
    lu "Who? Who appeared?"
    scene ch1sc8_60 with dissolve
    mc "The man who'd become my mentor."
    mc "Eliza’s father... Oren."
    scene ch1sc8_63 with dissolve
    mc "He told me that if I followed him... I'd be able to avenge my parents one day."
    mc "So, we left that night. I left behind everything familiar to me, everything and everyone I'd ever cared for."
    mc "I swore I'd make Taron pay. And that vow keeps me going against any odds. I push through so that I can keep my oath someday."
    scene black with Dissolve(1)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc01_060 with Dissolve(1)
    "*Fist tightens*"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    lu "Hey... come here."
    scene ch5sc01_061 with dissolve
    "Luna mounts you without hesitation and wraps her arms and legs around you."
    lu "Thank you... for sharing that with me."
    scene ch5sc01_062 with dissolve
    lu "I can tell that it took a lot for you to tell me..."
    lu "That those memories hurt you."
    lu "I promise I won’t betray your trust."
    lu "We’ll make him pay... together."
    lu "He'll regret messing with either of our parents."
    scene ch5sc01_063 with dissolve
    mct "Even if we don’t know each other that well... we're bound together by tragedies caused by Taron."
    mct "We're... friends, I actually trust her."
    mc "Luna... thank you."
    lu "No need to thank me... I can’t believe I threatened to fireball your parents earlier..."
    lu "That was so insensitive..."
    mc "You couldn’t have known."
    scene ch5sc01_062 with dissolve
    lu "*Squeezes tightly* Sorry..."
    mct "Damn... This is not a regular hug."
    mct "There’s a lot of emotion in it."
    scene ch5sc01_061 with dissolve
    lu "Thank you... Thank you so much for trying to help my mom."
    mc "Speaking of... you said you needed me for something?"
    scene black with Dissolve(1.5)
    scene ch5sc01_054 with Dissolve(1.5)
    "Luna reluctantly lets you out of her grasp and sits beside you again."
    scene ch5sc01_053 with dissolve
    lu "{b}OK!{/b}"
    lu "So what I need you for is a simple spell."
    scene ch5sc01_056 with dissolve
    lu "Alice and I have been trying to locate the mage who cast the hex on my mom."
    lu "Normally a simple locator spell would suffice, but it seems he’s been expecting that-"
    scene ch5sc01_053 with dissolve
    lu "He's managed to conceal his presence... most likely with an obscurro incantation."
    lu "I’ve tried channeling Alice because I wasn’t strong enough to break through on my own..."
    scene ch5sc01_057 with dissolve
    mc "You’ve been channeling Alice? How does that work?"
    scene ch5sc01_056 with dissolve
    lu "Basically I link our essences, and that allows me to draw on her magic too."
    scene ch5sc01_057 with dissolve
    mc "Magic? Alice doesn’t have any magic..."
    scene ch5sc01_056 with dissolve
    lu "Everyone does. Every living being has magic within them."
    lu "Humans, elves, dwarves, goblins, slimes, griffons, dragons, vampires, anything really."
    lu "It’s just that most people can't harness it or control it."
    scene ch5sc01_054 with dissolve
    mct "Hmm. I do recall Oren telling me something similar once."
    mct "It explains why I'm able to absorb the essences of all beings."
    mct "I just never really thought about it..."
    scene ch5sc01_053 with dissolve
    lu "My mother told me that only about one percent of the population are able to access their magic, wield it like a mage does."
    lu "So it’s not really that common."
    scene ch5sc01_054 with dissolve
    mc "I’m assuming that channeling Alice didn’t work?"
    mc "Otherwise you wouldn’t need me..."
    scene ch5sc01_056 with dissolve
    lu "Correct... Alice’s magic is too weak."
    lu "Even with her help, I still couldn’t trace the mage."
    scene ch5sc01_057 with dissolve
    mc "So... you want to channel me?"
    scene ch5sc01_056 with dissolve
    lu "Uh-Huh!"
    lu "It’s our best shot at breaking through his Obscurro incantation."
    scene ch5sc01_057 with dissolve
    mc "Okay, but as you know, my magic isn’t what you’re used to."
    mc "You might find it hard to control... assuming you don’t immediately pass out."
    scene ch5sc01_064 with dissolve
    lu "*Snickers* Challenge accepted! You do remember I’m the heir to the Mages Guild, right?"
    mc "*Chuckles* That may be so... but I haven’t seen you in action yet."
    scene ch5sc01_065 with dissolve
    mc "Being the child of a powerful sorceress doesn’t mean you are also good."
    scene ch5sc01_066 with dissolve
    lu "Not easily satisfied, are you?"
    lu "Hmh. Guess I’ll have to aim to impress then. Come."
    scene ch5sc01_067 with dissolve
    lu "Stand in the middle of the circle... and lose your shirt."
    scene ch5sc01_068 with dissolve
    mc "You could at least buy me dinner first."
    lu "*Scoffs lightly*"
    scene ch5sc01_067 with dissolve
    lu "Mh-Hm... Is that what you want?"
    lu "For me to go on a date with you?"
    ####Choice####
    menu:
        "Yes. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc01_068 with dissolve
            mc "A date with the beautiful and talented heir to the Mages Guild?"
            mc "I’d consider myself lucky."
            scene ch5sc01_067 with dissolve
            lu "Didn’t you just question my abilities a few moments ago?"
            scene ch5sc01_068 with dissolve
            mc "It feels like a lifetime ago."
            scene ch5sc01_069 with dissolve
            lu "*Giggling* Good to know that your faith in me has been restored..."
            lu "And that you think I’m beautiful."
            $ luna_trust += 2
            "Luna enjoyed your flirting, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            lu "Now take off your shirt, loverboy. I’ll be with you in a moment."
            scene black with Dissolve(1.5)
            "You remove your shirt and place yourself in the middle of the circle."

        "No. (Neutral)":
            scene ch5sc01_068 with dissolve
            mc "I don’t have the time to be going out on dates... Not until-"
            scene ch5sc01_067 with dissolve
            lu "Not until we defeat that bastard."
            scene ch5sc01_068 with dissolve
            mc "Yeah."
            scene ch5sc01_067 with dissolve
            lu "Okay."
            lu "But I’ll still need you to take your shirt off and stand in the circle."
            scene ch5sc01_068 with dissolve
            mc "Sure."
            scene black with Dissolve(1.5)
            "You remove your shirt and place yourself in the middle of the circle."

    scene ch5sc01_070 with Dissolve(1.5)
    mc "Is this how you want me?"
    lu "That... will suffice."
    "She eyes you up and down, clearly curious about your physique."
    scene ch5sc01_071 with dissolve
    lu "Try not to move. And if the pain becomes too much, I implore you to refrain from screaming."
    mc "I can handle it."
    mc "Wait... Didn’t you say you did this with Alice? If you caused her to suffer-"
    scene ch5sc01_072 with dissolve
    lu "*Snickers* Gotcha!"
    lu "You should see your face!"
    lu "From overly confident, to confused, to worried, then to protective in just a few moments..."
    scene ch5sc01_071 with dissolve
    mc "*Relieved sigh* So you didn’t hurt Alice?"
    scene ch5sc01_072 with dissolve
    lu "Of course I didn't!"
    lu "I wouldn’t hurt her, you silly goose! She’s my only-... best friend."
    scene ch5sc01_071 with dissolve
    mc "In the future... I’d appreciate it if you refrain from joking about hurting my friends."
    mc "I just told you about my parents... But my friends haven’t been unaffected either."
    scene ch5sc01_072 with dissolve
    lu "[mc]... I know-... I’m sorr-"
    scene ch5sc01_073 with dissolve
    mc "It’s fine. Let’s just get this over with."
    lu "..."
    scene ch5sc01_074 with dissolve
    lu "I’m sorry. It was distasteful to joke about that."
    scene ch5sc01_075 with dissolve
    lu "I do that sometimes... whenever I’m nervous or uncomfortable..."
    lu "I try to make light of a situation..."
    scene ch5sc01_076 with dissolve
    lu "..."
    "She stops a few feet from you, visibly ashamed of herself."
    mct "She looks so defeated... I almost feel bad for telling her off."
    mct "She said Alice is her only friend. She must be alone a lot of the time."
    scene ch5sc01_077 with dissolve
    lu "..."
    mc "Sorry I snapped at you."
    mc "I don’t have the best temper when it comes to stuff like that."
    scene ch5sc01_078 with dissolve
    "A subtle smile appears on Luna’s face."
    scene ch5sc01_079 with dissolve
    lu "It’s okay... I was out of line."
    lu "Try not to move while I’m channeling."
    scene ch5sc01_080 with dissolve
    lu "If you feel any discomfort let me know, okay?"
    scene ch5sc01_081 with dissolve
    mc "I feel very comfortable."
    scene ch5sc01_080 with dissolve
    lu "Me too. You’re astonishingly warm."
    scene ch5sc01_081 with dissolve
    mc "I get that a lot... I’ve been this way ever since I can remember."
    mc "It’s been handy at times during winter when I’ve had to sleep outside."
    scene ch5sc01_080 with dissolve
    lu "*Mumbles quietly* {size=-10}{b}My bed wouldn’t be cold if you were in it...{/b}{/size}"
    scene ch5sc01_081 with dissolve
    mc "Huh? Did you say something?"
    scene ch5sc01_082 with dissolve
    lu "..."
    scene ch5sc01_083 with dissolve
    lu "Your chest... firm... powerful heartbeats throbbing inside it."
    scene ch5sc01_084 with dissolve
    lu "I can easily sense your magic... flowing all through your body..."
    lu "It’s... incredible. I’m not sure how you can contain it all."
    scene ch5sc01_083 with dissolve
    lu "Even the strongest mage would burst wide open from that..."
    lu "But here you are... right in front of me. Clearly containing it like it’s just a regular Wednesday."
    scene ch5sc01_084 with dissolve
    lu "Just... what are you?"
    scene ch5sc01_085 with dissolve
    mc "I’ll... tell you after we’ve rescued your mom."
    scene ch5sc01_082 with dissolve
    lut "A week ago I didn’t know him... except from Alice’s stories."
    lut "And now I can’t imagine what I'd do without him."
    lut "He’s making it possible... to save Mother."
    scene ch5sc01_083 with dissolve
    lu "Okay. Let’s begin!"
    scene ch5sc01_086 with dissolve
    "She takes a step towards you, placing both of her delicate hands on your chest."
    "As she traces her fingertips across your skin, you feel your magic respond..."
    "Surprisingly, the reaction is calm... not chaotic and volatile like usual."
    mct "She’s... able to calm me? How?"
    mct "Can my body sense that she has no ill intentions?"
    scene ch5sc01_087 with dissolve
    lut "I’m going to channel him now... I’ve never done this with a man before."
    lut "It’s an... intimate thing for mages and witches..."
    scene ch5sc01_088 with dissolve
    lut "Sharing your magical essence with someone else... It’s a sign of enormous trust."
    lut "A connection that nobody else understands."
    lut "[mc]... I-... Thank you."
    "She spends a few minutes silently channeling you, then your combined magic takes effect."
    scene ch5sc01_088a with dissolve
    with vpunch
    $ renpy.pause(1)
    lut "Incredible... I... I feel him."
    mct "Woah... I can feel every emotion within her, I..."
    scene black with Dissolve(1.5)
    "A woman appears in both of your minds."
    with vpunch
    scene ch5sc01_089 with Dissolve(1.5)
    lu "No... It-It can’t be."
    scene black with Dissolve(1.5)
    scene ch5sc01_090 with Dissolve(1.5)
    mc "Luna, who is that woman?"
    scene black with Dissolve(1.5)
    scene ch5sc01_091 with Dissolve(1.5)
    lu "It’s... She-..."
    scene black with Dissolve(1.5)
    scene ch5sc01_089 with Dissolve(1.5)
    lu "Rose... The Mages Guild’s second-in-command."
    lu "My mothers closest ally and friend."
    scene black with Dissolve(1.5)
    scene ch5sc01_090 with Dissolve(1.5)
    mc "Why would someone like that be involved in hexing your mother?"
    lu "It... It can’t be... I’ve known her my entire life."
    scene black with Dissolve(1.5)
    scene ch5sc01_091 with Dissolve(1.5)
    lu "She’s watched over me countless times when Mother had important guild business."
    lu "Why... would she do this??"
    scene ch5sc01_089 with dissolve
    mc "Are you certain the hex comes from her?"
    lu "There’s no mistaking it. With the power from your magic, the locator spell is working with pinpoint accuracy."
    scene ch5sc01_090 with dissolve
    lu "Rose is the one who hexed my mom."
    lu "How could she betray us like this? I don’t... I don’t understand!"
    scene ch5sc01_091 with dissolve
    mc "Let's not jump to conclusions. We can’t know for certain until we find her..."
    mc "You said she was second only to your mother in the Mages Guild?"
    scene ch5sc01_089 with dissolve
    mc "It could be that she wanted to get out from under your mother's shadow."
    mc "Getting rid of your mother would allow her to become the next guildmaster."
    scene ch5sc01_090 with dissolve
    mc "Or it could be that Taron has something on her..."
    mc "Something precious to her that he is using to get what he wants."
    scene black with dissolve
    scene ch5sc01_092 with dissolve
    with vpunch
    lu "*Groans* Ahhh!"
    lu "Ishai, Ittu, Deto, Mur!"
    scene ch5sc01_088a with dissolve
    "Luna snaps the two of you out of the channeling, the ambiance in the room returns to normal."
    scene ch5sc01_088a with dissolve
    $ renpy.pause(1.5)
    scene ch5sc01_086 with dissolve
    mc "What was that? It felt like she was looking right at us?"
    scene ch5sc01_077 with dissolve
    lu "..."
    scene ch5sc01_093 with dissolve
    lu "She detected us."
    lu "She won’t know who was locating her, but she definitely felt our presence."
    scene ch5sc01_077 with dissolve
    mc "She will be expecting us then."
    scene ch5sc01_093 with dissolve
    lu "I still can’t believe she is actually behind this..."
    lu "Someone I've known my whole life? She-... she was like family."
    lu "I feel so... alone."
    scene ch5sc01_077 with dissolve
    mc "Hey... come here."
    scene ch5sc01_094 with dissolve
    "She wraps her arms closely around you and you're able to feel her shaking slightly."
    mc "You’re not alone. I’ll help you figure this out."
    lut "He’s being so kind to me..."
    scene ch5sc01_095 with dissolve
    lu "[mc]... I-... thank you. Rescuing my mom means everything to me..."
    lu "It’s all I can think about."
    lu "I’ve felt so isolated... so alone these last couple of months."
    scene ch5sc01_096 with dissolve
    lu "I’ve always been alone, I don’t have any siblings or friends..."
    lu "Every time I thought I'd made a friend in the past, it turned out they just wanted favors from my mom."
    scene ch5sc01_095 with dissolve
    lu "I managed to make friends with Alice all on my own and it’s been great, so so great!"
    lu "And now, you as well. You’re willing to risk yourself to help me get my mom back..."
    scene ch5sc01_094 with dissolve
    mc "Hey... It’s the least I could do."
    mc "Despite all that you’ve had to deal with, you still made friends with Alice."
    mc "You found it within yourself to give her a chance, and you clearly care about her. That means a lot to me."
    scene ch5sc01_095 with dissolve
    lu "[mc]..."
    mc "Don’t worry Luna. I’ll make sure we get your mom back... safe and sound."
    lu "I-... I don’t know what to say..."
    scene ch5sc01_096 with dissolve
    mc "You don’t have to say a word. The way you’re hugging me right now-"
    mc "Is telling me everything I need to know. We trust each other."
    lu "..."
    scene ch5sc01_097 with dissolve
    mc "Oh?"
    scene ch5sc01_098 with dissolve
    lu "*Mwaahh!*"
    lu "Just a little thanks..."
    "Her lips lingers on your cheek for a few moments before she breaks it off."
    scene ch5sc01_068 with dissolve
    mc "Where are you running off to?"
    scene ch5sc01_067 with dissolve
    lu "If you want more of that... you’ll have to take me on a proper date."
    lu "For now, I've gotta prepare some stuff and meet up with Alice."
    scene ch5sc01_066 with dissolve
    lu "Meet me back here tomorrow? We can go see Rose together."
    scene ch5sc01_065 with dissolve
    mc "Sure, I’ll probably stop by around noon."
    scene ch5sc01_067 with dissolve
    lu "Great. See you tomorrow then... Loverboy."
    scene ch5sc01_068 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1.5)
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc6 with Dissolve(2)
    $ renpy.pause()
    scene ch4sc19_227 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Hey, Dalen. Eliza said you had something for me?"
    scene ch4sc19_228 with dissolve
    da "Oh, I’ve got something for you alright."
    mc "Is it about Eliza? Did you find something about her vampirism?"
    da "No... Not yet. I’ve put word out to several of my acquaintances that I’m looking for info on vampires."
    da "But I'm afraid vampire history seems to be veiled in mystery. At least on Luxeron..."
    scene ch4sc19_229 with dissolve
    mc "If it isn’t about Eliza, then why did she make it sound so important?"
    scene ch4sc19_230 with dissolve
    da "We’ve just landed the biggest contract in the Guild’s history."
    scene ch4sc19_230 with dissolve
    mc "That big? I knew we were doing better... but this sounds major."
    scene ch4sc19_233 with dissolve
    mc "What is the contract? Some sort of terrifying monster? A rare species of cave troll?"
    mc "Wait... Don't tell me a dragon is terrorising a nearby village?!"
    mc "I've always wanted to see a dragon."
    scene ch4sc19_228 with dissolve
    da "Well... sit down and I'll give you the details."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ss13 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc02_001 with Dissolve(1.5)
    "Distant shouting."
    scene ch5sc02_002 with dissolve
    with vpunch
    am "{b}WHAT?!{/b} Daddy no!"
    am "Absolutely not!"
    scene ch5sc02_003 with dissolve
    am "I don’t need a babysitter! I’m nineteen for heaven's sake!"
    am "My 20th name day is coming up soon!"
    scene ch5sc02_004 with dissolve
    bn "Darling... he's not a babysitter."
    bn "He's a bodyguard, your bodyguard."
    scene ch5sc02_002 with dissolve
    am "I don’t need that either! No!"
    scene ch5sc02_003 with dissolve
    am "You’re always trying to control my life!"
    am "'Amelia, stay inside the castle' this... 'Amelia, don’t run around the city' that..."
    scene ch5sc02_004 with dissolve
    bn "Amelia... it’s for your own good."
    bn "You know full well that the neighbouring lords have been growing bolder."
    bn "How the kingdom is on the verge of civil-war, making you a prize target."
    scene ch5sc02_003 with dissolve
    am "Nuh-Uh! I refuse to listen to that excuse one more time!"
    am "I'm always going to be a 'target' because I'm your daughter!"
    am "But I'm old enough to experience things on my own! I can't live inside the castle my entire life!"
    scene ch5sc02_004 with dissolve
    bn "*Sigh* Well, since you’re so grown up..."
    bn "The other nations have been pressuring us to select a suitable marriage candidate."
    bn "Since your mother and I haven’t been able to produce a male heir..."
    bn "You'll have to marry a highborn son from one of the other four nations."
    scene ch5sc02_002 with dissolve
    with vpunch
    am "{b}WHAT?!{/b} You can’t be serious, Daddy! There’s no way I’ll agree to that!"
    am "You can't just use me as some sort of bargaining chip... for what?!"
    scene ch5sc02_004 with dissolve
    bn "For peace. If we can’t form a strong alliance with the other nations they'll look to overthrow us instead."
    bn "I’m not young anymore... They're pressuring me to see if I'll succumb to their demands."
    scene ch5sc02_005 with dissolve
    am "What does this have to do with me needing a bodyguard?"
    scene ch5sc02_004 with dissolve
    bn "I've been dragging my heels on this since your eighteenth nameday... and they're getting impatient."
    bn "We've intercepted an increasing number of foreign spies."
    bn "Those we were able to interrogate all had the same objective... you."
    scene ch5sc02_005 with dissolve
    am "Me? Why would spies be so interested in me?"
    scene ch5sc02_004 with dissolve
    bn "As I just told you, sweetheart, you’re the only heir to Luxeron."
    bn "Which means you’re the key to ruling the five kingdoms of Midomir... At least without declaring an all-out war."
    bn "Which is why I have decided... *Sighs heavily*"
    bn "On your 20th nameday we will be hosting an event where suitors from the other kingdoms will come to court you."
    bn "We'll also invite several noble houses from within Luxeron."
    bn "There could be a potential match with one of them as well."
    scene ch5sc02_002 with dissolve
    with vpunch
    am "Absolutely not! Ugh! Daddy, you can't do this!"
    scene ch5sc02_004 with dissolve
    bn "It’s already been put into motion. You will be able to choose an appropriate husband."
    bn "It’s something every royal and noble family goes through. And now it’s your turn."
    bn "I know it feels unfair, but it is a burden we carry as the Royal family."
    scene ch5sc02_005 with dissolve
    am "But... why can’t there be an alliance without marriage?"
    am "Why do I have to be sold off like a piece of meat? The thought alone disgusts me!"
    am "I want to meet a proper man, fall in love the genuine way! Not become some object to a stranger!"
    scene ch5sc02_004 with dissolve
    bn "I’m sorry, darling. Try to understand... If we fail to form an alliance and war breaks out..."
    bn "Thousands... if not tens of thousands, will die."
    bn "Is that a responsibility you want to take on?"
    scene ch5sc02_002 with dissolve
    am "Obviously I don't want war!"
    am "I don’t want that at all. The stories you've told me are bad enough."
    scene ch5sc02_004 with dissolve
    bn "Good. Then you understand why it’s paramount that you find a suitable husband to secure the realm."
    scene black with Dissolve(1.5)
    scene ch5sc02_006 with Dissolve(1.5)
    mc "*Sigh* Really? I don’t think this is necessary..."
    cbl "It will have to suffice. Scrub yourself clean, then we’ll make you presentable for His Majesty."
    mc "Fine..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc02_007 with Dissolve(1.5)
    mct "Hnngh... I can’t believe I let Dalen and Eliza talk me into this..."
    mct "‘High priority contract’ ... ‘Think of the guild’ ... ‘All the profit it will generate’ ..."
    scene ch5sc02_008 with dissolve
    mct "Easy for them to say... They aren’t the ones being pampered and forced to clean up..."
    mct "The coin better be as ridiculous as Dalen suggested."
    mct "I guess having a member of the guild being employed by the Royal family is quite the reputation boost."
    "You hear the door creak open and to your surprise it’s not the chamberlain from earlier."
    scene ch5sc02_009 with dissolve
    md2 "..."
    scene ch5sc02_010 with dissolve
    mct "She looks timid..."
    mct "She probably wants to be here just about as much as myself..."
    mc "State your business."
    scene ch5sc02_011 with dissolve
    md2 "Oh... Uh... I’m here to bring you a towel..."
    scene ch5sc02_010 with dissolve
    mc "And here I thought you were sent by his majesty to wash my back."
    scene ch5sc02_012 with dissolve
    md2 "*Stuttering* W-What? ... N-No! H-He wouldn’t ask such a thing!"
    md2 "*Stuttering* I... I’m Amelia’s p-personal handmaiden!"
    scene ch5sc02_010 with dissolve
    mc "You can relax... I was merely jesting."
    scene ch5sc02_011 with dissolve
    md2 "Y-You shouldn’t joke about such matters..."
    scene ch5sc02_010 with dissolve
    mc "*Chuckles* Right, you can leave the towel on the stool and I'll be done shortly."
    scene black with Dissolve(1.5)
    scene ch5sc02_013 with Dissolve(1.5)
    mct "Not gonna lie, it felt great to get cleaned up. The water is even heated."
    scene ch5sc02_014 with dissolve
    cbl "Hmm. This must suffice."
    scene ch5sc02_015 with dissolve
    mc "Think Bennen cares if I’m clean?"
    scene ch5sc02_016 with dissolve
    cbl "The gentleman will refer to His Imperial Majesty by his full title, or not at all."
    mct "This guy is so full of himself..."
    cbl "If the gentleman will be seated, the shaving and trim will commence shortly."
    scene ch5sc02_015 with dissolve
    mc "The what now? You’re not cutting my hair."
    scene ch5sc02_016 with dissolve
    cbl "No. Not me, obviously. One of our handmaidens will... *Raised voice* You can enter now."
    scene ch5sc02_017 with dissolve
    "You sit down in protest and the girl from earlier enters the room."
    cbl "Please see to it that the gentleman is groomed and ready for an audience with His Excellency."
    scene ch5sc02_018 with dissolve
    "The chamberlain leaves the room and the timid maiden approaches you nervously."
    scene ch5sc02_019 with dissolve
    md2 "P-Please... hold still."
    scene ch5sc02_020 with dissolve
    mc "You don’t have to do this. I’m fine the way I am."
    scene ch5sc02_019 with dissolve
    md2 "N-No. I... I have to. Otherwise-..."
    "The girl manages to stop herself mid sentence."
    md2 "Please... let me do this."
    mct "Sounds like she’s scared of getting into trouble. They are probably pretty strict with the staff."
    mct "She seems sweet... There’s no reason to cause her any trouble."
    scene ch5sc02_020 with dissolve
    mc "Okay. But just trim the edges alright? I like my hair the way it is."
    scene ch5sc02_021 with dissolve
    md2 "Okay! T-Thank you!"
    "Her delicate hand guides your chin upwards."
    scene ch5sc02_022 with dissolve
    mc "Sorry if my joke earlier made you uncomfortable."
    md2 "..."
    scene ch5sc02_023 with dissolve
    md2 "It’s okay... It just caught me by surprise."
    md2 "I’m not used to jokes like that..."
    md2 "Usually when men make such comments at me... they’re being serious."
    scene ch5sc02_024 with dissolve
    mc "You have to endure those comments often?"
    "The girl nods."
    scene ch5sc02_025 with dissolve
    md2 "Luckily, I was picked to be Princess Amelia's personal handmaiden before I came of age."
    md2 "Now I’m off limits to men."
    md2 "Even nobles and their... comments and desires."
    scene ch5sc02_024 with dissolve
    mc "Good..."
    mc "I can only imagine how bad it must be to be surrounded by rich entitled assholes."
    scene ch5sc02_026 with dissolve
    with vpunch
    md2 "*Laughs* Oh my! I’m not supposed to laugh at such vulgar language!"
    scene ch5sc02_022 with dissolve
    mc "Your secret is safe with me."
    mc "It’s not like I owe these presumptuous pricks anything."
    scene ch5sc02_026 with dissolve
    md2 "*Laughs* S-Stop! I’ll get in trouble!"
    scene ch5sc02_022 with dissolve
    md2 "..."
    mct "She has a cute smile."
    scene ch5sc02_025 with dissolve
    fr "I’m Frida."
    scene ch5sc02_022 with dissolve
    mc "[mc]. Pleasure to meet you, Frida."
    fr "*Nods*"
    scene ch5sc02_025 with dissolve
    fr "Okay! All done!"
    scene ch5sc02_022 with dissolve
    mc "Oh? You’re quick. How do I look?"
    scene ch5sc02_025 with dissolve
    fr "Beautiful..."
    scene ch5sc02_023 with dissolve
    with vpunch
    fr "I-... I mean presentable!"
    scene ch5sc02_024 with dissolve
    mc "Beautiful, huh? I’ll take it."
    scene ch5sc02_026 with dissolve
    fr "*Laughs* You’re trouble!"
    mct "That tattoo she has, I've seen similar ones back in the Sen'ju region, is she from there?"
    scene ch5sc02_027 with dissolve
    cbl "How are we doing in here?"
    cbl "If you’ve got time to fool around, I'll assume the gentleman is ready."
    cbl "Now leave and return to your duties."
    scene ch5sc02_028 with dissolve
    fr "S-Sorry..."
    "The girl returns to her timid self and leaves the room."
    scene ch5sc02_029 with dissolve
    mct "Frida... Hmh."
    mct "She was starting to feel comfortable, but as soon as this asshole entered..."
    mct "She went straight back to being timid."
    mc "Was that really necessary? She’s not a puppet."
    scene ch5sc02_030 with dissolve
    cbl "Commoners- Ugh."
    cbl "We can bathe you, shave you and clothe you, but teaching you manners..."
    cbl "That is the real challenge."
    scene ch5sc02_031 with dissolve
    mc "You’re a real peach to be around, you know that?"
    scene ch5sc02_032 with dissolve
    cbl "*Sigh* The gentleman may now dress."
    cbl "Sadly, I wasn’t able to get your exact measurements."
    cbl "If the garments chafe, our tailor will adjust them."
    scene ch5sc02_033 with dissolve
    mc "My measurements?"
    scene ch5sc02_015 with dissolve
    with vpunch
    mc "Where are my clothes?!"
    scene ch5sc02_016 with dissolve
    cbl "Where they should have gone long ago: to the laundress."
    cbl "Fret not. They will be returned to you after the audience, clean and starched."
    scene ch5sc02_015 with dissolve
    mc "You’re kidding... right?"
    scene ch5sc02_016 with dissolve
    cbl "This is no time for jests."
    cbl "The gentleman will approach me once he has dressed himself."
    scene black with Dissolve(1.5)
    mct "At least they picked black... *Sigh* Let’s get this over with."
    scene ch5sc02_035 with Dissolve(1.5)
    mct "This is ridiculous... I look like a damn peacock."
    mct "Is this really how nobles dress? ... Suddenly being poor doesn’t seem so bad."
    scene ch5sc02_036 with dissolve
    cbl "Ah. Black suits the gentleman."
    cbl "Does the outfit satisfy the gentleman?"
    scene ch5sc02_037 with dissolve
    mc "My own flexible, tried and tested clothes are what would satisfy me. I’m stiff as a board in these..."
    scene ch5sc02_036 with dissolve
    cbl "If the gentleman isn’t pleased, I could fetch him another outfit?"
    scene ch5sc02_037 with dissolve
    mc "It’s fine... I doubt it would be any better..."
    mc "So what now? Powder my nose?"
    scene ch5sc02_038 with dissolve
    cbl "No need. The gentleman’s complexion is light enough."
    mc "..."
    scene ch5sc02_037 with dissolve
    mc "Great. So can we go see Benn- His Majesty now?"
    scene ch5sc02_036 with dissolve
    cbl "Not quite... The gentleman is to stand before the King of Luxeron, Lord Protector of the Realms..."
    scene ch5sc02_038 with dissolve
    cbl "I must confirm that he knows how to bow when meeting His Excellency."
    mct "I’m going to kill Dalen..."
    ####Choice####
    menu:
        "Comply.":
            scene ch5sc02_039 with dissolve
            mc "Alright... *Sighs heavily*"
            scene ch5sc02_038 with dissolve
            cbl "Please, demonstrate."

        "Refuse.":
            scene ch5sc02_039 with dissolve
            mc "I know how to bow... I’m not some boor you know?"
            scene ch5sc02_038 with dissolve
            cbl "Nevertheless, a demonstration is in order before we proceed."

    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch5sc02_040 with Dissolve(1)
    mc "Happy?"
    scene ch5sc02_041 with dissolve
    cbl "That, sir, is how you might bow to a common whore on a street corner, not the King of Luxeron."
    mct "This fucking guy... He should consider himself lucky I’m not currently drowning him in the washtub."
    mct "*Sigh* Probably won’t do the guild any favors if I kill a royal servant..."
    cbl "It goes like this, left leg extended behind, right arm straight, hand flat, head down, chin to chest."
    scene black with Dissolve(1.5)
    scene ch5sc02_042 with Dissolve(1.5)
    mc "..."
    cbl "Hmm, lacking fluidity and grace. But we’ve learned to expect less from commoners."
    cbl "Good, good. Let’s proceed..."
    scene ch5sc02_043 with dissolve
    cbl "If the gentleman will follow along."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch5sc02_044 with Dissolve(1.5)
    cbl "The gentleman will address his majesty only when spoken to, using the appropriate title of course."
    scene ch5sc02_045 with dissolve
    mc "What? His Archexellency? His Holy-Magnificency?"
    cbl "Ah, I see the gentleman is in the mood for jests. I fear His Majesty might not share his disposition."
    scene ch5sc02_046 with dissolve
    cbl "'Your Majesty' will suffice. Spoken loudly, clearly, and with respect."
    cbl "The gentleman may enter."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch5sc02_002 with Dissolve(1.5)
    with vpunch
    am "{b}UUURH!{/b} I don’t need or want some lame bodyguard breathing down my neck!"
    am "You never understand me! Always trying to keep me in this boring castle!"
    scene ch5sc02_004 with dissolve
    bn "Sweetheart, we've discussed this at length. I’m doing it for your own good. Please see reason."
    bn "Besides I’ve already arranged for a bodyguard. He’s very capable, I'm told."
    am "Ugh... Who is this bodyguard then? Probably some old guy..."
    scene ch5sc02_004a with dissolve
    bn "You can judge for yourself, here he is now."
    scene ch5sc02_004b with dissolve
    amt "He looks familiar... Wait-"
    scene ch5sc02_004c with dissolve
    amt "It’s the guy from this morning! The knucklehead who bumped into me!"
    if charisma >= 7:
        amt "And he had the nerve to call me beautiful after helping me up..."
        amt "Ugh! I hope he doesn't expect me to be happy about this!"

    else:
        amt "What in the heavens is he doing here!? How is he going to be my bodyguard!?"

    scene ch5sc02_047 with dissolve
    mct "So that’s the king... And that’s-"
    cbl "Approach. Don’t keep His Majesty waiting."
    scene ch5sc02_048 with dissolve
    cbl "Stop at the stairs and bow as we rehearsed."
    scene ch5sc02_049 with dissolve
    mct "*Sigh* I can’t believe I’m doing this."
    scene ch5sc02_050 with dissolve
    "You proceed to bow as instructed by the chamberlain."
    scene ch5sc02_051 with dissolve
    "Both the king and the princess seem pleasantly surprised."
    amt "He-... He's bowing?"
    scene ch5sc02_052 with dissolve
    amt "He... knows how to bow properly?"
    scene ch5sc02_053 with dissolve
    amt "Ugh! So what? Anyone can learn how to bow..."
    amt "In fact, the knucklehead should have bowed to me this morning instead of trampling on me in the market!"
    scene ch5sc02_054 with dissolve
    am "Don’t come near me, you oaf!"
    am "If I see you again I'll call the guards on you."
    mct "Bitch..."
    scene ch5sc02_055 with dissolve
    bn "Please, excuse my daughter. She isn’t too fond of the idea of being assigned a bodyguard."
    bn "Now, stand. Your back must be getting sore from holding that dreadful bow."
    scene ch5sc02_056 with dissolve
    mc "Your Majesty."
    scene ch5sc02_057 with dissolve
    bn "*Chuckles* Hah! First a proper bow and now addressing me correctly? That’s unusual for a commoner."
    mc "I didn’t want to disappoint the chamberlain, we’re friends."
    bn "*Chuckles* Hah! Nobody's friends with the chamberlain, but I like your attitude."
    scene ch5sc02_058 with dissolve
    mc "*Scoffs* Yeah... he doesn't seem too fond of me."
    mc "I take it you didn’t hire me to talk about social etiquette, though?"
    scene ch5sc02_059 with dissolve
    bn "My daughter... Amelia, she’s in danger."
    mc "I presume she's the one who just stormed off, hissing at me?"
    scene ch5sc02_057 with dissolve
    bn "*Chuckles* That'd be the one."
    bn "I need you to keep an eye on her, protect her with your life if need be."
    scene ch5sc02_058 with dissolve
    mc "Why do you suspect that she's in danger?"
    mc "I’ll need details if I’m to guard her. I need to know what to be on the lookout for."
    scene ch5sc02_059 with dissolve
    bn "*Sigh* I suppose you do need some information to go on."
    bn "Come, we’ll discuss the matter further in my office."
    scene ch5sc02_059a with dissolve
    mc "Your Majesty."
    mct "That ring... It’s hard to tell from this distance but it’s definitely enchanted."
    mct "Just like his daughter's."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch5sc02_060 with Dissolve(1)
    $ renpy.pause()
    scene ch5sc02_061 with dissolve
    bn "Before we begin, are you familiar with the Five Kingdoms that make up Midomir?"
    mc "I’ve heard bits here and there, but I’ve never traveled beyond Luxeron, sir."
    bn "I suspected as much. Most people never get to venture beyond the continent they are born on."
    bn "Here, take a look at this. It should help you visualize it as I explain."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene map01 with Dissolve(1.5)
    $ renpy.pause()
    mc "Interesting, I’ve never really seen a map this detailed."
    bn "I’ve had the best explorers travel the continents and write down what they’ve seen."
    bn "There are still unexplored areas though, and many discoveries yet to be made."
    bn "As you can see, we have the five main kingdoms of Midomir."
    scene map02 with Dissolve(1.5)
    bn "First we have Luxeron. The continent we live on."
    bn "It is the ruling kingdom and the seat of the High-King of Midomir."
    mc "High-King?"
    bn "Each continent has its own King or Queen ruling over it, but ever since the succession wars some 500 years ago-"
    bn "The five kingdoms elected a High-King who would be the protector of all the realms."
    bn "That duty befell my family, and has been passed down through my lineage to this day."
    bn "Now, as you can see, Luxeron is the largest kingdom and contains the most diversity."
    mc "Yeah, I come from a small village north of Luxenford. I don’t see it here, though."
    bn "*Chuckles* Not every little detail is mapped, only points of significant value or interest."
    bn "For a more detailed layout you'll have to visit the League of Explorers and inquire about more localized maps."
    scene map03 with Dissolve(1.5)
    bn "Now let’s turn our attention northwest, to the kingdom of Izentul."
    bn "We haven’t explored it completely, as it's not a very hospitable environment to visit."
    scene iz1 with Dissolve(1.5)
    bn "It’s home to Ice Wyverns: ruthless beasts with an appetite as large as themselves."
    scene iz2 with Dissolve(1.5)
    bn "Then there are the Frost Giants. Not the friendliest of neighbors to meet."
    bn "Like their regular giant counterparts, they mostly keep to themselves but they'll crush anyone who intrudes on their territory."
    scene iz3 with Dissolve(1.5)
    bn "And then there’s the faction who controls the kingdom, Sney-dwarves."
    bn "We haven’t had much interaction with them over the centuries."
    bn "They are the same size as regular dwarves but their skin appears like a mixture of ice and gemstones."
    scene iz4 with Dissolve(1)
    bn "The ruler of Izentul is King Osirion. Not much is known about him and he's never shown much interest in communicating with us."
    mc "I’ll go out on a limb here and assume they're not the people you’re worried about?"
    scene map03 with Dissolve(1)
    bn "You would be correct. They’ve never shown any interest in what lies beyond their own kingdom."
    scene map04 with dissolve
    bn "Now, let’s move on to Arazalia. It's a land of vast deserts and large mountains."
    bn "There are said to be huge cavern networks below the sands that provide refuge from the heat."
    scene ara1 with Dissolve(1)
    bn "It's home to the obscenely large Arazalian lions, ferocious predators."
    scene ara2 with Dissolve(1.5)
    bn "Another fierce predator that calls the vast deserts home are Drakehounds."
    bn "They're slightly smaller than the lions, but their agility and speed make them terrifying foes."
    bn "Their bodies are covered in hardened scales that serve as protection."
    scene ara3 with Dissolve(1.5)
    bn "If you ever find yourself searching for treasure in the mountains and mines of Arazalia..."
    bn "You'll want to be on the lookout for Ravagers as well. They are powerful creatures and very territorial."
    bn "They've been reported to tear limbs off humans who venture too close to their breeding grounds."
    scene ara4 with Dissolve(1.5)
    bn "Beneath the sand dunes and mountains you can find the most pure deposits of diamonds and gems."
    bn "That makes it a valuable kingdom and they have vast amounts of wealth."
    scene ara5 with Dissolve(1)
    bn "Their Queen, Sahi. She's the embodiment of ambition... ruthless ambition."
    bn "She killed her husband, the previous king on the night of their wedding."
    bn "Since then, Arazalia has become a Matriarchy, the first of it's kind."
    mc "Ruthless indeed, with wealth, ambition often follows..."
    bn "You know your stuff. We’ve already caught several spies from Arazalia."
    bn "All of whom bit off their own tongues before we could interrogate them."
    scene map05 with Dissolve(1)
    bn "Let’s move on to Elfwyr. As you can probably imagine, it's the homeland of the elves."
    scene elf4 with Dissolve(1)
    bn "Unlike the other kingdoms, theirs is ruled by dual leaders: a pair of elven siblings."
    bn "Prince Ninthalor and Princess Nuin. They took over after the death of their father half a century ago."
    mc "They've been co-ruling for fifty years? I assume Elves live longer than humans?"
    bn "Correct. From what I’ve been able to gather, an elf lives roughly ten times longer than a human."
    bn "Some live to 800, 900, and a few even make it to a 1000 years old."
    bn "They’re a noble race who've been our close allies ever since the succession wars."
    scene elf1 with Dissolve(1)
    bn "Their kingdom mostly consists of large serene forests and neverending rivers."
    bn "Large valleys and mountains that reaches the clouds."
    scene elf2 with Dissolve(1)
    bn "Besides elves, you'll also find dryads, fairies, centaurs and elementals there."
    mct "Hmh, I wonder if Sylph is from Elfwyr?"
    mc "Since you have an alliance with the elves, I’m assuming you aren’t suspecting them of plotting against you?"
    scene map05 with Dissolve(1)
    bn "I'd be surprised if that were the case. As I said, they are a noble race."
    scene map06 with Dissolve(1.5)
    bn "Lastly, we have Nerzir. Much like Izentul, we haven’t been able to explore it properly."
    bn "It's a land shrouded in mystery, but we know a wide range of beasts and creatures reside there."
    scene ner1 with Dissolve(1)
    bn "This includes Magma Wyverns. Just like the Ice Wyverns, they’re vicious and won’t hesitate to make a meal out of you."
    scene ner2 with Dissolve(1.5)
    bn "Another formidable foe are the Dracobulls..."
    bn "The size of Arazalian elephants, they easily trample anyone who gets in their way."
    scene ner3 with Dissolve(1.5)
    bn "Their lands are also home to a wide variety of ogres and goblins."
    mc "I’m familiar with those... nasty creatures."
    bn "Sadly, many of them have taken residence in other kingdoms over the years ..."
    scene ner4 with Dissolve(1)
    bn "It’s ruled by a vicious vampire lord who is known as Ducalion."
    mct "The king knows about vampires? Hmh, maybe once I'm more familiar with him I could ask what more he knows about them."
    bn "He's rumored to be the oldest among his kind. However, there’s no way to be certain."
    mct "Hmh... I wonder if he's a pure-blooded vampire like Eliza?"
    bn "We haven’t had any contact with them for at least a century at this point."
    scene map06 with Dissolve(1)
    bn "But we've caught a few spies from their domain too. None of which leads us to anything concrete."
    scene ch5sc02_061 with Dissolve(1)
    mc "So, Arazalia and Nerzir are the two suspects who might be plotting against you?"
    bn "That's the conclusion I’ve come to. Obviously it would be naive to just rule out Izentul and Elfwyr."
    bn "But it would be highly unlikely that they would be involved."
    scene ch5sc02_063 with dissolve
    bn "Our alliance with Elfwyr is strong and beneficial to both sides, we have great trade routes there."
    bn "As for Izentul, as I said they are secluded and haven’t ever shown any interest in the rest of Midomir."
    scene ch5sc02_062 with dissolve
    mc "Why do you suspect they would be targeting your daughter?"
    scene ch5sc02_063 with dissolve
    bn "It’s the best way for them to gain control over Luxeron. I don’t have a male heir..."
    scene ch5sc02_064 with dissolve
    bn "So kidnapping my only heir and forcing a marriage agreement upon us would allow them to-"
    bn "To become High King of Midomir once my rule is over."
    scene ch5sc02_063 with dissolve
    bn "It’s the best and most strategic way for them to acquire the title without an all-out war."
    scene ch5sc02_061 with dissolve
    mct "That does make sense."
    mct "The smart play is to go for his daughter and avoid a war."
    scene ch5sc02_062 with dissolve
    mc "What do you need from me, Your Majesty?"
    scene ch5sc02_063 with dissolve
    bn "My daughter should be safe here in the castle. But she loves to get out and visit the city..."
    bn "That’s when I need you to accompany her and make sure she’s protected at all times."
    scene ch5sc02_062 with dissolve
    mc "How would you like me to handle it, if a situation arises?"
    scene ch5sc02_063 with dissolve
    bn "I will grant you complete authority in such cases. You deal with it however you see fit."
    bn "I'll alert my guards about you and inform them of your position."
    scene ch5sc02_062 with dissolve
    mc "Your daughter's outburst earlier..."
    mc "Threatening to set the guards on me if she sees me again. Will that be a problem?"
    scene ch5sc02_063 with dissolve
    bn "No... She just gets like that when she doesn’t get her way ... I’m afraid I’ve spoiled her."
    bn "I'll be sure to let the guards know not to heed her commands when it comes to you."
    scene ch5sc02_062 with dissolve
    mc "That’s a lot of power and trust you’re placing in me. Why?"
    scene ch5sc02_063 with dissolve
    bn "You’ve been recommended to me by someone I trust. And my daughter's safety is on the line."
    bn "I hope to marry Amelia off to a representative from Elfwyr. That would create a strong union-"
    bn "-From that point on, she'll be guarded by not just one, but two kingdoms."
    scene ch5sc02_062 with dissolve
    mc "That would make her far less vulnerable."
    mc "And put her and her future husband in a powerful position."
    scene ch5sc02_063 with dissolve
    bn "Exactly, You've got a good head on your shoulders kid."
    bn "None of the other kingdoms would dare move against her."
    scene ch5sc02_065 with dissolve
    bn "But I need you to protect her until that happens."
    bn "You'll be well compensated for your troubles... 40 silvers each time you're on duty."
    mct "Damn... Dalen wasn't kidding when he said it would pay well."
    bn "You'll be needed once or twice a week to escort Amelia when she visits the city."
    bn "And for the occasional royal event."
    scene ch5sc02_066 with dissolve
    mc "I won’t let you down. Amelia will be safe with me, Your Majesty."
    scene ch5sc02_067 with dissolve
    bn "Good, good. And please... You can skip the formalities when we’re alone."
    bn "It all becomes so formal. Tedious if you ask me. But it's tradition."
    bn "Now go. My wife, Queen Merida awaits you in her chambers."
    scene ch5sc02_066 with dissolve
    mc "Your wife?"
    scene ch5sc02_067 with dissolve
    bn "Yes, when she found out I was hiring a personal bodyguard for Amelia-"
    bn "-She demanded an audience once they had been hired."
    mct "Ahh. Makes sense, she probably wants to size me up herself and make sure I’m capable."
    scene ch5sc02_066 with dissolve
    mc "Alright, Your Majes- Bennen. Where will I find her?"
    scene ch5sc02_067 with dissolve
    bn "Her chambers are up the stairs from this office. Take two left turns and it will be at the end of the hallway."
    bn "Now go. She doesn’t like to be kept waiting."
    scene black with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc02_068 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mct "This palace is huge... Bennen made it seem like a short walk from his office..."
    scene ch5sc02_069 with dissolve
    mct "That must be the Queen’s chambers up ahead."
    mct "Hopefully it won’t take too long... Eliza is probably getting impatient back at the guild."
    scene black with Dissolve(1.5)
    scene ch5sc02_070 with Dissolve(1.5)
    qm "..."
    qm "Are we almost finished? I’m expecting a visitor any moment now."
    scene ch5sc02_071 with dissolve
    md "Yes, My Queen."
    md "Just a few more adjustments and you’re all set."
    scene ch5sc02_072 with dissolve
    qm "What would I do without you?"
    scene ch5sc02_071 with dissolve
    md "You would manage just fine."
    md "You’re a very capable woman, my Queen."
    scene ch5sc02_072 with dissolve
    qm "That’s kind of you to say, but you don’t have to flatter me... you’re already my favorite maid."
    scene ch5sc02_073 with dissolve
    qm "*Sighs heavily* Where did my youth go?"
    scene ch5sc02_071 with dissolve
    md "My Queen? You’re still young."
    scene ch5sc02_072 with dissolve
    qm "I wish it were so... I turned 40 last spring."
    qm "My value as a woman is diminishing with every passing day..."
    scene ch5sc02_070 with dissolve
    md "You’re as beautiful as ever, my Queen."
    qm "I used to be so full of life, you know?"
    qm "My very first time at court was when my family sent me to the capital to attend the prince’s annual ball. "
    scene ch5sc02_073 with dissolve
    qm "It was so extravagant! The flowers! The bards and their ballads! The dresses... everything."
    scene ch5sc02_072 with dissolve
    qm "And then, that very same evening... the prince himself asked me for a dance."
    scene ch5sc02_074 with dissolve
    qm "It felt like I was in a dream come true!"
    qm "We danced... We went to events together... Everything was perfect."
    scene ch5sc02_071 with dissolve
    md "Sounds like a fairytale, my Queen."
    scene ch5sc02_072 with dissolve
    qm "Mhh... That it was. It wasn’t until after our wedding that everything became clear."
    qm "You see... the wedding was arranged. My family sending me to court was not the happy accident I'd thought."
    scene ch5sc02_073 with dissolve
    qm "They'd arranged everything with Bennen’s father. Even Bennen knew."
    qm "I felt so betrayed... The mirage of my blissful fairytale had all been a lie."
    scene ch5sc02_070 with dissolve
    qm "Every dance... every event... it was all just a facade to keep up appearances."
    md "My Queen?"
    scene ch5sc02_072 with dissolve
    qm "Bennen isn’t interested in... well, us, you see? But his father was desperate to bury those rumors."
    qm "That’s where I came in. A young and beautiful and very naive girl from outside of court life."
    scene ch5sc02_073 with dissolve
    qm "A perfect match to throw off unwanted accusations about a soon-to-be king."
    qm "I’ve only ever spent one night with Bennen. Our wedding night, nineteen years ago."
    scene ch5sc02_074 with dissolve
    qm "That's when Amelia was conceived. But ever since, we’ve had separate rooms..."
    qm "We attend events together for the sake of appearances. But as soon as they are over, we part."
    scene ch5sc02_073 with dissolve
    qm "This big castle... All of the servants and court attendants... And yet I feel so alone."
    scene ch5sc02_071 with dissolve
    md "My Queen. I didn’t know..."
    scene ch5sc02_072 with dissolve
    qm "You’re the only person I’ve told. I guess I’m just feeling a little anxious and I needed to finally tell someone."
    scene ch5sc02_071 with dissolve
    md "It will stay with me till I die."
    scene ch5sc02_072 with dissolve
    qm "Heavens, no need to be so dramatic. Even if it were to come out, it wouldn’t matter at this point."
    qm "But I would still appreciate it if you would keep it between us."
    scene ch5sc02_073 with dissolve
    qm "There’s no need to sully my husbands reputation just because I didn’t get the happily-ever-after I desired."
    scene ch5sc02_071 with dissolve
    md "All done, my Queen."
    scene ch5sc02_075 with dissolve
    qm "Thank you, you may go now."
    scene ch5sc02_076 with dissolve
    md "As you wish, my Queen. I’ll head to the kitchens and prepare your dinner."
    scene ch5sc02_075 with dissolve
    qm "Thank you. I hope you know how much I appreciate you."
    scene ch5sc02_076 with dissolve
    md "I do. Because of your kindness, my family has been able to afford a roof over their heads."
    scene ch5sc02_075 with dissolve
    qm "It’s the least I could do."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    with vpunch
    scene ch5sc02_077 with Dissolve(2)
    md "Oh! Sorry! I didn’t see you there."
    mc "The fault is mine. I’m looking for the queen’s personal chambers. Am I in the right place?"
    md "So you’re the one she's waiting for? Go on ahead, she’s waiting for you."
    scene black with Dissolve(2)
    scene ch5sc02_078 with Dissolve(1)
    $ renpy.pause(1.5)
    scene ch5sc02_079 with dissolve
    mct "That must be her, Queen Merida... High-Queen of Midomir."
    scene ch5sc02_080 with dissolve
    mct "She does embody a certain charisma. This should be interesting."
    scene ch5sc02_081 with dissolve
    qm "Join me... please?"
    scene ch5sc02_080 with dissolve
    mc "Certainly, Your Majesty."
    scene ch5sc02_082 with dissolve
    mc "I didn’t think a woman of your stature would ever utter the word ‘please’ to a commoner?"
    scene ch5sc02_083 with dissolve
    qm "I know what you must think."
    qm "It’s what everyone thinks..."
    qm "She’s the queen! She must be so noble! I bet she was born right into this!"
    scene ch5sc02_084 with dissolve
    qm "But in fact... people don’t know me at all."
    qm "They- They don’t see me."
    scene ch5sc02_085 with dissolve
    mc "My apologies. I didn’t mean to offend."
    scene ch5sc02_084 with dissolve
    qm "You didn’t. The reason I asked you politely, as an equal, is because..."
    qm "*Sighs heavily* I was a commoner myself once. Born into poverty, I grew up at my family’s homestead."
    scene ch5sc02_083 with dissolve
    qm "Binding hay, shoveling after the pigs, milking the cows, peeling potatoes and pulling weeds..."
    scene ch5sc02_085 with dissolve
    mc "That definitely doesn't sound very queen-like. How did you end up as the queen?"
    mc "I mean-... If I may ask, Your Majesty?"
    scene ch5sc02_086 with dissolve
    qm "Please, let’s drop the formalities. I hear them every day, and quite frankly, I’m tired of them."
    qm "Besides, I find your boldness... refreshing."
    scene ch5sc02_084 with dissolve
    qm "We’ll speak as equals here."
    scene ch5sc02_085 with dissolve
    mc "Merida, then."
    scene ch5sc02_086 with dissolve
    qm "Mhm. There’s that boldness of yours again, assuming it's okay to address me by my first name."
    scene ch5sc02_085 with dissolve
    mc "You wanted to speak as equals, I’m just making sure you get the proper experience... Merida."
    scene ch5sc02_087 with dissolve
    qm "Goodness! *Light giggle* You’re a brazen young man, aren’t you?"
    qm "I hope you aren’t this much trouble when you watch over Amelia, she'll have a fit."
    scene ch5sc02_085 with dissolve
    mc "Maybe she needs someone to ruffle her perfect feathers."
    scene ch5sc02_086 with dissolve
    qm "Now that would be a sight... Bennen and I, we’ve spoiled her for too long."
    scene ch5sc02_085 with dissolve
    mc "She won’t have that problem with me. I’m horrible at spoiling anyone."
    scene ch5sc02_084 with dissolve
    qm "Mh-Hm. I think you might be better at it than you think."
    qm "Did my husband go over the details with you?"
    scene ch5sc02_085 with dissolve
    mc "Yes, he explained the situation you’re facing until Amelia is safely married."
    scene ch5sc02_083 with dissolve
    qm "It's quite the predicament. I myself was tricked into an arranged marriage."
    qm "I wouldn’t wish it upon anyone. Most especially my own daughter."
    scene ch5sc02_085 with dissolve
    mc "You were tricked into marrying the king?"
    scene ch5sc02_088 with dissolve
    qm "*Sigh* I’m afraid so ... It's an odd thing to complain about, I know."
    qm "I’m often reminded how good I have it. How I should be grateful for the life I’ve been given..."
    scene ch5sc02_089 with dissolve
    qm "But a life spent like a bird trapped in a cage? ... Devoid of love? ... Far from your family?"
    qm "If I hadn't had Amelia, and the sense of joy and love she brought into my life... I don’t know."
    scene ch5sc02_090 with dissolve
    "She pauses, clearly distraught."
    mct "She's getting emotional, the pitch in her voice changed."
    scene ch5sc02_091 with dissolve
    qm "..."
    mc "No woman should be made to feel like that. Especially-"
    ####Choice####
    menu:
        "One as beautiful as you.":
            scene ch5sc02_091 with dissolve
            mc "A woman as beautiful and strong as you."
            qm "Oh... You don’t have to flatter an old woman like myself."
            mc "You’re right, I don’t have to. But that’s my honest opinion."
            mc "And who are you calling old? You don’t look a day over 30."
            "A slight blush appears in Merida’s cheeks. Whether it's your words or the touch of your hand, you can't say."
            qm "I... Thank you. I’ll take the compliment then."
            $ queen_trust += 2
            "Merida is surprised by your boldness to compliment her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "The Queen.":
            scene ch5sc02_091 with dissolve
            mc "As the Queen you shouldn’t have to feel like that."
            qm "Thank you, I appreciate it."

    scene ch5sc02_091 with dissolve
    mct "She still hasn’t said anything about my hand... Maybe she finds it comforting."
    mct "Her skin sure is smooth. Softer than I expected."
    scene ch5sc02_088 with dissolve
    qm "Where was I?"
    qm "Oh, right. I was telling you how I came to be Queen."
    scene ch5sc02_092 with dissolve
    qm "The former king, Bennen’s father, was looking for a marriage for his son."
    qm "I can’t discuss why, but he was strongly motivated. And my family saw a way for me to live a prosperous life."
    scene ch5sc02_093 with dissolve
    qm "But I wasn’t told anything other than I would be attending court. Long story short..."
    qm "I fell for the prince. He made me believe we were in love... right up until our wedding night."
    scene ch5sc02_092 with dissolve
    qm "That’s when the curtains for our ‘romance’ came crashing down."
    qm "He didn’t love me, he couldn’t... *Shaken voice* It-it was all just a means to get married."
    scene ch5sc02_091 with dissolve
    mc "Hey... Merida, it’s alright."
    mc "I’m not here to judge you. In fact, if what you’re saying is true, that makes you incredibly strong."
    mc "I doubt many women could have handled that at such a young age."
    scene ch5sc02_094 with dissolve
    qm "You’re quite good at this..."
    mc "At what?"
    qm "Making an old woman forget her age..."
    mct "I didn’t expect to find myself comforting the Queen today..."
    mct "Her scent is incredible... Vanilla-root with a hint of Dawnflower."
    qm "Uhh... How long have you been...? Your hand..."
    scene ch5sc02_095 with dissolve
    mc "Sorry, instinct."
    qm "It’s okay... I’m at fault too for allowing it."
    scene ch5sc02_096 with dissolve
    qm "It... It felt nice. But it can’t happen again, you understand?"
    scene ch5sc02_097 with dissolve
    mc "I understand. It would put you in a bad light if anyone saw."
    qm "..."
    qm "You'd best leave, it’s getting late. Your first escort duty is in two days."
    scene ch5sc02_096 with dissolve
    qm "Just announce yourself to the castle guards and they will send for Amelia."
    qm "I’ll talk to her beforehand and make sure she understands the need for a bodyguard."
    scene ch5sc02_097 with dissolve
    mc "Thank you. I’ll get out of your hair then."
    scene ch5sc02_096 with dissolve
    qm "And [mc]? Thank you, for talking to me... I did enjoy our chat."
    mc "Anytime, Merida."
    mc "I hope to be blessed enough to enjoy your company another time."
    qm "*Giggles* Heavens... you're a charmer! Yes, I'd like to talk to you again sometime."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ss45 with Dissolve(2)
    $ renpy.pause()
    scene ch5sc03_001 with Dissolve(2)
    $ renpy.pause(1.5)
    play music dark_5 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc03_002 with dissolve
    $ renpy.pause()
    scene ch5sc03_003 with dissolve
    $ renpy.pause()
    scene ch5sc03_004 with dissolve
    $ renpy.pause()
    scene ch5sc03_005 with dissolve
    $ renpy.pause()
    scene ch5sc03_006 with dissolve
    $ renpy.pause()
    scene ch5sc03_006a with dissolve
    $ renpy.pause()
    scene ch5sc03_007 with dissolve
    $ renpy.pause()
    scene ch5sc03_008 with dissolve
    $ renpy.pause()
    scene ch5sc03_009 with dissolve
    $ renpy.pause()
    scene ch5sc03_010 with dissolve
    fn "And that, my acolytes... is our lord's will."
    scene ch5sc03_011 with dissolve
    fn "His vision, our hands."
    fn "We will be the ones to bring about the new dawn."
    scene ch5sc03_010 with dissolve
    fn "No longer will we be looked down upon by our 'betters'."
    scene ch5sc03_011 with dissolve
    fn "No more poverty! No more injustice!"
    scene ch5sc03_010 with dissolve
    fn "In the new dawn, everything and everyone will be equal! HIS WILL!"
    evr "Our hands!"
    scene ch5sc03_012 with dissolve
    fn "Ahh, Sister Lux."
    fn "You’re just in time."
    fn "I’ve just finished bestowing our lord’s will upon these three."
    scene ch5sc03_013 with dissolve
    fn "They’re ready for judgment."
    scene ch5sc03_015 with dissolve
    lx "Mh-Hm. A fine selection, Brother Ember."
    lx "The lord will be pleased with your dedication."
    scene ch5sc03_014 with dissolve
    be "His will, my hands."
    scene ch5sc03_016 with dissolve
    lx "Are you three ready for enlightenment?"
    scene ch5sc03_017 with dissolve
    evr "His will, our hands."
    scene ch5sc03_016 with dissolve
    lx "Perfect."
    lx "Remember... When our lord rises, all those who have served him faithfully will be rewarded."
    scene ch5sc03_018 with dissolve
    lx "Your deepest desire... Your greatest wish... Everything will be granted to you."
    lx "But the road to our new world is long and not easily traveled."
    lx "It will take more devotion than you can possibly imagine."
    scene ch5sc03_016 with dissolve
    lx "Only those truly dedicated to our lord will live to see his new world."
    scene ch5sc03_017 with dissolve
    evr "We will do whatever it takes... His new world is worth any sacrifice."
    scene ch5sc03_016 with dissolve
    lx "Sacrifice... yes."
    scene ch5sc03_019 with dissolve
    lx "Mhm... his will is strong."
    lx "You will serve our lord perfectly. He has great things in store for you."
    scene ch5sc03_020 with dissolve
    lx "Let’s see..."
    lx "A flower in it's bloom, an unsoiled beauty."
    lx "Hmmh... Your will is not fully cemented. Look at me."
    scene ch5sc03_021 with dissolve
    lx "You’re full of anger... A deep rooted, burning desire for vengeance."
    lx "Continue to serve faithfully and you will have your vengeance."
    scene ch5sc03_020 with dissolve
    fma "*Nods*"
    scene ch5sc03_022 with dissolve
    lx "Hmmh..."
    lx "You don’t have the will of fire within you."
    scene ch5sc03_023 with dissolve
    ac "What do you mean? I-... I want to serve our lord."
    lx "No. Our lord won’t accept a flickering flame..."
    ac "Please! There must be something I can do to earn it, to prove it?"
    scene ch5sc03_024 with dissolve
    lx "There is one thing you could do to serve our lord..."
    ac "Anything! Please! I don’t have anywhere else to go."
    scene ch5sc03_025 with dissolve
    lx "Perfect, our lord will be pleased."
    lx "Now, please remove your robes and ascend the altar."
    scene ch5sc03_023 with dissolve
    ac "M-My robes?"
    ac "I-... I-"
    scene ch5sc03_024 with dissolve
    lx "Yes. You will present yourself before our lord as you were made."
    scene ch5sc03_026 with dissolve
    "The acolyte undresses nervously then climbs the altar."
    "The others watch attentively, following his every movement."

    scene black with dissolve
    scene ch5sc03_027 with dissolve
    #play music dark_5 fadein 1.0
    #stop music fadeout 1.0
    ac "I-Is this good?"
    lx "Yes, our lord will be pleased by your sacrifice."
    ac "S-Sacrifice? What?"
    scene ch5sc03_028 with dissolve
    lx "Acolytes."
    be "I’ll leave you to it, Sister Lux."
    scene ch5sc03_029 with dissolve
    with vpunch
    ac "H-Hey! What are you guys doing?! L-Let go of me!"
    lx "Shh... They are only doing our lord's will."
    lx "It will all be over soon..."
    scene ch5sc03_030 with dissolve
    ac "{b}GUYS!!{/b} Do something! She’s lost her mind!"
    with vpunch
    "The acolytes tighten their grasp on him as he panics."
    lx "My Lord, he who shall bring forth the new dawn upon this accursed world."
    scene ch5sc03_031 with dissolve
    lx "He who will wash away all suffering. He who shall judge all those who are unjust."
    lx "My Lord, you who were born in flames, please accept this offering!"
    lx "Purify this wretched soul in your everburning flames!"
    scene ch5sc03_032 with dissolve
    with vpunch
    $ renpy.pause(1)
    with vpunch
    $ renpy.pause()
    scene ch5sc03_033 with dissolve
    $ renpy.pause()
    ac "*Groans in anguish* Hhrhhck-Hrkrh..."
    scene ch5sc03_034 with dissolve
    #play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    lx "Take him to the cleansing chamber below and prepare him for the pyre."
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    ac "As you command, Sister."
    scene ch5sc03_035 with dissolve
    $ renpy.pause()
    scene ch5sc03_036 with dissolve
    $ renpy.pause()
    scene ch5sc03_037 with dissolve
    $ renpy.pause()
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc03_038 with Dissolve(2)
    $ renpy.pause()
    scene ch5sc03_039 with dissolve
    $ renpy.pause()
    scene ch5sc03_040 with dissolve
    $ renpy.pause()
    scene ch5sc03_041 with dissolve
    #####ANIMATION#####
    show rin_01 with fade
    $ renpy.pause(1, hard=True)
    $ renpy.pause()
    ri "..."
    scene ch5sc03_042 with dissolve
    $ renpy.pause()
    scene ch5sc03_043 with dissolve
    $ renpy.pause()
    scene ch5sc03_044 with dissolve
    $ renpy.pause()
    scene ch5sc03_045 with dissolve
    $ renpy.pause()
    scene ch5sc03_046 with dissolve
    $ renpy.pause()
    scene ch5sc03_047 with dissolve
    $ renpy.pause()
    scene ch5sc03_048 with dissolve
    $ renpy.pause()
    scene ch5sc03_049 with dissolve
    $ renpy.pause()
    scene ch5sc03_050 with dissolve
    $ renpy.pause()
    scene ch5sc03_051 with dissolve
    $ renpy.pause()
    scene ch5sc03_052 with dissolve
    $ renpy.pause()
    scene ch5sc03_053 with dissolve
    $ renpy.pause()
    scene ch5sc03_054 with dissolve
    $ renpy.pause()
    scene ch5sc03_055 with dissolve
    $ renpy.pause()
    scene ch5sc03_056 with dissolve
    $ renpy.pause()
    scene ch5sc03_057 with dissolve
    $ renpy.pause()
    scene ch5sc03_058 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1)
    scene ch5sc03_041 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1)
    scene ch5sc03_059 with dissolve
    $ renpy.pause()
    scene ch5sc03_061 with dissolve
    $ renpy.pause()
    scene ch5sc03_062 with dissolve
    $ renpy.pause()
    scene black with Dissolve(2)
    scene ch5sc03_041 with Dissolve(2)
    ri "..."
    scene ch5sc03_040 with dissolve
    ri "....."
    scene black with Dissolve(2)
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc03_063 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    el "Okay guys, I’m heading home for the day!"
    scene ch5sc03_064 with dissolve
    ml "Miss Eliza, do you need anyone to walk you home?"
    scene ch5sc03_064a with dissolve
    el "I appreciate that Milton, but I’ll manage. I’m going straight to the tavern."
    el "I want to make sure they keep a warm meal on hand for [mc]."
    scene ch5sc03_064b with dissolve
    sy "*Busy* Take care, Eliza! Make sure it's a big meal!"
    sy "The royals will surely have left him famished! They can be a lot to deal with!"
    el "You think so? Would they really work him that hard on his first day?"
    scene ch5sc03_064c with dissolve
    br "Aye! Hah! Surely the lad will be exhausted! He will be begging for my old-lady quests soon enough!"
    sy "*Laughing*"
    ml "*Chuckles*"
    scene ch5sc03_064d with dissolve
    el "Keep blowing smoke out your ass and I’ll make sure those are the only quests you get!"
    br "*Nervous* Ye wouldn’t do me like that, would ye lass? Ye know I was jesting!"
    el "Byyyeee!"
    scene black with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc03_065 with Dissolve(1.5)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    elt "[mc] is quite late today..."
    elt "I suppose the major contract we got is keeping [mc] busy."
    scene ch5sc03_066 with dissolve
    elt "I can’t imagine meeting the royal family! Let alone working for them..."
    elt "One thing is for sure... [mc] won’t be too thrilled. He hates socializing and nobles."
    scene ch5sc03_067 with dissolve
    elt "*Giggling* Heh-heh! I can just imagine the look on his face when he realized what this contract was!"
    scene ch5sc03_068 with dissolve
    elt "It’ll be good for him, though. He'll definitely benefit from socializing!"
    elt "Besides, a contract this huge will help the guild tremendously."
    scene ch5sc03_065 with dissolve
    elt "And spending time with the royal family could lead to them becoming allies."
    elt "Or at the very least making some valuable connections."
    scene ch5sc03_066 with dissolve
    elt "I'd better get to the tavern and make sure the innkeeper keeps a juicy roast warm for [mc]."
    scene ch5sc03_068 with dissolve
    elt "He’s been taking care of me so attentively, it’s time I take care of him."
    scene ch5sc03_069 with dissolve
    elt "Hmh... Maybe I could draw a hot bath for him? And maybe follow it with a deep massage?"
    elt "Yes, he'll definitely like that! He hasn't been able to properly relax since he got back."
    ##########
    if samarah_alive == True:
        scene ch5sc03_070 with dissolve
        sl "Eliza?"
        elt "That voice... Selena?!"
        scene ch5sc03_071 with dissolve
        elt "What in the five hells is she doing here?"
        elt "Ugh! Whatever..."
        scene ch5sc03_072 with dissolve
        sl "..."
        scene ch5sc03_073 with dissolve
        sl "Eliza, please? Can we talk?"
        scene ch5sc03_074 with dissolve
        el "I have nothing to say to you."
        scene ch5sc03_073 with dissolve
        sl "That’s fine. You don’t have to say anything, but please... hear me out?"
        scene ch5sc03_075 with dissolve
        sl "Come, we can talk in private back here."
        elt "After everything she’s put us through, she has the nerve to assume I’m willing to hear her out?"
        scene ch5sc03_076 with dissolve
        elt "Gods! She pisses me off!"
        elt "..."
        scene ch5sc03_077 with dissolve
        elt "Her-... Neck, looks so inviting..."
        elt "No... *Inhales deeply* Control..."
        scene ch5sc03_078 with dissolve
        elt "This had better be good... I have to get home and prepare for [mc]."
        scene ch5sc03_079 with dissolve
        el "Okay, this is far enough. Start talking."
        scene ch5sc03_080 with dissolve
        sl "..."
        scene ch5sc03_081 with dissolve
        sl "I’m-... I’m sorry, okay?"
        scene ch5sc03_082 with dissolve
        sl "You have to understand. Taron, he-... he had my sister!"
        sl "When he asked me to smooch up to two strangers in return for freeing Samarah..."
        scene ch5sc03_081 with dissolve
        sl "It wasn’t a hard decision to make at that moment."
        sl "At first, all he wanted was for me to get close to the two of you and report back to him."
        scene ch5sc03_082 with dissolve
        sl "Then he made me lure you away from [mc]. He said that he just wanted to talk to you..."
        sl "But clearly that was a lie, as we both found out..."
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        scene ch5sc03_083 with dissolve
        play music forestnight_3 fadein 1.0
        #stop music fadeout 1.0
        with vpunch
        el "*Raised voice* Wanting to protect your sister I get, but why not come clean to us? Why betray us!?"
        el "If only you had told us! We could've helped you break out your sister!"
        el "Instead you left me to suffer in that cell!"
        scene ch5sc03_080 with dissolve
        sl "..."
        scene ch5sc03_081 with dissolve
        sl "I had to..."
        sl "Taron is the one who let me in to see you."
        scene ch5sc03_082 with dissolve
        sl "I couldn’t let him hear me trying to comfort you... He was right outside the door."
        sl "I had to keep playing the part."
        sl "I needed to guarantee that he'd keep up his end and free my sister!"
        scene ch5sc03_083 with dissolve
        el "As long as your sister got free, it didn’t matter who paid the price... right?"
        el "Even if your friends were being hurt, potentially about to die, that didn't matter to you!?"
        scene ch5sc03_084 with dissolve
        sl "Eliza, wouldn’t you have done the same thing to save [mc]?"
        el "..."
        sl "I’m sure you would! You'd do anything for [mc]!"
        sl "I’ve seen how strongly you feel about him."
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        sl "[mc] he would-"
        play music darknight_4 fadein 1.0
        #stop music fadeout 1.0
        scene ch5sc03_085 with dissolve
        with vpunch
        el "Shut up! Don’t you dare mention his name!"
        el "Do you have any clue what you’ve put him through?!"
        scene ch5sc03_086 with dissolve
        el "How much he has had to endure for me?!"
        el "Forget about the pain you put me through, losing my ability to walk... that I can deal with."
        scene ch5sc03_087 with dissolve
        sl "Eliza! Calm down... you’re acting crazy!"
        sl "I just want to apologize!"
        scene ch5sc03_085 with dissolve
        with vpunch
        el "I’m acting crazy?!"
        el "You have some nerve! You really piss me off!"
        scene ch5sc03_086 with dissolve
        with vpunch
        el "{b}FINE!{/b} You know what? I’ll forgive you."
        el "{b}HAPPY?!{/b} Now leave me the fuck alone!"
        scene ch5sc03_088 with dissolve
        sl "Geez! You don’t have to act like that, I’m being kind to you... I'm trying to make amends."
        scene ch5sc03_089 with dissolve
        sl "We’ll talk another time, once you’ve come to your senses."
        scene ch5sc03_090 with dissolve
        with vpunch
        sl "Argh!! Let go!"
        sl "What are you doing, you crazy bitch!?"
        scene ch5sc03_091 with dissolve
        el "There won’t be another time for you."
        el "You see... I can forgive you for putting me in harm's way."
        scene ch5sc03_092 with dissolve
        sl "You’ve lost your mind! Release me!"
        scene ch5sc03_091 with dissolve
        el "But there is one thing... that I simply cannot forgive."
        el "Betraying [mc]... Hurting him... That is something I won’t forgive."
        scene ch5sc03_092 with dissolve
        sl "Let me go you bitch!!"
        scene ch5sc03_093 with dissolve
        el "*Hissing* Hhhrrh!"
        scene ch5sc03_094 with dissolve
        with vpunch
        sl "*Groans* Aiiiyhh! {b}AHH!{/b}"
        scene ch5sc03_095 with dissolve
        el "*Sucks intensely* Mhhnm..."
        elt "Mhmm... Can’t stop... So... Delicious..."
        scene ch5sc03_096 with dissolve
        elt "More! Hhrrhh... Her blood is so warm... Mhmm."
        "As Eliza gorges on her blood, Selena begins to fall unconscious."
        scene black with Dissolve(1)
        scene ch5sc03_095a with Dissolve(1)
        mc "Eliza. Stop..."
        elt "[mc]?"
        mc "Focus on my voice... Find your happy place."
        mc "Any memory that gives you a warm feeling in your belly. Latch on to that."
        elt "I-... I just wanted her to be quiet..."
        mc "Release her before you become... that which you fear the most."
        mc "Don't let her be the reason you fail to control your urges."
        elt "He's right- I won't let her ruin my life... She's not worth it."
        scene black with Dissolve(1)
        scene ch5sc03_096 with Dissolve(1)
        $ renpy.pause(1.5)
        scene ch5sc03_097 with dissolve
        $ renpy.pause(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        scene ch5sc03_098 with dissolve
        play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        el "AahHhh..."
        scene ch5sc03_099 with dissolve
        elt "I did it! I stopped!"
        scene ch5sc03_100 with dissolve
        elt "She finally stopped talking!"
        scene ch5sc03_101 with dissolve
        el "Huh?"
        scene ch5sc03_102 with dissolve
        elt "Why isn’t she getting up?"
        elt "Don't tell me-... But I stopped! Is she?"
        elt "No... No, no-no-no!"
        elt "I... I didn’t do this? I-I can’t have!"
        elt "I just wanted to scare her! She got me so angry!"
        elt "*Trembling* I couldn’t stop! No-no-no-no! Why am I like this?!"
        scene ch5sc03_102a with dissolve
        sl "*Groans* Hnngh? W-What?"
        sl "*Groans* My head is pounding like I was trambled by a herd of pigs..."
        scene ch5sc03_102 with dissolve
        elt "She's alive!! Oh, thank the heavens!"
        elt "I didn't kill her! I actually stopped myself in time!"
        scene ch5sc03_102a with dissolve
        sl "*Groans* Eliza? You-... you bit me?!"
        scene ch5sc03_102b with dissolve
        el "I did. And this will be your only warning... Stay away from us."
        el "You finally have your sister back. Go and make a life with her. Far from here."
        el "I don't want to see you in the capital again..."
        el "I don't want you trying to weasel your way back into our lives..."
        el "I don't trust you... Leave, get out of here!"
        scene ch5sc03_102c with dissolve
        el "I mean it, Selena. Leave Luxenford and never return."
        sl "I got the message, loud and clear... hmph."
        slt "Bitch..."
        elt "Cow..."
        scene ch5sc03_102d with dissolve
        elt "*Sighs heavily* I-... I almost killed her, that could have gone so horribly wrong."
        elt "I keep putting those around me in danger... Even if I don't like Selena, she doesn't deserve to die."
        elt "I may have been able to stop this time... But what about next time?"
        elt "What if I really hurt someone or, divines forbid, kill someone!"
        scene black with Dissolve(1)
        "An hour passes by..."
        scene ch5sc03_102d with dissolve
        elt "I-... I'm a freak."
        scene ch5sc03_102e with dissolve
        el "[mc]? ..."
        el "*Cracked voice* I’m a monster! A hideous, disgusting, blood-sucking monster!"
        mc "Hey... It’s alright. Everything is going to be fine."
        mc "What happened?"
        scene ch5sc03_102f with dissolve
        el "*Cracked voice* S-Selena... I attacked her!"
        el "*Cracked voice* She wanted to talk but things escalated... I-... lost my temper."
        mc "Hey... It's okay. I don't see a body anywhere. Is it safe to assume you managed to control your hunger?"
        el "Y-Yes... I let her go. But I still attacked her like some hideous freak who can't control herself!"
        mc "The last thing you are is a freak. You did well."
        mc "Let’s get you home and into bed..."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(1.5)

    else:
        scene ch5sc03_070 with dissolve
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        elt "Huh? Wait... That’s!"
        elt "She has some nerve showing herself in this city after what she’s done."
        play music darknight_4 fadein 1.0
        #stop music fadeout 1.0
        scene ch5sc03_075 with dissolve
        elt "[mc] may have killed her sister as punishment, but he said it was up to me to judge Selena."
        elt "I guess judgment day has finally arrived."
        scene ch5sc03_076 with dissolve
        elt "Mhm. Her neck looks juicy..."
        scene ch5sc03_077 with dissolve
        elt "I can literally smell the warm blood coursing through her veins..."
        scene ch5sc03_078 with dissolve
        elt "Why the fuck would she even stick around? Nobody wants her here."
        elt "I bet she's trying to squirm her way into [mc]'s good graces. Whatever... she has this coming."
        scene ch5sc03_082 with dissolve
        sl "E-Eliza? What-... Why are you here?"
        scene ch5sc03_083 with dissolve
        el "I live at the nearby tavern, as you well know. The more interesting question would be..."
        el "Why in the five hells would you still be here?"
        el "You do realize there’s a whole fucking world out there for you to trick people in?"
        scene ch5sc03_084 with dissolve
        sl "Eliza... Hear me out. I know I wronged you and [mc], okay?"
        sl "I didn’t intend for any of that to happen, but what was I to do? Taron had my sister."
        sl "Was I supposed to choose two strangers over my own blood?"
        scene ch5sc03_083 with dissolve
        el "You could’ve told us! You could have trusted us to help free her."
        scene ch5sc03_087 with dissolve
        sl "Are you kidding? You’ve met Taron! There’s no way I was going to gamble with my sisters life!"
        scene ch5sc03_088 with dissolve
        sl "Ugh, you wouldn’t understand... You’re an only child."
        scene ch5sc03_083 with dissolve
        with vpunch
        el "Of course I understand! It’s called fucking EMPATHY!"
        scene ch5sc03_087 with dissolve
        sl "Okay, okay... Geez, Eliza! Settle down... As for why I’m here-"
        scene ch5sc03_082 with dissolve
        sl "I’ve found a way to bring her back. To bring Samarah back."
        scene ch5sc03_081 with dissolve
        sl "I just need [mc]’s help to do it."
        scene ch5sc03_083 with dissolve
        el "The fuck you do?!"
        el "Do you honestly think you can have it all after what you put us through?!"
        scene ch5sc03_084 with dissolve
        elt "Gods! She makes my blood boil!"
        scene ch5sc03_088 with dissolve
        sl "You need to check yourself. You’re acting like a total bitch."
        sl "Didn’t you just preach to me about empathy? Then be happy for me!"
        scene ch5sc03_089 with dissolve
        sl "You know what? Forget it. You’re being petty..."
        scene ch5sc03_084 with dissolve
        elt "..."
        scene ch5sc03_085 with dissolve
        el "You really think you’ll just get to walk away?"
        el "After all the trauma and pain you’ve caused?"
        scene ch5sc03_086 with dissolve
        el "You don't even recognize the months... {b}MONTHS{/b} of torment you caused me and [mc]!"
        el "All because you were so selfish and wouldn’t trust us!"
        scene ch5sc03_089 with dissolve
        sl "Eliza, you’re acting crazy! We can settle this another time-"
        scene ch5sc03_086 with dissolve
        with vpunch
        el "{b}BITCH!{/b} I’m settling this now!"
        scene ch5sc03_090 with dissolve
        with vpunch
        sl "{b}ARGH!!{/b} Let me go, you psycho!"
        scene ch5sc03_091 with dissolve
        el "You’re not going anywhere..."
        el "It's time you felt a fraction of the pain you've caused us."
        scene ch5sc03_092 with dissolve
        sl "Y-Your eyes?! You’re a freak!"
        scene ch5sc03_091 with dissolve
        el "You have no idea... I’m going to enjoy this!"
        scene ch5sc03_093 with dissolve
        el "*Hissing* Hrrhhrhh!"
        scene ch5sc03_094 with dissolve
        with vpunch
        sl "*Painful Yelp* Aiiiigh!"
        scene ch5sc03_095 with dissolve
        elt "Mhm! I was right... She is delicious!"
        elt "I can’t let her get away with what she’s done... I won’t forgive her for betraying [mc]."
        elt "This should scare her enough to make her never return..."
        scene ch5sc03_096 with dissolve
        elt "Mmhmm... So warm..."
        "Selena’s pulse weakens with every drop of blood drained."
        scene ch5sc03_097 with dissolve
        with vpunch
        "Grabbing her head forcefully, Eliza continues sucking eagerly."
        scene ch5sc03_098 with dissolve
        el "Ahhh! More! Give me more!!"
        scene ch5sc03_097 with dissolve
        with vpunch
        el "Mmhmm!"
        scene ch5sc03_098 with dissolve
        $ renpy.pause(1.5)
        scene ch5sc03_099 with dissolve
        $ renpy.pause(1.5)
        scene ch5sc03_100 with dissolve
        elt "That was... exhilarating!"
        scene ch5sc03_101 with dissolve
        elt "C’mon, get up... I want more."
        elt "Maybe I was a little eager..."
        elt "Dead?"
        scene ch5sc03_102 with dissolve
        elt "Wait... I killed her? I killed Selena?!"
        elt "F-Fuck! No! No-no-no! What do I do?"
        elt "Even if she deserved to feel pain..."
        scene ch5sc03_103 with dissolve
        elt "I just wanted to scare her! Make her regret her choices... She got me so angry!"
        elt "I wanted to hurt her... But-..."
        elt "I-... I killed her! And... I enjoyed it?!"
        scene ch5sc03_104 with dissolve
        elt "*Trembling* I couldn’t stop! No-no-no-no! Why am I like this?! I’m a killer!"
        elt "*Trembling* She called me a freak... And she’s right."
        elt "*Trembling* How can I claim to be a good person? A decent person?"
        with vpunch
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        elt "*Trembling* I’m-... I’m not even human anymore! I’m a disgusting monster!"
        scene black with Dissolve(1)
        "An hour passes by..."
        play music forestnight_3 fadein 1.0
        #stop music fadeout 1.0
        scene ch5sc03_105 with Dissolve(1)
        $ renpy.pause(1)
        scene ch5sc03_106 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_107 with dissolve
        el "[mc]? ... Don't look at me!"
        el "I’m a monster! A hideous, disgusting, blood-sucking monster!"
        scene ch5sc03_106 with dissolve
        mct "She killed Selena? Hmph... Can’t say she didn’t have it coming."
        mc "Hey... It’s alright. Everything is going to be fine."
        ####Choice####
        menu:
            "You didn’t mean to kill her. ({color=#87e1fa}Light Path{/color})":
                scene ch5sc03_106 with dissolve
                $ light += 3
                "{b}{color=#87e1fa}Light Morality{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                mc "I know you didn’t intend for her to die. You’re still learning to control your bloodlust."
                mc "Besides, Selena wasn’t exactly innocent."
                scene ch5sc03_108 with dissolve
                el "I really didn’t! I just wanted her to feel some of the pain she has caused..."
                el "She just got me so angry! In the end, I couldn’t forgive her for hurting you."

            "You did me a favor. ({color=#f00}Dark Path{/color})":
                scene ch5sc03_106 with dissolve
                $ dark += 3
                "{b}{color=#f00}Dark Morality{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                $ el_dark = True
                mc "You did me a favor by killing her. You saved me the trouble of doing it myself."
                mc "Thank you, Eliza. I knew I could count on you."
                $ eldark += 1
                scene ch5sc03_108 with dissolve
                el "Always... I'll do anything for you."

        scene ch5sc03_106 with dissolve
        mc "C'mon let’s get you home and into bed..."
        mc "We’ll leave her for the guards to find. They’ll just assume it was a mugging."
        scene ch5sc03_109 with dissolve
        el "O-Okay... How did you know where I was?"
        scene ch5sc03_110 with dissolve
        mc "I picked up your scent as I was about to turn for the tavern, and I thought I should investigate."
        el "I’m glad you did, I-... I don’t know what I would’ve done..."
        scene ch5sc03_111 with dissolve
        mc "We’ll talk when we get to our room."
        el "Are you... mad at me?"
        mc "..."
        el "I’m sorry..."
        scene ch5sc03_112 with dissolve
        $ renpy.pause()
        scene black with Dissolve(2)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0


    if irene_alive == True:
        scene ir1 with dissolve
        play music explore_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause()
        scene black with dissolve
        scene ir_ani1 with dissolve
        $ renpy.pause(3, hard=True)
        scene black with dissolve
        scene ir_ani2 with dissolve
        $ renpy.pause(1)
        irt "Hmm."
        irt "Interesting..."
        irt "I knew he was heading to the capital... but I didn't imagine I'd actually see him again."
        irt "I wonder... would he recognize me? I had to change my hair after leaving Raden's legion."
        irt "[mc]... you spared me..."
        irt "*Snickers* You're quite handsome..."
        irt "*Sighs* Sadly there's no time for games... not even the pleasurable kind."
        irt "This is my initiation test for {b}the society{/b} after all, I need to find my target and... eliminate them."
        irt "How hard can it be? A {b}white-haired woman{/b} should stand out, even in a city as crowded as this."
        irt "I'll have to remain vigilant, according to my intel, she kills indiscriminately, even killed several of our sisters."
        irt "The society wanted her brought back in alive if possible, otherwise I am to at least get a decent amount of her blood."
        irt "Why they want something like that... who knows, it's not for me to ask questions if I want to be accepted as a member."
        irt "*Sighs* I better get to it... hopefully I get to run into you again someday... [mc]."
        scene black with Dissolve(2)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)


    else:
        scene black with dissolve

    scene ch5sc03_113 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    el "Say something... Please? You’ve been quiet the whole way back."
    mc "..."
    scene ch5sc03_114 with dissolve
    mc "It upsets me when you call yourself a monster."
    mc "Nothing could be further from the truth. If you’re a monster, then so am I."
    scene ch5sc03_115 with dissolve
    el "Don’t say that!! You’re not!"
    el "Neither of us are! We’re just trying our best and it doesn’t always go according to plan!"
    mc "*Chuckles*"
    scene ch5sc03_116 with dissolve
    el "Why are you laughing?! This isn’t funny!"
    scene ch5sc03_118 with dissolve
    mc "*Laughs* It’s a little funny. Getting you worked up to psych yourself out of a bad state seems to be effective."
    el "Hnnnrh!"
    scene ch5sc03_119 with dissolve
    mc "Don’t pout... Sylph says it promotes wrinkles."
    mc "Now, make some room. It's been quite the day and I’m about to pass out."
    scene black with Dissolve(1)
    "The two of you finish undressing and crawl under the covers together."
    scene ch5sc03_120 with Dissolve(1)
    el "This feels nice..."
    scene ch5sc03_121 with dissolve
    mc "I’m not much of a holy man but... damn, this surely feels like heaven."
    el "Mhm-Hm! It feels amazing having you back and sharing my bed again."
    scene ch5sc03_122 with dissolve
    with vpunch
    el "{b}OH NO!!{/b}"
    el "I completely forgot I was supposed to have a warm meal for you and-..."
    scene ch5sc03_123 with dissolve
    el "*Mumbles* Give you a massage."
    mc "*Chuckles* It’s alright. Right now, all I want is some rest."
    scene ch5sc03_124 with dissolve
    el "*Sigh* Okay... Tomorrow I’ll make sure I manage it! Goodnight!"
    scene ch5sc03_125 with dissolve
    mc "Looking forward to it. Sweet dreams."
    scene black with Dissolve(1)
    ##########
    if eliza_path == True:
        #####ANIMATION#####
        show el_sleep2 with fade
        $ renpy.pause(1, hard=True)
        $ renpy.pause()
        elt "It feels so good to have him laying next to me again..."
        elt "I really wanted to do something for him tonight, to show how much I appreciate him."
        elt "*Sigh* Why’d I have to lose control like that? It ruins everything..."
        elt "..."
        scene ch5sc03_125 with dissolve
        $ renpy.pause()
        scene ch5sc03_126 with dissolve
        $ renpy.pause()
        scene ch5sc03_127 with dissolve
        $ renpy.pause()
        scene ch5sc03_128 with dissolve
        el "..."
        mc "You’re staring."
        scene ch5sc03_129 with dissolve
        el "I’m gazing."
        scene ch5sc03_130 with dissolve
        mc "It’s creepy."
        scene ch5sc03_129 with dissolve
        el "It’s romantic!"
        scene ch5sc03_130 with dissolve
        el "..."
        scene ch5sc03_129 with dissolve
        el "Hey [mc]?"
        scene ch5sc03_130 with dissolve
        mc "Mhh?"
        scene ch5sc03_129 with dissolve
        el "Cuddle me?"
        scene ch5sc03_130 with dissolve
        mc "You know, I think we’re way past the point where you have to ask for cuddles."
        scene ch5sc03_129 with dissolve
        el "I know... Sometimes a girl likes a little confirmation, you know?"
        scene ch5sc03_131 with dissolve
        mc "Get over here kitten."
        "You lift the cover and Eliza scoots closer to you until her body is fully entwined with yours."
        mc "Better?"
        scene ch5sc03_132 with dissolve
        el "Much! This is exactly what I needed."
        el "I’ve really missed you, you know?"
        scene ch5sc03_133 with dissolve
        with vpunch
        mc "I’m not surprised, I’m pretty amazi-Mhhh-hhmhh-"
        el "*Giggling* {b}HUSH!{/b} I’m trying to compliment you!"
        scene ch5sc03_131 with dissolve
        mc "*Chuckles* Heh, alright-alright."
        mc "I’ve missed you too."
        scene ch5sc03_134 with dissolve
        mc "Come here, you cute little kitten!"
        scene ch5sc03_135 with dissolve
        with vpunch
        el "*Giggling* H-Hey! You can’t just muscle me around like that!"
        mc "Can’t I?"
        el "Noooo! You’re supposed to treat me like a lady!"
        el "Your brutish ways should be left at the door."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch5sc03_136 with dissolve
        with vpunch
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        el "{b}*Squeals*{/b} Aiiiyh!"
        mc "*Whispering* {size=-10}{b}Is that so? I thought you liked my brutish ways? How I take what I want.{/b}{/size}"
        scene ch5sc03_137 with dissolve
        el "*Soft moan* Nnnghhh... Nhooo..."
        "You begin caressing her soft, perky breast, which is firmly in your grasp."
        mc "*Whispering* {size=-10}{b}It sure sounds like you enjoy it when I claim what’s mine.{/b}{/size}"
        scene ch5sc03_138 with dissolve
        el "*Moans* Hnngh! Y-You’re imagining things! Y-Yeah... Mmh..."
        mc "*Squeezing firmly* Yeah, it must be my imagination."
        with vpunch
        el "*Moans* Ahhh! Ouhhmm!"
        mc "Sweet dreams kitten."
        el "Goodnight... My lion."
        scene ch5sc03_139 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_140 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_139 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_140 with dissolve
        $ renpy.pause(1)
        mc "*Whispering* This isn't sleeping..."
        el "*Soft moan* Mnnhh..."
        scene ch5sc03_139 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_140 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_139 with dissolve
        $ renpy.pause(1)
        scene ch5sc03_140 with dissolve
        $ renpy.pause(1)
        el "Mh-Hm... Just-... trying to get comfortable."
        scene ch5sc03_138 with dissolve
        el "Your thing keeps poking me."
        mc "Obviously, you keep rubbing against it."
        el "Mhm... Its your own fault. You still haven’t let go of my breast and it’s making me... horny."
        scene ch5sc03_141 with dissolve
        mc "Holding your breasts makes me sleep better."
        #####ANIMATION#####
        show el_sleep3 with fade
        $ renpy.pause(1, hard=True)
        $ renpy.pause()
        el "*Giggles* I’m sure it does! But I think this will make you sleep even better."
        mc "*Moans* Ahh... You’re a naughty little thing tonight."
        el "*Moans softly* Nnnhh... Mh-Hm! O-Only for you."
        el "Does this feel good? Mmhm... Me rubbing against you?"
        mc "Y-Yeah... You feel amazing."
        el "I wanted to take care of you tonight... Mmh... I suppose this is a way of doing just that."
        mc "Ahhhh... You won’t hear... Mh... any objections from me."
        el "Nnngh! G-Good! J-Just let me take care of you... Mmhm! Just-... Just rest."
        mc "I’m gonna-... Ahh!"
        el "Mhhh! That’s right... Cum on me. Let it out. Ahhnnh!"
        with vpunch
        scene ch5sc03_142 with dissolve
        with vpunch
        el "*Moans* Ahh-AHh! MMH!"
        el "*Panting* Hnnhh! From all the warmth I can feel on my lower back and ass..."
        el "I’m going to assume you thoroughly enjoyed that!"
        scene ch5sc03_143 with dissolve
        mc "I did... You always find a way to drain every last bit of energy within me."
        mc "*Sigh* I suppose you have to get up and wash now?"
        scene ch5sc03_142 with dissolve
        el "Nuh-uh. I’m sleepy! Bathing can wait til the morning."
        scene ch5sc03_143 with dissolve
        mc "But you’re covered in my cum?"
        scene ch5sc03_144 with dissolve
        el "Am I? I couldn’t tell... *Giggles*"
        el "I’ll wear it as a badge of ownership until the morning..."
        el "Just in case any frisky women should visit us in the night."
        scene ch5sc03_145 with dissolve
        mc "*Chuckles* You’re crazy... Goodnight then."
        scene ch5sc03_144 with dissolve
        el "*Whispering* {size=-10}{b}Crazy about you. Night-night.{/b}{/size}"
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0

    else:
        #####ANIMATION#####
        show el_sleep2 with fade
        $ renpy.pause(1, hard=True)
        $ renpy.pause()
        elt "It feels so good to have him laying next to me again..."
        elt "I really wanted to do something for him tonight to show how much I appreciate him."
        elt "*Sigh* Why’d I have to lose control like that? It ruins everything..."
        elt "..."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0

    ###########
    scene ch5sc03_146 with Dissolve(1.5)
    $ renpy.pause()
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc03_147 with dissolve
    $ renpy.pause(1.5)
    scene ch5sc03_148 with dissolve
    $ renpy.pause()
    al_t "Mhh, my bed looks so inviting!"
    scene ch5sc03_149 with dissolve
    al_t "I still can’t believe the professor was able to secure me a room at the Academy."
    al_t "Luna said the rooms here are expensive and sought after."
    scene ch5sc03_150 with dissolve
    al_t "She doesn’t have to worry about it since she has a room at the Mages guild."
    al_t "But the professor said she'd be mentoring me and making me her assistant."
    scene ch5sc03_151 with dissolve
    al_t "I'm honestly a little surprised she wants me for the position. I’m not exactly the best in our class."
    al_t "But she did say that I reminded her of herself when she first arrived here in the capital."
    scene ch5sc03_152 with dissolve
    al_t "Hnnghh!!"
    al_t "Heavens! I’ve been so busy with classes and helping Luna lately-"
    al_t "I haven’t had any time to relax at all."
    scene ch5sc03_153 with dissolve
    al_t "Mmh! This is definitely the best bed I’ve ever slept in!"
    al_t "I suppose that’s what expensive housing gets you."
    scene ch5sc03_154 with dissolve
    al_t "It’s rather exciting. Only one person gets selected for the assistant position each year."
    al_t "Professor Venetos seems to be very knowledgable. There’s a lot I can learn from working closely with her."
    scene ch5sc03_155 with dissolve
    al_t "*Relieved sigh* Hnnhhmh..."
    al_t "I finally managed to successfully brew my first potion!"
    scene ch5sc03_155a with dissolve
    $ renpy.pause()
    al_t "It's just a regular healing potion with some swift recovery enhancements added."
    scene ch5sc03_156 with dissolve
    al_t "But Venetos seemed happy with the results, so I must be making good progress."
    al_t "At least it boosts my confidence about choosing this path."
    scene ch5sc03_157 with dissolve
    al_t "This is my first real step towards being able to help [mc]."
    al_t "If I keep making good progress, I'll be able to accompany him on quests someday!"
    scene ch5sc03_158 with dissolve
    al_t "[mc]... *Giggles* How exciting that would be."
    al_t "I haven’t even told him about getting my own room yet..."
    scene ch5sc03_159 with dissolve
    al_t "Maybe... Mhh... Maybe he could visit me sometime."
    #####Choice#####
    menu:
        "Watch Alice solo scene.":
            scene ch5sc03_159 with dissolve
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            al_t "We’d be alone... Nnhghh... And I could-... Show him my bed."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            scene ch5sc03_160 with dissolve
            al_t "*Soft moan* Aahhngh... He could lay here with me... Holding me..."
            al_t "We’d be so close that we’d be feeling each other's racing pulses as we finally give in..."
            al_t "Finally our lips meet as we share a loving embrace! Nnngh! Our hands eagerly exploring each other! Mmnh!"
            scene ch5sc03_161 with dissolve
            al_t "Oh, [mc]! Mhm... Y-Yes... Touch me... Caress my tender breasts with your strong hands."
            al_t "Ahhh... We’re being so lewd! *Moans* Mmnh! [mc]... You’re touching me so indecently!"
            scene ch5sc03_162 with dissolve
            al_t "Y-Youre right... It’s time we stopped pretending... Ahhnn! T-Touch me!"
            al_t "Explore my naked body with your rough hands... with your warm lips..."
            scene ch5sc03_163 with dissolve
            al_t "Ohh... [mc]! You’re going to touch me? Your childhood friend... down there?"
            al_t "Ahhnnhh... You’re such a ravenous man! O-Okay... I’ll allow it."
            al_t "First we have to get rid of this pesky towel! Mnhh!"
            scene ch5sc03_164 with dissolve
            with vpunch
            al_t "Heavens yes! Touch my breasts like you own them! Ahhh! While you explore me!"
            al_t "Let me adjust for you..."
            scene ch5sc03_165 with dissolve
            al_t "Ahhnhh... How's that? Do you like my little flower?"
            al_t "It’s yours... We’ve waited our entire lives for this moment... for you to be one with me."
            scene ch5sc03_166 with dissolve
            al_t "Ohhh... [mc]... I’m already drenched... It’s your fault for touching me so lewdly!"
            al_t "Nnhhh... That means it's your job to take care of me."
            scene ch5sc03_167 with dissolve
            al_t "My flower is tingling for you... P-Please... Taste me! Do indecent things with your childhood friend!"
            scene ch5sc03_168 with dissolve
            with vpunch
            al_t "Ohhh!! [mc]! Heavens y-you’re eager! Aahhh!"
            #####ANIMATION#####
            show al_lewd1 with fade
            $ renpy.pause(1, hard=True)
            $ renpy.pause()
            al_t "*Moans* Nnhh!-Ahh! Oh my... You’re inside me! Mmhh!"
            al_t "I’ve dreamt of this moment for years... You touching me... Lusting for me..."
            al_t "Ahh, Yes! Take your childhood friend! Ravage me! Ahh-Ahh!"
            al_t "OHHH! I’M!! I’M-AHH!"
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            scene ch5sc03_168 with dissolve
            al_t "[mc]!! YES!! AHHH!"
            scene ch5sc03_169 with dissolve
            al_t "*Panting* Haaahh... Whew... That was wild."
            al_t "*Panting* It’s been a while since I had time for that. Guess my body finally had enough of waiting."
            scene ch5sc03_170 with dissolve
            al_t "It feels so tantalizing when I think about [mc] while touching myself like that..."
            al_t "I wonder if I’ll ever find the courage to ask him..."
            scene black with Dissolve(1.5)
            scene ch5sc03_171 with Dissolve(1)
            al_t "*Heavy sigh* That drained me... I'd better get some sleep."
            al_t "I wonder what elixir or potion I'll be working on next with professor Venetos?"
            scene black with Dissolve(2)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0

        "Skip Alice solo scene.":
            scene ch5sc03_155 with dissolve
            al_t "I'd better get some rest. I have a lot of classes tomorrow..."
            scene black with Dissolve(1)
            scene ch5sc03_171 with Dissolve(1)
            al_t "I hope I get a chance to show [mc] my room soon. I’m sure he'll be jealous! Heh-heh."
            al_t "I wonder what elixir or potion I'll be working on next with professor Venetos?"
            scene black with Dissolve(2)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0

    scene ch5sc03_172 with Dissolve(2)
    play music morning_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    pl "You miss him too, huh?"
    ki "Yeah... He's really become a major part of our lives over the past two moons, huh?"
    scene ch5sc03_173 with dissolve
    pl "He certainly has. Is that why you’re wearing the jacket he gave you back on Inmortui?"
    ki "N-No... I was-... I was cold."
    scene ch5sc03_174 with dissolve
    pl "Suuuure Sis!"
    pl "We’re close to Looter’s Bay here. I’ve been midnight dipping here often and it's never chilly at all."
    scene ch5sc03_175 with dissolve
    ki "W-Whatever... You’re talking crazy!"
    ki "Speaking of Looter’s Bay... What do you think we’ll be greeted with?"
    scene ch5sc03_176 with dissolve
    pl "Hmmhh..."
    pl "I imagine they'll most likely want our heads."
    scene ch5sc03_177 with dissolve
    ki "So we kill them all?"
    scene ch5sc03_176 with dissolve
    pl "It’s an option... But I think we have better alternatives available."
    pl "There’s probably still a lot of infighting going on. I don’t imagine they'll be organized yet."
    scene ch5sc03_177 with dissolve
    ki "So, what do you suggest?"
    scene ch5sc03_176 with dissolve
    pl "Stealth."
    pl "We’ll sneak into the bay and seek out anyone who is loyal to us."
    pl "Then we’ll meet up with Creed. We’ve known him since we were younglings."
    scene ch5sc03_178 with dissolve
    pl "We’ll appoint him as the new head of Looter’s Bay."
    pl "He’s already integral to the infrastructure, after all."
    scene ch5sc03_179 with dissolve
    with vpunch
    ki "{b}WE WHAT?!{/b}"
    ki "Pearl, have you lost your marbles? We can’t let that baby-chicken devouring tadpole lead!"
    pl "It’s our best option. He’s not as bad as the others, and with him leading Looter’s Bay..."
    scene ch5sc03_180 with dissolve
    pl "We’ll be free to do our own thing."
    pl "Such as... visiting Luxenford. Y'know... where [mc] lives?"
    scene ch5sc03_181 with dissolve
    ki "You’re right, we’ll make Creed head of Looter’s Bay!"
    scene ch5sc03_182 with dissolve
    pl "*Giggles* My, my! That was a quick change of heart."
    ki "Not another word out of you! Come on, we have a Bay to liberate!"
    scene black with Dissolve(2)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    stop music fadeout 1.0
    jump ch5sc2

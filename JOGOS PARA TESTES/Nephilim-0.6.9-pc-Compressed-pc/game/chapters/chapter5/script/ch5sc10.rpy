label ch5sc10:

    window hide dissolve
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (2.0)
    $ renpy.pause(1)
    scene ch4sc6 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve (1.5)
    scene ch5sc10_001 with Dissolve (1.5)
    da "Glad both of you could make it. I know the hour is late."
    sy "Hnngh... late? It’s the crack of dawn, Dalen!"
    br "Aye, this must be important since ye called both of us here so early."
    scene ch5sc10_002 with dissolve
    da "Usually, I’d wait for a more civilized hour to bring you up to speed, but time is of the essence."
    scene ch5sc10_003 with dissolve
    da "King Bennen has asked us for our help."
    scene ch5sc10_004 with dissolve
    sy "King Bennen?! Asking for our assistance?"
    sy "That’s never happened before."
    scene ch5sc10_005 with dissolve
    br "Hmh... Must be important then."
    scene ch5sc10_002 with dissolve
    da "Indeed."
    da "His Grace suspects there may soon be foul play at court."
    scene ch5sc10_003 with dissolve
    da "That's why he asked me to provide him with a bodyguard for the princess."
    scene ch5sc10_004 with dissolve
    sy "I was wondering about that."
    sy "They've always chosen a bodyguard from their royal guard previously."
    scene ch5sc10_006 with dissolve
    sy "But if they're worred that some retainers in the court can’t be trusted, it makes sense to get outside help."
    scene ch5sc10_005 with dissolve
    br "Aye, it does make sense. But then, what do they need us for? They've already hired [mc], so why do they want us too?"
    scene ch5sc10_002 with dissolve
    da "The princess's 20th name-day celebration is about to happen."
    da "And His Grace wishes to have extra security for it."
    scene ch5sc10_003 with dissolve
    da "The leaders of other nations, and even some nobles from within Luxeron, have been pressuring the crown because-"
    scene ch5sc10_006 with dissolve
    sy "Because the Princess isn't married, and she’s in her prime."
    sy "Whoever gains her hand, will rule after Bennen."
    scene ch5sc10_005 with dissolve
    br "Hmh... That sounds like an awful amount of pressure t' put on a young lass."
    scene ch5sc10_002 with dissolve
    da "It is. Usually, the parents arrange such a marriage in advance."
    da "Unfortunately, the princess has been resisting."
    scene ch5sc10_003 with dissolve
    da "Traditionally, her betrothal should have been announced two years ago. So, as you can imagine-"
    scene ch5sc10_004 with dissolve
    sy "-The other nations are growing impatient. And they might be tempted to try something desperate."
    scene ch5sc10_006 with dissolve
    sy "And stupid."
    scene ch5sc10_005 with dissolve
    br "But why ask for our help? Adventurers aren’t known for guarding nobles or their houses."
    scene ch5sc10_007 with dissolve
    da "That’s exactly why we’re perfect for the job. Major guilds are always expected to attend royal events."
    da "So, our presence will be unremarkable."
    da "No one will anticipate that we'll be there to watch for suspicious behavior."
    scene ch5sc10_008 with dissolve
    da "But to be effective, we need to start our preparations before the celebration begins."
    da "Which is why I summoned you both here at this hour,"
    da "Sylph, I need you to enclose the palace with your tracking dust."
    scene ch5sc10_009 with dissolve
    sy "You bet! I’ve been hoarding that stuff for ages."
    scene ch5sc10_008 with dissolve
    da "I also need you to magically seal off some of the less-used entrances into the palace."
    da "I doubt anyone will be brazen enough to try something, but the less exits we need to cover, the better."
    scene ch5sc10_009 with dissolve
    sy "Consider it done!"
    sy "Given how uncommon my people are in Luxeron, it's not likely that anyone will know how to break fairy seals."
    scene ch5sc10_007 with dissolve
    da "Borri, you’ve impressed everyone with your work ethic, and your ability to stubbornly tackle any quest."
    da "Which is why I want you to take point for this mission."
    scene ch5sc10_010 with dissolve
    br "Me... are ye sure? What about [mc]? The lad has a head fer these things."
    scene ch5sc10_011 with dissolve
    da "I’m sure. But [mc] is already assigned to guard the princess, so he's out."
    da "Trust me, Borri. I wouldn’t appoint you as leader if I didn’t think you have what it takes."
    scene ch5sc10_010 with dissolve
    br "Aye... just a little surprised is all."
    br "But... aye. Hah! Let’s do it!"
    scene ch5sc10_012 with dissolve
    br "Sylph! Ye heard Dalen. Get cracking on the tracking dust! I’ll find Milton and bring him up t' speed."
    br "He’ll be needed to arrange our equipment and logistics."
    scene ch5sc10_011 with dissolve
    da "Don’t forget to inform Eliza and [mc] as well."
    scene ch5sc10_010 with dissolve
    br "Aye. As soon as they’re back, I’ll be cracking t' whip! Hah!"
    scene black with Dissolve (2.0)
    $ renpy.pause(1)

    if eliza_relationship == True:
        scene ch5sc10_013 with Dissolve (1.5)
        $ renpy.pause()
        scene ch5sc10_014 with dissolve
        $ renpy.pause()
        scene ch5sc10_015 with dissolve
        $ renpy.pause()
        scene ch5sc10_016 with dissolve
        el "*Whimpers softly* Hnnhh..."
        elt "{i}Dawn... already? *Sigh*{/i}"
        scene ch5sc10_017 with dissolve
        elt "{i}[mc] is sleeping like a baby. Deservedly so. *Soft giggle* ...{/i}"
        elt "{i}He really did a wonderful job planning this date. I hope he knows how much I appreciate it.{/i}"
        scene ch5sc10_018 with dissolve
        elt "{i}*Mwah* I just want him to wake up so I can tell him how much I love him...{/i}"
        elt "{i}*Mwah* Mnhh... Maybe... No. That'd be crazy, right?{/i}"
        scene ch5sc10_019 with dissolve
        elt "{i}*Giggles softly* What if it wakes him up? He really liked it yesterday...{/i}"
        elt "{i}Besides... I’m his woman now.{/i}"
        scene ch5sc10_020 with dissolve
        elt "{i}Which means he'll have to get used to... feeding me. *Giggles*{/i}"
        elt "{i}*Snickers* I’m a big breakfast person!{/i}"
        scene black with Dissolve(1)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ch5sc10_021 with Dissolve(1)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mct "{i}Mnhh... Warm... Wet... Mnhh...{/i}"
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch5sc10_021 with Dissolve(1)
        $ renpy.pause(1)
        scene ch5sc10_022 with dissolve
        mc "*Moans* Mnhh... What are you... Hnnhh... up to?"
        scene el_date31 with dissolve
        $ renpy.pause()
        el "*Muffled moan* Ih’m... *Sucks* having bhreakfasst... Mhhn *Lick*"
        el "So... Mnhh, Ghoood! MNh! Hnh! *Suck*"
        $ renpy.pause()
        mc "*Moans* Damn... Mnhh... You’re relentless!"
        el "*Moans* Mnhh... Not shtoppingh. *Suck* Not until... Mhhh... you feed me... Hnngh! Every. Last. Droppph. Mnhh!"
        mc "*Moans* You little... Ahnhh ... she-devil. Mnhh. Eliza... I’m-"
        with vpunch
        el "*Sucks harder* Yes! MNhh... Fill my mouth! *Sucks* Mh! Fill me up! I want to taste your delicious cum! MH!"
        scene ch5sc10_023 with dissolve
        "The intensity of her sucking and the sound of her lustful moans leaves you no choice but to give her what she wants."
        scene ch5sc10_024 with dissolve
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        el "*Muffled* {b}MNh!! HNNGH!! HNH!!! AHMH!!{/b}"
        "She struggles to contain it all, not realizing how much you would have for her after resting."
        scene ch5sc10_025 with dissolve
        "After holding still for a few moments, she manages to swallow it all."
        el "*Moans* Mnhh... Yum. *Lick*"
        scene ch5sc10_026 with dissolve
        mc "What a way to wake up! *Chuckles*"
        scene ch5sc10_027 with dissolve
        el "Mnhh... *Lick* Tasty. *Lick* Hnnh."
        scene ch5sc10_026 with dissolve
        mc "You’re a little sex kitten..."
        scene ch5sc10_027 with dissolve
        el "Mnh-Mh... I’m {b}your{/b} little sex kitten. *Licks*"
        scene ch5sc10_028 with dissolve
        el "Mnhh... Happy with your wake up? *Licks* Mnhh..."
        mc "Happy doesn’t even begin to describe how you make me feel... Mnhh."
        scene ch5sc10_029 with dissolve
        el "*Giggles* Thank you for breakfast. It was delicious."
        mc "Is this what it'll be like waking up with you from now on? *Chuckles*"
        scene ch5sc10_028 with dissolve
        el "*Licks* You mean this?"
        el "Hmmhh... Yes! *Licks* This is exactly what you can expect."
        mc "Fuck... you can wake me up with that little mouth of yours any time you feel like it... mmh."
        scene ch5sc10_029 with dissolve
        el "*Giggles happily* I knew you'd never deny me breakfast!"
        el "C’mon... Let’s pack up and head back."
        el "I can’t wait to tell the others how amazing our new place is!"
        scene black with Dissolve(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)


    else:
        scene black with Dissolve(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)

    scene ch5sc10_030 with Dissolve (2)
    play music happy_1 fadein 1.0
    #stop music fadeout 1.0
    el "*Stretches* Hnnnghh!!"
    el "Alrighty! A new day is upon us! I feel like I’m ready to grab it by the balls, and make it my bitch!"
    mc "Heh... Someone’s in high spirits today."
    scene ch5sc10_031 with dissolve
    el "Uh-Huh! Of course I am. I feel amazing!"
    el "I’m purified! I don’t have any blood-cravings! And I’ve just spent an entire day and night alone with you! *Giggles*"
    scene ch5sc10_030 with dissolve
    el "Everything is perf-"
    mc "Don’t say it."
    scene ch5sc10_031 with dissolve
    el "Huh? Why not?"
    mc "Whenever someone says everything is perfect, that's when things always take a turn..."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc10_032 with dissolve
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    el "Huh, what’s that?!"
    mc "What?"
    scene ch5sc10_033 with dissolve
    el "Over there in the bushes. Something is rustling."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc10_034 with Dissolve(1.5)
    $ renpy.pause(1)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    el "Trouble! [mc], it’s Trouble! Look!"
    scene ch5sc10_035 with dissolve
    el "*High-pitched voice* Hiiiii girl! How’ve you been? *Checks fur* You look healthy."
    scene ch5sc10_036 with dissolve
    el "How did she know where to find us?"
    scene ch5sc10_035 with dissolve
    mc "She probably picked up our scent at the outskirts of the capital and tracked us here."
    el "Did you hear that, Trouble? [mc] also thinks you have the bestest nose any wolf could wish for! *Giggles*"
    trb "*Whines* Hnniiih, Hniihh."
    scene ch5sc10_037 with dissolve
    el "What’s wrong, girl? Are you hurt? [mc], something is wrong!"
    el "She's whining, but she doesn't look hurt?"
    scene ch5sc10_038 with dissolve
    mc "Let me have a look."
    mc "{color=#2bff8b}{b}*Animal communion*{/b}{/color} Hey, girl. What’s wrong? Are you hurt?"
    trb "*Whines* Hnniiih, Hniihh."
    mc "{color=#2bff8b}{b}*Animal communion*{/b}{/color} Oh. You were attacked? They have your companion? Yes, we'll come. Can you show us?"
    trb "*Whines* Hnniiih, Hniihh."
    scene ch5sc10_039 with dissolve
    el "What happened to her? Is she injured?"
    el "Please tell me she's okay!"
    scene ch5sc10_040 with dissolve
    mc "Her companion was caught in a poacher's trap. They were beating him when she rushed off to find us."
    el "......................."
    scene ch5sc10_041 with dissolve
    with vpunch
    el "We’re going. {b}NOW.{/b}"
    scene black with Dissolve(1.5)
    #play music tavern_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_042 with Dissolve(1.5)
    play music tavern_3 fadein 1.0
    #stop music fadeout 1.0
    aa "*Sighs* Flynn... it’s morning. Don’t you think you’d be better off getting some rest?"
    scene ch5sc10_043 with dissolve
    fy "*Groans* Do you know what life is? It’s like a great pair of tits."
    aa "*Scoffs* Okay?"
    fy "Great, most of the time. But it's bound to give you back problems now and again."
    scene ch5sc10_044 with dissolve
    aa "Are you talking about my tits, or your life?"
    fy "My life, Anna. Pay attention."
    scene ch5sc10_045 with dissolve
    aa "Right... *Drawn out sigh* So, tell me. What's weighing you down?"
    scene ch5sc10_046 with dissolve
    fy "Oh Anna... Where do I even begin?"
    fy "I’ve been tasked with capturing one of the most infamous and hardened criminals in Luxenford."
    scene ch5sc10_045 with dissolve
    aa "Oh? That sounds serious. What did they do?"
    scene ch5sc10_046 with dissolve
    fy "They’re a master-thief, Anna. The worst of the worst!"
    fy "They're not content with stealing trifles like gold or jewelry. No. They have a far more sinister agenda."
    scene ch5sc10_045 with dissolve
    aa "Like what? Are they kidnapping children?"
    scene ch5sc10_046 with dissolve
    fy "Panties, Anna. They’re stealing panties... used panties... from unsuspecting and innocent women!"
    scene ch5sc10_047 with dissolve
    aa "*Gasps mockingly* The horror! What are we to do when such an evil lurks amongst us?"
    scene ch5sc10_046 with dissolve
    fy "I know. It won't look good for the women of Luxenford, if I can’t bring this panty-sniffing scoundrel to justice."
    scene ch5sc10_045 with dissolve
    aa "Panty-sniffing? How do you know that?"
    scene ch5sc10_046 with dissolve
    fy "Educated guess, Anna. I’m a professional."
    scene ch5sc10_048 with dissolve
    aa "Then why are you sitting in here wallowing in self-pity, when there are women out there who need your help?"
    aa "Do you think the panty-sniffer will stop just because you wanted to take a break? How will the women of Luxenford react?"
    scene ch5sc10_046 with dissolve
    fy "*Sigh* I was up all night, running around and interviewing the victims. But I haven't found any solid clues."
    fy "I’m at a loss, Anna."
    scene ch5sc10_044 with dissolve
    aa "Hmh... I might be able to help."
    fy "Really? I’ll accept your tits- I mean, help!"
    scene ch5sc10_048 with dissolve
    aa "Right... So, since the thief is targeting panties, and mostly the used kind..."
    scene ch5sc10_049 with dissolve
    aa "You should probably investigate areas that are densely populated with women."
    scene ch5sc10_046 with dissolve
    fy "I’m liking where this is going!"
    scene ch5sc10_045 with dissolve
    aa "I’m thinking you should ask around in some of the established venues of... pleasure."
    scene ch5sc10_043 with dissolve
    fy "Oh! {b}OHH!{/b} I didn’t think of that! You’re a genius!"
    fy "But getting into the more prominent ones, like ‘The Velvet Pearl’, ‘Midnight’s Delights’, or ‘The Sheath and Sword’..."
    scene ch5sc10_044 with dissolve
    fy "It’s nigh impossible for a man without coin or status."
    scene ch5sc10_047 with dissolve
    aa "*Gasps mockingly* Flynn! And here I thought you were famous."
    fy "I will be! One day. Especially after I catch that good-for-nothing panty-thief!"
    scene ch5sc10_044 with dissolve
    aa "I might be able to help you get into ‘The Velvet Pearl.’ I know someone who works there."
    fy "Really? That’s the best news you’ve ever given me! Let’s go!"
    scene ch5sc10_049 with dissolve
    aa "Not so fast. You go home and rest. I'll talk to my friend later and see if she can get you in."
    scene ch5sc10_050 with dissolve
    fy "Some rest does sound good. I’ll see you later then, Anna. Thank you!"
    aa "Bye, bye!"
    scene black with Dissolve(1.5)
    #play music tavern_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_051 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    uk "Can you believe the bitch just took off?"
    uk1 "If ye hadn’t been so reckless, we could’ve gotten her too. Shame. Wolf fur prices have been pretty good lately."
    scene ch5sc10_052 with dissolve
    uk2 "At least we got the black one. His pelt is pristine."
    uk2 "I’m going to have wenches sucking my cock day and night with the coin that beast'll bring."
    scene ch5sc10_051 with dissolve
    uk1 "Hah! Spoken like a proper man!"
    uk1 "I’m going to be balls deep in the first wench I find!"
    uk "How about you two knuckleheads start skinning the hide and dressing the meat. We don’t wanna be out here all day."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch5sc10_053 with Dissolve(1)
    el "There they are! Look, those bastards have Trouble’s companion!"
    scene ch5sc10_054 with dissolve
    el "They’re just sitting there... laughing?"
    el "Ugh! They make my blood boil!"
    el "We have to save him."
    scene ch5sc10_055 with dissolve
    mc "Eliza..."
    scene ch5sc10_056 with dissolve
    el "What? The more time we waste-"
    scene ch5sc10_055 with dissolve
    mc "He’s already dead."
    scene ch5sc10_056 with dissolve
    el "No... I don’t accept that. I refuse to accept that!"
    scene ch5sc10_057 with dissolve
    trb "*Whimpers*"
    el "Don’t worry, girl. They’re going to pay for this."
    scene ch5sc10_058 with dissolve
    mc "From the amount of blood on the ground, they inflicted a lot of trauma before he died."
    mc "You stay here."
    scene ch5sc10_059 with dissolve
    mc "I’ll handle this."
    scene ch5sc10_060 with dissolve
    el "No."
    el "You stay."
    el "Trouble is family, so this is {b}personal.{/b}"
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc10_061 with dissolve
    mc "Make them suffer."
    scene ch5sc10_060 with dissolve
    el "You know I will."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch5sc10_062 with Dissolve(1)
    uk1 "I’m going to order the virgin special after this... I like my cock bloodied as they scream."
    uk2 "*Scoffs* You’re twisted. I prefer the older ones. The things they can do... worth every silver."
    uk1 "Hah! You don’t know what you’re missing out on. Young and tight is the best. They don’t know whether to scream or cry."
    scene ch5sc10_063 with dissolve
    with vpunch
    el "*Shouting* {b}Heeelp! Somebody, please help!{/b}"
    uk1 "Speaking of young and tight... What do we have here?"
    scene ch5sc10_064 with dissolve
    el "Help! *Out of breath* Can you... Can you guys help me? There's a wolf! C-Chasing me!"
    uk2 "You’ve come to the right place, miss. No wolves here. *Chuckles* Come, we’ll take care of you."
    uk1 "*Whispers* She’s mine. There’s nobody around for miles and I want to have some... fun."
    scene ch5sc10_065 with dissolve
    el "I’m so happy I ran into you guys. I thought I was done for! It had such sharp teeth!"
    uk2 "The feeling's mutual, believe me. Heh... right this way."
    scene ch5sc10_066 with dissolve
    uk1 "What’s a young thing like you doing out in the middle of the woods?"
    el "I was looking for something..."
    scene ch5sc10_067 with dissolve
    uk1 "If you follow me around this tree, I have something that will help calm you-"
    #play music darknight_4 fadein 1.0
    stop music fadeout 1.0
    scene ch5sc10_068
    with vpunch
    play music dark_3 fadein 1.0
    #stop music fadeout 1.0
    uk1 "Ghgh... Ggh..."
    "With a single punch, Eliza's fist penetrates the thug’s ringmail and skull."
    scene ch5sc10_069
    with vpunch
    uk2 "What the {b}FUCK?!{/b} John?! The bitch killed John!!"
    uk2 "{b}YOU’LL PAY FOR THIS, SLUT!!{/b}"
    scene ch5sc10_070 with dissolve
    uk2 "{b}I'm gonna slice you in half!{/b}"
    el "Oh? You want to play too? Don’t worry, I wasn’t planning on skipping you."
    scene ch5sc10_071
    with vpunch
    uk2 "{b}WHAT?! HOW THE FUCK DID YOU...?! FREAK!!{/b}"
    scene ch5sc10_072
    with vpunch
    uk2 "W-What?! S-She disappeared?!"
    scene ch5sc10_073
    with vpunch
    el "Surprise!"
    uk2 "What are you? Argh!!"
    scene ch5sc10_074
    "Holding him firmly, Eliza twists his neck slowly so that he feels every inch of movement."
    with vpunch
    uk2 "{b}ArghH!!!{/b} Stop! Stop!! We didn’t mean it! {b}ArgHH!!{/b}"
    scene ch5sc10_075 with dissolve
    el "Oh? You didn’t mean it when you told your buddy you wanted to fuck me bloody behind the tree?"
    el "And you didn't mean to torture the wolf instead of killing it and ending its misery?"
    el "No... But you still took your time tormenting and hurting it, didn't you?"
    scene ch5sc10_076 with dissolve
    uk2 "{b}Bitch!!{/b} How did you even...?! Arghh!! {b}STOP!{/b}"
    el "There, there. Shhh... I've heard there’s a special place in the five hells for people like you. Guess you’re about to find out."
    scene ch5sc10_077 with dissolve
    uk2 "Hrhgh-Hgh... HrRgGh..."
    scene ch5sc10_078 with dissolve
    #play music dark_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    el "..."
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc10_079 with dissolve
    with vpunch
    uk "John! Eddy?! What have you done?!"
    el "Sweet little ol' me? You can’t honestly believe a girl could do this?"
    scene ch5sc10_080 with dissolve
    el "And here I thought you guys were supposed to be scary, tough, wolf-killing, virgin-bloodfucking men?"
    scene ch5sc10_081
    with vpunch
    uk "I’m going to fuck your corpse into the ground for this!"
    el "Woah, woah... Why so hostile? I’m not even the one you should be worried about."
    uk "What the fuck are you talking abouuuu-"
    scene ch5sc10_082
    with vpunch
    uk "Hrhgh-Hgh! HrRgGh!"
    scene ch5sc10_083 with dissolve
    el "Told you. That’s who you should've been worried about."
    #play music dark_3 fadein 1.0
    stop music fadeout 1.0
    el "Good girl. At least we managed to avenge your companion."
    scene black with Dissolve(1)
    play music sad_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_052 with Dissolve(1)
    $ renpy.pause(1)
    scene ch5sc10_084 with dissolve
    $ renpy.pause(1)
    trb "*Licks gently* Hnniih... Hniih *Whimpers*"
    scene tb_1 with dissolve
    trb "*Howling in despair*"
    scene ch5sc10_084 with dissolve
    mc "Hey, girl. Let me try something, okay?"
    trb "*Whimpers* ..."
    scene ch5sc10_086 with dissolve
    mc "*Sighs heavily* It’s a long shot, but still worth a try."
    scene ch5sc10_087 with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch5sc10_088 with dissolve
    el "Right! Your healing ability! Will it work?"
    scene ch5sc10_089 with dissolve
    mc "Don’t get your hopes up. This guy has been dead for a while already. Chances are it won’t work."
    mc "My healing ability is limited. So far I’ve only used it to heal flesh wounds. This ... is much worse."
    scene ch5sc10_087 with dissolve
    mc "..."
    scene ch5sc10_086 with dissolve
    mc "*Exhales deeply* ..."
    el "Did it... Did it work?"
    mc "I’m sorry, Trouble. Your friend’s gone."
    scene ch5sc10_084 with dissolve
    trb "*Whimpers*"
    mc "C’mon, let’s give him a proper burial."
    scene black with Dissolve(1.5)
    "Trouble follows the two of you back to the campsite."
    #play music sad_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_090 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    el "It’s not fair. Why would they do this? Hmmgh."
    mc "Greed. Sadly, this isn’t my first encounter with poachers."
    mc "When I was younger, your father and I came across people like that every so often."
    scene ch5sc10_091 with dissolve
    el "Please tell me you erased them from existence."
    mc "I wish I could say that we did. But mostly, we left them alone. Oren didn’t want to leave a trail of bodies that could be tracked."
    scene ch5sc10_092 with dissolve
    el "I wish we could do something more for Trouble."
    mc "We could let her stay on our land. That way she'll stay out of reach of any other trappers."
    scene ch5sc10_093 with dissolve
    el "Wait, really!? That’s so sweet! I’d love for her to stay here!"
    mc "She can help keep unwanted guests such as poachers and bandits out of the area while we’re getting set up."
    scene ch5sc10_092 with dissolve
    el "Yay! We’re keeping her! *Giggles*"
    mc "She’s not a dog."
    scene ch5sc10_094 with dissolve
    el "Don’t listen to that brute, Trouble! You’re the best puppy anyone could wish for!"
    el "I’m gonna love you forever, and I’ll take care of you!"
    trb "*Whines happily* ..."
    scene ch5sc10_095 with dissolve
    mc "{color=#2bff8b}{b}*Animal communion*{/b}{/color} Okay, Trouble. Use this place as the center. A few miles in all directions from this point is our territory."
    mc "{color=#2bff8b}{b}*Animal communion*{/b}{/color} If you stay within it, you should be safe. We’ll come here regularly as we’re going to make it our home."
    trb "*Happy whimper* ..."
    mc "{color=#2bff8b}{b}*Animal communion*{/b}{/color} Good girl. We have to head back to the city now. Take care of this place until we return, okay?"
    scene ch5sc10_094 with dissolve
    el "Byeee sweetie! Don’t worry. We’ll come back soon, and I’ll make sure we bring a fat juicy steak with us!"
    trb "*Happy whimper* ..."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "When the two of you reach Luxenford, you split up. Eliza heads to the guild and you go to the tavern to get cleaned up."
    scene ch5sc10_096 with Dissolve(1.5)
    play music tavern_3 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}I’ll just wash off, have a bite, and then head to the guild.{/i}"
    scene ch5sc10_097 with dissolve
    mct "{i}Eliza sure was eager to get to the guild. I bet she’s excited to tell the others that the purification worked.{/i}"
    scene ch5sc10_098 with dissolve
    aa "There he is. The man of the hour, our very own casanova."
    scene ch5sc10_099 with dissolve
    mc "Oh hey, Anna. Casanova?"
    scene ch5sc10_100 with dissolve
    aa "Yeah, you know... Like in the romance novels you find in libraries?"
    scene ch5sc10_101 with dissolve
    mc "Afraid I’m not familiar with them."
    scene ch5sc10_100 with dissolve
    aa "I’ll summarize for you, then!"
    scene ch5sc10_102 with dissolve
    aa "The impossibly hot and mysterious guy takes the matchless beauty on a date."
    aa "The two of them aren’t seen until the following day, leaving their peers to wonder what happened..."
    scene ch5sc10_103 with dissolve
    aa "But we all know what happens when a hot guy and a beautiful girl spend time alone together."
    scene ch5sc10_104 with dissolve
    mc "*Chuckles* What?"
    scene ch5sc10_103 with dissolve
    with vpunch
    aa "*Whispers* Babies! They make lots and lots of babies!"
    scene ch5sc10_104 with dissolve
    mc "Right. You’ve clearly forgotten to take your mandatory break. *Chuckles* I’m heading to the baths."
    scene ch5sc10_105 with dissolve
    aa "Mhm-Hm... Was that an invitation? 'Cause I might just take you up on that."
    aa "My skin is tingling in anticipation of a good, deep... back scrub. *Giggles softly*"
    scene ch5sc10_099 with dissolve
    mc "Keep dreaming, Anna."
    aa "Oh, believe me, I will! *Snickers*"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "One bath later..."
    scene ch5sc10_106 with dissolve
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}That was just what I needed. Whoever invented baths... thank you.{/i}"
    mct "{i}I'm already looking forward to having our own place. We'll have to make sure to install a heated bath.{/i}"
    mct "{i}And we already have that small lake we discovered, too.{/i}"
    scene ch5sc10_107 with dissolve
    fr "......"
    fr "Uh-Uhhh-UhhHhhh..."
    scene ch5sc10_108 with dissolve
    fr "H-Hi..."
    scene ch5sc10_106 with dissolve
    mc "Hmh?"
    scene ch5sc10_109 with dissolve
    mc "Frida? What are you doing here?"
    fr "I-I... I-Uhh... Y-Your thing... Uh-"
    scene ch5sc10_110 with dissolve
    mc "Oh. My bad. I wasn't expecting anyone to be in my room."
    scene ch5sc10_108 with dissolve
    fr "S-Sorry... The Innkeeper said I could wait for you here."
    scene ch5sc10_111 with dissolve
    mc "Don’t apologize... I don’t mind."
    mc "You’re a friend, and you're welcome to visit whenever you want."
    fr "O-Okay... thank you."
    scene ch5sc10_112 with dissolve
    fr "Wait- R-Really? You’d really be okay with that?"
    mc "Yes, really."
    mc "If you ever need to take a break from the stress of the palace, you're welcome to hang out here."
    scene ch5sc10_113 with dissolve
    frt "{i}W-We’re standing so close... It’s really hot in here...{/i}"
    fr "*Mumbles* He’s so hot..."
    mc "Sorry, what? Did you say something?"
    scene ch5sc10_114 with dissolve
    with vpunch
    fr "Huh?! Uh! Uh... I-I said it’s hot in here."
    fr "I-I need to sit!"
    scene ch5sc10_115 with dissolve
    fr "Yes. Sitting is uh- good for your health!"
    mc "*Chuckles* Okay... Oh, did Amelia get you a new outfit?"
    scene ch5sc10_116 with dissolve
    fr "Oh, this? N-No. It’s nothing."
    fr "Just a regular outfit that I wear when I’m not on duty."
    ####Choice####
    menu:
        "Looks cute on you. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc10_116 with dissolve
            mc "I like it on you... You look cute."
            $ frida_trust += 2
            scene ch5sc10_117 with dissolve
            fr "T-Thank you."
            fr "That’s kind of you to say. I’m- I’m glad you like it."
            "Frida's trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch5sc10_116 with dissolve
            fr "It’s not often I get to wear my own clothes, but I enjoy it when I do."

        "Must be nice to change it up. ({color=#2bff8b}Friendship{/color})":
            scene ch5sc10_116 with dissolve
            mc "Ah, I see. Must feel nice as a change from your normal maid outfits."
            scene ch5sc10_117 with dissolve
            fr "Uh-Huh! I don't get to wear my own clothes often, but I like it when I do."

    scene ch5sc10_118 with dissolve
    mc "So, to what do I owe the pleasure of your visit? Did something happen at the palace?"
    scene ch5sc10_119 with dissolve
    fr "I’m here at Amelia’s request. She wanted me to deliver a letter to you."
    scene ch5sc10_118 with dissolve
    mc "A letter? Couldn’t she just have sent a courier with it?"
    scene ch5sc10_119 with dissolve
    fr "No... She’s never written a letter to anyone, and she felt it was too personal to risk anyone else opening it."
    fr "She spent hours in her study writing it."
    scene ch5sc10_118 with dissolve
    mc "Hours? Now I’m intrigued."
    mc "Maybe it's a secret assignment...?"
    scene ch5sc10_120 with dissolve
    fr "I don't know."
    fr "I'll admit, I'm curious about her first-ever handwritten letter, but I wouldn't breach her confidentiality."
    scene ch5sc10_121 with dissolve
    mc "I'd wager that most people would have read it."
    scene ch5sc10_120 with dissolve
    fr "I couldn’t do that to her."
    fr "After everything Amelia has done for me, I won’t break her trust."
    scene ch5sc10_121 with dissolve
    mc "You’re loyal to your friend."
    mc "That’s something I respect."
    scene ch5sc10_122 with dissolve
    fr "I don’t have much to my name, but loyalty to people I care about is something I value highly."
    fr "Something that can’t be bought. And no matter how poor I am, it’s something valuable that I can still provide."
    scene ch5sc10_121 with dissolve
    mc "That's a nice way of putting it. Am I also in the group of people you care about?"
    scene ch5sc10_120 with dissolve
    fr "*Nods* You are."
    scene ch5sc10_121 with dissolve
    fr "..."
    scene ch5sc10_122
    fr "The letter! Y-You'd better read the letter!"
    scene ch5sc10_123 with dissolve
    fr "Here. I can leave the room while you read it, if you want?"
    scene ch5sc10_124 with dissolve
    mc "That isn't necessary. You also happen to be in the group of people that I trust."
    fr "......"
    scene ch5sc10_125 with dissolve
    mc "Okay... Let’s see."
    rd "[mc], it would please me if you would attend the celebration of my 20th name day."
    rd "I hope to see you, Amelia."
    scene ch5sc10_126 with dissolve
    mc "*Inhales* It’s scented?"
    fr "She probably sprayed some of her perfume on it, so you’d know it was from her."
    scene ch5sc10_127 with dissolve
    mc "Women do that?"
    fr "Some do. Although it depends on who the letter is intended for."
    mc "Have you ever sent a perfumed letter?"
    scene ch5sc10_128 with dissolve
    fr "I-I Uhmm... W-What makes you ask such a thing?"
    fr "I wouldn’t know what to write."
    fr "Uhhh... Also, I don’t own any perfumes."
    scene ch5sc10_129 with dissolve
    fr "So... Uhh- I..."
    scene ch5sc10_130 with dissolve
    fr "Sorry!"
    fr "I should probably get back to the castle and see if Amelia needs anything."
    scene ch5sc10_131 with dissolve
    fr "It was really nice talking to you!"
    fr "Thank you for letting me visit a little!"
    scene ch5sc10_132 with dissolve
    $ renpy.pause()
    ####Choice####
    menu:
        "Stay a little longer. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc10_132 with dissolve
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            mc "Stay."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            scene ch5sc10_133 with dissolve
            fr "W-What?"
            fr "Y-You want me to stay?"
            mc "Mhm. Stay here with me."
            scene ch5sc10_134 with dissolve
            "*Sound of door locking* ..."
            fr "Okay."
            scene ch5sc10_135 with dissolve
            fr "I’ll stay."
            if frida_path == True:
                scene ch5sc10_136 with dissolve
                fr "You’ve been thinking about it as well, then? That time we got interrupted..."
                mc "Yes."
                scene ch5sc10_137 with dissolve
                fr "Me too."
                fr "I haven't been able to stop thinking about it..."
                fr "Do you want to continue our indecent behavior, then?"
                mc "Yes."


            else:
                scene ch5sc10_136 with dissolve
                fr "You’ve felt it too, right? Whenever our eyes meet..."
                $ frida_path = True
                mc "Yes."
                scene ch5sc10_137 with dissolve
                fr "I don't have any perfumes, but I could rub a letter between my breasts and send it to you."
                fr "Would you like that?"
                mc "Yes. I'd love it."

            scene ch5sc10_138 with dissolve
            fr "I’ve had nothing but scandalous thoughts since I saw your cock earlier."
            fr "My breasts are already tingling..."
            mc "Oh yeah? Tell me more about them."
            scene ch5sc10_139 with dissolve
            fr "I think it’s better if I just show you... We don’t have that much time, after all."
            fr "You want to see them, don’t you?"
            mc "I do. Your outfit shows off your curves beautifully."
            scene ch5sc10_140 with dissolve
            fr "Here you go... Just for you."
            mct "{i}It’s a wonder of the world that a petite girl like Frida can have such impressive... volume.{/i}"
            fr "Do you like them? As you can tell by my nipples... they’re excited to be out."
            scene ch5sc10_141 with dissolve
            mc "Frida... I love them."
            fr "Oh? *Giggles softly* I’m such a bad maid! I haven’t even offered you a taste!"
            fr "Would you... like to taste them... *Sensual* Master?"
            mc "Yes... Come here."
            scene ch5sc10_142 with dissolve
            mct "{i}She’s actually roleplaying as my maid... Five hells.{/i}"
            scene ch5sc10_143 with dissolve
            fr "*Sensual* I’ve been a naughty maid... Thinking such lewd things about my master."
            scene ch5sc10_144 with dissolve
            fr "I’ve even been touching myself... thinking about you. Such an indecent thing for a servant to do."
            scene ch5sc10_143 with dissolve
            mc "What am I to do with such a naughty maid? ... Hmh."
            fr "I think there’s only one thing to be done when a maid turns lewd. You have to fulfill her desires."
            scene ch5sc10_144 with dissolve
            fr "Starting with my left nipple... Mnhh-"
            scene ch5sc10_145 with dissolve
            fr "*Moans* Ohh! That feels- Mhhh! So good!"
            fr "*Moans* Nobody’s ever tasted my nipples before... H-How are they?"
            scene ch5sc10_146 with dissolve
            fr "*Moans* OHhh... I see... Mhhh! Y-You like them that much? AHhhh..."
            scene ch5sc10_145 with dissolve
            fr "*Moans* Please! Please suck my nipple, Master! Yes! Mnhh..."
            scene ch5sc10_146 with dissolve
            $ renpy.pause(0.7)
            scene ch5sc10_145 with dissolve
            $ renpy.pause(0.7)
            scene ch5sc10_146 with dissolve
            $ renpy.pause(0.7)
            scene ch5sc10_145 with dissolve
            $ renpy.pause(0.7)
            scene ch5sc10_146 with dissolve
            $ renpy.pause(0.7)
            scene ch5sc10_147 with dissolve
            fr "*Moans* L-Lean back... I want to see your cock again."
            scene ch5sc10_148 with dissolve
            mc "Mnhh... All yours."
            fr "I should have done this as soon as you walked in with your cock out."
            scene ch5sc10_149 with dissolve
            fr "Will you forgive me, Master, if I suck your beautiful cock?"
            mc "Mnh... All will be forgiven."
            scene ch5sc10_150 with dissolve
            fr "I’ve never had a cock in my mouth before. You’re taking all my firsts, Master."
            mc "Good. That’s how I like it."
            scene ch5sc10_151 with dissolve
            fr "I live to please, my master. Mnhh... I’ll do anything."
            mct "{i}By all the gods. I’ll have to claim her if this is what she’ll be like ...{/i}"
            scene ch5sc10_152 with dissolve
            fr "Ooops! What am I thinking? Still being dressed when my master is naked. Bad maid. *Giggles*"
            scene ch5sc10_153 with dissolve
            fr "There we go! Much better. Wouldn’t you agree, Master?"
            mc "Much better indeed. Now, you'd better start before I spank you for being such a little tease."
            scene ch5sc10_154 with dissolve
            fr "Oh my! *Giggles* I'd better put this little mouth to use right away!"
            fr "I bet if I work really hard... I’ll be able to fit it just perfectly!"
            scene ch5sc10_155 with dissolve
            fr "Mnhhh ... Master."
            scene fr_lewd6 with dissolve
            $ renpy.pause()
            fr "*Suck* Your cock... Mhh-Soh good... *Lick* Warm... Mnhh..."
            mc "F-Fuck... That hits the spot. You’re doing well."
            scene fr_lewd7 with dissolve
            $ renpy.pause()
            fr "*Moans* Mnhh... Master likes having me on my knees? Mnhh *Suck* Enjoying his large cock?"
            mc "Yeah... I like that. Mnhh. Be a good maid and take me in your mouth now."
            scene fr_lewd8 with dissolve
            $ renpy.pause()
            with vpunch
            fr "*Muffled moan* Likeh thiiss? MNhh! Nngghh... Mhaster I-I love *Suck* sucking your hard cock. MNhhh!"
            mc "Ahhh... Frida, that’s it. Keep doing that with your tongue."
            scene fr_lewd9 with dissolve
            $ renpy.pause()
            fr "*Muffled* Thissh? MhHh!! *Swirls tongue* Mnhh..."
            mc "Fuck. Y-Yeah... Your little mouth is like a den of pleasure... Mnhh."
            fr "*Muffled* Mnhh... P-Please, Master... fill my mouth with- MNhh your... cum."
            with vpunch
            mc "Ahhh! Frida... I’m- I’m about to- Mnhh!"
            with vpunch
            fr "*Sucks harder* MNhh!! Ahmmh!"
            scene ch5sc10_156 with dissolve
            $ renpy.pause()
            scene ch5sc10_157 with dissolve
            $ renpy.pause()
            scene ch5sc10_158 with dissolve
            with vpunch
            fr "Mnhh! ... Mngh!!"
            mc "That’s it. Be a good girl and swallow everything."
            fr "*Suck* Mnnhh..."
            scene ch5sc10_159 with dissolve
            fr "*Gulp* Mnhghh! ... Mnhh... *Kiss*"
            scene ch5sc10_160 with dissolve
            fr "Th-Thank you, Master. I thoroughly enjoyed that!"
            fr "I hope I served you well. *Giggles*"
            scene ch5sc10_161 with dissolve
            mc "Mmm... Fuck... You did."
            mc "*Chuckles* I may have to steal you away from Amelia if this is how dutiful you intend to be."
            fr "*Mwah* ..."
            scene ch5sc10_160 with dissolve
            fr "Y-Yeah... You may just have to do something reckless like that... Mnh."
            scene ch5sc10_161 with dissolve
            fr "*Mwah* I'd better get dressed. I need to get back."
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)
            scene ch5sc10_131 with Dissolve(1.5)
            play music explore_1 fadein 1.0
            #stop music fadeout 1.0
            fr "*Sighs* Sorry for leaving so quickly, but I need to get back."
            fr "Otherwise, they'll wonder why it’s taken so long to deliver a letter."
            fr "Will I see you at the castle?"
            scene ch5sc10_132 with dissolve
            mc "Sure. I’ll be around."
            scene ch5sc10_133 with dissolve
            fr "..."
            fr "[mc]?"
            mc "Mmh?"
            $ frida_path = True
            scene ch5sc10_135 with dissolve
            fr "T-Thank you. I really enjoy spending time with you."
            mc "Me too, Frida. I enjoy your company."
            fr "I like how I don’t have to put on a front with you, or conform to certain expectations."
            fr "I feel I can just be myself."
            scene ch5sc10_136 with dissolve
            fr "It's really... freeing."
            mc "Yeah, I can imagine."
            mc "You must feel like you're living in a cage, even if the royals do treat you well."
            scene ch5sc10_135 with dissolve
            fr "Yes... so, thank you."
            fr "I really want to do this again... soon!"
            scene ch5sc10_134 with dissolve
            fr "Bye bye!"
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)

        "Thank you for delivering the letter. ({color=#2bff8b}Friendship{/color})":
            scene ch5sc10_132 with dissolve
            mc "Thank you for delivering the letter. It was nice talking to you, Frida."
            $ frida_path = False
            fr "You too! See you around!"
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)

    scene black with Dissolve(2)
    "You get dressed and head back down to the tavern."
    scene ch5sc10_162 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Hey, Anna."
    mc "Are there any breakfast leftovers available, or am I too late?"
    scene ch5sc10_100 with dissolve
    aa "Hi, [mc]."
    aa "You’re in luck! We do have a little bit left. I could heat it up for you?"
    scene ch5sc10_101 with dissolve
    mc "That’d be great. Thank you, Anna."
    scene ch5sc10_103 with dissolve
    aa "*Quietly* {size=-10}{b}I’m not really supposed to serve anyone breakfast this late, but it’ll be our little secret.{/b}{/size}"
    scene ch5sc10_104 with dissolve
    mc "*Quietly* {size=-10}{b}All knowledge about this outrageous criminal act will go with me to the grave.{/b}{/size}"
    aa "Mnh-Hm."
    scene ch5sc10_105 with dissolve
    aa "Then I’ll be right back with something for you."
    scene ch5sc10_163 with dissolve
    mct "{i}It's kind of her to risk trouble with her boss just so I can have some breakfast.{/i}"
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch5sc10_164 with Dissolve(1)
    aa "Here you go."
    aa "The innkeeper is running errands at the market, so I think we’re safe!"
    aa "Eggs, bacon, roasted mushrooms, a couple slices of bread and some apples."
    aa "I hope this will fill you up, you're a big man after all..."
    scene ch5sc10_165 with dissolve
    mc "Thank you, Anna. This is great."
    mc "It looks beyond appetizing."
    aa "Mnh-hm. I bet it does."
    scene ch5sc10_166 with dissolve
    aa "It’s important for a man to get the proper nutrients to stay healthy."
    aa "Yet, so many neglect it."
    mc "I didn't know you were such an passionate advocate for healthy nutrition."
    scene ch5sc10_167 with dissolve
    mc "Mnh... This is delicious. The bacon is perfect and crispy."
    aa "Glad you like it. I threw them on the pan again to get them a little crispier."
    scene ch5sc10_168 with dissolve
    aa "As for nutrition... I grew up on my family's farm, remember? And Mother had to feed all of us."
    aa "Keeping our family's energy high for farm work was vital. We depended totally on the strength of our menfolk."
    mc "Makes sense. Do you miss it?"
    scene ch5sc10_169 with dissolve
    aa "The farm? Yeah... Some of it, at least."
    aa "I do like living in the city, but the air on the farm is so different."
    aa "And I loved working with the animals. Feeding them, grooming them, herding them."
    aa "Pleased with your breakfast?"
    scene ch5sc10_171 with dissolve
    mc "Loved it. Thank you, Anna."
    mc "I can understand why you miss the animals."
    mc "I befriended a wolf shortly after arriving here in Luxenford."
    scene ch5sc10_170 with dissolve
    aa "*Gasps* A wolf?! How did you pull that off?"
    scene ch5sc10_171 with dissolve
    mc "I was on a quest for the Adventurers Guild."
    mc "The stables outside Luxenford had been having some trouble with their horses running off."
    mc "It turned out to be because of a wolf without a pack."
    mc "It was in a desperate state, but I managed to calm it."
    scene ch5sc10_170 with dissolve
    aa "Calmed a desperate wolf?"
    aa "My... You’re just full of surprises, aren’t you?"
    scene ch5sc10_171 with dissolve
    mc "I’ve got a few up my sleeve. Let’s just leave it at that."
    scene ch5sc10_170 with dissolve
    aa "Tall, dark, handsome, mysterious and an animal lover too?"
    aa "You really know how to captivate a woman."
    aa "If I brought you home to the farm, Mother wouldn’t let you leave. *Quietly* {size=-10}{b}And neither would I.{/b}{/size}"
    ####Choice####
    menu:
        "Flirt. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc10_171 with dissolve
            mc "Just your mother?"
            $ aa_path = True
            scene ch5sc10_172 with dissolve
            aa "Not just my mother, no..."
            aa "If you tried to leave, I’d probably lock you up in the barn."
            scene ch5sc10_173 with dissolve
            mc "The barn? *Chuckles*"
            scene ch5sc10_174 with dissolve
            aa "Mhm-hmm!"
            aa "That way, I’d have you all to myself and nobody would disturb us."
            scene ch5sc10_173 with dissolve
            mc "We wouldn’t want that."
            scene ch5sc10_174 with dissolve
            aa "No, we wouldn’t."
            aa "Milking is best done in private..."
            scene ch5sc10_173 with dissolve
            mc "Are you saying-"
            scene ch5sc10_174 with dissolve
            aa "I’m saying I’m about to go on break."
            aa "So, you should meet me downstairs..."
            scene black with Dissolve(2)
            $ renpy.pause(1)
            scene ch5sc10_175 with Dissolve(2)
            aa "This room will do perfectly. I’m pretty much the only one who comes down here."
            mc "You’re not going to lock me up, are you?"
            aa "Don’t give me ideas... I’m a woman of action. But no, I have something else in mind."
            scene ch5sc10_176 with dissolve
            aa "Like getting you out of these pants..."
            mc "I was starting to wonder if you were all talk."
            aa "*Snickers* I’m going to show you how farm girls milk their men."
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene ch5sc10_177 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            aa "Mhm... Now that’s what I call a proper cock."
            aa "You’ve got some nice scars too. I bet you’ve seen a lot of action...?"
            scene aa_lewd1 with dissolve
            mc "Maybe... Mnh."
            aa "You’re rock hard. You must’ve been anticipating this moment... Mnh."
            aa "Your chest is so firm... Do you like feeling my breasts rubbing against it?"
            mc "Yeah... Mnh... Your breasts are perfectly full and dense."
            mc "Not a lot of younger women are as filled out as you."
            aa "Good of you to notice. I guess they help me stand out. Mmmh..."
            aa "I think you’re ready ... to be milked."
            scene ch5sc10_178 with dissolve
            aa "After I’m done with you, you’ll probably want to become a farmer. I’m sure of it. *Snickers*"
            scene ch5sc10_179 with dissolve
            mc "If this is what a farmer’s life is like, I could be persuaded."
            aa "Mhm... Just imagine tending to the farm, and having a girl like me... tending to your every need."
            scene ch5sc10_180 with dissolve
            mc "*Moans* Mnhh ..."
            aa "Oh? You like that? You like feeling the warmth of my soft breasts wrapped around your hard cock?"
            mc "Yeah... They’re amazing."
            scene aa_lewd2 with dissolve
            aa "*Moans* Mnhh... Let the... Mnhh... milking begin."
            mc "*Moans* Ahh... Have I told you I’m glad you started working here?"
            aa "*Giggles* Oh, I know you are. I feel it between my breasts... MNhh."
            scene aa_lewd3 with dissolve
            aa "I've always dreamed of acting a little scandalous... mnhHH..."
            aa "But I’d never met anyone interesting enough to take the chance on til now."
            mc "Mnhh... You’re definitely acting scandalous right now. Ahh."
            aa "*Moans* Guess that means... Ahnghh... that you’re... MNhh! my type!"
            mc "Fuck... Anna. Mnh. I’m close..."
            with vpunch
            aa "{b}*Moans*{/b} Yes! [mc]... Mnhh! Don’t hold back... I want you to cover me in your warm cum!"
            scene ch5sc10_181 with dissolve
            with vpunch
            aa "{b}*Moans*{/b} I feel it! Mnh!! You’re about to burst! Yes!! Let me milk you! AHh!"
            scene ch5sc10_182 with dissolve
            with vpunch
            mc "AAhhh! MMm!"
            scene ch5sc10_183 with dissolve
            with vpunch
            aa "{b}AhhHh!!{/b}"
            scene ch5sc10_184 with dissolve
            with vpunch
            aa "MNh! Yes!! {b}Cover me!{/b}"
            scene ch5sc10_185 with dissolve
            aa "MMmm... So warm..."
            mc "Damn, Anna. Your breasts squeezed every drop out of me..."
            aa "MNhhmm... So tasty. I can’t believe you had this much for me. Hnnghh!"
            scene ch5sc10_186 with dissolve
            aa "How do I look?"
            mc "Like a proper farmer’s daughter."
            aa "*Snickers* Good! Could you grab us some rags? They're by the barrels."
            scene black with Dissolve(1.5)
            "You grab the towel by the barrels and the two of you wipe off."
            scene ch5sc10_187 with Dissolve(1.5)
            mc "*Chuckles* I certainly didn’t expect this when I asked about breakfast..."
            aa "*Giggles softly* Well, I needed a little protein myself. You were tasty. A perfect mix of salt and sweet."
            mc "Well, it wouldn't do to let you go hungry all day."
            scene ch5sc10_178 with dissolve
            aa "How kind of you! *Snickers* I’ll add ‘thoughtful’ to your list of traits."
            aa "I guess I’ll keep this in mind whenever I’m feeling a bit... hungry."
            scene ch5sc10_177 with dissolve
            aa "This is a cock that counts as a three course meal, after all... Mnhh."
            mc "You’re the nutrition expert. I’m just providing what you need."
            scene ch5sc10_178 with dissolve
            aa "*Sighs heavily* We... we'd better go upstairs. I've definitely exceeded my break time."
            mc "Yeah... I have to go to the guild and see what’s on the program for today."
            scene black with Dissolve(1.5)
            $ renpy.pause(1)
            scene ch5sc10_176 with Dissolve(1.5)
            aa "Okay... You should head up first, just in case the Innkeeper is back."
            aa "I don’t want to have to explain why you were down here."
            aa "I’ll see you later?"
            mc "Sure. See you later, Anna."
            $ aa_trust += 5
            "Anna thoroughly enjoyed milking you, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)

        "Move on. ({color=#2bff8b}Friendly{/color})":
            scene ch5sc10_171 with dissolve
            $ aa_path = False
            mc "Heh... I bet she'd love to have another pair of hands around the farm."
            mc "Anyways, I’d better get going and see what they’re up to at the guild."
            mc "Thank you again for the delicious breakfast."
            scene ch5sc10_170 with dissolve
            aa "No problem! Just don’t tell anyone! *Giggles*"
            scene black with Dissolve(1.5)
            #play music ch4sc6 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)



    scene ch4sc6 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc10_188 with Dissolve(1.5)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    da "So, here’s what you’ll need to do tonight-"
    scene ch5sc10_189 with dissolve
    da "Ahh, [mc]. Good... I was just about to brief Eliza about tonight, but it'll be easier to brief you both at once."
    scene ch5sc10_190 with dissolve
    el "*Whispers* {size=-10}{b}Hi!{/b}{/size}"
    scene ch5sc10_191 with dissolve
    mc "*Whispers* {size=-10}{b}Hey you...{/b}{/size}"
    "She gently squeezes your arm."

    if eliza_relationship == True:
        scene ch5sc10_192 with dissolve
        el "*Whispers* {size=-10}{b}Did you remember to have some breakfast? Sounds like we’ll be busy today.{/b}{/size}"
        mc "*Whispers* {size=-10}{b}I did. Anna, the tavern maid, heated some leftovers for me. I should be all set for the day.{/b}{/size}"
        el "*Whispers* {size=-10}{b}Good... I missed you.{/b}{/size}"
        scene ch5sc10_193 with dissolve
        mc "*Whispers* {size=-10}{b}I missed you too, Kitten.{/b}{/size}"
        el "*Whispers* {size=-10}{b}Mnhh... I can’t stop thinking about you. About us... About, you know...{/b}{/size}"
        da "*Clears throat* I am still here, you know? If you two lovebirds are done...?"


    else:
        scene ch5sc10_192 with dissolve
        el "Did you remember to have some breakfast? We’ll be busy today."
        mc "I did. I'm all set for the day."

    scene ch5sc10_194 with dissolve
    mc "I assume this briefing is about Amelia’s name day celebration, correct?"
    scene ch5sc10_195 with dissolve
    el "You already know?"
    scene ch5sc10_191 with dissolve
    mc "Yeah, Amelia sent me an invitation. Her maid delivered it this morning."
    scene ch5sc10_195 with dissolve
    with vpunch
    el "An invitation? From the princess?"
    el "That's huge!"
    scene ch5sc10_196 with dissolve
    da "Good, that must mean she’s warming up to you."
    da "Since you're her bodyguard, protecting her is your main objective for tonight."
    da "The rest of the guild has also been hired to keep watch during the celebration."
    da "King Bennen himself requested our help."
    scene ch5sc10_197 with dissolve
    el "Woah! Hold up! T-The king?!"
    el "We’re going to meet the King? And the Queen? Heavens..."
    scene ch5sc10_198 with dissolve
    da "Remember, this is not a regular meet and greet. While we need to appear to be regular guests..."
    da "That's merely a guise. We have a duty to stay vigilant, and to prevent anything bad from happening."
    scene ch5sc10_199 with dissolve
    el "I’m sorry, but why would something bad happen during her celebration? Isn’t it an occasion for fun and joy?"
    scene ch5sc10_198 with dissolve
    da "Normally, it would be."
    da "But... the princess is already turning 20, and she is still not betrothed despite being eligible for the last two years."
    scene ch5sc10_196 with dissolve
    da "Stubborn as she is, she's refused any and all suitors that have tried to court her."
    da "And this puts her family under a lot of political pressure."
    da "Marriages are one of the best ways to secure alliances between nations..."
    scene ch5sc10_200 with dissolve
    el "But because she’s refusing everyone... it weakens the throne?"
    scene ch5sc10_201 with dissolve
    da "Correct. Many of the greater noble houses within our own kingdom are getting restive."
    da "And increasingly, more and more spies from the other Kingdoms have also been caught here in the capital."
    scene ch5sc10_200 with dissolve
    el "Would they really attempt something during her celebration? It'd be an incredibly risky move."
    scene ch5sc10_198 with dissolve
    da "It would. And His Grace doesn’t really expect that anyone will dare to try anything."
    da "But he's also unwilling to risk being wrong about that."
    da "That’s why he wants us, unassuming regular guests, who'll double as secret allies inside the palace walls, in case there's trouble."
    scene ch5sc10_202 with dissolve
    mc "Anyone who's up to no good, won't be as wary around us as they would be around the King's men."
    scene ch5sc10_196 with dissolve
    da "Exactly. As far as they're concerned, we'll just be regular guests."
    da "Their guard will be down around us, and they may let something slip."
    da "I’ve already briefed the others."
    da "Eliza you'll be in charge of the guest list. Everyone attending is on there."
    scene ch5sc10_198 with dissolve
    da "Make sure that every guard gets a copy of the list, and vet it carefully to be sure no one unexpected is listed."
    da "This will also be a good opportunity for you to get familiar with the various nobles and their retainers."
    scene ch5sc10_196 with dissolve
    da "[mc], as I said earlier, your focus is to keep protecting the princess."
    scene ch5sc10_202 with dissolve
    mc "Got it."
    scene ch5sc10_196 with dissolve
    da "In the event that something does happen..."
    da "We must notify the King or Queen directly, and we are authorized to detain anyone we deem suspicious."
    da "However, we also need to avoid making a scene. The King doesn't want to alarm Amelia, or cause a scene in public."
    scene ch5sc10_203 with dissolve
    with vpunch
    el "Uh! Stealth! I always wanted to go on a stealth mission!"
    scene ch5sc10_204 with dissolve
    da "*Sighs* No... This is not a stealth mission. We are guests, remember?"
    el "B-But... stealth?"
    da "No stealth."
    scene ch5sc10_205 with dissolve
    el "Rats! ..."
    scene ch5sc10_202 with dissolve
    mc "Are we supposed to mingle with the guests?"
    scene ch5sc10_196 with dissolve
    da "Yes, that’s what events at court are all about."
    scene ch5sc10_202 with dissolve
    mc "*Sighs deeply* Great ..."
    scene ch5sc10_206 with dissolve
    el "C’mon! It’ll be fun! You’ve already come a long way in socializing! This will be good for you."
    el "You’ll have a grand time! I promise!"
    scene ch5sc10_207 with dissolve
    mc "*Sighs* Fine, fine. Whatever..."
    el "*Giggles* Heeh-heeh-heeh!"
    da "One last thing... Taron might also be attending."
    scene ch5sc10_208a with dissolve
    with vpunch
    bth "{b}WHAT?!!{/b}"
    el "You can’t be serious?! He killed [mc]’s parents!"
    mc "He injured Eliza! Why the fuck-"
    scene ch5sc10_208 with dissolve
    da "Calm yourselves. Like myself, Taron is a trusted vassal of the King."
    da "We attended the Knights Academy together."
    scene ch5sc10_209 with dissolve
    da "In the eyes of the King, and the court, Taron is a Guildleader. And a successful one, at that."
    da "He has status and a lot of influential connections. So, you will have to behave yourselves- both of you."
    scene ch5sc10_208 with dissolve
    mc "*Grits teeth* But..."
    el "You expect us to smile and play nice with that psycho?! I’d rather tear his head off! With my teeth!"
    scene ch5sc10_209 with dissolve
    da "*Sigh* We know that Taron is corrupt and despicable, but we need solid proof of his misdeeds before taking any action against him."
    scene ch5sc10_210 with dissolve
    da "The King won’t take kindly to unfounded accusations against one of his most trusted associates."
    el "Dalen! If Taron is there... It’ll finally be our chance to-"
    scene ch5sc10_211 with dissolve
    with vpunch
    da "{b}NO. DAMMIT!{/b}  You two... get your heads on straight!"
    da "I know you feel like you're on top of the world, right now. But you've only just got back on your feet, dammit!"
    da "We have no idea what Taron is capable of. And you will not put yourself in danger like that! ... Besides-"
    da "If Taron does turn up, he'll most likely be trying to provoke you into making that kind of mistake."
    da "It’s paramount you don’t react violently."
    da "If you accuse or attack him, in front of all those witnesses..."
    da "you’ll be spending the rest of your lives in the dungeon."
    scene ch5sc10_212 with dissolve
    el "But-"
    scene ch5sc10_213 with dissolve
    mc "Eliza... it’s okay."
    mc "We both know Taron is going to die by our hands. It just won’t be tonight."
    scene ch5sc10_214 with dissolve
    el "*Sighs heavily* Okay..."
    el "I swear, if that psycho so much as smiles at me... *Growls* Hmhh!"
    scene ch5sc10_210 with dissolve
    da "I get it."
    da "But if you still aspire to become accomplished adventurers, you’re going to need to learn to deal with impossible situations."
    da "This is one of those situations where you are required to maintain a civil façade, even with your worst enemy."
    scene ch5sc10_209 with dissolve
    da "Just know that if you decide to pursue him tonight, I won’t be able to protect you. You’ll be branded as enemies of the state."
    scene ch5sc10_194 with dissolve
    mc "We understand, Dalen. We’ll keep our cool."
    scene ch5sc10_198 with dissolve
    da "Eliza? ..."
    scene ch5sc10_199 with dissolve
    el "Fine! ... Fine. We won’t act rashly..."
    scene ch5sc10_200 with dissolve
    el "Do you really think he'll be there?"
    scene ch5sc10_201 with dissolve
    da "I don’t know. The King did invite all the guilds and their leaders."
    da "But Taron often skips events like this. We won’t know for certain until tonight."
    scene ch5sc10_200 with dissolve
    el "It just infuriates me that he gets to waltz around like someone important, after all he's done!"
    el "Even ignoring what he's done to us... how many others have suffered at his hands?"
    scene ch5sc10_202 with dissolve
    mc "I have to agree with Eliza. We know he extorted Selena and kidnapped her sister."
    mc "He also kidnapped Luna’s mother, Cassandra... and she's the Guildmaster of the Mages guild!"
    scene ch5sc10_196 with dissolve
    da "I had the location you gave me checked out. But all the cells are empty."
    da "There are no signs of her being there."
    scene ch5sc10_197 with dissolve
    with vpunch
    el "{b}WHAT?!{/b} That’s impossible!"
    el "We know for a fact that she's bound there by some sort of dark magic! A hex, I think."
    scene ch5sc10_198 with dissolve
    da "I’m not saying I don’t believe you."
    da "I’m just saying we don't have any proof of it right now."
    scene ch5sc10_199 with dissolve
    el "No... But-"
    scene ch5sc10_198 with dissolve
    da "And that's a huge problem. Blindly charging against him will only backfire on us."
    da "The only one who wins in that scenario, is him."
    da "Which is why he's likely going to try to get a rise out of you tonight."
    scene ch5sc10_196 with dissolve
    da "Both of you need to understand that."
    da "If we could somehow find Cassandra, that would be a good start."
    da "We’d still need more proof, and lots of it."
    da "But with Cassandra backing us up, it wouldn't just be our word against his."
    scene ch5sc10_195 with dissolve
    el "Luna! Maybe she knows something?"
    scene ch5sc10_196 with dissolve
    da "Good idea. [mc], do you think you could check on Luna today? See if she knows anything?"
    scene ch5sc10_202 with dissolve
    mc "Yeah, I’ll go see her before the celebration tonight."
    mc "At the very least, she needs to know that her mother isn't in the cell any more."
    mc "The celebration is supposed to start at sundown, correct?"
    scene ch5sc10_189 with dissolve
    da "Correct. The doors will open at sunset, so you still have a few hours."
    da "There won't be any other quests assigned today."
    da "The two of you can use the day as you please once Eliza has vetted the guest list."
    scene ch5sc10_191 with dissolve
    mc "I’ll help her."
    mc "Four eyes are better than two."
    scene ch5sc10_190 with dissolve
    el "Thank you."
    el "That’s really sweet."
    scene ch5sc10_196 with dissolve
    da "Sounds good to me. Now, get out of here."
    da "I’ll see you both at the celebration tonight."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc09_019 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    amt "{i}Ugh... My neck is killing me. How does it even get sore? I’ve got the best pillows in the kingdom.{/i}"
    scene ch5sc10_215 with dissolve
    amt "{i}I wonder if [mc] liked my letter...{/i}"
    amt "{i}I bet [mc] would be great at giving a massage.{/i}"
    scene ch5sc09_019 with dissolve
    amt "{i}Stop it... Stop thinking about him like that.{/i}"
    scene ch5sc10_215 with dissolve
    amt "{i}*Sighs* Sending him a perfumed letter... What was I thinking?{/i}"
    amt "{i}He’s going to think I’m such a weirdo.{/i}"
    scene ch5sc09_020 with dissolve
    amt "{i}Hopefully, he liked it. I’ll have to ask Frida when she gets back!{/i}"
    scene ch5sc10_216 with dissolve
    amt "{i}Speaking of... Why is she taking so long? I thought the tavern he's staying in wasn’t that far from the palace...{/i}"
    scene ch5sc10_217 with dissolve
    fr "Y-Your Grace. Sorry I took so long! I-I..."
    scene ch5sc10_218 with dissolve
    am "Frida, there you are! I’ve been waiting for your return."
    am "So? How did it go? Did he like it?"

    if frida_path == True:
        scene ch5sc10_219 with dissolve
        fr "He... He..."
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch5sc10_146 with Dissolve(1)
        $ renpy.pause()
        scene ch5sc10_155 with Dissolve(1)
        $ renpy.pause()
        scene ch5sc10_161 with Dissolve(1)
        $ renpy.pause()
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch5sc10_222 with Dissolve(1)
        am "Well? Spit it out!"
        am "The suspense is bad for my health!"
        scene ch5sc10_221 with dissolve
        fr "He liked it!"
        fr "V-Very much so! H-He was pleased! Fully pleased!"
        scene ch5sc10_220 with dissolve
        am "Really?"
        am "He enjoyed it that much?"
        scene ch5sc10_221 with dissolve
        fr "Yes!"
        fr "He was smiling from ear to ear when I left!"
        scene ch5sc10_220 with dissolve
        am "No way? Good!"
        am "Good... *Quietly* {size=-10}{b}He must've liked it then... maybe my perfume helped?{/b}{/size}"
        scene ch5sc10_221 with dissolve
        fr "He even noticed the scent!"
        fr "If-... if you need more letters delivered to him, I'll... I'll be happy to do it!"
        scene ch5sc10_220 with dissolve
        am "Oh? Noted, but I don't think I need to write him anything else at the moment."
        am "Now..."


    else:
        scene ch5sc10_219 with dissolve
        fr "Y-Yes, he seemed to like it. He even smelled it and said how nice the scent was."
        scene ch5sc10_220 with dissolve
        am "No way? Good! Good... *Quietly* {size=-10}{b}He must've liked it then.{/b}{/size}"

    am "Frida, please draw me a bath."
    am "And could you lay out that dress I bought recently?"
    scene ch5sc10_219 with dissolve
    fr "The one from when you went shopping with [mc]?"
    scene ch5sc10_220 with dissolve
    am "Yes. That's the one. Thank you."
    am "Afterwards, you can draw yourself a bath too. You've earned it."
    scene ch5sc10_219 with dissolve
    fr "T-Thank you... Amelia."
    fr "I'll get right to it!"
    scene black with Dissolve(2)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss59 with Dissolve(2)
    $ renpy.pause()
    scene ch5sc08_133 with Dissolve(2)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    bn "*Sighs* It’s one headache after another."
    scene ch5sc10_223 with dissolve
    wo "Your Grace."
    wo "My fleet, the 1st Vanguard is ready to mobilize."
    wo "Just give the command."
    scene ch5sc10_224 with dissolve
    bn "*Sighs* I was hoping it wouldn’t be necessary but... Looter’s Bay has become a chaotic mess."
    bn "We’ve lost contact with the ambassadors we posted there."
    bn "It’s one of the most prominent ports of trade in the Kingdom..."
    bn "Every day that passes, we lose valuable income and trade goods."
    scene ch5sc10_225 with dissolve
    wo "Pirates... Tsk!"
    wo "They can’t be depended on to do anything but act on their own greed. Tsk!"
    wo "Give the command, and Looter’s Bay will be under your control within a fortnight."
    scene ch5sc10_224 with dissolve
    bn "Your father served me faithfully as Lord Admiral of my fleet, for many years."
    bn "Yet, he was slain by Captain Blackheart."
    bn "Are you sure you’re up for this?"
    scene ch5sc10_223 with dissolve
    wo "He'll pay for his crimes against the Crown."
    wo "I vowed that upon my father’s casket."
    wo "As your Lord Admiral, I'll avenge my father and retake Looter’s Bay for you."
    wo "For our kingdom."
    scene ch5sc10_224 with dissolve
    bn "Your achievements speak for themselves."
    bn "You haven't let the crown down yet."
    bn "Very well. You have complete authority to bring Looter’s bay to heel. Any way you see fit."
    scene ch5sc10_225 with dissolve
    wo "It will be done, Your Grace."
    scene ch5sc10_226 with dissolve
    wo "I’ll set sail within the hour."
    wo "The King’s justice will fall like a hammer on any who oppose us."
    bn "I’m counting on you, Admiral. This is your chance to fill your father’s boots."
    scene ch5sc10_227 with dissolve
    wo "Your Grace."
    scene black with Dissolve(2)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss22 with Dissolve(2)
    $ renpy.pause()
    scene ch5sc10_228 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    al "*Humming* Hm-Mh-Hm-Mh, Dragonroot, Silvercap, and a dash of Allspice."
    scene ch5sc10_229 with dissolve
    al "Yes! Come on! Please turn pink!"
    scene ch5sc10_230 with dissolve
    with vpunch
    al "Hah! {b}YES!!{/b} I did it! My first successful enhancement brew!"
    scene ch5sc10_231 with dissolve
    al "It was my last batch of ingredients too! Phew! I’ve brewed what? Four batches this morning?"
    al "Just wait til Venetos hears about this! And... [mc]. He’ll be so proud! *Giggles*"
    scene ch5sc10_232 with dissolve
    el "*Knocks* Alice? You in here?"
    al "Doors open! Come on in, Eliza. You have to see this!"
    scene ch5sc10_233 with dissolve
    el "Hi Alice! Hug!"
    al "*Giggles softly* Okay, okay!"
    scene ch5sc10_234 with dissolve
    with vpunch
    el "Squeeeeeze! *Hugs tightly*"
    al "*Laughs* Eliza! You’re in a good mood!"
    scene ch5sc10_235 with dissolve
    al "I take it your date with [mc] went well?"
    el "Uh-Huh! It couldn’t have been more amazing!"
    scene ch5sc10_236 with dissolve
    el "Y-You’re not mad at me, right?"
    scene ch5sc10_237 with dissolve
    al "Don’t be silly! [mc]'s a man... he can date as many or as few women as he wants."
    al "You know how it is in Luxeron. Men are free to take multiple wives or mistresses as they desire."
    scene ch5sc10_236 with dissolve
    el "Privilege of being a human male, I guess. Borri told me that Dwarves have very different customs."
    el "Apparently, they're always monogamous. Elves are too, and they even bond for life."
    el "Which is a long time since they can live for a thousand years or so!"
    scene ch5sc10_235 with dissolve
    al "If only we were born Elves, huh?"
    el "*Giggles* Yeah! Feels like human women drew the short straw when it comes to romantic privilege..."
    scene ch5sc10_238 with dissolve
    al "At Least we’re fortunate enough to have [mc] in our lives. It’s a whole lot worse for other women."
    el "Yeah... I feel blessed to have him in my life. You have no idea how many despicable men I’ve met."
    scene ch5sc10_235 with dissolve
    al "I’ve been lucky on that account. In Riverside, everyone treats each other respectfully."
    al "Benefit of life in a small village, I suppose."
    al "But here in the capital... men are definitely not as well-mannered."
    scene ch5sc10_238 with dissolve
    al "When I first started at the Academy, some of them would call out indecent things whenever I walked past."
    al "But one day, Luna overheard them and... well, she made sure that was the last time they tried anything like that."
    scene ch5sc10_239 with dissolve
    el "AWwh! I bet she totally whooped their butts!"
    el "Maybe roasted them with a fireball or two? *Snickers*"
    scene ch5sc10_238 with dissolve
    al "Hey, Eliza?"
    el "Mhh?"
    scene ch5sc10_240 with dissolve
    al "I’ve got an idea... can we make a deal not to discuss our romantic feelings for [mc] with each other?"
    al "We both clearly love him with all of our hearts."
    al "And I worry that being too open about it might cause jealousy and resentment between us."
    scene ch5sc10_241 with dissolve
    el "I like that idea. I can get a little jealous, sometimes."
    el "But if neither of us flaunts it, it'll help me cope with the situation better."
    al "Let’s just agree to be happy for each other if [mc] chooses to be with one or both of us someday."
    el "Agreed! It's probably the best solution."
    scene ch5sc10_242 with dissolve
    al "Ahh... I'm so relieved we're in agreement."
    al "Okay... are you ready to see what I’ve made?"
    el "Yush! Totally ready! Amaze me!"
    scene ch5sc10_243 with dissolve
    al "Until now, I’ve only been able to brew healing potions."
    al "But today I successfully brewed my first enhancement elixir!"
    el "Woah! An enhancement elixir. That sounds pretty cool! What does it do?"
    al "Supposedly, it enhances the physical prowess of whoever drinks it."
    al "Stamina and strength, and stuff like that."
    scene ch5sc10_244 with dissolve
    al "I still have to provide a sample of it to the Professor."
    al "She needs to run it through some tests before we can know for sure."
    el "Alchemy is so complicated. You’re pretty amazing, Alice!"
    scene ch5sc10_243 with dissolve
    al "It’s taken me a long time to get the basics down. I’m still far off from where I want to be."
    el "You should ask [mc] to bring you along on a quest."
    el "That way, you'll be able to test out some of your elixirs and potions."
    scene ch5sc10_244 with dissolve
    al "You really think he’d take me? Wouldn’t I just be a hindrance?"
    scene ch5sc10_245 with dissolve
    el "Pish-posh! Hindrance-schmindrance! He’s not going to take you out hunting for trolls!"
    el "Maybe you can help take down a bandit or two, rescue kittens from trees, fix broken fences... that sorta thing."
    scene ch5sc10_242 with dissolve
    al "Maybe I should ask him. That doesn’t sound so bad."
    al "It'd be nice to test out some of my brews properly."
    el "You’ll love it! [mc] told me that when you were young, you used to dream about going on adventures together."
    el "This is your chance to make it a reality!"
    al "Okay... Yeah! You’re right!"
    scene ch5sc10_234 with dissolve
    el "Hug!! *Giggles*"
    al "*Giggles* Eliza... I’m really glad we’re friends."
    el "Me too, Alice. Me too."
    el "I’ve gotta get going. Our guild is attending the royal celebration tonight, and I still have to get home and change."
    scene ch5sc10_238 with dissolve
    al "I wasn’t going to say anything, but your outfit is a little... cheeky?"
    el "*Soft laugh* Heh... Yeah. Not what I want to be wearing when meeting the royal family for the first time."
    scene ch5sc10_240 with dissolve
    al "I’ll see you another day, then! Have fun tonight."
    scene ch5sc10_241 with dissolve
    el "Bye, bye, Alice! I’ll make sure to tell you all about it next time!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)

    if sylph_relationship == True:
        scene ch4sc06_159 with Dissolve(1.5)
        mc "Sylph? Borri said you needed my help with something down here?"
        scene ch4sc06_177 with dissolve
        with vpunch
        sy "Mhp!!"
        mc "*Chuckles* Hey... is this what you needed me for?"
        scene ch4sc06_178 with dissolve
        sy "Mnh... I missed you! And I really wanted to be close to you!"
        scene ch4sc06_177 with dissolve
        mc "I missed you too, my favorite fairy."
        scene ch4sc06_178 with dissolve
        sy "I’m your only fairy, riiight?"
        scene ch4sc06_179 with dissolve
        mc "Yes-"
        with vpunch
        sy "Mmmhhpfh!"
        scene ch4sc06_182 with dissolve
        sy "*Mwah* Hnnghhh... Mhh!"
        scene sy_lewd1 with Dissolve(1)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        sy "Mnhh! *Lick* I love kissing you! Mnhh!"
        mc "You’re a great kisser... Mnh... Soft and fruity lips."
        scene sy_lewd2 with Dissolve(1)
        sy "*Kiss* We’re... magica ... together. Mhhhh... Mnh!"
        mc "*Kiss* I can feel your magic softly tingling over your lips and tongue..."
        sy "Hnnghh! Yes... I know. Mnh! I want to taste you again! Mnh! Let’s get naked!"
        scene ch4sc06_193 with dissolve
        sy "Like what you see?"
        scene ch4sc06_195 with dissolve
        mc "I love that tight little body of yours..."
        scene ch4sc06_197 with dissolve
        sy "Then I should probably come a little closer. So you can get a better view..."
        scene ch4sc06_201 with dissolve
        sy "Like this... Mnhh. Kiss me."
        scene ch4sc06_202 with dissolve
        sy "*Mwah* I feel like such a naughty little fae around you. MNhh *Lick*"
        scene ch4sc06_204 with dissolve
        sy "I’ll just take a peek down here for a bit... You don’t mind, do you?"
        scene ch4sc06_205 with dissolve
        mc "Mnhh... Definitely not. You'd better get a closeup..."
        scene ch4sc06_208 with dissolve
        $ renpy.pause(1)
        scene ch4sc06_209 with dissolve
        $ renpy.pause(1)
        sy "Mnhh... I love tasting your body..."
        scene ch4sc06_210 with dissolve
        sy "Let’s get this off. I want a proper taste! *Giggles*"
        mc "Mnh... They're starting to get a little tight."
        scene ch4sc06_211 with dissolve
        sy "*Moans* OHH! No wonder they felt so tight! You’re already ready for me!"
        sy "Mnhh... Hi again. I had no idea you liked my lips this much!"
        mc "*Chuckles* I think we both know how amazing your magical little lips are..."
        sy "Just in case... let me remind you!"
        scene ch4sc06_213 with dissolve
        sy "*Muffled* MNHH!! HNNHH!! AHHMH!!"
        scene ch4sc06_214 with dissolve
        sy "Mnhhh... MNghhHhghh..."
        scene sy_lewd4 with Dissolve(1)
        $ renpy.pause()
        sy "*Suck* Mnhh... Shoh ghoood! mnHh! *Lick*"
        "After edging your tip for a while, making sure you’re covered in her saliva, she begins moving."
        scene sy_lewd7 with Dissolve(1)
        $ renpy.pause()
        mc "Mnhh... Sylph... Keep going."
        sy "Mnhhh! ... Mh! Hnnhh... *Lick* Mnh..."
        scene sy_lewd6 with Dissolve(1)
        $ renpy.pause()
        mc "F-Fuck... That’s a good fae. I’m close..."
        scene ch4sc06_213 with dissolve
        sy "Mnh... Not so fast! I have an idea."
        scene black with Dissolve(1.5)
        $ renpy.pause(1)
        scene ch5sc10_246 with Dissolve(1.5)
        sy "W-What do you think?"
        mc "Beautiful."
        scene ch5sc10_247 with dissolve
        sy "Will you... uh... taste me?"
        sy "I... I’d like to... imprint my taste on you."
        scene ch5sc10_248 with dissolve
        mc "I’d love to taste you, Sylph. You’re my fairy. I intend to get very familiar with your taste."
        sy "R-Really?!"
        scene ch5sc10_249 with dissolve
        mc "Mnh... really. Get ready to imprint on me..."
        scene ch5sc10_250 with dissolve
        sy "I... I’ll get right on that. Mhhhh... Careful... Hnnghh... I’m hypersensitive right now."
        scene ch5sc10_249 with dissolve
        mc "Mnhh... I can even taste your magic down here... *Kiss*"
        scene ch5sc10_250 with dissolve
        sy "Mhhh... Y-yuup... As a fae, my entire body is brimming with magic. Every part of my skin, inside and out."
        scene ch5sc10_251 with dissolve
        mc "I love how smooth your thighs are. It’s like they’ve never been touched. So delicate."
        scene ch5sc10_252 with dissolve
        sy "Oohhh... Mnhh. Y-You know they’ve never been touched... until now. Mnhh!"
        scene ch5sc10_251 with dissolve
        sy "Please... [mc]! I-I can’t take much more... MH-nngh!"
        scene ch5sc10_252 with dissolve
        mc "Mnhh... Your scent is wonderful, Sylph. It’s like the forests on a rainy summer morning."
        scene ch5sc10_251 with dissolve
        sy "[mc]-Mnnhh! Please!"
        scene ch5sc10_252 with dissolve
        mct "{i}Heh ... She’s trembling with anticipation. Good. Let’s get a proper taste.{/i}"
        scene ch5sc10_253 with dissolve
        $ renpy.pause(1)
        with vpunch
        sy "{b}OH!! MH!! AiiYH! Y-Your tongue! AHhh!!{/b}"
        scene sy_lewd8 with Dissolve(1)
        $ renpy.pause()
        mc "*Licks* Mnhh... You’re so... Mnhh... wet. It’s practically running out of you. *Lick*"
        sy "*Moans* Ahh-MNh! Y-Yes! I know! I-I feel it! MNHH!! Taste me! Please..."
        sy "By the Earth-mother! Ahhh! I-Imprinting on you feels... MMmm!! ... amaaziiing!"
        scene sy_lewd9 with Dissolve(1)
        $ renpy.pause()
        with vpunch
        sy "OHhhhHH!! I love it! I love how your tongue feels inside me! MNH!!"
        mc "Sylph... You’re delicious. Mnhh... very unique."
        sy "Do you taste it? Mngghh! The magic in my juices? Mnhh!"
        mc "It’s incredible. So potent... Mnhh. *Lick*"
        sy "It’s-AHhh! All for you! [mc]!! Mnhh... This is what fae imprinting is all about. Ahhnh..."
        with vpunch
        sy "Absorbing your partner’s taste... Mnhh... Their scent... Their emotions... Ahhh! I’m-I’m!!"
        scene ch5sc10_254 with dissolve
        with vpunch
        sy "*Moans loudly* {b}AYYYHHH!! MHH-AHH!! YESS!!{/b} Don’t stop!"
        with vpunch
        scene ch5sc10_253 with dissolve
        sy "*Moans* Ohh... [mc]! K-Keep kissing my flower like that! AHhh!"
        scene ch5sc10_255 with dissolve
        $ renpy.pause(1)
        mct "{i}*Muffled* Mnhhh.. Mnhhh! Damn, I’ve never had a girl orgasm this much just from licking her.{/i}"
        mct "{i}I suppose being sensitive to my magic, combined with the pleasure, sends it far over the edge for her.{/i}"
        sy "*Panting* Hnnghh... T-That was incredible. Hnnghh... I almost can’t breathe. Mhhh."
        scene ch5sc10_258 with dissolve
        sy "*Panting softly* I can’t believe I just imprinted on you. Mnhh... Do you know what that means?"
        scene ch5sc10_256 with dissolve
        mc "*Kisses* Mnh... That you enjoyed it?"
        scene ch5sc10_258 with dissolve
        sy "I did. But, it's more than that... a Fae can only imprint once in her life. When she loves her partner."
        sy "I... I love you."
        scene ch5sc10_256 with dissolve
        ####Choice####
        menu:
            "I love you, Sylph.":
                scene ch5sc10_256 with dissolve
                mc "I love you too. You’re my little Fae."
                $ sylph_trust += 5
                "Sylph has fallen in love with you, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                scene ch5sc10_258 with dissolve
                sy "That I am!"
                sy "I love it when you call me that."
                scene ch5sc10_256 with dissolve
                mc "What? That you’re my little Fae?"
                scene ch5sc10_258 with dissolve
                sy "Mnhh... That. From this moment... for the rest of my life, that is what I’ll be. Yours."
                sy "Let’s get dressed, you don't have long before you have to be at the royal celebration."

            "Avoid.":
                scene ch5sc10_256 with dissolve
                mc "I really appreciate you sharing this with me. It means a lot, Sylph."
                $ sylph_trust -= 5
                "Sylph noticed you did not return her expression of feelings, her trust has decreased by {size=+3}{b}{color=#f00}5{/color}{/b}{/size}."
                scene ch5sc10_258 with dissolve
                sy "You’re welcome, I just wanted to make sure you knew what it meant."
                sy "Let’s get dressed, you don't have long before you have to be at the royal celebration."

        scene black with Dissolve(1.5)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)
        scene ch4sc06_177 with Dissolve(1.5)
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
        sy "Mnhhh..."
        mc "You’re not participating in the celebration?"
        scene ch4sc06_178 with dissolve
        sy "No, I’m a fairy. Remember what I told you about nobles, and how they like to use fairies?"
        scene ch4sc06_177 with dissolve
        mc "Right... the less their kind knows you’re here, the better."
        scene ch4sc06_178 with dissolve
        sy "Exactly! Also, I spent the entire morning making seals and enchantments around the castle."
        sy "And after all that? Puuuh! I need a warm, relaxing bath and a big’ol’rest! Yuup!"
        scene ch4sc06_177 with dissolve
        mc "Well-earned. You should probably order a massage while you’re at it."
        scene ch4sc06_180 with dissolve
        sy "I only want a massage if it’s from you."
        scene ch4sc06_181 with dissolve
        mc "Alright, I’ll owe you a massage then."
        sy "A deeeep massage... Real deep. Yuup! Full body, too!"
        mc "*Chuckles* Now you’re being greedy."
        scene ch4sc06_182 with dissolve
        sy "C’mere! *Mwah* Mnhh-Hnnhh..."
        sy "*Lick* I'm looking forward to that massage! Mnhh... Have fun tonight, okay? *Mwah*"
        mc "You too. Try to get some rest. *Kiss*"
        scene ch4sc06_184 with dissolve
        sy "Okay, go on. Get going before I strip you naked again. I still have to finish counting provisions."
        scene ch4sc06_185 with dissolve
        mc "Heh... Sure I’ll get going."


    else:
        scene black with Dissolve(1.5)

    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss13 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc10_259 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_260 with dissolve
    $ renpy.pause(1)
    scene ch5sc10_261 with dissolve
    am "Mhh... This is perfect. If only..."
    am "I had someone to share these moments with. *Sighs*"
    scene ch5sc10_262 with dissolve
    amt "So many men of the court will be trying to win my affections tonight..."
    amt "As if I’d fall in love with them just because they declare themselves available. Ugh!"
    scene ch5sc10_263 with dissolve
    amt "At least [mc] will be attending. He’s a nice distraction from all this royal nonsense."
    amt "But it’ll probably be hard to get some time alone with him, given that I’ll be the center of attention tonight."
    scene ch5sc10_264 with dissolve
    amt "Maybe... Maybe we'll find a chance to sneak away?"
    amt "Then he could tell me how beautiful I look. Maybe even take a step towards me..."
    scene ch5sc10_265 with dissolve
    amt "Mnhh... He'd gaze into my eyes and silence would wrap around us. Then he'd..."
    qm "Amelia? Honey? You need to finish up. You don’t want to be all wrinkly when the guests arrive."
    scene ch5sc10_266 with dissolve
    with vpunch
    am "Mother! Haven’t you heard of knocking?! Get out!"
    scene ch5sc10_267 with dissolve
    qm "Honey... I wanted to have a chat with you about tonight."
    am "Can we not, Mother?"
    scene ch5sc10_268 with dissolve
    qm "Amelia, it’s paramount you understand the importance of tonight."
    am "I’m not marrying any of those fools! Nobility, ugh! None of them has ever done anything noble!"
    scene ch5sc10_269 with dissolve
    qm "Sweetie, we’re not asking you to get married tonight. Just... give them a chance and get to know them."
    qm "Maybe you’ll be surprised? One of them could make a great match for you."
    scene ch5sc10_270 with dissolve
    am "Not likely! ... *Sigh* Whatever... I’ll be courteous of course, Mother."
    qm "Good. Your father has been very stressed lately. You know he’s under a lot of pressure from all sides."
    scene ch5sc10_271 with dissolve
    am "It’s not fair! Why should it fall to me to solve your problems?"
    am "He’s the High King! If he cares so much about the throne, then he should fight for it!"
    scene ch5sc10_272 with dissolve
    qm "Sweetie... you know it isn’t that simple. And at least you'll have some say in who you will marry."
    qm "I wasn’t afforded that luxury, but you don’t see me moping about it, do you?"
    scene ch5sc10_271 with dissolve
    am "No-But... I know you haven’t been happy since you married Father! I’m not blind!"
    scene ch5sc10_273 with dissolve
    qm "One good thing came from it, though. You. You’ve grown up to be a beautiful and strong woman."
    qm "Tonight, all eyes will be on you. What you choose to do with that, will be up to you."
    am "..."
    scene ch5sc10_274 with dissolve
    qm "I saw the dress Frida was laying out for you. You’ll look absolutely stunning tonight."
    qm "I’ll leave you to get ready. Our guests will be arriving within the hour, at sundown."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch4sc15_005 with Dissolve(1.5)
    $ renpy.pause(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch5sc10_275 with Dissolve(1.5)
    $ renpy.pause(1)
    lu "[mc]! Mhh! So glad you’re here. There’s something I want to show you!"
    mc "Happy to see you too. I have something to tell you, as well."
    scene ch5sc10_276 with dissolve
    lu "Whatever it is, it can wait! Prepare yourself to be amazed! Boggled! Astounded!"
    mc "*Chuckles* Okay, okay... you can go first."
    scene ch5sc10_277 with dissolve
    "Luna excitedly clears her throat."
    lu "You may enter!"
    mc "I’m feeling a little nervous. Are you nervous?"
    lu "As you should be! This is a pivotal moment between any boy and girl!"
    scene ch5sc10_278 with dissolve
    lu "The meeting of the in-laws! Tadaa!"
    mc "We’re not married..."
    lu "Yet! *Giggles softly* I know you two have already met, but that didn’t count 'cause I wasn’t there!"
    scene ch5sc10_279 with dissolve
    cas "Hey, [mc]. It’s good to see you again."
    cas "You’ve taken good care of my babygirl, I see."
    scene ch5sc10_280 with dissolve
    lu "Moooom!!"
    mc "Hey, Cassandra."
    mc "Likewise. I must say, I’m pleasantly surprised to see you here? How is this possible?"
    scene ch5sc10_281 with dissolve
    cas "It's thanks to my amazing daughter."
    cas "She found a magical loophole and exploited it."
    scene ch5sc10_282 with dissolve
    mc "I’m impressed! Well done, Luna."
    lu "I... It was nothing, really. But thank you."
    lu "I just crisped a few thugs... broke a steel lock... and re-bound the hex to a gemstone... the usual stuff."
    lu "Now Mother can go wherever the gem is."
    scene ch5sc10_283 with dissolve
    mc "As I said, I’m impressed. You’re pretty amazing."
    lu "*Whispers* {size=-10}{b}Y-You better stop complimenting me in front of my mother!{/b}{/size}"
    lu "*Whispers* {size=-10}{b} Or else..!{/b}{/size}"
    ####Choice####
    menu:
        "Tease her. ({color=#ff8cdd}Romance{/color})":
            scene ch5sc10_284 with dissolve
            mc "Or else what?"
            $ luna_path = True
            scene ch5sc10_283 with dissolve
            lu "I’ll have to... take action."
            scene ch5sc10_285 with dissolve
            mc "Is that so?"
            mc "Maybe I should take action first, then?"
            scene ch5sc10_286 with dissolve
            lu "*Whispers* {size=-10}{b}Mppphh!! Stop it! Mnhh ... She’s looking right at us!{/b}{/size}"
            mc "*Whispers* {size=-10}{b}Why so flustered, Luna? Are you getting excited?{/b}{/size}"
            lu "*Whispers* {size=-10}{b}No. Y-You’re wrong... I’m-I’m not feeling flustered! Mnhh...{/b}{/size}"
            scene ch5sc10_283 with dissolve
            $ luna_trust += 2
            lu "*Whispers* {size=-10}{b}You’ve no idea what you just started... Just you wait!{/b}{/size}"
            "Luna enjoys being playful with you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Don’t. (Neutral)":
            scene ch5sc10_283 with dissolve
            mc "Heh, alright, alright."

    scene ch5sc10_281 with dissolve
    cas "Shouldn’t you two be getting to the palace? The celebration is due to start any moment."
    cas "I obviously shouldn’t make an appearance tonight. Taron probably already knows I’ve escaped..."
    scene ch5sc10_279 with dissolve
    cas "But he has no idea how, or where I can be found."
    cas "I’d like to keep it that way. At least for now."
    scene ch5sc10_280 with dissolve
    mc "Of course."
    mc "Cassandra, I need to talk to you more about Taron, at some point."
    scene ch5sc10_279 with dissolve
    cas "Once everything quiets down, I'll be happy to tell you what I know."
    scene ch5sc10_280 with dissolve
    mc "Thank you, I appreciate that."
    scene ch5sc10_282 with dissolve
    mc "Shall we?"
    lu "You go ahead, I’ll meet you there."
    lu "I’ve gotta change real quick."
    mc "Sure. I'll see you there then."
    scene black with Dissolve(2)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss13 with Dissolve(2)
    $ renpy.pause()
    scene ch5sc10_287 with Dissolve(2)
    play music happy_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch5sc10_288 with dissolve
    $ renpy.pause()
    scene ch5sc10_289 with dissolve
    $ renpy.pause()
    scene ch5sc10_290 with dissolve
    $ renpy.pause()
    scene ch5sc10_291 with dissolve
    $ renpy.pause(1)
    da "Looks like a lot of people have already arrived."
    scene ch5sc10_292 with dissolve
    $ renpy.pause()
    scene ch5sc10_293 with dissolve
    $ renpy.pause()
    scene ch5sc10_294 with dissolve
    $ renpy.pause()
    scene ch5sc10_295 with dissolve
    $ renpy.pause()
    scene ch5sc10_296 with dissolve
    $ renpy.pause()
    scene ch5sc10_297 with dissolve
    $ renpy.pause()
    scene ch5sc10_298 with dissolve
    $ renpy.pause()
    scene ch5sc10_299 with dissolve
    $ renpy.pause()
    scene ch5sc10_300 with dissolve
    $ renpy.pause()
    elt "I can’t believe I’m standing in the royal palace!!"
    elt "There are so many people here already."
    scene ch5sc10_301 with dissolve
    $ renpy.pause()
    scene ch5sc10_302 with dissolve
    $ renpy.pause()
    scene ch5sc10_303 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc10_304 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mc "Hey... You ready?"
    scene ch5sc10_306 with dissolve
    am "[mc], Hi... You decided to accept my invitation!"
    scene ch5sc10_307 with dissolve
    mc "I wasn’t about to miss out on your 20th name day..."
    mc "Besides, it's not every day you get a personal invitation from a princess."
    scene ch5sc10_306 with dissolve
    am "No... It certainly isn't. *Giggles softly*"
    scene ch5sc10_308 with dissolve
    am "..."
    mc "Feeling nervous?"
    scene ch5sc10_309 with dissolve
    am "No..."
    am "Maybe a little? ... But it’s better now that you’re here."
    scene ch5sc10_307 with dissolve
    mc "Don’t worry, I’ll be here all night."
    mc "You look beautiful, by the way."
    scene ch5sc10_306 with dissolve
    am "T-Thank you."
    am "You too."
    am "I mean... you look handsome tonight."
    scene ch5sc10_304 with dissolve
    mc "Shall we?"
    am "*Nods* Mhm."
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(1)
    stop music fadeout 1.0
    jump ch5sc11

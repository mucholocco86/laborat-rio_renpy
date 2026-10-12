label ch3sc18:

    window hide dissolve
    play music tavern_3 fadein 1.0
    scene black with Dissolve (1.0)
    $ renpy.pause(1)
    scene ch3sc18_intro with Dissolve(2.0)
    $ renpy.pause(2)
    scene ch3sc18_001 with Dissolve(2.0)
    $ renpy.pause()
    mct "..."
    scene ch3sc18_002 with dissolve
    mct "*Sigh* Crowds..."
    scene ch3sc18_003 with dissolve
    $ renpy.pause(2)
    scene ch3sc18_004 with dissolve
    $ renpy.pause(2)
    scene ch3sc18_002 with dissolve
    mct "I hate crowds..."
    mct "I much prefer the inns on the road."
    scene ch3sc18_005 with dissolve
    el "Hmm? You haven't sat down yet?"
    el "Feeling out of place?"
    scene ch3sc18_006 with dissolve
    mc "Not anymore."
    menu:
        "Compliment her.":
            scene ch3sc18_007 with dissolve
            mc "Beautiful as ever, I see."
            scene ch3sc18_008 with dissolve
            el "[mc]... Thank you..."
            el "You look handsome as well."
            $ eliza_trust += 1
            "Eliza’s trust increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

        "Don’t keep Borri waiting.":
            scene ch3sc18_007 with dissolve
            mc "Let’s not keep Borri waiting. I’m sure he’s already three ales deep."
            scene ch3sc18_008 with dissolve
            el "Right! Let’s get our drink on!"

    scene black with Dissolve(1)
    scene ch3sc18_009 with dissolve
    br "Ahh! The beauty and the brute!"
    br "Come! Sit, sit! Before ye ales go stale!"
    scene ch3sc18_010 with dissolve
    el "Hi Borri!"
    el "Always a charmer I see! *Giggling*"
    scene ch3sc18_011 with dissolve
    mc "Charmer?"
    mc "He just called me a brute!"
    scene ch3sc18_012 with dissolve
    el "Well he’s not wrong, is he?"
    el "Besides, he called me a beauty!"
    el "Now scoot over and make some room for your butt-buddy!"
    scene ch3sc18_013 with dissolve
    mct "*Chuckles* ..."
    mct "It's nice to see her be this playful, even in front of others."
    scene ch3sc18_014 with dissolve
    br "*Scoffs* Hah! I told ye this lass is a keeper!"
    br "Beauty and wits! That's a lass who'll keep ye on yer toes!"
    scene ch3sc18_015 with dissolve
    el "You’re as cheerful as always, Borri."
    el "I still can’t believe [mc] convinced you to join the guild."
    scene ch3sc18_014 with dissolve
    br "Aye, nearly couldn’t believe it m’self, lass!"
    br "But he made a mighty convincing argument."
    scene ch3sc18_015 with dissolve
    el "Oh? Pray tell. How did he seduce you?"
    el "Don't tell me that he promised you that the guild was filled with female dwarves in need of aid?"
    scene ch3sc18_016 with dissolve
    mc "*Chuckles* I didn't need to sell him that hard."
    mc "All I said was that it pays decent coin."
    scene ch3sc18_014 with dissolve
    br "As I said, mighty convincing!"
    br "I know it's not exactly the most noble of causes te join a guild..."
    scene ch3sc18_015 with dissolve
    el "Everyone has their own reasons for joining the different guilds in Luxenford..."
    scene ch3sc18_017 with dissolve
    el "If coin is your motivation, I definitely won’t judge you for yours, Borri."
    el "Besides, it is one of our main reasons for joining as well."
    scene ch3sc18_014 with dissolve
    br "Arrh Lass! Yer too kind."
    scene ch3sc18_018 with dissolve
    br "Ye got a heart o' gold! If only ye were a dwarf."
    br "M'wife would shiver in her boots! Hah!"
    scene ch3sc18_019 with dissolve
    el "*Giggles*"
    scene ch3sc18_020 with dissolve
    el "Hear that, [mc]?"
    mct "Great, here we go..."
    el "Beautiful, witty and a heart of gold! I'm a keeper!"
    scene ch3sc18_021 with dissolve
    mc "*Sigh* Please don't inflate her ego any further..."
    mc "It’ll be good to have you around the guild though, Borri."
    mc "Things won’t be boring, that's for sure."
    scene ch3sc18_014 with dissolve
    br "Aye! I’ll keep ye on yer toes, lad!"
    br "Cheers to friendship and new opportunities ahead!"
    scene ch3sc18_022 with dissolve
    el "To new friendships!"
    scene ch3sc18_023 with dissolve
    with vpunch
    evr "{b}Cheers!!{/b}"
    scene ch3sc18_024 with dissolve
    sl "Hi guys!"
    sl "I see you’ve already begun downing ales."
    scene ch3sc18_025 with dissolve
    el "Selena! Hi!"
    el "Sit, sit! We’ve only just begun."
    scene ch3sc18_026 with dissolve
    sl "Are you sure I’m not disturbing?"
    sl "I don’t want to intrude on your celebrations."
    scene ch3sc18_027 with dissolve
    br "Hah! Don’t talk nonsense, lass!"
    br "The more, the merrier, I say! And it seems yer friends already, so why be shy?"
    br "Come! Sit! Drink!"
    scene ch3sc18_028 with dissolve
    sl "Right... silly me!"
    sl "In that case I think I will join you for a drink!"
    if selena_kiss == True:
        scene ch3sc18_029 with dissolve
        mct "Selena keeps looking at me with those seductive eyes..."
        mct "I guess our kiss from earlier is still on her mind."
        scene ch3sc18_028 with dissolve
        $ renpy.pause(1)
        sl "It definitely seems like a festive little group we've got. *Snickers*"
        sl "Sorry I took so long to find you, I had to freshen up after a rather... heated moment earlier."
        scene ch3sc18_030 with dissolve
        sl "What were you toasting to?"
    else:
        scene ch3sc18_030 with dissolve
        sl "What were you toasting to?"

    scene ch3sc18_031 with dissolve
    el "Friendship!"
    scene ch3sc18_032 with dissolve
    br "New opportunities!"
    scene ch3sc18_031 with dissolve
    el "Adventure!"
    scene ch3sc18_032 with dissolve
    br "Sacks filled with coin!"
    scene ch3sc18_033 with dissolve
    mc "See what I have to deal with?"
    scene ch3sc18_034 with dissolve
    sl "*Giggles* I can imagine how much trouble these two can be!"
    sl "Would be hard to deal with for most men..."
    scene ch3sc18_035 with dissolve
    sl "Not you though, you're the type of man who handles trouble with ease... I know from experience."
    scene ch3sc18_017 with dissolve
    el "Yeah, you've seen him first hand today."
    el "What did you think?"
    scene ch3sc18_035 with dissolve
    sl "Oh I think he's someone worthy of a cheer, allow me to add to the cheer?"
    sl "Hmm... to new beginnings? And new relations..."
    scene ch3sc18_036 with dissolve
    el "I'll definitely cheer to that! Cheers!"
    scene ch3sc18_037 with dissolve
    with vpunch
    br "Aye! {size=+5}{b}CHEERS!{/b}{/size}"
    scene ch3sc18_038 with dissolve
    with vpunch
    evr "{size=+5}{b}CHEERS!{/b}{/size} *Laughs*"
    scene ch3sc18_039 with dissolve
    evr "To unlikely friendships and new adventures!"
    evr "{size=+5}{b}CHEERS!{/b}{/size}"
    scene ch3sc18_040 with dissolve
    mct "Heh. It’s good to see them all get along so well."
    mct "Friendship huh? I guess it can’t be helped at this point..."
    if selena_kiss == True:
        scene ch3sc18_041 with dissolve
        with vpunch
        mct "Huh! Is that?"
        scene ch3sc18_042 with dissolve
        $ renpy.pause(1)
        sl "*Snickers* ..."
        "You feel something soft, gently moving up your shin."
        scene ch3sc18_041 with dissolve
        mct "What is she thinking?"
        mct "Right here in front of the others?"
        scene ch3sc18_043 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_043_b with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_043 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_043_b with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_042 with dissolve
        "Selena keeps her gaze fixed upon you as she moves her naked foot further up..."
        scene ch3sc18_043_b with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_044 with dissolve
        "Once she makes contact with your crotch, she begins rubbing her foot back and forth."
        $ renpy.pause(1.5)
        scene ch3sc18_044_b with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_044 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_044_b with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_044 with dissolve
        $ renpy.pause(1.5)
        scene ch3sc18_045 with dissolve
        mct "F-Fuck... that feels good."
        ###Choice###
        menu:
            "Stop her.":
                scene ch3sc18_046 with dissolve
                $ renpy.pause(1)
                scene ch3sc18_047 with dissolve
                $ renpy.pause(1)
                scene ch3sc18_047_b with dissolve
                $ selena_trust -= 2
                "Selena didn't like that you didn't play along, her trust has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."

            "Let her continue. ({color=#ff8cdd}Romance{/color})":
                scene ch3sc18_046 with dissolve
                mct "She's such a little vixen. Teasing me right in front of the others."
                mct "Two can play this game."
                "You hold firmly onto her naked foot squeezing it tenderly in your palm while you begin moving it."
                $ renpy.pause(1.5)
                scene ch3sc18_046_b with dissolve
                $ renpy.pause(1.5)
                scene ch3sc18_046 with dissolve
                $ renpy.pause(1.5)
                scene ch3sc18_046_b with dissolve
                $ renpy.pause(1.5)
                scene ch3sc18_042 with dissolve
                slt "Oh! He’s playing along!"
                slt "Mmhm... Naughty, [mc]."
                scene ch3sc18_049 with dissolve
                slt "He’s... Mhhh! He’s really big!"
                slt "Gosh! The way he’s rubbing me with his palm!!"
                slt "The things I want him to do to me... Hnhnhh!"
                $ selena_trust += 2
                "Selena enjoyed that you were down to play, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene ch3sc18_041 with dissolve
                mct "Fuck... better stop before the others notice."
                scene ch3sc18_050 with dissolve
                mc "To friendship and all that... cheers!"
    else:
        scene ch3sc18_050 with dissolve
        mc "To friendship and all that... cheers!"

    scene ch3sc18_035 with dissolve
    sl "My, my. Look at that, guys! He cheered!"
    sl "I wonder what got him in the mood? *Snickers*"
    scene ch3sc18_051 with dissolve
    el "I know! I'm as surprised as you."
    el "How much did you have to drink, [mc]?"
    mc "..."
    scene ch3sc18_037 with dissolve
    br "Hah! Two pretty girls is all it takes te get yer flustered, lad?"
    br "Don’t ye worry, Borri will show ye how te handle the lasses!"
    scene ch3sc18_031 with dissolve
    el "Right... let’s go get some more ales, Selena."
    el "Then the boys can talk their nonsense."
    scene ch3sc18_034 with dissolve
    sl "Great idea! *Snickers*"
    sl "I’ll be needing more if I have to listen to Borri give relationship advice!"
    scene ch3sc18_052 with dissolve
    el "*Whispers* {size=-7}{b}Please don’t take advice about women from Borri...{/b}{/size}"
    el "*Whispers* {size=-7}{b}Personally, I think you’re doing well already.{/b}{/size}"
    scene ch3sc18_053 with dissolve
    el "We’ll be back in a bit."
    scene ch3sc18_054 with dissolve
    br "Arrrh Don’t listen to them lad..."
    br "I’ve been married for five summers and happily so!"
    scene ch3sc18_055 with dissolve
    mc "Didn’t you mention that your wife told you not to return unless you found a fountain of gold?"
    mc "And that she would skin your ass if you dare return without pockets filled to the brim?"
    scene ch3sc18_056 with dissolve
    br "Shh, lad! Keep it down, will ye? It was in the heat of the moment..."
    br "Ye know how it is... tempers flare when coin is low."
    scene ch3sc18_057 with dissolve
    br "Surely she couldn’t have been serious... right?"
    scene ch3sc18_055 with dissolve
    mc "*Chuckles* I’m guessing you took it pretty seriously?"
    mc "You’re joining the guild in pursuit of coin, after all."
    scene ch3sc18_058 with dissolve
    br "Damnit, ye have a point! It will be a while till I can return home."
    br "Argh... have I been foolin me'self? "
    ###CHOICE###
    menu:
        "Encourage him. ({color=#87e1fa}Charisma{/color})":
            scene ch3sc18_059 with dissolve
            mc "Don’t worry about it, Borri. I’m sure you will be able to make a great profit with the guild."
            $ charisma += 1
            mc "And when you do, you will return to your wife with purses filled to the brim."
            "Borri appreciate you encouraging his new path, his trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch3sc18_060 with dissolve
            br "I like the way ye think!"
            br "Aye it will sort itself... I just have to give it time."
            $ borri_trust += 2
            scene ch3sc18_059 with dissolve
            mc "That's right, focus on the guild for now and everything will fall into place."
            "Your attempt to encourage Borri was a {b}Success! {color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

        "Shift his focus. ({color=#ffee54}Leadership{/color})":
            scene ch3sc18_059 with dissolve
            mc "Don’t bother worrying about your wife."
            mc "You’re the one out here trying to make ends meet for the two of you."
            $ leadership += 1
            mc "She should support you and appreciate your efforts."
            mc "And if she doesn't, maybe you should find someone who does."
            scene ch3sc18_057 with dissolve
            br "Hmmmh... ye have a point lad. Busting me balls every chance she gets!"
            br "Bloody woman... does she really care for me? ... *Sigh*"
            scene ch3sc18_059 with dissolve
            mc "Follow my lead, and your wife will be begging for you to take her back."
            mc "And when she does, it'll be up to you whether or not you still want her."
            scene ch3sc18_057 with dissolve
            br "Hmmmh... begging te be taken back by me?"
            br "Does sound musical to me ears... aye."
            scene ch3sc18_054 with dissolve
            br "Alright lad! Ye do seem to know a thing or two about women..."
            $ borri_trust += 2
            "Borri’s trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            br "Ol' Borri will follow yer lead and win his wife back!"
            "Your attempt to sway Borri was a {b}Success! {color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

    scene ch3sc18_060 with dissolve
    $ renpy.pause(0.5)
    br "Cheers fer the advice lad! Ye have given me much te look forward te!"
    scene ch3sc18_061 with dissolve
    $ renpy.pause(0.5)
    "Meanwhile the girls stands by the bar, awaiting the ales."
    scene ch3sc18_062 with dissolve
    $ renpy.pause()
    el "Hey Selena..."
    sl "Hmm?"
    el "I hope you don’t mind..."
    scene ch3sc18_063 with dissolve
    el "[mc] told me he ran into you earlier."
    el "Is everything okay?"
    scene ch3sc18_064 with dissolve
    sl "Oh, yeah."
    sl "In fact, he helped me with a bad man... someone from my past who just couldn’t seem to let go."
    scene ch3sc18_065 with dissolve
    el "If you ever, you know... need someone to talk to, I'm a good listener."
    scene ch3sc18_066 with dissolve
    sl "Awwh! Eliza! That's really sweet of you."
    sl "I will keep it in mind if I feel a need for it."
    scene ch3sc18_065 with dissolve
    el "Is it all sorted now, though?"

    if thug_1_dead == True:
        scene ch3sc18_066 with dissolve
        sl "Yeah, I don't think that guy will be causing me any further issues."
        scene ch3sc18_068 with dissolve
        slt "[mc] he really did protect me without hesitation... killing that bastard with ease."
        slt "He's just made life for my sister and me so much simpler, by the gods he's so fine..."
        scene ch3sc18_066 with dissolve
        sl "[mc] took care of the bastard. He didn't even break a sweat!"
        sl "And he hasn't even asked for anything in return, he's really quite the man."
        scene ch3sc18_065 with dissolve
        el "Yeah... [mc] tends to protect anyone that he cares about as a friend."
        el "So if he chose to protect you, he's definitely seen something good in you, something worth protecting."
        scene ch3sc18_066 with dissolve
        sl "I don't know about that... but if he did, I hope can I live up to whatever he saw."

    else:
        scene ch3sc18_066 with dissolve
        sl "It would seem so."
        sl "[mc] took care of it. He didn't even break a sweat!"
        scene ch3sc18_065 with dissolve
        el "Yeah... [mc] tends to have that effect on anyone that harms his friends."
        el "He has a lot of walls up but..."


    scene ch3sc18_067 with dissolve
    el "He doesn't like to show it... but he has a kind heart."
    el "He protects those he cares about relentlessly."
    scene ch3sc18_068 with dissolve
    $ renpy.pause(0.5)
    bth "*Giggling* ..."
    scene ch3sc18_069 with dissolve
    $ renpy.pause(0.5)
    br "*Chuckles* Heh! Cheers te that!"
    scene ch3sc18_070 with dissolve
    sl "He’s quite special."
    scene ch3sc18_071 with dissolve
    el "He sure is."
    scene ch3sc18_070 with dissolve
    sl "And handsome."
    scene ch3sc18_071 with dissolve
    el "Yeah... very."
    scene ch3sc18_070 with dissolve
    sl "Don't you just wanna grab him and kiss those manly lips?"
    scene ch3sc18_071 with dissolve
    el "Y-Yeah... more than anything"
    scene ch3sc18_072 with dissolve
    sl "*Laughs* Should we find a tree where you and [mc] can sit and make out?"
    scene ch3sc18_073 with dissolve
    el "Wai-"
    el "I didn’t mean anything by that!"
    el "I-I was just spacing out! Y-Yeah..."
    scene ch3sc18_074 with dissolve
    sl "Hey, I’m not judging, how could I? I agree with all of it."
    sl "He's the most attractive man I've met since I first started noticing boys..."
    scene ch3sc18_075 with dissolve
    el "Y-You... you’re interested in [mc]?"
    el "*Mumbles* {size=-10}{b}G-Great... I knew it...{/b}{/size}"

    if eliza_path == True:
        if selena_path == True:
            elt "I knew they had kissed, [mc] told me... but I thought maybe it was a fleeting moment of attraction."
            elt "This confirms it though, she's totally into him! And she's super beautiful..."

        else:
            pass
    else:
        pass

    scene ch3sc18_076 with dissolve
    sl "He’s definitely caught my eye. He’s very interesting."
    sl "I’ve honestly never met anyone like him."
    scene ch3sc18_077 with dissolve
    sl "He seems so calm and collected most of the time, but he clearly cares a lot about people that are close to him."
    sl "I can tell he’s willing to go through fire to protect anyone he cares about."
    scene ch3sc18_076 with dissolve
    sl "I find those qualities very attractive..."
    scene ch3sc18_075 with dissolve
    el "I-I see... He's not serious all the time, though."
    scene ch3sc18_078 with dissolve
    "Eliza's eyes light up as she begins praising you."
    el "He has a fun side too! Mhm-hm!"
    el "Sometimes, when it’s just me and him, he relaxes and allows himself to have a bit of fun, he can be both goofy and playful!"
    el "We've even been swimming together! That was so much fun!"
    el "Well it was... until an assassin showed up and tried to kill us."
    scene ch3sc18_079 with dissolve
    el "It just takes a lot for him to be open with people. He’s been through a lot from a young age."
    el "More than most of us will ever understand."
    scene ch3sc18_080 with dissolve
    sl "You really care about him, huh?"
    scene ch3sc18_081 with dissolve
    $ renpy.pause(0.5)
    "Upon being confronted about her feelings for you, Eliza begins to turn red."
    scene ch3sc18_082 with dissolve
    $ renpy.pause(0.5)
    "Her face keeps blushing the more she thinks about how much she likes you."
    scene ch3sc18_083 with dissolve
    el "I... I do."
    scene ch3sc18_084 with dissolve
    sl "Oh, my! You’re red like a tomato!"
    sl "I guess you more than just 'like' [mc]!"
    scene ch3sc18_082 with dissolve
    el "!!"
    scene ch3sc18_083 with dissolve
    el "Selena! Not so loud."
    scene ch3sc18_084 with dissolve
    sl "*Whispers* {size=-10}{b}Right! My bad.{/b}{/size}"
    scene ch3sc18_085 with dissolve
    sl "Let’s head back to the boys, shall we?"
    sl "No telling what silliness Borri is trying to fill [mc]’s head with."
    scene ch3sc18_086 with dissolve
    el "*Giggling* Nothing good, I imagine!"
    scene ch3sc18_087 with dissolve
    sl "Heeey boys! Did you miss us?"
    scene ch3sc18_055 with dissolve
    mc "Hey."
    scene ch3sc18_088 with dissolve
    el "*Whispers* {size=-10}{b}Hi...{/b}{/size}"
    ###CHOICE###
    menu:
        "Be flirtatious.":
            scene ch3sc18_089 with dissolve
            mc "*Whispers* {size=-7}{b}Hey gorgeous.{/b}{/size}"
            scene ch3sc18_090 with dissolve
            mc "*Whispers* {size=-7}{b}I missed you.{/b}{/size}"
            scene ch3sc18_091 with dissolve
            el "*Whispers shyly* {size=-7}{b}I-I’ve missed you too... Mhmh.{/b}{/size}"
            scene ch3sc18_090 with dissolve
            mc "*Whispers* {size=-7}{b}I can't wait to get you alone...{/b}{/size}"
            scene ch3sc18_091 with dissolve
            el "*Whispers shyly* {size=-7}{b}You're going to make me blush... quit it! *Giggles*{/b}{/size}"
            scene ch3sc18_090 with dissolve
            $ renpy.pause(1.5)
            "Eliza likes being caressed by you, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ eliza_trust += 1

        "Be annoyed.":
            scene ch3sc18_092 with dissolve
            mc "Hey. Finally, you’re back. Took you long enough..."
            scene ch3sc18_093 with dissolve
            el "We weren’t gone that long, were we?"
            el "We just talked a bit."
            $ eliza_trust -= 1
            scene ch3sc18_092 with dissolve
            mc "*Sigh* I'm sorry."
            mc "I feel a bit on edge after today..."
            scene ch3sc18_093 with dissolve
            el "Don't worry about it..."
            el "It's been hectic since we arrived at Luxenford..."
            "Eliza appreciates your apology but did not like you being cross with her, her trust has decreased by {size=+3}{b}{color=#f00}1{/color}{/b}{/size}."

        "Be neutral.":
            scene ch3sc18_089 with dissolve
            mc "Hey. You guys good?"
            scene ch3sc18_093 with dissolve
            el "Oh, for sure!"
            el "What about you guys?"
            scene ch3sc18_089 with dissolve
            mc "*Chuckles* We're fine as well."

    scene ch3sc18_020 with dissolve
    el "He didn’t teach you too many of his {b}'tricks'{/b} I hope?"
    scene ch3sc18_037 with dissolve
    br "Wah? I have no tricks lass!"
    br "Just solid advice coming from years o' experience! Ain’t it right, lad?"
    scene ch3sc18_021 with dissolve
    mc "Keep me out of it."
    scene ch3sc18_096 with dissolve
    br "Barhh!"
    br "Anywho... Selena, how did ye meet these two rascals?"
    scene ch3sc18_035 with dissolve
    sl "I was their first Quest!"
    scene ch3sc18_036 with dissolve
    el "Phrasing, Selena. Phrasing!"
    el "That sounds so naughty!"
    scene ch3sc18_034 with dissolve
    sl "*Giggles* Well it’s true!"
    sl "They had a Quest to stop wolves hunting the horses at the stables I work at."
    scene ch3sc18_096 with dissolve
    br "Ah, wolves."
    br "I’ve met my fair share on my routes making deliveries... they usually keep to the deeper woods."
    scene ch3sc18_097 with dissolve
    br "But every now and then, a few bold wolves try to sneak some food from the caravans, or spook some horses so they run away at night."
    scene ch3sc18_098 with dissolve
    sl "Yeah, these had already chased one of our horses away. Maybe they even ate it..."
    sl "So now we can’t sell horses for a while until they have started breeding again."
    scene ch3sc18_096 with dissolve
    br "Good thing these two managed te help out."
    br "If there’s one thing they are good at, it’s helping people who need it."
    scene ch3sc18_022 with dissolve
    el "Mh-hm! That's what we do!"
    el "Even when a certain someone starts off by rudely shouting at us..."
    scene ch3sc18_057 with dissolve
    br "Ahhrh... Ye didn’t deserve that."
    br "I was a little hotheaded... I shan't deny it."
    scene ch3sc18_035 with dissolve
    sl "Ah, rough beginning. But it seems you’re all good friends now."
    scene ch3sc18_096 with dissolve
    br "These two couldn’t resist my dwarven charms, lass!"
    br "They didn’t even get mad at me! Well, except fer a small but deserved scolding from Eliza."
    scene ch3sc18_034 with dissolve
    sl "Awwh, cute!"
    scene ch3sc18_036 with dissolve
    el "[mc] and I have been traveling on our own for a while."
    el "I didn’t expect us to make such good friends this fast coming here."
    scene ch3sc18_014 with dissolve
    br "Well, how could ye not? Yer a sweetheart Eliza!"
    scene ch3sc18_018 with dissolve
    br "[mc]... well, not much sweetness te him."
    br "But he's a good lad."
    scene ch3sc18_035 with dissolve
    sl "I don’t know, Borri."
    sl "I think [mc] has a sweet side... You just have to earn it."
    scene ch3sc18_055 with dissolve
    mc "No, Borri was right."
    scene ch3sc18_035 with dissolve
    sl "We’ll see, I have a feeling you won’t keep it hidden for long."
    scene ch3sc18_099 with dissolve
    elt "Is she flirting with him?"
    elt "She just asked me how I felt about him when we were at the bar..."
    scene ch3sc18_100 with dissolve
    elt "No, I’m being silly. Why am I even feeling jealous?"
    elt "It's not like I own him. She's free to like him as well."
    elt "[mc]'s a man as well, he can enjoy as many women as he desires... such is our society."
    elt "But that doesn't mean I have to like it! Not one bit!"
    scene ch3sc18_035 with dissolve
    sl "Eliza told me you can be quite sweet to those you care about."
    sl "I hope to be one of them some day... if I'm not already?"
    scene ch3sc18_099 with dissolve
    elt "'I hope to be one of them some day.' Ughrr!"
    elt "Where does she even come up with this horseshit?"
    scene ch3sc18_101 with dissolve
    elt "Oh, right! She works at a stable! *Giggles*"
    elt "Maybe if she spent less time flirting with [mc] and more time attending the horses she wouldn't need aid?"
    scene ch3sc18_100 with dissolve
    elt "*Sighs* No, I shouldn't think like that... that's mean."
    elt "But she could at least make her flirting less obvious and not... right in front of my face."
    scene ch3sc18_033 with dissolve
    mc "She lied. I don’t have a sweet side."
    mc "You'd have better luck finding a sweet Rocktroll."
    scene ch3sc18_042 with dissolve
    $ renpy.pause(1)
    sl "*Snickers* Mh-hmm..."
    scene ch3sc18_102 with dissolve
    sl "I suppose I will just have to... pull the sweetness out of you."
    sl "Every. Last. Drop."
    scene ch3sc18_099 with dissolve
    elt "Okay! What the heck, Selena?? Urrgh!"
    elt "I don't care if it's mean, I hope she trips and falls face first into a pile of horse manure!"
    scene ch3sc18_101 with dissolve
    elt "*Giggles* Yes... that would definitely be fitting with how she's acting right now!"
    scene ch3sc18_043 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc18_043_b with dissolve
    $ renpy.pause(0.5)
    scene ch3sc18_043 with dissolve
    $ renpy.pause(0.5)
    scene ch3sc18_043_b with dissolve
    $ renpy.pause(0.5)
    scene ch3sc18_055 with dissolve
    mc "I’m heading to bed."
    mc "I’ll need to be rested for tomorrow's Quest. Thanks for the ales."
    scene ch3sc18_035 with dissolve
    sl "Awwh, okay."
    sl "It was nice hanging with you guys!"
    scene ch3sc18_098 with dissolve
    sl "Nice to meet you, Borri!"
    sl "I better get going... the stables aren't that close."
    scene ch3sc18_097 with dissolve
    br "I’ll walk ye home, lass."
    br "Don’t even try te say otherwise, no lass should walk on her own at night."
    scene ch3sc18_098 with dissolve
    sl "Thank you, Borri."
    sl "That’s very kind of you... I would feel better with an escort."
    scene ch3sc18_036 with dissolve
    el "See you guys!"
    sl "Goodnight you two!"
    br "See yer around the guild! Goodnight!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch3sc18_093 with Dissolve(1.5)
    el "She was flirting with you..."
    el "I think the whole tavern noticed!"
    ###CHOICE###
    menu:
        "Someone else had my attention. ({color=#ff8cdd}Eliza Romance{/color} & {color=#2bff8b}Selena friendship{/color})":
            scene ch3sc18_089 with dissolve
            mc "Was she? I didn’t notice. Someone else had my attention."
            mc "Someone incredibly mesmerizing."
            $ eliza_relationship = True
            scene ch3sc18_088 with dissolve
            el "You're sweet..."
            el "You always know what to say..."
            $ eliza_trust += 2
            "Eliza’s likes that you're focused on her, her trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch3sc18_089 with dissolve
            mc "Just being honest."
            mc "Nobody compares you to, especially not Selena."
            scene ch3sc18_088 with dissolve
            $ eliza_path = True
            el "Mhh, I like your honesty!"
            el "I'm really glad you didn't return her flirting, especially in front of me."
            el "Let’s head to bed?"
            el "I’m in desperate need of a cuddle!"
            scene ch3sc18_089 with dissolve
            mc "Say no more!"
            scene black with Dissolve(1.5)
            $ renpy.pause(1)
            scene ch3sc18_104 with Dissolve(1.5)
            $ renpy.pause(1)
            scene ch3sc18_105 with dissolve
            el "Mmhm... this is nice."
            el "Your body is so warm. Is it always like this?"
            scene ch3sc18_106 with dissolve
            mc "Pretty much."
            mc "Even when I’ve been in cold regions up north, my body always keeps warm."
            scene ch3sc18_105 with dissolve
            el "It must be a Nephilim thing."
            scene ch3sc18_104 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_105 with dissolve
            el "Your scars... do they... hurt? I don't want to harm you by feeling them."
            scene ch3sc18_106 with dissolve
            mc "No... they've been completely healed for several years now, as you know."
            mc "You can feel them if you like."
            scene ch3sc18_105 with dissolve
            el "Like this?"
            stop music fadeout 1.0
            el "Maybe they will heal if I do this?"
            scene ch3sc18_107 with Dissolve(1.5)
            play music lewd_1 fadein 1.0
            $ renpy.pause(1)
            "She runs her fingers down your chest towards your ribs while she plants tender kisses along the way."
            el "Nnhhnhh..."
            scene ch3sc18_108 with dissolve
            $ renpy.pause()
            mct "I don't think I've ever felt anything as soft as her sweet lips..."
            $ selena_path = False
            mct "Every time she moves, it feels like her lips almost stick to my skin, not wanting to lose contact."
            scene ch3sc18_109 with dissolve
            "She begins switching between placing wet kisses on your skin, and gently sucking along your scars."
            $ renpy.pause()
            mc "Fuck... Eliza. That feels incredible."
            "As you praise her efforts, she traces your scars with her tongue, licking carefully back and forth."
            scene ch3sc18_110 with dissolve
            $ renpy.pause(1.5)

            ####Animation####
            show el_lick1 with fade
            $ renpy.pause(2, hard=True)
            el "*Soft moan* Mmhmh... Mhhnn..."
            elt "I love licking him! Nhnn..."
            "She keeps running her tongue gently along your scars-"
            "-Then you feel her hand brushing back and forth against your cock."
            elt "Mhmhmhh... He's already hard! He must really like me licking him. Mnhh..."
            mc "Eliza... Fuck. You're driving me insane here."
            el "*Soft moan* Mmmh... Ghoood! Nhhhnnmm."
            scene ch3sc18_109 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_108 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_107 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_105 with dissolve
            el "That’s all for tonight!"
            scene ch3sc18_106 with dissolve
            mc "You tease..."
            scene ch3sc18_105 with dissolve
            el "*Giggles softly* Can't a kitten lick her lion these days?"
            scene ch3sc18_106 with dissolve
            mc "You can lick me anytime you want... somehow you manage to make it both naughty and intimate."
            scene ch3sc18_105 with dissolve
            el "Good... then my tongue conveyed my feelings perfectly."
            el "*Purrs softly* Nhyahh... Goodnight, my Lion."
            scene ch3sc18_106 with dissolve
            mc "Goodnight, my Kitten..."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            $ renpy.pause(0.5)
            jump ch3sc19

        "Yeah I noticed... She’s cute. ({color=#ff8cdd}Selena Romance{/color} & {color=#2bff8b}Eliza friendship{/color})":
            scene ch3sc18_089 with dissolve
            mc "Selena is cute, I don’t mind her flirting a little."
            $ selena_trust += 2
            "Selena’s trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch3sc18_093 with dissolve
            $ eliza_path = False
            el "I could tell."
            el "Let’s just go to sleep... I'm exhausted!"
            $ eliza_trust -= 2
            "Eliza isn't too keen on the idea of Selena flirting with you, her trust has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            scene ch3sc18_103 with Dissolve(1.5)
            $ eliza_relationship = False
            el "Goodnight..."
            $ selena_path = True
            mc "Goodnight."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            $ renpy.pause(0.5)
            jump ch3sc19

        "Two beautiful women flirting with me? ({color=#ff8cdd}Harem{/color})":
            scene ch3sc18_089 with dissolve
            mc "Having two beautiful women vying for my attention, I'm a lucky guy."
            mc "Especially with one of them being you."
            $ harem_path = True
            scene ch3sc18_093 with dissolve
            el "If you weren't so damn sweet, I'd punch you! *Scoffs*"
            mc "You wouldn't dare, you're going to be my harem queen after all."
            scene ch3sc18_088 with dissolve
            el "You're lucky I like you as much as I do! Otherwise I wouldn't allow this!"
            el "Harem queen, hmm... it does sound pretty cool."
            scene ch3sc18_090 with dissolve
            $ selena_path = True
            el "I'm not fond on the idea of having to share your attention or... affections."
            mc "I know... most women aren't too keen on the idea... yet-"
            $ eliza_path = True
            scene ch3sc18_091 with dissolve
            el "*Sighs* Yet it is the way our society functions, I know... I know."
            el "You're a great man, obviously I knew I was going to be in this situation."
            scene ch3sc18_090 with dissolve
            el "I had just hoped it wouldn't come this soon..."
            mc "Let's not get ahead of ourselves, Selena has just been flirting a little."
            $ eliza_relationship = True
            mc "Besides, no matter what, you'll always be my number one."
            el "Mhm, o-okay... yeah, you're right."
            $ eliza_trust += 1
            "Eliza is pleased to know she's your number one, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            el "Let’s head to bed?"
            el "I’m in desperate need of a cuddle!"
            scene ch3sc18_089 with dissolve
            mc "Say no more."
            scene black with Dissolve(1.5)
            scene ch3sc18_104 with Dissolve(1.5)
            $ renpy.pause()
            scene ch3sc18_105 with dissolve
            el "Mmhm... this is nice."
            el "Your body is so warm. Is it always like this?"
            scene ch3sc18_106 with dissolve
            mc "Pretty much. Even when I’ve been in cold regions up north, my body always keeps warm."
            scene ch3sc18_105 with dissolve
            el "It must be a Nephilim thing."
            scene ch3sc18_104 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_105 with dissolve
            el "Your scars... do they... hurt?"
            scene ch3sc18_106 with dissolve
            mc "No. They've been completely healed for several years now."
            mc "You can feel them if you like."
            scene ch3sc18_105 with dissolve
            el "Like this?"
            stop music fadeout 1.0
            el "Maybe they will heal if I do this?"
            play music lewd_1 fadein 1.0
            "She runs her fingers down your chest towards your ribs while she plants tender kisses along the way."
            scene ch3sc18_107 with dissolve
            $ renpy.pause()
            el "Nnhhnhh..."
            scene ch3sc18_108 with dissolve
            $ renpy.pause()
            mct "I don't think I've ever felt anything as soft as her sweet lips..."
            mct "Every time she moves, it feels like her lips almost stick to my skin, not wanting to lose contact."
            scene ch3sc18_109 with dissolve
            "She begins switching between placing wet kisses on your skin, and gently sucking along your scars."
            $ renpy.pause()
            mc "Fuck... Eliza. That feels incredible."
            "As you praise her efforts, she traces your scars with her tongue, licking carefully back and forth."
            scene ch3sc18_110 with dissolve
            $ renpy.pause(1.5)

            ####Animation####
            show el_lick1 with fade
            $ renpy.pause(2, hard=True)
            el "*Soft moan* Mmhmh... Mhhnn..."
            elt "I love licking him! Nhnn..."
            "She keeps running her tongue gently along your scars-"
            "-Then you feel her hand brushing back and forth against your cock."
            elt "Mhmhmhh... He's already hard! He must really like me licking him. Mnhh..."
            mc "Eliza... Fuck. You're driving me insane here."
            el "*Soft moan* Mmmh... Ghoood! Nhhhnnmm."
            scene ch3sc18_109 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_108 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_107 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc18_105 with dissolve
            el "That’s all for tonight!"
            scene ch3sc18_106 with dissolve
            mc "You tease..."
            scene ch3sc18_105 with dissolve
            el "Goodnight, my Lion."
            scene ch3sc18_106 with dissolve
            mc "Goodnight, my Kitten..."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            $ renpy.pause(0.5)
            jump ch3sc19

        "Was she? I don't have time for such things. ({color=#2bff8b}Eliza & Selena Friendship{/color} ({color=#f00}End Romance{/color})":
            scene ch3sc18_092 with dissolve
            mc "She can flirt all she wants, I'm not interested in a relationship at the moment."
            mc "I have no intention of commiting to anyone as things currently stand."
            $ selena_trust -= 1
            "Selena’s trust decreased by {size=+3}{b}{color=#f00}1{/color}{/b}{/size}."
            scene ch3sc18_093 with dissolve
            $ eliza_path = False
            el "I could tell."
            el "Let’s just go to sleep... I'm exhausted!"
            $ eliza_trust -= 1
            "Eliza's trust has decreased by {size=+3}{b}{color=#f00}1{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            scene ch3sc18_103 with Dissolve(1.5)
            $ eliza_relationship = False
            el "Goodnight..."
            $ selena_path = False
            mc "Goodnight."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            $ renpy.pause(0.5)
            jump ch3sc19

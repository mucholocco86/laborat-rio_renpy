label ch7sc3:

    window hide dissolve
    scene ss22 with Dissolve (1.5)
    $ renpy.pause()
    scene black with Dissolve (1.5)
    $ renpy.pause(0.5)
    scene ch7sc02_001 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.8)
    mct "The academy is bustling with activity, even though it’s barely dawn…"
    mct "I’m glad I didn’t choose this path, I would definitely hate having this many people around at all hours of the day."
    mct "I can see why Alice likes it though, she’s much more of a people person than myself."
    mct "I’m looking forward to seeing Luna though, we’ve wanted a day to ourselves since before Amelia was kidnapped."
    mct "Things just kept happening… now we finally get the entire day to ourselves-"
    scene ch7sc02_002 with dissolve
    lu "[mc]! Hiiii!"
    mc "There she is, my favorite little witch. *Chuckles*"
    scene ch7sc02_003 with dissolve
    lu "Brace yourself! Your favorite witch is incoming! *Giggles*"
    mc "What are you-"
    scene ch7sc02_004 with dissolve
    with vpunch
    lu "Mmhphh! Much better!"
    lu "Good morniiing!"
    mc "*Chuckles* Good morning… Luna, there’s a lot of people here…"
    lu "I entirely fail to see the point you’re trying to make, so you might as well stop complaining. *Giggles happily*"
    scene ch7sc02_005 with dissolve
    lu "I hope I didn’t make you wait too long? My hair was being annoying this morning since I made it wavy for the banquet yesterday."
    mc "Ah, that explains the ponytail. *Chuckles*"
    lu "Uh-huh! Ponytails work for everything, I can see why Eliza is such a big fan of them."
    scene ch7sc02_006 with dissolve
    lu "But… she’s not the one I’m spending the day with, so… question is…"
    lu "Do you like my ponytail? It’s okay if you don’t-"
    scene ch7sc02_007 with dissolve
    mc "I like it."
    mc "It suits you and while your hat is goofy and funny, it also suits you well, however… I’m glad you aren’t wearing it today."
    scene ch7sc02_008 with dissolve
    lu "Y-You are? How come?"
    scene ch7sc02_007 with dissolve
    mc "Because now I get to see your cute little face all day without it being hidden by your hat."
    scene ch7sc02_008 with dissolve
    lu "[mc]..."

    if luna_relationship == True:
        lu "I… I think you should kiss me."
        scene ch7sc02_009 with dissolve
        lu "*Squeals* Aiiyh-mmh! Mmh! Nnnghh…"
        lu "[mc]- Nnngh… there’s a lot of people around! *Giggles whilst kissing*"
        mc "Who’s feeling shy now? Mmmh…"
        scene ch7sc02_010 with dissolve
        lu "*Giggles* Is this the type of behavior I can expect from you now that we’re on a date?"
        mc "You bet it is."
        lu "Nnngh… then kiss me again and show all the boys here at the academy what a man I’m dating."
        scene ch7sc02_011 with dissolve
        lu "Mmmgh-mmh!"
        "Her warm soft lips intimately accept yours as you lean in, this time she is more eager in her kiss, more passionate."
        scene ch7sc02_012 with dissolve
        lu "I-... mmmh…  I can’t believe your tongue is in my mouth… in front of everyone… nnngh…"
        scene ch7sc02_011 with dissolve
        mc "You’re the one who keeps sucking my lips… nnngh… and you’re incredibly delicious."
        scene ch7sc02_012 with dissolve
        lu "So are you… mmh… I love how your lips feel against mine… and the taste of your tongue."
        scene ch7sc02_010 with dissolve
        lu "*Panting softly* Phew… I think that showed just about every boy here why they are of zero interest to me."
        mc "A woman like you needs a man."
        lu "Mhm-hm, luckily I’ve found myself a handsome man."
        scene ch7sc02_011 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_010 with dissolve
        lu "Okay that was the last one! For now… *Giggles*"
        mc "*Chuckles* I’m already looking forward to the next one, here I’ll help you up."
        scene ch7sc02_005 with dissolve
        lu "Now let’s go! We have a full day of adventures ahead of us!"
        lu "I have a place in mind for us later, but I’ll let you start off our adventure, what do you have in mind?"


    else:
        lu "You’re being very sweet, thank you."
        scene ch7sc02_005 with dissolve
        lu "Now let’s go! We have a full day of adventures ahead of us!"
        lu "I have a place in mind for us later, but I’ll let you start off our adventure, what do you have in mind?"


    mc "Hmm, I say we go explore the city before the streets become too crowded."
    lu "Ooh! I like exploring the city! There’s always a bunch to see and new things happen all the time!"
    mc "Then we better get to it. C’mon little witch."
    lu "Lead on! *Giggles*"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss68 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc02_013 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.7)
    lu "Wait, actually?! There’s no way!"
    mc "It’s true, eggs, bread, bacon, pancakes, everything you could want."
    scene ch7sc02_014 with dissolve
    lu "The queen, her royal highness, made you… breakfast?!"
    lu "Amelia’s mother, the queen? Married to King Bennen, the queen? The most influential woman in Luxeron, the queen?"
    scene ch7sc02_015 with dissolve
    lu "*Mimics you* Yes, your highness, I’d like my eggs poached and my bread toasted, and some butter with my pancakes please."
    lu "*Mimics you* And make it snappy! I’m hungry and you don’t want to keep me waiting, do you?"
    scene ch7sc02_016 with dissolve
    mc "Surprisingly accurate. *Chuckles*"
    lu "No way, actually?! There’s no way you spoke to her like that!"
    mc "No, I certainly didn’t. But she did make me breakfast."
    scene ch7sc02_017 with dissolve
    lu "*Belly rumbles* Uh! And to think I skipped breakfast today… meanwhile you had a royal feast!"
    mc "*Chuckles* Then let’s get some food in you, I won’t have you starving on my watch."
    "Luna nods in agreement, clearly she made a bad call skipping breakfast."
    mc "C’mon, I see a place up ahead where we can fill you up."
    scene ch7sc02_018 with dissolve
    mc "See anything you like?"
    lu "*Nods* Uh-huh!"
    uk "Hey there, is there anything here that entices a beauty such as you?"
    uk "You know, I could show you where the goods are made, if you’d like? *Scoffs*"
    mc "*Whispers*{size=-10}{b} You want those square pastries, don’t you?{/b}{/size}"
    lu "*Nods* Mhm-hm!"
    lu "*Whispers*{size=-10}{b} But I don’t want you to spend your money on this creep…{/b}{/size}"
    mc "I’ve got it covered."
    uk "So what do you say, miss? You want me to give you a private tour, don’t you? Heh…"
    scene ch7sc02_019 with dissolve
    with vpunch
    mc "You must be as stupid as you look to think you’d get away with being a creep to a sweet girl like her, with her man next to her."
    uk "*Gasps for air* Hnnrrhh! B-Bastard!"
    mc "Now, she’s going to enjoy some of your pastries, and they’ll be free of charge. Right?"
    uk "Ghhrhh… hhrhh! R-Right!"
    mc "Now run back to whatever hole you live in, I don’t want your ugly mug ruining her appetite."
    scene ch7sc02_020 with dissolve
    uk "*Coughs* B-Bastard! You’ll pay for this!"
    mc "He says as you’re such a beautiful woman, you can enjoy as many pastries as you want, free of charge."
    lu "*Giggles sarcastically* Oh? That’s so sweet of him!"
    scene ch7sc02_021 with dissolve
    mc "I know right? *Chuckles* What a kind soul."
    lu "*Giggles softly* Thank you… for doing that."
    $ luna_trust += 2
    "Luna appreciates you standing up for her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
    scene ch7sc02_022 with dissolve
    lu "I don’t know why so many men have to act like that… such creeps."
    lu "They are acting worse than literal pigs… do they not realize how pathetic they come across?"
    scene ch7sc02_023 with dissolve
    mc "I’m sure they know how gross they’re being, it’s just that they aren’t used to being put in their place."
    mc "They’re a product of the way society is structured in Luxeron."
    mc "With it being so heavily male favoured, they are used to getting away with that behavior."
    scene ch7sc02_022 with dissolve
    lu "That doesn’t excuse it… they’re pathetic, through and through."
    lu "You’ve lived in Luxeron your entire life, and I’ve never once seen you act like a creep towards anyone."
    scene ch7sc02_023 with dissolve
    mc "Well I had the benefit of actually having caring parents and after that… a strict mentor."
    mc "I heard a saying once at a tavern, which I tend to agree with… it goes like this-"
    mc "Every creep acts high and mighty until they get punched in the face."
    scene ch7sc02_022 with dissolve
    lu "*Giggles* Uh! I like that saying! And it seemed to be true, look at that guy you sent running."
    lu "You only held him up against the wall and he ran like a little sissy! *Snickers*"
    scene ch7sc02_023 with dissolve
    mc "I thought about punching him, but getting blood all over my new clothes? Not the best way to start the date."
    scene ch7sc02_022 with dissolve
    lu "I’m glad you didn’t, I wouldn’t want this sexy shirt of yours ruined this early today!"
    scene ch7sc02_023 with dissolve
    mc "Go on, have at it. I know you’re starving."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Luna proceeds to devour the delicious baked goods."
    scene ch7sc02_024 with Dissolve(1.5)
    $ renpy.pause(0.5)
    lu "Mmmh! Nngh…"
    mc "Damn, you ate all of them… they any good?"
    lu "Mhm-hm!!"
    scene ch7sc02_025 with dissolve
    lu "Here, try it it’s the last one… I already nibbled it, I hope you don’t mind?"
    "She shares the last pastry with you by gently putting it between your lips."
    lu "Do you like it?"
    mc "Mhm-hmm… isss… good… mmh."
    scene ch7sc02_026 with dissolve
    mc "Thanks for letting me try one, ready to get out of here?"

    if luna_relationship == True:
        lu "Not yet… I still have pastry powder on my fingers…"
        scene ch7sc02_027 with dissolve
        lu "Here, lick them clean for me. *Giggles*"
        "The sugary powder covering her is delicious and you intimately lick them while she teases your tongue."
        lu "Mmmh… you’re such a good man, taking care of me like this."
        lu "Don’t stop until you’ve gotten all of it. *Giggles softly*"
        mc "Mmmgh-mmh…"
        scene ch7sc02_026 with dissolve
        lu "Thank you… *Sensual* I’ll be sure to return the favor later."
        mc "Oh? You’ll be sucking something of mine?"
        scene ch7sc02_027 with dissolve
        lu "Here! Suck them a little more and I could be convinced! *Snickers*"
        mc "Mmmh! Mmmh…"
        scene ch7sc02_026 with dissolve
        mc "Now that we’ve both had our taste buds satisfied momentarily, how about we get out of here?"
        lu "*Giggles* Let’s go!"

    else:
        lu "Let’s go!"

    scene ch7sc02_013 with dissolve
    lu "Where are we off to next?"
    scene ch7sc02_014 with dissolve
    lu "While you did handle that creep like a heroic knight, I would prefer if we don’t have to deal with any more of those today."
    scene ch7sc02_015 with dissolve
    lu "Although! Watching you deliver some good old judgement onto some mongrels like him would be rather entertaining!"
    scene ch7sc02_016 with dissolve
    mc "*Chuckles* With a gorgeous girl like you around, I’m sure we’ll attract them like sharks to blood."
    lu "W-What’s that supposed to mean? That I’m some sort of creep-magnet?"
    mc "*Chuckles* Well, yeah?"
    scene ch7sc02_014 with dissolve
    lu "Uh-huh… c’mon, I think I’ve heard enough of your silly theories!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch7sc02_028 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.7)
    "Having been told by Eliza how Luna enjoys the onsen on the outskirts of Luxenford, inspired by the baths in the Sen’ju region of Luxeron."
    "You decide to take Luna to a Sen’ju inspired garden located in the southern district of Luxenford."
    lu "This place looks so nice! I can’t believe I’ve never been here before?"
    mc "Luxenford is one of the largest cities in all of Midomir, I doubt even the king has seen all of it himself."
    scene ch7sc02_029 with dissolve
    lu "I love it here! This is so cute! {b}*Squeals happily* iiiiihhh!{/b}"
    mct "*Chuckles* She’s cute when she gets like this."
    lu "[mc] look! There’s even a little pond in here! *Giggles* And so many different plants!"
    scene ch7sc02_030 with dissolve
    lu "Thank you so much for bringing me here! I love it!"
    lu "How did you know I was into Sen’ju culture?"
    mc "Come, let’s sit over there in the shade."
    scene ch7sc02_031 with dissolve
    lu "Okay, we’re sitting now! Spill the beans!"
    mc "*Chuckles* A certain ponytail wielding friend of ours might have mentioned you enjoying a certain type of… bath."
    lu "Eliza! *Snickers* That little cutiebutt!"
    scene ch7sc02_032 with dissolve
    lu "She’s right though, I’m really fascinated with culture pertaining to the Sen’ju region, their architecture, plants, wildlife, their way of life."
    lu "Sometimes there’s food imported from the Sen’ju region in the market, but you have to be lucky to get any, people eagerly buy all of it."
    scene ch7sc02_033 with dissolve
    lu "Trust me you don’t want to mess with elderly ladies in the market on Sen’ju days, they can be downright aggressive!"
    lu "I even got knocked on my ass one time because the crowd was so big and everyone was elbowing each other to get some fruits."
    scene ch7sc02_032 with dissolve
    lu "It’s weird how one of the most tranquil and serene regions of our kingdom inspire such ferocity when it arrives here…"
    scene ch7sc02_034 with dissolve
    mc "‘The greed of men’ is a phrase my mentor often used, not men as in males specifically, but more our race as humans."
    mc "Basically a great deal of us have this other side to us which bares its ugly teeth when there’s something we want within reach."
    scene ch7sc02_032 with dissolve
    lu "Yeah… I think it’s important we learn to control our impulses and try to do better."
    lu "I’m sure the other races of Midomir have their share of turmoil as well, but with humans it always seem to be so… extra?"
    scene ch7sc02_033 with dissolve
    lu "Like why are we always bickering amongst ourselves, treating each other like animals as soon as something is to be gained?"
    scene ch7sc02_034 with dissolve
    mc "I can see why you’re so intrigued by the Sen’ju culture, it’s like the total opposite of what we experience here in the cities."
    scene ch7sc02_033 with dissolve
    lu "I’d love to visit the Sen’ju region sometime, but I’ve never been able to, it’s quite far away and isolated."
    lu "When I was little I used to fantasize about sneaking into one of the trade wagons so I could see it."
    scene ch7sc02_034 with dissolve
    mc "I’ll take you sometime."
    scene ch7sc02_035 with dissolve
    lu "Wait- actually?!"
    lu "You-... you’ll take me there someday?"
    lu "D-Don’t mess with me… this means a lot to me!"
    scene ch7sc02_036 with dissolve
    mc "I promise, Luna. I’ll make sure you get to experience everything Sen’ju has to offer."
    "Luna's eyes widen with wonder as you continue."
    mc "From the winding rivers with crystal clear water, to the mountain peaks with air so fresh you wouldn’t believe it."
    mc "You’ll get to meet the people, living a simple, yet entirely fulfilling life. And the exotic animals living in the bamboo forests."
    scene ch7sc02_037 with dissolve
    lu "*Giggles softly* [mc]... there’s nobody else I would rather experience all of that with."
    lu "It would literally be a dream come true."
    scene ch7sc02_031 with dissolve
    mc "You’ll love it there."
    lu "Oh! I just remembered, you totally lived there! For like five or so years, right?"
    scene ch7sc02_035 with dissolve
    lu "Sorry…"
    lu "I didn’t mean to yap on about it like this, you must miss it?"
    scene ch7sc02_036 with dissolve
    mc "I do miss it. but it’s nothing you have to apologize for…"
    mc "If anything, it’s nice to talk about it and think about it with someone who’s genuinely curious."
    scene ch7sc02_037 with dissolve
    lu "*Giggles* Oh I’m curious alright!"
    lu "You’ve lived such an interesting life."
    scene ch7sc02_033 with dissolve
    lu "And you don’t seem to be slowing down in that department."
    lu "Running off on grand island adventures out of nowhere, not even giving me the chance to join you!"
    scene ch7sc02_034 with dissolve
    mc "*Chuckles* Bring Luna to Sen’ju and fulfill her lifelong dream, bring Luna to A’nai and give her an adventure. Noted."
    lu "*Snickers* …"
    scene ch7sc02_033 with dissolve
    lu "Is that too much to ask? For a little adventure with a handsome man?"
    scene ch7sc02_032 with dissolve
    lu "All the gods know I’m craving a little excitement in my life."
    lu "*Quietly* {size=-10}{b}And you definitely make me feel excited…{/b}{/size}"
    mc "Hmmh?"
    scene ch7sc02_033 with dissolve
    lu "N-Nothing! *Giggles*"
    scene ch7sc02_037 with dissolve
    lu "Hey… remember how we talked about Rose the other day?"
    lu "I believe I have thought of something."
    scene ch7sc02_036 with dissolve
    mc "Great, what do you need?"
    scene ch7sc02_033 with dissolve
    lu "The more I think about it, the less it makes sense for her to be helping Taron."
    lu "She clearly despises the guy, rightfully so…"
    scene ch7sc02_038 with dissolve
    lu "And her own ambition to lead the guild isn’t enough to betray my mother."
    lu "The two of them have been like sisters my entire life, and Rose has always been like an aunt to me…"
    scene ch7sc02_039 with dissolve
    lu "[mc], there’s foul play involved here… I know there is."
    lu "Hexes are dark magic… why would Rose betray us, work with a creep like Taron AND use dark magic?"
    scene ch7sc02_038 with dissolve
    lu "Just to lead the mage’s guild? No fucking way! Either Taron or someone else has something on her."
    scene ch7sc02_039 with dissolve
    lu "Something so bad that she is willing to go to these lengths!"
    lu "We’re going to find out what it is, and when we do… use it to force her to free my mother."
    scene ch7sc02_040 with dissolve
    mc "Sure, a little blackmail is nothing compared to what she has put you through."
    mc "How are we going to gain this information though?"
    scene ch7sc02_039 with dissolve
    lu "One of two ways…"
    scene ch7sc02_038 with dissolve
    lu "My first idea is we distract her, specifically you."
    lu "While I sneak into her office and search for anything that could be of use."
    scene ch7sc02_040 with dissolve
    mc "And the 2nd option?"
    scene ch7sc02_039 with dissolve
    lu "We force her hand."
    scene ch7sc02_038 with dissolve
    lu "That would involve you putting the fear of all the gods into her, just like you did with that creep earlier."
    scene ch7sc02_039 with dissolve
    lu "But this is my backup plan, I don’t want to resort to violence unless we have to…"
    scene ch7sc02_040 with dissolve
    mc "*Sighs* So I have to… talk to her?"
    scene ch7sc02_039 with dissolve
    lu "Yes! Although… she’s a bit of a maneater… I’ve seen countless men attempt to woo her, yet none have succeeded."
    scene ch7sc02_038 with dissolve
    lu "But even so, they do her bidding like lovesick little puppies."
    scene ch7sc02_039 with dissolve
    lu "I can’t believe I’m saying this… but, you might have to work your charm on her… eck!"
    scene ch7sc02_040 with dissolve
    mc "You want me to… seduce her?"
    scene ch7sc02_039 with dissolve
    lu "N-Not want! I think ‘need’ is the better word."
    scene ch7sc02_038 with dissolve
    lu "Her office is sealed by a strong spell, if I attempt to break it without her thoroughly distracted, she will feel it."
    lu "So, I need you to… eck, put the moves on her…"
    scene ch7sc02_040 with dissolve
    mc "*Sighs* I can’t believe I’m agreeing to this… fine, I guess I can flirt with her for a bit."
    mc "But you better be quick about searching her damn office."
    scene ch7sc02_032 with dissolve
    lu "Trust me! I’m going to be swift as an eagle diving through the sky!"
    lu "I have no intentions of having you flirt with her for a second longer than needed."
    scene ch7sc02_033 with dissolve
    lu "Thank you… I know this is a lot to ask-"
    scene ch7sc02_036 with dissolve
    mc "I told you I would do anything to help you, you need only ask."
    mc "While I’m not a fan of having to socialize for your plan to work… I will do anything it takes, for you."
    scene ch7sc02_037 with dissolve
    lu "[mc]..."
    lu "Thank you for being here for me when I need you… it means so much to me."
    scene ch7sc02_036 with dissolve
    mc "Just let me know when and where, and we’ll get your mother free of that hex."
    scene ch7sc02_032 with dissolve
    lu "Yes! I’ll let you know as soon as I figure out when we have the best chance of success."
    scene ch7sc02_039 with dissolve
    lu "Speaking of my mother..."
    lu "Wasn't there something you've been meaning to tell me?"
    lu "I believe you said after we had freed my mother you'd tell me about yourself?"
    scene ch7sc02_038 with dissolve
    lu "I'm not trying to push you into telling me by the way..."
    lu "If you don't think it's the right time, I'll understand."
    scene ch7sc02_039 with dissolve
    lu "But I do believe we're close enough at this point for me to know whatever it is you're keeping from me."
    scene ch7sc02_040 with dissolve
    mct "She's right, I did promise I'd tell her what I am once we got her mom to safety."
    mct "Not to mention we're definitely at the point where I fully trust her... I guess it's time."
    scene ch7sc02_039 with dissolve
    lu "I know this is only our first dat-"
    scene ch7sc02_040 with dissolve
    mc "I'm a Nephilim."
    scene ch7sc02_035 with dissolve
    lu "A what? Nephalem?"
    scene ch7sc02_036b with dissolve
    mc "Nephilim."
    mc "I'm a Demi-god."
    with vpunch
    lu "{b}!!!!!!!!!!{/b}"
    scene ch7sc02_035 with dissolve
    lu "D-Demi-god! Of course!"
    lu "That totally explains the potency of your magic!"
    scene ch7sc02_032 with dissolve
    lu "*Snickering* Pheeew! Here I thought it was something horrible!"
    lu "Like an incurable disease..."
    scene ch7sc02_034 with dissolve
    mc "*Scoffs* No incurable diseases that I know of. But you're taking this well..."
    scene ch7sc02_033 with dissolve
    lu "Why wouldn't I? You're forgetting I'm a member of the Mages Guild."
    lu "You're not the first Demi-god I have encountered."
    lu "We have all sorts of species at the guild! Demi-gods included."
    scene ch7sc02_037 with dissolve
    lu "*Giggling* Demi-gods included!"
    scene ch7sc02_039 with dissolve
    lu "[mc]... thank you for telling me though."
    lu "I've never heard of a Nephilim before... I'm glad you trust me enough to share this with me."
    scene ch7sc02_040 with dissolve
    mc "Your reaction to me being non-human has me feeling foolish for not telling you sooner."
    mc "I had expected... well, I don't know what I expected... maybe that you'd see me differently?"
    lu "..."
    scene ch7sc02_039 with dissolve
    lu "I resent how you worded that."
    lu "What you are... Demi-god... Elf... Efreeti... it doesn't matter."
    lu "What matters is {b}WHO{/b} you are, your actions."
    scene ch7sc02_033 with dissolve
    lu "Hold still, dummy."
    scene ch7sc02_036c with dissolve
    mc "*Chuckles* What are you-"
    lu "*Giggling softly* ..."
    scene ch7sc02_036d with dissolve
    mc "Really?"
    lu "I told you to hold still."
    scene ch7sc02_036e with dissolve
    "You feel Luna crawl onto your lap, wrapping her arms around you and squeezing you tightly."
    lu "You really are a big dummy..."
    lu "You being a Nephilim doesn't change anything for me... least of all how I feel about you."
    lu "Thank you for telling me."
    mc "Lun-"

    if luna_path == True:
        scene ch7sc02_036f with dissolve
        lu "Nnghh... be quiet and kiss me."
        "Luna melts into your kiss, pressing herself entirely against you."
        lu "MMh... I lov-... mmh... I like you so much."
        lu "So stop worrying about how I'll perceive you... I'm in your corner- mmmhh..."
        mc "And I'm in yours as well... mmh... I'm glad I told you."
        scene ch7sc02_036e with dissolve
        lu "*Heavy breaths* Nnhh... this date is getting steamy..."
        lu "I'd better dismount you before we do unspeakable things in a public garden."

    else:
        lu "One moment, let me dismount you... sitting like this is making me feel all funny."


    scene ch7sc02_032 with Dissolve(2)
    $ renpy.pause(0.5)
    lu "*Exhales deeply* Mmh!"
    lu "I'm glad we got that squared away!"
    scene ch7sc02_033 with dissolve
    lu "Is this something I can tell my mom? Or would you prefer I didn't?"
    lu "This is your secret to tell so I fully understan-"
    scene ch7sc02_036 with dissolve
    mc "You can tell her."
    mc "She's your mom, but I will ask you don't go around telling others."
    scene ch7sc02_035 with dissolve
    lu "'Of course I wouldn't!"
    lu "It's just... you can trust her. She's all I have."
    scene ch7sc02_036 with dissolve
    mc "I know... I'd give anything to be able to talk to my parents again..."
    mc "So yeah, tell her whenever you feel it's time."
    scene ch7sc02_033 with dissolve
    lu "Splendid! Who knows... maybe she even knows stuff about Nephilims."
    lu "She has all sorts of knowledge in that pretty noggin of hers! *Snickering*"
    scene ch7sc02_032 with dissolve
    lu "Ready to get out of here?"
    lu "It’s my turn to take you somewhere! *Giggles*"
    scene ch7sc02_036 with dissolve
    mc "Yeah, I'm ready to see what you have in store for me."
    scene ch7sc02_037 with dissolve
    lu "Oh I've got things in store for you buddy!"
    lu "I hope you’re ready to get a little sweaty with me! *Snickers*"
    lu "Cause I know just the place where I can… turn up the heat."
    scene ch7sc02_036 with dissolve
    mc "*Chuckles* Go on little witch, let’s see how hot you can get."
    scene ch7sc02_030 with dissolve
    lu "C’mon on then handsome! Today we won’t be inside like that time at the guild, so we can properly let loose!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "The two of you head out of the Sen’ju garden and through the southern city gate, heading into the nearby forest."


    if samarah_alive == True:
        scene ss120 with Dissolve(1.5)
        $ renpy.pause()
        scene sl1 with Dissolve(1.5)
        play music explore_1 fadein 1.0
        $ renpy.pause(0.7)
        slt "I never imagined I’d be living in a village… tucked away from most of civilization."
        slt "It’s growing on me though, not as exciting as the bustling life of the capital…"
        scene sl2 with dissolve
        slt "But it certainly beats living under the heels of thugs."
        slt "Living here might be a little on the boring side… but it keeps Samarah safe."
        scene sl3 with dissolve
        slt "Her safety and happiness is all that matters."
        slt "I’ve never seen her happier than now, she has taken a liking to the calm and quaint village life."
        scene sl4 with dissolve
        slt "I haven’t received word from the stablekeeper back in Luxenford."
        slt "But I imagine he’ll want payment at some point for letting us seek refuge in his cabin."
        scene sl5 with dissolve
        slt "Samarah is making a bit of coin helping villagers with their laundry."
        slt "While I’ve been foraging the woods and selling what I find here at the market."
        scene sl6 with dissolve
        slt "It’s not much, but we make do… it’s enough to keep food on the table and put a little aside for the stablekeeper."
        slt "The local Innkeeper even offered me-"
        scene sl7 with dissolve
        uk "Mommy! Can we get rice today? Please mommy!"
        uk "Sorry sweetie, we’re here for potatoes today, we’ll get rice next time. Okay?"
        scene sl8 with dissolve
        slt "*Giggling softly* That girl reminds me of Samarah when she was younger."
        slt "She’d always beg mother to bring her to the market so she could get honeyed-treats."
        slt "If only mother could see the woman Samarah has grown into… she’d be proud."
        scene sl7 with dissolve
        slt "That’s enough sentimentality for one day…"
        scene sl6 with dissolve
        slt "Pumpkin, sweetroot and bread, better get to it before the stalls close for the day."
        scene sl9 with dissolve
        sl "One sweetroot, one pumpkin and two loaves of bread, please."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ss121 with Dissolve(1.5)
        $ renpy.pause()
        scene ss122 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene sl10 with Dissolve(1.5)
        $ renpy.pause()
        scene sl11 with dissolve
        slt "Looks like I made it back before dark."
        slt "Samarah doesn’t like it when I’m out on my own after nightfall… *Scoffs*"
        slt "Sometimes I almost forget that I’m the older sister… she’s quite overprotective."
        scene sl12 with dissolve
        slt "*Sighs* She’s still sorting through that stuff? I told her we’d do it together… she’s going to overwork herself."
        sl "Who’s huuunnngry? *Snickers* I’ve got my hands on the freshest of sweetroots the market had to offer."
        scene sl13 with dissolve
        sm "Selena! *Excitedly* You’re back!"
        sl "Heeeey giiiirl!"
        scene sl14 with dissolve
        sm "I was worried! You know I don’t like you being out when it's dark!"
        sl "*Scoffs* The sun has only just set as I made it back, I’ve told you… leave the worrying to me, okay?"
        scene sl15 with dissolve
        sm "Hhmmpfh!"
        sm "Did anyone harass you today? I’ll have words with them if they did!"
        sl "*Scoffs* Oh yeah? Is my little sister going to give them a scolding if they did?"
        sm "You know it! Hmpfh!"
        scene sl16 with dissolve
        sm "A scolding they’ll remember for the rest of their lives!"
        sl "*Giggling* What would I do without you…"
        sm "You’ll never have to find out! We’ll stick together forever! Just like you promised when we left home!"
        sl "You bet. Now, go wash your hands… dinner isn’t going to make itself."
        scene sl17 with dissolve
        sm "I’ll set the table while I’m at it! You get the groceries ready!"
        sl "*Snickers* Barking orders are we?"
        sl "Careful little lady… otherwise you’ll be doing the dishes!"
        scene sl18 with dissolve
        slt "*Sighs* Despite having gotten what I wanted…"
        slt "Samarah’s freedom… seeing her happy… it’s all I wanted… all I’ve fought for."
        slt "But… it came at a cost… [mc] and Eliza’s trust… if only I could make it right with them…"
        scene sl19 with dissolve
        slt "If they could meet Samarah… they’d realise how wonderful she is… how… innocent."
        slt "Maybe… maybe one day."
        slt "I’d love for [mc] to meet Samarah, they’d get along so well."
        scene sl18 with dissolve
        slt "*Exhales* Probably wishful thinking… I know the world better than to think I’d be granted a blessing like that."
        sm "Selenaaa? C’mon! Move your butt! I’m famished!"
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    else:
        pass


    scene ss69 with Dissolve(1.5)
    $ renpy.pause()
    scene ch7sc02_041 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.7)
    lu "Pretty cool huh?"
    mc "Yeah… what is this place?"
    lu "When I first discovered it, I inquired at the Explorer’s guild about this location, according to them it used to be the estate of a lord."
    scene ch7sc02_042 with dissolve
    lu "The statue here was apparently one the lord of the estate had carved in his own image."
    mc "*Chuckles* A pretentious lord? I would’ve never guessed."
    lu "*Giggles* Let’s not speak ill of those who have long passed, we can’t know if it’s actually depicting him or why it was made."
    scene ch7sc02_043 with dissolve
    lu "But it’s pretty awesome nonetheless!"
    mc "Yeah, I guess we’ll never know for sure. Which is one thing I enjoy about ruins like these… you’re free to imagine what has transpired."
    lu "Mhm-hm! I like doing that! My imagination can take me on some pretty interesting journeys! *Giggles*"
    scene ch7sc02_044 with dissolve
    lu "Our destination is just behind the ruins, there’s a small clearing that will suit our needs perfectly for today!"
    lu "Come, come!"
    mc "Alright, alright… lead on."
    scene ch7sc02_045 with dissolve
    lu "Okay, are you ready?"
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    mc "Ready for wha-"
    scene ch7sc02_046 with dissolve
    play music battle_3 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    mc "Luna! A little heads-up next time?"
    lu "Eliza says you should never expect your opponent to act with chivalry, so strike first and strike hard."
    scene ch7sc02_047 with dissolve
    mct "*Chuckles* Exactly what I taught Eliza from our first sessions, it’s good to see it stuck and now she’s teaching the others."
    mct "I guess it’s time to find out how well Luna stacks up."
    scene ch7sc02_048 with dissolve
    lu "Smiling huh?"
    lu "Very well, allow me to turn up the heat!"
    scene ch7sc02_049 with dissolve
    "The sky darken as Luna raises her hand into the air, channeling a vast amount of energy into the palm of her hand."
    lu "Infernum, ignitus, infernitas!"
    scene ch7sc02_050 with dissolve
    mct "Five hells… is she planning on burning the entire forest down? That’s no small amount of energy she is channeling."
    mct "To be able to change the sky itself in the surrounding area… impressive."
    scene ch7sc02_051 with dissolve
    mct "She intends to show me exactly what she is capable of, which means she isn’t going to hold back."
    mct "She is not as strong as Diana, however they are completely different kinds of mages."
    mct "Luna being a spellcaster, she is more of a typical sorceress, focusing on intense and powerful ranged magic."
    mct "While Diana is a battlemage, focusing on physical martial prowess and enhancing that with magical infusions."
    mct "This means Luna is frail up close, but dangerous at a distance, her spells will do more damage than someone like Diana’s."
    mct "For now, I’ll play this defensively and see what she’s got up her sleeve-"
    scene ch7sc02_052 with dissolve
    mct "Huh?!"
    mct "Five hells, Luna!"
    scene ch7sc02_053 with dissolve
    mct "Meteors?!"
    mct "Just how powerful has she gotten over the last couple of weeks?"
    scene ch7sc02_054 with dissolve
    with vpunch
    mct "I’m not going to attempt to tank those, I’ll have to dodge!"
    scene ch7sc02_055 with dissolve
    with vpunch
    mct "Close! Damn they’re hot!"
    scene ch7sc02_056 with dissolve
    with vpunch
    mct "I need to intercept her! Otherwise she will continue to rain down meteors!"
    scene ch7sc02_057 with dissolve
    mct "Now’s my chance, she’s focused on guiding the meteors!"
    scene ch7sc02_058 with dissolve
    mct "Got her!"
    lu "Advirum! Sealium, Confinum!"
    scene ch7sc02_059 with dissolve
    with vpunch
    mc "*Groans* Argh!"
    "After a short numbing sensation of the seal activating, you feel something you didn’t expect..."
    scene ch7sc02_060 with dissolve
    "Luna embraces you."
    lu "Barrierium, ad, infinitus!"
    scene ch7sc02_061 with dissolve
    mc "Luna, what are you doing?"
    lu "[mc]... trust me, okay?"
    scene ch7sc02_062 with dissolve
    lu "Barrierium, ad, infinitus!"
    mct "She’s creating a barrier around us?"
    scene ch7sc02_063 with dissolve
    with vpunch
    mc "Luna! You’re going to exhaust yourself!"
    lu "{size=+3}{b}Barrierium, ad, infinitus!{/b}{/size}"
    with vpunch
    scene ch7sc02_064 with dissolve
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "Luna powers through and manages to maintain the barrier until the meteor shower eventually subsides."
    scene ch7sc02_065 with dissolve
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    lu "*Weakened voice* B-Barrierium-... ad… barrier-..."
    lu "B-Barrier-... hnngh!"
    scene ch7sc02_066 with dissolve
    mc "Stop it… you’ve done enough."
    scene ch7sc02_067 with dissolve
    mc "Just, rest."
    lu "[mc]... I’m-.. I’m sorry…"
    scene ch7sc02_068 with dissolve
    "With Luna’s meteor shower being over, the sky returns to normal."
    lu "I-... I couldn’t handle the thought of you getting hurt."
    mc "Hey… I’m fine, you protected us both."
    "Luna releases her firm grasp on you to see if you’re alright."
    scene ch7sc02_069 with dissolve
    lu "I-... I just wanted to show you what I was capable of, how much I had improved…"
    lu "A-And in doing so, I almost burned you to a crisp!"
    scene ch7sc02_070 with dissolve
    mc "You can rest assured, impressive as your meteors were, it’ll take a lot more than that to take me down."
    mc "You did exactly as I wanted you to, you didn’t hold back."
    scene ch7sc02_071 with dissolve
    mc "You showed me just how strong you’ve gotten, both offensively and defensively."
    mc "Not only were you able to rapidfire a fireball that would have caught most fighters completely off guard."
    scene ch7sc02_070 with dissolve
    mc "You then followed up by a spell with unmatched devastation, you literally altered the sky when you summoned the meteors."
    scene ch7sc02_071 with dissolve
    mc "Then as I went in for the ‘kill’ so to speak, you had already prepared a seal that was ready to catch me."
    scene ch7sc02_070 with dissolve
    mc "Had I been a real opponent I would’ve been trapped while you rained meteors down on me."
    scene ch7sc02_071 with dissolve
    mc "And to top it all off…"
    scene ch7sc02_070 with dissolve
    mc "You stepped into your own seal, creating a barrier unlike any I’ve ever seen, able to protect us from the meteors."
    scene ch7sc02_072 with dissolve
    mc "You’ve really grown Luna, I’m honestly impressed and proud of you."
    lu "..."
    scene ch7sc02_073 with dissolve
    lu "R-Really?"
    scene ch7sc02_072 with dissolve
    mc "Really. You were incredible."
    mct "Obviously I could’ve easily blitzed her in the beginning, but this isn’t about who is stronger."
    mct "It was about her showing me what she can do, and how far she’s come."
    mct "Seeing how powerful she is now… puts me at ease, she can handle her own. And I’ve no doubt she will continue to grow."
    scene ch7sc02_073 with dissolve
    lu "*Giggles* Wanna go again? I’ve got more spells I’d love to show you!"
    scene ch7sc02_072 with dissolve
    mc "*Chuckles* Oh yeah? If you’re game, so am I."
    scene ch7sc02_073 with dissolve
    lu "This time, can you use magic against me as well? I’d like to showcase a new spell I learned a few days ago."
    scene ch7sc02_072 with dissolve
    mc "You got it, round two will be magic vs magic."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss49 with Dissolve(1.5)
    $ renpy.pause()
    scene ss50 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc09_443 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    la "Excellent work with House Metilius."
    la "My men told me upon arrival they found heads mounted on spikes at the entrance, and women naked and raped on the pavements."
    scene ch6sc09_445 with dissolve
    ta "I told my men to have a little fun with it."
    ta "Brutalities tend to send a more long lasting message."
    scene ch6sc09_446 with dissolve
    ta "The children were drowned in the moats surrounding the estate as well."
    ta "You don’t want any vengeful offspring coming for you down the road."
    scene ch6sc09_447 with dissolve
    la "If anyone tries, they will meet a fate worse than death."
    la "With House Metilius erased and their men and villagers now under my Lordship, nobody can stop me."
    la "Not even that pacifist fool that likes to call himself king, tsk!"
    scene ch6sc09_446 with dissolve
    ta "We’ll see. He still commands a larger force than you."
    ta "How do you wish to proceed?"
    scene ch6sc09_447 with dissolve
    la "We’ll continue to absorb the smaller houses in the area, adding to our army strength."
    la "This will give Bennen a false sense of security that we aren’t targeting him, and then… we’ll crush him."
    scene ch6sc09_446 with dissolve
    ta "A sound strategy, the smaller houses in the area aren’t impactful enough for Bennen to march south and defend."
    scene ch6sc09_445 with dissolve
    ta "I assume your '{b}Order of Nezgols{/b}' are ready? King Bennen has powerful fighters in his ranks."
    ta "Admiral Diana, General Geskir and High-Commander Gaan."
    la "I’m well aware of his powerhouses, which is why I started gathering my own, handpicking each for their ruthlessness and abilities."
    la "My Nezgols will not disappoint."
    scene ch6sc09_444 with dissolve
    la "What about your contacts in Luxenford? Are they still loyal to our cause?"
    ta "Some… when I was outed as a traitor, some of them tucked their tails and cut ties to me, which was to be expected."
    la "Pathetic… you really should instill proper obedience into your subjects, just as I do."
    scene ch6sc09_445 with dissolve
    ta "I can’t be bothered, they are of no importance to what is to come."
    la "And {b}she{/b}? Does {b}she{/b} still remain loyal to our cause?"
    scene ch6sc09_446 with dissolve
    ta "She does… I have something that ensures she won’t betray us."
    ta "Something most precious."
    scene ch6sc09_447 with dissolve
    la "For your sake, I hope it’s enough… she is a key player if we are to take down Bennen."
    la "And women… they are known to be fickle with a weak resolve, Tsk!"
    scene ch6sc09_446 with dissolve
    ta "Let me worry about her, she has already proven herself useful on several occasions."
    scene ch6sc09_444 with dissolve
    ta "You just continue building up your army. It won’t be long now…"
    la "Indeed… a new dawn is upon Luxeron, one that will usher in a proper ruler, me."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss15 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_083 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    da "Still no word from the missing adventurers?"
    sy "Nuh-uh! Not a thing… do you think they abandoned the quest and went somewhere else?"
    da "*Sighs* It’s possible, although their rank wasn’t exceptional, they seemed to have some experience under their belt."
    da "It’s unlikely for experienced adventurers to abandon a quest, as they would lose ranking points by doing so."
    scene ch6sc10_084 with dissolve
    el "Hi! What are you two discussing?"
    sy "Eliza! Hii!"
    da "Hey, we’re talking about those missing adventurers, wondering how to deal with the situation."
    scene ch6sc10_085 with dissolve
    sy "Uh-uh! Why don’t we put Eliza on it?"
    sy "She’s more than capable and she’s been working too much behind the desk!"
    scene ch6sc10_086 with dissolve
    el "Really? Sounds to me like you just don’t want to do it yourself…"
    el "The quest was to investigate and clear out a cave, deep in the forest… that’s literally your area of expertise, miss forest fae."
    scene ch6sc10_085 with dissolve
    sy "Valid points! Except! I’m not an adventurer! I’m just helping Dalen manage the guild because he’s my friend."
    sy "Besides… I didn’t say you have to take on the quest by yourself!"
    sy "*Snickers* I’m sure there’s a certain someone you’d love to tackle it with!"
    scene ch6sc10_086 with dissolve
    el "I hate you sometimes… *Sighs*"
    scene ch6sc10_087 with dissolve
    el "It would be nice to get to take on a quest with [mc], it’s been quite a while since we last did one together."
    scene ch6sc10_086 with dissolve
    el "Okay, I’ll accept the quest! [mc] won’t be available until tomorrow though."
    scene ch6sc10_088 with dissolve
    da "Thank you, if something did happen to those adventurers… I’m glad to know you and [mc] will be on it."
    da "The cave they were supposed to investigate is located near the village of Loboten."
    da "Now, since your schedule is clear for today… join me in the courtyard."
    scene ch6sc10_089 with dissolve
    el "Hmh? Why?"
    da "You’re joining today’s training session, Borri is already waiting for us out there."
    el "Uhh! I get to kick both your asses today?! Awesome! *Snickers*"
    scene ch6sc10_085 with dissolve
    sy "Goodluck! You’re gonna need it, yuup!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss69 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc02_074 with Dissolve(1.5)
    play music battle_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    with vpunch
    lu "Hnngh! Is this-... is this all you’ve got?!"
    lu "Stop holding back- hnngh! Otherwise we won’t know the limit of my barrier!"
    scene ch7sc02_075 with dissolve
    with vpunch
    lu "Nice try! Hnngh! But not enough!"
    scene ch7sc02_076 with dissolve
    with vpunch
    lu "N-Now we’re talking- Nngh! Hnngh!!"
    mc "Next one is going to shatter your barrier."
    lu "We’ll-... hnngh! We’ll see! Give it all you’ve got!"
    scene ch7sc02_077 with dissolve
    with vpunch
    lu "I-It broke!! Aaiiyh!"
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch7sc02_078 with dissolve
    with vpunch
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    lu "*Squeals* Aiiyh! [mc]! Hahaha- It tickles!"
    scene ch7sc02_079 with dissolve
    mc "Oh does it?"
    mc "Then this will really get you."
    lu "What are you-"
    scene ch7sc02_080 with dissolve
    lu "*Squeals* UuuaahHh-Aiiiyh!"
    with vpunch
    scene ch7sc02_079 with dissolve
    lu "You’re so done!! Aiiyhh! So done!"
    lu "Just wait until I-"
    scene ch7sc02_080 with dissolve
    lu "Ahh-Aiiyh! *Giggles* s-stop it!"
    scene ch7sc02_079 with dissolve
    mc "You were saying?"
    lu "That you’re going down! Uh-huh! Big time buddy!"
    scene ch7sc02_080 with dissolve
    lu "*Squeals* WuuaahhH!! I-I didn’t mean it! Hahaha! P-Please put me down, sweet and kind sir!"
    scene ch7sc02_079 with dissolve
    mc "*Chuckles* This is what you get for being overconfident."
    mc "Trust me… it’s a whole lot better than what I got whenever I was overconfident."
    mc "But your barrier did just take three of my wind-javelins, only the 4th managed to overwhelm you."
    scene ch7sc02_081 with dissolve
    lu "So you’re admitting I was pretty awesome? *Giggles*"
    mc "*Chuckles* Yeah, yeah… you were pretty awesome."
    lu "I’m still baffled at your ability to cast spells with such ease… now, are you going to-"
    scene ch7sc02_082 with dissolve
    uk "*Distant shouting* Help! Somebody help!"
    lu "*Gasps* [mc], did you hear that?! I think someone is in distress!"
    mc "Yeah, I heard it."
    mc "Let’s check it out, but be on guard… it could be a trap, bandits like to pretend to be in distress before they ambush you."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "The two of you trace the calls for help to the nearby ruins."
    scene ch7sc02_083 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    uk "Anybody?! H-Help! Please! *Coughs* Me wife! They-... they’ve got me wife!"
    lu "Sir?! Are you alright?!"
    scene ch7sc02_084 with dissolve
    uk "I think so? I got away with a few bruises… *Coughs* But me wife! They’ve got me wife!"
    lu "Your wife? Who has her? Bandits?!"
    scene ch7sc02_085 with dissolve
    uk "Bandits? Naye… it t’weren’t bandits miss!"
    lu "Sir, please… you need to tell us what happened if we are to help you."
    uk "B-Beasts! It t’were beasts miss! Foul creatures!"
    uk "T-They came out of nowhere! No warnings! Just attacked us! I can still hear the screams of me wife as I fled our home."
    scene ch7sc02_086 with dissolve
    with vpunch
    mc "You what?! You left your wife behind to be mutilated by ‘beasts’?!"
    mc "What kind of man leaves his wife to save his own ass?!"
    lu "Tsk!"
    scene ch7sc02_087 with dissolve
    lu "[mc], let’s not waste anymore time on him, we need to help her!"
    "You nod in agreement, the important thing is getting to the wife if she hasn’t been killed already."
    scene ch7sc02_086 with dissolve
    with vpunch
    mc "Where is your home located! SPEAK!"
    scene ch7sc02_085 with dissolve
    uk "Uh! A little ways to the north, I didn’t mean to leave her behind, but what was I to do?"
    uk "I’m no fighter! I tend to our crops is all!"
    scene ch7sc02_087 with dissolve
    with vpunch
    lu "[mc]! We need to get there now!"
    scene ch7sc02_088 with dissolve
    with vpunch
    lu "*Squeals* Aiiyh!"
    mc "Hold on tight, I’ll make this quick."
    lu "Mmh! Go!"
    scene ch7sc02_089a with dissolve
    lu "I wish you were lifting me under a more favorable circumstance…"
    scene ch7sc02_089 with dissolve
    mc "You’ll still feel a rush."
    scene ch7sc02_090a with dissolve
    with vpunch
    "The two of you vanish in a flash of red energy as you surge forward at full speed."
    scene ch7sc02_090 with dissolve
    $ renpy.pause(1)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene warning_2 with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Graphic scene ahead, skip it if you are sensitive to violence."
    menu:
        "Watch the scene":
            scene ch7sc02_091 with Dissolve(1.5)
            with vpunch
            $ renpy.pause(0.5)
            wo "*Groans* Aah! Auuah! Hnngh! Stop! {b}AAH!!{/b}"
            wo "{b}*Gut-wrenching moans*{/b} Aah! UghRh! Ah!"
            scene ch7sc02_092 with dissolve
            with vpunch
            wo "N-No! Not again! S-Stay away creature! Ah!"
            wo "I-I can’t handle anymore! Let go of mee- Urgh!"
            scene ch7sc02_093 with dissolve
            with vpunch
            gob "Ghnarr! More! Hnnaa!"
            scene ch7sc02_095 with dissolve
            wo "{b}*Screams* Aiiiyhhh!! NO!!{/b}"
            with vpunch
            scene black with Dissolve(1.5)
            wo "Please! *Sobbing and groaning* Not again! Stop!"
            with vpunch
            wo "{b}*Screams in pain* AHH!!{/b}- Aiigh!! Uaiiigh!"
            #play music summon_3 fadein 1.0
            #stop music fadeout 1.0
            $ renpy.pause(0.5)
            with vpunch
            wo "{b}*Screams in pain*{/b} Aiiyh-iighh! AhhHr!!"
            scene ch7sc02_098 with Dissolve(1.5)
            $ renpy.pause(0.5)
            gob "Ghaah! Good breed! Hooman soft and tight! Hegh-hegh-hegh!"
            wo "*Whimpers in pain* Nnh-ggnnh… no… no…"
            gob "Hooman no struggle when I filled pussy! Hooman wants to be bred! Hegh-hegh!"
            gob "Hooman best breeders! Hegh-hegh! Tighter than gobbos!"
            gob "True dat! Haagh! Love me hooman pussy!"
            scene ch7sc02_099 with dissolve
            gob "We tell bigboss Chief Gamthul this area has good hoomans fer breeding! Big reward fer us! Hegh-hegh!"
            gob "Hnnahh! Gamthul let us keep this one fer breeding ye’thinks?"


        "Skip the scene":
            scene ch7sc02_091 with Dissolve(1.5)
            with vpunch
            $ renpy.pause(0.5)
            wo "*Groans* Aah! Auuah! Hnngh! Stop! {b}AAH!!{/b}"
            wo "{b}*Gut-wrenching moans*{/b} Aah! UghRh! Ah!"
            scene ch7sc02_099 with dissolve



    scene ch7sc02_099
    gob "Me’thinks we breed her again tomorrow! Hegh-hegh! me wants more hooman pussy."
    scene ch7sc02_100 with dissolve
    with vpunch
    gob "*Groans in agony* Ghhrh! Me cock! GHhrh! It burns!!"
    with vpunch
    gob "Ghaaah! Hooman! Me breed you too!"
    scene ch7sc02_101 with dissolve
    with vpunch
    gob "Ghharh! Me burns! HhGgh!"
    scene ch7sc02_102 with dissolve
    with vpunch
    lu "Go! See if the wife is still alive! I’ll make sure these nasty bastards are burned to a crisp!"
    mc "On it!"
    scene ch7sc02_103 with dissolve
    mct "Fuck! She’s in bad shape!"
    mct "Judging by her wounds and the dried blood both on the floor and her body…"
    mct "They’ve been assaulting her for hours."
    scene ch7sc02_104 with dissolve
    mct "She’s alive!"
    mct "But-... her pulse is barely there, she’s hanging on by a thread!"
    "You grab her gently and place her on the bench."
    scene ch7sc02_105 with dissolve
    mct "I have to heal her."
    lu "[mc] is everything okay in here? Is she alive?"
    mc "Luna don’t come in! You shouldn’t see her like this!"
    with vpunch
    lu "*Squeals* Aiiiyh!"
    scene ch7sc02_106 with dissolve
    mc "I told you to stay out! You shouldn’t see another woman in this state."
    lu "Is she… is she dead?!"
    mc "No, she’s barely hanging on. I have to heal her. Did you take care of the goblins?"
    lu "Yes, I did a quick lap around the house, but there was only the two of them."
    mc "Luna, go outside and keep watch."
    with vpunch
    mc "{b}NOW!!{/b}"
    scene ch7sc02_105 with dissolve
    "Luna follows your command without objections, knowing she can handle them with ease if any more show up, you can focus on the woman."
    scene ch7sc02_107 with dissolve
    mc "I’m sorry this happened to you… I’ll do what I can to make it better."
    scene ch7sc02_108 with dissolve
    "To your surprise, the woman finds enough strength to lift her arm to reach for you."
    wo "*Whimpers in pain* Hnngh-hhnh… thank-... hnngh… thank you…"
    scene ch7sc02_107 with dissolve
    "After having managed to utter the words, her arm loses its remaining strength and you begin healing her before she fades completely."
    scene ch7sc02_109 with dissolve
    wo "*Moans and whimpers softly* Nngh- nngh…"
    mc "You’ll be okay… I’ll make sure of it."
    mc "My friend is just outside, she took care of the goblins that violated you… they will never hurt you again."
    scene ch7sc02_110 with dissolve
    "You manage to heal all her lacerations, bruises and wounds, she passed out during the process but her pulse is steady."
    mct "*Sighs* Five hells… fucking goblins… this close to the capital as well? They’re becoming a problem."
    scene ch7sc02_111 with dissolve
    mct "I know her husband isn’t a trained fighter, but when this is the fate that awaits your wife…"
    mct "You fucking man up and defend her with every little bit of strength you have."
    mct "What is a woman like her doing with such a pathetic man?"
    scene ch7sc02_112 with dissolve
    mc "Luna! Get in here, I could use your help to find some clothes for her!"
    lu "Coming!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch7sc02_113 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Thank you, I’m going to bring her to the healers back at the royal palace."
    lu "Will she be okay? I thought you healed her?"
    mc "I think so, but I’m not exactly an expert healer… I want her properly attended to."
    scene ch7sc02_114 with dissolve
    mc "Also… judging by her wounds and the state she was in, she endured hours of repeated rape."
    mc "Her mental state is severely traumatized."
    scene ch7sc02_113 with dissolve
    mc "She needs someone with her when she wakes up, someone more qualified than me, to talk to."
    scene ch7sc02_114 with dissolve
    lu "Mhm, you’re right, healers would be used to speaking to all sorts of victims… I’ll meet you there as fast as I can!"
    mc "Go straight there. I don’t want you out here on your own, goblins live in large groups."
    lu "Trust me, as much as I would love to call down a few meteors on their encampment, I’m not arrogant enough to attempt such a thing…"
    lu "Not without you."
    scene ch7sc02_113 with dissolve
    mc "I’ll see you at the palace. Be safe."
    lu "Run as fast as you can."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss13 with Dissolve(1.5)
    $ renpy.pause()
    scene ch7sc02_115 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "What do you think? Will she be alright?"
    uk "Ahh, most definitely! You say this woman was near death from a goblin attack when you found her?"
    uk "Curious, I don’t see any scars? No surface wounds or anything?"
    scene ch7sc02_116 with dissolve
    uk "In fact… I find it hard to believe this woman was attacked as you claim, she seems perfectly healthy to me."
    mc "You’ll just have to trust me."
    mc "She’s going to need someone around when she wakes up, someone who has experience with traumatic events."
    uk "Hmmh, naye… I doubt she will need such a thing, she most likely passed out from drinking."
    scene ch7sc02_115 with dissolve
    uk "I’ll send her on her way when she awakens, we can’t be keeping peasants here… she’ll just take up valuable space."
    scene ch7sc02_117 with dissolve
    with vpunch
    qm "You will do no such thing!"
    qm "The lady is to be treated the same as if she were a noblewoman, got it?"
    uk "My Queen! Oh of course… she will be treated as you wish."
    qm "Good, now leave us. Bring more clerics, I want her thoroughly examined."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch7sc02_118 with dissolve
    mc "Thank you…"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "I doubt he would’ve taken her injuries seriously if you hadn’t arrived."
    scene ch7sc02_119 with dissolve
    qm "You know better than to believe I need to be thanked for such a small gesture."
    qm "Is she a friend of yours sweetie?"
    scene ch7sc02_120 with dissolve
    mc "Not exactly… you know how I was supposed to spend the day with my friend, Luna?"
    scene ch7sc02_119 with dissolve
    qm "Yes?"
    scene ch7sc02_120 with dissolve
    mc "We went into the forest to the north of Luxenford, and we encountered a man and his wife, being attacked by goblins."
    scene ch7sc02_121 with dissolve
    qm "Then goblins remain a problem… growing bolder too it seems, to venture this close to the city."
    mc "Mhm… the villagers and peasants living secluded are easy pickings for goblins."
    qm "Tsk! And my husband does nothing to stop them! He doesn’t believe them to be a serious threat!"
    "You can tell by Merida's tone that seeing the woman suffer really bothers her."
    scene ch7sc02_122 with dissolve
    qm "Look at this woman! I can only imagine the condition she was in when you found her…"
    mc "It wasn’t pretty, I can tell you that."
    qm "These are our people… we can’t just leave them to fend for themselves just because they aren’t living within the city walls!"
    scene ch7sc02_121 with dissolve
    mc "I’m guessing Bennen isn’t willing to spend military might to squash the goblin menace?"
    qm "Not with a rebellion on the horizon…"
    scene ch7sc02_123 with dissolve
    qm "[mc], where is her husband? Why isn’t he here attending to her?"
    qm "Was he… killed by the goblins?"
    scene ch7sc02_124 with dissolve
    mc "No… worse, he abandoned her to a fate worse than death for a woman."
    "Merida doesn't need details, her expression clearly conveys that she is fully aware of what you mean."
    scene ch7sc02_125 with dissolve
    qm "Oh goodness… poor thing."
    qm "I can’t imagine how a man could possibly leave behind his wife? His partner?! His love?!"
    scene ch7sc02_123 with dissolve
    qm "I will have their marriage nullified. She deserves better… much better."
    scene ch7sc02_124 with dissolve
    mc "Probably a wise decision, I don’t imagine he will change… if they got attacked again, he would run off like a coward again."
    scene ch7sc02_125 with dissolve
    qm "[mc], I can’t let her go back to that place! Not with goblins getting this bold…"
    scene ch7sc02_126 with dissolve
    qm "Honey, would you be able to take her in? When you finish establishing your homestead?"
    scene ch7sc02_127 with dissolve
    mc "Oh… I don’t know… Merida, I don’t even know this woman?"
    mc "Wouldn’t it be better if she stayed here at least?"
    scene ch7sc02_126 with dissolve
    qm "You might not know her, yet. But you are the man who saved her, and I’m sure she will feel grateful to you for that."
    qm "It’s not possible for her to remain here, however…"
    scene ch7sc02_128 with dissolve
    qm "As I know you aren’t capable of taking her in right away, how about a compromise?"
    scene ch7sc02_127 with dissolve
    mc "A compromise? What do you have in mind?"
    scene ch7sc02_126 with dissolve
    qm "She will remain here at the palace until your homestead has been built."
    scene ch7sc02_128 with dissolve
    qm "I will have her partake in housekeeping and maid duties, in return she will be fed and have a warm bed."
    qm "Then when it’s time for you to take her in, she will be well versed in housekeeping and she can continue to earn her keep-"
    scene ch7sc02_126 with dissolve
    qm "-By serving you, as you’re a lord now, having maids and housekeepers amongst other things comes with the title."
    qm "In return for her services, you will provide her with a roof over her head and protection against the fate she avoided, thanks to you."
    scene ch7sc02_127 with dissolve
    mc "*Sighs heavily* How am I meant to argue when you make valid and reasonable points?"
    scene ch7sc02_129 with dissolve
    qm "*Giggles happily* Simple, you don’t argue against me!"
    qm "And since she’ll be staying here at the palace, I think it would be good if you stop by every so often and meet with her."
    scene ch7sc02_126 with dissolve
    qm "That will give you the chance to get to know each other before she joins you at your homestead."
    scene ch7sc02_127 with dissolve
    mc "Sounds good, I’m going to be here rather often anyways, because of you and Amelia."
    scene ch7sc02_119 with dissolve
    qm "Exactly, this is just one more reason for you to visit. *Giggles softly*"
    scene ch7sc02_120 with dissolve
    mc "When it’s time, I will ask her what she wants to do. If she doesn’t wish to work for me, then I won’t force it upon her."
    scene ch7sc02_119 with dissolve
    qm "And this is exactly why I believe you will be the best suited match for her, you’re actually a man."
    qm "And of course, if it comes to it and she doesn’t wish to join you, at least we will have allowed her to regain her footing in the world."
    scene ch7sc02_127 with dissolve
    mc "Yeah, thank you for helping with this… I’m sure you will have to jump through some hoops to make this happen."
    scene ch7sc02_128 with dissolve
    qm "Think nothing of it, Bennen is so occupied with the brewing war, that he isn’t concerned with our staff."
    scene ch7sc02_129 with dissolve
    qm "Now, I believe you should get back to your friend? I doubt this lady will wake up anytime soon."
    scene ch7sc02_127 with dissolve
    mc "You’re right, I appreciate you Merida."
    scene ch7sc02_129 with dissolve
    qm "As I appreciate you, I’m glad you continue to show what a rare kind of a man you are."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss66 with Dissolve(1.5)
    $ renpy.pause()
    scene ch7sc01_321 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "There she is, she must’ve ran like a bat out of hell to get here this soon."
    scene ch7sc02_130 with dissolve
    lu "[mc]! Hi, how is she?"
    lu "Is she awake?"
    scene ch7sc02_131 with dissolve
    mc "Hey… no, not yet."
    mc "But they examined her and they almost didn’t believe she had undergone any physical pain."
    scene ch7sc02_132 with dissolve
    lu "Huuh?! How could they not believe it?!"
    scene ch7sc02_133 with dissolve
    lu "Oh! Right… probably because you healed her?"
    scene ch7sc02_131 with dissolve
    mc "Exactly… the healer just thought she was passed out from being drunk or something."
    scene ch7sc02_132 with dissolve
    lu "He can’t be serious?! [mc], we have to do something!"
    lu "That type of healer won’t take her injuries seriously!"
    scene ch7sc02_131 with dissolve
    mc "Don’t worry, the queen handled it. They will treat her as if she was a noblewoman."
    scene ch7sc02_133 with dissolve
    lu "Thank goodness…"
    scene ch7sc02_134 with dissolve
    lu "But… what about after she’s fully restored?"
    lu "She can’t go back there… not to that deadbeat husband and… not to mention the trauma being in that place would inflict."
    scene ch7sc02_135 with dissolve
    mc "*Chuckles* Seems like you are of one mind with the queen herself."
    scene ch7sc02_134 with dissolve
    lu "Well obviously… we’re wise women! But… what do you mean?"
    scene ch7sc02_135 with dissolve
    mc "Queen Merida has offered to let her stay here at the palace for the time being, and have her trained in housekeeping and maid duties."
    scene ch7sc02_133 with dissolve
    lu "Oh! That’s actually really clever of her!"
    lu "Then she can earn her keep and not have to go back to that… coward."
    scene ch7sc02_131 with dissolve
    mc "Mhm, when the woman wakes up, Merida will offer her to nullify their marriage if that is what the woman wants."
    scene ch7sc02_134 with dissolve
    lu "Good! No woman deserves to be treated like that and she can do much better than that ugly coward!"
    scene ch7sc02_135 with dissolve
    mc "*Chuckles* I’m not used to seeing you this fired up, pun intended."
    scene ch7sc02_134 with dissolve
    lu "I don’t like creeps and cowardly men aren’t far behind creeps in that department."
    scene ch7sc02_135 with dissolve
    mc "Yeah… when I examined her body, she had old bruises…"
    scene ch7sc02_132 with dissolve
    lu "Huh?! As in… not from today?"
    scene ch7sc02_131 with dissolve
    mc "Yeah… her husband has been beating her regularly."
    scene ch7sc02_136 with dissolve
    with vpunch
    lu "{b}*Shouts in anger*{/b} Seriously!? What the fuck is wrong with such men! {b}UGH!{/b}"
    scene ch7sc02_134 with dissolve
    lu "Sorry… it’s just so fucking often you hear things like this…"
    scene ch7sc02_135 with dissolve
    mc "Hey, don’t apologize… your anger is warranted."
    mc "That man is trash, and I sincerely hope she will accept Merida’s offer of nullifying their marriage."
    scene ch7sc02_134 with dissolve
    lu "She better! She still has plenty of life ahead of her to find a better man."
    scene ch7sc02_133 with dissolve
    lu "She looked to be in her late 30’s or early 40’s. That’s like nothing! My mother is that age."
    lu "And I know she still longs to find a man who she can trust herself with and spend her life with."
    scene ch7sc02_131 with dissolve
    mc "Yeah, both your mother and this woman will find men worthy of them, I’m sure."
    scene ch7sc02_133 with dissolve
    lu "Speaking of worthy men… I suppose you’d like to end our day here?"
    scene ch7sc02_134 with dissolve
    lu "I’m sure you feel like this whole ordeal has put a damper on things?"
    scene ch7sc02_135 with dissolve
    mc "Don’t be silly, I’m still game if you are."
    "Luna looks at you pleasantly surprised by your answer."
    scene ch7sc02_137 with dissolve
    lu "I mean… a girl’s gotta eat, right? *Giggles softly*"
    lu "I suppose I wouldn’t find it too terrible if you… took me somewhere to eat?"
    scene ch7sc02_138 with dissolve
    mc "*Chuckles* C’mon then little witch, I know a spot just perfect for a dinner with you..."
    lu "Oh? You were already planning to take me out to eat today? Such a gentleman! *Giggles*"
    mc "You bet I did, I know what a little glutton you are. *Chuckles*"
    lu "Hey! I only ate that many pastries this morning because I was starving, besides… I was feeling spiteful towards that guy! *Snickers*"
    mc "Yeah, yeah… we’ll see soon enough. Let’s go."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "You bring Luna down to the royal port of Luxenford, where one of the overwater gazebos are available for the two of you."
    play music mmm_elven_forest fadein 1.0
    #stop music fadeout 1.0
    scene ch7sc02_139 with Dissolve(1.5)
    $ renpy.pause(0.5)
    lu "*Gasps* Stooopp! No way!"
    lu "[mc]... this is… just perfect."
    scene ch7sc02_140 with dissolve
    lu "*Squeals happily* iiihHh! This is so cute!"
    lu "You’re really setting a new standard for all men! *Giggles*"
    scene ch7sc02_141 with dissolve
    mc "My lady, your seat is ready."
    lu "*Giggles happily* Such a gentleman!"
    scene ch7sc02_142 with dissolve
    "You feel Luna’s soft delicate lips merge with your cheek."
    lu "*Mwaahh* Thank you for being such a man."
    mc "You’re welcome, after how you took down those goblins today, you’ve earned this."
    if luna_relationship == True:
        scene ch7sc02_143 with Dissolve(1.5)
        $ renpy.pause(0.5)
        lu "Quit it!"
        mc "*Chuckles* Quit what?"
        lu "You know full well what! You’re making me shy! Looking at me like this…"
        scene ch7sc02_144 with dissolve
        lu "You’re looking at me like… like… you want me for dinner!"
        mc "I am feeling a little hungry… and you do look very edible... *Chuckles*"
        lu "*Giggles* Stooop! You’re being bad!"
        scene ch7sc02_145 with dissolve
        mc "*Chuckles* Alright, alright… you know, I’m proud of you though."
        scene ch7sc02_146 with dissolve
        lu "Y-You are?"
        scene ch7sc02_145 with dissolve
        mc "I am."

    else:
        scene ch7sc02_143 with Dissolve(1.5)
        $ renpy.pause(0.5)
        lu "You're staring... stop, otherwise I'll blush."
        scene ch7sc02_145 with dissolve
        mc "*Chuckles* Alright, alright… you know, I’m proud of you though."
        scene ch7sc02_146 with dissolve
        lu "Y-You are?"
        scene ch7sc02_145 with dissolve
        mc "I am."

    scene ch7sc02_147 with dissolve
    mc "I was impressed with how well you handled yourself today."
    mc "Being faced with something that gruesome first hand… the shock of it can affect us all differently."
    scene ch7sc02_145 with dissolve
    mc "But despite the shock of seeing what they did to her, you kept yourself calm and collected."
    scene ch7sc02_146 with dissolve
    lu "Well I had to be, her life was on the line."
    lu "You’re giving me too much credit…"
    scene ch7sc02_145 with dissolve
    mc "Trust me, I’m not."
    mc "I’ve been in countless situations just like that one, and you’d be surprised how many people would react like the husband did."
    scene ch7sc02_147 with dissolve
    mc "But not you… you took care of those goblins and helped rescue someone."
    scene ch7sc02_148 with dissolve
    lu "I suppose we did save someone’s life together today."
    lu "That makes us pretty awesome, right?"
    scene ch7sc02_145 with dissolve
    mc "The awesomest of awesome. *Chuckles*"
    scene ch7sc02_146 with dissolve
    lu "Awesomest of awesome! I like that! *Giggles*"
    scene ch7sc02_148 with dissolve
    lu "It was a little scary… but it felt great, knowing that we’ve been able to help someone like her."
    lu "I guess I am an adventurer now after all."
    scene ch7sc02_145 with dissolve
    mc "You certainly are, it might not have been an official quest or anything…"
    scene ch7sc02_147 with dissolve
    mc "But a part of being an adventurer isn’t just accepting quests, but also taking on things as they happen."
    mc "Being present in the moment and doing what you can."
    scene ch7sc02_148 with dissolve
    lu "Yeah… I got a sense of that today, it felt so fulfilling to help someone."
    scene ch7sc02_149 with dissolve
    lu "If Rose is going to remain in charge of the Mage’s guild, I don’t want to have any part in it…"
    lu "So I suppose it’s a good thing I’m a part of your guild as well."
    scene ch7sc02_150 with dissolve
    lu "Although, I do hope not all quests or adventures involve nasty goblins! *Snickers*"
    lu "They smelled so bad when I crisped them! Eeuuw!"
    scene ch7sc02_143 with dissolve
    mc "With how charred they were after just one fireball… I’m glad you didn’t hit me with one earlier. *Chuckles*"
    lu "I totally could have! I just didn’t want to… you know, hurt you or anything."
    scene ch7sc02_144 with dissolve
    mc "I know, you were just trying to show me what you’re capable of."
    lu "Exactly… although I may have went a little overboard."
    mc "Nah, you kept us safe with that barrier… how did you even manage to produce one that powerful?"
    scene ch7sc02_146 with dissolve
    lu "Remember how I channeled you before? When we traced mother’s hex? Or when I taught you about seals?"
    scene ch7sc02_145 with dissolve
    mc "Mmh, yeah?"
    scene ch7sc02_146 with dissolve
    lu "Well, I was able to channel you since we made contact with our embrace, so your energy helped me enhance the barrier."
    scene ch7sc02_148 with dissolve
    lu "Otherwise I doubt I could manage a barrier powerful enough to protect from several meteors."
    scene ch7sc02_147 with dissolve
    mc "Still, I was quite impressed."
    mc "Even after all of that, you also managed to block three of my wind-javelins. And they are rather potent."
    scene ch7sc02_148 with dissolve
    lu "Y-Yeah… I felt each one of them as they struck my barrier, it really took a lot out of me."
    scene ch7sc02_149 with dissolve
    lu "In the end, I wasn’t strong enough to handle the 4th."
    scene ch7sc02_150 with dissolve
    lu "But I’m going to keep practicing and improving, just like I have been!"
    lu "I want to be able to-..."
    scene ch7sc02_149 with dissolve
    lu "To be someone who can stand by your side… and not hold you back."
    scene ch7sc02_147 with dissolve
    mct "It’s nice to see her this inspired."
    mct "Luna has grown a lot, she isn't just a young girl from the academy any longer."
    mct "She's growing into a beautiful and capable woman."
    mc "You’re more than capable of standing by my side already, but I agree. We should all strive to improve."
    scene ch7sc02_154 with dissolve
    uk "Here you go, two plates of lemon-roasted chicken with veggie-mix on the side for the lovely couple."
    mc "Thank you. That’ll be all."
    uk "Certainly, I hope the couple will let me know if there is anything you need. I’ll be in the port restaurant."
    scene ch7sc02_151 with dissolve
    lu "*Giggles happily* …"
    mc "What? *Chuckles*"
    scene ch7sc02_152 with dissolve
    lu "You didn’t correct him."
    scene ch7sc02_151 with dissolve
    mc "It doesn’t concern him what we are."
    lu "*Giggles* …"
    scene ch7sc02_152 with dissolve
    lu "You’re cute!"
    lu "Now, let’s devour this lemon-roasted chicken! I bet it’s real juicy! *Snickers*"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch7sc02_153 with dissolve
    lu "Ooohhh sweet magical goodness! I needed this!"
    mc "You sure looked like you enjoyed that."
    lu "D-Don’t look at me right now… I feel like my belly is going to burst my vest wide open any moment! Aaahhh…"

    if luna_relationship == True:
        mc "Oh the horror… I definitely wouldn’t want to see that happening. *Chuckles*"
        scene ch7sc02_155 with dissolve
        lu "Yeah we definitely wouldn’t want you to see my breasts burst out of this top like they have been attempting to do all day. *Giggles*"
        lu "You know I bought this top specifically for you?"
        scene ch7sc02_156 with dissolve
        mc "You did? I’ve gotta say… I agree with that decision."
        scene ch7sc02_155 with dissolve
        lu "Oh I’m well aware how much you like this decision…"
        lu "And yes, if you noticed, I started wearing it after we talked about going on a date a while back."
        scene ch7sc02_156 with dissolve
        mc "Now that you mention it, so you went out and bought it for tonight?"
        scene ch7sc02_155 with dissolve
        lu "Not just tonight, tonight was just the main event for it… but with the looks you’ve given me every time I’ve worn it around you…"
        lu "Makes me want to keep wearing it around you… I like seeing you hungry… for me. *Giggles*"
        scene ch7sc02_156 with dissolve
        mc "Mmh… I think I know what I want for dessert."
        lu "*Giggles softly* …"
        scene ch7sc02_157 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_156 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_158 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_160 with dissolve
        $ renpy.pause(1)
        mc "Five hells… you’re a naughty little witch."
        mc "Let me see them again."
        scene ch7sc02_158 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_160 with dissolve
        $ renpy.pause(1)
        "Luna giggles while enjoying how captivated you are by her breasts"
        scene ch7sc02_158 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_160 with dissolve
        $ renpy.pause(1)
        mc "Girl… stop teasing me already and let me enjoy the view of you with the sunset."
        scene ch7sc02_158 with dissolve
        lu "*Giggles* …"
        scene ch7sc02_159 with dissolve
        lu "I think it’s safe to say that you enjoy what you see?"
        scene ch7sc02_158 with dissolve
        mc "Saying I enjoy what I’m seeing in front of me would be the understatement of the century."
        mc "You’re an incredible woman, Luna."
        scene ch7sc02_159 with dissolve
        lu "An incredible woman… for an incredible man… I like that match."
        scene ch7sc02_158 with dissolve
        mc "As do I…"
        scene ch7sc02_161 with dissolve
        lu "*Giggles softly* My eyes are up here, you know?"
        mc "Oh I know… but your breasts are down here."
        lu "I think we both know what’s on the menu for dessert. *Giggles*"
        scene ch7sc02_162 with dissolve
        lu "The idea of sucking my sensitive and perky nipples is enticing to you?"
        scene ch7sc02_161 with dissolve
        mc "Yeah… it is."
        scene ch7sc02_162 with dissolve
        lu "Good… then I have an idea."
        scene ch7sc02_163 with dissolve
        mc "Oh? What are you-"
        lu "Just going to apply a little taste for you to enjoy when we get back to my dormitory. *Giggles*"
        scene ch7sc02_162 with dissolve
        lu "There we go… mmh… I’m thinking lemon juice will go well with my nipple."
        scene ch7sc02_161 with dissolve
        mc "Especially with all the activities we’ve done today… your skin is bound to be a little salty from sweat."
        scene ch7sc02_162 with dissolve
        lu "I can’t wait for your mouth to be around my nipples now… Mmmh."
        scene ch7sc02_158 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_160 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_155 with dissolve
        lu "That’s all you’re getting for now! *Giggles*"
        mc "Hey… I wasn’t done enjoying them."
        scene ch7sc02_155 with dissolve
        lu "Good, that means you will be eager to get to them once we’re alone."
        lu "It’s funny… I hate when guys stare at me at the academy… but when I notice you looking at me…"
        lu "I just want to keep you enticed to look at me… again… and again…"
        scene ch7sc02_156 with dissolve
        mc "It’s because you have feelings for me."
        scene ch7sc02_155 with dissolve
        lu "I suppose denying that would be incredibly silly at this point? *Giggles happily*"
        lu "You have feelings for me too, don’t you?"
        scene ch7sc02_155 with dissolve
        mc "Obviously… I can’t get enough of you."
        scene ch7sc02_157 with dissolve
        lu "*Snickers* …"
        scene ch7sc02_156 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_159 with dissolve
        $ renpy.pause(1)
        lu "I think you should escort me back to my dormitory… after all, you haven’t seen my room yet."
        scene ch7sc02_160 with dissolve
        mc "*Chuckles* Yeah… I think it’s time I thoroughly see your… room."
        scene ch7sc02_155 with dissolve
        lu "[mc]... will you… spend the night with me?"
        scene ch7sc02_156 with dissolve
        mc "There’s nothing I want more Luna. Let’s go."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        "Luna nods happily and she takes your arm as you leave the dockside gazebo."
        scene ch7sc02_164 with Dissolve(1.5)
        $ renpy.pause(1)
        play music morning_1 fadein 1.0
        #stop music fadeout 1.0
        lu "*Giggles* Arranging an overwater gazebo dinner… carrying me in your arms from the royal docks and all the way here to the academy…"
        lu "You really are a romantic!"
        scene ch7sc02_165 with dissolve
        lu "I feel so tiny in your arms…"
        lu "I feel really special right now… when you hold me like this."
        scene ch7sc02_166 with dissolve
        mc "You are special Luna. More so than you can imagine."
        scene ch7sc02_167 with dissolve
        lu "Mmmh…"
        "Luna gently runs her tongue across your lips, covering them in her saliva."
        scene ch7sc02_165 with dissolve
        lu "This is my first date… and you… you have made it so precious to me."
        scene ch7sc02_167 with dissolve
        lu "Mmnnh-nnh…"
        scene ch7sc02_168 with dissolve
        lu "I’ve-... I’ve fallen in love with you."
        lu "And please don’t feel obligated to say it back… not before you feel it as well-"
        scene ch7sc02_166 with dissolve
        mc "I’ve fallen in love with you as well."
        scene ch7sc02_165 with dissolve
        lu "[mc]... you-... you have?"
        scene ch7sc02_167 with dissolve
        mc "*Kisses* MMmh-hm. Completely…"
        lu "Nnnh… please… carry me to my room…"
        scene ch7sc02_168 with dissolve
        lu "We’re wearing way too much clothes for how happy you make me feel… way too much clothes."
        mc "Say no more."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You proceed to carry her through the academy dormitories until you reach her room."
        scene ch7sc02_169 with Dissolve(1.5)
        $ renpy.pause(0.7)
        lu "Hold on, it’s a little dark… allow me to set the mood. *Giggles softly*"
        lu "Incendia."
        scene ch7sc02_170 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_171 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_172 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_173 with dissolve
        $ renpy.pause(1)
        scene ch7sc02_174 with dissolve
        $ renpy.pause(1)
        lu "That should be sufficient, don’t you think?"
        mc "Damn Luna… I don’t know what I expected from a sorceress, but floating lights? That’s pretty awesome."
        scene ch7sc02_175 with dissolve
        lu "*Giggles* What’s the purpose of being able to do magic if you can’t enchant a few lights for ambiance!"
        lu "Don’t mind the mess… I was kind of scrambling this morning to meet you in time."
        scene ch7sc02_176 with dissolve
        mc "There’s a mess in here? All I see is a beautiful woman."
        lu "There you go again… giving me butterflies."
        lu "[mc]-"
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene ch7sc02_177 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        lu "*Gasps softly* Aaiih! [mc]!"
        lu "As if your compliments weren’t giving me enough butterflies already… you go and grab me like this? *Giggles*"
        scene ch7sc02_178 with dissolve
        mc "What can I say… I know how much my little witch enjoys a hands-on approach."
        "She looks you directly in the eyes with a cheeky smile."
        scene ch7sc02_177 with dissolve
        lu "Only when it’s your hands… anyone else’s hands would be set aflame."
        scene ch7sc02_179 with dissolve
        lu "I’m thinking… you should help me undress."
        lu "After all… it’s time for you to have your dessert. *Giggles softly*"
        scene ch7sc02_180 with dissolve
        with vpunch
        lu "*Gasps softly* Aiih! Mmh!"
        "You pull her close and hold her firmly as you begin exploring her tight body."
        mc "As much as I love this top on you… I much prefer it to be off you."
        scene ch7sc02_181 with dissolve
        lu "*Whimpers softly* Mmmnh… I love how you grab my breasts as if they already belong to you… nnngh."
        scene ch7sc02_182 with dissolve
        mc "They do belong to me."
        scene ch7sc02_181 with dissolve
        mc "You belong to me, Luna. Mmh…"
        scene ch7sc02_182 with dissolve
        lu "*Whimpers* Aahh… nnh… yes… I do… mmh."
        scene ch7sc02_181 with dissolve
        lu "Please… undress me… nngh… I-... I want to feel your warm hands touch them."
        scene ch7sc02_183 with dissolve
        lu "*Moans* Nnnghh… yes… just how I imagined you would feel- Nnnh…"
        mc "Fuck… your breasts are undeniably created by the gods themselves. Mmmh…"
        scene ch7sc02_184 with dissolve
        lu "Nnn-mmh… give me your tongue while you feel them."
        "Luna begins teasing your tongue with the tip of hers as they meet between your lips, and you continue to caress and squeeze her breasts."
        scene ch7sc02_185 with dissolve
        lu "*Moans* Mmmgh… I love the taste of your tongue…"
        scene ch7sc02_184 with dissolve
        mc "Mmmh… *Licks* I can’t get enough of yours either… kissing a sorceress really is different… I can feel the magic vibrating within you."
        scene ch7sc02_185 with dissolve
        lu "*Whimpers softly* Aah-ah… g-gentle… mmh… my nipples are so sensitive right now."
        scene ch7sc02_184 with dissolve
        mc "Sorry… mmgh… I forget this is the first time they're being touched by a man. Mmmh… they’re amazing."
        scene ch7sc02_183 with dissolve
        lu "Please… *Moans softly* Please suck them?"
        mc "Nothing in this world can stop me from sucking them… mmh. Lay down on the bed for me."
        mc "And keep your eyes closed until you feel me."
        scene ch7sc02_186 with dissolve
        "She does as you ask, keeping her eyes closed as she lays down on the bed."
        lu "*Giggles* I’m feeling a little exposed here… but it’s exhilarating."
        mc "I had a feeling you would enjoy this, knowing that I’m taking in the full view of your incredible and enticing body."
        lu "I-... I do like knowing you’re watching me."
        scene ch7sc02_187 with dissolve
        lu "*Moans* Aaahh… I-... I feel you… you’re so warm- nnnh… c-can I open my eyes now?"
        mc "Not yet… tell me what you feel."
        scene ch7sc02_188 with dissolve
        lu "Mmmh… I feel… your warm hand, caressing my arm gently, letting me know I’m completely safe."
        mc "You’ll always be safe with me… what else?"
        scene ch7sc02_189 with dissolve
        lu "Nnhh… I feel… your hardened muscular chest… pressing against my soft, perky breast…"
        lu "Which lets me feel your heartbeat… how we’re completely in sync."
        lu "It makes me feel… like we’re made to be together… that your chest and my breasts are meant to be touching."
        mc "You’re right… we’re meant to be together. Mmmh, what else do you feel?"
        scene ch7sc02_190 with dissolve
        lu "I feel something… hard… warm… it’s… big… and… mmmh… it’s pulsating… pressing against my butt cheek…"
        lu "W-What is it [mc]? I… mmh… I like the feeling of it but… I’m not sure what it is?"
        mc "Mmh… what does your body tell you? Follow your intuition."
        lu "Your… mmh… your cock. Nnnh… my body is telling me that it’s your cock pressing against me."
        scene ch7sc02_189 with dissolve
        mc "Good girl… you did well."
        lu "[mc]... nnghh… please-... mmh… reward my nipple… I need you to- Mmmh… suck me."
        scene ch7sc02_188 with dissolve
        mc "Keep your eyes closed, I just want you to feel as I enjoy my dessert."
        lu "Ohhhkay… mmmh… please enjoy me…"
        scene ch7sc02_191 with dissolve
        "As you lean down to her enticing breast, you continue to gently but firmly hold her arm, ensuring she feels both safe but also at your mercy."
        lu "*Gasps softly* NNnh! Oh my! Mmmh! My nipple is touching your lips- Nnnh!"
        scene lu_lewd1a with dissolve
        $ renpy.pause(1, hard=True)
        "With the intense pleasure, Luna’s energy surges and fills the room with light through her enchanted lanterns as her moans deepen."
        lu "Aahhh… [mc]- yes… yess… I feel you- aah-hhn! I feel you sucking my nipple! Mmh!"
        "You keep a steady rhythm, slowly but intimately sucking her silky-soft breast and her perky lemon-juice covered nipple into your mouth."
        mct "Mmgh… the slighty saltiness from her sweat mixed with the sour lemon-juice… nngh… what an interesting combo."
        mct "Not to mention… mmgh… I can feel and taste her magic coursing through her breast and nipple just below her smooth skin."
        $ renpy.pause()
        scene ch7sc02_192 with dissolve
        lu "*Whimpers in pleasure* Nnh-nnhh… I love being in your mouth… being your dessert… mmmgh…"
        mct "Mmmgh… how can a breast be this perfect? Mmmh… she’s been quivering for the last couple of minutes now, she’s ready for more."
        scene ch7sc02_193 with dissolve
        "You grab her juicy soft thigh and pull her leg to the side, revealing her delicate little pussy, while you continue to taste her nipple."
        lu "*Moans intimately* Oh-nhhh! MMhhh-[mc]... I feel your touch… your magical hands… mmh… I want more."
        scene ch7sc02_194 with dissolve
        "You slide your hand down her warm thigh and gently across her wet pussylips, keeping them between your fingers."
        mc "*Sucks nipple* Nnngh… you’re so wet… mmmh…"
        "While you caress her pussy carefully, she too caresses your chest with her soft fingers and nails."
        "You can feel her heart pulsating through her breast, an incredibly intimate feeling."
        lu "*Moans* [mc]- nnnghh… please… I want to feel you… inside me- mmmh!"
        scene lu_lewd2 with dissolve
        $ renpy.pause(1, hard=True)
        "Hearing her moan and beg for you to enter her, you know it’s finally time, the moment the two of you have been waiting for… for months."
        lu "*Whimpers* Aahh-nngh… g-gentle… mmh… your fingers are so big… mmmh!"
        mc "You’re just tight… incredibly tight- nngh… *Licks nipple* and tasty… you’re everything I desire Luna."
        with vpunch
        lu "{b}*Moans* Aahh! W-What’s happening?! Mmmgh! [mc]!! I feel something!! Aiiiyh!{/b}"
        with vpunch
        $ renpy.pause(0.7)
        with vpunch
        mc "*Sucks nipple* MMmgh… you just came. A lot… mmmh…"
        lu "*Moans intimately* Sorry-nnghh… I… I couldn’t hold it back… not when you treat me this well- Mmmgh…"
        mc "Don’t apologize… feeling your orgasm was amazing… you’ll be doing it a lot tonight."
        $ renpy.pause()
        lu "*Moans* Oohh [mc]- aahh… I-... I want my dessert now… nnngh! Please let me suck you as well!"
        scene ch7sc02_194 with dissolve
        $ renpy.pause(0.9)
        scene ch7sc02_193 with dissolve
        $ renpy.pause(0.9)
        scene ch7sc02_192 with dissolve
        $ renpy.pause(0.7)
        scene ch7sc02_188 with dissolve
        mc "Where’s my manners… just enjoying my dessert without allowing you to have yours."
        scene ch7sc02_195 with dissolve
        with vpunch
        "Luna swiftly shuffles herself on top of you."
        "She puts her entire weight into pinning you down with her arms and legs, resting her lower waist onto your cock."
        lu "*Giggles softly* We already established that I’m a little glutton… you better believe I’m not skipping dessert!"
        scene ch7sc02_196 with dissolve
        mc "Go on little witch… enjoy your dessert."
        lu "Mmmh… I love how hard and muscular your body is… I want to…"
        scene ch7sc02_197 with dissolve
        lu "*Licks gently* Taste it."
        mc "Mmmh… fuck… your tongue feels incredible."
        scene ch7sc02_198 with dissolve
        "She caresses your nipple with her thumb while she runs her pink little tongue across your chest."
        scene ch7sc02_197 with dissolve
        lu "Mmmgh… *Licks* tasty- nngh… a little salty, I’m guessing from your sweat, but I like it."
        scene ch7sc02_198 with dissolve
        lu "Nnngh… but this isn’t my dessert, just a slight appetizer… my dessert is…"
        scene ch7sc02_199 with dissolve
        lu "This guy… *Licks intimately*"
        scene ch7sc02_200 with dissolve
        mc "Five hells… you’re the definition of magical."
        scene ch7sc02_201 with dissolve
        lu "Strange… the girls here at the academy always gossip about their boyfriends' cocks…"
        scene ch7sc02_200 with dissolve
        lu "They often complain saying they taste weird or bad?"
        scene ch7sc02_199 with dissolve
        lu "How could they not love this taste?"
        scene ch7sc02_200 with dissolve
        lu "Mmmgh… each lick is getting me more and more addicted."
        scene ch7sc02_201 with dissolve
        mc "Well, I don’t taste like other men."
        scene ch7sc02_200 with dissolve
        lu "Oh? Mmmh… because of being a Nephilim? Nnngh…"
        scene ch7sc02_199 with dissolve
        mc "Yeah- Aahh… A goddess told me that I taste differently compared to regular mortals, that my taste is meant to entice."
        scene ch7sc02_200 with dissolve
        lu "Oh it’s enticing- mmmgh…"
        scene ch7sc02_201 with dissolve
        lu "[mc]... licking you isn’t enough… I… I want to taste you in my mouth…"
        scene ch7sc02_202 with dissolve
        lu "I want to suck you."
        "Luna looks up to you, waiting for your approval. She continues to caress your tip with her warm, wet tongue while awaiting your answer."
        mc "Mmmh… you want a proper mouthful, don’t you?"
        lu "*Licks* Nnngh… please… let me fill my mouth with your cock and suck you."
        mc "Do it… my cock belongs to you tonight."
        scene ch7sc02_203 with dissolve
        "She eagerly widens her mouth as she presses her lips against your cock."
        "Allowing it to slide inside where you’re greeted by her saliva covered tongue."
        mc "Fuck… Luna… your saliva is filled with magic residue- ahh… it tingles… mmh."
        scene lu_lewd3 with dissolve
        $ renpy.pause(1, hard=True)
        lu "Mmffhp-mffhph! *Sucks and licks* I can taste your magic as well… nnngh!"
        lu "It’s been driving me insane… mmffhph… hearing all these other girls gossip about their boyfriends."
        lu "How they suck their cocks… how they fuck… knowing full well I didn’t want anyone… not until I met you- nngh-mmh!"
        $ renpy.pause()
        mc "Fuck… I’m glad you waited… mmhh… makes tonight even more special… knowing I’ll be your first."
        lu "Mmmgh… you were my first kiss… mmhhh… my first date… *Sucks* And now… my first lover."
        mc "Fuck… Nngh! Luna… I’m close- Aahh…"
        with vpunch
        lu "{b}*Sucks harder*{/b} Mmmgh! I want my dessert! {b}MMH!{/b} Fill my mouth… fill me completely!"
        with vpunch
        mc "*Moans* Aahh-mmh! Here it comes- AahHh! Fuck!"
        with vpunch
        scene ch7sc02_203 with dissolve
        $ renpy.pause(0.5)
        scene ch7sc02_204 with dissolve
        with vpunch
        lu "{b}*Muffled sucking and swallowing* MMGH! MFFH!! FFHHH!{/b}"
        "Not knowing what to do, she keeps sucking and struggling to swallow at the same time, choking on the overflow of cum."
        scene ch7sc02_205 with dissolve
        with vpunch
        lu "*Coughs and gasps for air* Hnngh!- Hhaahh- aaahh!"
        mc "You okay? I know it’s a lot to take during your first time."
        lu "*Coughs* Mmh-hm! I’m- Hnngh… good. Just… needed a bit of air."
        mc "Let me see you."
        scene ch7sc02_206 with dissolve
        "She looks up to you, her mouth still full of leftovers from her dessert."
        mc "You can do this, I believe in you Luna."
        mc "Swallow once more and finish off by licking your lips."
        scene ch7sc02_207 with dissolve
        "Hearing that you aren’t disappointed with her but instead encouraging her, she swallows and begins licking her lips."
        scene ch7sc02_208 with dissolve
        $ renpy.pause(0.7)
        scene ch7sc02_207 with dissolve
        $ renpy.pause(0.7)
        scene ch7sc02_208 with dissolve
        $ renpy.pause(0.7)
        scene ch7sc02_207 with dissolve
        $ renpy.pause(0.7)
        mc "Damn… keeping eye contact while you clean yourself off from satisfying me?"
        mc "This may be your first time, but your intuition is on point as always."
        scene ch7sc02_209 with dissolve
        "She finishes off by kissing your tip gently with her soft and warm lips, while keeping her eyes locked with yours."
        mc "Good job… I’m proud of you."
        lu "*Mhwwaahh* Nnnh… sucking you was so much better than I dared hope for."
        scene ch7sc02_202 with dissolve
        lu "*Licks gently* Mmhh… from how the girls describe their men’s cocks… yours is certainly beautiful and big in comparison… and tasty…"
        mc "Luckily for you I’m not like other men."
        scene ch7sc02_201 with dissolve
        lu "*Giggles and licks* No… you’re definitely different."
        scene ch7sc02_202 with dissolve
        mc "As are you… every touch, every embrace, every kiss… even right now, as you're licking me, it tingles in the area of contact."
        mc "You’re different from any other girl I’ve met… and I like it."
        scene ch7sc02_209 with dissolve
        lu "*Kisses tip* I feel it as well, how our magical energies react and interact when we’re together."
        lu "We’re meant to be together… mmmh… I truly believe that."
        mc "As do I. Come up here, I’m getting hungry."
        scene ch7sc02_199 with dissolve
        lu "*Licks and nibbles with lips* Mnnhh… looks like I got all of it. Mmmh…"
        scene ch7sc02_198 with dissolve
        "She begins to ascend your body, caressing you with her wet tongue every inch of the way."
        scene ch7sc02_197 with dissolve
        lu "Mmmh… you’re getting hungry you say?"
        scene ch7sc02_198 with dissolve
        lu "*Licks* But you already had dinner… and dessert? Mmmgh…"
        scene ch7sc02_197 with dissolve
        lu "Who’s being a naughty glutton now? MMmh…"
        scene ch7sc02_198 with dissolve
        mc "Aaahh… I’m powerless to keep my appetite in check when you’re being like this."
        scene ch7sc02_196 with dissolve
        "She stops licking and moves further up, resting her dripping wet pussylips on your shaft, pressing you down."
        lu "*Moans softly* Mmmffhh… is this- Aahh… is this what you want for your 2nd dessert?"
        mc "Mmmh… no, not yet… this is to be our main course, what I want now is…"
        scene ch7sc02_210 with dissolve
        with vpunch
        mc "This!"
        lu "*Squeals softly* {b}Aiiyh!{/b} [mc]! W-What are you doing??"
        mc "I’m going to eat you… thoroughly."
        lu "*Gasps* L-Like this?! Y-You’ll suffocate!"
        lu "I'm- I'm sitting on your face! Nnghh!"
        scene ch7sc02_211 with dissolve
        lu "The girls gossiping never mentioned being eaten by their boyfriends, or anything like this! Sitting… on their face…"
        mc "Sounds like they have boring boyfriends. Just your scent alone is enough to keep me rock hard."
        lu "*Moans softly* R-Really? Mmmh… I feel… I feel your hot breath caressing my lips… aahh… what do I do?"
        mc "Relax your body completely, I’m the one who’s getting a delicious dessert, but you’re the one who’s getting an orgasm."
        lu "*Gasps* [mc]! Y-You mean like before?? When you entered me with your fingers? C-Can you really make me feel like that with your mouth?"
        scene ch7sc02_212 with dissolve
        lu "*Moans softly* Aaiiyh! W-What was that?!"
        scene ch7sc02_211 with dissolve
        mc "My tongue… running through your soaking wet lips. How did that feel?"
        scene ch7sc02_212 with dissolve
        lu "Oh gosh! That felt… oh that felt… like a rush… surging through my body."
        scene ch7sc02_211 with dissolve
        mc "You’ll feel this a lot, and when you’re on the edge, I’m going to push my tongue inside of you, just like my fingers were, okay?"
        scene ch7sc02_212 with dissolve
        lu "*Moans softly* O-Okay! I-I’d like that!"
        mc "Give me your hand. It’ll help keep you stable and relax you as you will undoubtedly tense up when I begin."
        scene ch7sc02_213 with dissolve
        lu "Oh-... this helps! Mmmh… you’re being so sweet."
        mc "A girl only gets to experience her first time once, and you deserve the best."
        mc "Now, as I begin just relax yourself and balance on my hand while you rest onto my mouth."
        mc "Once you get a feel for the rhythm, you can move along with me as I lick, increasing the pleasure even further."
        lu "*Inhales deeply while resting on your face* [mc], please eat me…"
        lu "I want to be treated and experience something the other girls can only dream of."
        scene lu_lewd4 with dissolve
        $ renpy.pause(1, hard=True)
        "Already from the moment she feels your tongue caress her wet pussylips she instinctively begins to move, rubbing herself onto your mouth."
        lu "*Moans* Aahh… [mc]-... this is… you’re so good to me- Aahh…"
        $ renpy.pause()
        mc "*Muffled licking* Mmmh… fuck… your scent is so potent and your taste enhanced by magical residue just like your saliva… mmffhh."
        mc "I could eat you every day for the rest of my life and not get tired of it… mmh."
        lu "*Moans* Oh [mc]! Mmmfh! D-Don’t say such things… I'll tie you to my bed and sit on your face every daayy- Aiiiyh!"
        with vpunch
        "Feeling Luna beginning to quiver and tremble, you start caressing her entrance and begin to penetrate her-"
        "-As you do… her juices overflows into your mouth."
        with vpunch
        lu "{b}*Moans loudly* AaH! Aiiyh- [mc]! Y-YES!! It’s happening! I-I FEEL YOU!! AiiiiyhhH!!{/b}"
        with vpunch
        scene ch7sc02_214 with dissolve
        with vpunch
        "She grasps your hair and keeps you pressed into her juicy and soaking wet pussy as she orgasms directly into your mouth."
        with vpunch
        lu "{b}*Squeals* Aiiiyh-AiiyH!{/b} I’m coming!! I’m coming into your mouth! {b}Aiiiyhhh!!{/b}"
        mct "Mmfhh-mmffh! I knew she was going to love this- Mmh! But damn! She came a lot harder than earlier… I guess I’ve found her weakness."
        scene ch7sc02_213 with dissolve
        lu "[mc]... wow… just wow… *Panting softly* I’ve never thought it possible to feel like this… mmh."
        scene ch7sc02_215 with dissolve
        "She collapses onto you, trying to catch her breath after the intensity of the orgasm she just had."
        scene ch7sc02_216 with dissolve
        lu "*Panting softly* Thank you… for doing that… I didn’t even know this was a thing… and it’s the best thing I’ve ever experienced."
        scene ch7sc02_215 with dissolve
        "While resting on you, she keeps her ass resting on your upper chest and chin while her lips remain gently pressed against yours."
        scene ch7sc02_216 with dissolve
        mc "Mmmh-hmm… you’re welcome… mmfh…"
        scene ch7sc02_215 with dissolve
        lu "Sorry… I’ll move in a moment… just a little while longer- Nnnhh…"
        scene ch7sc02_216 with dissolve
        "While she gathers herself, you take advantage of the position to keep drinking her delicious juices as it flows from her pussy onto your lips."
        scene ch7sc02_215 with dissolve
        lu "[mc]... is this… is this what it's like to have a boyfriend? *Giggles softly*"
        scene ch7sc02_216 with dissolve
        mc "Mhm-hmm… you like the idea of having a boyfriend?"
        scene ch7sc02_215 with dissolve
        lu "Mmmhh… I do… but only if it’s you."
        scene ch7sc02_216 with dissolve
        lu "[mc]... are you? My-... my boyfriend now?"
        mc "Come back up here and I’ll tell you."
        scene ch7sc02_195 with dissolve
        "She eagerly repositions herself on top of you awaiting your answer."
        mc "Yes Luna, I’m your boyfriend."
        lu "That makes me… your girlfriend! *Giggles happily*"
        mc "*Chuckles* It does. And I couldn’t wish for a better woman to be mine. How does that make you feel?"
        lu "It makes me feel… mmmh… it makes me feel like… doing something…"
        lu "Something like…"
        scene ch7sc02_217 with dissolve
        lu "*Moans softly* Aahh- thiiiisss… [mc]- Aahh…."
        mc "*Moans* Aahh… fffuuck… Luna… mmh."
        scene lu_lewd5 with dissolve
        $ renpy.pause(1, hard=True)
        "Hearing you moan with her, she knows you feel just as incredible as she does, she instinctively moves very gently on just your tip."
        mc "Fuck- Luna… mmmh… the way you’re squeezing just my tip right now- Mmmh! Incredible…"
        lu "*Moans softly* Aahh-Ahnnhh… you’re inside me… mmh… you’re really inside me."
        lu "*Moans* We’re one… finally we’re one. Mmmh… I want to make love to you [mc]... I want us to make love all night."
        $ renpy.pause()
        scene lu_lewd6 with dissolve
        $ renpy.pause(1, hard=True)
        "The room fills with wet slushing sounds as she pushes her soaking wet pussy further down onto your cock, getting used to your size."
        $ renpy.pause()
        mc "Fuck… Luna… Mmh… I love not only feeling how wet you are for me but also hearing it… Mmmh! Damn you’re tight!"
        lu "*Moans* Aiiyhh! I-I can’t help it! Mmmh! I’ve only ever had my own fingers inside me! Aiiyh! And they’re small as you know… Mmh!"
        with vpunch
        lu "{b}*Moans loudly* [mc]! OHH!!{/b} I’m going to- AiiiyhHH!! I’m coming agaaaiiiin!! {b}AHH!!{/b}"
        with vpunch
        mc "*Moans* Luna! Nhhgh! Fuck! Me too! You’re too thight- AahhH!"
        scene ch7sc02_218 with dissolve
        with vpunch
        lu "{b}*Squeals* AHH!{/b}! It’s so warm! Mmmh! I feel you inside me! Your cock and your cum! NNngh!"
        mc "Ffucck… you’re incredible… we weren’t even going that deep, but with how wet and tight you are… and our energies combining… mh."
        lu "I know… I wanted to push you deeper… nngh… but it stung a little."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        mc "Yeah… mmmh… it usually hurts a little the first time, for some even the first few."
        play music morning_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch7sc02_219 with dissolve
        lu "*Whimpers softly* You’re worth a little pain… us being together… is worth it."
        lu "I… I didn’t disappoint you then?"
        scene ch7sc02_220 with dissolve
        mc "You’re crazy if you think I experienced anything but complete and pure pleasure."
        scene ch7sc02_219 with dissolve
        lu "I… I love you."
        lu "I’m in love with you… I love you."
        scene ch7sc02_220 with dissolve
        mc "Mmmh… hearing you say it while I’m still inside you, elevates the intimacy of it."
        mc "I love you Luna."
        scene ch7sc02_219 with dissolve
        lu "*Moans softly* Mmmh… you’re right… hearing you say it while your inside of me, makes it feel like so much more than just words."
        scene ch7sc02_221 with dissolve
        lu "*Whispers softly* I love you [mc]. I love you so incredibly much."
        mc "Mmmh… I love you, Luna."
        lu "Kiss me, boyfriend."
        scene ch7sc02_222 with dissolve
        lu "*Whimpers softly* Mmmh-mhh… my whole body ignites when we kiss."
        mc "Mine too… mmmh… especially when you fully lean on me like this… our skin touching all over, and with me inside you…"
        lu "Mmmh… this is our first kiss as boyfriend and girlfriend… mmmh… it feels so intimate."
        scene ch7sc02_221 with dissolve
        lu "I love you."
        mc "I love you."
        scene ch7sc02_222 with dissolve
        lu "Mmgh… I’ve been claimed by a man who makes me feel happy… who values me and inspires me… mmh."
        scene ch7sc02_219 with dissolve
        lu "I’ve never felt this happy [mc], and you’re the entire reason for it. I almost feel guilty for experiencing this joy."
        scene ch7sc02_220 with dissolve
        mc "How so?"
        scene ch7sc02_219 with dissolve
        lu "So many people have less than desirable lives… living with great troubles… and here I am, happy as can be."
        lu "With the man I love."
        scene ch7sc02_220 with dissolve
        mc "You’ve had your fair share of struggles, and don’t ever feel guilty for being happy. It’s something we all strive for."
        mc "You said I inspire you? Well, wield your happiness with pride. And it’ll inspire others to find their own happiness."
        scene ch7sc02_219 with dissolve
        lu "[mc]... that’s actually… really wise. I’ll do that! I’ll be happy and proud of my happiness! *Giggles*"
        scene ch7sc02_221 with dissolve
        lu "In fact… I feel so happy right now… that I have to kiss my boyfriend."
        mc "Well then, don’t keep him waiting…"
        scene ch7sc02_222 with dissolve
        lu "Mmmh… nnghh! *Licks tongue* Mmmh…"
        "Luna caringly caresses your chin while resting her entire body on you, she gently keeps squeezing your cock while the two of you makeout."
        scene black with Dissolve(2.5)
        $ renpy.pause(0.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0


    else:
        scene ch7sc02_153 with dissolve
        mc "*Chuckles* Ready to get out of here? I’m about to pass out after a good meal like this."
        lu "Uh-huh! Could you escort me home?"
        mc "Sure thing."
        scene black with Dissolve(2.5)
        $ renpy.pause(0.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        "You bring Luna to the dormitories entrance and the two of you share a hug before you part ways and you head home to the tavern for the night."

    scene ss12 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_027 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    ec "Sivir, how is everyone from the Arugoh branch settling in so far?"
    siv "My A’nu, it pleases me that this is a concern to you. However it seems everyone has been adjusting fairly well."
    scene ch6sc10_028 with dissolve
    siv "It is a great honor to have been united once again, that you have welcomed us back into your warm embrace."
    ec "Please… think nothing of it. I’m greatly pleased to have our people united again."
    scene ch6sc10_029 with dissolve
    siv "My heart overflows with joy from your kind words, A’nu."
    ec "I understand that you and my sister, Riven. Were each leaders within Arugoh?"
    scene ch6sc10_030 with dissolve
    siv "We were… and I shan’t lie to you. We have clashed on several occasions over our different leadership ideologies."
    siv "I suppose me being set in the old ways, and her youthful determination made for a volatile concoction."
    siv "But none of that matters anymore, now that we have an A’khan, a true A’khan unlike which our ancestors has never seen."
    scene ch6sc10_029 with dissolve
    ec "*Giggles happily* You’re right. I doubt any A’khans of the past can hold a candle to [mc]."
    scene ch6sc10_030 with dissolve
    siv "I truly believe that, and I feel that the goddesses agree with us on the matter. Why else would he be able to meet them? Gain their blessings?"
    siv "He is an extraordinary man… one whom I can’t wait to see again."
    scene ch6sc10_029 with dissolve
    ec "I share your feelings on the matter. And even when he isn’t here, I want you to know…"
    ec "Riven may be my sister, but that does not play a role in my decisions. I want you to feel comfortable enough with me to speak your mind."
    scene ch6sc10_030 with dissolve
    siv "Oh Echo… you have no idea how happy it makes me to hear you say such words."
    siv "You are a reflection of your mother, something you can be proud of."
    scene ch6sc10_031 with dissolve
    mh "Tsk! What is the meaning of this?"
    mh "What is your snake-like tongue whispering into the ears of our A’nu?"
    scene ch6sc10_032 with dissolve
    siv "Marah! What a lovely surprise. *Giggles*"
    siv "I’m surprised you aren’t asleep currently? I thought women of your age-"
    scene ch6sc10_033 with dissolve
    with vpunch
    mh "We’re the same age! Bitch! Tsk!"
    ec "Marah, be nice. Everything has gone well with the merging of our tribes and I wish it to continue to do so."
    scene ch6sc10_034 with dissolve
    mh "Tsk! Fine, I didn’t come here to waste my time on this woman."
    mh "A’nu, we have not had any reports from Kisha and her huntresses in days. I… am concerned."
    scene ch6sc10_032 with dissolve
    ec "Hmm… yes, I too have been awake at night thinking about them. But they are more than equipped to handle this matter."
    siv "Marah’s concern is understandable, after all we dealt with this issue as well when we lived up near Arugoh."
    scene ch6sc10_031 with dissolve
    mh "We should send more huntresses! Whatever is happening up there, it likely is what caused [mc] to shipwreck."
    scene ch6sc10_033 with dissolve
    mh "He-... he is our A’khan, the most powerful man I’ve ever known… if anything could shipwreck him… it has to be powerful."
    scene ch6sc10_034 with dissolve
    mh "A’nu… I don’t think we should take this lightly."
    mh "I’m going to go pray to Gaia to watch over them. Please think on how to proceed."
    scene ch6sc10_027 with dissolve
    ec "Sivir, please… you’ve dealt with this matter for years. What is your opinion."
    siv "Normally I would brush Marah off but she has valid concerns… and we did lose several of our own huntresses as you know."
    ec "Yes, that was the whole reason for this expedition, to gain knowledge and potentially recover them."
    scene ch6sc10_028 with dissolve
    siv "A noble cause, A’nu. One I fear shan’t end well."
    ec "W-Why not? What is happening up north?"
    scene ch6sc10_027 with dissolve
    siv "*Sighs* Even we ourselves aren’t fully understanding it, but I believe what or who it is, doesn’t have good intentions."
    ec "But if someone or several someones was living on Aruna… wouldn’t we know about it?"
    siv "Not necessarily, Aruna is vast as  you well know, and the north has more land mass than the southern part here at A’nai."
    scene ch6sc10_028 with dissolve
    ec "So there could be another tribe further to the north? One… we’ve never encountered before?"
    siv "I can’t say for sure… but that is what I believe. The furthest we’ve managed to scout is the foot of the great fire-mountain, the Volcano."
    siv "We believe they have found a way to survive in the less than hospitable area of the Volcano."
    scene ch6sc10_029 with dissolve
    ec "Sivir, thank you so much for sharing this info with me."
    ec "It will be most useful should I decide on sending another group."
    scene ch6sc10_030 with dissolve
    siv "You are most welcome, I certainly don’t envy your predicament."
    siv "If you send another expedition, we will only have a few good fighters left to defend A’nai… far too few should more outsiders come."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch7sc02_223 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    ro "Tsk… he thinks he can just send a raven and expect me to jump through hoops?!"
    ro "I’ve already risked my neck several times for him and his foolish course!"
    scene ch7sc02_224 with dissolve
    ro "He’s forced me to betray everything I once held dear…"
    ro "I had to… for her. He would’ve killed her."
    scene ch7sc02_225 with dissolve
    ro "Ugh! What a bloody mess you’ve gotten yourself into Rose."
    ro "I need a way out… with what Taron is attempting to do… it won’t end well for anyone associated with him."
    ro "I need to find a way to protect her… only then will I be free from his grasp."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0

    if irene_alive == True:
        scene ss29 with Dissolve(1.5)
        $ renpy.pause()
        scene ss89 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ir146 with Dissolve(1.5)
        play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        uk "Darling? You in here?"
        scene ir147 with dissolve
        ir "He’s our target?"
        vi "Yes, I’ve made sure he’s alone."
        vi "Time for you to do your thing."
        scene ir148 with dissolve
        ir "I thought my first contract was going to be Rin?"
        vi "Your first official contract, this one I’ve cherry picked for you… I need to make certain you have what it takes."
        vi "Killing Rin from a desire of avenging Alana isn’t much of an indicator of how you will handle taking a life."
        scene ir149 with dissolve
        vi "This will ensure you are capable of fulfilling standard contracts going forward and give you a bit of experience."
        vi "You better get to it… we don’t have all night."
        uk "Honey? Where are you? I thought you’d have dinner at the ready upon my return?"
        scene ir150 with dissolve
        uk "Darling? Do I need to get out the belt? You know how it sours my mood…"
        scene ir151 with dissolve
        uk "Where the hell are you!?"
        scene ir152 with dissolve
        with vpunch
        uk "*Groans in agony* Aarghh!!"
        scene ir153 with dissolve
        with vpunch
        uk "Hnnghhh! It stings!!"
        scene ir154 with dissolve
        uk "*Groans* Hrrhh… fuck! I… I can’t feel my left leg!?"
        scene ir155 with dissolve
        ir "Your leg is the last thing you should be worried about at this moment."
        ir "Although I suppose it does sting a little, doesn’t it? I severed your achilles tendon after all."
        scene ir156 with dissolve
        uk "W-What do you want!? Is it money you’re after?"
        uk "I-I’ve got money! I’ll pay you! Please don’t kill me!"
        ir "I’m afraid I’ve already been bought."
        scene ir157 with dissolve
        with vpunch
        uk "*Blood-curdling groan* Hhragghh! HHhgrrrghh!"
        scene ir158 with dissolve
        ir "Pathetic…"
        ir "It’s a good thing your wife wasn’t home to witness you begging for your life like a child."
        scene ir159 with dissolve
        ir "What the hell?"
        ir "You’ve been hiding something back there? Hmm… wait… is that blood seeping through the doorframe?"
        scene ir160 with dissolve
        ir "If anyone’s back here… I’m warning you, I’m not in the mood for surprises… make yourselves known!"
        ir "You want to do it that way? So be it…"
        scene ir161 with dissolve
        with vpunch
        ir "I warned you! *Gasps* W-What!?"
        ir "What the hell is going on!?"
        scene ir162 with dissolve
        ir "Is that… his wife?"
        ir "We were only supposed to eliminate him… Vi-Viperia did this!"
        ir "W-Why!? She wasn’t a part of the contract?"
        scene ir163 with dissolve
        vi "*Scoffs* I’ll tell you why."
        vi "Oh don’t give me that look… we’re assassins, Irene."
        scene ir164 with dissolve
        vi "We don’t leave witnesses… and that’s exactly what his wife would’ve been."
        ir "His… wife? She was innocent!"
        vi "Don’t give me that crap… how many innocents did you hurt while working with Rammus as common thugs?"
        scene ir165 with dissolve
        vi "At least now your killings has purpose."
        vi "Yes, the wife was an innocent bystander tonight, had she been away from home or asleep, she’d been left alive."
        vi "But we don’t take chances with potential witnesses…"
        ir "I… I swore to him I wouldn’t harm innocents if he… let me live."
        scene ir166 with dissolve
        vi "I don’t know what the hell you’re on about, but you didn’t kill her, I did."
        vi "Now get a move on, we’re heading back, you’ve successfully handled your first assassination."
        vi "You’ll get used to it… you often will have to deal with collateral damage during your assassinations."
        ir "..."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    else:
        pass


    if luna_relationship == True:
        scene ss52 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch7sc02_226 with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        mc "*Chuckles* I’m starting to see how you’re breezing through your classes… you have access to quite the book collection."
        mc "How did you get this many? Aren’t they expensive?"
        scene ch7sc02_227 with dissolve
        lu "*Giggles* They are."
        scene ch7sc02_228 with dissolve
        lu "I didn’t buy them, I inherited them from my mother."
        scene ch7sc02_227 with dissolve
        lu "Also most of them aren’t useful for academy studies as they are focused on magic."
        mc "I see, you must’ve learned to read from an early age?"
        scene ch7sc02_228 with dissolve
        lu "Uh-huh, mother started going through books with me when I was around 5 summers."
        lu "By my 7th summer I was practically reading of my own accord."
        scene ch7sc02_226 with dissolve
        mc "Impressive. My parents knew a little as my mother also studied here in Luxenford when she was an active sorceress."
        mc "*Chuckles* She would try to teach me and my father, to little success."
        scene ch7sc02_227 with dissolve
        lu "*Giggles* Poor woman! I can’t imagine having to deal with you as a young little troublemaker!"
        scene ch7sc02_228 with dissolve
        lu "But you can read now? How did you learn?"
        mc "My mentor, when we found refuge in the Sen’ju region, we finally found a place to stay for five years or so."
        mc "It was a small village, only a few occasional traders passed through to export goods to the capital."
        scene ch7sc02_227 with dissolve
        lu "I guess that’s where you did most of your training as well as your studies then?"
        mc "Mhm. I remember it fondly… hopefully I get to visit it some day."
        scene ch7sc02_228 with dissolve
        lu "Is that where you want to take me? When we go?"
        mc "Mhm, there are several areas within the Sen’ju region I’d like to show you, but this village is definitely on the list."
        mc "Nakajima."
        scene ch7sc02_227 with dissolve
        lu "*Giggles* Yay! I look forward to seeing it, after all… it holds a large portion of your life, five years."
        scene ch7sc02_229 with dissolve
        mc "Five hells… I was staring at books this whole time? While you were laying here like this?"
        lu "*Giggles happily* Men! More interested in books than their cute and naked girlfriend!"
        lu "Soooo typical! Tsk, tsk! *Snickers*"
        scene ch7sc02_230 with dissolve
        mc "A mistake that shall soon be corrected."
        mc "I don’t think I’ve ever seen a more beautiful woman before my eyes."
        lu "*Giggles* Oh? Can I hold my own against the Princess?"
        scene ch7sc02_231 with dissolve
        mc "My girlfriend outclasses even the princess."
        lu "*Giggles* I like it when you call me that."
        mc "*Chuckles* You better get used to it, I have no intention of revoking your girlfriend status."
        lu "Good! Cause I don’t offer take backs! Nuh-uh! You’re stuck as my boyfriend forever and ever! *Giggles happily*"
        scene ch7sc02_232 with dissolve
        lu "Think you can handle that? Having to kiss me, take care of me, hug me, make love to me, for the rest of our lives?"
        scene ch7sc02_233 with dissolve
        mc "Handle it? I’m going to embrace it."
        scene ch7sc02_232 with dissolve
        lu "Are you certain… earlier you found out what a…"
        lu "Mouthful I can be. *Giggles*"
        scene ch7sc02_233 with dissolve
        mc "You’re the best mouthful I could desire… so yes, Luna."
        mc "I have no regrets about making you my girlfriend."
        scene ch7sc02_232 with dissolve
        lu "I don’t have any regrets either… none."
        scene ch7sc02_234 with dissolve
        mc "Now, what is my beautiful little witch writing? Are you cooking up a new spell?"
        lu "*Giggles softly* …"
        scene ch7sc02_235 with dissolve
        lu "J-Just! Uhh… *Giggles* a bit of… journaling."
        scene ch7sc02_234 with dissolve
        mc "Oh yeah? Can I read it?"
        scene ch7sc02_235 with dissolve
        lu "Uhhh! Yeah… I guess I don’t mind?"
        lu "B-But I didn’t write it thinking anyone was going to read it."
        scene ch7sc02_236 with dissolve
        lu "P-Promise me you won’t judge me! Only then can you read it!"
        mc "I promise."
        lu "Okay… go on."
        scene ch7sc02_237 with dissolve
        "Luna makes herself comfortable resting on your back."
        lu "Remember! No judgement!"
        mc "This must be good to have you this riled up. *Chuckles*"
        scene ch7sc02_238 with dissolve
        mc "*Reads* I’ve fallen in love with [mc], at first it was just a crush, a warm feeling… but it’s undeniable at this point."
        mc "*Reads* Every time our eyes meet, my heart flutters… when he touches me, my body fills with untamed energy."
        scene ch7sc02_239 with dissolve
        mc "*Reads* I’ve tried several times to tame the energy…"
        mc "*Reads* The only thing that works is when I… touch myself. That’s the only way to release it."
        scene ch7sc02_237 with dissolve
        lu "It’s so embarrassing!"
        mc "It’s not embarrassing, I like it."
        lu "O-Okay… you may continue."
        scene ch7sc02_238 with dissolve
        mc "*Reads* [mc] has finally returned! I can’t wait to see him again! To embrace him!"
        scene ch7sc02_239 with dissolve
        mc "*Reads* I hope he still feels as I do… that he remembers our plans to have a date."
        scene ch7sc02_238 with dissolve
        mc "*Reads* Today’s the day! We’re going on a date! On a daaaate! I’m going on my first date!"
        scene ch7sc02_239 with dissolve
        mc "*Reads* [mc] is going to be here any minute now, should I change?"
        mc "*Reads* Will he like my outfit? I knew I should’ve stayed up and thought this through!"
        scene ch7sc02_237 with dissolve
        lu "Hehehe… I was feeling nervous okay?!"
        mc "I’m not saying anything. *Chuckles* You’re cute."
        scene ch7sc02_238 with dissolve
        mc "*Reads* He touched my breast last night at the tavern… I can’t believe we did that! It was so… naughty… and… exciting!"
        scene ch7sc02_239 with dissolve
        mc "*Reads* We’re finally going to be alone today… the entire day! There’s so much I’d like to do! Where do we even start??"
        scene ch7sc02_238 with dissolve
        mc "*Reads* I shouldn’t confess to him… this is our first date… he’ll think I’m crazy."
        scene ch7sc02_237 with dissolve
        lu "Heheh… yeah… that didn’t go as planned."
        lu "B-But only because you kept kissing me! A-And holding me! How could I not confess when you overload my feelings?!"
        mc "It’s a good thing you did… otherwise you wouldn’t be laying on top of your boyfriend right now. Naked even."
        lu "*Giggles softly* I’m glad I did, I just hadn’t planned for it."
        scene ch7sc02_238 with dissolve
        mc "*Reads* We did it! We became as one! I’ve never felt this incredible before! Not once!"
        scene ch7sc02_239 with dissolve
        mc "*Reads* I fed him my breast, I need to do that again… it was so intimate having him suck my nipple."
        scene ch7sc02_238 with dissolve
        mc "*Reads* And I-... I sucked him as well! And he said he enjoyed it!"
        scene ch7sc02_239 with dissolve
        mc "*Reads* Tomorrow morning I’m going to-"
        scene ch7sc02_240 with dissolve
        with vpunch
        lu "Okaaay! That’s plenty of reading for tonight! You’re not allowed to see anymore!"
        mc "*Reads* I’m going to wake him up by-"
        scene ch7sc02_241 with dissolve
        lu "Nuuuh! Stop you meanie!"
        lu "{b}PUT THE JOURNAL DOWN! OR FACE THE WRATH OF YOUR GIRLFRIEND!!{/b}"
        mc "*Chuckles* Alright, alright! I guess I’ll find out in the morning."
        scene ch7sc02_242 with dissolve
        lu "Exactly! So don’t ruin the surprise by being too curious!"
        lu "A patient boyfriend is a boyfriend who is rewarded. *Giggles*"
        scene ch7sc02_243 with dissolve
        lu "Like this! *Mwah*"
        mct "I love this girl."
        scene ch7sc02_244 with dissolve
        with vpunch
        lu "*Gasps* Aahh!"
        lu "*Giggles happily* A-Again? This soon?!"
        scene ch7sc02_245 with dissolve
        mc "I believe my gorgeous girlfriend asked me earlier to make love to her all night?"
        lu "Aahh… she did… mmh… but-... the girls always mention how their man orgasms and then it’s over?"
        scene ch7sc02_246 with dissolve
        "You push yourself further onto her, pressing your cock against her incredibly sensitive clit."
        lu "*Moans softly* Oh-ohh… Nnhh..."
        lu "I-I think I need to throw out anything I hear from the girls here at the academy… they don’t have a boyfriend like you."
        mc "Exactly… mmh… forget anything you’ve ever heard and just… follow your intuition. You’ll learn everything as we go."
        lu "*Moans* [mc]... I-I trust that you will teach me everything I need to know to satisfy you- Aahh… please, make love to me."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene ch7sc02_247 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        lu "*Gasps* Ohh! Mmmh! Please be gentle with me- Aahh… I’m a little sore from before."
        "You nod at her in agreement while you push your tip between her wet and warm pussylips, they intimately greet you by surrounding you."
        scene lu_lewd7 with dissolve
        $ renpy.pause(1, hard=True)
        lu "*Whimpers* Nnnhh-Nngh! I-... I feel you baby… Mmmmhh… you’re treating me so well."
        "You carefully begin entering her, being fully aware of not going too deep right away."
        "Instead you take your time, letting her get used to you again. Allowing her to feel it all."
        mc "Mmmh… Fuck… you’re so incredibly wet."
        lu "I- Aahh… I hope you like that? Mmmh… I’m powerless to control my juices."
        mc "Mmmh… I love it… my cock is drenched in your warm juices and the way your tight little pussy is squeezing me… mmh."
        $ renpy.pause()
        scene ch7sc02_244 with dissolve
        lu "*Whispers softly* Ohh- Nngh! [mc]... it stings a little but… mmgh… please, go deeper. I want you deeper."
        scene ch7sc02_248 with dissolve
        with vpunch
        lu "*Gasps* Aah! I-I feel you! Oh heavens! Ffffhh… you’re so big…"
        lu "[mc]... make love to me! Aahh…"
        scene lu_lewd8 with dissolve
        $ renpy.pause(1, hard=True)
        lu "*Moans intimately* Ahh-mmh! Baby- Mmmh… I love how you’re spreading my legs and bumping my hips with each thrust- Aahh!"
        $ renpy.pause()
        mc "MMmh… Damn… even being this soaking wet, your pussy is ffhhh tight! I love being this deep inside you Luna."
        with vpunch
        lu "Me-... me too! Ahh! Yes! I can’t believe what I’m feeling- aahh! We’re making love… ahh!"
        with vpunch
        "With each thrust, Luna’s entire body quivers, she’s right at the edge of reaching her orgasm-"
        "Her pussy sucking your cock ensures you’re at the edge with her."
        with vpunch
        lu "{b}*Moans loudly*{/b} Aahh! Y-You’re pulsating! Mmmh! I feel you throbbing while you thrust! Cum with me! [mc]- I need you!"
        scene ch7sc02_248 with dissolve
        with vpunch
        lu "*Whimpers* I’m coming!! {b}Aiiiyhh!!{/b}"
        with vpunch
        mc "AahH! Fuck Luna!"
        scene ch7sc02_249 with dissolve
        "You drop down onto her, catching your breath after another amazing combined orgasm."
        lu "*Panting softly* Mmmh… we’re pretty good at this."
        scene ch7sc02_250 with dissolve
        mc "Yeah… you’re a natural."
        lu "I have the best teacher… mmmh… following my intuition is so natural with you."
        scene ch7sc02_249 with dissolve
        lu "I feel so safe with you… it’s rather easy to just allow my body to do as it desires."
        scene ch7sc02_250 with dissolve
        mc "Mmmh… I love you, Luna."
        scene ch7sc02_249 with dissolve
        lu "*Giggles* I love you too!"
        lu "Thank you… for making me feel so special."
        scene ch7sc02_251 with dissolve
        mc "You are special. I can’t imagine a woman I’d rather have as my girlfriend."
        lu "*Giggles* [mc]! There you go again… making me feel like I’m the only woman in the world."
        lu "*Moans softly* You’re fully emerged inside of me… pressing yourself down onto my sensitive breasts… telling me these lovely things…"
        lu "I need you to kiss me… otherwise I’m going to lose my mind… Mmmh…"
        scene ch7sc02_252 with dissolve
        lu "Mmmh! Nnnh! Nnh-hmm…"
        "You lean into her, resting your arm on her chest pushing her down into the bed while she caresses the back of your hair as your lips merge."
        scene ch7sc02_253 with dissolve
        lu "*Licks intimately* Mmmh… I love you [mc]... I love you so much. Mmmh… I’m yours."
        mc "I love you too… mmmgh… you’re mine."
        scene ch7sc02_252 with dissolve
        "With your hand on her chest, you’re easily able to tell her heart is galloping at full speed like she just sprinted for miles."
        "This girl lying beneath you is clearly and utterly in love with you."
        scene ch7sc02_253 with dissolve
        mct "Mmmh… I love being one with her… she’s beyond incredible."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)


    else:
        pass

    scene ss70 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch5sc08_173 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch5sc08_174 with dissolve
    ld "*Snickers* …"
    ldt "He’s getting close…"
    scene ch5sc08_175 with dissolve
    ld "He should just hurry up and Ascend already!"
    ld "Then I don’t have to sneak around to see him! *Snickers*"
    scene ch5sc08_176 with dissolve
    ld "We’ll all get to meet him officially!"
    ld "Aaah! I haven’t been this excited in over 6.000 years!"
    scene ch5sc08_177 with dissolve
    ld "Should I conjure a bunch of monsters for him to slay? That’ll surely get him to Ascend already!"
    ld "*Snickers* Naah… I better behave! He’ll Ascend soon enough on his own."
    scene ch5sc08_178 with dissolve
    ld "Hmmh?"
    scene ch5sc08_179 with dissolve
    $ renpy.pause(1)
    scene ch5sc08_180 with dissolve
    $ renpy.pause(0.5)
    ld "Maia? Lovely to see you! Mhm-hm!"
    scene ch5sc08_181 with dissolve
    mai "Lucid, we need to talk."
    mai "It’s about [mc]."
    scene ch5sc08_183 with dissolve
    ld "Oh? I’m all ears!"
    scene ch5sc08_186 with dissolve
    ld "You may sit."
    scene ch5sc08_187 with dissolve
    mai "Thank you."
    mai "I apologize for just barging in here… but you’re the only one who I can talk to about this… about him."
    scene ch5sc08_186 with dissolve
    ld "Pish-posh! You may come and go as you like, unless [mc] is visiting me! Then you better stay away! *Snickers*"
    scene ch5sc08_189 with dissolve
    mai "Uh-huh… funny."
    scene ch5sc08_188 with dissolve
    mai "Wait- has he visited you recently?!"
    ld "You can unclench… no, he hasn’t called upon me since I sent him to you for the purification magic."
    scene ch5sc08_190 with dissolve
    mait "Thank goodness…"
    ld "What are you smiling at!"
    scene ch5sc08_191 with dissolve
    mai "N-Nothing!"
    scene ch5sc08_192 with dissolve
    mai "..."
    ld "You wanted to speak about [mc]?"
    ld "What’s going on?"
    scene ch5sc08_193 with dissolve
    mai "Ugh… where do I even begin?"
    mai "Things are so complicated!"
    scene ch5sc08_194 with dissolve
    ld "Hey… little one."
    ld "Tell me what’s going on? You know I’m on your side."

    if soulbinding == True:
        scene ch5sc08_195 with dissolve
        ld "Trust me?"
        "Maia nods. Acknowledging that she trusts Lucid."
        scene ch5sc08_196 with dissolve
        mai "You’ve never given me a reason not to…"
        mai "I… I did something… with [mc]."
        scene ch5sc08_196a with dissolve
        mai "Something… that can’t be undone."
        mai "My sisters and I… we-..."
        mai "We restored my soulbinding with [mc], and we infused it… with the essence of all three of us."
        scene ch5sc08_194 with dissolve
        ld "*Gasps* Maia! You did what?!"
        scene ch5sc08_196 with dissolve
        mai "I know… when Castiel finds out… he’ll kill me."
        scene ch5sc08_194 with dissolve
        ld "A threeway soulbinding has never been done before… what led you to this madness?"
        scene ch5sc08_196a with dissolve
        mai "I couldn’t bear it Lucid! I couldn’t stand not being closer to him… you know how I feel."
        scene ch5sc08_196b with dissolve
        ld "Yes I know how you feel… that is not what surprised me."
        ld "And you’re right… Castiel will absolutely kill you for opposing his will."
        ld "You were wise to come to me with this… you came because you need my help, and that’s what you’ll get."
        scene ch5sc08_196a with dissolve
        mai "Lucid… I can’t ask that of you, I only came because I wanted you to know."
        mai "In case something happens to me… I need you to know so that you can watch over [mc]."
        scene ch5sc08_196b with dissolve
        ld "I told you before, I’m not going to let Castiel harm you."
        ld "For now… this needs to be kept a secret, your renewed soulbinding needs time to mature."
        scene ch5sc08_194 with dissolve
        ld "[mc] is close to his first Ascension. You’ve felt it too, haven’t you?"
        scene ch5sc08_196 with dissolve
        mai "Mmh, I have."
        scene ch5sc08_195 with dissolve
        ld "When he Ascends I believe your soulbinding will be strong enough to withstand Castiel's wrath."
        scene ch5sc08_194 with dissolve
        ld "Now, of course… just because he won’t be able to sunder your soulbinding as he did before…"
        ld "He can still erase you from existence."
        scene ch5sc08_195 with dissolve
        ld "Which is where I come in."
        scene ch5sc08_196 with dissolve
        mai "You’re really going to stand against Castiel? For me?"
        scene ch5sc08_196b with dissolve
        ld "No sweetie. Not for you… for [mc]."
        ld "I told you last time, I believe [mc] needs you. You have a bond with him that nobody else has."
        ld "If I let Castiel kill you… [mc] will become the next Balthazar, I know it."
        scene ch5sc08_196a with dissolve
        mai "You really think I will be enough to prevent that?"
        scene ch5sc08_196b with dissolve
        ld "I do… not just you though, all of the people he has grown to care about."
        ld "You will all play a role in who he becomes."
        scene ch5sc08_195 with dissolve
        ld "But you, little one… you will play the most important role. I truly believe that."
        scene ch5sc08_196 with dissolve
        mai "Lucid… thank you. I-... I’ll do my best for him. I love him."
        scene ch5sc08_194 with dissolve
        ld "I know you do… now, go. Live your life as usual, do your goddess things and act normal."
        ld "Castiel will summon [mc] when he Ascends, at that point he will feel the soulbinding, there won’t be any hiding it."
        scene ch5sc08_195 with dissolve
        ld "But I’ll be there as well. And I’ll make sure he understands what happens if he comes after you in any way."
        scene ch5sc08_196 with dissolve
        mai "Okay… I can’t think of any better solutions. Just promise me… if something happens to me, you will take care of [mc]."
        scene ch5sc08_196b with dissolve
        ld "I promise. But stop thinking like that… I may not be opposing my brother because of you, but I still care for you."
        scene ch5sc08_196a with dissolve
        mai "I know… okay, I’ll take my leave."

    else:
        pass

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss43 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch5sc10_281 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.7)
    cas "I hope my little sweetling is having a grand time today."
    cas "I’ve never seen her show an interest in boys before meeting him."
    scene ch7sc02_254 with dissolve
    cas "She’s been so giddy and excited since his return from his trip."
    cas "She needs someone like him, someone who can show her all life has to offer."
    scene ch7sc02_255 with dissolve
    cas "She’s been so worried about me as of late…"
    cas "I’m the one who’s supposed to worry about her while she goes through life being carefree and happy."
    scene ch7sc02_256 with dissolve
    cas "Taron is going to pay for putting my baby through such hardships."
    with vpunch
    cas "H-How dare he?! She’s just a kid! And yet he has put such a large cloud of darkness into her life!"
    scene ch7sc02_257 with dissolve
    with vpunch
    cas "Once we’ve dealt with this bloody hex and I can do magic again, he’ll wish he hadn’t used my loved ones against me!"
    scene ch7sc02_258 with dissolve
    cas "*Groans in pain* Aahh! My anger must’ve triggered some of my dormant magic which caused the hex to activate."
    cas "I need to calm down! Before it fully activates!"
    scene ch7sc02_259 with dissolve
    cas "Thank goodness… it worked."
    cas "I have to find a way to break this hex… I won’t allow Luna to take on this burden no matter how much she wants to."
    scene ch7sc02_254 with dissolve
    cas "Maybe now that Taron has fled the capital…"
    cas "Maybe… now’s my chance to face Rose and get some answers."
    scene ch7sc02_255 with dissolve
    cas "She hasn’t shown herself to me since I was captured… not once."
    cas "Is she that much of a coward? Or is something else at play here?"
    scene ch7sc02_256 with dissolve
    cas "Is it because she feels guilty? For betraying her closest friend and her niece?"
    cas "She might not be related to Luna, but we always joked about how she was basically her aunt given how close friends we were."
    scene ch5sc10_281 with dissolve
    cas "I just can’t fathom she would betray Luna… she adored Luna, it wasn’t an act… I know it wasn’t!"
    cas "If I face Rose… I could learn what has made her do all of this… maybe even… bring her back to our side."

    if luna_relationship == True:
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        scene ss29 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch7sc02_260 with Dissolve(1.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.7)
        with vpunch
        lu "*Moans* Aiyh! Again!"
        mct "*Chuckles* Naughty little witch… she loves being spanked."
        scene ch7sc02_261 with dissolve
        mc "What a naughty girlfriend I’ve gotten myself… you like having your hair pulled while being spanked."
        lu "*Giggles* D-Do it!"
        scene ch7sc02_260 with dissolve
        with vpunch
        lu "{b}*Squeals*{/b} Aiiyh-Ah! Mmmffhh!"
        scene ch7sc02_261 with dissolve
        lu "I love it!"
        lu "I love how you grab my ponytail firmly like you own me and how you press your hard cock between my firm and bubbly ass cheeks!"
        scene ch7sc02_260 with dissolve
        with vpunch
        lu "*Gasps* AiihhhH! Yes!"
        scene ch7sc02_261 with dissolve
        lu "I love feeling your manly hand slap my ass now that it belongs to you! Mmmfhh! Again! Please!"
        scene ch7sc02_260 with dissolve
        with vpunch
        lu "*Moans* Ahhh! [mc]! I-I need you! I need you to fuck me while we’re standing like this!"
        scene ch7sc02_262 with dissolve
        mc "I’ll never deny you what you desire most… mmmh."
        lu "*Moans* Oh heavens… mmh! I feel your tip teasing my lips… please, fuck me!"
        scene lu_lewd9 with dissolve
        $ renpy.pause(1, hard=True)
        "You give her what she’s craving..."
        "Having had you inside her multiple times tonight, she is more adjusted to your size and you’re able to go deeper."
        $ renpy.pause()
        lu "*Moans* Ahh-mmh! [mc]! Fffuuuhhh you’re deep! Oh! {b}OHH!! MMH!!{/b}"
        lu "*Moans* {b}Aiiiyh!{/b} Fuck me! Fuck your slutty little witch!"
        with vpunch
        mc "Fuck Luna! Mmmh… you’re coming already?! That spanking really turned you on- Mmmh!"
        with vpunch
        lu "{b}*Orgasmic moan* Aaiiyh-ah! AH!{/b} How could I not?! Mmh! You’re pulling my hair and fucking me so deep! AiiiyhhHH!"
        with vpunch
        $ renpy.pause()
        scene lu_lewd10 with dissolve
        $ renpy.pause(1, hard=True)
        mc "Mmgh! Fuck… I love this soaking wet pussy of yours… you’re an amazing little slut for me."
        with vpunch
        lu "*Moans* {b}AHH!{/b} Y-You’re not even giving me a break after that orgasm?! AHH! Yes! Keep fucking me like this!{b} MMH!{/b}"
        with vpunch
        mc "I’m not stopping until this naughty little pussy of yours has been filled with my cum- Mmmfh!"
        with vpunch
        lu "{b}*Squeals* AiiiyhH- [mc]!!{/b} I feel you throbbing! Fill me! MMhgh! Show me how much you love fucking me! {b}AHH!!{/b}"
        with vpunch
        scene ch7sc02_263 with dissolve
        with vpunch
        "Luna’s entire body trembles with pleasure as she can’t stop herself from cumming together with you."
        lu "*Moans* {b}[mc]- AHH!{/b} Heavens!! Mffh!"
        mc "*Chuckles* Looks like we made another mess, little witch."
        lu "*Giggles happily* I love making messes together with you."
        scene ch7sc02_264 with dissolve
        lu "You gave me so much this time… my pussy even forced you out due to being filled with our combined orgasm."
        mc "I couldn’t hold anything back… not with how tight and warm you were… your entire body was hungry for it."
        lu "*Giggles* It certainly was! Hnngh… owh… now that the pleasure is over I can feel we might’ve gone a little too rough this soon."
        scene ch7sc02_265 with dissolve
        lu "I don’t think I can handle anymore of this tonight… please don’t be mad."
        scene ch7sc02_266 with dissolve
        mc "You’re crazy if you think I’d ever be mad at you, especially over this?"
        mc "I’ve enjoyed every moment of our date, especially tonight. You’ve been nothing but incredible."
        scene ch7sc02_265 with dissolve
        lu "G-Good! Me too… so much! You’ve been everything I could dream of and then some."
        lu "Cuddle me until we fall asleep?"
        scene ch7sc02_266 with dissolve
        mc "C’mon my cute little witch… you’ve earned an all-night cuddle."
        scene ch7sc02_267 with dissolve
        lu "Yay! *Giggles softly*"
        lu "I definitely put in the work! And now I’m getting cuddled by my boyfriend!"
        scene ch7sc02_268 with dissolve
        mc "No funny-business though. Cuddle and sleep little witch. We’ve already gone a little overboard for your first time."
        mc "Your body needs to recover."
        scene ch7sc02_267 with dissolve
        lu "Buuh! Fine! No funny business… just an intimate cuddle and rest."
        scene ch7sc02_268 with dissolve
        mc "Get this bubbly little ass of yours into bed before I throw you in myself. *Chuckles*"
        scene ch7sc02_267 with dissolve
        lu "Uh-huh! Let’s goooo!"
        scene black with Dissolve(1.5)
        "Luna wipes herself off with a wet cloth and the two of you snuggle up beneath the covers."
        scene ch7sc02_269 with Dissolve(1.5)
        lu "*Whispers softly* I love you."
        mc "Mmh… I love you."
        lu "*Whispers softly* Thank you… for making me the happiest girl in the world."
        scene ch7sc02_270 with dissolve
        mc "Likewise… *Inhales* Mmmh…"
        lu "*Giggles softly* Are you going to smell my hair and caress my breast all night?"
        mc "Mh-hm."
        lu "Good… I like it when you do stuff like this… goodnight [mc]."
        mc "Goodnight Luna. *Kisses back of hair*"
        lu "*Giggles softly* …"
        scene ch7sc02_269 with dissolve
        $ luna_trust += 10
        "Luna has fallen in love with you, her trust has increased by {size=+3}{b}{color=#2bff8b}10{/color}{/b}{/size}."
        "The two of you keep caressing each other until both of you eventually drift off into the night."
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)


    else:
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)


    scene ch4sc17_001 with Dissolve(2.5)
    $ renpy.pause()
    scene ch7sc02_271 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "A quest huh?"
    mc "Do I really have to wear all this armor though?"
    scene ch7sc02_272 with dissolve
    el "Yes! We’re going looking for missing adventurers! Most likely something bad happened to them."
    el "Besides, you inherited this armor from Dalen! For questing and adventuring!"
    scene ch7sc02_271 with dissolve
    mc "Alright, alright… I’ll use it."
    scene ch7sc02_272 with dissolve
    el "*Giggles* Don’t fuss, you look rather handsome all suited up for work."
    scene ch7sc02_273 with dissolve
    el "Look over there on the shelves."
    scene ch7sc02_274 with dissolve
    mc "Hmm? The knight’s badge and the horn we found in the goblin ruins?"
    el "Exactly! I remember how excited I was when we found them after having dealt with the goblins."
    scene ch7sc02_275 with dissolve
    el "I remember how accomplished and proud I felt, that we had managed to complete an actual challenging quest."
    el "And we… we haven’t been on a quest together since! That is outrageous if you ask me!"
    scene ch7sc02_276 with dissolve
    mc "Mmh, you’re right… it’s about time we take on another, together."
    mc "I remember being quite impressed with you back then, you took out several goblins as a human."
    scene ch7sc02_275 with dissolve
    el "I had a very… thorough teacher. *Snickers*"
    scene ch7sc02_276 with dissolve
    mc "*Chuckles* I had to make sure you could hold your own."
    mc "So, what do we know about this quest?"
    scene ch7sc02_277 with dissolve
    el "While you were away, a small group of adventurers from out of town stopped by and picked up a quest."
    el "It wasn’t supposed to take more than 1-2 days… but it’s been weeks and nobody’s heard from them."
    scene ch7sc02_278 with dissolve
    el "They don’t get paid if they don’t return upon completion, so I doubt they would just have abandoned the quest on the fly."
    el "Something bad has happened to them… I can feel it."
    scene ch7sc02_271 with dissolve
    mc "Hey… don’t worry."
    mc "We’ll figure out what happened to them."
    scene ch7sc02_272 with dissolve
    el "I believe they were supposed to help a village, Loboten, that had been plagued by bandits in the area."
    el "Apparantly the bandits extort the locals living away from the city under the guise of ‘protection fees’"
    scene ch7sc02_278 with dissolve
    el "*Sighs* Knowing what I know about bandits from our own experiences… I hope the adventurers didn’t clash with such filth."
    el "They’re just as bad as goblins!"
    scene ch7sc02_276 with dissolve
    mc "C’mon, let’s get out there and see what we can find-"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch7sc02_279 with dissolve
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    el "Huh? Who… she’s… beautiful."
    mct "I had a feeling she would be arriving today."
    scene ch7sc02_280 with dissolve
    el "Woah… she has quite the aura… she looks important."
    mc "She is."
    scene ch7sc02_281 with dissolve
    el "Y-You know her?"
    mc "Mhm… remember how I told you about King Bennen’s Lord Admiral?"
    scene ch7sc02_282 with dissolve
    el "*Gasps* That’s her?! You forgot to mention how gorgeous she is!"
    mc "*Chuckles* My bad? Is her attractiveness something important to mention?"
    el "Yes!"
    scene ch7sc02_283 with dissolve
    "You and Diana lock eyes as she approaches."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    #"{color=#00ff00}End of v0.6.2 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    #"{color=#00ff00}End of v0.6.2 {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    scene black with dissolve
    $ renpy.pause(0.1)
    stop music fadeout 1.0
    #jump endofversion
    jump ch7sc4

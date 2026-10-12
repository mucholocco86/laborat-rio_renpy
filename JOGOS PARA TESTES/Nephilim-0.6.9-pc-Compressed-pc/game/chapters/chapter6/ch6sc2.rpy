label ch6sc2:

    window hide dissolve
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (1.0)
    $ renpy.pause(0.5)
    scene ch5sc13_260 with Dissolve(1.5)
    $ renpy.pause(2)
    scene ch5sc13_261 with Dissolve(1.5)
    $ renpy.pause(2)
    #scene ch5sc13_263 with dissolve
    #$ renpy.pause(2)
    scene ch6sc02_001 with Dissolve(1.5)
    $ renpy.pause(0.5)
    br "Blasted boot! Get on, will ye!"
    with vpunch
    $ renpy.pause(0.5)
    scene ch6sc02_002 with dissolve
    el "Morning, Borri! What are you cursing about so early in the day?"
    scene ch6sc02_003 with dissolve
    br "These darned tailors and artisans in Luxenford don’t make proper dwarven attire!"
    br "Me ol' boots gave out last week. Been struggling with these ever since! Egh!"
    scene ch6sc02_004 with dissolve
    el "I never really gave it much thought, but yeah ... dwarves would probably need specially made clothes."
    br "Aye. And since we’re few and far between here in t'capital, demand fer such is low."
    br "Now, what brings a lass like yerself here at t'crack o'dawn?"
    scene ch6sc02_005 with dissolve
    el "*Giggles* Heh-heh-heh!"
    br "Nay, lass, nay! I know yer up t'somethin', and I’m telling ye, {b}NAY!{/b}"
    scene ch6sc02_006 with dissolve
    el "Shopping!"
    el "We’re going shopping!"
    scene ch6sc02_007
    with vpunch
    br "Nay!! Abso-friggin-lutely not!"
    br "Ye better get it out of yer noggin!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_008 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    br "*Groans* Brrah! T' things ye make me do, lass. Not even me wife would have succeeded!"
    br "So... what’re ye looking fer... shoes? ... dresses?"
    scene ch6sc02_009 with dissolve
    el "Neither. I'm not cruel enough to bring you shopping for that. No, we're here to get..."
    el "Tools!"
    scene ch6sc02_010 with dissolve
    br "T-Tools?! By Drusilda’s hammer... yer serious?!"
    br "HAH! Why didn’t ye blasted say so from t' get-go!"
    scene ch6sc02_011 with dissolve
    el "Because it amuses me when you get all grumpy! *Giggles*"
    scene ch6sc02_012 with dissolve
    br "Bah! Yer gonna be t' reason me ol' heart gives out one of these days."
    scene ch6sc02_013 with dissolve
    el "Pish-Posh! You have at least another 100 - 150 years left in you, from what I know about dwarves!"
    el "And if you dare die before that... I’ll kill you myself!"
    scene ch6sc02_014 with dissolve
    br "*Chuckles* Heh... I’ve said it before, and I’ll say it again, lass... ye have t' heart of a dwarven woman!"
    br "So... what are we buying tools fer?"
    scene ch6sc02_015 with dissolve
    el "[mc] and I just finished transporting building materials to our home site, but something came up with the pirates he knows."
    el "It sounded like they were in trouble, so he’s taking care of that for a while."
    scene ch6sc02_016 with dissolve
    el "So, instead of the materials just laying about in the elements, I thought we’d get some tools and start working!"
    br "*Chuckles* Heh! And what makes ye think I know anything about building?"
    scene ch6sc02_009 with dissolve
    el "You’re a dwarf! I've heard male dwarves are typically in charge of construction, while the women forge tools, armor and weapons."
    scene ch6sc02_008 with dissolve
    br "Blasted books... be telling too much! *Exhales*"
    br "*Exhales* Alright, lass. We both know arguing with ye is futile... let’s see what tools we can find."
    scene ch6sc02_014 with dissolve
    el "That’s the spirit! C’mon, it’ll be fun!"
    br "Beats shopping fer clothes... let’s get to it, lass."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_017 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}Mhm...{/i}"
    scene ch6sc02_018 with dissolve
    mct "{i}Despite the small bed... that wasn’t a bad sleep...{/i}"
    mct "{i}Looks like the sun is starting to rise.{/i}"
    scene ch6sc02_019 with dissolve
    mct "{i}Hmm... Pearl’s up already?{/i}"
    mct "{i}Let's go see what she's up to.{/i}"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_020 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_021 with dissolve
    mc "There you are. Morning."
    scene ch6sc02_022 with dissolve
    pl "Here I am. Morning!"
    scene ch6sc02_021 with dissolve
    mc "You always up this early or was the bed too uncomfortable?"
    scene ch6sc02_022 with dissolve
    pl "The bed was... comfortable."
    pl "I’m just used to rising early. Kira likes to sleep in, and someone has to steer the ship, so I usually take the morning shift."

    if pearl_relationship == True:
        scene ch6sc02_022 with dissolve
        pl "How about you? Did you... you know, sleep well?"
        scene ch6sc02_021 with dissolve
        mc "Yeah. I slept like a baby... sharing a bed with you gave me peace."
        scene ch6sc02_022 with dissolve
        pl "G-Good... me too... I’ve never slept so soundly. The sun was already up when I awoke, which is never the case."
        scene ch6sc02_021 with dissolve
        mc "How do you feel?"
        scene ch6sc01_314 with dissolve
        mc "You’re not feeling any pain?"
        scene ch6sc01_316 with dissolve
        mc "You’re not..."
        scene ch6sc01_317 with dissolve
        mc "Feeling sore this morning?"
        pl "*Whimpers* Mnfhh... j-just a little. But it’s okay."
        pl "It was... Mmhm... worth it."
        scene ch6sc01_318 with dissolve
        mc "Yeah? There are no regrets on your part?"
        scene ch6sc01_317 with dissolve
        pl "N-No... Mmffhh... none."
        scene ch6sc01_318 with dissolve
        pl "What about you? Was I... enough?"
        scene ch6sc01_317 with dissolve
        mc "Mm. You were more than enough... no regrets here."
        scene ch6sc01_319 with dissolve
        pl "G-Good... [mc] I..."
        scene ch6sc01_320 with dissolve
        pl "I really enjoyed last night..."
        scene ch6sc01_321 with dissolve
        pl "..."
        scene ch6sc01_322 with dissolve
        mc "You’re worried about Kira?"
        pl "*Nods*"
        scene ch6sc01_323 with dissolve
        pl "We’ve talked about it at length since we parted ways with you."
        pl "We both have feelings for you..."
        scene ch6sc01_322 with dissolve
        mc "I knew Kira felt that way... but you do as well?"
        pl "*Nods* Mh..."
        scene ch6sc01_323 with dissolve
        pl "Do you really think last night would’ve happened if I wasn’t in lov- if I didn’t care about you?"
        scene ch6sc01_321 with dissolve
        mc "No... last night was real, our feelings were real... our bodies conveyed that perfectly."
        scene ch6sc01_322 with dissolve
        mc "So, you know full well that I feel the same."
        scene ch6sc01_323 with dissolve
        pl "Kira and I agreed that if you picked either one of us we would accept it and be happy."
        pl "And if... if you have feelings for both of us, then... we’ll accept that as well."
        scene ch6sc01_322 with dissolve
        mc "Really? You’d be okay with that? There wouldn’t be any jealousy?"
        scene ch6sc01_323 with dissolve
        pl "No. We'd just ask that you don’t get overly affectionate in front of the other. So as not to rub it in their face."
        pl "Apart from that, we’re twins, we’ve been together our whole lives... we want the best for each other."
        scene ch6sc01_322 with dissolve
        pl "..."
        scene ch6sc01_323 with dissolve
        pl "And if both of our hearts point to you, then how could we fault each other for that?"
        scene ch6sc01_321 with dissolve
        mc "Pearl... that’s awfully mature of the two of you. I know that it’s common for a man to have multiple partners."
        mc "But sisters are a different prospect... twins no less."
        scene ch6sc01_322 with dissolve
        mc "Look at me."
        if twins == True:
            scene ch6sc01_322 with dissolve
            mc "I want both of you. You’ve both shown me loyalty and your genuine selves."
            scene ch6sc01_331 with dissolve
            mc "I’m attracted to both of you and my feelings for each of you grow every moment we’re together."
            scene ch6sc01_330 with dissolve
            pl "[mc]... you have no idea what a relief this is. This way, we’ll all get to be happy!"
            pl "Both of us will get to be with you and know real happiness."

        else:
            scene ch6sc01_331 with dissolve
            mc "Pearl... I only want you."
            mc "Kira is great, but I only see her as a friend... unlike you."
            scene ch6sc01_330 with dissolve
            pl "[mc]... you have no idea what a relief that is. I feel so... so happy!"
            pl "I was willing to share you with Kira at the expense of my own happiness, but now I won't have to!"

        scene ch6sc01_330 with dissolve
        pl "I’m glad we got that out of the way..."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc01_320 with dissolve
        pl "Now I can do this!"
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch6sc01_326 with dissolve
        pl "*Mwaah* Mnnnhmm-MMm..."
        scene ch6sc01_328 with dissolve
        $ renpy.pause(1)
        scene ch6sc01_326 with dissolve
        $ renpy.pause(1)
        scene ch6sc01_328 with dissolve
        $ renpy.pause(1)
        scene ch6sc01_329 with dissolve
        pl "*Sensual* I want to taste you... Mmm..."
        scene ch6sc01_331 with dissolve
        mc "Go on then, you little sea-minx. Have your breakfast, I’ll steer the ship."
        scene ch6sc01_319 with dissolve
        pl "Do try not to steer us off course... *Snickers*"
        scene ch6sc02_023 with dissolve
        pl "I'd intended to taste you last night..."
        pl "But I completely passed out after you claimed me... I was so overwhelmed with joy."
        scene ch6sc02_024 with dissolve
        mc "Yeah... I passed out with you."
        pl "Mhm... You’re hard already."
        scene ch6sc02_025 with dissolve
        mc "Well, the idea of you getting on your knees and taking me in your mouth is stimulating..."
        scene pl_lewd7 with dissolve
        $ renpy.pause()
        pl "*Mwah* Mhmm... w-wait... *Sucks* Why does it taste slightly of Bluekelp?"
        mc "*Moans* Mnhmm... I was inside you all of last night... Ahhh... we haven't bathed since."
        pl "*Giggles* R-Right! Mhmm... so good... *Sucks gently*"
        pl "Do you like it when I *Lick* make out with your cock? Mhmm *Suck*"
        scene pl_lewd8 with dissolve
        $ renpy.pause()
        "She doesn’t wait for your answer, instead she pushes you deeper inside her warm, wet mouth."
        "The now familiar softness of her tongue teases your tip as she lubricates your shaft with her saliva."
        mc "*Moans* Pearl... Mmhm- Fuck... that’s good."
        pl "*Sucks harder* Mhmm!! So delicious! Ammh... [mc] I- I can’t stop... I want your cum!"
        with vpunch
        mc "*Moans* F-Fuck! Ahhh! K-Keep sucking like that and you'll get a mouthful - Ahhh!"
        with vpunch
        scene ch6sc02_026 with dissolve
        "Hearing you’re on the edge, she tightens her lips around you and her tongue eagerly rubs your tip."
        scene ch6sc02_027
        with vpunch
        "Her naughty little tongue sends you flying straight over the edge, and you fill her tight mouth."
        with vpunch
        scene ch6sc02_028 with dissolve
        "Pearl’s cheeks balloon outward as you send load after load to the back of her throat."
        "Her lack of experience tells as the unexpected volume surprises her, and she struggles to contain it all."
        scene ch6sc02_029 with dissolve
        mc "Fuck... Mhmm... take your time... I know it’s a lot."
        pl "*Suck* ... *Swallows* ... *Suck*  ..."
        scene ch6sc02_030 with dissolve
        pl "Aaahh ..."
        mc "Five hells, woman ... you look incredible with your mouth filled with my cum."
        scene ch6sc02_031 with dissolve
        pl "Mmhmm... *Licks* So good..."
        pl "You almost choked me with all that cum..."
        scene ch6sc02_032 with dissolve
        mc "My bad... I forgot all about it being your first time, I should’ve warned you."
        pl "Mhm... sounds like I’ll have to practice more... regularly."
        mc "*Chuckles* I like the sound of that. Go on, show me your tongue."
        scene ch6sc02_033 with dissolve
        pl "Aaaaahh..."
        mc "Good girl... you managed to get it all."
        scene ch6sc01_331 with dissolve
        "A proud smile appears on Pearl’s cute little face."
        pl "*Giggles softly* heheheh!"
        scene ch6sc01_330 with dissolve
        pl "I..."
        pl "I really want to kiss you... but if you'd rather wait a bit, I'll understand."
        ####Choice####
        menu:
            "Kiss your woman.":
                scene ch6sc01_331 with dissolve
                mc "Are you kidding? Come here."
                $ pearl_trust += 3
                "Pearl loves that you are man enough to show her affection after what she just did. Trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                scene ch6sc01_329 with dissolve
                pl "*Gasps* Oh! Mmmh!"
                scene ch6sc01_328 with dissolve
                pl "*Mwaah* Mhm... I really liked making out with your cock... but I do prefer your lips! *Kiss*"
                mc "You’re an amazing kisser... your lips are perfectly soft and silky smooth."
                scene ch6sc01_328 with dissolve
                pl "MMmnghh... I think it’s because I snack on Bluekelp often. It’s a popular ingredient in skin creams for women to keep their skin soft."
                scene ch6sc01_329 with dissolve
                mc "Mmhm... I wonder what else you've got up your sleeves?"
                pl "*Mwah* You’ll just have to keep me close and find out! *Kiss*"
                scene ch6sc01_330 with dissolve
                pl "Pheew... thank you. After doing what we just did... I really wanted to be close to you."
                scene ch6sc01_331 with dissolve
                mc "Me too. Now, you'd better turn around and steer."
                mc "I’m not sure I kept a straight course during all that excitement..."
                scene ch6sc01_330 with dissolve
                pl "*Snickers softly* I'd be surprised if you did!"


            "Wait a while.":
                scene ch6sc01_331 with dissolve
                mc "I prefer it if we wait."
                scene ch6sc01_330 with dissolve
                pl "Okay, sure!"
                $ pearl_trust -= 3
                "Pearl is a little disappointed you didn't show her affection, her trust has decreased by {size=+3}{b}{color=#f00}3{/color}{/b}{/size}."



    else:
        scene black with Dissolve(1)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)

    scene ch6sc02_022 with Dissolve(1)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    pl "Based on what I know about this area, we're approaching Aruna Island. Look, you can see it on the horizon."
    scene ch6sc02_021 with dissolve
    mc "You been to Aruna before?"
    scene ch6sc02_022 with dissolve
    pl "I haven’t set foot on the island itself, but we have sailed past Aruna and Maroh islands a few times over the years."
    scene ch6sc02_021 with dissolve
    mc "Maroh?"
    scene ch6sc02_022 with dissolve
    pl "Mhm. Sibling island of Aruna. Both of them are decently large, and each has their own tribe inhabiting them."
    pl "Aruna is home to a females-only tribe, while Maroh is the opposite and inhabited only by men."
    scene ch6sc02_034 with dissolve
    mc "Ahh. I see... from what Diana told me, the ambassador we’re looking for should have shipwrecked near Aruna."
    scene ch6sc02_035 with dissolve
    pl "Let’s hope they’re alright then. Neither Aruna or Maroh are known for their friendly reputations."
    pl "Sailors tend to give both islands a wide birth. They're known to take prisoners from vessels that get too close, or that go ashore."
    scene ch6sc02_034 with dissolve
    mc "Hopefully that’s just sailors' tales. I really don’t feel like playing prisoner again so soon."
    scene ch6sc02_035 with dissolve
    pl "What do you mean?"
    scene ch6sc02_034 with dissolve
    mc "I was imprisoned in the dungeons of the royal palace not too long ago."
    scene ch6sc02_036
    with vpunch
    pl "[mc]! *Gasps* What happened?"
    scene ch6sc02_037 with dissolve
    mc "I was set up by the man who killed my parents, Taron. He had more pull within the court than I realized."
    scene ch6sc02_036 with dissolve
    pl "Don’t tell me he got away with that shit?"
    scene ch6sc02_037 with dissolve
    mc "He did... for now."
    mc "But he'll get what's coming to him. I'll make sure of that."
    mc "I only spent one night in the dungeon, and the issue was resolved quickly. Still... I’d prefer to avoid cells for a while."
    scene ch6sc02_038
    with vpunch
    pl "If they try anything funny, I’ll stick 'em with the pointy end!"
    mc "*Chuckles* Heh... good to know you have my back."
    scene ch6sc02_039 with dissolve
    pl "Always!"
    scene ch6sc02_040
    with vpunch
    pl "{b}*Squeals*{/b} Auuahhh!!"
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    scene ch6sc02_041
    with vpunch
    pl "What?! There aren't supposed to be any rocks or reefs this far out from the island!"
    pl "What's going on?"
    scene ch6sc02_042 with dissolve
    "You notice something on the shore."
    mc "There’s someone on the beach casting a spell. This is probably how they got the ambassador's ship too."
    mc "They must be intentionally shipwrecking any ships who get too close."
    scene ch6sc02_043 with dissolve
    pl "Oh no! The rocks have penetrated the ship's hull, we won't be going anywhere..."
    mc "Great... at least we’re at our destination."
    scene ch6sc02_044 with dissolve
    pl "We’ll have to swim ashore."
    pl "I’ll grab my bikini. You see if there’s anything useful we might need."
    scene black with Dissolve(1)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_045 with Dissolve(1)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}*Sighs* Better prepare for a swim...{/i}"
    scene ch6sc02_046 with dissolve
    mct "{i}We’ll have to swim a little ways around. I don’t want whoever shipwrecked us to notice us coming.{/i}"
    mct "{i}Whoever it is, they're clearly adept at earth magic if they can conjure and control magic from that distance.{/i}"
    mct "{i}That’s no easy feat. I can’t even control my wind magic at that distance yet.{/i}"
    scene ch6sc02_047 with dissolve
    mc "Hmh? How long have you been standing there?"
    scene ch6sc02_048 with dissolve
    pl "*Giggles softly* ..."
    pl "Not nearly long enough..."
    scene pl_ani1 with dissolve
    $ renpy.pause(9.5, hard=True)
    scene ch6sc02_049
    pl "..."
    scene ch6sc02_050 with dissolve
    pl "What? ... Am I wearing too much?"
    scene ch6sc02_051 with dissolve
    mc "I know we’re swimming ashore, but is that really practical?"
    mc "We don’t know what we’re up against yet... or whether they’re hostile or not. Although, based on our ship... I’d say hostile."
    scene ch6sc02_052 with dissolve
    pl "What do you mean it isn’t practical? It’s very aquadynamic... I swim like a fish in this!"
    pl "And it serves a dual purpose. If there are hostile men on the island, they’ll be distracted and I can slice them without any effort."
    mc "Didn't you tell me earlier that it's a females-only island?"
    pl "From what I've been told, yes. But things change over time. And since we haven't been there ourselves, we can't know for sure."
    scene ch6sc02_053 with dissolve
    pl "Besides..."
    pl "What is there to worry about?"
    scene ch6sc02_054 with dissolve
    pl "I’ll be with you..."
    scene ch6sc02_055 with dissolve
    pl "My strong..."
    scene ch6sc02_054 with dissolve
    pl "Fearless..."
    scene ch6sc02_055 with dissolve
    pl "*Giggles* And handsome protector."
    scene ch6sc02_054 with dissolve
    pl "I may just have to get captured on purpose... so you’ll come and rescue me."
    scene ch6sc02_055 with dissolve
    pl "The things I’d let my rescuer do to me... *Giggles sensually* Downright illegal."
    scene ch6sc02_056
    with vpunch
    pl "Hiyyahh! *Snickers* Let’s go say hi to the locals!"
    scene ch6sc02_057 with dissolve
    mc "*Chuckles* You’re crazy... fine, let’s see if they've prepared us a welcoming party."
    pl "Yay! Take me on an adventure! *Giggles* I hope we’ll find new fishys!"
    scene ch6sc02_058 with dissolve
    mc "You really love your fishys, huh?"
    pl "Mh-Hm! They’re cute!"
    scene ch6sc02_059 with dissolve
    pl "And -"
    scene ch6sc02_060 with dissolve
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    pl "..."
    mct "{i}From excited to silent in a moment... there’s more to her love for fish than she’s letting on.{/i}"
    scene ch6sc02_061
    play music chill_2 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    mc "*Shouting* C’mon, let’s go find you some new fishys to befriend!"
    pl "*Laughs* H-Hey! Wait up!"
    scene ch6sc02_062 with dissolve
    $ renpy.pause()
    "Pearl doesn't hesitate to jump in after you."
    scene ch6sc02_063 with dissolve
    $ renpy.pause()
    mct "{i}She glides through the water so effortlessly... she must really love it.{/i}"
    mct "{i}I can understand why. Swimming must give her a feeling of freedom, in a way. Freedom from the tyranny of her father...{/i}"
    scene ch6sc02_064 with dissolve
    "The two of you stay submerged until you’re closing in on the beach."
    "Pearl’s breath control must be close to the limits of peak human conditioning."
    scene ch6sc02_065 with dissolve
    $ renpy.pause()
    scene ch6sc02_063 with dissolve
    $ renpy.pause()
    scene ch6sc02_066 with dissolve
    $ renpy.pause()
    mct "{i}She looks happy... Good.{/i}"
    scene ch6sc02_067 with dissolve
    mct "{i}It’s nice to see her being carefree and relaxed.{/i}"
    mct "{i}After living her entire life oppressed by her father’s rule, she can finally enjoy herself.{/i}"
    scene ch6sc02_068 with dissolve
    "Pearl effortlessly lets herself glide upwards to break the surface and take a gulp of air."
    scene ch6sc02_069 with dissolve
    $ renpy.pause()
    scene ch6sc02_070 with dissolve
    $ renpy.pause()
    scene ch6sc02_071 with dissolve
    $ renpy.pause()
    scene ch6sc02_072 with dissolve
    $ renpy.pause()
    scene ch6sc02_073 with dissolve
    $ renpy.pause()
    scene ch6sc02_074 with dissolve
    $ renpy.pause()
    pl "..."
    scene ch6sc02_075 with dissolve
    $ renpy.pause()
    mc "..."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_076 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "*Chuckles* You realize we’re stranded on an island with inhabitants whose intentions are unknown?"
    pl "Mmm-Hmm."
    mc "And that whoever attacked us could still be looking for us?"
    scene ch6sc02_077 with dissolve
    pl "The sun feels too good after a swim like that to worry about such things."
    pl "Relax with me... at least until my hair dries, please?"
    scene ch6sc02_076 with dissolve
    mc "*Sighs* ... fine. But only until your hair is dry."
    scene ch6sc02_078 with dissolve
    mct "{i}I can’t remember the last time I was at a beach and actually sat down.{/i}"
    mct "{i}I've been so consumed with revenge for the last few years of my life... I've rarely enjoyed anything.{/i}"
    mct "{i}Only small moments with Rin... and then Eliza. Both managed to bring me out of my shell of darkness.{/i}"
    scene ch6sc02_079 with dissolve
    pl "Doesn’t this feel great? The scent of the ocean, the seagulls in the distance, the warm sand..."
    scene ch6sc02_080 with dissolve
    mc "Yeah... I can’t deny that. I was just trying to recall the last time I did something like this."
    mc "But I can’t remember. The closest would probably be times when I've gone swimming with Eliza. But that was only in lakes."
    scene ch6sc02_079 with dissolve
    pl "She’s a lucky girl."
    pl "You may not have been to sandy beaches with her, but at least she gets a lot of time with you."
    scene ch6sc02_080 with dissolve
    mc "*Chuckles* Are you saying you want to spend more time with me too?"
    scene ch6sc02_079 with dissolve
    pl "Maaybe... *Giggles*"
    pl "I suppose you’re not the worst company in the world!"
    ####Choice####
    menu:
        "Did you just tease your Captain? ({color=#ffee54}Leadership{/color})":
            scene ch6sc02_080 with dissolve
            mc "Teasing your Captain?"
            mc "*Chuckles* Maybe I should write you up for a spanking."
            pl "*Snickers* ..."
            scene ch6sc02_079 with dissolve
            pl "Maybe you should!"
            pl "If you spank me hard enough I might even squeal your name, Captain."
            scene ch6sc02_080 with dissolve
            mc "Oh you'll be squealing alright..."
            $ leadership += 1
            "Pearl enjoys the idea of being spanked by her Captain, your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch6sc02_078 with dissolve
            bth "*Chuckles* ... *Giggles* ..."

        "Tell me more... ({color=#87e1fa}Charisma{/color})":
            scene ch6sc02_080 with dissolve
            mc "Not the worst company in the world? Do tell."
            pl "*Snickers* ..."
            scene ch6sc02_079 with dissolve
            pl "Maaaybe I like spending time with you! Mmh-hm!"
            pl "Especially when it's just the two of us, like this... you're embracing it."
            scene ch6sc02_080 with dissolve
            mc "I guess it's easy to embrace being out here when the company is great."
            pl "*Giggles happily* ..."
            scene ch6sc02_079 with dissolve
            pl "Careful, a girl might think you're trying to charm her..."
            scene ch6sc02_080 with dissolve
            mc "*Chuckles* I don't know where she'd get such an idea..."
            pl "*Giggles* Mh-hmmm!"
            $ charisma += 1
            "Pearl enjoys the friendly banter between the two of you, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch6sc02_078 with dissolve
            bth "*Chuckles* ... *Giggles* ..."




    scene ch6sc02_081 with dissolve
    pl "Speaking of Eliza..."
    pl "did you manage to help her? With that artifact thingy."
    scene ch6sc02_082 with dissolve
    mc "Mhm. I did. It turned into a whole mess, but she’s fine now. Actually, better than fine."
    scene ch6sc02_079 with dissolve
    pl "I’m glad. I look forward to meeting her!"
    pl "She must be quite amazing if you care for her so deeply."
    scene ch6sc02_080 with dissolve
    mc "I have a feeling you two will hit it off. She’s carefree and adventurous like you, eager to experience things."
    mc "And she’s also quite stubborn, like your sister. And if you get on her bad side, her temperament matches Kira’s too."
    pl "*Giggles softly*"
    scene ch6sc02_079 with dissolve
    pl "I hope I can befriend her. She sounds great!"
    pl "If she likes fishys, we can go swimming together!"
    scene ch6sc02_080 with dissolve
    mc "She does love swimming, so you've already got that in common."
    mc "Eliza is easy to get along with, she’s basically befriending the whole capital..."
    scene ch6sc02_081 with dissolve
    pl "You also seem different this time. Like you’re less... weighed down?"
    pl "Last time, when we went to Inmortui, you seemed to carry the weight of your entire world on your shoulders."
    pl "Knowing that the person you care about the most was depending on you."
    scene ch6sc02_082 with dissolve
    mc "Yeah... I suppose I’m able to relax a little more now, knowing that she is alright."
    scene ch6sc02_079 with dissolve
    pl "Speaking of relaxing, I’m going to take a nap! Watch over me?"
    scene ch6sc02_080 with dissolve
    mc "*Sighs* Fine... but only for a bit."
    pl "Mmmh-Hmmm!"
    scene black with Dissolve(2)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "An hour later ..."
    scene ch6sc02_083 with Dissolve(2)
    $ renpy.pause()
    scene ch6sc02_084 with dissolve
    pl "Mhmmm..."
    mc "Pearl... it’s time to wake up. You’ve been out for an hour."
    scene ch6sc02_085 with dissolve
    pl "*Mumbles* N-No... Mhm... [mc] is being mean to me!"
    pl "*Mumbles* Kira... stab him! Mhmm..."
    scene ch6sc02_086 with dissolve
    pl "*Mumbles* N-No don’t! mhm- Just kiddinghh..."
    scene ch6sc02_085 with dissolve
    pl "Nnghh... I like him a lot... no stabby-stabby."
    scene ch6sc02_086 with dissolve
    pl "Nhhoo... I like him most, mmh... not you, me! ... Definitely me."
    mct "{i}Five hells...{/i}"
    scene ch6sc02_087 with dissolve
    mc "*Pokes* Hey... Pearl? Wake up... no more asking Kira to stab me."
    pl "Mhmm... [mc]?"
    scene ch6sc02_088 with dissolve
    pl "*Yawns* Wheew, Hnnnghh! That was a great nap."
    mc "*Chuckles* Yeah, I bet... you were out cold for an hour."
    scene ch6sc02_089 with dissolve
    pl "Looks like my hair is all dry too. *Stretches* Let’s go! We’ve got a whole island to explore."
    pl "This is no time for dilly-dallying! *Giggles*"
    scene ch6sc02_090
    with vpunch
    pl "*Laughs* C’mon! Adventure waits for no one!"
    mc "Says the one who got to nap comfortably for an hour!"
    scene ch6sc02_091 with dissolve
    "She shoots you a cheeky smile as she bolts down the beach."
    scene ch6sc02_092 with dissolve
    pl "Look! There’s a path over here!"
    mct "{i}Where does this girl get all her energy...?{/i}"
    scene ch6sc02_093 with dissolve
    mct "{i}Although, it’s nice to see her happy like this. She’s much like Eliza when it comes to being easily excited.{/i}"
    mct "{i}When they get all riled up, nothing will stand in their way... *Chuckles*{/i}"
    scene ch6sc02_094 with dissolve
    pl "C’mon, you turtle! I bet we’ll find something awesome up here!"
    mc "Who are you calling a turtle?"
    scene ch6sc02_095 with dissolve
    mc "I ran across the Cerulean seas in a matter of hours to get to you and Kira."
    mc "A trip which took us a week by ship..."
    pl "*Giggles* Good! Then you shouldn’t have any trouble keeping up!"
    scene ch6sc02_096 with dissolve
    $ renpy.pause()
    mc "*Exhales* Right..."
    mc "Keep an eye out for edibles, we don’t know how long we’ll be here."
    pl "Aye-aiiy! Captain!"
    scene ch6sc02_097 with dissolve
    pl "I can’t believe Kira and I have never landed here before. It’s so tropical and relaxing."
    pl "I wish she could be here and experience this too. She’d be grumpy at first, but I know she would love it."
    scene ch6sc02_098 with dissolve
    mc "I know what you mean... she was quite grumpy when she accompanied me on Inmortui."
    mc "But she loosened up after a while. It was nice seeing a different side to her."
    pl "Mhm. She takes a while to open up... but when she does, she’s a total goop!"
    scene ch6sc02_099 with dissolve
    mc "*Chuckles* A goop?"
    pl "A goopy-goop!"
    pl "A biiiig romantic who wants all the sweet things that she pretends she doesn’t care about."
    scene ch6sc02_100 with dissolve
    pl "She’s spent her entire life worrying about me. And I, her."
    pl "We never had the time or freedom to stop and decide what we wanted for our own lives."
    pl "Not until... you."
    scene ch6sc02_098 with dissolve
    mc "Me?"
    pl "Mhm-Hm. You! You came out of nowhere and removed the dark cloud looming over both our lives... our father."
    scene ch6sc02_097 with dissolve
    pl "You’ve helped Kira open up and be more honest about her feelings."
    pl "She doesn’t hide her emotions out of shame or fear anymore."
    scene ch6sc02_099 with dissolve
    mc "What about you?"
    pl "..."
    pl "I..."
    scene ch6sc02_100 with dissolve
    pl "Hear that? I think there’s running water up here!"
    pl "Let's check it out!"
    scene ch6sc02_101 with dissolve
    mct "{i}*Sighs* ... I’m going to get her to open up one of these days.{/i}"
    pl "Come! Water means potential fishys!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_102 with Dissolve(1.5)
    $ renpy.pause(1)
    pl "It definitely came from up here... Hmh."
    scene ch6sc02_103 with dissolve
    pl "There! [mc], look!"
    pl "Woah!"
    scene ch6sc02_104 with dissolve
    pl "Look at the flowers! They’re huge!! And the water is so clear!"
    pl "It’ll be nice to wash off the salt water!"
    scene ch6sc02_105 with dissolve
    mc "Damn... that does look nice."
    scene ch6sc02_106 with dissolve
    mc "Like a second beach, but inland- not on the coast."
    scene ch6sc02_107 with dissolve
    pl "It’s like a mini freshwater beach! Seas be good!"
    pl "I bet the water feels so good!"
    scene ch6sc02_108 with dissolve
    pl "C’mon! Let’s get cleaned up!"
    mc "*Sighs* ... just as she dries off, she wants to get wet again. A mermaid. She has to be a mermaid..."
    scene ch6sc02_109 with dissolve
    pl "Mhm! The water feels amazing! It’s nice and cool compared to the ocean."
    pl "*Giggles lightly* I'm living a dream!"
    scene ch6sc02_110 with dissolve
    pl "Are you comin- Ohh!!"
    pl "Y-You’re getting naked..."
    mc "Yeah. I’m not getting my pants wet again if we have to walk around exploring afterwards."
    scene ch6sc02_111 with dissolve
    pl "R-Right! Luckily, I don’t mind! *Giggles*"
    pl "Not one bit..."
    scene ch6sc02_112 with dissolve
    mc "*Undresses* I bet you don’t."
    pl "*Bites lip* ..."
    scene ch6sc02_113 with dissolve
    mc "Pearl...?"
    mc "Hellooo... anybody home in that cute noggin of yours, little miss mermaid?"
    scene ch6sc02_114 with dissolve
    pl "H-Huh? I was just... taking in the view!"
    pl "Yeah, totally... just the view! Mmh-hm."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_115
    play music happy_1 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    pl "{b}*Squeals* Aiiyyhh!!{/b} H-Hey!! *Giggles* Ohh! You’re so gonna get it!"
    with vpunch
    mc "*Laughs* Just making sure you’re nice and wet!"
    pl "*Laughs* Okay, Okay! Cease the splashing! *Giggles*"
    scene ch6sc02_116 with dissolve
    mc "You were right, this is great... *Chuckles*"
    scene ch6sc02_117
    with vpunch
    pl "Never take your eyes off your target! Hiiyyah!"
    with vpunch
    pl "*Snickers* How do you like it?!"
    scene ch6sc02_118 with dissolve
    pl "*Dancing* You'd better submit to your Mermaid Queen!"
    scene ch6sc02_119 with dissolve
    pl "*Snickers confidently* I rule these waters!"
    scene ch6sc02_120 with dissolve
    pl "You’re nothing but a fish swimming in my ocean!"
    scene ch6sc02_118 with dissolve
    pl "That’s right! A little sharky-shark thinking he can get me! *Giggles*"
    scene ch6sc02_119 with dissolve
    pl "*Dancing* You'd better submit to your Mermaid Queen! I rule these waters!"
    scene ch6sc02_120 with dissolve
    pl "*Sings* You’re nothing but a fish in my ocean! A little fishy-fish!"
    scene ch6sc02_118 with dissolve
    pl "*Sings* A little sharky-shark thinking he can get me! *Giggles*"
    scene pl_ani3 with dissolve
    $ renpy.pause()
    mc "*Laughs* Oh yeah?"
    pl "*Giggles* All the seas knows it Mr. Shark! The Mermaid Queen rules over all life in the ocean!"
    pl "*Snickers* And as my loyal subject, you will submit to my will!"
    mct "*Chuckles* Dancing victoriously? Too soon, Pearl... too soon."
    pl "*Giggling* Who’s the greatest in the water?! Mee! Nobody can defeat me in my element!"
    scene ch6sc02_120 with dissolve
    mc "Didn’t you just tell me not to take my eyes off my target?"
    pl "W-Wha-"
    scene ch6sc02_121
    with vpunch
    pl "{b}*Squeals* Aiiiiiiiyhh!!{/b}"
    pl "*Laughs* Noooo! My-My victory was within reach!"
    pl "*Nervous giggle* What’ll you do with the Mermaid Queen now that you've caught her, Mr. Sharky?"

    if pearl_relationship == True:
        scene ch6sc02_124 with dissolve
        pl "Y-You wouldn’t eat your Queen... *Giggles* R-Right?"
        mc "Now, there’s an intriguing thought. I’ve felt my appetite growing ever since we jumped off the ship."
        scene ch6sc02_125 with dissolve
        "As Pearl feels your hard cock pressing against her, she firmly presses back into you, holding your cock prisoner."
        pl "Your appetite has been growing, you say? I think something else has been growing as well!"
        pl "Mhmm... could that be... because you’ve been enjoying the sight of my peachy all day?"
        mc "I think that may have something to do with it."
        scene ch6sc02_124 with dissolve
        pl "Nnghh... I did choose this bikini for you..."
        mc "Mhm... you seem to know my taste well then."
        #play music summon_3 fadein 1.0
        stop music fadeout 2.0
        $ renpy.pause(1)
        scene ch6sc02_126 with dissolve
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        pl "Mhm... I do. Which is why I know you’ll enjoy this."
        "Pearl leads your hand to her supple breast, which molds itself perfectly to the grasp of your hand."
        pl "*Moans softly* Ohh... Sharky... you’re being naughty... Mmhmm."
        scene ch6sc02_127 with dissolve
        mc "Mhmm... you’re one to talk. I've heard that mermaids lure men into the water to eat them."
        pl "*Giggles* Mnnghh... now that you mention it... I am getting the urge to put something in my mouth."
        "Pearl turns around and slowly moves down your body until she reaches her destination."
        scene ch6sc02_128 with dissolve
        pl "This thing has been poking me ever since you caught me... Mhmm..."
        mc "*Moans* Ahhh... Sorry, not sorry?"
        pl "I know you like my mouth. This time I won't go easy on you, I'll suck you dry- Mmmh."
        scene pl_lewd9 with Dissolve(1.5)
        $ renpy.pause()
        pl "Ghhnghh... Mhmm... *Suck* Hghhh... I’ll make you apologize... *Suck* Grghh..."
        mc "*Moans* F-Fuck... Mhm... twice in one day? Mmmm... your mouth is incredible, Pearl."
        with vpunch
        pl "*Sucks harder* Nnghh! Mmnghh! I love the taste of your cock! Mmhm!!"
        mc "F-Fuck! Pearl... AHhh! Y-You’re sucking the life out of me! Mmmh!"
        "She keeps her pace steady as she takes you deep, with her tongue rubbing your tip and shaft and covering you with her warm saliva."
        with vpunch
        mc "Fuck... that’s good! Mmhm- I’m! I’m going to cum- AHhh!"
        scene ch6sc02_129
        with vpunch
        pl "{b}*Muffled gagging* MNMngHH!! GHhGHh!!{/b}"
        scene ch6sc02_130
        with vpunch
        "And just like earlier, your intense orgasm shoots load after load, into her mouth and throat."
        "Doing her best to swallow, it’s still too much for Pearl to handle and some of your warm cum spills out."
        scene ch6sc02_131 with dissolve
        "You feel her gently running her tongue around your tip and attempting to swallow what’s left."
        mct "{i}Mmm... she may be inexperienced, but damn... her tongue and eagerness certainly make up for it.{/i}"
        scene ch6sc02_132 with dissolve
        mct "{i}Mmhm... She’s not in a rush to get away either... She really enjoys having me in her mouth.{/i}"
        scene ch6sc02_131 with dissolve
        $ renpy.pause(1)
        scene ch6sc02_132 with dissolve
        $ renpy.pause(1)
        pl "*Sucks tenderly* Nnghh... so ghood... *Licks* MmMm..."
        scene ch6sc02_133 with dissolve
        mc "Guess we found out mermaids really do eat men... Mhmm..."
        pl "*Giggles softly* This mermaid only has an appetite for you."
        mc "Get up. I want to taste your peach."
        scene ch6sc02_121 with dissolve
        pl "Oohh... Mhm... I like it when you get handsy with me."
        scene ch6sc02_134
        with vpunch
        pl "*Moans* Aahh!!"
        scene ch6sc02_135 with dissolve
        pl "So eager... Mmhm!"
        scene ch6sc02_134 with dissolve
        pl "You want my peach that badly? MMmm..."
        scene ch6sc02_135 with dissolve
        mc "Ever since tasting you last night..."
        scene ch6sc02_134 with dissolve
        mc "I’ve had a hunger for more."
        scene ch6sc02_135 with dissolve
        pl "Seas... you really know how to get me riled up... MMffh!"
        pl "My peachy is only for you... Nnghh... so have it as much as you want-"
        scene ch6sc02_136
        with vpunch
        pl "{b}*Moans* Aiiiyhh-AHhH!! Oh! [mc] ...{/b}"
        scene pl_lewd10 with dissolve
        $ renpy.pause()
        "As you dive between her plump cheeks, you’re met with a citrusy scent and taste as your tongue moves between her lips."
        pl "*Moans* Oohhh... OOh!! Mffhh - Yes! Taste me-Ahhh!"
        mc "*Muffled* Mmf... you’re absolutely delicious, even without the Bluekelp... *Licks*"
        pl "*Moans* I-I didn’t think to put any on today- Ahhh! It would’ve been washed away by the ocean dive... MMhmm!"
        mc "*Muffled licking* Mmfhh... you don’t need it. *Licks* Your pussy tastes perfect and very... unique."
        scene pl_lewd11 with dissolve
        $ renpy.pause()
        "Pearl struggles to contain her excitement. She gently grabs the back of your hair and keeps you pressed between her cheeks."
        with vpunch
        pl "*Moans* Aiiyhh... Mhmm... citrus... like you sai- said last night? MMhppfhh!"
        pl "Maybe it's because I love all the exotic fruits that are imported to Looter’s Bay?"
        pl "{b}*Moans loudly* Aiiyh-Aiiiiiyh!{/b} Y-Yes! Seas, your tongue is so amazing! Ahh!! I’m- [mc]!! I’m!!!"
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        scene ch6sc02_137 with dissolve
        "With Pearl's moans filling the air, she orgasms with your tongue still inside her, forcing her juices to flow directly to your mouth."
        mc "*Muffled* Mmhpphh... delicious."
        scene ch6sc02_138 with dissolve
        pl "*Heavy breathing* Hnngh-Hnaahh... I’m out of breath... and I was just standing still..."
        mc "*Muffled* MMhfhh..."
        scene ch6sc02_139 with dissolve
        pl "*Panting softly* Ohh... sorry! ... can’t have you suffocating down there! *Giggles*"
        mc "*Panting* Death by Pearl's peachy... I’ll accept my fate."
        scene ch6sc02_138 with dissolve
        pl "At least we’d know you’d go straight to the high-heavens! *Giggles*"
        scene ch6sc02_137 with dissolve
        pl "I love how much you enjoy my taste... it's quite the confidence boost."
        scene ch6sc02_136 with dissolve
        $ renpy.pause(1)
        scene ch6sc02_135 with dissolve
        $ renpy.pause(1)
        scene ch6sc02_134 with dissolve
        $ renpy.pause(1)
        mc "*Sighs* See you soon, little peachy."
        scene ch6sc02_121 with dissolve
        $ renpy.pause(1)
        pl "*Giggles* Such a gentleman. Don’t worry, my peachy needs constant care and attention... from {b}you{/b}."
        scene ch6sc02_124 with dissolve
        mc "Is that so? *Chuckles* I’ll have to remember that."
        pl "*Giggles* You'd better! Otherwise your mermaid will be very... upset."
        scene ch6sc02_126 with dissolve
        pl "*Moans softly* And you wouldn’t want that... would you?"
        mc "No... I’d do anything to keep her happy... and satisfied."
        scene ch6sc02_127 with dissolve
        pl "*Moans* OOohh... I’m feeling very satisfied right now... Mmhmm!"
        pl "I love feeling your warm, strong hands on my body."
        pl "*Belly rumble*..."
        scene ch6sc02_114 with dissolve
        pl "Why don’t you... go see if there’s anything we can eat?"
        pl "With the way you’re making me feel... we’re going to need a lot of energy tonight..."
        scene ch6sc02_113 with dissolve
        mc "*Chuckles* Yeah, I have a feeling we will. I’ll have a look around."
        scene ch6sc02_111 with dissolve
        pl "Great! But please don’t go too far..."
        scene ch6sc02_110 with dissolve
        mc "*Ties pants* Scared of being on your own?"
        pl "N-No... but I prefer your company!"

    else:
        scene ch6sc02_123
        with vpunch
        mc "This!"
        with vpunch
        pl "{b}*Screams* Auuuaahh!!{/b}"
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch6sc02_118 with Dissolve(1)
        pl "*Giggles* That was fun!"
        mc "Hey, I’m going to go forage for some food. Will you be okay here?"
        scene ch6sc02_111 with dissolve
        pl "Of course! I’m perfectly capable of handling myself."
        scene ch6sc02_110 with dissolve
        mc "*Ties* Great, I'll see what I can find."

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_140 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mct "{i}Hhm... there don’t appear to be any berry bushes. And I don't see any fruits on these flowery plants.{/i}"
    scene ch6sc02_118 with dissolve
    mct "{i}I guess I could go a little deeper inland... Pearl’s busy doing... well, Pearl things.{/i}"
    pl "*Dancing and singing*"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_141 with Dissolve(1.5)
    $ renpy.pause(1)
    "You make your way from the beach into the thick jungle that borders it."
    scene ch6sc02_142 with dissolve
    mct "{i}The vegetation here is quite a bit denser than beside the beach. And despite the pathways at the beach -{/i}"
    mct "{i}There don’t seem to be any paths in here. But if people live in the area, shouldn't there be some paths?{/i}"
    scene ch6sc02_143 with dissolve
    mct "{i}Berries... Hmm, they look similar to black currants but their scent is slightly different. Sweeter and more aromatic.{/i}"
    mct "{i}Probably not as exotic as the fruits Pearl is used to. But if they’re like black currants, they’ll be fine.{/i}"
    scene ch6sc02_144 with dissolve
    mct "{i}I wonder what they are? ... Their scent is really quite strong: sweet, but with a hint of bitterness as well.{/i}"
    mct "{i}Hmh, I'll grab a few handfuls. Won’t be the most filling meal, but it’ll do for one night.{/i}"
    scene ch6sc02_145 with dissolve
    mct "{i}I'd better get back to the beach before she realizes I’ve ventured off into the jungle.{/i}"
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_146 with Dissolve(1.5)
    play music dark_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(2)
    scene ch6sc02_147 with Dissolve(1.5)
    $ renpy.pause(1)
    uk "..."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_148 with Dissolve(1.5)
    $ renpy.pause(2)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_149 with Dissolve(1.5)
    $ renpy.pause(2)
    scene ch6sc02_150 with Dissolve(1.5)
    $ renpy.pause(1)
    mc "Taking in the view?"
    scene ch6sc02_151 with dissolve
    pl "You’re back! Mmhm, look-look! Isn’t it beautiful?"
    mc "Mh. It sure is."
    pl "Come... sit with me?"
    scene ch6sc02_152 with dissolve
    pl "Did you find any yummies while you were in the jungle?"
    scene ch6sc02_153 with dissolve
    mc "*Chuckles* Noticed that, did you?"
    scene ch6sc02_152 with dissolve
    pl "Yes! And I’ll punish you for it later."
    scene ch6sc02_154 with dissolve
    mc "Don’t be too harsh on me, here... I found these for us to eat."
    pl "Black currants? Yum! ... no, can’t be. They’re too large to be black currants."
    scene ch6sc02_153 with dissolve
    mc "Yeah, that’s what I thought at first too. But their scent is different, sweet with a hint of spiciness."
    scene ch6sc02_155 with dissolve
    pl "I want some! Aaaahh..."
    mc "*Sighs* ... really?"
    pl "{b}Aaaaaahhh...{/b}"
    scene ch6sc02_156 with dissolve
    mc "..."
    pl "Mmfhhfh... Yhum-yhum!"

    if pearl_relationship == True:
        scene pl_lewd12 with dissolve
        $ renpy.pause()
        pl "*Moans softly* Mmfhh... Nnfgghh *Suck* Aaannnhhhh."
        mct "{i}She nibbled the berry, and now she's sucking the juices from it and sucking my fingers at the same time...{/i}"
        mc "That good, huh?"
        pl "*Licks* Mmffhh... Soo good! *Licks* The spicy aftertaste actually hits soooo good!"
        scene pl_lewd13 with dissolve
        $ renpy.pause()
        pl "More! Mmhm!"
        "You place another berry in her mouth, and she eagerly nibbles it and sucks the juices once more."
        pl "MMnnfhhh! *Licks* Your fingers- Mmhm... taste like the berries now! *Suck*"
        mct "{i}Fuck... this actually feels good...{/i}"
        scene ch6sc02_154 with dissolve
        pl "Mnh! Let’s eat them all! *Giggles*"
        mc "*Chuckles* Sure, dig in... I brought plenty."

    else:
        scene ch6sc02_152 with dissolve
        pl "Delicious! The spicy aftertaste actually hits soooo good!"

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_157 with Dissolve(1.5)
    $ renpy.pause(1)
    pl "Mhhfh... I didn’t think I’d get so full just from berries! We actually ate them all..."
    scene pl_ani4 with dissolve
    $ renpy.pause(2)
    mc "Yeah, they were quite filling. But then again, some of them were the size of a small apple."
    pl "[mc]... I... thank you for finding us food."
    mc "You don’t have to thank me. I didn’t come all that way to save you, only to let you starve to death."
    pl "*Giggles* True! Still... I’m not used to- well, this. So thank you."
    mc "You’re most welcome, my little mermaid."
    pl "Your little mermaid, huh?"
    pl "I like that. *Laughs softly*"
    pl "Then you’re my sharky-shark!"
    mc "*Chuckles* Sharky-shark?"
    pl "Mhm! Cause you’re cute and deadly! Just like sharks! *Giggles*"
    mc "I don’t think I’ve ever heard anyone call sharks cute before."
    pl "They’re just misunderstood..."
    mc "Like you."
    pl "Mhm. *nods*"
    mc "Is that why you like fish so much? You relate to them in some way?"
    pl "I guess... mostly I’m just curious about them. And spending years at sea..."
    pl "... you go a little crazy if you don’t find something to entertain yourself."
    mc "I bet... but I want to know more about you. Why are fish so important to you?"
    pl "You’re not going to let this go, are you?"
    mc "No. But if you aren’t ready to talk about it yet, then I’ll relent for now."
    pl "*Sighs* No. I do want to tell you... I trust you. It’s just... I don’t even talk to Kira about this stuff."
    mc "You can with me, though. Trust me enough to open up to me... like I trusted you with my past."
    pl "Mhm. *Nods* Okay."
    scene ch6sc02_157 with dissolve
    pl "My love for fishys has its roots all the way back in my childhood... When Mother was still alive."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch4sc12_022 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    pl "Father always had a temper, but Mother was able to mellow him out."
    scene ch6sc02_158 with dissolve
    pl "Whenever he got upset with me and Kira for playing around, he'd scold us and make us feel like we weren’t good enough."
    pl "But she'd scold him right back and put him in his place."
    scene ch6sc02_159 with dissolve
    pl "He even threatened to send us away on a ship..."
    pl "Never to see him or Mother again."
    scene ch6sc02_160 with dissolve
    pl "Whenever he scolded us, Mother would always be there to comfort us..."
    pl "She always knew what we needed... and despite being twins, she knew how different we are."
    scene ch6sc02_161 with Dissolve(1.5)
    $ renpy.pause(1)
    pl "She'd take Kira to train swordplay."
    pl "Kira had a lot of aggression and it helped her vent her frustrations."
    scene ch6sc02_162 with dissolve
    pl "I wasn’t as filled with anger."
    pl "At least, not so obviously. I just got quiet instead."
    scene ch6sc02_163 with dissolve
    $ renpy.pause(1)
    pl "Kira inherited Mother’s beautiful crimson hair."
    pl "And her willful determination."
    scene ch6sc02_164 with dissolve
    pl "While I..."
    pl "I inherited her beautiful sapphire eyes and her curiosity for life."
    scene ch6sc02_165 with dissolve
    pl "She could tell I wasn’t as diverted by swordplay..."
    scene ch6sc02_166 with dissolve
    pl "So, instead of drilling me in that, she knew I needed something different."
    scene ch6sc02_167 with dissolve
    pl "She came up with the idea of going with me down to the docks to count the fishys."
    pl "One little fishy, two little fishy... she would say it out loud and I’d join in."
    pl "She would sit with me for hours, never complaining or being too busy."
    scene ch6sc02_168 with dissolve
    pl "Eventually, we also started keeping track of the colors and sizes too. And soon it sparked something inside me."
    pl "My curiosity became my outlet from Father's harassment."
    scene ch6sc02_169 with dissolve
    pl "Everyone thought I was weird... ‘Silent, pretty Pearl. Rather spend time with the fishes than us’ people would say."
    pl "Which only reinforced that preference. Fishys were much better company than most people."
    scene ch6sc02_170 with dissolve
    pl "Fishys didn’t judge me, they never yelled at me or threatened me... they'd just swarm around me."
    pl "Looking at me with the same curiosity that I had for them."
    pl "Sometimes they'd even nibble gently at my feet, which really tickled!"
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_171 with Dissolve(1)
    $ renpy.pause(1)
    pl "Then one day... Mother fell sick. Nobody could find a cure... and within a fortnight she was..."
    scene ch6sc02_172 with dissolve
    pl "Gone."
    scene ch6sc02_173 with dissolve
    pl "Our only beacon of light, snuffed out."
    scene ch6sc02_174 with dissolve
    pl "Father wouldn’t even let us say goodbye to her... just... ‘We already burned her body, scurry off!’"
    pl "After the only good part of our lives was gone, you can imagine how Father spiraled..."
    scene ch6sc02_175 with dissolve
    with vpunch
    pl "Getting worse and worse... his aggression increased over time. Kira would shield me from it by putting herself in the line of fire."
    pl "And we found ways to spend more and more time away from Looter’s Bay."
    scene black with Dissolve(1)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_157 with Dissolve(1)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    pl "When we were at sea, Father wasn’t around. We were... almost free."
    scene pl_ani4 with dissolve
    $ renpy.pause(1)
    pl "So that’s where my enthusiasm for fishys comes from. It's the only thing I have left of her."
    mct "{i}Damn, they really didn’t have it easy... even as young kids.{/i}"
    mct "{i}I thought their father was only that vile in his later years... but it seems like he was always a horror.{/i}"
    mc "Pearl... I appreciate you sharing that with me. Opening up about your childhood, your Mother, like that..."
    mc "That can’t have been easy for you... so, thank you."
    pl "I'm glad I told you."
    scene ch6sc02_157 with dissolve
    mc "Come here."
    scene ch6sc02_176 with dissolve
    pl "*Exhales deeply* Honestly? I’m glad you were so persistent. It feels good to have shared that with someone... with you."
    pl "At least I’m a little less... alone, now? That’s how it feels."
    scene ch6sc02_177 with dissolve
    mc "Mhm. You’re not on your own anymore. I’m here for you whenever you need me."
    scene ch6sc02_176 with dissolve
    pl "*Giggles softly* Thank you, Sharky..."

    if pearl_relationship == True:
        scene ch6sc02_176
        pl "You know what I could really use right now?"
        scene ch6sc02_177 with dissolve
        mc "What?"
        scene ch6sc02_176 with dissolve
        pl "A kiss from my sharky!"
        scene ch6sc02_178 with dissolve
        mc "Come here- Mmmh..."
        pl "Mhmmm..."
        scene ch6sc02_179 with dissolve
        "Pearl leans back into you, tilting her head. You lean in to meet her, and your lips come together in a soft embrace."
        scene ch6sc02_178 with dissolve
        "Her tongue tenderly invites yours to play, your spit mixes with hers as your tongues entwine."
        scene ch6sc02_179 with dissolve
        pl "*Kiss* Mnghh... I can’t get enough of you and your sweetness... *Licks*"
        scene ch6sc02_178 with dissolve
        mc "Likewise... Mhmm..."
        scene ch6sc02_179 with dissolve
        pl "You make me- Mmhmm... so happy. *Licks* Happiness I haven’t felt since Mother was alive...*Kiss*"
        pl "You... you're my new light."
        scene ch6sc02_178 with dissolve
        mc "Mmhm... you deserve to be happy. *Kiss* I love seeing that beautiful smile of yours."
        scene ch6sc02_180 with dissolve
        pl "[mc]... so... *Licks* Ti-Tired... Mhmmm... Zzz..."
        mc "Y-Yeah... Mhmm... feeling sleepy..."
        "The two of you fade away together, lips locked and everything."
        scene black with Dissolve(2.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)

    else:
        scene ch6sc02_176 with dissolve
        pl "*Yawns* Hnngh... I’m feeling sleepy... and the sun isn’t even down yet."
        scene ch6sc02_177 with dissolve
        mc "Yeah... me too... I suppose we did have an adventurous day..."
        scene ch6sc02_176 with dissolve
        pl "Just... a little nappy-nap... Mhmm..."
        scene ch6sc02_177 with dissolve
        mc "Y-Yeah... ZzZz..."
        scene black with Dissolve(2.5)
        "The two of you doze off rather quickly..."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)

    scene ch6sc02_181 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    el "Pheew! That’s what I call a day's work! Good job everyone!"
    el "I'm surprised we managed all this in a day."
    scene ch6sc02_182 with dissolve
    al "I still can’t believe you and [mc] own this land... and this is just the center of it?"
    el "Correct! When we were here the first time, we explored a good portion of it. It’s pretty vast."
    scene ch6sc02_183 with dissolve
    fy "You guys could run your own village out here! There’s so much land... a blacksmith's workshop-"
    fy "A farm or two, a tavern, a couple houses, maybe a mill."
    scene ch6sc02_182 with dissolve
    al "Uh! And a bakery! Maybe even a herbalist's hut for medicine and such."
    scene ch6sc02_184 with dissolve
    br "Aye! And a lumber mill fer wood production! Mayhaps a quarry near t' riverbanks."
    el "*Giggles lightheartedly*"
    scene ch6sc02_181 with dissolve
    el "Yeah... that would be amazing, actually. We could work towards creating our own little settlement out here."
    el "Then we could all move out here, be self-sufficient, and live care-free."
    scene ch6sc02_182 with dissolve
    al "That honestly sounds like a dream!"
    al "All villages and cities must have started off with just a single house."
    scene ch6sc02_183 with dissolve
    fy "Alice is on to something, and look at what we managed in a single day."
    scene ch6sc02_182 with dissolve
    el "Yeah, it’s nice to finally get started, even if it’s just a little roof over the materials."
    el "I don’t want to do too much before [mc] gets back... I want to share this process with him."
    scene ch6sc02_184 with dissolve
    br "Aye... building yer own home... those memories will last ye a lifetime, lass."
    scene ch6sc02_182 with dissolve
    al "I agree. He definitely should be a part of this! But as you said, this was needed to keep the materials dry."
    scene ch6sc02_183 with dissolve
    fy "Are we all spending the night out here? I don’t think we’ll make it back to Luxenford before nightfall."
    scene ch6sc02_181 with dissolve
    el "*Stretches* Hnngh-Yup! I’ve brought food for everyone and we have two tents that are packed away."
    al "Perfect! Borri, Flynn, you’re on tent duty! Eliza and I will take care of preparing the food."
    scene ch6sc02_184 with dissolve
    br "*Chuckles* Heh! C'mon, lad, let's show these lasses how t' build a fire!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    if pearl_relationship == True:
        "After passing out for several hours, you wake up in the jungle to a warm and familiar sensation..."
        scene ch6sc02_185 with Dissolve(1.5)
        $ renpy.pause(1)
        scene black with Dissolve(1)
        mc "Mmmh..."
        scene ch6sc02_185 with Dissolve(1)
        pl "*Licks* Nnh..."
        mc "*Groggy* Mhmm ... Pearl?"
        scene ch6sc02_186 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mc "W-What are we doing here? How did we get from the beach to the jungle?"
        scene ch6sc02_187 with dissolve
        pl "I don’t know. *Mwah* Last thing I remember, we were making out. And then... I woke up right here beside you."
        scene ch6sc02_186 with dissolve
        pl "All I know is, right now... *Licks* Mhm... I really want to suck your cock."
        scene ch6sc02_187 with dissolve
        pl "I told you that you'd need your energy tonight, and I meant it. *Mwah*"
        scene pl_lewd14 with dissolve
        $ renpy.pause()
        mc "Mmfhh... F-Fuck... keep going..."
        pl "You like this? Feeling my lips and tongue move up and down your hard shaft?"
        mc "Yeah... feels fucking amazing. What’s gotten into you?"
        pl "Shhh. *Suck* Just... Mmh... share this moment with me... *Licks*"
        pl "Focus on this moment... How it feels... How I make you feel. Mmhmm..."
        mc "*Moans* Your mouth is warm... wet... soft... Mhmm..."
        scene ch6sc02_187 with dissolve
        pl "*Licks* I have something for you that fits that description perfectly... *Licks*"
        scene ch6sc02_188 with dissolve
        pl "Here... *Muffled* All yours, my sharky."
        scene pl_lewd15 with dissolve
        $ renpy.pause()
        mct "{i}It’s like there’s a tingling sensation all over my body. Warm. And I'm itching to be closer to her.{/i}"
        mct "{i}Is she feeling it too? She must be... Mmhm... It's hard to tell with Pearl, she's naturally horny- Mmmh...{/i}"
        pl "*Muffled gag* Mnfhhh... I’m going to- Mmhhff- suck you dry! MMmh!!"
        mc "Fuu... you’re amazing... Mhmm."
        mc "And so is your little mouth... so eager to have my cock inside..."
        pl "*Suck* MMfhh... I love how warm and tasty you are. I want you to taste me again as well! MMfhh!!"
        scene ch6sc02_189 with dissolve
        "She shifts herself on top of you, presenting you with her dripping wet pussy. Her scent alone entices you to dive in."
        scene pl_lewd16 with dissolve
        $ renpy.pause()
        "You give in to the sensation of increased lust and the tingling feeling across your body continues as you devour each other."
        pl "*Muffled moan* Mmnfhhh! Y-Yess!! Lick my pussy like it belongs to you! MMfhh!"
        with vpunch
        mc "Fuck, Pearl... I can’t get enough of your juicy little pussy. I’m going to fill your mouth any moment."
        pl "Release everything you have for me! Mmf! This time I’m ready for you! Mmfhh!! Make me cum with you!"
        with vpunch
        "You slurp up all of her juices as she comes all over your face, as you also release in her mouth."
        scene ch6sc02_190 with dissolve
        pl "*Panting* Mmfhhh! So amazing..."
        mc "You want more?"
        pl "You’ve no idea... just wait for what I have in store for you, my handsome shark."
        mct "{i}*Chuckles* Five hells... taking her virginity last night really has gotten her excited.{/i}"
        scene ch6sc02_191 with dissolve
        pl "Come on."
        pl "Follow me... I'll find us a good mating spot. *Giggles*"
        scene ch6sc02_192 with dissolve
        mc "Wait a second, don’t just go running off."
        pl "*Giggling* Come get me!"
        scene ch6sc02_193 with dissolve
        mc "Hey, Pearl! Wait up!"
        pl "*Giggles* Find me and claim your prize!"
        scene ch6sc02_194 with dissolve
        mc "Pearl!"
        mc "You don’t know what’s out there..."
        scene ch6sc02_195 with dissolve
        mct "{i}*Sighs* ... Women.{/i}"
        "Left with little choice, you follow Pearl into the vegetation to ensure her safety."
        scene ch6sc02_196 with dissolve
        mc "Pearl?"
        mc "This is hardly the time for games..."
        scene ch6sc02_197 with dissolve
        mc "There you are. What are you up to?"
        pl "*Giggles softly* You found me..."
        scene ch6sc02_198 with dissolve
        pl "*Sensual* Finally, you decided to join me..."
        scene ch6sc02_199 with dissolve
        mc "Follow the naked woman into the jungle and ensure her safety... easy decision."
        scene ch6sc02_198 with dissolve
        pl "Mhm... my hero."
        scene ch6sc02_200 with dissolve
        pl "How will I ever thank you?"
        scene ch6sc02_201 with dissolve
        mc "Ohh... Mhmm..."
        scene ch6sc02_200 with dissolve
        pl "*Sensual* Get primal with me?"
        scene ch6sc02_201 with dissolve
        mc "You want to get in tune with the jungle and channel our inner animals?"
        scene ch6sc02_200 with dissolve
        pl "Mhmm... that’s all I can think about when you get hard for me..."
        scene ch6sc02_201 with dissolve
        pl "Getting fucked like an animal by your hard cock..."
        scene ch6sc02_200 with dissolve
        mc "Go stand by that tree, bend over, and present yourself to me."
        scene ch6sc02_202 with dissolve
        $ renpy.pause()
        pl "*Giggles softly* Mmmh..."
        scene ch6sc02_203 with dissolve
        pl "Like this? Is this how you want me?"
        pl "Is this how you want to take your mermaid and fulfill her desires?"
        mc "Yeah... that’s perfect. Your ass was created for this position..."
        scene ch6sc02_204 with dissolve
        pl "Come closer... I want to feel your warmth."
        pl "Show me how much you like me being in this position."
        mc "Mhm... I love seeing you covered in sweat."
        scene ch6sc02_205 with dissolve
        pl "*Sensual gasp* Aahh... yes, the humidity is crazy in here. Let’s use it to our advantage... Mhmm..."
        scene pl_lewd17 with Dissolve(1.5)
        $ renpy.pause()
        mc "I like the way you think... Mhm... your ass is nice and slippery - Mmghh."
        pl "Fuu... fuckk... you really are an animal. Rubbing your hard cock between my cheeks like that..."
        pl "Such a naughty shark... Mmhmm!"
        mc "You’re one to talk- Mmm... a tight little mermaid with a voluptuous ass, offering herself to me."
        pl "Fuuu- Mhhfp! I can't wait to feel you inside me- AHh..."
        pl "Your cock is so big and hard. I vividly remember how you felt inside me last night in the captain's cabin..."
        with vpunch
        pl "P-Put it in! Please!"
        scene ch6sc02_206 with Dissolve(1.5)
        pl "Mfhh... stop teasing... Mmhmm!"
        scene pl_lewd18 with Dissolve(1.5)
        $ renpy.pause()
        mc "Mhm... doesn’t sound like you want me to stop."
        pl "Nnghhh... you’re driving me crazy..."
        pl "You and that big cock of yours... Nnngh!"
        mc "I know... Mhmm."
        mc "I love seeing you like this."
        pl "Mhmmm-O-Okay... just don’t- Mmm... don’t make me wait too long- Ahhh..."
        scene ch6sc02_206 with Dissolve(1.5)
        mc "I wouldn’t dare. Mmhm... here you go."
        scene ch6sc02_207 with dissolve
        $ renpy.pause(0.5)
        with vpunch
        pl "Ohhh..."
        scene pl_lewd19 with Dissolve(1.5)
        $ renpy.pause()
        with vpunch
        pl "Fuuck! Yessss... f-finally!"
        mc "Five hells... Mmm... you’re so tight."
        mc "Mmm-Mm! You’re amazing, Pearl."
        pl "*Moans* S-So are youuu! AHh!! Fuu .. you’re huge!"
        scene pl_lewd20 with Dissolve(1.5)
        $ renpy.pause()
        mc "You aren’t feeling sore anymore? Mmh... Fuck..."
        pl "N-No... Ahh! I don’t feel sore at all- Aiiyhh! Just... a tingling... ever since we awoke."
        mc "Mmhm... me too. It must be the berries; they could have medicinal properties."
        with vpunch
        pl "*Moans* All I know is- AHh... I want you to keep fucking me! Ahhh!!"
        with vpunch
        mc "Fuu... P-Pearl! You’re fucking tight! Ahhh- I’m- I’m!!"
        scene ch6sc02_208
        with vpunch
        pl "*Moans* No!! Wait!!"
        "She pushes you away at the last second."
        scene ch6sc02_210 with dissolve
        mc "What is it?"
        mc "Did your soreness return?"
        scene ch6sc02_209 with dissolve
        pl "No, no..."
        scene ch6sc02_211 with dissolve
        pl "I just wanted to turn around... so I can see you."
        scene ch6sc02_209 with dissolve
        pl "I want to watch you fuck me right here... against this tree."
        scene ch6sc02_211 with dissolve
        mct "{i}I love when she talks like this... she’s a complete turn-on and she knows it.{/i}"
        scene ch6sc02_209 with dissolve
        mct "{i}This time she’s not going to be able to push me away. I’m going to take her until we both orgasm together.{/i}"
        scene ch6sc02_212 with dissolve
        pl "*Moans* Ohh! Yes... Fuck me..."
        scene pl_lewd21 with Dissolve(1.5)
        $ renpy.pause()
        pl "This is so..."
        pl "Mhmm... exciting. Being claimed by you right here in the jungle... so adventurous- Mmm..."
        mc "You want adventure? I’ll show you an adventure... Mmm."
        with vpunch
        pl "Ahhh!! [mc]! MMh! Y-You’re so deep-Ahhh... we’re so close like this! Mmh..."
        scene pl_lewd22 with Dissolve(1.5)
        $ renpy.pause()
        pl "*Moans* I-I love how you’re holding me against the tree - MMgh... I couldn’t escape even if I wanted to- Ahh!!"
        mc "You’re such a dirty mermaid... Mmm... filled with lust."
        pl "Y-Yesss... whenever I look at you, I just want to get naked and flirt with you until you fuuu...! Fuck me! Ahh!!"
        with vpunch
        pl "Fuck me! Yes!! [mc]!! I’m!! I’m going to- {b}AHHH!! DON’T STOP!!{/b}"
        with vpunch
        scene ch6sc02_213 with dissolve
        with vpunch
        pl "*Breathing heavily* Hnngh... I’ve made you cum three times today... Mmm... and you still have this much for me?"
        mc "*Panting* Fuuuuck... your pussy completely sucked it out of me..."
        pl "Then she served her purpose! *Giggles* To make us both very... happy."
        mc "Mhm... you definitely made me happy."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc02_212 with dissolve
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        pl "I can’t believe we just did that. It was so raw... feral even. I just needed you so badly."
        mc "Likewise... you have a way of making me feel like that."
        pl "I need to lie down- Mmmhmm..."
        scene ch6sc02_214 with Dissolve(1.5)
        $ renpy.pause(1)
        pl "*Giggles softly* I can’t believe you took my virginity in a bed yesterday, and today you fucked me against a tree... in a jungle!"
        scene ch6sc02_215 with dissolve
        mc "*Chuckles* Yeah... I suppose we’ve both wanted each other for quite a while."
        scene ch6sc02_214 with dissolve
        pl "Yeah... I can admit it now. You’re the first man I’ve ever... wanted... desired, even."
        pl "I don’t want to waste that. I don’t want to live with any regrets when it comes to you."
        scene ch6sc02_216 with dissolve
        pl "I just want to follow my... my heart."
        pl "You know?"
        mc "I feel the same."
        pl "[mc], I... lov-"
        scene ch6sc02_217 with Dissolve(1.5)
        pl "I... ZzZz..."
        "The two of you drift off once again..."
        scene black with Dissolve(2)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(1)


    else:
        scene black
        #play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(1)

    scene ss4 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_218 with Dissolve(2)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "You slowly come to your senses..."
    "The sound of birdsong and the feeling of sun rays warming your skin gives you a sense of calm."
    scene ch6sc02_219 with dissolve
    "But as you come to, you realize Pearl isn’t beside you, even though you fell asleep in each other's arms."
    mct "{i}What the hell happened? I’m... I’m in the jungle, but where? How?{/i}"
    scene ch6sc02_220 with dissolve
    "You sit up, trying to get your bearings. Your head is still foggy and hazed as if you'd been slamming ales the entire night."
    mct "{i}Those berries... it must be a side effect of eating them.{/i}"
    scene ch6sc02_221 with dissolve
    mct "{i}Where’s Pearl?{/i}"
    mct "{i}Don’t tell me she wandered off in the night under the influence of those berries?{/i}"
    scene ch6sc02_222 with dissolve
    mct "{i}I can hear the ocean in this direction. Maybe she went back to the beach?{/i}"
    scene ch6sc02_223 with dissolve
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    "..."
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    "......"
    scene ch6sc02_224
    with vpunch
    $ renpy.pause()
    scene ch6sc02_225 with dissolve
    tz "{b}UUuaaahh!{/b}"
    scene ch6sc02_226
    with vpunch
    tz "*Groans* Owwh..."
    tz "I've really got to practice my landings..."
    scene ch6sc02_227 with dissolve
    tz "Weird. My translocator usually works with pinpoint accuracy... but I don’t see him anywhere."
    tz "Something must be interfering with the magic in my translocator... Hmh, curious."
    scene ch6sc02_228 with dissolve
    tz "I'd better start looking! It’s hard to chronicle a hero when he isn’t present!"
    tz "He surely went this way! *Snickers* My instincts are superior!"
    scene ch6sc02_223 with dissolve
    $ renpy.pause(1)
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_140 with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_229 with dissolve
    "When you arrive back at the cliffs overlooking the beach, there’s no sign of Pearl. Only the distant sound of seagulls."
    mct "{i}Nothing’s ever easy. Where the hell is she?{/i}"
    mct "{i}This is so strange... she wouldn’t just venture off on her own.{/i}"
    scene ch6sc02_230 with dissolve
    mct "{i}*Sighs* Back to scouring the jungle it is...{/i}"
    mct "{i}The island is huge and the jungle is very dense. This'll be like looking for a needle in a haystack.{/i}"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    "You wander for about an hour, venturing into the thick of the jungle."
    scene ch6sc02_231 with Dissolve(2)
    $ renpy.pause(1)
    mct "{i}It would actually be pretty awesome exploring this jungle properly, if I wasn’t so worried about finding Pearl.{/i}"
    mct "{i}Everything is so colorful and lush.{/i}"
    scene ch6sc02_232 with dissolve
    mct "{i}Huh? What the...{/i}"
    mct "{i}Is that what I think it is?{/i}"
    scene ch6sc02_233 with dissolve
    mct "{i}Yeah, it's definitely some sort of structure. It’s huge.{/i}"
    mct "{i}It towers over the tree canopy like it’s nothing.{/i}"
    scene ch6sc02_234 with dissolve
    mct "{i}Hmh. I feel drawn to it... like... Fuck, I don’t know like what. But it feels strange, and good.{/i}"
    mct "{i}It’s beckoning me... calling to me.{/i}"
    mct "{i}Maybe there's some strong magic within the structure? Is that what I’m feeling drawn to?{/i}"
    scene ch6sc02_235 with dissolve
    mc "Huh? Pearl?! Is that you?"
    mc "I could've sworn I saw something move..."
    scene ch6sc02_236 with dissolve
    mc "*Calls out* Pearl!"
    scene ch6sc02_237
    with vpunch
    mc "What the...?"
    scene ch6sc02_238 with dissolve
    mc "Oww..."
    scene ch6sc02_239
    with vpunch
    mc "Fuuu..."
    mc "The same dizziness as this morning- Nngh..."
    mc "I’m... being... attacked? Hnngh..."
    scene ch6sc02_240 with dissolve
    "A sensation of deep calm and tranquility washes over you as you fall to the ground."
    scene black with Dissolve(2)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    "You recognize the feeling... it’s like what you experienced last night, only much more potent."
    scene ch6sc02_241 with Dissolve(2)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "Shifting in and out of consciousness, you're dimly aware of being dragged through the leafy undergrowth."
    scene ch6sc02_242 with dissolve
    "Somehow, you feel yourself drawing closer to the source of whatever strange force was calling to you."
    scene ch6sc02_241 with dissolve
    "Could your attackers have been the ones who attacked your ship?"
    scene ch6sc02_242 with dissolve
    "Have they also captured Pearl? As you contemplate their intentions, you finally feel able to speak."
    scene ch6sc02_241 with dissolve
    mc "*Stutters* Nnghh... P-Pearl? W-Who are you?"
    scene ch6sc02_242 with dissolve
    uk "Silence, Outsider."
    scene ch6sc02_243 with dissolve
    "Your vision blurs once more and you try to form words but your lips won’t move."
    uk "How is he able to speak?"
    uk "I do not know. One of our darts should take down an elephant for hours, or a deer for over a day."
    uk "Remember when Huntress Ohira accidentally pricked herself on a dart? She passed out for almost two full days."
    scene ch6sc02_244 with dissolve
    uk "And yet, it took several darts to take him down! A single man? It is very strange."
    uk "*Nods* It is."
    uk "Come, we need to get him back before he wakes up again."
    scene black with Dissolve(1.5)
    "You lose all sense of time as you drift back into what feels like a dream, where a sense of comfort and joy surrounds you."
    "You feel like you... belong. That you being here is... fated... somehow."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_244a with Dissolve(1.5)
    $ renpy.pause(1)
    elt "C'mon Eliza... how hard can it be?"
    elt "[mc] does it all the time... he doesn't even put in any effort to it either."
    scene ch6sc02_244b with dissolve
    elt "If I can learn how to do this... I won't have to remain behind next time."
    elt "I can run by his side... okay, let's do this!"
    scene ch6sc02_244c with dissolve
    elt "Nngh! As fast as I can!"
    scene ch6sc02_244d with dissolve
    $ renpy.pause(0.7)
    with vpunch
    elt "*Excitedly* Yes! I'm doing it!"
    scene ch6sc02_244e with dissolve
    $ renpy.pause(0.7)
    elt "*Snickers* I'm actually running on water!"
    scene ch6sc02_244f with dissolve
    $ renpy.pause(0.5)
    with vpunch
    elt "WuuaahHH!"
    scene ch6sc02_244g with dissolve
    $ renpy.pause(0.5)
    with vpunch
    elt "........"
    elt "I got too cocky..."
    scene ch6sc02_244h with dissolve
    $ renpy.pause(0.5)
    elt "I got two steps though."
    elt "*Exhales* And I got drenched... did I really think I'd just be able to do it first try?"
    scene ch6sc02_244i with dissolve
    $ renpy.pause(0.5)
    elt "I can do this... I know I can!"
    elt "But first... I'm gonna need to dress for the occasion."
    scene ch6sc02_244j with dissolve
    $ renpy.pause(0.5)
    scene ch6sc02_244k with dissolve
    $ renpy.pause(1)
    scene ch6sc02_244j with dissolve
    $ renpy.pause(0.5)
    scene ch6sc02_244l with dissolve
    $ renpy.pause(0.5)
    elt "Alright!"
    elt "Time to get to work!"
    elt "I'm getting to ten steps before sunset at the very least!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.7)
    scene ch4sc15_019b with Dissolve(1.5)
    $ renpy.pause()
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_245 with Dissolve(1.5)
    "Eventually, you slowly return to the world of consciousness."
    scene ch6sc02_246 with dissolve
    mc "*Groans* Ugh... what in the five hells?"
    mc "I’m inside a... hut?"
    scene ch6sc02_247 with dissolve
    mc "Where am I?"
    mc "How did I even get here? ... Right, I was knocked out and dragged..."
    scene ch6sc02_248 with dissolve
    mc "By two... women?"
    mc "All I saw was glimpses of their backsides... definitely women."
    "As you’re attempt to get to your feet, you notice something heavy weighing your legs down."
    scene ch6sc02_249 with dissolve
    $ renpy.pause(0.5)
    with vpunch
    mc "Chains?! What the fuck?"
    mc "Hnnghh... dammit. My body is still weak from the drugs they hit me with..."
    scene ch6sc02_248 with dissolve
    mc "*Sighs* Guess I’m stuck here until my strength returns."
    scene ch6sc02_250 with dissolve
    mc "Anyone out there?! Hey!"
    mc "*Sighs* ... Stuck as a prisoner again, great."
    scene ch6sc02_251 with dissolve
    "Your call seems to have been noticed. You hear footsteps outside; someone is approaching."
    "You can hear the quiet whispers of female voices outside the hut."
    mc "Reveal yourselves."
    scene ch6sc02_252 with dissolve
    uk1 "I guess he heard us."
    uk2 "You're always too loud."
    scene ch6sc02_253 with dissolve
    mct "{i}The locals captured me?{/i}"
    uk1 "*Snickers* Can you believe this outsider? Commanding us."
    scene ch6sc02_254 with dissolve
    uk2 "At least he’s funny... unlike other outsiders."
    scene ch6sc02_255 with dissolve
    uk1 "Maybe the outsider will tell us some jokes next?"
    scene ch6sc02_254 with dissolve
    uk2 "Maybe..."
    scene ch6sc02_255 with dissolve
    uk1 "Hmm, I'll bet you two coconuts that he'll make another joke!"
    scene ch6sc02_254 with dissolve
    uk2 "Easiest coconuts I've ever earned."
    scene ch6sc02_256 with dissolve
    mc "Outsider? Funny? You don’t see me as a threat?"
    "Both women stare at you frankly, assessing you."
    scene ch6sc02_257 with dissolve
    uk2 "Should we? Are you a threat to us, outsider?"
    scene ch6sc02_256 with dissolve
    mc "Well... no."
    mc "At least, not right now."
    scene ch6sc02_257 with dissolve
    uk2 "Right now? What do you mean by that? Do you intend to harm us later?!"
    scene ch6sc02_258
    with vpunch
    uk1 "Maybe we should spear him now and be done with it?"
    mc "Woah! Woah! Ladies... I didn’t intend to threaten you. But you've kidnapped me and chained me up."
    scene ch6sc02_256 with dissolve
    mc "I don’t exactly know what your intentions are, but that isn't exactly a friendly action."
    mc "Can you blame me for wanting to protect myself?"
    bth "..."
    scene ch6sc02_257 with dissolve
    uk2 "Our actions aren’t friendly, he says? We brought him to A’nai and gave him a nice bed to rest on..."
    uk2 "Tsk, outsiders. Ungrateful and greedy."
    scene ch6sc02_259 with dissolve
    mc "No, I do appreciate that part. But you’re also keeping me chained up, and you drugged me with darts."
    bth "..."
    scene ch6sc02_260 with dissolve
    wo "Play nice, you two."
    wo "You'll scare the poor man."
    scene ch6sc02_261 with dissolve
    wo "Suji, behave..."
    wo "Leave your judgment for those who actually wrong us."
    scene ch6sc02_262 with dissolve
    wo "Zyra, that goes for you as well."
    zy "*Nods* Mm."
    scene ch6sc02_263 with dissolve
    mct "{i}Hmm? The way they bow their heads and silently obey her... she’s obviously respected here.{/i}"
    mct "{i}She must be a leader of some sort, but she doesn't look much older than me. Maybe a couple of years?{/i}"
    scene ch6sc02_264 with dissolve
    wo "I apologize for how my huntresses have treated you."
    wo "They are a little wary of outsiders. But not without reason, let's leave it at that for now."
    scene ch6sc02_265 with dissolve
    mc "It’s fine... I can understand where they’re coming from."
    mc "They are probably just protective of what you've got here."
    scene ch6sc02_266 with dissolve
    mc "Who are you...?"
    ec "Echo."
    scene ch6sc02_268 with dissolve
    ec "I am the A’nu of my tribe."
    ec "Welcome to our home, A’nai."
    scene ch6sc02_269 with dissolve
    mc "A’nai... I've heard that name before..."
    mc "A man I met several years ago once mentioned something about the lost city of A’nai."
    scene ch6sc02_270 with dissolve
    ec "Lost? *Scoffs* No... we're not lost."
    ec "Hidden. Our home is hidden."
    scene ch6sc02_269 with dissolve
    mc "Hidden? Hmm..."
    mc "That'd explain why he said it couldn't be found on any maps."
    scene ch6sc02_270 with dissolve
    ec "Yes, A’nai is hidden away from outsiders like yourself."
    ec "Our jungle shields us from the outside world and the troubles it brings."
    scene ch6sc02_271 with dissolve
    mc "Why are you hiding?"
    ec "..."
    mc "Sorry, I don’t mean to pry. I'm just curious."
    scene ch6sc02_272 with dissolve
    ec "Zyra, Suji..."
    scene ch6sc02_273 with dissolve
    sj "Yes, A’nu?"
    scene ch6sc02_274 with dissolve
    ec "Please, leave us."
    ec "You’re no longer needed here."
    scene ch6sc02_272 with dissolve
    ec "You’re free to resume your duties elsewhere."
    scene ch6sc02_275 with dissolve
    sj "Echo... A’nu. *Sighs* ..."
    scene ch6sc02_276 with dissolve
    ec "Yes? Speak freely, Suji."
    scene ch6sc02_277 with dissolve
    sj "Please, be careful with the outsider..."
    sj "We don't know his intentions, or why he's intruded on our lands."
    sj "And... he’s a man."
    scene ch6sc02_276 with dissolve
    ec "Thank you, Suji."
    ec "Your concern is valid and I will keep it in mind."
    scene ch6sc02_278 with dissolve
    ec "Please, forgive them..."
    ec "We're not used to outsiders showing up unexpectedly."
    ec "Their concerns... are also well founded."
    scene ch6sc02_279 with dissolve
    mc "As I said earlier, I'm not offended."
    mc "I can understand that they might be wary of me."
    mc "They don't know me, so they're still trying to assess whether I'm a threat to your village or not."
    scene ch6sc02_280 with dissolve
    ec "Thank you."
    ec "You’re very intuitive, and kind... compared to most outsiders we’ve dealt with."
    scene ch6sc02_281 with dissolve
    ec "As I said, we have good reason to be wary of outsiders."
    ec "You must understand, we keep to ourselves and don’t wish to be disturbed."
    scene ch6sc02_282 with dissolve
    ec "*Quietly* The last time is still a horrific memory for many of us."
    mc "What happened to make you feel this way? Why do you hide from outsiders?"
    scene ch6sc02_281 with dissolve
    ec "That's a tale for a different time, I’m afraid."
    scene ch6sc02_283 with dissolve
    ec "Now, I’d like you to answer some of my questions."
    ec "Your presence here raises quite a few."
    scene ch6sc02_284 with dissolve
    mc "Sure. You’ve been welcoming towards me, so far. I’ll answer what I can."
    ec "It pleases me that my manners aren’t wasted."
    scene ch6sc02_285 with dissolve
    ec "Firstly, who are you, outsider?"

    if leadership >= 5:
        scene ch6sc02_286 with dissolve
        mc "I'm a Captain, of the Bloody Banshee, a ship from Looter's Bay."
        scene ch6sc02_285 with dissolve
        ec "Is that how you got here? By ship?"
        scene ch6sc02_286 with dissolve
        mc "Yeah, I sailed here."
        scene ch6sc02_285 with dissolve
        ec "I do not know the meaning of this... 'Captain' ... what is that?"
        scene ch6sc02_286 with dissolve
        mc "A Captain is a leader, one who governs a crew of sailors on his ship."
        scene ch6sc02_285 with dissolve
        ec "A... leader? Hmmm, interesting."
        $ ec_trust += 2
        "Echo seems intrigued by the fact you're a leader, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        scene ch6sc02_286 with dissolve
        mct "She seemed to take an interest in me being a leader?"

    else:
        scene ch6sc02_286 with dissolve
        mc "I'm a commoner from the mainland..."
        scene ch6sc02_285 with dissolve
        ec "I see... hmm."
        "Your {color=#ffee54}Leadership{/color} was too low to provide Echo with a satisfying answer."


    scene ch6sc02_285 with dissolve
    ec "So, what were you doing in the outskirts of A’nai?"
    ec "You were roaming in our sacred hunting grounds."
    scene ch6sc02_286 with dissolve
    mc "Sacred? I'm sorry, I didn't realize where I was."
    mc "I didn’t even know you existed until your huntresses captured me."
    scene ch6sc02_285 with dissolve
    ec "Hmm... you don’t seem to be lying. So, you weren’t directly looking for A’nai, then."
    ec "Perhaps you didn’t know about us... but..."
    ec "I wonder if you would’ve still crossed into our territory if you'd known about our boundaries? We have to protect ourselves."
    scene ch6sc02_286 with dissolve
    mc "We mean you no harm."
    scene ch6sc02_287 with dissolve
    ec "We? You’re not alone?"
    scene ch6sc02_286 with dissolve
    mc "Well, I was alone when you caught me. But, no. I came here with a friend, a woman named Pearl."
    mc "We were together last night. But something must have happened, we got separated..."
    scene ch6sc02_288 with dissolve
    mc "I was trying to find her when your huntresses captured me."
    mc "I’m not really sure what happened exactly... I’m a little hazy on what happened last night."
    scene ch6sc02_285 with dissolve
    ec "We have no knowledge of the woman you speak of. My huntresses haven’t reported any sightings of her."
    ec "Which leads me to my next question..."
    ec "Following up on what you just said."
    scene ch6sc02_289 with dissolve
    ec "Why is your mind hazy about last night?"
    scene ch6sc02_290 with dissolve
    mc "I think... it had something to do with some berries we ate."
    mc "We were getting hungry, so I foraged for something edible in the jungle. I stumbled on some berry bushes that looked like black berries."
    scene ch6sc02_289 with dissolve
    ec "Black berries? Oh..."
    scene ch6sc02_291 with dissolve
    ec "You poor thing... your head must’ve felt terrible."
    scene ch6sc02_292 with dissolve
    mc "Yeah... I was definitely feeling a bit weird when I woke up."
    ec "..."
    scene ch6sc02_291 with dissolve
    ec "You don’t seem to have a severe fever, thankfully."
    mc "I'm guessing the berries aren’t edible?"
    scene ch6sc02_293 with dissolve
    ec "No... they are not to be eaten."
    ec "At least... not without gradually building up a tolerance over time."
    ec "The berries of the sacred grounds are used for both medicinal and poisonous uses."
    scene ch6sc02_294 with dissolve
    mc "Both medicinal and poisonous? No wonder they knocked me out."
    scene ch6sc02_293 with dissolve
    ec "Yes, it depends on what else you mix with them. Our shamans can use them to increase vigor and cure fevers."
    ec "While our huntresses use them as tranquilizers when hunting prey."
    scene ch6sc02_295 with dissolve
    ec "You’re actually well acquainted with their effect already."
    scene ch6sc02_296 with dissolve
    mc "*Sighs* The darts, I’m assuming?"
    scene ch6sc02_295 with dissolve
    ec "Correct, our huntresses coat the tips of their darts with the concentrated juices of the berries, mixed with earthroot extract."
    scene ch6sc02_297 with dissolve
    ec "This creates a powerful sedation effect that can knock out most creatures almost instantaneously."
    ec "The drug is quickly absorbed into the blood, which is why it works so swiftly."
    scene ch6sc02_298 with dissolve
    mc "Your huntresses shot me full of them..."
    scene ch6sc02_297 with dissolve
    ec "Yes... they were surprised it took so many. We were all surprised when they returned and claimed it took seven darts to knock you out."
    ec "One dart is usually enough to bring down an elephant for a couple of hours, you know?"
    scene ch6sc02_298 with dissolve
    mct "{i}*Chuckles* I suppose my toxin resistance works then.{/i}"
    scene ch6sc02_297 with dissolve
    ec "What? Is something funny?"
    scene ch6sc02_298 with dissolve
    mc "No, just... it's nothing."
    scene ch6sc02_293 with dissolve
    ec "The fact that you're even awake right now, after only a few hours..."
    ec "You should've been unconscious for at least a week after being struck by seven darts."
    ec "It’s fascinating..."
    scene ch6sc02_294 with dissolve
    mc "Are there... any side-effects to the drug on the darts?"
    scene ch6sc02_293 with dissolve
    ec "Well..."
    ec "When you consume the berries, as you did last night, it takes some time before the sedative effect happens."
    ec "And it usually leaves you with a potent hangover. But before that, it's not unusual to experience... increased lust."
    scene ch6sc02_297 with dissolve
    ec "As for the darts..."
    ec "When I was a youngling, one of the village huntresses was brought back from a hunt, her mind blissfully unaware."
    ec "Apparently, during the pursuit of their prey, one of the other huntresses accidentally hit her in the thigh with a dart."
    scene ch6sc02_299 with dissolve
    ec "She was in and out of consciousness for two days straight."
    ec "When she awoke, it sounded like she'd had some... pleasant dreams, though."
    ec "Like... very pleasant."
    scene ch6sc02_298 with dissolve
    mc "Yikes... so you’re telling me I’m likely to have some... adventurous dreams of my own?"
    scene ch6sc02_297 with dissolve
    ec "Goddess... no. I’m telling you that you’ll be fine."
    ec "The fact that you’re up and about already suggests that you’re safe from any side-effects."
    scene ch6sc02_298 with dissolve
    mc "*Chuckles* Shame. I could do with a few of those."
    scene ch6sc02_299 with dissolve
    ec "*Quietly* You and me both..."
    scene ch6sc02_298 with dissolve
    mc "Well, I’m relieved to hear your huntresses didn’t poison me into the next realm..."
    mc "So, is there anything else you want to know?"
    scene ch6sc02_299 with dissolve
    ec "Yes..."
    scene ch6sc02_300 with dissolve
    ec "There is one more thing I’d like to know..."
    ec "What is it you long for? What do you desire?"
    scene ch6sc02_301 with dissolve
    mc "What do you mean by that?"
    scene ch6sc02_300 with dissolve
    ec "You’re the first man to set foot in A’nai in two decades..."
    ec "you've coped with seven potent tranquilizer darts inhumanely well."
    ec "You managed to find our sacred city..."
    scene ch6sc02_301 with dissolve
    mc "Somehow, I felt drawn to your city. I can’t explain why."
    scene ch6sc02_302 with dissolve
    ec "You don’t feel any different?"
    ec "After arriving here?"
    scene ch6sc02_303 with dissolve
    mc "I suppose a little? You’d have to be more specific."
    scene ch6sc02_302 with dissolve
    ec "Does your blood run hotter than before?"
    ec "Does it feel like a weight has been lifted from your broad shoulders?"
    ec "*Quietly* Or that your soul’s ... deepest longings, are achievable?"
    scene ch6sc02_303 with dissolve
    mc "Hmm? To some degree? I’m not entirely sure."
    scene ch6sc02_302 with dissolve
    ec "Do you feel the will of Malanthe run through you? Does the will of Gaia guide you? Do you feel the will of Maia embrace you?"
    scene ch6sc02_303 with dissolve
    mct "{i}Maia?? Is she talking about Maia, the maiden of purity?{/i}"
    mct "{i}I suppose these must be the goddesses they revere here in the tribe?{/i}"
    mc "I’m not really sure if I feel their wills inside me."
    scene ch6sc02_304 with dissolve
    ec "Never mind, then."
    ec "Time will tell... *Quietly* whether you're the one who was promised."
    scene ch6sc02_302 with dissolve
    ec "I thank you for your willingness to answer my questions."
    scene ch6sc02_293 with dissolve
    ec "Now it’s time for me to give you something in return..."
    mc "What are you-"
    scene ch6sc02_305 with dissolve
    mc "Hmh?"
    ec "I’m giving you-"
    scene ch6sc02_306 with dissolve
    ec "Your freedom."
    mc "Thank you..."
    scene ch6sc02_307 with dissolve
    ec "Echo. You may use my birth name."
    mc "Thank you, Echo."
    scene ch6sc02_308 with dissolve
    mc "I appreciate the gesture."
    ec "..."
    scene ch6sc02_309 with dissolve
    ec "You’re most welcome..."
    mc "[mc]."
    ec "[mc]... a warrior's name."
    scene ch6sc02_310 with dissolve
    ec "However, don’t assume this means you can do whatever you please."
    scene ch6sc02_311 with dissolve
    ec "For the time being, you will be observed carefully..."
    scene ch6sc02_310 with dissolve
    ec "You’re still an outsider here in A’nai, and... a man."
    scene ch6sc02_311 with dissolve
    ec "I believe you’ve been truthful with me, but we’ll see. Your intentions will be made clear in time."
    scene ch6sc02_312 with dissolve
    mct "{i}Wandering the jungle aimlessly looking for Pearl is hopeless ...{/i}"
    mct "{i}My best bet is to befriend them and have them help me find her.{/i}"
    mc "Of course, I’m a guest here. I don’t intend to overstep any boundaries or cause trouble."
    scene ch6sc02_313 with dissolve
    ec "Indeed, you are... a guest."
    ec "I'm pleased you are understanding of our situation."
    scene ch6sc02_314 with dissolve
    ec "Hmmmh..."
    ec "Actually... yes. This is a good idea..."
    mc "What is?"
    scene ch6sc02_315 with dissolve
    ec "As our- as my guest..."
    ec "I wish to give you a little tour of A’nai, our home."
    scene ch6sc02_316 with dissolve
    ec "Come, [mc], follow me."
    ec "You're the first to get a personal tour from me."
    scene ch6sc02_317 with dissolve
    ec "A’nai awaits."
    ec "I feel it in my body... we are changing our fate."
    scene ch6sc02_318 with dissolve
    mc "I don't know about fates, but I'd love a tour."
    mc "What is this place?"
    scene ch6sc02_319 with dissolve
    mc "This hut seems a little too nice for a prisoner."
    scene ch6sc02_320 with dissolve
    ec "This is one of the huntresses huts, we don’t have an area for prisoners..."
    ec "As I said earlier, we haven’t had an outsider here in over two decades..."
    scene ch6sc02_321 with dissolve
    mc "Well, despite being chained up, I did still feel... comfortable?"
    mc "Surprisingly comfortable, actually. I had a pillow, a bed, the warmth of a fire."
    scene ch6sc02_322 with dissolve
    ec "This surprises you?"
    scene ch6sc02_323 with dissolve
    mc "Yeah. It’s not common where I’m from. Usually, prisoners are treated as less than human."
    scene ch6sc02_322 with dissolve
    ec "Hmh... Horrendous, but not entirely surprising."
    scene ch6sc02_324 with dissolve
    ec "I can easily imagine the conditions you outsiders make your prisoners endure."
    mc "What makes you say that? I thought you haven’t had any outsiders for a long time?"
    scene ch6sc02_325 with dissolve
    ec "Mhm. We haven’t. But there are stories that have been passed down. Tales of the past."
    ec "But such unpleasant topics can wait until after the tour... for now, let’s just enjoy A’nai."
    mct "{i}Something really bad must have happened in the past for them to be so wary of outsiders.{/i}"
    scene ch6sc02_326 with dissolve
    ec "Come, it’s time that I show you how we live here in A’nai."
    ec "Please, take it all in, listen, look and learn."
    scene ch6sc02_327 with dissolve
    mc "Perfect. I’m quite interested to see what A’nai is all about, Echo- if I can really call you by name?"
    "She silently assesses you."
    mc "I know you gave me your name earlier, but -"
    scene ch6sc02_328 with dissolve
    ec "Hmmmm..."
    mc "I noticed your huntresses addressed you by your title, {b}A’nu{/b}. So, if I’m overstepping -"
    scene ch6sc02_329 with dissolve
    ec "Yes, you may use my birth name."
    ec "You’re not a member of the tribe, or a subject, but a guest..."
    ec "And being called by my name is quite refreshing."
    scene ch6sc02_327 with dissolve
    mc "Well, then, Echo... I’m eager to see what the tour will bring, lead on."
    scene ch6sc02_329 with dissolve
    ec "Most wonderful! I’m pleased to see you taking an interest in this."
    ec "This way, please."
    scene ch6sc02_330 with dissolve
    ec "There’s no reason to linger here in the homes of our huntresses."
    ec "You’ve already seen some of it and I don’t want to further disturb them."
    scene ch6sc02_331 with dissolve
    mc "*Chuckles* Yeah, they didn’t take much of a liking to me. We'd better not disturb them further."
    "She let's out a small laugh."
    scene ch6sc02_332 with dissolve
    ec "I apologize, once again. Their behavior towards you was harsh and lacked manners."
    scene ch6sc02_333 with dissolve
    mc "Echo, I understand completely. Their role is to defend and protect the tribe from anything, and anyone."
    mc "If they weren’t on guard against a possible threat, your tribe could suffer because of it."
    scene ch6sc02_332 with dissolve
    ec "Yes, precisely."
    scene ch6sc02_334 with dissolve
    ec "Thank you for understanding and respecting our ways. We are civil... even if our tribal culture may seem otherwise."
    mc "To me, it seems you are plenty civilized here. Your buildings and infrastructure seem solid. And to have the leader of your people -"
    mc "Personally oversee my welcome? ... That's not common in other nations."
    scene ch6sc02_335 with dissolve
    ec "I’m glad that treating guests poorly is not something we have in common with other nations."
    ec "Let’s banish them and their ways from our minds."
    scene ch6sc02_336 with dissolve
    ec "There is still much to see."
    ec "This way, [mc]."
    scene ch6sc02_337 with dissolve
    mc "Hmh?"
    mc "That’s one of the huntresses from earlier? She doesn’t seem happy to see me."
    scene ch6sc02_338 with dissolve
    mc "Are you sure the villagers are okay with my presence?"
    ec "Oh, you need not worry..."
    scene ch6sc02_339 with dissolve
    ec "They are likely sizing you up, trying to figure you out."
    ec "Let us continue. In time they will lower their guard and accept your presence."
    scene ch6sc02_340 with dissolve
    ec "Our next stop is the huntress’s training grounds. I have a feeling you’ll like it."
    scene ch6sc02_341 with dissolve
    mc "What makes you say that?"
    scene ch6sc02_335 with dissolve
    ec "Judging by your..."
    ec "Well-developed physique, you must have experienced combat."
    ec "The training ground is where we train for combat and for surviving the jungle."
    scene ch6sc02_330 with dissolve
    mc "Oh? That does sound like a place I’d enjoy."
    scene ch6sc02_331 with dissolve
    mc "I’m not quite feeling at full strength yet, though."
    scene ch6sc02_332 with dissolve
    ec "That is to be expected. Seven darts... the fact that you’re walking is a miracle."
    ec "Your strength will return in due time."
    scene ch6sc02_342 with dissolve
    mc "From what I can tell, your tribe is pretty well developed, despite your isolation on Aruna."
    ec "*Nods*"
    scene ch6sc02_343 with dissolve
    ec "Come, it’s just up ahead. Looks like training is in session."
    mc "Who are they?"
    scene ch6sc02_344 with dissolve
    ec "Vex."
    ec "She’s one of our youngest, at just 19 summers. She’s aspiring to become a Huntress."
    vx "..."
    scene ch6sc02_345 with dissolve
    ec "Kisha."
    ec "Kisha is our Head-Huntress. She leads hunts into the jungle as well as overseeing the training of others."
    scene ch6sc02_346 with dissolve
    "The two women bow their heads as Echo approaches."
    ks "A’nu. Your presence honors us."
    scene ch6sc02_347 with dissolve
    ks "An outsider..."
    ks "Who is this man? Are you keeping him as a pet?"
    scene ch6sc02_348 with dissolve
    ec "Pet? Don't be ridiculous, Kisha."
    ec "No, he’s my guest."
    scene ch6sc02_349 with dissolve
    ks "*Scoffs* An outsider as a guest in A’nai?"
    ks "A’nu... I respect your choice but..."
    scene ch6sc02_350 with dissolve
    ec "But?"
    ec "Speak freely, Kisha..."
    scene ch6sc02_351 with dissolve
    ks "Don't you think it’s a big risk? Treating an outsider as a guest..."
    ks "It could severely impact our way of life."
    ks "He could be another threat... disguised by a friendly facade."
    scene ch6sc02_352 with dissolve
    vx "..."
    mct "{i}The little one is eyeing me up, she doesn't seem too thrilled with my presence.{/i}"
    ec "Kisha, your concerns are valid and... I am not yet sure."
    scene ch6sc02_353 with dissolve
    ec "That is exactly what I’m trying to figure out."
    ec "I wish to determine his worth. Does he have a warrior's heart? Or... that of a snake?"
    scene ch6sc02_351 with dissolve
    ks "Marah will not be-"
    scene ch6sc02_352 with dissolve
    ec "Marah’s fears are not mine."
    scene ch6sc02_350 with dissolve
    ec "Her worries, and everyone else’s, are understandable. Even the outsider - [mc] - has been very understanding of this."
    ec "She might be High-Priestess, and enjoys an elevated position, but my decisions are still my own to make"
    scene ch6sc02_353 with dissolve
    ec "And for now, I choose to trust him. To open our home to him."
    ec "Be it fate, or the will of the goddesses, he was drawn here... to A’nai."
    scene ch6sc02_352 with dissolve
    ec "You know our history and the tales passed down, as well as I. He could be..."
    scene ch6sc02_354 with dissolve
    ks "Of course, A’nu."
    ks "I will respect your decision to determine his worth."
    scene ch6sc02_350 with dissolve
    ec "Thank you, Kisha... I value your counsel."
    ec "Now, please continue the training."
    scene ch6sc02_352 with dissolve
    ec "We wish to observe. Show [mc] your prowess."
    scene ch6sc02_354 with dissolve
    ks "Of course, we were just about to start when you arrived."
    scene ch6sc02_355
    with vpunch
    ks "Huntress! Ready yourself!"
    scene ch6sc02_356 with dissolve
    vx "Hyaahh!"
    scene ch6sc02_357
    with vpunch
    ks "Hmh? What’s this sudden aggression?"
    ks "Why are you trying to show off now? Flashy moves like that aren’t practical."
    scene ch6sc02_358 with dissolve
    vx "I’m not showing off! Hnngh!"
    scene ch6sc02_359 with dissolve
    ks "Oh yeah? Then why is your breath control lacking?"
    ks "And why isn’t your footwork as good as before?"
    scene ch6sc02_358 with dissolve
    vx "My breathing is fine!"
    scene ch6sc02_360
    with vpunch
    vx "And so is my footwork!"
    ks "Then why can I do this?"
    scene ch6sc02_361
    with vpunch
    ks "Hyaah!"
    vx "WuuaahH!"
    scene ch6sc02_362 with dissolve
    vx "*Squeals* Aiiyh!"
    scene ch6sc02_363
    with vpunch
    vx "Hnnghh... not fair!"
    ks "*Scoffs* ..."
    scene ch6sc02_364 with dissolve
    vx "I was distracted..."
    mct "{i}Why is she glaring at me? ... I’m just watching.{/i}"
    scene ch6sc02_365 with dissolve
    ks "To survive the jungle you must be alert to your surroundings, and your focus unwavering."
    ks "Your footing is paramount, be it climbing trees, descending steep slopes, or jumping from rock to rock across rivers."
    scene ch6sc02_366 with dissolve
    ks "You cannot afford to be distracted out there. The jungle is our home, but it can also be treacherous."
    ks "You know as well as I do that good huntresses have been lost out there."
    mct "{i}Huh? Even they can be lost in the jungle? There must be more to this place than meets the eye.{/i}"
    scene ch6sc02_367 with dissolve
    vx "I... I know. I’ll do better, Head-Huntress."
    vx "..."
    scene ch6sc02_350 with dissolve
    ec "Exceptional training, Huntresses."
    scene ch6sc02_344 with dissolve
    ec "Young one, I’ve no doubt you will grow into a great Huntress once you gain more experience."
    scene ch6sc02_368 with dissolve
    vx "A’nu... t-thank you!"
    vx "I will strive to do better... I-I will make you proud!"
    ec "I have no doubt that you will make us all proud. Huntresses, you may continue."
    scene ch6sc02_369 with dissolve
    ec "Come, [mc]. We shall give them space to train with a focused mind."
    ec "Next up is one of our sacred temples. You may not enter... but observing shouldn’t be an issue."
    scene ch6sc02_370 with dissolve
    mc "As you wish."

    if charisma >= 7:
        mc "I don’t want to cross any boundaries or accidentally insult your ways."
        mc "Your culture is important. Having an outsider waltz around and touch things that are sacred to you, would also upset me."
        scene ch6sc02_371 with dissolve
        ks "You surprise me, outsider... respecting our ways and traditions? Hmm."
        $ ks_trust += 2
        "You had enough {color=#87e1fa}Charisma{/color} experience to earn a little respect, Kisha's trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        ks "Disrespecting our ways and culture is a quick way to become an enemy of our tribe."

    else:
        mc "I don’t want to cross any boundaries or accidentally insult your ways."
        scene ch6sc02_371 with dissolve
        ks "Your presence here in A'nai is a boundary being crossed.. tsk."
        "Your {color=#87e1fa}Charisma{/color} was too low to earn any respect from Kisha."
        ks "Disrespecting our ways and culture is a quick way to become an enemy of our tribe."

    scene ch6sc02_372 with dissolve
    mc "I don’t want that. I’m not interested in being your enemy..."
    mc "Thank you for the demonstration. I can tell both of you are capable warriors."
    scene ch6sc02_373 with dissolve
    bth "..."
    "The two huntresses share a puzzled look with each other, taken back by your compliment."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_335 with Dissolve(1)
    ec "Come... we have much to see."
    scene ch6sc02_336 with dissolve
    ec "Take a look."
    scene ch6sc02_374 with dissolve
    ec "As you can see, the tribe is quite busy. Everyone has tasks to accomplish."
    ec "We all have to pull our own weight in order for the tribe to thrive."
    scene ch6sc02_375 with dissolve
    ec "Huntresses provide food and teach survival skills, they are essential to the prosperity of the tribe."
    ec "They also serve as protectors alongside our War-maidens."
    ec "They provide security and patrol the area, both inside and outside the village."
    mc "If you haven’t had outsiders in two decades, then what is the security for?"
    ec "We’re not alone on this island. Aruna is vast, and we share it with another tribe. They aren't very friendly."
    mct "{i}Hmm... could it be the other tribe who shipwrecked us?{/i}"
    scene ch6sc02_376 with dissolve
    ec "Herbalists forage for edible plants and medicinal herbs, and tend to our wounded."
    ec "While shamans and priestesses keep us in touch with our spiritual ancestry and beliefs."
    scene ch6sc02_335 with dissolve
    ec "There is one more job assignment that some fulfill, but we’ll get to that at the end of the tour."
    ec "As you can see, we take pride in our work. No one is idle in our community."
    scene ch6sc02_341 with dissolve
    mc "I understand."
    mc "I also get a little restless if I’ve got nothing to do."
    scene ch6sc02_339 with dissolve
    ec "So, what is it that you do? Where you’re from."
    scene ch6sc02_338 with dissolve
    mc "I’m an Adventurer."
    mc "I take assignments from the guild I’m a member of. Usually, it’s to help people who are in need of assistance."
    scene ch6sc02_339 with dissolve
    ec "Ah, you help people then? That’s an honorable trait."
    scene ch6sc02_338 with dissolve
    mc "I do. But adventuring is more than just helping others."
    mc "I also enjoy discovering places and things. Especially things that are believed to be lost to time, or made up."
    scene ch6sc02_339 with dissolve
    ec "And... as you said earlier, you were told A’nai was a lost city?"
    scene ch6sc02_338 with dissolve
    mc "Yeah. That's what I was told years ago by a traveler..."
    mc "Clearly he was wrong. As you said, your city is not lost... it’s hidden. And thriving from what I can tell."
    scene ch6sc02_332 with dissolve
    ec "I like to believe we are doing well for ourselves."
    scene ch6sc02_333 with dissolve
    mc "Echo, why was that young huntress so bothered by me?"
    mc "She looked directly at me when she said she was distracted."
    scene ch6sc02_332 with dissolve
    ec "Vex? She’s young... just nineteen summers."
    scene ch6sc02_334 with dissolve
    ec "You’re the first outsider she’s ever laid eyes upon. And you're also... the first man she's seen."
    mct "{i}Hmh, so there are no men here at all? Pearl did mention something of the sort.{/i}"
    mc "She’s never seen a man?"
    scene ch6sc02_335 with dissolve
    ec "No. In fact... most of us haven’t. Most of us were newborns or younglings the last time men were here."
    ec "Myself included. I was just five summers at that point."
    scene ch6sc02_341 with dissolve
    mc "If I may, where are all the men? This place... it seems like it would attract plenty of men."
    scene ch6sc02_340 with dissolve
    ec "*Giggles softly* Why? Because it’s filled with scantily clad, beautiful women?"
    scene ch6sc02_341 with dissolve
    mc "Well... yes?"
    scene ch6sc02_332 with dissolve
    ec "We’re a tribe of women. Not only that... the other tribe on Aruna is also female only."
    ec "There is another island a little ways off where all the inhabitants are men, but we don't interact with each other."
    ec "Sour relations in the past."
    ec "Men were banished from Aruna decades ago. Their presence here is forbidden."
    scene ch6sc02_333 with dissolve
    mc "Ah, no wonder your tribe has been giving me the side-eye."
    scene ch6sc02_332 with dissolve
    ec "Mhm. Your presence here is quite unusual. Most of us only know of men from cave drawings, or tales passed down from our mothers."
    scene ch6sc02_333 with dissolve
    mc "I almost can’t believe it... this place..."
    scene ch6sc02_326 with dissolve
    ec "Do you feel I’ve been untruthful with you?"
    scene ch6sc02_327 with dissolve
    mc "No, quite the opposite."
    mc "I think you’ve been completely honest and forthcoming with me. Which I value highly."
    ec "..."
    scene ch6sc02_329 with dissolve
    ec "Yes, I have been honest. And I too, value honesty."
    ec "So, you’ll have to believe me when I tell you there are no other men here... apart from you."
    scene ch6sc02_324 with dissolve
    mc "I’ve heard from others that sailors who venture too close to Aruna have been attacked before."
    mc "Do you really hold no prisoners?"
    scene ch6sc02_325 with dissolve
    ec "No. We of the A'nai tribe distance ourselves from all others... we keep to the jungle."
    ec "Such attacks are committed by the Arugoh tribe. They are the ones we share the island with..."
    scene ch6sc02_330 with dissolve
    ec "They are known to keep men as prisoners, and enslave them even."
    ec "Tsk! Despicable behavior..."
    scene ch6sc02_331 with dissolve
    ec "They aren’t attacking the ships in self-defense... they do it to capture the men."
    ec "They use them for... *Sighs* Let’s banish such indecencies from our minds."
    mct "{i}She doesn't need to say it out loud. I can imagine what they want men for...{/i}"
    scene ch6sc02_334 with dissolve
    mc "So... I really was the first man Vex has seen?"
    scene ch6sc02_377 with dissolve
    ec "Yes. It seems to have been quite a shock to her since you broke her concentration like that."
    ec "She's usually very focused during training."
    scene ch6sc02_378 with dissolve
    ec "They are taught to hone their ability to concentrate, and drilled over many years."
    ec "Of all of us, the huntresses are the ones who venture the furthest from A’nai. So they are the most at risk."
    scene ch6sc02_379 with dissolve
    ec "Their focus and skills are vital for surviving the jungle. Sometimes they stay out hunting for days at a time."
    ec "Furthermore, young ones like Vex are forbidden from entering the Chambers of Malanthe."
    ec "Only once they become a woman at the age of twenty summers are they allowed to partake."
    scene ch6sc02_380 with dissolve
    mc "Chambers of Malanthe?"
    ec "You will learn about it shortly... once our tour is over."
    scene ch6sc02_381 with dissolve
    ec "Behind us, you can see the heart and foundation of A’nai."
    ec "The temple of A’nai. I reside at the very top, as previous A'nus have done before me."
    ec "There are also several entrances to the lower sections of the temple. These lead to the baths, the Priestess' chambers and the Ancestral chambers."
    scene ch6sc02_382 with dissolve
    mc "It’s extraordinary... I’ve never seen architecture like it."
    mc "Who built it?"
    scene ch6sc02_383 with dissolve
    ec "Built what? The temple? The city of A’nai? or-"
    scene ch6sc02_382 with dissolve
    mc "Everything. Temples, city, statues, huts..."
    mc "Who built all this?"
    scene ch6sc02_383 with dissolve
    ec "To our knowledge, everything you see that is made of stone was built by our distant ancestors."
    scene ch6sc02_382 with dissolve
    mc "I see, what about your walls and huts then?"
    scene ch6sc02_384 with dissolve
    ec "Most of the homes and perimeter walls you see are our work, and that of our mothers' generation too."
    ec "We don’t have many experienced builders left. So we make do with what we are still able to accomplish."
    scene ch6sc02_382 with dissolve
    mc "Well your huts are solid, and everything looks well maintained. I’d say you’ve done well."
    scene ch6sc02_383 with dissolve
    ec "Thank you. I’m glad you think so."
    scene ch6sc02_382 with dissolve
    mc "I wonder how your ancestors created something like the temple, though... it’s massive."
    scene ch6sc02_384 with dissolve
    ec "There are certain stories that have been passed down, etched on stone tablets and a few scrolls."
    ec "The construction of the temple is a tale woven with magic."
    scene ch6sc02_385 with dissolve
    mc "Magic? How so?"
    scene ch6sc02_384 with dissolve
    ec "We only have stories at this point. But we believe they had a connection to the Divine Malpheon at the time."
    ec "They worshipped him, and in return, he bestowed on them the knowledge and skills to create such marvels."
    scene ch6sc02_385 with dissolve
    mct "{i}Hmh... fascinating. Given what I know about Lucid, it seems possible that Malpheon could have taken an interest in them.{/i}"
    mc "You said your distant ancestors worshipped Malpheon. What about now?"
    scene ch6sc02_386 with dissolve
    ec "We’ve lost our connection to Malpheon. I’m not sure when it happened. I only know that since the time of our mothers..."
    ec "We’ve only known and worshipped the Trinity of Life."
    scene ch6sc02_385 with dissolve
    mc "Trinity of Life?"
    scene ch6sc02_384 with dissolve
    ec "Mhm. The three Goddesses who have bestowed their blessings on us."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_387 with Dissolve(2.5)
    $ renpy.pause(1)
    ec "Gaia. The Maiden of Life, Prosperity, and Nature."
    scene ch6sc02_388 with Dissolve(2.5)
    $ renpy.pause(1)
    ec "Malanthe. The Maiden of Lust, Desire, and Pleasure."
    scene ch6sc02_389 with Dissolve(2.5)
    $ renpy.pause(1)
    ec "And Maia. The Maiden of Purity, Love and Fertility."
    mct "{i}Ahh, so they worship the same Maia I've met... I haven’t heard of the other two, though.{/i}"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_386 with Dissolve(1.5)
    $ renpy.pause(0.7)
    ec "Our ancestors believed that they can take physical forms and interact with us."
    ec "That they enjoy walking among their followers from time to time."
    mct "{i}Well, I know for certain Maia has a physical form. I’ve met her and felt her touch.{/i}"
    mct "{i}But I wasn't under the impression that she does visitations...{/i}"
    scene ch6sc02_385 with dissolve
    mc "Echo, are there any stories of your ancestors meeting any of these deities themselves? Of interacting with them directly?"
    scene ch6sc02_384 with dissolve
    ec "Not in my lifetime, but... there are rumors from the distant past."
    ec "Elders of our tribe say that once each year, with the rising of the harvest moon..."
    scene ch6sc02_386 with dissolve
    ec "The three celestial maidens used to grace us with their presence and bestow their blessings upon us in person."
    scene ch6sc02_390 with dissolve
    ec "But we haven’t felt their presence since the {b}Great Desecration{/b}."
    ec "Our priestesses and shamans can no longer establish any connection to our goddesses, or our ancestors spirits."
    ec "It’s like all the magic from our past has left us for good."
    scene ch6sc02_382 with dissolve
    mc "{b}The Great Desecration?{/b} What happened?"
    scene ch6sc02_390 with dissolve
    ec "I’m... *Sighs deeply* That isn’t something I’m fully ready to tell you about."
    mc "Of course, my curiosity got the better of me. I apologize if I overstepped."
    scene ch6sc02_383 with dissolve
    ec "You needn't apologize. I quite like your curiosity... I wouldn’t want that to vanish."
    scene ch6sc02_382 with dissolve
    mc "I have to admit... being here, in A’nai, meeting you... I feel like I used to when I was a kid."
    mc "Dreaming of discovering the unknown, finding myself in any magical place my mind could conjure."
    scene ch6sc02_391 with dissolve
    ec "*Giggles softly* I can tell, your eyes are full of wonder and curiosity."
    ec "Just like a child."
    scene ch6sc02_392 with dissolve
    mc "Is that a compliment?"
    ec "..."
    scene ch6sc02_391 with dissolve
    ec "Very much so."
    ec "Wonder and life, curiosity and desire, intimacy and love."
    scene ch6sc02_393 with dissolve
    ec "They all go hand in hand."
    ec "They each make life what it is and truly worth living."
    scene ch6sc02_392 with dissolve
    mc "Mhm. I’d be inclined to agree with that."
    scene ch6sc02_394 with dissolve
    ec "..."
    "Echo shares a gentle smile with you."
    scene ch6sc02_395 with dissolve
    ec "Come, I’m afraid our tour is nearing it’s end."
    mc "Oh? Already?"
    scene ch6sc02_396 with dissolve
    ec "Mh-Hm. There are only two places we’ve yet to visit."
    ec "Believe me, I’ve saved the best for last."
    scene ch6sc02_397 with dissolve
    mc "*Chuckles* Sure, lead the way."
    ec "Sounds like someone is enjoying having their own personal guide."
    mc "I am."
    scene ch6sc02_398 with dissolve
    ec "[mc], please don’t take offense at those who might look at you with contempt or fear."
    ec "They can’t help it. Our past... it’s deeply ingrained in them."
    scene ch6sc02_399 with dissolve
    mc "Mhm. Will you share the reason for that with me?"
    "Echo pauses for a few moments."
    scene ch6sc02_400 with dissolve
    ec "When we reach my bedchamber..."
    ec "Then... I’ll be ready to tell you."

    ####Choice####
    menu:
        "{color=#ff8cdd}Flirt.{/color}":
            scene ch6sc02_401 with dissolve
            mc "Then, I’ll look forward to... visiting your personal chamber."
            ec "..."
            scene ch6sc02_402 with dissolve
            mc "Too forward for your liking?"
            scene ch6sc02_400 with dissolve
            ec "No, worry not. I... understand your intent, completely."
            ec "I share your sentiment. I, too, look forward to you visiting my bedchamber."
            ec "It will mark a significant milestone: the first man to enter my chamber since I became the A'nu."
            scene ch6sc02_398 with dissolve
            ec "The first since... the desecration two decades ago."
            scene ch6sc02_401 with dissolve
            mc "I'm happy to be your first."
            $ ec_trust += 2
            ec "..."
            "Echo enjoys your playfulness and forwardness, trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Don't flirt.":
            scene ch6sc02_399 with dissolve
            mc "Great, I'll look forward to hearing more about your tribe then."

    scene ch6sc02_403 with dissolve
    ec "Come, come."
    ec "Before we see my bedchamber, there is one other location to visit first."
    scene ch6sc02_404 with dissolve
    mc "I’ll admit, I could get used to living here."
    ec "Does A’nai appeal to your... senses?"
    scene ch6sc02_405 with dissolve
    ec "Does seeing the beauties of A’nai stir something within you?"
    mc "Well, yeah. To be honest, it does."
    scene ch6sc02_406 with dissolve
    ec "I do not judge. You have a warrior’s body and... as far as I can tell, a warrior’s spirit."
    ec "It would be strange if you didn't feel something when seeing women like this."
    ec "Not to mention, you’re young, healthy, strong... you’re in the prime of your life."
    scene ch6sc02_407 with dissolve
    mc "You know, you look to be in your prime too."
    mc "Your leadership is obviously respected, you’re young and healthy, you appear to be very intuitive."
    mc "And your beauty stands out, even amongst all these beautiful women."
    scene ch6sc02_409 with dissolve
    ec "Y-You truly think so?"
    scene ch6sc02_408 with dissolve
    mc "Mhm. You’re like a precious gem in a chest filled with coins... or-"
    mc "Like a jewel found in some ancient ruins, unique and rare."
    scene ch6sc02_409 with dissolve
    ec "A jewel... huh..."
    scene ch6sc02_410 with dissolve
    ec "*Giggles softly* That’s... nobody has said anything like that to me before."
    ec "What a silly thing to say... *Giggles*"
    scene ch6sc02_411 with dissolve
    mc "Hey, if you don’t like it... I’ll take it back."
    mc "You can be... Mhm, a rock. A rock in the midst of a sea of rocks in a stone quarry."
    scene ch6sc02_412
    with vpunch
    ec "{b}No!{/b} I refuse to give it back... your compliment belongs to me now."
    ec "*Giggles* I’m keeping it, you hear me!?"
    mct "{i}*Chuckles* So she does have a playful side.{/i}"
    mct "{i}She’s probably so busy being the leader of the tribe that she doesn’t get to display it often.{/i}"
    scene ch6sc02_411 with dissolve
    mc "Fine, I'll let you keep it."
    ec "*Snickers* ..."
    scene ch6sc02_413 with dissolve
    ec "We have arrived."
    ec "The Chambers of Malanthe."
    scene ch6sc02_414 with dissolve
    mm "Well, well, well... this looks interesting."
    mm "What do we have here? A man in A'nai? Who is this man?"
    scene ch6sc02_415 with dissolve
    ec "He’s a guest, my guest... Mistress."
    ec "He found his way to our sacred city. And there’s something about him..."
    scene ch6sc02_416 with dissolve
    mm "Mmm... Yes, I can see why you’d say that."
    mm "He’s practically oozing potential... but-"
    scene ch6sc02_417 with dissolve
    mm "Have you forgotten our rules? The rules of Malanthe’s Chambers?"
    mm "Outsiders... men especially, are not allowed to enter our sacred places."
    scene ch6sc02_418 with dissolve
    ec "I have not forgotten the rules my own mother put in place."
    scene ch6sc02_417 with dissolve
    mc "Rules? What rules?"
    scene ch6sc02_419 with dissolve
    mm "Speak when spoken to, Outsider. Otherwise, be quiet."
    scene ch6sc02_420 with dissolve
    ec "Hey, I told you he’s my guest... take it easy."
    scene ch6sc02_416 with dissolve
    mm "Look at him. I'm sure he can endure a little rough handling..."
    scene ch6sc02_420 with dissolve
    ec "Sakari... I wish for him to be treated well. Any insult to him is an insult to me."
    ec "He has been nothing but kind and respectful towards me and everyone here."
    scene ch6sc02_415 with dissolve
    ec "And... I believe Malanthe’s will dwells inside him."
    ec "He’s no ordinary man. I... I can feel it."
    scene ch6sc02_416 with dissolve
    sk "Mm... is that so? I won’t deny his... appealing stature."
    sk "But what makes you inclined to think so highly of him?"
    scene ch6sc02_420 with dissolve
    ec "He ate several Blacknip berries last night for dinner. And as you can see, he’s up and about."
    ec "And if that's not enough to impress you, it took seven hunting darts to knock him out."
    scene ch6sc02_415 with dissolve
    ec "And he still awoke only a few hours later."
    sk "Hmh... that is impressive. Impossible, even, I would have thought."
    scene ch6sc02_416 with dissolve
    sk "What manner of animal are you, Outsider... Mmm?"
    sk "Perfect."
    scene ch6sc02_420 with dissolve
    ec "Perfect?"
    scene ch6sc02_421 with dissolve
    sk "Yes."
    sk "Banish all your concerns, A’nu."
    sk "He will be treated well. If he truly has the will of Malanthe within him... we will know."
    scene ch6sc02_422 with dissolve
    mc "What do you intend to show me?"
    scene ch6sc02_423 with dissolve
    sk "I will show you all the forms of pleasure you could possibly imagine, if Malanthe has truly blessed you with her grace."
    sk "Or pain, if that is what you desire."
    sk "Then we'll see how deep her desire flows within you."
    scene ch6sc02_422 with dissolve
    mc "If those are my choices, I’m going with pleasure."
    scene ch6sc02_423 with dissolve
    sk "My preferred choice as well. Come now. I’m curious to see what you’re capable of."
    scene ch6sc02_424 with dissolve
    ec "[mc]..."
    ec "When you’ve had your needs met and your desires sated..."
    ec "Come find me at the top of the temple in my personal chambers. This gift is my apology for kidnapping you."
    scene ch6sc02_425 with dissolve
    mc "Thank you, Echo. You’re very generous."
    scene ch6sc02_426
    with vpunch
    sk "Silence, Outsider! You dare speak to her like that?!"
    sk "You said you wanted pleasure? I'm starting to believe you want pain."
    scene ch6sc02_427 with dissolve
    ec "Easy, Sakari."
    ec "I have allowed the outsider- [mc], to call me by my birth name."
    sk "Hnnnrhh... as you wish, A’nu."
    mct "{i}This woman has some pent up... frustrations.{/i}"
    scene ch6sc02_428 with dissolve
    ec "[mc], join me in my bedchamber afterward. I hope you find my gift pleasant."
    mc "I’m sure I will. See you later."
    scene ch6sc02_429 with dissolve
    mc "So... I think I can imagine what this place is, since you named it after the Maiden of Pleasure."
    sk "*Scoffs* ..."
    scene ch6sc02_430 with dissolve
    sk "This place, {b}The Chambers of Malanthe{/b}, is where our tribeswomen come to seek Malanthe’s blessing."
    sk "They give in to their desires, their primal lusts, their longing for pleasure."
    sk "And if their offering is satisfactory, Malanthe may bless them with good health."
    scene ch6sc02_429 with dissolve
    mc "Even though men have been gone for so long?"
    sk "It is true that our ancestors used to have a man partake: the tribe's leader."
    sk "But that is no longer the case."
    sk "Some women seek Malanthe’s guidance alone, while others share their pleasures together."
    scene ch6sc02_431 with dissolve
    sk "Is this a foreign concept to you, Outsider?"
    scene ch6sc02_432 with dissolve
    mc "It’s not something that's common where I’m from. But I’m not opposed to it."
    mc "I’m not here to judge anyone, or your culture. And it’s not like you’ve had any men around recently..."
    scene ch6sc02_431 with dissolve
    sk "*Smirks* Until now..."
    sk "Who knows how things will change with you around?"
    scene ch6sc02_430 with dissolve
    sk "Tell me, what is it that you desire?"
    scene ch6sc02_432 with dissolve
    mc "I’m sure you can imagine."
    sk "*Scoffs lightly* Hmh."
    scene ch6sc02_433 with dissolve
    sk "Follow me. I know exactly what men want."
    mc "How would you know? Echo said there have been no outsiders, no men... in over two decades."
    scene ch6sc02_434 with dissolve
    sk "Stories from the last time have been passed down. Tales of men and their... ways."
    sk "Men such as you. We could hardly forget such... horrors."
    scene ch6sc02_435 with dissolve
    sk "But now is not the time to speak of that. Our A'nu senses something within you."
    sk "It’s time to show you what you can expect, should you wish to devote yourself to Malanthe."
    scene ch6sc02_436 with dissolve
    sk "But keep this in mind: if you harm any of these women- my women..."
    sk "I will personally remove your cock and hang it in a tree for the seagulls to feast upon."
    scene ch6sc02_437 with dissolve
    mc "Duly noted. I don’t plan on hurting anyone."
    sk "..."
    ####Choice####
    menu:
        "There's nothing better than a woman's pleasure. ({color=#87e1fa}Charisma{/color})":
            mc "Nothing is more sacred than a woman's pleasure."
            $ charisma += 1
            mc "A woman's scent during her orgasm is unmatched, as is the taste of her lips."
            scene ch6sc02_436 with dissolve
            sk "You surprise me outsider... hmm."
            "Sakari is pleased with your answer, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch6sc02_437 with dissolve
            mc "I look forward to seeing what you have on offer."


        "I know how to take care of the women I'm with. ({color=#ffee54}Leadership{/color})":
            mc "Your maidens aren't the first women I've enjoyed."
            mc "If I decide to enjoy what they have to offer, they will be well taken care of."
            $ leadership += 1
            scene ch6sc02_436 with dissolve
            sk "Hmm, you seem like quite the man..."
            "Sakari is pleased with your answer, your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch6sc02_437 with dissolve
            mc "I'm intruged to see what you have on offer."

        "Don't worry, I didn't come here to hurt your maidens. ({color=#2bff8b}Persuasion{/color})":
            mc "You and your maidens have nothing to fear from me."
            mc "I'm not here to harm anyone."
            $ persuasion += 1
            scene ch6sc02_436 with dissolve
            sk "Hmm, yes... I do believe your words carry truth within them."
            "Sakari is pleased with your answer, your {b}{color=#2bff8b}Persuasion{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch6sc02_437 with dissolve
            mc "I look forward to discovering what your maidens have to offer."



    scene ch6sc02_438 with dissolve
    sk "Good, I’m trusting you... but only because the A'nu has put her faith in you."
    sk "Tatiana is inside, awaiting company. Today that will be you."
    sk "If you don’t find her to your liking, you can ask her to leave and make an offering to Malanthe on your own."
    sk "Go on, enjoy your gift."
    scene ch6sc02_439 with dissolve
    mc "This should be interesting..."
    scene ch6sc02_440 with dissolve
    tai "Welcome- oh?"
    tai "An outsider and... a man?"
    scene ch6sc02_441 with dissolve
    tai "You must be a legendary warrior if they have let you inside Malanthe’s Chamber."
    mc "You could say that."
    tai "MMmm... I’ve never laid eyes on a man before... but my eyes are pleased."
    scene ch6sc02_442 with dissolve
    tai "Will you show me your spear, great warrior?"
    tai "Will you join me in making an offering of pleasure to Malanthe?"
    scene ch6sc02_443 with dissolve
    tai "I will give you anything you desire..."
    mct "{i}Hmh... I could accept Echo’s gift and enjoy this woman.{/i}"
    mct "{i}Maybe it could be beneficial to be on good terms with this goddess, Malanthe?{/i}"
    mct "{i}I could also ask her to leave and use Onyx to make an offering.{/i}"
    mct "{i}Option three would be to just knock one out solo and be done with it.{/i}"

    ####Choice####
    menu:
        "Make an offering with Tatiana. ({color=#ff8cdd}Scene{/color})":
            scene ch6sc02_445 with dissolve
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            mc "Only a eunuch would deny himself from sharing pleasure with a beauty like you."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            tai "*Snickers* You find me beautiful? Good... it pleases me to know this."
            scene ch6sc02_443 with dissolve
            tai "Let me show you what I have to offer."
            scene ch6sc02_446 with dissolve
            tai "Like what you see, handsome outsider?"
            scene ch6sc02_447 with dissolve
            mc "Mmm... yes. I like what I see."
            mc "You look delicious."
            scene ch6sc02_448 with dissolve
            tai "You can't hold back your urges can you, Outsider?"
            mc "I could..."
            mc "But that wouldn’t be a very satisfying offering for Malanthe, would it?"
            scene ch6sc02_449 with dissolve
            tai "No, she would be very upset..."
            tai "You need not hold back at all."
            tai "Let me fulfill your desires. And you, mine."
            scene ch6sc02_450 with dissolve
            tai "Do with me as you please."
            tai "I want you as much as you want me, possibly more. A man... the first man in decades, inside me? Mmm..."
            scene ch6sc02_451 with dissolve
            mc "Five hells... you’re a little temptress. I’m getting hard just looking at you."
            tai "Show me... let me see your spear, great warrior."
            tai "Let me... let me feel it!"
            scene ch6sc02_452 with dissolve
            mc "*Chuckles* Don’t you worry. You’ll feel it plenty."
            $ tat_path = True
            tai "Come, take me... I can’t wait any longer."
            scene mm_lewd1 with dissolve
            $ renpy.pause()
            tai "Oohh... I feel you... you’re making me feel so hot."
            mc "Damn..."
            tai "W-What is it? Mmm..."
            mc "Your ass feels amazing... the way your smooth cheeks tighten around my tip- MMm..."
            tai "It would feel even better if you were inside me. Malanthe wills it so."
            mc "Then let’s not disappoint her."
            scene mm_lewd2 with dissolve
            $ renpy.pause()
            tai "Oohhmmm... Yessss..."
            tai "You’re so large- Ahhnn... we- we aren’t used to something like this."
            tai "Only fingers or tongues- Ahhh... so- big... and warm."
            tai "Much better than any tools of pleasure we’ve carved from wood."
            mc "Nothing compares to the real thing... a real man."
            tai "I-I believe you! Mm... your statement is truth spoken from experience- AHhh!"
            with vpunch
            tai "There are only a few elders left in A’nai who have had a real man. Mmm... The rest of us? Not so luuuucky..."
            mc "So I’ve heard... lucky for you that I came along."
            with vpunch
            tai "Aiiyhh... yes! I feel blessed by Malanthe with you inside me! Your spear must’ve been carved by her! Aiiyhh!!"
            tai "Take me! Deeper! I want you to fully stretch my wet pussy!"
            scene mm_lewd3 with dissolve
            $ renpy.pause()
            with vpunch
            tai "{b}AAhhhH!{/b}"
            tai "You’re so deep! Ahhh! Your spear so hard and big- MMm! I need it!"
            tai "You must be a true warrior, equipped with a weapon like this! Aiiiyh!"
            mc "Mmh... seems like I’ve caught quite the sexy prey..."
            mc "Maybe they’ll announce me as the first male hunter of A’nai"
            with vpunch
            tai "Yessss... you’ve definitely earned it! AhhH! K-Keep thrusting into me like that! {b}YES!!{/b}"
            with vpunch
            tai "Give it to me! Give me your seed, great warrior! Ahhh!! My offering is reaaaady!! Join me!"
            scene ch6sc02_453
            with vpunch
            mc "F-Fuck! Hnnghh!! You’re so fucking tight-I’m going to- Ahhh!"
            scene ch6sc02_454
            with vpunch
            mc "Aaahh!"
            with vpunch
            tai "AiiiyhH!! Yes! Yes!! I feel your seed!"
            tai "*Panting* So warm... Ahh... Malanthe is pleased with us..."
            mc "Oh, we’re not done... roll over. It’s time you got a taste."
            scene ch6sc02_455 with dissolve
            tai "Mmh... you intend to spear my throat, handsome warrior?"
            tai "While I'm still filled with your seed?"
            mc "That’s exactly what I intend. Now, open wide."
            scene mm_lewd4 with dissolve
            $ renpy.pause()
            mc "You like that, you naughty maiden?"
            mc "I bet you’re loving that there’s finally a proper man in the village, a hunter... hunting you."
            tai "*Muffled* Ahhnghh! Hgrhh! Yesss..."
            tai "*Gasps* Hunt me... use me... let Malanthe’s desire guide us! MMmfhhh!!"
            with vpunch
            tai "I’m your prey- Hnnghhh! Your plaything. My wet mouth is- Mmhmm... *Tightens mouth* yours to enjoy."
            with vpunch
            mc "Fuuu... Mmhm!"
            scene ch6sc02_456
            with vpunch
            tai "*Muffled* {b}MMPFH! MMFHH!! NNNGHH!!{/b}"
            mc "MMmghh! F-Fuck! Tatiana! MMm... your wet little mouth is a den of pleasure."
            tai "*Sucks* Mmh... *Licks* Nnnghh... *Sucks* Mmhh..."
            scene ch6sc02_457 with dissolve
            tai "*Giggles* Mmmm..."
            mc "*Panting* Fuck... that was something else."
            scene ch6sc02_458 with dissolve
            tai "So tasty... I... Malanthe is greatly pleased with you."
            tai "Please, don’t leave already? I... Malanthe needs more."
            scene ch6sc02_457 with dissolve
            mc "Sorry, Tatiana... but you and Malanthe will have to wait. I’m supposed to meet Echo."
            scene ch6sc02_458 with dissolve
            tai "A’nu? She has chosen you?"
            mc "Yeah, so it would seem."
            scene ch6sc02_459 with dissolve
            tai "Goddess... I’ve truly been blessed then."
            tai "To get the honor of pleasuring you... and for you to enjoy me..."
            scene ch6sc02_460 with dissolve
            mc "You were lovely. Maybe I’ll visit you again sometime."
            scene ch6sc02_459 with dissolve
            tai "You must... if A’nu has chosen you... it is my greatest honor and desire to fulfill you."
            tai "I’ll eagerly await our next encounter, handsome warrior. I’m already dripping at the thought of your blessed spear."
            scene ch6sc02_460 with dissolve
            mc "*Chuckles* I look forward to it as well. See you."
            "As you leave the chamber, you can hear the young maiden giggling happily."
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(1)
            $ renpy.pause(1)
        "Make an offering with Onyx. ({color=#ff8cdd}Scene{/color})":
            scene ch6sc02_443 with dissolve
            mc "Your offer is very tempting. I’m sure most wouldn’t refuse. But I didn’t come here for you."
            scene ch6sc02_441 with dissolve
            tai "Say no more, I do not judge. How one wishes to achieve pleasure is their own choice."
            scene ch6sc02_444 with dissolve
            tai "I’ll leave you to it. I hope we’ll get to see each other again..."
            tai "I’m quite... curious about you, Outsider."
            scene black with Dissolve(1)
            "After Tatiana has left the chamber, you call on Onyx."
            scene ch6sc02_461 with Dissolve(1)
            mc "Come on out, Onyx... it’s time for a feeding."
            ox "Oh Master... I love it when you talk dirty to me!"
            scene ch6sc02_462 with dissolve
            ox "MMm..."
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc02_463 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            ox "I feel your presence, Master... I’ve missed being with you in my physical form."
            mc "Mm. I know what you mean. I’ve been looking forward to feeding you again. And in the honor of a goddess, no less."
            scene ch6sc02_464 with dissolve
            ox "*Snickers* We mustn't disappoint her then, Master..."
            ox "You’ll have to stuff me full of your warm essence."
            mc "Come, I want your mouth."
            ox "Of course! Let me position myself for you, Master."
            scene ch6sc02_465
            with vpunch
            ox "MMmfhh!!"
            ox "Mmmm... take my mouth, Master."
            scene ox_lewd1 with dissolve
            $ renpy.pause()
            mc "There it is ... Mhm. I’ve missed this warm, tight mouth of yours, Onyx."
            mc "You feel completely different to humans... so soft and elastic and yet still tight and wet."
            ox "Mmfhh! I love your cock, Master! Feed me! I need your essence!"
            with vpunch
            mc "MMn! I can’t get enough of your tongue... Mmm! The way you can freely shape it and the liquid softness feels- Ahhh!"
            ox "Fill my throat with your warm essence, Master! *Sucks* Mmmfhh! Feed your little symbiote!"
            with vpunch
            scene ch6sc02_466
            with vpunch
            mc "AAahhh! Fuck! Mmmmh!"
            ox "Mmmfhhh... so warm... Mmmhm! So tasty!"
            scene ch6sc02_467 with dissolve
            ox "Thank you, Master. You always fulfill my needs- MMm..."
            mc "Five hells... I don’t know how you do it, but that mouth of yours is like a warm, gooey suction cup."
            ox "I live to serve you and only you, Master. As you know I’ve never been sexual with a host before."
            scene ch6sc02_466 with dissolve
            ox "*Sucks gently* Mmmgh... nnnghh..."
            scene ch6sc02_467 with dissolve
            ox "But I’m glad to be with you... it fulfills me in ways I can’t describe, Mmmm..."
            scene ch6sc02_468 with dissolve
            mc "Yeah... I’m glad we’re able to do this. It deepens our bond and symbiosis."
            ox "It does! I can feel it too, it's such a blissful feeling."
            mc "So, do you think this goddess... Malanthe, is happy with our offering?"
            scene ch6sc02_469 with dissolve
            ox "I’ll speak on her behalf and say yes. The amount of essence you just offered is only possible from true pleasure."
            ox "We'd better get going, you have a meeting with their Queen."
            scene ch6sc02_468 with dissolve
            mc "*Chuckles* Right, better not keep her waiting."
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene black with Dissolve(1)
            $ renpy.pause(1)
        "Make an offering solo. (No Scene)":
            scene ch6sc02_443 with dissolve
            mc "Your offer is very tempting. I’m sure most wouldn’t refuse. But I didn’t come here for you."
            scene ch6sc02_441 with dissolve
            tai "Say no more, I do not judge. How one wishes to achieve pleasure is their own choice."
            scene ch6sc02_444 with dissolve
            tai "I’ll leave you to it, I hope we’ll get to see each other again..."
            tai "I’m quite... curious about you, Outsider."
            scene black with Dissolve(1)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            "You knock one out and make your offering."

    scene ch6sc02_470 with Dissolve(1)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    sk "Well? Did you enjoy our gift?"
    sk "Did you find our services satisfying?"
    scene ch6sc02_471 with dissolve
    mc "Well... why do you ask?"
    scene ch6sc02_470 with dissolve
    sk "I am the Mistress of Malanthe. I am in charge of her Chambers of Pleasure and oversee our maidens."
    sk "And you’re the first outsider and man to visit us and to make an offering to Malanthe."
    scene ch6sc02_472 with dissolve
    sk "So, I’ll ask again. How was your experience in the chambers, Outsider?"
    scene ch6sc02_471 with dissolve
    mc "It was... quite something."
    scene ch6sc02_470 with dissolve
    sk "*Scoffs lightly* Speechless? At a loss for words?"
    scene ch6sc02_471 with dissolve
    mc "I enjoyed it. And so did your goddess."
    scene ch6sc02_472 with dissolve
    sk "Oh? You presume to know her mind? How bold..."
    scene ch6sc02_473 with dissolve
    sk "You will have to return to us. Actions speak louder than words when it comes to fulfilling Malanthe's desires."
    scene ch6sc02_471 with dissolve
    mc "Mhm. We’ll see."
    scene ch6sc02_474 with dissolve
    sk "*Quietly* Perhaps he is different from those in our tales... Hmmm."
    sk "*Quietly* Maybe... maybe I’ll see for myself."
    scene ch6sc02_475 with dissolve
    mc "Hmm?"
    scene ch6sc02_473 with dissolve
    sk "Nothing. I was merely thinking out loud, Outsider."
    scene ch6sc02_472 with dissolve
    sk "You should not keep the A’nu waiting any longer."
    scene ch6sc02_470 with dissolve
    sk "I’m sure we’ll see you soon enough. Today was just an appetizer for what our chambers offer."
    scene ch6sc02_471 with dissolve
    mc "*Chuckles* Bye, Mistress."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_476 with Dissolve(1)
    mc "They’re either on guard around me, or they’re intrigued by me. What am I? Some sort of exotic species?"
    mc "Actually, I suppose that is what I am if the elders are the only ones who have seen another man."
    scene ch6sc02_477 with dissolve
    mc "*Chuckles* The only man in a tribe filled with beautiful women. Flynn would lose his mind here."
    mc "It’ll probably take them a while to get used to me being here."
    scene ch6sc02_478 with dissolve
    mc "Once I find Pearl, maybe we can have ourselves a little vacation here whilst we search for the ambassador."
    mc "I’m not too concerned yet. Pearl and Kira are both capable of fending for themselves and surviving alone."
    mc "And Pearl was alone on Inmortui the entire time. She knows how to survive on an island."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_479 with dissolve
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    "As you stand before the Temple of A’nai, you notice someone is waiting at the top for you."
    scene ch6sc02_480 with dissolve
    "Knowing who awaits you, you begin ascending the many steps effortlessly."
    scene ch6sc02_481 with dissolve
    "Even though Echo told you that magic had been lost to the tribe..."
    "You can clearly feel a powerful magic resonating within the temple."
    scene ch6sc02_482 with dissolve
    "Your eyes remain locked on the beautiful maiden ahead of you, the leader of the A'nai."
    scene ch6sc02_483 with dissolve
    ec "Come to me, [mc]."
    "Echo beckons you to join her with a gentle gesture of her hand."
    scene ch6sc02_484 with dissolve
    ec "Stand beside me and tell me what you see."
    mc "Sure."
    scene ch6sc02_485 with dissolve
    mc "I see..."

    if charisma >= 10:
        scene ch6sc02_486 with dissolve
        mc "A civilization that is thriving despite being cut off from the rest of the world and being thought lost."
        mc "A city that exists in the midst of nature, fully in tune with its environment."
        scene ch6sc02_487 with dissolve
        mc "I see..."
        mc "A culture that is deeply rooted in their history and full of wonders."
        scene ch6sc02_488 with dissolve
        mc "I see a proud people, willful and strong, but caring and protective. People who take care of one another."
        mc "A people who guard their way of life, as they should."
        scene ch6sc02_489 with dissolve
        ec "[mc]... you-"
        ec "You really see all that?"
        scene ch6sc02_490 with dissolve
        mc "Mhm. I do."
        "You had enough {color=#87e1fa}Charisma{/color} to give a response that pleased Echo."
        $ ec_trust += 3
        ec "..."
        "Echo is pleasantly surprised by your in-depth response, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

    else:
        scene ch6sc02_486 with dissolve
        mc "A city in the midst of the jungle..."
        scene ch6sc02_487 with dissolve
        mc "I see... people living their lives."
        scene ch6sc02_489 with dissolve
        ec "*Scoffs* You needn't say anymore... I think I've heard enough."
        $ ec_trust -= 2
        "You didn't have enough {color=#87e1fa}Charisma{/color} to give a response that pleased Echo."
        "Echo is slightly disappointed by your response, her trust has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."


    scene ch6sc02_491 with dissolve
    ec "Come, my bedchamber awaits."
    ec "It’s time for you to hear the darkest tale of the past. Of {b}the Great Desecration.{/b}"
    scene ch6sc02_492 with dissolve
    ec "But first, I wish to know... I am curious-"
    ec "How was your time in the Chambers of Malanthe?"
    mc "It was..."
    scene ch6sc02_493 with dissolve
    ec "Please, be honest with me."
    ec "I wish to know if my gift was well received."
    mc "I enjoyed it. You’ve been very generous to me."
    scene ch6sc02_494 with dissolve
    ec "This pleases me."
    ec "I’m glad you enjoyed my gift."
    ec "I was worried that you might not have been satisfied..."
    scene ch6sc02_495 with dissolve
    ec "I know how Sakari can be."
    ec "She’s a fierce lioness, and her maidens are her cubs."
    ec "I was afraid they’d eat you up whole."
    scene ch6sc02_496 with dissolve
    mc "*Chuckles* Don’t worry, Echo... I can handle myself."
    mc "Nothing like a couple of lionesses to keep a man on his toes."
    scene ch6sc02_497 with dissolve
    ec "*Snickers* I’m glad they didn’t scare you off."
    ec "Please. Sit with me."
    scene ch6sc02_498 with dissolve
    mc "Your bedchamber is lovely."
    scene ch6sc02_499 with dissolve
    ec "Thank you. I wanted us to have some privacy to get to know one another better."
    scene ch6sc02_498 with dissolve
    mc "Yeah, the tour was great. But I prefer privacy too, if I'm honest."
    mc "So, how come you were so curious about my experience in the chambers?"
    scene ch6sc02_499 with dissolve
    ec "Oh... I... well, it sort of ties into our ancestry and our beliefs."
    scene ch6sc02_500 with dissolve
    ec "You see, there is a leader for each role in our society: Huntresses, Priests, Maidens, Herbalists, and Guards."
    scene black with Dissolve(1)
    $ renpy.pause(0.5)
    scene ch6sc02_501 with Dissolve(1)
    ec "For Huntresses, that leader is Kisha, the Head-Huntress."
    scene ch6sc02_502 with Dissolve(1)
    $ renpy.pause(0.5)
    ec "For our Priests it’s Marah, the High-Priestess."
    scene ch6sc02_503 with Dissolve(1)
    $ renpy.pause(0.5)
    ec "For Maidens it’s Sakari, the Mistress of Malanthe."
    scene ch6sc02_504 with Dissolve(1)
    $ renpy.pause(0.5)
    ec "For the Herbalists, it’s Sewah, Chief-Herbalist."
    ec "Although Sewah isn't with us at A'nai currently, long story."
    scene ch6sc02_505 with Dissolve(1)
    $ renpy.pause(0.5)
    ec "And for the Guards and War-Maidens it’s Riven, Grandhuntress."
    ec "She too, is currently not present in A'nai..."
    scene ch6sc02_498 with dissolve
    mc "So, each role or group within your tribe has a leader assigned to it?"
    scene ch6sc02_499 with dissolve
    ec "Correct. And I... as the A’nu... I suppose I would be considered a Queen, where you’re from."
    ec "I am the highest authority within the tribe, but I rarely have to use my authority."
    scene ch6sc02_500 with dissolve
    ec "It’s important to appoint good leaders for each group, because they oversee and handle the tasks given to their members."
    scene ch6sc02_498 with dissolve
    mc "I see, that’s quite smart."
    mc "We have a similar system where I’m from, although on a larger scale, and with more conflicting interests."
    mc "We have groups of people that we call guilds. They function a little like your role groupings, albeit with some differences."
    scene ch6sc02_499 with dissolve
    ec "Right. Earlier, I believe you said you were part of an 'Adventurer’s guild?'"
    scene ch6sc02_506 with dissolve
    mc "Yeah. So... you were explaining your curiosity about my visit to the Chamber of Malanthe?"
    scene ch6sc02_499 with dissolve
    ec "Right... as I was saying, none of the leaders, including myself as the A’nu..."
    ec "Participate in the pleasures that the Chamber of Malanthe provides the rest of the tribe."
    scene ch6sc02_498 with dissolve
    mc "Oh? How come?"
    scene ch6sc02_500 with dissolve
    ec "It is forbidden."
    ec "Each leader is saving herself for..."
    scene ch6sc02_506 with dissolve
    mc "For?"
    scene ch6sc02_500 with dissolve
    ec "For our next {b}A'khan{/b} to emerge."
    scene ch6sc02_499 with dissolve
    ec "Our histories teach that, someday, a great champion will arise."
    ec "And when he does, he will claim A’nai as his tribe, and become it’s {b}A'khan{/b}."
    ec "A King, in your speech."
    scene ch6sc02_500 with dissolve
    ec "So, it's important that our leaders remain pure for him."
    scene ch6sc02_506 with dissolve
    mc "I see..."
    scene ch6sc02_498 with dissolve
    mc "So, you’ve never...?"
    scene ch6sc02_507 with dissolve
    ec "I... I’ve done... things, on my own."
    ec "To prepare for the day he emerges."
    mct "{i}*Chuckles* She’s getting a little shy? I guess I was being a little too direct.{/i}"
    scene ch6sc02_506 with dissolve
    mc "I understand, whoever that man is... he is in for a treat."
    scene ch6sc02_508 with dissolve
    ec "A-Anyways... I think it’s time for you to hear about our past."
    ec "You said you wanted to know what happened? Why there are no men among us?"
    scene ch6sc02_509 with dissolve
    mc "I do ... it piques my interest. But I can tell that it troubles you."
    mc "I can wait."
    scene ch6sc02_510 with dissolve
    ec "It does pain me to think about it, but you need to know if you wish to understand us."
    ec "If we continue to hold on to our pain, to blame all outsiders for what happened years ago..."
    ec "Then... we’ll never heal our wounds."
    scene ch6sc02_511 with dissolve
    ec "Those who suffered and endured the desecration must be remembered and honored."
    ec "It all started when I was only a newborn. I hadn’t even learned to walk yet."
    scene ch6sc02_512 with dissolve
    ec "You see... at the time, we had an A’khan. He was kind, brave and strong."
    ec "Those were peaceful times. Aruna, our island was unified then. We all lived here in A’nai. One big tribe."
    scene ch6sc02_509 with dissolve
    mc "The A’khan, was he the one who built this temple?"
    scene ch6sc02_499 with dissolve
    ec "No, no. As I said, this temple is ancient."
    ec "It was built long ago by our ancestors."
    scene ch6sc02_511 with dissolve
    ec "There are many old temples and ruins scattered throughout Aruna and its jungles."
    scene ch6sc02_510 with dissolve
    ec "The temple we’re in right now is the heart of A’nai."
    ec "It is one of four, large ancient temples on the island."
    ec "Each of the three Goddesses that we worship has a temple dedicated to her."
    ec "And then there’s this one."
    scene ch6sc02_511 with dissolve
    ec "We believe that this was the very first temple."
    ec "Built to honor the old ways by the followers of Malpheon."
    scene ch6sc02_510 with dissolve
    ec "The other three temples are believed to have been built soon after, using knowledge that Malpheon had bestowed upon the tribe."
    scene ch6sc02_511 with dissolve
    ec "The temple of Maia is in the territory of the Arugoh tribe, who we share the island with."
    scene ch6sc02_499 with dissolve
    ec "But the temple of Malanthe and the temple of Gaia have both been lost to the jungle, nobody in our generation has seen them."
    ec "As for the Temple of Maia, it is located further to the north, deep within the jungle."
    scene ch6sc02_498 with dissolve
    mc "Imagine uncovering them..."
    scene ch6sc02_499 with dissolve
    ec "If only it were possible. Even for us, the jungle is mysterious and can be both... a refuge and a danger."
    scene ch6sc02_498 with dissolve
    mc "Echo, what happened to divide the tribe in two?"
    scene ch6sc02_499 with dissolve
    ec "During the peaceful times that our A’Khan provided, Aruna island became known for its ancient culture and exotic goods."
    scene ch6sc02_513 with dissolve
    ec "We were prosperous in our dealings with others. The variety of fruits from the jungle were popular both for medicine and making alcohol."
    ec "Nobles from the mainlands prized those wines for their potency and their sweet taste."
    ec "But after a few good years of prosperity... it all came to an end."
    scene ch6sc02_511 with dissolve
    ec "During the early days of trading with the outside world, our A'khan allowed sailors to take refuge here."
    ec "And as all men have desires... they made an arrangement with our A'khan to be allowed to..."
    scene ch6sc02_512 with dissolve
    ec "... 'enjoy' the Chambers of Malanthe, and its maidens. But only if the maidens willingly accepted the men."
    ec "Those were the terms that our A'khan set, and in return the sailors could trade freely with A'nai."
    ec "Unfortunately, some of the outsiders grew vile and aggressive towards our maidens, sometimes ending in physical abuse."
    scene ch6sc02_511 with dissolve
    ec "Our A'khan did not take this lightly."
    ec "Once he learned about these transgressions, he immediately terminated the deal with the outsiders."
    ec "It seemed to work. After a while, the sailors stopped visiting A'nai."
    scene ch6sc02_512 with dissolve
    ec "The greed of men... our joy was short-lived."
    scene ch6sc02_511 with dissolve
    ec "One day, a few men from an unknown land arrived seeking aid after being shipwrecked."
    scene ch6sc02_512 with dissolve
    ec "But they arrived under false pretenses."
    ec "They tricked our great A’Khan... they tricked all of us."
    ec "We allowed them into the midst of A’nai, we gave them shelter, provided aid and food..."
    scene ch6sc02_511 with dissolve
    ec "Weeks went by, and they established relations within the tribe. After a time, we let our guard down."
    ec "But these men had not shipwrecked at Aruna by chance, it was intentional."
    scene ch6sc02_509 with dissolve
    ec "..."
    scene ch6sc02_510 with dissolve
    ec "How naive... how hopelessly foolish we were."
    ec "One night, they managed to light a beacon and we didn’t notice before it was too late."
    scene ch6sc02_511 with dissolve
    ec "Suddenly, we were set upon by many men."
    ec "We outnumbered them, but they were able to overpower us due to their treachery."
    scene ch6sc02_512 with dissolve
    ec "The group we'd been aiding had insisted on a celebration that evening..."
    ec "And many of our people had over-indulged in the sweet alcohol and were in no shape to fight."
    scene ch6sc02_513 with dissolve
    ec "[mc]... we were attacked from within, betrayed by those who had gained our trust."
    ec "The people we had only sought to aid... turned into monsters."
    ec "They captured our guards and huntresses first, and after that we were powerless when they seized the temple."
    scene ch6sc02_510 with dissolve
    ec "What happened next was... {b}The Great Desecration{/b}."
    ec "Our... oppression."
    scene ch6sc02_511 with dissolve
    ec "They killed our A’Khan by brutally beating him to death in front of the whole tribe."
    ec "It is told that the wails of our tribeswomen could be heard all over Aruna that night."
    scene ch6sc02_510 with dissolve
    ec "Everyone was imprisoned here in the Great Temple of A’nai. They ransacked the lower sections and then turned it into a prison."
    ec "Nothing was sacred to these men, they broke the statues we built to honor the gods."
    scene ch6sc02_514 with dissolve
    ec "They beat anyone that earned their ire..."
    ec "But... but that wasn’t enough for them..."
    ec "It only took a few days for the beatings to become increasingly brutal. And the men... their urges were unleashed."
    ec "*Clenches teeth* The women of A’nai were mercilessly brutalized and raped. That is the true horror our tribe suffered."
    scene ch6sc02_510 with dissolve
    ec "Those sick bastards reveled in the pleasures of the flesh, not given freely but taken forcefully."
    ec "It is told by our elders that they were relentless."
    ec "Night after night the cries and screams of women being taken against their will filled the city."
    ec "The darkest hour of A'nai had come."
    scene ch6sc02_509 with dissolve
    mc "Echo, I’m... that’s horrible. I’m so sorry for what your tribe suffered."
    ec "*Nods* ..."
    scene ch6sc02_510 with dissolve
    ec "My mother, who was A’nu before me, was now widowed... but she bided her time, together with a few others who still had the strength."
    scene ch6sc02_511 with dissolve
    ec "They used the intruders own tactics against them and slowly earned their trust."
    scene ch6sc02_512 with dissolve
    ec "Eventually, they learned their routines, and gained a little more freedom outside the temple cells."
    ec "They needed to act swiftly and decisively, and so they struck one night when the men had been drinking heavily."
    scene ch6sc02_511 with dissolve
    ec "They brought secretly crafted wooden weapons to the pleasure session that night..."
    scene ch6sc02_510 with dissolve
    ec "And killed the men there while they were vulnerable."
    ec "Then they snuck around the village in the dark, quietly slaying any that they found sleeping."
    scene ch6sc02_512 with dissolve
    ec "Soon, they were able to retake our homes, and the remaining outsiders were all put to the spear."
    scene ch6sc02_513 with dissolve
    ec "They now suffer in the most wretched of hells, I’m certain!"
    ec "Months of torture, violence, and rape was finally over for our people ..."
    scene ch6sc02_514 with dissolve
    ec "*Exhales deeply* But reclaiming what had been lost came with a heavy price."
    ec "Most of our best war-maidens had been killed in the initial attack."
    ec "And many others lost their lives to the ongoing brutality of the abuse and rape."
    ec "My mother... she fell that night, too. The tribe's victory cost us both our A'khan and A'nu."
    scene ch6sc02_509 with dissolve
    mc "Echo..."
    mc "You don't have to say any more."
    mc "I can tell its taking its toll on you."
    scene ch6sc02_510 with dissolve
    ec "It is alright."
    ec "I- I must tell it."
    scene ch6sc02_511 with dissolve
    ec "After the gruesome event was behind us, the tribe was never the same."
    ec "Some women were unable to endure their traumas."
    ec "Those ones left to go into the jungle, never to return."
    scene ch6sc02_512 with dissolve
    ec "And a growing discontent amongst the survivors here in A’nai grew worse over time."
    scene ch6sc02_513 with dissolve
    ec "Eventually, about half the tribe broke away and formed their own Tribe, the Arugoh."
    ec "They settled to the north side of A'nai."
    ec "Those who remained here in A’nai all agreed to hide ourselves away from the outside world."
    ec "We forbade all outsiders from entering our territory, especially men."
    scene ch6sc02_512 with dissolve
    ec "But the Arugoh felt this approach was too lenient."
    ec "They believed outsiders should be enslaved in the same way that had been done to us."
    ec "That all outsiders were evil."
    scene ch6sc02_509 with dissolve
    mct "{i}Then the one who attacked our ship has to be from the Arugoh tribe.{/i}"
    scene ch6sc02_510 with dissolve
    ec "They believe in attacking first, and I can’t honestly fault their reasons."
    scene ch6sc02_511 with dissolve
    ec "But, we don’t wish to carry such hatred."
    ec "Instead, we chose to distance ourselves from the outside world."
    scene ch6sc02_512 with dissolve
    ec "Most of the younger women in the tribe today, myself included, never suffered the horrors of that time."
    ec "I was only four or five summers when it happened, and most of the others you see around A'nai today were also too young."
    ec "But our remaining elders did have to endure it."
    ec "And they have taught us all the tales of the desecration."
    scene ch6sc02_513 with dissolve
    ec "Which is why many are so wary of you."
    ec "Both because you're an outsider and a man."
    ec "You'd need to earn their respect, by proving yourself."
    scene ch6sc02_498 with dissolve
    mc "All that makes sense, but..."
    mc "Haven't there been any boys born into your tribe?"
    scene ch6sc02_499 with dissolve
    ec "After the trauma that men had brought upon our tribe, the elders who took charge after my mother’s passing-"
    ec "-Decided that the boys would be sent to the neighboring island, to join the male tribes there."
    scene ch6sc02_513 with dissolve
    ec "And since no man has been here since... there have been no newborns for two decades."
    ec "*Sighs* No more of this, not tonight."
    ec "Discussing this has taken its toll on me."
    scene ch6sc02_509 with dissolve
    mc "Hey, it's fine... Echo, you’re fine."
    mc "You’ve shared more with me than I could've expected... I had no idea your tribe had such a horrible past."
    scene ch6sc02_500 with dissolve
    ec "*Nods* Have I answered all your questions, then?"
    scene ch6sc02_506 with dissolve
    mc "You have, Echo."
    mc "Thank you for trusting me."
    scene ch6sc02_507 with dissolve
    ec "You’re different, [mc]... an outsider, true."
    ec "But you don’t harbor ill intent towards us... I can feel it."
    scene ch6sc02_506 with dissolve
    mc "I promise you, I don't have any bad intentions."
    mc "Once I find my friend, Pearl... if you would allow us to, I’d love to stay a bit and get to know more about you."
    scene ch6sc02_508 with dissolve
    ec "A-About me?"

    ####Choice####
    menu:
        "Yes, about you. ({color=#ff8cdd}Romance{/color})":
            scene ch6sc02_506 with dissolve
            mc "Yes, Echo... I’d like to learn more about you."
            $ ec_trust += 2
            mc "You’re beautiful, strong, kind... getting to know you seems like something I’d enjoy."
            "Echo is pleased with your compliment, her trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            if leadership >= 11:
                scene ch6sc02_507 with dissolve
                ec "*Shyly* It's getting a little hot in here..."
                scene ch6sc02_506 with dissolve
                mc "*Chuckles* Was it something I said? I just thought I'd be straightforward with you."
                mc "One leader to another."
                scene ch6sc02_508 with dissolve
                ec "At first I wasn't sure what to think about you, but you do seem like a capable leader."
                ec "You're quite interesting! Genuine... strong... curious..."
                $ ec_trust += 2
                "Echo likes that you're coming across as a strong leader, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                scene ch6sc02_507 with dissolve
                ec "[mc]... I- I’m interested-"

            else:
                scene ch6sc02_507 with dissolve
                ec "[mc]... I- I’m interested-"

        "Yes, and about your tribe. ({color=#2bff8b}Friendly{/color})":
            scene ch6sc02_506 with dissolve
            mc "Yeah, I’d love to know more about your tribe, and your culture."
            scene ch6sc02_500 with dissolve
            ec "Oh... yeah, I’m glad you’re interested in us. I’d allow you to sta-"

    scene ch6sc02_515 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    with vpunch
    uk "Outsider! You dare trespass in our city and sacred temple?!"
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_515 with dissolve
    mc "*Whispers* {size=-10}{b}She seems nice.{/b}{/size}"
    scene ch6sc02_516 with dissolve
    ec "High-Priestess Marah..."
    ec "What are you doing in my bedchamber?"
    scene ch6sc02_517 with dissolve
    mh "What is this... this man... this outsider doing in your sacred bedchamber, A’nu?"
    mh "And why is his devilish tongue so intimate with your name?"
    scene ch6sc02_518 with dissolve
    ec "I’ve allowed him to use my name, he is my guest... Marah."
    ec "And, his name is [mc]... not outsider."
    scene ch6sc02_519 with dissolve
    mh "Do you not remember our suffering? The horrors we had to endure?"
    mh "The softened version of {b}our{/b} past you just told this... outsider, does not reflect the true horror."
    scene ch6sc02_520 with dissolve
    mh "Tsk! Outsider! Do you wish to hear what really happened?"
    scene ch6sc02_521 with dissolve
    mc "I have a feeling you’ll tell me either way..."
    scene ch6sc02_520 with dissolve
    mh "Right you are... Let me enlighten you."
    mh "What A’nu has told you was true, but she neglected to tell you how truly horrific it was."
    scene ch6sc02_518 with dissolve
    ec "I didn't feel it necessary to share every vile detail with him."
    ec "He understands enough of the tale."
    scene ch6sc02_519 with dissolve
    mh "And, why would you feel that way? Why would you spare him all the details?"
    scene ch6sc02_522 with dissolve
    ec "Because... he is nothing like them."
    ec "[mc] is respectful and kind!"

    if leadership >= 11:
        ec "He is a strong leader, I can sense it..."
        ec "He's a Captain! Of a great ship called the Bloody Banshee!"

    else:
        ec "And he's..."

    ec "He is curious, he is filled with wonder, and he wishes to learn about us, Marah."
    scene ch6sc02_519 with dissolve
    mh "How quickly you forget!"
    mh "He only fakes it in order to conquer us!"
    scene ch6sc02_520 with dissolve
    mh "Outsiders only know of conquest and inflicting pain."
    mh "They will enslave us again if we give them the chance."
    scene ch6sc02_523 with dissolve
    mh "Our great A’Khan was slain like a beast!"
    mh "They didn’t just beat and brutalize him in front of everyone. No..."
    scene ch6sc02_524 with dissolve
    mh "They learned that he had a wife, Echo’s mother."
    mh "So they brought her to him and commanded her to stab him to death with a dull blade."
    scene ch6sc02_522 with dissolve
    ec "High-Priestess!"
    scene ch6sc02_519 with dissolve
    mh "He must hear it to truly understand."
    scene ch6sc02_520 with dissolve
    mh "Of course, she refused to commit this horrific crime against the man she loved."
    scene ch6sc02_523 with dissolve
    mh "So, to force our beloved queen, our A’nu, to commit this terrible act, they dragged out a woman from the tribe."
    mh "They threw her down next to our A’Khan..."
    mh "They beat her, and raped her into the dirt. And for each hour that our Queen refused-"
    scene ch6sc02_524 with dissolve
    mh "-Another women would be brought out... and so it went on."
    mh "Our queen wept in horror at the choice she faced."
    mh "She knew that killing her beloved, her husband, her A’Khan..."
    mh "The father of her child... was the only way to stop her tribe from suffering."
    scene ch6sc02_523 with dissolve
    mh "Our A'khan was barely able to speak after his brutalization."
    mh "But he pleaded with her to kill him and spare the women."
    mh "The whole village bore witness to it all."
    mh "She finally took the dull dagger and shakily tried to stab Echo’s father."
    scene ch6sc02_525 with dissolve
    ec "Please... no more."
    ec "He... he understands."
    scene ch6sc02_520 with dissolve
    mh "Luckily, Echo was only a youngling nearing her fifth summer."
    mh "So she wasn't brought out to witness the horror."
    mh "Our queen’s first attempt at stabbing her husband failed."
    mh "The blade was so dull, and her strength and determination was lacking."
    scene ch6sc02_523 with dissolve
    mh "So, another woman was brought out..."
    mh "And it began again."
    scene ch6sc02_520 with dissolve
    mh "Our A'nu screamed in agony as she thrust the blade harder into her husband’s chest."
    mh "This time, piercing the skin."
    scene ch6sc02_523 with dissolve
    mh "But the usurpers just laughed and shouted at her to try again, while they continued to assault the woman next to her."
    scene ch6sc02_524 with dissolve
    mh "Her husband kept yelling at her to just do it, to end it. And she stabbed him again."
    mh "*Mimics* {b}'Again, do it again, bitch! Finish him! Once more!'{/b}... they yelled these things even as they abused the women."
    mh "Eventually, her eyes glazed over, and her weeping stopped, and she stabbed her husband over and over again."
    scene ch6sc02_523 with dissolve
    mh "Until she was left stabbing only a lifeless corpse."
    mh "The stabbing didn’t stop until she couldn’t lift her arm anymore."
    mh "And then, to everyone's horror... the bastards didn’t stop!"
    mh "They kept taking turns on the woman next to our queen."
    scene ch6sc02_520 with dissolve
    mh "The whole village wept as we witnessed what you outsiders are capable of!"
    scene ch6sc02_525 with dissolve
    ec "Marah, no more... please."
    mh "Worry not, sweet Echo. The tale is over."
    scene ch6sc02_519 with dissolve
    mh "I will not let this man harm you or anyone else in our tribe."
    scene ch6sc02_520 with dissolve
    mh "Outsider, come."
    mh "Now that you know our history, it’s time you saw it for yourself."
    scene ch6sc02_521 with dissolve
    mc "See what?"
    scene ch6sc02_523 with dissolve
    mh "The dungeons below the temple..."
    mh "Nobody has had the strength to restore them to their former purpose. There is too much... pain."
    scene ch6sc02_524 with dissolve
    mh "A’nu, Outsider... come."
    scene ch6sc02_525 with dissolve
    ec "L-Let's go..."
    scene black with Dissolve(1)
    $ renpy.pause(0.7)
    "And so you and Echo follows Marah down into the depths of the temple."
    scene ch6sc02_526 with Dissolve(1)
    $ renpy.pause(0.7)
    mc "*Whispers* {size=-10}{b}Echo... what is this place?{/b}{/size}"
    scene ch6sc02_527 with dissolve
    ec "*Quietly* {size=-10}{b}Sshh... [mc], do not speak... not here.{/b}{/size}"
    ec "*Quietly* {size=-10}{b}These are the sacred halls of the temple that were turned into our prison.{/b}{/size}"
    scene ch6sc02_528 with dissolve
    mh "This is where we used to worship the goddesses, to pray for their guidance and blessings."
    mh "One of our most sacred places, now defiled by outsiders... desecrated beyond recognition."
    scene ch6sc02_529 with dissolve
    mh "Your kind doesn’t belong here. You shouldn’t be allowed anywhere near this place."
    mh "But our A’nu, Echo, she insists that you learn about us. And so you shall. With your own eyes."
    scene ch6sc02_530 with dissolve
    mh "See the conditions that we suffered! That we were subjected to!"
    mh "Witness what your kind does! What was done to us!"
    scene ch6sc02_531 with dissolve
    mh "Tormented... kept in cages like animals... only taken out when they..."
    with vpunch
    mh "When they wanted to do... horrible... perverse things to us."
    scene ch6sc02_532 with dissolve
    mh "Hours became days, days became weeks, moons came and passed... no end to being their playthings!"
    mh "We vowed to never let it happen again."
    mh "That those we lost would not have died in vain."
    scene ch6sc02_533 with dissolve
    mh "Echo’s mother was only a shell of her former self after what she endured..."
    mh "But, after several months, she somehow found the strength to rally the others. We finally managed to reclaim our freedom and home."
    mh "She saved us all. She even saved me..."
    mh "I was 26 summers at the time... The night of our rebellion was the first time-"
    scene ch6sc02_531 with dissolve
    mh "I had been removed from my cage."
    mh "They had decided it was my time to become their... plaything."
    mh "I was fortunate enough that they speared the man just before he had his way with me."

    if charisma >= 11:
        scene ch6sc02_532 with dissolve
        mc "Marah, I'm sorry for what happened to your people all those years ago."
        mc "Some people are scum, who will take advantage of others."
        mc "Doesn't matter if they were born on the mainland or on an island."
        scene ch6sc02_531 with dissolve
        mh "Hmph, on that we can agree."
        $ mh_charm = True
        mh "But if you think-"
        mc "I know what kind of man I am, I did not come here to harm anyone."
        mc "I didn't even know this place existed until I woke up in a tent here... chained."
        scene ch6sc02_533 with dissolve
        $ mh_trust += 1
        mh "*Scoffs* Your words..."
        "Marah detects a sliver of truth in your words, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
        mh "No! Your words are venomous!"
        mh "We lost our precious A'nu... we lost nearly half the tribe..."

    else:
        scene ch6sc02_532 with dissolve
        mc "Marah, I'm sorry for what happened to your people all those years ago."
        mc "I agree some 'outsiders' would have bad intentions if they found your tribe."
        mc "But I'm not-"
        scene ch6sc02_531 with dissolve
        mh "'But you're not like them'? *Scoffs* Do you think us fools!?"
        "Your {color=#87e1fa}Charisma{/color} was too low to gain any trust from Marah."
        mh "We lost our precious A'nu... we lost nearly half the tribe..."


    scene ch6sc02_532 with dissolve
    mh "Now her daughter, our A'nu, is too eager to forget the past and has allowed you inside our home."
    scene ch6sc02_534 with dissolve
    ec "Marah, I do not forget the past, but I also don’t desire to live trapped within it."
    ec "Things are not the same, time has passed, decades..."
    scene ch6sc02_533 with dissolve
    mh "Nothing has changed! He’s an outsider!"
    scene ch6sc02_534 with dissolve
    ec "He comes with good intentions, he is not like the ones from our past."
    scene ch6sc02_531 with dissolve
    mh "How can you be so sure of that?"
    mh "You have only known this man for a day!"
    scene ch6sc02_534 with dissolve
    ec "Because... he and I have talked."
    ec "We’ve spoken a great deal since his arrival... I believe he has a pure heart."
    scene ch6sc02_535
    with vpunch
    mh "*Laughs in disbelief* Hahahah! You can’t possibly be that naive?"
    scene ch6sc02_536 with dissolve
    mh "Outsiders are demons... wolves dressed up as sheep."
    mh "They only speak lies... their true intentions shrouded in shadows."
    scene ch6sc02_537 with dissolve
    mh "Outsider, do you know what their leader said just before we drove our spears through him?"
    mc "I don’t imagine he had anything nice to say?"
    mh "*Scoffs* No, he certainly didn’t."
    scene ch6sc02_538 with dissolve
    mh "He vowed he'd return to finish what he had started... to finish conquering us."
    mh "To enslave us and take away our freedom forever."
    scene ch6sc02_534 with dissolve
    ec "Marah, you saw him die with your own eyes."
    ec "His corpse was burned... you cannot believe that he can return."
    scene ch6sc02_538 with dissolve
    mh "Whether he returns in his physical form, or as a spirit disguised in another form, I am certain that his malign will endures."
    mh "His will to defile and dominate, to desecrate and ruin, it lives on in this outsider!"
    scene ch6sc02_539 with dissolve
    mh "Letting them enslave us, letting them destroy our sacred temple and ruin our tributes to the goddesses... it’s a bad omen."
    mh "Why else did the magic abandon our people after the desecration? We’ve been cursed."
    scene ch6sc02_540 with dissolve
    mh "Yet, you still bring an outsider to our very home."
    mh "You ignore the curse put on us? Do you seek to have the past repeat itself?"
    mh "Naive child! If only you had been older when it happened, then you would take it more seriously."
    scene ch6sc02_541
    with vpunch
    ec "{b}Marah!{/b} I’m no child and you’re overstepping!"
    scene ch6sc02_542 with dissolve
    mh "Outsider... come, there is something else you must see."
    mh "The one place they didn’t manage to defile, our last sacred place... is tucked away."
    scene ch6sc02_543 with dissolve
    mh "See the shimmering light from the tunnel? Our last remnant of the past."
    mh "Since we’re breaking tradition, you might as well see it for yourself."
    scene ch6sc02_541 with dissolve
    ec "Marah, what is the meaning of thi-"
    scene ch6sc02_544 with dissolve
    mc "Hmm, I do sense magic flowing up from inside this shaft..."
    mh "If you will not protect our tribe, I will!"
    scene ch6sc02_545
    with vpunch
    ec "{b}[mc]!!{/b}"
    "You manage to dodge her shove. But she flings opens her palm... releasing a powdery cloud into your face."
    scene ch6sc02_546
    with vpunch
    mc "*Cough* What the... *Cough*"
    scene ch6sc02_547
    with vpunch
    ec "{b}[mc]!!{/b}"
    scene ch6sc02_548 with dissolve
    mc "Hnnghh... what the? Can’t... move..."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_549 with Dissolve(1)
    ec "Marah! What manner of evil has taken hold of you?"
    ec "What... what have you done?!"
    scene ch6sc02_550 with dissolve
    mh "I did what you should have done yourself! He was an outsider..."
    mh "Naive girl."
    scene ch6sc02_551
    with vpunch
    ec "Hold your venomous tongue!"
    ec "You forget who you’re talking to! You’re in no position to speak to me like that."
    ec "Especially after what you’ve just done!"
    scene ch6sc02_552 with dissolve
    mh "*Scoffs* Has this outsider... this man... already corrupted your mind?"
    mh "Has your respect for me and my opinion really been dissolved this swiftly?"
    scene ch6sc02_553 with dissolve
    ec "You have served me faithfully. You even taught me a great deal after my mother’s passing..."
    ec "But you are the one lacking respect."
    ec "And this lack of respect, lack of trust..."
    scene ch6sc02_554 with dissolve
    ec "I'm your A’nu."
    ec "It has brought this man to his death... a good man."
    scene ch6sc02_555 with dissolve
    mh "Possibly... we both know where that tunnel leads."
    scene ch6sc02_556 with dissolve
    ec "The depths of A’nai, once used to determine the worth of an A’khan."
    scene ch6sc02_555 with dissolve
    mh "You may see him again, if the goddesses will it so."
    mh "I severely doubt it, though."
    scene ch6sc02_554 with dissolve
    ec "Marah, for your sake... I hope he returns to us unharmed."
    scene ch6sc02_552 with dissolve
    mh "I am sorry to undermine you, but you know I have our tribe's wellbeing at heart."
    mh "This had to be done, believe me."
    mh "Good man or not, he was a threat, a risk... one that we cannot afford to take."
    scene ch6sc02_553 with dissolve
    ec "I'll be in my chambers."
    ec "I suggest you go pray to the goddesses and hope they hear you."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene tunnel_1 with Dissolve(1)
    "As your consciousness returns, you feel yourself sliding down a seemingly endless corridor that is illuminated with an ominous red light."
    mc "Marah... that fucking bitch... she surprised me with some sort of powder."
    mc "I was making good progress with Echo until that hag came along."
    "Suddenly you reach the end of the tunnel. Unable to stop your momentum, you go flying through a dense fog wall."
    scene black with Dissolve(1)
    $ renpy.pause(0.5)
    scene ch6sc02_557 with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene tunnel_2 with dissolve
    $ renpy.pause(3.6, hard=True)
    scene ch6sc02_558
    with vpunch
    ox "Don’t worry, Master! I’ve got you!"
    mc "Thanks. For some reason I couldn’t use my wind abilities to cushion the landing..."
    mc "Now that I think about it, I haven’t felt my magic since arriving here on Aruna."
    mc "The only magic I’ve felt was what drew me towards A’nai. But Echo claims their magic is lost."
    scene ch6sc02_559 with dissolve
    ox "Maybe it’s connected? Whatever has caused their magic to disappear, maybe it's also disrupting yours?"
    scene ch6sc02_560 with dissolve
    mc "That’s likely the case... But this place is filled with magical presence, and it seems you’re functioning fine?"
    scene ch6sc02_559 with dissolve
    ox "You forget, Master... I’m not just magical. I’m part of your being. Just like your hands, feet, and nose."
    scene ch6sc02_560 with dissolve
    mc "Good to know that you’re not so easily vanquished."
    mc "However, if something is powerful enough to eliminate magic, or at the very least subdue it across the entire island..."
    mc "That’s going to be troublesome, to say the least."
    scene ch6sc02_559 with dissolve
    ox "Didn’t they say that they lost touch with their magic after the desecration? After their enslavement?"
    ox "It sounds like they think they've angered their gods, but I’ve never heard of gods interfering in this way with mortals."
    ox "The most they usually do is to imbue an artifact with magic, or bestow a temporary blessing on their followers."
    ox "But to remove magic entirely, or subdue it? I've never heard of such a thing."
    scene ch6sc02_560 with dissolve
    mc "Mhm, yeah... Maia said something like that too. I don’t think it’s anything to do with angering their gods."
    mc "My guess is those men who tried to enslave A’nai are at the root of it. Maybe they did something? Or it could be the Arugoh tribe."
    mc "One of them attacked our ship with magic, so they must still have access to it. It could be that they're responsible."
    scene ch6sc02_559 with dissolve
    ox "Right now, all we can do is guess. Which won’t help much down here."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_560 with dissolve
    mc "You’re right... let’s take a look around."
    play music mystery_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_561 with dissolve
    mc "I came from up there, through that thick red fog."
    mc "Given how long it took, and the speed I was sliding, we’re a long... long way below the temple."
    mc "*Sighs* It’s going to be one hell of a trek to get out of here, if it's even possible."
    scene ch6sc02_562 with dissolve
    mc "This place looks ancient... does Echo and her tribe even know it exists?"
    mc "And these statues..."
    scene ch6sc02_563 with dissolve
    mc "They’re lit by some sort of red light coming from their basins. Funny, the tunnel had dim red light as well."
    mc "There’s definitely magic emanating from this temple. It’s even making my skin tingle."
    scene ch6sc02_564 with dissolve
    mc "Question is, why? Why build this so far below the surface? Was it to hide it?"
    mc "Ancient civilizations often built their burial chambers, treasure troves and religious offerings deep below ground."
    mc "Probably to protect and hide them from raiders. Huh? There’s a different light coming from over there."
    scene ch6sc02_565 with dissolve
    mc "Staying here in this chamber won’t do much good anyway..."
    mc "I might as well check it out."
    scene ch6sc02_566 with dissolve
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    mc "The magical presence feels stronger here..."
    scene ch6sc02_567 with dissolve
    #play music mystery_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Definitely increasing as I get closer to the blue light... what’s going on?"
    scene ch6sc02_568 with dissolve
    mc "A fog wall? How ominous..."
    mc "Should I enter?"

    ####Choice####
    menu:
        "No! Absolutely not! Fuck no! I know how this story goes!":
            scene ch6sc02_568 with dissolve
            mc "*Sighs* I really can’t be bothered but... it’s either this or wither away down here..."

        "Enter through the fog... I’m not a bitch.":
            scene ch6sc02_568 with dissolve
            mc "How bad could it be?"

    scene ch6sc02_569 with dissolve
    $ renpy.pause(1)
    mc "Woah... it feels strange: cool to the touch."
    scene black with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_570 with Dissolve(1)
    $ renpy.pause(1)
    scene ch6sc02_571 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_572 with dissolve
    $ renpy.pause(1)
    mc "*Coughs* Damn... should’ve taken a deep breath before coming through."
    scene ch6sc02_573 with dissolve
    mc "That’s... not creepy at all."
    mc "There’s something in this room. I can feel a presence."
    scene ch6sc02_574 with dissolve
    $ renpy.pause(1)
    mc "What the... self-lighting fires?"
    with vpunch
    uk "*Echoing Rumble* ..."
    scene ch6sc02_575
    $ renpy.pause(1)
    with vpunch
    uk "*Echoing Rumble*  ..."
    mc "The sounds are coming from that... thing at the end of the hall."
    scene ch6sc02_576 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mc "That’s no ordinary statue... it’s..."
    scene ch6sc02_577 with dissolve
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    with vpunch
    uk "*Echoing Rumble* ..."
    scene ch6sc02_577 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_578 with dissolve
    mc "A golem? ... Must've been enchanted by whoever built this place."
    scene ch6sc02_579 with dissolve
    $ renpy.pause(1)
    mc "*Exhales* Well, I’ve been itching to punch something ever since that... Marah appeared."
    scene ch6sc02_580 with dissolve
    $ renpy.pause()
    scene ch6sc02_581
    with vpunch
    uk "*Roaring rumble* Rhooohrhhh!"
    scene black
    with vpunch
    $ renpy.pause(0.5)
    with vpunch
    $ renpy.pause(0.5)
    scene ch6sc02_582 with Dissolve(1)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "One punch? Really? *Sighs* Disappointing."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mc "I suppose he was put here to thrash potential raiders, not oppose a Nephilim."
    scene ch6sc02_583 with dissolve
    mc "Speaking of raiders... that looks like the door to a treasury if ever I saw one."
    scene ch6sc02_584 with dissolve
    mc "It looks ancient... and massive..."
    mc "I wonder how long it's been here? Was it a part of the temple, or was it built long before?"
    scene ch6sc02_585 with dissolve
    mc "Whoever built this place must’ve been giants ... or maybe they used enchanted golems like the one guarding this place as workers."
    mc "These glyphs inscribed on the door... probably a language lost to time."
    scene ch6sc02_586 with dissolve
    mc "Maybe it's a warning telling me not to touch this conveniently placed handle?"
    mc "Ancient tombs and traps usually go hand in hand, after all."
    scene ch6sc02_587 with dissolve
    mc "Onyx, be a dear...?"
    ox "Master! I can’t believe you'd use me this way! *Fake sobbing* I’ve been downgraded to a mere trap decoy!"
    scene ch6sc02_588 with dissolve
    mc "Calm down. We both know this won’t kill you..."
    ox "*Fake weeping* It’s the thought that counts!"
    scene ch6sc02_589
    with vpunch
    ox "{b}OWH!!{/b}"
    mc "Are you hurt?"
    ox "No. *Snickers* You know blades can’t hurt me."
    mc "*Sighs* ... just open the damn door, you drama-oozeling."
    "The handle clicks a few times as Onyx twists it, then a loud thump is followed by a final click."
    scene ch6sc02_590 with dissolve
    ox "That should do it, Master."
    mc "Good job, Onyx. You’re not too shabby at this adventuring stuff."
    "The door begins to rumble..."
    scene tunnel_3 with dissolve
    $ renpy.pause(4.6, hard=True)
    scene ch6sc02_591
    ox "Woah! Master... this is incredible! We’re rich!!"
    mc "Easy... we don’t know if there are any more traps inside."
    mc "And we won’t be able to get all of this out of here anyway."
    scene ch6sc02_592 with dissolve
    mc "Woah... I’ve never seen this much loot in one treasury..."
    mc "This must have been gathered over centuries."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_593 with dissolve
    play music mystery_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Huh? What’s that..."
    mc "A... necklace? It’s levitating? It must be an effect of the magic surrounding it."
    mc "It’s similar to the fog wall I went through."
    scene ch6sc02_594 with dissolve
    mc "There’s no mistaking it..."
    mc "This is the feeling that was drawing me towards A’nai when I was in the jungle."
    mc "Out there it was faint, I could barely feel it."
    mc "But here... being this close, it makes my skin tingle."
    scene ch6sc02_595 with dissolve
    ox "Careful, Master... what if it's a dark object?"
    ox "Maybe it's the thing that is subduing magic?"
    mc "No... this doesn’t feel like a trap."
    mc "It feels... fated."
    scene ch6sc02_596 with dissolve
    ox "Fated? There’s no such thing!"
    mc "I can’t explain it, Onyx."
    mc "It’s just the feeling I get. Like it’s safe... like it was meant for me, or for someone like me."
    scene ch6sc02_597 with dissolve
    "As you get closer and your hand approaches the floating talisman, it’s soothing aura reaches out to meet you."
    mc "Woah... its reacting to me?"
    mc "Let’s see if I can absorb this essence."
    scene ch6sc02_598 with dissolve
    "As you guessed, the essence merges with you as you come into contact with it."
    mc "It's working."
    scene ch6sc02_599 with dissolve
    mc "Incredible... I feel... stronger? More... durable?"
    mc "Strange, that usually only happens when I absorb the lifeforce of enemies I’ve defeated."
    scene ch6sc02_600 with dissolve
    mc "Let’s see what this necklace is all about."
    scene ch6sc02_601 with dissolve
    mc "It’s heavy... way heavier than something this size should be. I don’t think an average human could possibly lift it."
    mc "Maybe that was the purpose of the magical essence surrounding it? To allow whoever finds it to be its wielder?"
    mc "Might as well try it on..."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_602 with Dissolve(2)
    $ renpy.pause()
    mc "I feel stronger..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_603 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "Onyx... do you feel this as well?"
    ox "Yes... you were right, Master."
    ox "It is... fated."
    scene ch6sc02_604 with dissolve
    mc "It feels like it’s part of me now. Just like you?"
    mc "I... absorbed the essence it was imbued with."
    ox "Could this be... no, surely not?"
    mc "What?"
    scene ch6sc02_605 with dissolve
    ox "Could it be an artifact of the Divines?"
    ox "Echo said their ancestors were followers of Malpheon?"
    scene ch6sc02_606 with dissolve
    mc "Right... the more recent generations worship {b}The Celestial Trinity{/b} of Gaia, Malanthe and Maia."
    mc "But way back when A’nai was first founded..."
    scene ch6sc02_605 with dissolve
    mc "They were followers of Malpheon... one of the seven divines, just like Lucid."
    mc "If this is an artifact from the Divines, then it would explain why it feels so... powerful."
    scene ch6sc02_606 with dissolve
    mc "It gives me the same vibe as when I’ve been in the presence of Lucid."
    mc "Familiar and... right?"
    mc "It just feels... right."
    scene ch6sc02_605 with dissolve
    mc "When I put it on, I felt myself gain the affinity for Earth-magic."
    mc "And these wisps? It’s like they’re alive, but also part of me somehow?"
    scene ch6sc02_606 with dissolve
    mc "But I still feel unable to do any magic..."
    scene ch6sc02_607 with dissolve
    ox "Rats! Then this can't be the magic dampener that we suspected."
    mc "Looks like I’m able to control the wisps, though. I can freely send them back into the necklace."
    ox "Great! But we've still got a magic problem to grapple with."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_608 with dissolve
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    mc "Don’t worry, Onyx... we’ll figure it out."
    mc "Let’s grab a few gems and see if we can find a way out."
    scene ch6sc02_609 with dissolve
    ox "Ooohh... nicking a few ancient and possibly incredibly valuable gems? I love it when you’re being naughty!"
    mc "*Chuckles* Right... there’s no reason to leave empty-handed from a place like this. We’ll need plenty of coin back home."
    scene ch6sc02_610 with dissolve
    mc "Hmh? A chain?"
    scene ch6sc02_611 with dissolve
    mc "Let’s see... I doubt it's a trap, we’re already inside the treasury."
    scene ch6sc02_612 with dissolve
    "As you pull the chain, a rumbling can be heard from the hallway."
    $ renpy.pause(0.5)
    with vpunch
    mc "Did you feel that? Something shifted in the other room."
    ox "Don’t just stand there, Master... let’s check it out!"
    scene ch6sc02_613 with dissolve
    mc "Looks like the fog wall changed color. Guess that’s our way forward."
    ox "Into the unknown we go!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Going through the wall of fog once more, you encounter a long, winding corridor punctuated with faint red lights."
    "You follow it for well over an hour..."
    #play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_614 with Dissolve(2)
    $ renpy.pause(1)
    mc "By the Divines... this is..."
    scene ch6sc02_615 with dissolve
    mc "These carvings... the intricate stonework and statues..."
    mc "This has to be older than the Temple of A’nai that is built on top of it."
    mc "When was the last time a living being walked these halls?"
    scene ch6sc02_616 with dissolve
    mc "My guess is... it must date back to the first Era."
    mc "Which makes it over a thousand years old."
    scene ch6sc02_617 with dissolve
    mc "Hmh... looks like... beasts? Dragons?"
    ox "Dragons were not very common in my time, but they were still more widespread than they are today."
    scene ch6sc02_618 with dissolve
    mc "A throne? ... What is that doing down here?"
    mc "Was this built by an underground civilization? Or has this temple sunken below ground over the ages?"
    scene ch6sc02_619 with dissolve
    mc "These statues... they’re the same as the ones in the ruins I first fell into."
    scene ch6sc02_620 with dissolve
    mc "*Chuckles* Might as well..."
    scene ch6sc02_621 with dissolve
    mc "Imagine... ruling a whole civilization..."
    mc "It does have a certain... appeal."
    scene ch6sc02_622 with dissolve
    mc "*Exhales* But I’m busy enough as it is, with all that’s going on back home."
    mc "Can’t imagine the amount of work it would take to keep a whole civilization in line and happy."
    scene ch6sc02_623 with dissolve
    mc "Huh? Something shifted behind the throne?"
    ox "Maybe it's a secret passage? Back in my day, rulers often had escape tunnels in their bedchambers or throne rooms."
    mc "Let’s have a look."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss8 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_624 with Dissolve(2)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ki "What do you mean 'you’re fully aware that they haven’t responded?!'"
    scene ch6sc02_625 with dissolve
    di "Don’t make me repeat myself."
    scene ch6sc02_624 with dissolve
    ki "But they were supposed to send a raven once they arrived at Aruna! We haven’t heard anything in days!"
    scene ch6sc02_625 with dissolve
    di "Kira, I have more important things to worry about than your boyfriend and your sister."
    scene ch6sc02_626 with dissolve
    di "We have to establish a whole new infrastructure and logistics center here in Looter’s Bay."
    di "Besides, [mc] went toe to toe with me and lived to tell the tale. He's the only person to ever accomplish that."
    scene ch6sc02_625 with dissolve
    di "I think he can handle whatever Aruna throws at them."
    scene ch6sc02_624 with dissolve
    ki "Let me go... let me retrieve them."
    scene ch6sc02_627 with dissolve
    di "You’re my only insurance that they won’t just run off into the sunset."
    di "[mc] made a deal with me. I'm handling things here while he handles the ambassador situation. I intend to uphold my end."
    scene ch6sc02_626 with dissolve
    di "Upon returning with the ambassador, the charges of piracy against you and Pearl will be dropped."
    di "Now, if you made yourself useful and helped me organize everything here..."
    scene ch6sc02_625 with dissolve
    di "We’d get it done sooner. And if [mc] and your sister still haven't returned by then, we can go look for them."
    scene ch6sc02_624 with dissolve
    ki "Tsk! ... what do you need from me?"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss12 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_524 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mh "A’nu... you need to forget the outsider..."
    mh "We will not see him again. Your people need you to be out amongst them. Not hiding away up here..."
    scene ch6sc02_522 with dissolve
    ec "It’s been seven hours! I think our people can handle their responsibilities as usual."
    ec "If you believe there’s anything special they need to be doing, go and instruct them to do it yourself."
    scene ch6sc02_628 with dissolve
    mh "A’nu..."
    mh "Has this... outsider... really corrupted you so deeply already?"
    mh "Will you abandon your duties as our A’nu, as the leader who guides us?"
    scene ch6sc02_629 with dissolve
    ec "No, he has not corrupted my mind. He was sweet and kind, curious and respectful..."
    ec "I wished to know more about him."
    ec "But I will never choose an outsider over our tribe. You know that!"
    scene ch6sc02_630 with dissolve
    ec "Yet, here you come before me..."
    ec "Questioning my honor? My allegiance to our home?"
    scene ch6sc02_631 with dissolve
    mh "A’nu... Echo... *Sighs*"
    mh "I know my actions have hurt you... that I went against your wishes."
    scene ch6sc02_632 with dissolve
    ec "*Scoffs* Hffh..."
    scene ch6sc02_631 with dissolve
    mh "I know my choice has soured our bond... damaged our trust."
    scene ch6sc02_630 with dissolve
    ec "Yes, you have."
    ec "You went against my will. You attacked my guest."
    scene ch6sc02_631 with dissolve
    mh "I did it for you, for our tribe, for us all-"
    scene ch6sc02_633 with dissolve
    ec "*Scoffs* Don’t say you did it for everyone. You only did it for yourself!"
    ec "Because of your past experiences."
    scene ch6sc02_634 with dissolve
    ec "The only outsider who escaped back then, he is long dead!"
    ec "He wouldn’t survive decades on his own in the jungle. And he certainly has nothing to do with [mc]!"
    scene ch6sc02_631 with dissolve
    mh "And what if he escaped the jungle?"
    mh "What if he has spent decades planning to come back and finish what was started?"
    scene ch6sc02_635 with dissolve
    mh "This [mc]... he's probably his lackey who he brought here to seduce us."
    mh "And when we lower our guard..."
    mh "Just like last time, they'll come in force to conquer us!"
    scene ch6sc02_631 with dissolve
    mh "I have every right not to trust outsiders!"
    mh "Echo, this [mc]... he is just like them! I know it!"
    scene ch6sc02_635 with dissolve
    mh "Had we given him the opportunity, he would happily have enslaved us. History would have repeated!"
    scene ch6sc02_636 with dissolve
    ec "Despite your years and wisdom, Marah..."
    ec "You’re not a shaman, nor are you a farseer."
    ec "You are only a priestess. You cannot claim to know his heart."
    scene ch6sc02_635 with dissolve
    mh "I’m... I’m well aware that I’m no farseer, but you don’t need to be one to know that outsiders are bad!"
    scene ch6sc02_636 with dissolve
    ec "Why are you here? Why have you come to see me?"
    scene ch6sc02_631 with dissolve
    mh "I desired to check up on you, A’nu... to make sure you remain strong as ever."
    mh "To ensure the outsider has not caused too much terror."
    if mh_charm == True:
        mh "His words... they nearly had me convinced, that's how dangerous he is!"
        mh "If he can convince me, he would be able to have all of A'nai eating out of his palm, tsk!"

    else:
        pass

    scene ch6sc02_634 with dissolve
    ec "My head is in the right place, if that’s what you’re asking me."
    ec "My duties as A’nu, as the leader of our people, are my reason to live."
    scene ch6sc02_633 with dissolve
    ec "If you think to question that again... may the goddesses have mercy on you then."
    scene ch6sc02_637 with dissolve
    mh "My A’nu... I meant no disrespect. I will take my leave and seek redemption from the goddesses."
    mh "I will not have our trust broken."
    mh "I can only hope they will guide me upon a path of mending."
    scene ch6sc02_638 with dissolve
    ec "..."
    scene ch6sc02_639 with dissolve
    ec "*Quietly* {size=-10}{b}This is the first time she has betrayed me... is her fear of outsiders so deeply rooted?{/b}{/size}"
    ec "*Quietly* {size=-10}{b}[mc]... I’m sorry I never got the chance to know you.{/b}{/size}"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_640 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "After following the passage from the throne room for hours, you finally see daylight."
    scene ch6sc02_641 with dissolve
    $ renpy.pause(0.5)
    mct "{i}Finally! I’m not sure how long I was down there for, but the sun is setting.{/i}"
    scene ch6sc02_642 with dissolve
    mct "{i}*Inhales deeply* Aaahh...{/i}"
    mct "{i}The jungle air feels so fresh after being stuck in the dusty, ancient tomb.{/i}"
    scene ch6sc02_643 with dissolve
    mct "{i}I’m never taking fresh air for granted again...{/i}"
    scene ch6sc02_644 with dissolve
    mct "{i}Huh? The wisps are reacting to something?{/i}"
    mct "{i}Let’s see what it’s leading me to.{/i}"
    scene ch6sc02_645 with dissolve
    $ renpy.pause(0.5)
    mc "What's up, little guy? Where are you taking me?"
    scene ch6sc02_646 with dissolve
    mc "Huh? Is someone back there?"
    mc "I think I can see someone behind the pillar."
    mc "Whoever is back there, make yourself known. I’m not in the mood for games."
    scene ch6sc02_647 with dissolve
    pl "[mc]...?"
    pl "*Shaky voice* Is that... is it really you?"
    scene ch6sc02_648 with dissolve
    mc "Pearl? Pearl, is that you?"
    mc "Come, it’s okay. You’re safe now."
    scene ch6sc02_649
    with vpunch
    pl "MMffhh... [mc]... *Voice cracks* I-I couldn’t find you!"
    scene ch6sc02_650 with dissolve
    mc "Ssh-Shh... it’s okay, I’m right here."
    mc "First, are you okay? Are you hurt?"
    scene ch6sc02_649 with dissolve
    pl "Hurt? N-No ... I think I’m fine."
    scene ch6sc02_651 with dissolve
    mc "You don’t look fine, you’re covered in dirt and grime."
    mc "And your feet are freezing ..."
    scene ch6sc02_652 with dissolve
    pl "It’s okay... I’m okay... you’re nice and warm."
    mc "I’m glad I found you, I know you’re fully capable of handling yourself, but I was a little worried..."
    scene ch6sc02_653 with dissolve
    mc "But what are you doing here?"
    mc "How’d you know where I was?"
    scene ch6sc02_654 with dissolve
    pl "I didn’t... I’ve been hiding. This place seemed nice and sheltered."
    pl "I was about to look inside that tunnel when I heard someone coming out, so I hid here not knowing what was going on."
    scene ch6sc02_653 with dissolve
    mc "It’s a blessing that you’re okay and unharmed."
    mc "You have no clue how happy I am to see you."
    scene ch6sc02_655 with dissolve
    pl "Me too, [mc]... I’m so happy to have found you."
    pl "I-I thought I’d never see you again..."
    scene ch6sc02_656 with dissolve
    mc "Now, that’s crazy talk..."
    mc "You know I’d be searching this jungle through and through for you."
    scene ch6sc02_655 with dissolve
    pl "Really?"
    scene ch6sc02_656 with dissolve
    mc "Yeah... I don’t want to face Kira’s wrath if I return without you."
    scene ch6sc02_658 with dissolve
    pl "*Giggles* Ass..."
    scene ch6sc02_659 with dissolve
    mc "You said you were hiding? What from?"
    scene ch6sc02_660 with dissolve
    pl "Yeah... when I woke up, I... I felt like I was being watched."
    scene ch6sc02_661 with dissolve
    pl "And sure enough, when I found some running water, an arrow flew right by my head when I bent down to quench my thirst."
    scene ch6sc02_660 with dissolve
    pl "So I legged it straight into the jungle..."
    pl "I lost my attackers, but I also lost my own bearings."
    scene ch6sc02_655 with dissolve
    pl "I’ve been wandering around aimlessly ever since, looking for a safe spot to huddle up."
    scene ch6sc02_657 with dissolve
    pl "Huh, what’s this thing?"
    mc "It’s a necklace or talisman of some sort... I found it deep inside that ruin I emerged from."
    scene ch6sc02_656 with dissolve
    mc "It seems to have some magical properties, and it linked with me when I put it on."
    scene ch6sc02_655 with dissolve
    pl "*Sighs* Okay..."
    scene ch6sc02_656 with dissolve
    mc "*Chuckles* Just, okay?"
    scene ch6sc02_661 with dissolve
    pl "I’m too exhausted to be able to think about strange magical artifacts right now."
    scene ch6sc02_659 with dissolve
    mc "Yeah, let’s get you out of here. The sun is setting and we don’t want to be stuck in the jungle at night."
    scene ch6sc02_660 with dissolve
    pl "Where are we going? Did you find some shelter?"
    scene ch6sc02_659 with dissolve
    mc "I may have befriended the locals."
    scene ch6sc02_662 with dissolve
    mc "Well... some of them. I’d say half want me dead, and the other half seem... interested?"
    pl "..."
    scene ch6sc02_663 with dissolve
    pl "Locals... the ones that were hunting me?!"
    scene ch6sc02_662 with dissolve
    mc "No. Apparently, there are two separate tribes inhabiting the island."
    mc "The semi-friendly ones from A’nai, and then the ones who probably shipwrecked us and were hunting you."
    scene ch6sc02_659 with dissolve
    mc "The Arugoh tribe."
    scene ch6sc02_663 with dissolve
    pl "So, we’re seeking shelter with the tribe where only half of them want us dead?"
    scene ch6sc02_659 with dissolve
    mc "*Chuckles* When you say it like that, it sounds like a bad idea."
    mc "But they aren’t that terrible, they're just very cautious about outsiders."
    mc "And... I was told they have baths."
    scene ch6sc02_664 with dissolve
    pl "*Exhaustedly* Hnnghh... I can’t believe I’m risking my life for a bath... *Sighs* but I can’t deny the appeal."
    mc "Here, lean on me and I’ll get us there."
    scene ch6sc02_665 with dissolve
    pl "How do you even know where we’re going?"
    pl "Did you suddenly become King of the Jungle or something?"
    scene ch6sc02_666 with dissolve
    mc "*Chuckles* Who knows...?"
    mc "But this artifact, somehow it makes me feel in tune with the jungle."
    scene ch6sc02_667 with dissolve
    mc "*Language of the Ancients* Asha, locah A’nai."
    scene ch6sc02_668
    pl "What the? Since when do you speak the tongue of the Ancients?"
    scene ch6sc02_666 with dissolve
    mc "I don’t know... I was just telling the wisps to guide us to A’nai... and it came out like that."
    scene ch6sc02_668 with dissolve
    pl "I’ve only heard Father use that language before... when he was researching ancient artifacts."
    pl "It took him years with his nose buried in ancient texts to learn a few sentences."
    scene ch6sc02_666 with dissolve
    mc "This artifact must have taught me the language, or something."
    mc "C’mon, we’ll follow the wisp. It’ll lead us to A’nai."
    scene ch6sc02_669 with dissolve
    pl "Y-Yeah... okay."
    pl "A bath and a bed would be really nice..."
    mc "You’ll have both. Their leader was welcoming towards me, I’m sure she will be to you as well."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "About an hour of trekking through the undergrove of the jungle you arrive at the gates of A'nai."
    scene ch6sc02_670 with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mc "We’re here."
    pl "I can’t believe that wisp of yours took us directly here..."
    scene ch6sc02_671 with dissolve
    sj "Is that...?"
    sj "How did he...?"
    scene ch6sc02_672 with dissolve
    zy "By the goddesses, it is him!"
    zy "Looks like he has a woman with him too."
    scene ch6sc02_673 with dissolve
    sj "Get the A’nu! She’ll want to see this... swiftly!"
    scene ch6sc02_674 with dissolve
    zy "I’ll be as swift as a leopard hunting its prey."
    scene ch6sc02_675 with dissolve
    sj "She’ll be pleased..."
    sj "Everyone was shocked when Marah proclaimed the outsider dead earlier."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_676 with Dissolve(1.5)
    $ renpy.pause(0.5)
    with vpunch
    zy "{b}A’nu!!{/b}"
    scene ch6sc02_677 with dissolve
    ec "Yes, Huntress?"
    ec "Why are you out of breath? Did you sprint up all the stairs to my chamber?"
    scene ch6sc02_678 with dissolve
    zy "Yes! Like a leopard, I bring news! There is something you must see!"
    zy "Your eyes will think it a dream."
    scene ch6sc02_679 with dissolve
    ec "Can't Marah handle this?"
    ec "I’m not feeling well today... I just want to be alone."
    scene ch6sc02_678 with dissolve
    zy "I must insist, A’nu. You will not wish for Marah to handle this."
    zy "You will quite surprised. Pleasantly so, even!"
    scene ch6sc02_680 with dissolve
    ec "Oh? Is that so? Well, I suppose I’ll have to see it, then."
    ec "Lead me to this pleasant surprise, Huntress."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_681 with Dissolve(1.5)
    $ renpy.pause(1)
    sj "What happened? Why did you come from the jungle, and with... another outsider?"
    mc "As I said, your high-priestess... Marah... pushed me down a tunnel inside the temple."
    scene ch6sc02_682 with dissolve
    sj "Marah did that? She committed an act of violence against a guest?"
    sj "Hmm... that is anything but honorable."
    sj "You might be an outsider, but A’nu made it clear you were a guest and wanted you treated well."
    scene ch6sc02_683 with dissolve
    mc "Your high-priestess seems very paranoid. She was telling me about your people's past..."
    mc "Then she led us down into the once-sacred chamber, which was turned into a prison."
    mc "She tricked me into looking down a tunnel shaft and attacked."
    mc "I managed to dodge her initial shove, but she had some kind of powder that knocked me out."
    scene ch6sc02_682 with dissolve
    sj "Typical... just like high-priestesses of the past."
    scene ch6sc02_683 with dissolve
    mc "They have a history of being snakes?"
    sj "*Nods*"
    scene ch6sc02_684 with dissolve
    sj "Mhm, they are second-in-command, directly below the A’nu."
    scene ch6sc02_682 with dissolve
    sj "Cunning, ambitious, ruthless... venomous women."
    scene ch6sc02_684 with dissolve
    sj "You’ll want to be careful with her."
    scene ch6sc02_683 with dissolve
    mc "Noted."
    scene ch6sc02_684 with dissolve
    sj "So, you made it back here after being pushed into the underground?"
    scene ch6sc02_683 with dissolve
    mc "Yeah. At first I slid down a long, twisting tunnel that was dimly lit by some red light."
    scene ch6sc02_685 with dissolve
    mc "At the end of the tunnel there was a fog-barrier that I fell right through. And I ended up in a large underground ruin."
    "The huntress observes you carefully as you recount these events."
    scene ch6sc02_686 with dissolve
    mc "It looked ancient... really ancient. And once again it was lit up by a red atmosphere."
    scene ch6sc02_685 with dissolve
    mc "And it had these large, faceless statues, and they were holding... what looked like basins?"
    scene ch6sc02_686 with dissolve
    mc "After getting my bearings, I noticed a place with a different colored light. More of a teal hue. So I went to investigate."
    scene ch6sc02_685 with dissolve
    mc "It led me to another fog-barrier, this time in the shape of a door. When I went through it, I found myself in a different hall."
    scene ch6sc02_686 with dissolve
    mc "I fought off a guardian golem and found myself in a treasury filled with gold, gemstones, relics and..."
    scene ch6sc02_687 with dissolve
    sj "This... the necklace you’re wearing. You didn’t have it when I saw you last."
    sj "Amazing, you’re a... Nobody has ventured into the deep ruins and returned."
    scene ch6sc02_688 with dissolve
    mc "Nobody?"
    sj "None in my lifetime, at least."
    sj "You’re the... only one."
    scene ch6sc02_687 with dissolve
    sj "I’m not sure what this means, but it feels... important."
    sj "You must show it to our A’nu."
    scene ch6sc02_689 with dissolve
    sj "She’ll know."
    scene ch6sc02_690 with dissolve
    mc "I will. I trust her a great deal, she has been genuine with me."
    scene ch6sc02_691 with dissolve
    sj "Hmh... you’re interesting, Outsider."
    sj "There’s something special about you... something... primal."
    scene ch6sc02_690 with dissolve
    mc "Is that so?"
    scene ch6sc02_691 with dissolve
    sj "Yes, I feel it. Your energy, it’s... brave and powerful. You made it through the depths of A’nai unscathed."
    mct "{i}*Chuckles* I wonder if that’s all she’s feeling... I know that look.{/i}"
    scene ch6sc02_689 with dissolve
    sj "I believe... you’re on the path, Outsider."
    scene ch6sc02_690 with dissolve
    mc "The path?"
    scene ch6sc02_689 with dissolve
    sj "Mmm... {b}The Path of A’khans{/b}. The man who was promised..."
    scene ch6sc02_691 with dissolve
    sj "Our legends tell that, one day, a great warrior will arise among us..."
    sj "And his will, his determination, his power, his... primal energy will overshadow all previous A'khans."
    scene ch6sc02_692 with dissolve
    sj "A-Anyway..."
    sj "I’m glad you’ve managed to find your friend and that she appears to be in good health."
    scene ch6sc02_693 with dissolve
    mc "Yeah, it was pure luck I managed to find her."
    sj "Echo... the A’nu, while you were in the Chambers of Malanthe, she asked us to keep an eye out for your friend."
    mc "Really?"
    sj "*Nods* Mhm. The jungle is dangerous and she commanded we bring her back here immediately upon finding her."
    scene ch6sc02_682 with dissolve
    sj "The jungle is a blessing and a curse... a shield and a trap."
    scene ch6sc02_683 with dissolve
    mc "Yeah, nature does not discriminate. It gives and it takes."
    scene ch6sc02_684 with dissolve
    sj "Exactly... it’s all a matter of perspective."
    scene ch6sc02_681 with dissolve
    sj "Handsome, strong... and wise?"
    sj "You are a triple threat, [mc]."
    scene ch6sc02_685 with dissolve
    mc "You seem quite wise yourself."

    ####Choice####
    menu:
        "Compliment her.":
            scene ch6sc02_691 with dissolve
            sj "Thank you..."
            scene ch6sc02_686 with dissolve
            mc "And beautiful, too."
            mc "Not to mention strong, otherwise you wouldn’t be trusted as a huntress."
            scene ch6sc02_691 with dissolve
            sj "*Scoffs lightly* [mc]... Outsider, you’re too much."
            $ sj_trust += 2
            scene ch6sc02_692 with dissolve
            sj "But... thank you, it was nice to hear."
            "Suji appreciates you noticing her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch6sc02_690 with dissolve
            mc "Anytime Suji, my gut feeling about you is that you're genuine."
            scene ch6sc02_691 with dissolve
            sj "I'd like to believe I am, unless you cross us."
            scene ch6sc02_690 with dissolve
            mc "Genuine and protective? Attractive qualities in a woman."
            scene ch6sc02_692 with dissolve
            sj "You better stop talking like that..."
            mct "*Chuckles* She's getting shy? I guess these huntresses aren't used to having a man around after all."

        "Don’t say anything.":
            scene ch6sc02_691 with dissolve
            sj "Thank you."

    scene ch6sc02_694
    with vpunch
    ec "{b}[mc]!{/b}"
    ec "Y-You’re here!? By the goddesses! Alive and unharmed?!"
    mc "Hey, Echo-"
    scene ch6sc02_695 with dissolve
    ec "You’re back! I can’t believe this... and you’re okay? You’re not hurt?"
    "She caresses both your cheeks as she looks you over for injuries."
    scene ch6sc02_696 with dissolve
    ec "*Voice cracks* W-When you went down that tunnel, I thought I’d never see you again!"
    ec "I feared the worst. I was so afraid I felt sick to my -"
    scene ch6sc02_697 with dissolve
    mc "Hey... Echo, I’m here. I’m right here..."
    mc "You don’t need to worry any longer."
    mc "I’m okay, it takes more than a little tumble through some ancient ruins to take me out."
    scene ch6sc02_695 with dissolve
    ec "You jest... that must mean you’re fine? It seems my worrying was for naught."
    mc "You needn’t worry about me, I told you... I’m an adventurer."
    mc "Handling the unexpected comes with the job."
    scene ch6sc02_698 with dissolve
    ec "My instincts tell me you’re more than just an ordinary adventurer..."
    ec "Something... much more."
    scene ch6sc02_699 with dissolve
    sj "I believe your instincts are correct, A’nu."
    sj "After his trial in the depths below the temple..."
    scene ch6sc02_700 with dissolve
    sj "I believe he might be the one our legends refer to. He has the spirit of A'khan within him."
    scene ch6sc02_701 with dissolve
    ec "Oh? That’s a bold claim to make, Huntress."
    ec "You were quite against having him here this morning, but now you proclaim him our man of legend?"
    scene ch6sc02_700 with dissolve
    sj "He emerged from the ancient tombs, the first in our lifetime. And look what he brought up from the depths!"
    scene ch6sc02_702 with dissolve
    ec "Fascinating..."
    ec "It looks like the Talisman of Malpheon, the one depicted in our tablets. It was wielded by the A’khans of old."
    scene ch6sc02_701 with dissolve
    ec "How in the name of the Goddesses did you manage to find this? It has been thought lost to time."
    scene ch6sc02_703 with dissolve
    mc "It’s a long story."
    "The two women stare you patiently."
    mc "*Sighs*... So, here’s what happened -"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    "You go over your tomb raider tale once more... from start to finish."
    scene ch6sc02_703 with Dissolve(1.5)
    $ renpy.pause(1)
    ec "..."
    scene ch6sc02_701 with dissolve
    ec "You... you truly are extraordinary. One of a kind."
    scene ch6sc02_703 with dissolve
    mc "If only you knew."
    scene ch6sc02_704 with dissolve
    ec "I will have to speak to the village Elders. They know our history and ancient tales better than anymore."
    ec "Their guidance and knowledge will be important going forward."
    scene ch6sc02_699 with dissolve
    sj "A’nu, if I remember correctly, some of the tales of old speak of this necklace and other ancient relics."
    sj "They say the man who will arise as the greatest A’khan and elevate our people will undergo a series of trials."
    scene ch6sc02_700 with dissolve
    sj "If such tales are true, then the outsider... [mc]... has completed the first trial of the A'khans."
    scene ch6sc02_701 with dissolve
    ec "That is what I believe too, Suji. But I’ll have to confirm this knowledge."
    ec "You've completed the trial unharmed, not even a scratch on you."
    scene ch6sc02_702 with dissolve
    ec "And this... you acquired an artifact of Malpheon. The first in several generations to do so."
    ec "*Quietly* Intriguing... you may very well be..."
    scene ch6sc02_703 with dissolve
    mc "What? What is it, Echo?"
    ec "Hmm..."
    scene ch6sc02_704 with dissolve
    ec "I wonder... if the other temples of the goddesses hold similar challenges?"
    ec "If so, then you could -"
    scene ch6sc02_705 with dissolve
    ec "Oh? You’ve found your friend too? I had asked my huntresses to help you search for her."
    scene ch6sc02_706 with dissolve
    mc "Yeah, Suji mentioned you asked them to help. Thank you for the gesture."
    ec "Will you introduce me? I’d love to meet her."
    scene ch6sc02_707 with dissolve
    mc "Pearl, there’s someone I’d like you to meet. Echo, the A’nu of the tribe."
    ec "Hello, friend of [mc]."
    scene ch6sc02_708 with dissolve
    pl "Hi! I’m Pearl, thank you for letting us inside your city."
    pl "This place is incredible, and your hospitality is more than we could hope for."
    scene ch6sc02_709 with dissolve
    ec "Thank you. That’s very kind of you to say. [mc] said something similar when he first saw our home."
    ec "As for our hospitality, think nothing of it."
    ec "I will not have either of you trekking around in the jungle. It is not safe."
    scene ch6sc02_708 with dissolve
    pl "Y-Yeah... I've come to realize that."
    scene ch6sc02_710 with dissolve
    ec "You look like you’ve been through hell and back..."
    ec "The two of you must rest, relax, and clean up."
    scene ch6sc02_708 with dissolve
    pl "Being chased through the jungle by unknown attackers has left me a little tired..."
    pl "Thank you for allowing this."
    scene ch6sc02_710 with dissolve
    ec "I will have a maiden prepare you a bath. The baths are located on the ground floor of the temple."
    ec "The waters come from an underground spring. They're both warm and soothing."
    scene ch6sc02_711 with dissolve
    pl "A natural hotspring?"
    pl "Right here, below your temple?"
    scene ch6sc02_712 with dissolve
    ec "*Giggles softly* It surprises you?"
    ec "We don't bathe in murky rivers just because we live in the jungle."
    ec "The ones who built the temple must’ve enjoyed bathing too."
    ec "They made an incredible bath chamber and it’s built directly on top of the hot spring."
    scene ch6sc02_711 with dissolve
    pl "It sounds incredible... I’m almost scared I’m dreaming right now."
    scene ch6sc02_713 with dissolve
    ec "Come, you two. Let us not remain idle."
    ec "I'll lead you to the baths, there you will be able to relax and freshen up."
    scene ch6sc02_714 with dissolve
    pl "You’re too generous... thank you!"
    ec "I'm just pleased you're both alright. Please, follow me."
    scene ch6sc02_715 with dissolve
    pl "I can’t believe it... you really did befriend the locals! Their leader is so kind to us."
    scene ch6sc02_716 with dissolve
    mc "*Chuckles* I told you, didn’t I?"
    scene ch6sc02_715 with dissolve
    pl "Mhm-Hm... still, I had to see it with my own eyes."
    scene ch6sc02_717 with dissolve
    pl "You aren’t known to be the most social of butterflies! *Giggles*"
    mc "I befriended a whole tribe while you made enemies with another. You may have to retract that statement."
    scene ch6sc02_715 with dissolve
    pl "*Snickers* Fair. C’mon, we have a bath waiting for us!"
    scene ch6sc02_716 with dissolve
    mc "After you, little mermaid."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_718 with Dissolve(1.5)
    $ renpy.pause(1)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    mh "Tsk! ..."
    mh "By all the goddesses! How did he survive falling into the ancient depths?"
    mh "Bastard... nobody has ever survived a journey there."
    scene ch6sc02_719 with dissolve
    mh "Goddesses, I’ve failed you. I must do more to protect us..."
    mh "I will not let this... outsider... corrupt us. His presence here is a mockery of us all."
    scene ch6sc02_720 with dissolve
    mh "I will have to take things into my own hands... Mhm."
    mh "So much to do. I can’t allow this to go on!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss1 with Dissolve(1)
    $ renpy.pause()
    scene ch5sc13_234 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    el "Great work today, Borri. I wouldn’t have managed to build that shelter for the building materials without you."
    scene ch5sc13_238 with dissolve
    br "Bah! Ye would’ve done just fine. Might’ve taken a few extra nails, but yer more than capable, lass."
    scene ch5sc13_237 with dissolve
    el "Be that as it may, I’m still grateful for the help."
    el "It feels good to have something to do... while [mc] is away."
    scene ch5sc13_238 with dissolve
    br "Aye, I don’t want ye locking yerself in a room fer a week again..."
    scene ch5sc13_239 with dissolve
    el "Hey! ... Rude."
    scene ch5sc13_242 with dissolve
    el "Do you think he’s okay? It sounded like his friends, Kira and Pearl, were in serious trouble."
    scene ch5sc13_240 with dissolve
    br "Bah! The lad will be fine. Ye know him... trouble follows him everywhere, but he always handles it."
    scene ch5sc13_237 with dissolve
    el "Yeah... you’re right. I’m going to continue working long shifts at the guild to earn more coin while he’s gone."
    scene ch5sc13_236 with dissolve
    el "We might have been given the basic materials by King Bennen, but we'll need so much more."
    scene ch5sc13_235 with dissolve
    br "Hah! Don’t tell me yer already thinking about furniture, lass? *Chuckles*"
    el "What? It’s a valid thing to think about!"
    scene ch5sc13_234 with dissolve
    el "A home will do us little good if it’s just going to be empty."
    el "[mc] agrees with me. It didn’t take much to convince him after he had tried the beds at Palace Valois."
    scene ch5sc13_235 with dissolve
    br "*Chuckles* Heh! I bet he had a sore back from the soft mattresses!"
    el "No way! That’s not a thing... is it?"
    scene ch5sc13_238 with dissolve
    br "Those puppy eyes of yours, lass, they'll have him agreeing to just about anything."
    scene ch5sc13_239 with dissolve
    el "Huuh? Are you suggesting I’m only getting my way because I’m pretty?"
    scene ch5sc13_240 with dissolve
    br "Nay, lass. Not because yer pretty... because he loves ye, through and through."
    scene ch5sc13_242 with dissolve
    el "And I him... *Sighs* Do you think... he’ll be back soon?"
    scene ch5sc13_238 with dissolve
    br "He'll be back before ye know it, lass. I think ye had the right idea about keeping busy."
    br "The less time yer mind has t' think about it, t' sooner he’ll pop up."
    scene ch5sc13_237 with dissolve
    el "Yeah... I’m getting another ale."
    scene ch5sc13_243 with dissolve
    el "Do you want one too?"
    br "Aye! Thank ye, lass."
    scene ch5sc13_244 with dissolve
    br "Make it two! Me ol' bones are in need of a good night's rest!"
    el "*Shouting* You’re not that old!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ss12 with Dissolve(1)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc02_722 with Dissolve(2.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    pl "Woah... Echo! I’ve never seen anything like this!"
    scene ch6sc02_721 with dissolve
    pl "Calling this a bath is an understatement!"
    ec "It pleases me to hear that you’re happy about this place."
    scene ch6sc02_723 with dissolve
    pl "I am... this is like a dream. Thank you so much."
    ec "You are welcome, I’m just glad the two of you are alright."
    scene ch6sc02_724 with dissolve
    mc "The water looks so refreshing..."
    mc "Why does it have that slightly teal tint even though we're indoors?"
    scene ch6sc02_725 with dissolve
    ec "Remember how I told you our ancestors worshipped Malpheon?"
    ec "According to legend, they used one of the blessings they received from him to enchant the hot spring below here."
    ec "The water will stay eternally fresh, warm and cleansed."
    mc "Enchanted water... huh, your tribe really has a nice setup here."
    scene ch6sc02_726 with dissolve
    ec "We’re blessed to have had ancestors with such ties to Malpheon."
    ec "And we still strive to regain a close connection to our goddesses of today."
    scene ch6sc02_727 with dissolve
    pl "Magical water... *Giggles*"
    pl "If I wasn’t a mermaid already... this would surely turn me into one!"
    scene ch6sc02_728 with dissolve
    ec "A mermaid?"
    scene ch6sc02_729 with dissolve
    pl "Just a little joke. [mc] likes to think I’m a mermaid 'cause I love water so much."
    scene ch6sc02_728 with dissolve
    ec "*Scoffs lightly* Is that so? Then you’ll definitely love this."
    ec "The water here completely loosens your muscles and releases all the tension in your body."
    ec "You’ll relax like never before."
    scene ch6sc02_730 with dissolve
    pl "Seas! Really?"
    pl "That sounds exactly what my body needs right now..."
    scene ch6sc02_731 with dissolve
    mc "I wonder how your ancestors managed all this? Sure, I get that they were blessed by Malpheon..."
    mc "But they'd still need a lot of manpower to build these places."
    scene ch6sc02_732 with dissolve
    ec "It is unknown to us now. Our ancestor's methods have been lost over the centuries."
    ec "We can only preserve their accomplishments to the best of our abilities, and enjoy the fruits of their labor to this day."
    scene ch6sc02_733 with dissolve
    pl "[mc], enough with the questioning... we’re here to unwind."
    pl "I’m sure you’ll have plenty of time to talk about history, but for now... let’s relax and enjoy this amazing bath!"
    mc "*Chuckles* Alright, alright... I’ll spare you from my fascination with ancient civilizations."
    scene ch6sc02_734 with dissolve
    pl "Good, because right now..."
    pl "All that is keeping me from passing out is the thought of my body sinking into this water..."
    pl "Having all this dirt and mud washed away, and letting the soothing water rejuvenate my spirit and body."
    scene ch6sc02_735 with dissolve
    pl "I can hear the water speaking to me."
    pl "It’s telling us to get naked and enjoy it."
    mc "*Chuckle* I get it, I get it... then let’s get to it."
    scene ch6sc02_736 with dissolve
    ec "I’ll let the two of you have some privacy, then. I need to seek guidance from our elders anyway."
    ec "Enjoy the bath, and relax as long as you need."
    scene ch6sc02_737 with dissolve
    ec "[mc], if you need me... you know where my personal chambers are."
    ec "Anything at all, come find me... your presence is one which I enjoy."
    scene ch6sc02_738 with dissolve
    mc "Sure, I might pay you a visit later."
    ec "Oh? ..."
    scene ch6sc02_739 with dissolve
    ec "That would be ... lovely."
    ec "I’ll see you later then, [mc]."
    scene ch6sc02_740 with dissolve
    ec "Come, Suji. Let’s give our guests some privacy."
    sj "As you wish, A’nu."
    scene ch6sc02_741 with dissolve
    ec "Enjoy the bath you two."
    ec "Suji will stand guard at the outer entrance and ensure that nobody disturbs you."
    mc "Bye, Echo. Thank you."
    pl "Bye! Thank you again!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_742 with Dissolve(1.5)
    $ renpy.pause(1)
    pl "Bath time! *Giggles* Let’s get naked!"
    mc "Let’s indeed."
    scene ch6sc02_743 with dissolve
    pl "Could you?"
    mc "Mhm-Hm, of course."
    scene ch6sc02_744 with dissolve
    pl "[mc]... thank you."
    pl "You’re so good to me..."
    scene ch6sc02_745 with dissolve
    mc "You’re welcome."
    pl "Mmh... much better."
    scene ch6sc02_746 with dissolve
    mc "What do you think of this place?"
    pl "Of A’nai? I like it."
    pl "At first glance it seemed a little primitive, but I can tell there’s more to it than I thought."
    mc "Yeah, I’m glad they’re civilized at least."
    scene ch6sc02_747 with dissolve
    pl "To think, Kira and I have been sailing past Aruna for years but never set foot upon its shores."
    mc "That is often the case. Same goes for travelling on land."
    pl "I can't believe this island is home to such a paradise."
    scene ch6sc02_748 with dissolve
    mc "Minus the other tribe that wants us dead."
    pl "*Giggles* Minus that, yeah. But this place? It’s like a utopia hidden away from the world."
    pl "Let’s get wet..."
    scene ch6sc02_749 with Dissolve(1.6)
    $ renpy.pause(1)
    pl "Ohh... Praise the seas... this is amazing!"
    mc "*Exhales* Yeah... I can practically feel the water soothing my muscles already."
    scene ch6sc02_750 with dissolve
    pl "I knoooow... Mmm!"
    pl "This has to be the best water in the whole world!"
    mc "*Chuckles* That’s high praise coming from you."
    scene ch6sc02_751 with dissolve
    pl "You feel it too! All the stress and dirt is simply... washing away."
    scene ch6sc02_752 with dissolve
    mc "I do. Enjoy it. You’ve been through a lot today."
    pl "That’s putting it mildly..."
    pl "Waking up in the middle of an unknown jungle, without you... being hunted..."
    scene ch6sc02_753 with dissolve
    mc "I can imagine."
    mc "I felt pretty disoriented when I woke up. Then I was attacked when I went looking for you."
    mc "Only, I was knocked out with tranquilizer darts and brought back here to A’nai."
    scene ch6sc02_752 with dissolve
    pl "*Scoffs lightly* I wish that had been me!"
    pl "I could’ve been here bathing and waiting for you to show up!"
    scene ch6sc02_753 with dissolve
    pl "I still can’t believe eating those yummy berries knocked us out!"
    scene ch6sc02_752 with dissolve
    pl "Why make something yummy and then give it nasty side effects? Nature is cruel."
    scene ch6sc02_754 with dissolve
    mc "*Chuckles* I know, right?"
    mc "They told me the berries are used for medicine, tranquilizers, and to make a sweet but potent alcohol."
    scene ch6sc02_755 with dissolve
    pl "Oooh... think they’ll offer us any?"
    scene ch6sc02_754 with dissolve
    mc "Perhaps... if we behave."
    scene ch6sc02_755 with dissolve
    pl "*Giggles* I’ll be on my best behavior for some yummy wine!"
    scene ch6sc02_754 with dissolve
    mc "Best behavior, huh?"
    scene ch6sc02_755 with dissolve
    pl "Mmm-Hmm!"

    if pearl_relationship == True:
        scene ch6sc02_757 with dissolve
        mc "*Chuckles* What are you up to?"
        scene ch6sc02_758 with dissolve
        pl "I’m feeling a little dirty... think you could help clean me up?"
        pl "I’m already wet... it shouldn’t be hard to get it off."
        scene ch6sc02_757 with dissolve
        mc "Already wet... you don’t say."
        pl "*Snickers softly* ..."
        scene ch6sc02_759 with dissolve
        pl "Do my legs first. They’ve been running around the jungle all day."
        scene ch6sc02_760 with dissolve
        pl "*Moans* Mmm... that... that’s just what they need."
        scene ch6sc02_761 with dissolve
        mc "I can imagine... these poor little tender legs. They’ll need proper treatment."
        scene ch6sc02_760 with dissolve
        pl "MMm... yes... you’re being so good t-to me."
        scene ch6sc02_761 with dissolve
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        pl "Allow me to... Mmm... return the favor."
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch6sc02_762 with dissolve
        $ renpy.pause(1)
        scene ch6sc02_763 with dissolve
        mc "Aahh..."
        pl "*Moans* Mmhm... someone's happy to bathe with me. *Giggles*"
        mc "Fuck... Mmh... What happened to being on our best behavior?"
        scene ch6sc02_761 with dissolve
        pl "We’re lovers... aren’t we?"
        scene ch6sc02_760 with dissolve
        mc "Mmm. Yes, we are."
        scene ch6sc02_764 with dissolve
        pl "As lovers, it’s good to make your partner happy, right?"
        scene ch6sc02_765 with dissolve
        pl "It’s our duty to fulfill each others needs and desires. So, that means we are, in fact, exhibiting good behavior."
        scene ch6sc02_764 with dissolve
        mc "*Moans* Mmmh... fuck... you’re making a strong point. It’s hard to argue against you."
        scene ch6sc02_765 with dissolve
        pl "*Snickers* I like making things hard..."
        scene ch6sc02_766 with dissolve
        pl "Oh? Looks like my legs are all cleaned up."
        pl "I think you should move on to my ass... I slid down a hill when I was escaping."
        scene ch6sc02_767 with dissolve
        pl "Be honest, does it look like it needs your attention?"
        mc "I have to be brutally honest, Pearl... it definitely needs some attention."
        scene ch6sc02_768 with dissolve
        pl "*Giggles* I thought as much. You'd better be thorough... I want it to be spotless!"
        scene ch6sc02_769 with dissolve
        pl "*Squeals* Aiiyh!"
        mc "Don’t worry, I’ll always be thorough when it comes to taking care of my little mermaid."
        scene ch6sc02_770 with dissolve
        pl "*Moans* MMm... I knew I could count on my sharky."
        scene pl_lewd23 with dissolve
        $ renpy.pause()
        pl "*Moans* Oh! Yes... my cheeks are so dirty. They need you, baby- AHh!"
        mc "Mmm... you’re so smooth and tight..."
        pl "*Moans* Only for you - Ahh! You’re the only man in the world that gets to do this- MMm!!"
        scene pl_lewd24 with dissolve
        $ renpy.pause()
        mc "Mmm! You belong to me, Pearl."
        with vpunch
        pl "{b}*Moans* Aiiyh!{/b} Yes! Only you! Mmm!! Use my cheeks baby! I love how- Ahh! How you spread my legs!"
        with vpunch
        pl "*Moans* I want you to cum! Mmm! Enjoy my ass and cum all over me! {b}AHhH!!{/b}"
        with vpunch
        mc "Fuuu... Pearl! Here it comes! {b}MMM!!{/b}"
        scene ch6sc02_771 with dissolve
        $ renpy.pause(0.5)
        with vpunch
        $ renpy.pause(0.5)
        mc "Ahhh!"
        scene ch6sc02_772 with dissolve
        pl "*Panting* Mmm! So much... You really love my peachy ass, huh?"
        mc "That I do... *Chuckles*"
        pl "I really needed this... Mmm. I'd better finish cleaning up. You’ll wait for me... right?"
        scene ch6sc02_773 with dissolve
        mc "Sure, I’ll go dry off first."
        pl "Thank you! I won’t take long... just need to get the last of the dirt off, and sadly your cum."
        mc "This won't be the last time you're covered in it."
        pl "*Giggles gently* Mmm."
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch6sc02_774 with Dissolve(1)
        pl "All done! You’re not looking, right?"
        mc "*Chuckles* Really? I’m not allowed to see you naked now?"
        pl "No, we may be lovers but... you should still be a gentleman! *Giggles*"
        mc "*Sighs* Women... fine, fine... I won’t look."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0

    else:
        scene ch6sc02_756 with dissolve
        pl "As much as I love being in here, I'd better finish washing off. The sun was already setting so it’s probably pretty late by now."
        mc "Yeah... let’s finish off. I’ll dry off first, then you can come up."
        scene black with Dissolve(1)
        $ renpy.pause(1)
        scene ch6sc02_774 with Dissolve(1)
        pl "All done! You’re not looking, right?"
        mc "Don’t worry..."
        pl "Good..."

    scene ch6sc02_775 with dissolve
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    pl "This was so good... I have a feeling I’ll find my way in here every day until we find the ambassador."
    mc "Yeah... me too. A bath like this shouldn’t be taken for granted."
    scene ch6sc02_776 with dissolve
    pl "No, it definitely shouldn’t. It’ll be hard going back to regular baths after this."
    pl "Do you think we could convince Diana to install a bath like this, now that she's taking over Looter's Bay?"
    scene ch6sc02_777 with dissolve
    mc "*Chuckles* I’m sure she’d be happy to comply to such a request."
    pl "Maybe she would... if you were the one asking her?"
    mc "Heh... yeah, no."
    pl "Meanie..."
    scene ch6sc02_778
    with vpunch
    pl "*Gasps* [mc]! ..."
    pl "You’re supposed to be a gentleman! ... no peeking!"
    scene ch6sc02_779 with dissolve
    mc "Sorry, my curiosity got the better of me."
    mc "It was just a short glance, I didn’t see much."
    scene ch6sc02_778 with dissolve
    pl "It’s okay... it’s just a little embarrassing."

    if pearl_relationship == True:
        scene ch6sc02_778
        pl "*Quietly* {size=-10}{b}I don’t want you to lose interest from seeing me naked too often...{/b}{/size}"
        scene ch6sc02_779 with dissolve
        mc "Hmh? Did you say something?"
        scene ch6sc02_778 with dissolve
        pl "No, just don’t look!"

    else:
        scene ch6sc02_778
        $ renpy.pause(0.4)
    scene ch6sc02_779 with dissolve
    mc "Eyes closed... you can get dressed."
    scene ch6sc02_780 with dissolve
    pl "Huh?? Wait a moment..."
    mc "What is it?"
    pl "My bikini..."
    scene ch6sc02_781 with dissolve
    pl "Do you have my bikini? I can’t see it anywhere..."
    scene ch6sc02_782 with dissolve
    mc "No, I haven’t seen it. Can I open my eyes?"
    scene ch6sc02_781 with dissolve
    pl "Hmmm... I don’t know."
    scene ch6sc02_782 with dissolve
    mc "Pearl, it’s a little hard to help you if I can’t see anything..."
    scene ch6sc02_781 with dissolve
    pl "*Sighs* Okay... you can open them, but only to help me look!"
    scene ch6sc02_783 with dissolve
    mc "Hmm, it seems you’re right. Your bikini isn’t here... and it should be easy to spot given the bright teal color."
    mc "It was quite dirty, maybe one of the maidens took it to clean it?"
    scene ch6sc02_784 with dissolve
    pl "Fantastic... but what am I supposed to wear?"
    pl "I may enjoy being naked around you... but around a whole tribe? No thanks."
    scene ch6sc02_785 with dissolve
    mc "*Chuckles* I’m sure you’d turn quite a few heads."
    with vpunch
    pl "!!"
    scene ch6sc02_784 with dissolve
    pl "Hey... c’mon, quit teasing me and help!"
    scene ch6sc02_786 with dissolve
    mc "Alright, alright ... look over there on the bench. They left some clothes for you."
    pl "You knew this whole time?!"
    mc "Maybe... *Chuckles*"
    scene ch6sc02_787 with dissolve
    pl "I’m gonna get you for this..."
    mc "Sure, now put on some clothes."
    scene ch6sc02_788 with dissolve
    pl "Is this all they left me?"
    mc "*Chuckles* What? Is tribal out of fashion in Looter’s Bay?"
    scene ch6sc02_789 with dissolve
    pl "Hah-Hah... Mr. Funny-man."
    pl "Why am I the only one who’s getting a new outfit? Why do you get to keep your -"
    scene ch6sc02_790 with dissolve
    mc "You were saying?"
    pl "New pants? They look shorter than before..."
    mc "They are... but I don’t mind, it’ll help with the warm climate here. Now stop complaining and put it on."
    scene ch6sc02_789 with dissolve
    pl "Hmmfh..."
    scene ch6sc02_788 with dissolve
    pl "*Sighs* Alright, I’ll try them on."
    scene ch6sc02_791 with dissolve
    pl "They seem to have gotten my size correct at least..."
    pl "The fabric is surprisingly high quality."
    pl "It’s just..."
    scene ch6sc02_792 with dissolve
    mc "What is it?"
    pl "It’s a little skimpy, don’t you think?"
    scene ch6sc02_793 with dissolve
    mc "First of all... we're staying with a tribe full of women. I’m the only man on the entire island."
    mc "Secondly, you’re used to revealing outfits, no?"
    pl "Right... still, it’s different when it’s your own outfit. And it’s not like I’m always walking around in a bikini!"
    scene ch6sc02_794 with dissolve
    pl "Look! My ass is practically falling out!"
    mc "*Chuckles* And that’s a bad thing?"
    pl "Stooop! You’re teasing me..."
    mc "Well, you’re still missing one piece of clothing. Put on the last bit and see if it helps."
    scene ch6sc02_795 with dissolve
    pl "Oh? You're right."
    pl "Let’s have a look!"
    scene ch6sc02_796 with dissolve
    pl "That feels better... what do you think?"
    mc "It looks great on you."
    scene ch6sc02_797 with dissolve
    pl "Yeah? You think I can pull off the tribal woman look?"
    mc "Most definitely... you’ll fit right in."
    scene ch6sc02_798 with dissolve
    pl "Charmer..."
    pl "You look quite dashing yourself... that ancient necklace and tropical pants suit you."
    pl "From city-boy to... {b}King of the Jungle.{/b}"
    scene ch6sc02_799 with dissolve
    mc "King of the Jungle, huh?"
    scene ch6sc02_798 with dissolve
    pl "Mhm-Hm... I wouldn’t be opposed to letting you boss me around."
    scene ch6sc02_800 with dissolve
    mc "*Chuckles* Interesting idea..."
    pl "I had a feeling you'd like that. *Snickers*"
    pl "*Yawns* Nnnghh..."
    scene ch6sc02_801 with dissolve
    mc "C’mon, let’s head back to our hut. You must be exhausted, I know I am."
    pl "We have our own hut?"
    mc "Mhm. They assigned one to me when they brought me here."
    scene ch6sc02_802 with dissolve
    pl "I don’t even care if there’s a bed at this point... just give me a blanket and I’ll pass out."
    mc "*Chuckles* Don’t worry. There’s beds, pillows, blankets..."
    mc "I was in chains when I woke up, but aside from that I’ve been very comfortable here."
    scene ch6sc02_803 with dissolve
    pl "Chains? Seas... are you planning on tying me up while I sleep and having your way with me?"
    mc "Who knows...?"
    $ renpy.pause(0.5)
    with vpunch
    pl "[mc]! ... *Giggles*"
    scene ch6sc02_804 with dissolve
    pl "I’m... I’m really glad that it’s you I’m here with."
    mc "Mmh. Me too, Pearl... me too."
    pl "I'm calling dibs on the best bed and the softest pillows!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_805 with Dissolve(1.5)
    $ renpy.pause(1)
    pl "Seas! You weren’t kidding... this place is so cozy!"
    pl "It reminds me of a cozy little sea-side shanty town Kira and I visit sometimes."
    scene ch6sc02_806 with dissolve
    mc "Looks like they already set up a bed for you as well."
    pl "This is so cute! It’s the best thing ever!"
    scene ch6sc02_807 with dissolve
    mc "*Chuckles* Not the enchanted baths?"
    scene ch6sc02_808 with dissolve
    pl "The bath was magical! And this is just icing on the top!"
    pl "Oh? I didn’t expect them to be so comfortable?"
    scene ch6sc02_809 with dissolve
    pl "Usually beds like this are quite stiff, but it’s... soft?"
    pl "It’s made of woven straw but it's not itchy or pokey!"
    scene ch6sc02_810 with dissolve
    mc "Perhaps they have a special way of processing the materials to make it softer."
    pl "They live really well out here compared to most established cities... it's amazing."
    mc "Yeah, I was quite surprised myself. Maybe finding meaning and comfort in the simple things isn’t a bad way to live."
    scene ch6sc02_811 with dissolve
    pl "Mmhm... I could get behind that kind of philosophy."
    pl "*Stretches* Hnngh... I’m getting sleepy."
    mc "Yeah... let’s get some well deserved rest."
    scene ch6sc02_812 with Dissolve(1.5)
    pl "Mmm... goodnight, [mc]."
    mc "Goodnight, Pearl. Sleep well."
    scene ch6sc02_813 with Dissolve(1.5)
    $ renpy.pause(1)
    "The two of you quickly doze off after a long day..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)

    if pearl_relationship == True:
        "After about an hour you hear the sound of soft footsteps near your bed, followed by a soft voice."
        scene ch6sc02_814 with Dissolve(1.5)
        $ renpy.pause(1)
        pl "[mc]?"
        scene black with Dissolve(1.5)
        $ renpy.pause(1)
        mc "Hmm? Pearl?"
        scene ch6sc02_815 with Dissolve(1.5)
        $ renpy.pause(1)
        pl "[mc]..."
        mc "Hey... what’s wrong?"
        pl "I can’t sleep."
        mc "Huh? How come?"
        scene ch6sc02_816 with dissolve
        pl "I don’t feel comfortable... the bed is nice but... you’re not in it."
        mc "Oh? That is unacceptable."
        pl "*Nods*"
        scene ch6sc02_815 with dissolve
        pl "Can I... you know? Sleep next to you?"
        mc "I’d love to say yes, but there’s really not much room on these straw beds."
        scene ch6sc02_818 with dissolve
        pl "Hmh... what if I lay on top of you?"
        pl "I really think it would calm m ..."
        mc "Sure, come on then."
        scene ch6sc02_817 with dissolve
        pl "Thank you, [mc]..."
        pl "You’re always so good to me."
        scene ch6sc02_819 with dissolve
        pl "Mhh... cozy."
        pl "*Giggles softly* You were right... these beds are a tight fit."
        scene ch6sc02_820 with dissolve
        mc "Told you so."
        scene ch6sc02_821 with dissolve
        pl "Sorry..."
        scene ch6sc02_820 with dissolve
        mc "It’s alright, I prefer you being comfortable and feeling safe."
        mc "I can handle a night of awkward sleep, but after what you went through today..."
        scene ch6sc02_821 with dissolve
        mc "You deserve a proper rest. Anything you want."
        scene ch6sc02_821 with dissolve
        pl "You’re so sweet, [mc]. I feel safe with you."
        scene ch6sc02_822 with dissolve
        pl "I’m lucky to be sharing a bed with someone who takes care of me."
        scene ch6sc02_823 with dissolve
        mc "You know, I feel pretty lucky too."
        scene ch6sc02_822 with dissolve
        pl "How so?"
        scene ch6sc02_823 with dissolve
        mc "I was able to rescue you and Kira from Diana and survived the fight."
        mc "Now I'm getting to go on an adventure with my favorite little mermaid and we've discovered an ancient culture."
        mc "What I’m trying to say is, I’m glad I found you today. I'm glad you're in my life."
        scene ch6sc02_822 with dissolve
        pl "Mhm, I am too... [mc]."
        pl "Really glad..."
        scene ch6sc02_821 with dissolve
        mc "You don’t need to worry, I won’t let anyone harm you."
        scene ch6sc02_820 with dissolve
        pl "*Nods* Mm."
        scene ch6sc02_821 with dissolve
        pl "I wanted to ask you something."
        scene ch6sc02_820 with dissolve
        mc "Ask away."
        scene ch6sc02_824 with dissolve
        pl "I know you say I don’t have to worry, that we’re safe here..."
        pl "But the reason you found me, the reason you were in those ruins at all... was because someone here tried to kill you."
        scene ch6sc02_825 with dissolve
        mc "*Exhales* Mmm. Marah is her name."
        scene ch6sc02_824 with dissolve
        pl "Marah?"
        scene ch6sc02_825 with dissolve
        mc "Mhm. She’s the high-priestess and their second-in-command."
        mc "She's only below Echo, their A’nu."
        scene ch6sc02_824 with dissolve
        pl "I see..."
        pl "She was trying to kill you, though?"
        scene ch6sc02_825 with dissolve
        mc "She was... she is very skeptical of outsiders, and especially men."
        scene ch6sc02_822 with dissolve
        pl "I could kill her for you? *Giggles*"
        scene ch6sc02_823 with dissolve
        mc "*Chuckles* No killing the locals."
        mc "Not unless our hands are forced, okay?"
        scene ch6sc02_822 with dissolve
        pl "Boooh, okay!"
        pl "But she'd better not try to harm you again, otherwise it's stabby-stabby time! *Giggles softly*"
        scene ch6sc02_824 with dissolve
        pl "We need to be careful. I know they've welcomed us with open arms and I love that-"
        pl "-But trusting them blindly, especially since there’s another hostile tribe here too, it could be dangerous."
        scene ch6sc02_825 with dissolve
        mc "I agree, we won’t trust them naively, but we’re also not here to judge them or be paranoid."
        mc "Echo has been very forthcoming. She didn’t have to stick her neck out for us or welcome us into their home."
        mc "She's risking the ire of her own people for our sake."
        scene ch6sc02_824 with dissolve
        pl "*Nods* Mhm... Echo, she does seem genuine... and I spoke a bit with Vex? She also seems sweet."
        pl "Do you think that... Marah? Will try to hurt you again?"
        scene ch6sc02_825 with dissolve
        mc "She might, unless I can find a way to prove to her that I’m not a threat."
        mc "But I’ll keep my guard up around her."
        scene ch6sc02_824 with dissolve
        pl "Good..."
        scene ch6sc02_826 with dissolve
        pl "You know... if they did anything to hurt you..."
        pl "I would kill them all."
        scene ch6sc02_825 with dissolve
        mc "I know... and you know that goes the other way too. If they even attempt to harm you..."
        mc "I’ll descend upon their little civilization and nothing but rubble and ashes will be left behind."
        scene ch6sc02_822 with dissolve
        pl "*Giggles* Really? You’d destroy an ancient civilization just to protect me?"
        scene ch6sc02_823 with dissolve
        mc "I wouldn’t even flinch."
        scene ch6sc02_822 with dissolve
        pl "You're so romantic with me... it's making me feel funny."
        scene ch6sc02_823 with dissolve
        mc "I can't help but feel protective of you."
        scene ch6sc02_822 with dissolve
        pl "Same! Nobody hurts my sharky and gets away with it."
        scene ch6sc02_823 with dissolve
        mc "Don’t worry. I’m not going anywhere."
        scene ch6sc02_821 with dissolve
        pl "Mmmm... *Rubs*"
        scene ch6sc02_820 with dissolve
        mc "Didn’t you get enough in the baths?"
        scene ch6sc02_821 with dissolve
        pl "*Moans* I don’t know what you’re talking about... Mmm..."
        scene ch6sc02_820 with dissolve
        mc "Oh, really? Then who’s rubbing against me?"
        scene ch6sc02_821 with dissolve
        pl "You’re imagining things... such a silly sharky. *Giggles* Mmm..."
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc02_827 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mc "Yeah... I must be... Mmm..."
        pl "*Kiss* I want you."
        scene ch6sc02_828 with dissolve
        mc "I want you too, Pearl... Mmm."
        scene ch6sc02_827 with dissolve
        pl "Mmhm... I was hoping you'd say that... [mc]..."
        scene ch6sc02_828 with dissolve
        pl "I can’t stop thinking about it... *Lick* And... Mmm... wanting to kiss you... taste you... Mmm."
        scene ch6sc02_829 with dissolve
        mc "I feel the same..."
        pl "*Kiss* Mmm... I love feeling your hands on my body... Ahhngh..."
        scene ch6sc02_830 with dissolve
        mc "Your ass is perfect... so plump and juicy."
        pl "Mmfhhm... how does it feel knowing- Ahhh..."
        pl "That you’re the only one who ever has and ever will get to touch it?"
        scene ch6sc02_831 with dissolve
        mc "Like I’m the luckiest man alive."
        pl "*Moans softly* Nnnghh... I love making you feel this way... I feel the same."
        scene ch6sc02_828 with dissolve
        pl "No woman has ever been as lucky as I am... right now, right here... in this moment with you."
        scene ch6sc02_827 with dissolve
        pl "*Mwah* ..."
        scene ch6sc02_828 with dissolve
        pl "Are we really... Mmm... going to do this? Here?"
        scene ch6sc02_827 with dissolve
        mc "Why wouldn’t we? Nobody’s around..."
        scene ch6sc02_828 with dissolve
        pl "I know but... Mmm... isn’t it wrong to be so... naughty while being guests?"
        scene ch6sc02_830 with dissolve
        mc "I don’t care... let’s be naughty."
        scene ch6sc02_831 with dissolve
        pl "*Moans* Aiiyh... [mc]... O-Okay... *Kiss* Mmm..."
        scene ch6sc02_832 with dissolve
        pl "My body is... *Mwah*"
        pl "So hot... *Mwah*"
        scene ch6sc02_833 with dissolve
        mc "How come?"
        pl "You know why... [mc]... I really enjoy sharing a bed with you, mmm."
        scene ch6sc02_834 with dissolve
        mc "Mmhmm... me too."
        scene ch6sc02_835 with dissolve
        pl "Mmm ..."
        scene ch6sc02_834 with dissolve
        pl "I love how you squeeze my ass like that as we kiss ... MMm."
        scene ch6sc02_835 with dissolve
        mc "I can’t resist you..."
        scene ch6sc02_834 with dissolve
        pl "Good... me either..."
        scene ch6sc02_836 with dissolve
        pl "You’re excited... Nngh- really... excited... Mmm."
        pl "*Bites lip* Seas... I can’t believe I make you this hard. Mhm, it turns me on so... unbelievably much."
        mc "There’s no point denying it, is there?"
        scene ch6sc02_837 with dissolve
        pl "*Giggles softly* With something this big? No... trying to deny it would be futile."
        pl "This is something women would fight over... maybe even kill for."
        mc "Would you?"
        scene ch6sc02_838 with dissolve
        pl "You have such a dirty mind..."
        scene ch6sc02_839 with dissolve
        mc "You didn’t answer... would you?"
        scene ch6sc02_838 with dissolve
        pl "M-Maybe..."
        pl "*Giggles* Since it’s yours... maybe I would."
        scene ch6sc02_840
        with vpunch
        mc "Come here!"
        pl "*Moans* Ohh!"
        scene ch6sc02_841 with dissolve
        mc "You like that, huh?"
        pl "*Snickers* No... I absolutely can’t stand it when you have your hands on my body."
        mc "Is that so?"
        scene ch6sc02_842 with dissolve
        pl "MMmfh..."
        mc "Then why are you moaning at the slightest touch?"
        scene ch6sc02_843 with dissolve
        mc "You’re eager to be touched by me."
        scene ch6sc02_842 with dissolve
        pl "Y-Yeah..."
        scene ch6sc02_843 with dissolve
        pl "Mmm... I really am."
        scene ch6sc02_844 with dissolve
        pl "Does it feel good? When I move on you like this?"
        scene ch6sc02_845 with dissolve
        mc "Mmm... so good."
        scene ch6sc02_844 with dissolve
        pl "Mmmffh..."
        scene ch6sc02_845 with dissolve
        mc "You’re incredibly hot, Pearl."
        scene ch6sc02_844 with dissolve
        pl "If we keep going- Mmm... we’ll be dripping in sweat."
        scene ch6sc02_845 with dissolve
        mc "Good thing we know where the baths are."
        scene ch6sc02_844 with dissolve
        pl "*Gentle moan* Your mind is so dirty..."
        scene ch6sc02_845 with dissolve
        pl "First you want to have your way with me here, and then wash off all our sexual sweat in their baths..."
        scene ch6sc02_844 with dissolve
        mc "Tell me you weren’t thinking the same... Mmm."
        scene ch6sc02_845 with dissolve
        pl "M-Maaybe... Mmm... seas, I love grinding on you..."
        scene ch6sc02_846 with dissolve
        pl "Here... they need you."
        mc "Mmmffhh... such an enticing scent..."
        scene ch6sc02_847 with dissolve
        pl "*Gentle moan* Mmmh... [mc], they... they belong in your mouth."
        pl "Please... Mmm, s-suck on them?"
        scene ch6sc02_848 with dissolve
        pl "*Moans* Oohhh... yes... s-sharky... Mmm. They’re yours... only yours."
        pl "*Moans gently* Mmm... your lips-Nnghh... feels so good."
        scene ch6sc02_849 with dissolve
        mc "*Suck* Mmm... so tasty... I love the salty taste of your skin mixed with the sweet aroma of your breasts... Mmm."
        pl "*Gentle moan* Oohhh... yes! Yes... suck my nipple... MMm! I've been wanting to feel your mouth on me all day..."
        scene ch6sc02_850 with dissolve
        mc "*Sucks* Mmm... me too, every time I see you waltz around in your skimpy outfits, I can’t help but want you."
        scene ch6sc02_849 with dissolve
        pl "*Moans* MMm! Then I'd better keep wearing them- Aahh... you’re so hard right now."
        scene ch6sc02_850 with dissolve
        mc "*Suck* Mmm... as are your nipples, perfectly aroused and delicious."
        scene ch6sc02_849 with dissolve
        pl "*Giggles* You’re such a hungry sharky... MMm... I’ll have to feed you more often."
        scene ch6sc02_850 with dissolve
        mc "Mmm... take off your top."
        scene ch6sc02_851 with dissolve
        pl "What my handsome sharky wants... he will get. *Giggles*"
        scene ch6sc02_852 with dissolve
        mc "You’re so incredibly mesmerizing..."
        pl "..."
        scene ch6sc02_853 with dissolve
        pl "Thank you... it makes me, really happy when you’re being so sweet to me..."
        pl "So, I’ll be sweet to you as well."
        scene ch6sc02_854 with dissolve
        "While she begins to fidget with your pants, you can feel the warmth and wetness between her legs as she rests on your thigh."
        pl "I can’t hold back anymore..."
        pl "He needs to breathe."
        scene ch6sc02_855 with dissolve
        pl "There, that’s much better."
        mct "{i}Damn... the way she’s looking at it, I’m about to feel really good.{/i}"
        scene ch6sc02_856 with dissolve
        pl "Mmm... you’re twitching like crazy..."
        pl "Was it sucking my breasts or my grinding that caused it?"
        scene ch6sc02_857 with dissolve
        mc "Mmm! Both... definitely both."
        scene ch6sc02_856 with dissolve
        pl "*Giggles* You’re speaking the truth... throbbing like this is so... honest."
        scene ch6sc02_857 with dissolve
        pl "You really want me..."
        scene ch6sc02_856 with dissolve
        mc "Mmh... yeah, I do."
        scene ch6sc02_857 with dissolve
        mc "You’re driving me crazy, MMm..."
        scene ch6sc02_858 with dissolve
        pl "Oh am I? *Snickers*"
        pl "I’m just getting started..."
        pl "I wonder how much pleasure you can handle before you explode, Mmh..."
        scene ch6sc02_859 with dissolve
        mc "MMmm... fuck..."
        scene ch6sc02_860 with dissolve
        pl "That’s it... I know how you like being in my little hands. MMm..."
        scene ch6sc02_861 with dissolve
        pl "Just let yourself feel... let yourself relax... I’ll take care of you."
        scene ch6sc02_859 with dissolve
        mc "Fuuu... Pearl, Mmm..."
        scene ch6sc02_860 with dissolve
        pl "What? Was I squeezing too firmly?"
        scene ch6sc02_861 with dissolve
        mc "N-No... this feels amazing."
        scene ch6sc02_859 with dissolve
        mc "You’re amazing, a natural..."
        scene ch6sc02_860 with dissolve
        pl "Oh, really?"
        scene ch6sc02_861 with dissolve
        mc "*Moans* Yes, mmm... your grip is perfectly firm, yet your palm is soft and sweaty, Mmm ..."
        scene pl_lewd25 with dissolve
        $ renpy.pause()
        pl "I’m going to make you feel amazing."
        mc "Mmm... you already are... how did I find such a naughty mermaid?"
        pl "*Gentle moan* Nnghh... I can’t help it..."
        pl "If being naughty satisfies my sharky, then I’ll be the naughtiest little mermaid he can imagine. *Grip tightens*"
        with vpunch
        mc "Fuu... Pearl! MMm!"
        with vpunch
        pl "*Moans* Yes... yes, baby! Mmm! You’re throbbing so good in my hand! Mmm! Give it to me!"
        scene ch6sc02_862
        with vpunch
        mc "Aaahh! Mmm!"
        pl "*Gasps* MMMgh!"
        scene ch6sc02_863 with dissolve
        pl "*Giggles softly* Mmm... I love how easily I can make you cum!"
        mc "Fuck... that was incredible."
        scene ch6sc02_864 with dissolve
        pl "Mmmhh... so good... delicious and warm. *Lick*"
        mct "{i}She’s so unbelievably hot... Mhh.{/i}"
        scene ch6sc02_865 with dissolve
        pl "MMm! *Lick* I’m starting to get used to your flavor... I could get used to having it every day."
        scene ch6sc02_864 with dissolve
        mc "*Chuckles* Every day?"
        scene ch6sc02_865 with dissolve
        pl "Every... Day. Mmmm..."
        scene ch6sc02_857 with dissolve
        pl "Oh? You’re still throbbing and so... hard..."
        scene ch6sc02_856 with dissolve
        mc "Because of you... Mnnghh."
        scene ch6sc02_857 with dissolve
        pl "Me? I’m the cause of this severe condition?"
        scene ch6sc02_856 with dissolve
        mc "Mmmh... Y-Yeah."
        scene ch6sc02_858 with dissolve
        pl "Hmmm... it seems I’ll have to work harder to satisfy you."
        pl "You know what...?"
        scene ch6sc02_866 with dissolve
        mc "What are you-"
        pl "I know exactly what you need... *Snickers softly*"
        scene ch6sc02_867 with dissolve
        mc "Come here, you little vixen..."
        pl "Patience, [mc]..."
        mc "Remove your panties."
        scene ch6sc02_868 with dissolve
        pl "I love when you tell me what to do, mmm."
        mc "Slowly."
        scene ch6sc02_869 with dissolve
        pl "Don’t worry, sharky... I know you enjoy a good show."
        pl "Mmm..."
        mc "Unbelievable..."
        scene ch6sc02_870 with dissolve
        pl "*Giggles softly* What? ... seeing something you like?"
        pl "Am I able to stand out? Even amongst a tribe of beautiful women?"
        scene ch6sc02_871
        with vpunch
        pl "*Gasps* Aah!*"
        mc "Feel how hard you make me?"
        scene ch6sc02_872 with dissolve
        pl "*Moans softly* Nnghh- Yesss... so... incredibly hard."
        scene ch6sc02_871 with dissolve
        mc "You’re the woman in this tent with me, the woman who makes me feel this way..."
        scene ch6sc02_872 with dissolve
        pl "Oohh... I must really be special... Mmm... otherwise you wouldn’t be so hard right now..."
        scene ch6sc02_871 with dissolve
        mc "That you are... Mmm."
        scene ch6sc02_872 with dissolve
        mc "You’re one of a kind, Pearl... the jewel of the seas."
        scene ch6sc02_871 with dissolve
        pl "I want you to show me how much you desire me, [mc]... Mmmhhh..."
        scene ch6sc02_873 with dissolve
        pl "Let me feel you, I want to feel all of you... please, take me."
        scene ch6sc02_874
        with vpunch
        pl "*Moans* Aiiyhh... y-you can’t just spread my legs like that! MMm..."
        mc "And why is that? Sounds like you’re loving it."
        scene ch6sc02_875 with dissolve
        pl "*Moans* It’s so naughty... you’re really going to take me? Right here on the floor? NNnghh..."
        scene pl_lewd26 with dissolve
        $ renpy.pause()
        mc "Mm-Hmm... that’s exactly what I’ll do."
        pl "Seas... you’re driving me wild... [mc]- Ahh..."
        pl "*Moans* Fuu... I need you! I need you inside! Please... MMm!"
        pl "I want you so badly... Mmffhh!"
        "You press your tip further down, sliding it between her dripping lips."
        scene ch6sc02_876 with dissolve
        pl "*Moans* Ahh-Ahh! G-Gently... all this build up has- MMm... made me hyper sensitive..."
        scene pl_lewd27 with dissolve
        $ renpy.pause()
        mct "{i}MMmh... her opening is so warm... she really is at peak arousal.{/i}"
        mct "{i}The way her wet lips suction onto my tip- Mmmh... amazing.{/i}"
        pl "*Moans* Ohh... [mc], I-I feel you... MMm."
        pl "Your tip is - Ahh... so amazing... Mmmh... I love feeling you..."
        mc "I’m going to go deeper now, Mmm..."
        pl "S-Slowly! Please..."
        mc "Don’t worry... I’m taking my time with you."
        scene pl_lewd28 with dissolve
        $ renpy.pause()
        pl "*Moans* Ahh... MMm! So... so good..."
        mc "Fuuu... you’re just as tight as I remember... Mmm."
        pl "Aaahh... [mc]... you’re so deep."
        pl "Seas... I love your big cock! Mmm! I’m becoming addicted... Ahhh!"
        scene pl_lewd29 with dissolve
        $ renpy.pause()
        mc "Fuck... Pearl... MMm, you’re so damn tight! Ahhh..."
        pl "O-Only for you! Ahh!! F-Fuck me! [mc]! Fuck me right here on the floor of their guest hut!"
        with vpunch
        pl "I don’t care if anyone hears us! MMm!! All I care about is feeling you deep inside me! AHhh!"
        scene pl_lewd30 with dissolve
        $ renpy.pause()
        pl "*Moans* Aiiyh-Aiii! Yes!! MMfffh! Grab my legs like that! AHhh!!"
        with vpunch
        pl "[mc] - Ahhh!! You’re so deep! {b}D-DON’T STOP! AHH!!!{/b}"
        with vpunch
        mc "MMm!! There’s no stopping! Ahh! I’m going to fuck you until you can’t stand-AHhh!"
        with vpunch
        pl "*Moans loudly* {b}AYYYHH!! [mc]!! AHH!! I’M-I’M CUMMING!! AHH!! SEAS!!{/b}"
        with vpunch
        $ renpy.pause(0.7)
        with vpunch
        mc "That’s it! Mmm!! Let it all out! You deserve to feel good. MMm!"
        scene pl_lewd31 with dissolve
        $ renpy.pause()
        pl "*Squeals* Aiiiyh! [mc]! You’re not even- AHhH! giving me a break? AHh!"
        mc "Mmm! No. No breaks for you tonight... Hnngh!"
        pl "*Moans* AHh-Hnngh!! Yes! I love how- AHhh! You’re fucking me like a wild animal! AHhh!"
        with vpunch
        pl "I belong to you! Mmm! K-Keep fucking me! AHh!"
        scene pl_lewd32 with dissolve
        $ renpy.pause()
        mc "Fuu... fuck! You’re so damn tight and warm... Mmm!"
        with vpunch
        pl "Aiiiyh!! [mc]!! Ahh! I can’t! {b}I CAN’T! I CAN’T HOLD BACK!! AHHH!!{/b}"
        with vpunch
        pl "{b}I’M! I’M GOING TO!! AHh-MM!!{/b}"
        "Pearls last orgasm has barely subsided before you bring her another."
        pl "*Moans loudly* Cum with me! AHh!! Fill me up with your warm cum!! MMm!!"
        pl "I know you want to cum in my tight little pussy! AHh!! The only man in the world that gets to enjoy it! AHhH!!"
        with vpunch
        scene ch6sc02_874 with dissolve
        mc "Fuu...! Hnnfh! Here it comes!! MMm!"
        with vpunch
        pl "*Moans* {b}NNNGHH!! MM!!{/b} Yes! Ahh!! I feel you baby! You’re filling me up! AHhH!"
        scene ch6sc02_876 with dissolve
        $ renpy.pause(0.7)
        scene ch6sc02_877
        with vpunch
        $ renpy.pause(0.7)
        pl "MMmm... It feels so good... warm and satisfying."
        mc "*Panting* Heh... that was something... Mmm."
        mc "I love knowing that I'm the only man who'll ever know the feeling of your pussy."
        scene ch6sc02_878 with dissolve
        pl "*Giggles* Me too. Knowing I belong to you and your cock... it makes me feel excited and at peace."
        pl "This felt soooo good... Mmm."
        scene ch6sc02_879 with dissolve
        mc "Amazing, Pearl... it felt fucking amazing."
        scene ch6sc02_878 with dissolve
        pl "*Giggles exhaustedly* You brought me to the edge of the seas and then kept going... Mmm."
        pl "You think anyone heard us?"
        scene ch6sc02_879 with dissolve
        mc "Most likely... but, do we care?"
        scene ch6sc02_878 with dissolve
        pl "No, my sharky... we definitely don’t. *Giggles*"
        scene ch6sc02_880 with dissolve
        pl "*Yawns* Hnnnghh!"
        pl "I want nothing more than to continue... *Sighs* But my body is screaming at me to get some rest."
        mc "*Chuckles* Yeah... I’m right with you on that sentiment."
        scene ch6sc02_879 with dissolve
        mc "Think you can handle sleeping in your own bed now?"
        scene ch6sc02_878 with dissolve
        pl "You literally just fucked every worry out of my mind... I’ll be sleeping like a baby. MMm."
        scene ch6sc02_879 with dissolve
        mc "C’mon on, let’s get some rest."
        scene black with Dissolve(1)
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        "Pearl cleans up the leftovers of your primal act, and the two of you get comfortable."
        scene ch6sc02_810 with Dissolve(1)
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        scene ch6sc02_810
        pl "I still can’t believe we just did that... we’ve been going at it like wild animals since the first night in the ship's cabin."
        mc "Are you suggesting we slow down?"
        scene ch6sc02_811 with dissolve
        pl "If you ever suggest such a thing again... I’ll poke you with the pointy end of my blades!"
        scene ch6sc02_812 with Dissolve(1.5)
        mc "*Chuckles* My bad. Goodnight, beautiful."
        pl "*Giggles softly* Night, night, sharky!"
        $ pearl_trust += 10
        "Pearl's feelings for you have grown, her trust increased by {size=+3}{b}{color=#2bff8b}10{/color}{/b}{/size}."
        scene ch6sc02_813 with Dissolve(1.5)
        $ renpy.pause(1.5)
        scene black with Dissolve(2)
        "It doesn’t take long before sleep claims the both of you..."

    else:
        scene black with Dissolve(1)


    scene ch6sc02_881 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}Hnnghh...{/i}"
    mct "{i}It’s still dark out? Wonder what time it is...{/i}"
    scene ch6sc02_882 with dissolve
    mct "{i}These huts get pretty hot, I could do with some fresh air.{/i}"
    scene ch6sc02_883 with dissolve
    mct "{i}Mmm... incredible.{/i}"
    mct "{i}The night air is nice here, cool and fresh.{/i}"
    scene ch6sc02_884 with dissolve
    mct "{i}The village seems quiet at night, just a few guards patrolling the perimeter.{/i}"
    scene ch6sc02_885 with dissolve
    mct "{i}Hmm ... Echo.{/i}"
    mct "{i}I could see if she’s awake. She did say I was free to visit her any time.{/i}"
    scene ch6sc02_886 with dissolve
    mct "{i}It would be nice to spend some more time alone with her.{/i}"
    scene ch6sc02_887 with dissolve
    mct "{i}No wonder Echo is in peak condition... having to get up here day in and day out? Pff.{/i}"
    scene ch6sc02_888 with dissolve
    mct "{i}I need to be quiet. If she’s sleeping, I don’t want to wake her.{/i}"
    mct "{i}Her hospitality might end if an outsider turns up in her bedchamber while she’s sleeping.{/i}"
    scene ch6sc02_889 with dissolve
    mct "{i}Hmh? Is she... meditating?{/i}"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_890 with dissolve
    ec "*Quietly* If you’re so eager to greet death, then my blade will guide you there..."
    scene ch6sc02_891 with dissolve
    mc "Hey-"
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_892
    with vpunch
    ec "{b}So be it! I’ll be the last thing you see!{/b}"
    with vpunch
    mc "{b}WOAH! Echo!{/b} It’s me!"
    scene ch6sc02_893 with dissolve
    ec "*Gasps* [mc]?!"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    ec "By the G-Goddesses! I’m sorry!"
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_894 with dissolve
    ec "W-What have I done?! Goddesses forgive me."
    ec "First Marah sends you to your doom, and now I nearly did the same."
    scene ch6sc02_895 with dissolve
    mc "Echo..."
    ec "Uuurrgh!"
    mc "Echo! Relax, it’s okay... I’m fine."
    scene ch6sc02_896 with dissolve
    ec "It is not..."
    ec "I nearly killed you... my blade nearly ended your life."
    scene ch6sc02_897 with dissolve
    mc "Hey... It’s alright. Really..."
    mc "You thought I was an intruder, it could’ve been anyone sneaking up on you."
    mc "You were defending yourself, you’re probably just a little jittery with all that's been going on."
    scene ch6sc02_898 with dissolve
    ec "I know, b-"
    scene ch6sc02_899 with dissolve
    mc "Echo, enough..."
    mc "You don’t need to explain. Besides, nothing happened."
    mc "And if I’m being honest, I’m happy to know you can handle yourself."
    ec "..."
    scene ch6sc02_900 with dissolve
    mc "Shouldering the weight of an entire tribe, then having outsiders come into your midst, it is bound to leave you on edge."
    mc "Being the leader and caring for your people's wellbeing, that’s... that’s not an easy burden to bear."
    scene ch6sc02_901 with dissolve
    ec "It is my duty and my honor to protect the tribe."
    scene ch6sc02_902 with dissolve
    ec "It’s my mother’s legacy... it passed down to me when she was taken from us."
    scene ch6sc02_901 with dissolve
    ec "To honor her, and because of our horrific past, I needed to become a capable fighter, a ferocious warrior."
    ec "So that if the horrors of our past should ever return... I will be able to fight."
    ec "To protect my loved ones, and not be made a victim."
    scene ch6sc02_903 with dissolve
    mc "You’re definitely both capable and ferocious when you need to be..."
    mc "The speed and agility you just demonstrated... it's on the upper end of what the human body is capable of."
    scene ch6sc02_904 with dissolve
    mc "And... you're also kind when there’s no need for hostility."
    ec "..."
    scene ch6sc02_905 with dissolve
    ec "Y-You think I’m kind?"
    scene ch6sc02_904 with dissolve
    mc "Mmm. You’ve been nothing but warm towards me ever since I woke up in that hut."
    scene ch6sc02_903 with dissolve
    mc "It would’ve been much easier for you to just keep me there in chains. You wouldn’t have upset anyone in the tribe."
    mc "But you stuck your neck out for me and gave me a chance, you even allowed me to roam freely."
    scene ch6sc02_901 with dissolve
    ec "You’re kind too... and brave, quite... brave."
    scene ch6sc02_903 with dissolve
    mc "*Chuckles* You said brave twice."
    scene ch6sc02_901 with dissolve
    ec "Oh... *Giggles* I suppose that means I really believe it to be true, then."
    scene ch6sc02_906 with dissolve
    ec "The more I know of you, the more I see a hero. Every moment we share... I see you more and more clearly."
    scene ch6sc02_907 with dissolve
    mc "A hero? ... Echo, that’s the last thing I am."
    mc "I just act according to my own will and beliefs."
    scene ch6sc02_906 with dissolve
    ec "Heroes never proclaim themselves as such."
    scene ch6sc02_908 with dissolve
    ec "Therefore, you're not qualified to make that judgment."
    ec "Only other people can decide whether a person has the spirit of a hero within."
    scene ch6sc02_909 with dissolve
    ec "Come, join me..."
    scene ch6sc02_910 with dissolve
    ec "I wish to celebrate your heroism and survival of the Trial of A'khans."
    ec "You have accomplished something... something nobody living has ever done."
    scene ch6sc02_911 with dissolve
    mc "Sure... I'm not one to refuse a drink with a queen."
    mc "But, despite my recent accomplishment, I’ve never really been one to boast."
    scene ch6sc02_912 with dissolve
    ec "I haven’t seen you be boastful even once. You are allowed to celebrate..."
    scene ch6sc02_913 with dissolve
    ec "Everyone should be free to take pride in their accomplishments, even celebrate some of them."
    scene ch6sc02_914 with dissolve
    ec "As long as it’s not overly done"
    ec "Even you, the non-boasting [mc]. *Giggles softly*"
    scene ch6sc02_915 with dissolve
    mc "*Chuckles* It’s good to see you in such a cheerful mood."
    mc "Suji mentioned you were upset earlier. I'm glad that isn't the case anymore."
    scene ch6sc02_916 with dissolve
    ec "I have good reason to be in a good mood, there is much to celebrate."
    mc "Is there? Like what?"
    scene ch6sc02_917 with dissolve
    ec "Like you being alive! Like you surviving the Trial of A'khans-"
    ec "-Like me not accidentally killing you. And you just being... wonderful."
    scene ch6sc02_918 with dissolve
    ec "To your success in the Trial of A'khans!"
    scene ch6sc02_919 with dissolve
    mc "*Chuckles* Cheers!"
    ec "*Giggles* Cheers!"
    scene ch6sc02_920 with dissolve
    $ renpy.pause(1)
    mc "Mmmh."
    scene ch6sc02_921 with dissolve
    mc "Aahh... that tastes familiar."
    mc "It’s very potent but sweet... what is it?"
    scene ch6sc02_922 with dissolve
    ec "It’s partly made from the berries you ate. Remember how I told you about our wine becoming quite popular on the mainland?"
    ec "We call it A’zul wine because it’s made with the A’zul berries that grow throughout the jungle."
    ec "We mix those with the blacknip berries you and Pearl ate, to get a combination without side effects."
    scene ch6sc02_921 with dissolve
    mc "I think I’ve tasted it before at a royal banquet."
    scene ch6sc02_922 with dissolve
    ec "Oh? You're royalty?"
    scene ch6sc02_921 with dissolve
    mc "*Chuckles* No, I’m just a commoner. But I recently befriended some of the royal family through my work."
    scene ch6sc02_922 with dissolve
    ec "I do not know of this royal family, but I believe you."
    ec "You’re quite interesting, Outsider."
    scene ch6sc02_923 with dissolve
    mc "You wound me, Echo."
    scene ch6sc02_924 with dissolve
    ec "Oh? How have I wounded you?"
    scene ch6sc02_925 with dissolve
    mc "I thought, out of everyone here, I wouldn’t hear that name from you."
    ec "..."
    scene ch6sc02_926 with dissolve
    ec "[mc]... I... *Sighs deeply* I’m sorry. I didn't mean it like that."
    scene ch6sc02_921 with dissolve
    mc "Echo, relax... I'm just messing with you."
    scene ch6sc02_924 with dissolve
    ec "Oh? You mess with me in my own chambers?"
    ec "Just for that, I’ll call you outsider for another day."
    scene ch6sc02_921 with dissolve
    mc "*Chuckles* Anything but that! Given my recent victory in your ancient tombs, haven’t I earned it?"
    scene ch6sc02_922 with dissolve
    ec "*Snickers softly* Ahh... and now the boasting begins!"
    scene ch6sc02_927 with dissolve
    ec "I admit, you have earned something."
    ec "You have earned my respect... [mc]."
    scene ch6sc02_928 with dissolve
    mc "That’s more like it!"
    scene ch6sc02_929 with dissolve
    ec "No, no..."
    ec "I am not jesting."
    scene ch6sc02_921 with dissolve
    mc "Oh?"
    scene ch6sc02_922 with dissolve
    ec "You very much deserve every bit of respect you have earned."
    ec "You have returned to us, unscathed from a place lost to time."
    scene ch6sc02_929 with dissolve
    ec "You’re the only living being that knows what lies down there."
    ec "You alone have seen it with your own eyes."
    scene ch6sc02_927 with dissolve
    ec "And as if that weren’t enough, to further demonstrate the heroism that resides within you..."
    ec "You recovered an ancient relic that was once bestowed upon my people by the gods themselves."
    scene ch6sc02_924 with dissolve
    ec "To you, [mc]!"
    ec "Raider of tombs, hero of the jungle, handsome adventurer, and our potential future A’khan!"
    scene ch6sc02_919 with dissolve
    mc "*Chuckles* Thank you, Echo."
    mc "*Scoffs quietly* Potential future A’khan? ... Has a nice ring to it, though."
    scene ch6sc02_920 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_921 with dissolve
    mc "Mhm. I can see why the lords of the capital would praise this wine."
    mc "It even tingles my tongue on it’s way down."
    scene ch6sc02_927 with dissolve
    ec "*Giggles softly* It certainly does!"
    ec "You like it then?"
    scene ch6sc02_928 with dissolve
    mc "*Nods* Mhh, I’m happy you chose to share it with me."
    scene ch6sc02_930 with dissolve
    ec "Your name... it has the same effect on me."
    scene ch6sc02_931 with dissolve
    mc "My name?"
    ec "*Nods* ..."
    scene ch6sc02_930 with dissolve
    ec "It is a good name, a warrior's name."
    ec "[mc]."
    scene ch6sc02_927 with dissolve
    ec "*Giggles* Yes, it definitely tingles my tongue, same as the wine."
    scene ch6sc02_928 with dissolve
    mc "*Chuckles* Glad to hear that’s the effect I have."
    mc "You’ve been very open and welcoming to me and to my friend."
    scene ch6sc02_923 with dissolve
    mc "And, despite Marah’s attempt at ending our friendship prematurely..."
    mc "I feel that you and I, we... we understand each other."
    scene ch6sc02_931 with dissolve
    mc "We have a mutual respect and admiration for one another."
    scene ch6sc02_932
    with vpunch
    ec "Ugh! May the goddesses take pity on Marah! And may their will force her to leave you be!"
    scene ch6sc02_926 with dissolve
    ec "I haven’t spoken to her since... I was so upset that I didn’t even leave the temple."
    scene ch6sc02_918 with dissolve
    mc "Then cheers to your worries not coming to fruition."
    scene ch6sc02_919 with dissolve
    ec "I’ll cheer to that!"
    scene ch6sc02_920 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_922 with dissolve
    ec "Thank you..."
    ec "You’re good at snapping me right out of my fugue, and back to the... lovely present."
    scene ch6sc02_921 with dissolve
    mc "You’re welcome."
    scene ch6sc02_929 with dissolve
    ec "You need not worry about Marah. I was very stern with her after she tricked you."
    scene ch6sc02_925 with dissolve
    mc "Oh? You don’t think she’ll attempt anything again?"
    mc "She seems very paranoid and hellbent on seeing me as the devil incarnate."
    mc "In my experience, paranoid people don't always act rationally."
    scene ch6sc02_926 with dissolve
    ec "She overstepped... there’s no denying it."
    scene ch6sc02_929 with dissolve
    ec "But she will not harm you or your friend."
    ec "I promise you that."
    scene ch6sc02_921 with dissolve
    mc "How can you know?"
    scene ch6sc02_933 with dissolve
    ec "Marah is the high priestess and second in command, second only to me."
    ec "But when push comes to shove, she cannot gainsay my decisions."
    ec "I am the A’nu of my people, and she serves as my counselor... not our ruler."
    scene ch6sc02_928 with dissolve
    mc "Well, I don’t trust Marah and her intentions... but I do trust you."
    mc "If you say she won’t act out again, I’ll believe you."
    mct "I won’t trust that old hag, though. Echo's clearly fiercely loyal to her people."
    mct "She could be naive to Marah’s nature."
    scene ch6sc02_914 with dissolve
    ec "One more! I wish to cheer again! *Giggles*"
    scene ch6sc02_915 with dissolve
    mc "I’m surprised there’s anything left."
    ec "Nooo! We’re down to the last drop!"
    mc "Seems like we really went through it."
    scene ch6sc02_917 with dissolve
    ec "Perfect! *Soft giggle* It has served its purpose then!"
    scene ch6sc02_918 with dissolve
    mc "Our last cheer. What should we make it about?"
    scene ch6sc02_919 with dissolve
    ec "Let’s cheer to having found each other in a world that's so big and hectic."
    ec "That we can share this moment of peace and happiness, together."
    mc "Now that’s something I’ll happily cheer to. Cheers!"
    scene ch6sc02_920 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_923 with dissolve
    ec "MMh..."
    scene ch6sc02_934 with dissolve
    ec "I’m happy you came to me tonight."
    scene ch6sc02_935 with dissolve
    mc "So am I. But... I'd better take my leave."
    ec "..."
    scene ch6sc02_936 with dissolve
    ec "You’re leaving? So soon?"
    scene ch6sc02_935 with dissolve
    mc "Well, it’s pretty late. I’m sure you’d like some peace and quiet to sleep?"
    scene ch6sc02_937 with dissolve
    ec "Nonsense! Who told you that? ... I know it wasn’t me."
    scene ch6sc02_938 with dissolve
    mc "Nobody, I just assumed -"
    scene ch6sc02_937 with dissolve
    ec "Assumptions are the devils work!"
    scene ch6sc02_938 with dissolve
    mc "So, you want me to stay?"
    scene ch6sc02_939 with dissolve
    ec "Of course... the night is still young."
    ec "Please, stay."
    scene ch6sc02_938 with dissolve
    mc "You’re not worried Marah might come bursting in and interrupt us again?"
    scene ch6sc02_937 with dissolve
    ec "Didn’t we just address that but a moment ago?"
    ec "She has no say over me, or what I do, or who I choose to spend my time with."
    scene ch6sc02_939 with dissolve
    ec "If she comes in here, interrupting us again... she will get intimate with the prison cells she despises so much."
    scene ch6sc02_940 with dissolve
    mc "I’m glad you enjoy our quality time together."
    "She lets out a soft giggle."
    scene ch6sc02_941 with dissolve
    ec "Likewise... it pleases me."
    ec "Would you like to join me?"
    scene ch6sc02_942 with dissolve
    ec "My bed is..."
    ec "Far more comfortable than those chairs."
    scene ch6sc02_943 with dissolve
    mc "Mmm, I believe you."
    scene ch6sc02_944 with dissolve
    $ renpy.pause()
    scene ch6sc02_945 with dissolve
    $ renpy.pause()
    scene ch6sc02_946 with dissolve
    ec "What will it be, Hero?"

    ####Choice####
    menu:
        "Join her in bed. ({color=#ff8cdd}Romance{/color})":
            scene ch6sc02_953 with dissolve
            "As you walk towards her, Echo studies every movement of your body attentively."
            ec "..."
            $ ec_trust += 3
            "She is pleased that your desires match her own, Echo’s trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch6sc02_954 with dissolve
            "Her body relaxes as if your choice to join her has put her at ease."
            scene ch6sc02_955 with dissolve
            "Her hazel eyes brim with life..."
            $ ec_path = True
            "... and a fiery passion that has been building from the moment you met."
            scene ch6sc02_956 with dissolve
            ec "Your choice... pleases me."
            ec "Tonight, you’ll belong to me... you are mine."
            scene ch6sc02_957 with dissolve
            mc "And you’ll be mine."
            ec "*Nods* Mmm."
            scene ch6sc02_956 with dissolve
            ec "I’ll be yours."
            scene ch6sc02_957 with dissolve
            mc "That’s what I like to hear."
            mc "Just one thing: earlier you said that all the village leaders, including you, are virgins."
            mc "That you're all saving yourselves for the one who was promised. Your future A'khan?"
            scene ch6sc02_956 with dissolve
            ec "That is true."
            scene ch6sc02_958 with dissolve
            ec "And it's why I invited you into my bed. [mc], my body has been on fire since we met."
            ec "I’ve felt things I’ve never experienced before... powerful things."
            scene ch6sc02_956 with dissolve
            ec "You’ve proven so much in such a short time, and while there is still much to prove and learn..."
            ec "My body, mind, and soul all tell me that you’re... {b}him{/b}. The one who was promised."
            ec "You have already completed the first trial and taken the first step towards becoming our A'khan."
            scene ch6sc02_958 with dissolve
            ec "If there was any doubt in me, I would've sent you back to your hut much sooner..."
            scene ch6sc02_957 with dissolve
            mc "Echo... I-"
            scene ch6sc02_959 with dissolve
            ec "Sshh... I am certain."
            ec "Lie with me... Hero."
            scene ch6sc02_960 with dissolve
            $ renpy.pause()
            ec "..."
            scene ch6sc02_961 with dissolve
            mc "You’re a blessed woman, Echo..."
            mc "Stunningly beautiful. You have an exotic body, perfectly filled out, yet firm and athletic."
            scene ch6sc02_962 with dissolve
            mc "And your hazel eyes, one look into them and any man would be mesmerized."
            ec "*Giggles softly* ..."
            scene ch6sc02_963 with dissolve
            ec "Curious. Despite your hard exterior, heroic nature and bravery..."
            scene ch6sc02_964 with dissolve
            ec "... You’re still so... tender and attentive. Mmm."
            scene ch6sc02_965 with dissolve
            ec "It's so alluring... a man who cares."
            scene ch6sc02_966 with dissolve
            mc "If I care for a woman, she will be taken care of."
            scene ch6sc02_964 with dissolve
            ec "I believe you. Mmmh... but tonight, I will take care of you."
            scene ch6sc02_965 with dissolve
            ec "I will treat you to pleasures no outsider will ever experience."
            scene ch6sc02_967 with dissolve
            ec "Tonight, [mc]... I, the A’nu, will serve you."
            scene ch6sc02_968 with dissolve
            $ renpy.pause(1)
            "Echo gently pushes you down, shifting herself on top of you."
            scene ch6sc02_969 with dissolve
            $ renpy.pause(1)
            mct "{i}Mmm ... she’s fucking sexy.{/i}"
            mct "{i}Nothing better than a woman who goes for what she wants.{/i}"
            scene ch6sc02_970 with dissolve
            ec "Mmmh..."
            scene ch6sc02_971 with dissolve
            ec "Your body is firm, powerful, warm... it’s as if you were carved by Malanthe herself."
            ec "To match my every desire..."
            mc "Years of adventuring and fighting for survival does that."
            ec "*Scoffs lightly* It certainly made its mark. Your body is that of a great warrior."
            scene ch6sc02_972 with dissolve
            ec "I desire... to see your weapon."
            ec "I... am curious to finally see the real thing."
            scene ch6sc02_973 with dissolve
            ec "*Gasps* {b}OH!{/b} By the Goddesses! I knew I felt something powerful when I was on top of you."
            ec "It’s so... hard? And big?"
            scene ch6sc02_974 with dissolve
            mc "That’s what happens when a woman arouses a man."
            ec "According to the etchings on our stone tablets, this... spear of yours is supposed to pierce me?"
            mc "That is one way to put it... it serves to connect a man and woman in euphoric pleasure."
            scene ch6sc02_975 with dissolve
            ec "And... I’m the cause for this... great weapon of yours?"
            scene ch6sc02_974 with dissolve
            mc "Mhm. I don’t see any other beautiful and exotic women in the room with us."
            scene ch6sc02_975 with dissolve
            ec "I like this! Your spear pleases me, I find it alluring."
            ec "Allow me to feel it..."
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc02_976 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            mc "Mmm..."
            ec "Does my touch please you?"
            mc "Y-Yeah... Mmmm, keep doing that."
            scene ec_lewd1 with dissolve
            $ renpy.pause()
            ec "I may not have the experience that the Maidens of Malanthe have..."
            mc "Fuu... you’re doing well- Mmm... I’m glad to be your first."
            ec "And my only. Once an A’nu gives herself to a man, it is permanent. Their bond will never be broken."
            mc "MMm... is that so? Then I’m a lucky man to be chosen by you."
            ec "It’s so warm... hard and firm, yet... it feels so alive..."
            scene ch6sc02_975 with dissolve
            ec "I want to taste you... [mc], I desire your spear."
            scene ch6sc02_974 with dissolve
            mc "I must be dreaming."
            scene ch6sc02_977 with dissolve
            ec "MMmh... we’re both wide awake... but now, I’m going to blur the lines for us with my mouth."
            mc "Oohh, fuck... your lips- Mmm..."
            scene ec_lewd2 with dissolve
            $ renpy.pause()
            mc "Mmm... Fuck..."
            mc "This is amazing, Echo... Hnngh."
            mct "{i}Fuck... I can barely hold back, I’m so close to flipping her over and taking her right here.{/i}"
            mct "{i}But she’s a virgin... and a queen. I’ll follow her lead tonight and see how far she is comfortable with taking this.{/i}"
            ec "Mmfhh... you are... delicious. More, I desire more- MMmnh!"
            scene ec_lewd3 with dissolve
            $ renpy.pause()
            mc "Fuuu! MMh! Your mouth is incredible- Ahhh... so warm and wet, and the way your exotic lips latch on to my cock."
            ec "[mc]... Mmmh... I wish to give you so much more..."
            ec "I can feel all your desires flow through your cock- MMmm..."
            mc "I’d love to give you my spear... Mmm."
            ec "Mmfhh... Oh? Would you?"
            ec "Speaking to your A’nu like that? So indecent... MMm! *Tightens lips*"
            with vpunch
            mc "Ahhhgnh! Mmm..."
            ec "MMffgh? Did I hurt you? Mmm..."
            mc "N-No... Mmm! You’re doing perfectly. If you keep sucking like that, I’ll finish in only a moment -"
            with vpunch
            ec "*Sucks harder* MMffgh! Give me your essence! Share all of your desire with me - MMfhh!"
            with vpunch
            ec "I want to fully taste you! [mc], let me taste your heroic essence!"
            scene ch6sc02_978 with dissolve
            $ renpy.pause(1)
            mc "Fuck-Ahhgn!! Echo-Mmfhh!"
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            scene ch6sc02_979 with dissolve
            ec "MMfhh... fill me with your desire- Nnnghh!"
            with vpunch
            mc "Fuu... your mouth is amazing, Echo- Mm!"
            scene ch6sc02_980 with dissolve
            ec "*Muffled gasp* Mmffph! Mmhfp!! So much... Mmm! So delicious..."
            ec "*Kiss* Your heroic spear... Mmm... has left me satisfied. *Licks* Nnnghh..."
            mc "I want to taste you as well."
            scene ch6sc02_981 with dissolve
            ec "Not tonight. But maybe... I’ll allow you to enjoy me again, soon..."
            ec "Are you not pleased with my efforts?"
            scene ch6sc02_982 with dissolve
            mc "Oh, I am... incredibly so. Which is why I’m eager for more."
            ec "*Mwah*"
            scene ch6sc02_981 with dissolve
            ec "Good... I wish for your desire for me to grow."
            scene ch6sc02_982 with dissolve
            ec "Mmmh..."
            scene ch6sc02_981 with dissolve
            ec "And when it has grown to the point that just one look from me will make you hard..."
            ec "Maybe then... *Giggles*"
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc02_983 with dissolve
            play music forest_1 fadein 1.0
            #stop music fadeout 1.0
            mc "If you keep holding my cock like that, I’ll reach that point sooner than you think."
            ec "*Scoffs lightly* ..."
            scene ch6sc02_984 with dissolve
            ec "We’ll see, handsome hero."
            ec "But now, I am tired. It is time we part ways for the night."
            scene ch6sc02_985 with dissolve
            ec "Know that you have satisfied me greatly, [mc]."
            ec "I will thank the goddesses for sending you to me tonight. It has pleased me greatly-"
            ec "-To know our desire is mutual."
            scene ch6sc02_986 with dissolve
            mc "Mmh, me too. At first I was worried you might be asleep, but I wanted to see you... so I had to check."
            scene ch6sc02_985 with dissolve
            ec "And I hoped you would come to me... it seems our desires are perfectly matched."
            scene ch6sc02_986 with dissolve
            mc "I would say so. *Chuckles*"
            scene ch6sc02_985 with dissolve
            ec "Our desires are one of the three pillars of fate, together with love and life."
            scene ch6sc02_987 with dissolve
            ec "And tonight... we were fated."
            ec "Chosen by Malanthe herself to share our passion."
            scene ch6sc02_988 with dissolve
            mc "*Chuckles* Just tonight?"
            ec "Giggles softly* ..."
            scene ch6sc02_989 with dissolve
            ec "We’ll se ..."
            mc "Goodnight, Echo."
            ec "Goodnight, [mc]... here, a parting token of my affection."
            scene ch6sc02_990 with dissolve
            ec "Mmm..."
            mc "Nnnh, her lips are perfect... soft and full."
            scene ch6sc02_991 with dissolve
            ec "*Mwahh* ..."
            scene ch6sc02_992 with dissolve
            ec "You made me feel special tonight... thank you."
            ec "I pray our dreams will unite us once more."
            scene ch6sc02_989 with dissolve
            mc "Me too. I’ll see you tomorrow."
            ec "*Nods* Mmh... see you tomorrow."
            scene ch6sc02_990 with dissolve
            ec "*Mwaah* Nnnghh... just one more for the night."
            mc "Mmh... I’ll never deny these lips of yours."
            scene ch6sc02_989 with dissolve
            ec "Good... it pleases me to know this. Now, go... rest and regain your strength."
            ec "Perhaps tomorrow, we can investigate this ambassador that you’re searching for."
            mc "I would appreciate the help. Goodnight, Echo."

        "Say goodnight. ({color=#2bff8b}Friendly{/color})":
            scene ch6sc02_947 with dissolve
            mc "I’m going to call it a night, Echo."
            mc "It’s been the longest day, to say the least. I’m in dire need of rest."
            scene ch6sc02_948 with dissolve
            ec "That is... unfortunate."
            mc "I hope I haven’t offended you-"
            scene ch6sc02_949 with dissolve
            ec "Offended? No, you’ve done nothing of the sort... you need not worry."
            ec "We’ll have other chances to share moments in private..."
            scene ch6sc02_950 with dissolve
            ec "Of this I am certain. I’ll pray to the goddesses to make it so."
            scene ch6sc02_951 with dissolve
            mc "*Chuckles* I bet."
            ec "Hmmh?"
            scene ch6sc02_949 with dissolve
            ec "This phrase is unfamiliar to me, I do not know it."
            scene ch6sc02_951 with dissolve
            mc "Oh, it just means that I’m certain as well."
            mc "Saying you’ll bet on something means you believe in something enough that you would risk something of value."
            scene ch6sc02_950 with dissolve
            ec "Ahh... then, it pleases me to hear you say this."
            ec "I shall bet on it also."
            ec "May your dreams be sweet and filled with wonder, Hero..."
            scene ch6sc02_951 with dissolve
            mc "You too, Echo. I’ll see you tomorrow."
            scene ch6sc02_952 with dissolve
            $ renpy.pause(1)

    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_883 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "{i}Hhm... Echo seems so genuine.{/i}"
    mct "{i}Despite her people's past, she doesn’t hold grudges against those who weren’t involved.{/i}"
    mct "{i}Unlike that hag... Marah. She seems to be hellbent on convicting me of being a harbinger of evil.{/i}"
    scene ch6sc02_885 with dissolve
    mct "{i}It’s still hard to believe we’ve found a place like this. It really feels like a marvel of a time long lost.{/i}"
    scene ch6sc02_886 with dissolve
    mct "{i}To build a structure like this temple, not to mention the vast ruins below it ...{/i}"
    mct "{i}It would take a lot of manpower and time, even in today's age... let alone back then.{/i}"
    scene ch6sc02_883 with dissolve
    mct "{i}Being out here... it reminds me of the early days before me and Oren settled in Senju.{/i}"
    scene ch6sc02_993 with dissolve
    mc "Huh?"
    mc "Is someone there?"
    scene ch6sc02_994 with dissolve
    "Your call is met with silence and the ambiance of cicadas in the distance."
    scene ch6sc02_995 with dissolve
    mct "Guess I better get back to the hut and rest up for the night."
    "As you take a few steps towards your hut, you hear the crunch of a twig snapping not far behind you."
    scene ch6sc02_996 with dissolve
    "Your eye is drawn to the silhouette of a women hiding in the foliage."
    mc "There you are, come out!"
    scene ch6sc02_997 with dissolve
    vx "AH!!"
    scene ch6sc02_998
    with vpunch
    mc "Woah! ... Huh?"
    vx "..."
    mc "Vex?"
    scene ch6sc02_999 with dissolve
    vx "Outsider! ... Sneaking around our village!"
    scene ch6sc02_1000 with dissolve
    mc "Your name is Vex, right?"
    scene ch6sc02_1001 with dissolve
    vx "*Nods* Y-Yes, that is my name."
    vx "B-But, it matters not what my name is!"
    vx "What are you doing out here in the cover of darkness?"
    scene ch6sc02_998 with dissolve
    mc "In the cover of darkness? You mean night? I was just getting some fresh air ... the huts are a little stuffy."
    scene ch6sc02_1001 with dissolve
    vx "Taking a walk? Hmm ... maybe."
    scene ch6sc02_1002 with dissolve
    vx "Or maybe you were checking our defenses!? Looking for exploits to enslave us!"
    scene ch6sc02_1003 with dissolve
    mc "Vex, please..."
    mc "I’m a guest here, enough games..."
    scene ch6sc02_1002 with dissolve
    vx "I am not playing games, Outsider..."
    vx "I am fulfilling my duty to my tribe and my people."
    scene ch6sc02_1004 with dissolve
    vx "So that I may become a great huntress, one day."
    vx "Maybe even a war-maiden, if the goddesses bless me with enough determination."
    scene ch6sc02_1005 with dissolve
    mc "I promise you, I’m not a threat to you or your people."
    mc "I’m an adventurer. I didn’t even know your village or people existed a couple of days ago."
    mc "I’m only here on Aruna to find an ambassador that was shipwrecked here."
    scene ch6sc02_1006 with dissolve
    vx "You could be telling the truth..."
    vx "But from what I’ve heard, the ones who enslaved us... they came under false pretenses. Their evil masked by an illusion of friendship."
    scene ch6sc02_1005 with dissolve
    mc "Vex ... do you see me lugging around weapons? Do I have an army at the ready?"
    scene ch6sc02_1004 with dissolve
    vx "No. But it matters not!"
    vx "I am on patrol tonight, and I will do my duty."
    scene ch6sc02_1005 with dissolve
    mc "I feel much safer with you being on patrol. Seeing how alert you are brings me some peace of mind."
    mc "But, I’d still like to finish my walk and enjoy the cool night air."
    scene ch6sc02_1007 with dissolve
    mc "If your duty permits it, would you like to join me?"
    "The young aspiring huntress looks at you with disbelief."
    vx "..."
    scene ch6sc02_1008 with dissolve
    vx "N-Never! You’ll try something..."
    mc "Vex, I give you my word... I’ll be on my best behavior."
    scene ch6sc02_1007 with dissolve
    mc "And... it would mean you'd get to keep an eye on me. You could make sure I don’t mess about."
    mc "You’ll be able to protect your people most effectively if you’re watching me closely, no?"
    scene ch6sc02_1008 with dissolve
    vx "Well..."
    vx "Hmmpfhh..."
    scene ch6sc02_1009 with dissolve
    vx "The things you say do make sense. Keeping a close eye on you would be wise."
    vx "The wellbeing of the tribe rests on my shoulders tonight, and accompanying you would serve that purpose."
    scene ch6sc02_1010 with dissolve
    vx "Fine, Outsider."
    vx "I will keep an eye on you tonight."
    scene ch6sc02_1011 with dissolve
    mct "{i}There’s a slightly rosy tint to her cheeks. It could be the cool air, or she could be blushing.{/i}"
    mct "{i}*Chuckles* Cute. She may be developing a bit of a crush. She was flustered when we observed her training session as well.{/i}"
    scene ch6sc02_1012 with dissolve
    vx "What is it? Why are you smiling?"
    vx "Tell me."
    scene ch6sc02_1013 with dissolve
    mc "*Chuckles* It’s nothing. I’m just happy you decided against spearing me."
    vx "Who says I’m not still considering it?"
    vx "..."
    scene ch6sc02_1014 with dissolve
    vx "So..."
    vx "Everyone has been talking about you returning from the ancient tombs."
    scene ch6sc02_1012 with dissolve
    vx "That you... completed the first Trial of A'khans?"
    scene ch6sc02_1015 with dissolve
    mc "Apparently so. Honestly, I was just trying to survive and find a way out after your high priestess forced me down there."
    scene ch6sc02_1016 with dissolve
    vx "Her actions were foolish and reckless..."
    scene ch6sc02_1017 with dissolve
    vx "But..."
    vx "I’m glad you didn’t suffer a horrible death down there."
    mc "Oh? You are?"
    scene ch6sc02_1016 with dissolve
    vx "I said so, didn't I?"
    scene ch6sc02_1014 with dissolve
    vx "So... how did you manage it?"
    scene ch6sc02_1012 with dissolve
    vx "How were you able to accomplish what no other has?"
    scene ch6sc02_1013 with dissolve
    mc "Experience."
    vx "You have experience with ancient tombs, Outsider?"
    mc "*Chuckles* Not exactly, but I’ve lived my entire life on the move."
    mc "So, I’ve experienced a variety of sticky situations."
    scene ch6sc02_1014 with dissolve
    vx "You’ve lived a harsh life?"
    mc "Mhm."
    scene ch6sc02_1012 with dissolve
    vx "G-Good... our elders say that harsh times make warriors strong."
    vx "Completing the Trial of A'khans... you must be a strong warrior, Outsider."
    scene ch6sc02_1013 with dissolve
    mc "I suppose I am? Oh, and I found this necklace down in the ruins too."
    mc "It was guarded by a golem and locked in a treasury."
    scene ch6sc02_1018 with dissolve
    vx "You did? T-This necklace?"
    mc "Mhm, that’s the one."
    vx "I’ve never seen anything like it..."
    scene ch6sc02_1019 with dissolve
    vx "It feels... heavy, and warm to the touch."
    vx "My fingers... I cannot move it in the slightest!"
    mc "Yeah, it’s no ordinary necklace. It’s enchanted with some powerful and ancient magic."
    scene ch6sc02_1020 with dissolve
    vx "Powerful and ancient magic..."
    vx "Could it be...?"
    scene ch6sc02_1021 with dissolve
    vx "Our ancestors spoke of a relic that was gifted to our people by Malpheon himself."
    vx "A relic that only the one who was promised could acquire..."
    scene ch6sc02_1022 with dissolve
    mc "From what Echo has told me, and considering where it was located, it seems likely to be that relic, yes."
    vx "..."
    scene ch6sc02_1023 with dissolve
    vx "*Quietly* {size=-10}{b}The one who was promised... fascinating...{/b}{/size}"
    mc "So, you mentioned earlier that you want to become a huntress, maybe even a war-maiden?"
    scene ch6sc02_1013 with dissolve
    vx "Mhm, this is true... a great war-maiden."
    scene ch6sc02_1024 with dissolve
    mc "I was under the impression you were training to become a huntress?"
    vx "For now, this is true."
    scene ch6sc02_1025 with dissolve
    vx "Anyone who wishes to ascend our ranks must start out as a huntress, even our healers and herbalists."
    vx "Although those ones only undergo the huntress training for basic survival skills."
    vx "The training to become a proper huntress, guard or war-maiden is much more rigorous."
    scene ch6sc02_1026 with dissolve
    mc "Interesting system you’ve got. It make good sense that everyone needs to know the basics for surviving in the jungle."
    mc "Even if they aren’t going to be out hunting prey or defending against attackers."
    vx "Everyone must be able to carry their own weight. Otherwise they risk becoming a burden to the tribe... it is known."
    scene ch6sc02_1027 with dissolve
    "You feel a tentative touch on your back."
    vx "Outsider, tell me... these scars..."
    scene ch6sc02_1028 with dissolve
    vx "They interest me."
    scene ch6sc02_1027 with dissolve
    vx "Who... who did this to you, and why?"
    scene ch6sc02_1028 with dissolve
    mc "It wasn’t any one person or event. I’ve gradually acquired them over the years..."
    scene ch6sc02_1027 with dissolve
    vx "In battle, yes?"
    scene ch6sc02_1028 with dissolve
    mc "Mhm... in battle."
    scene ch6sc02_1027 with dissolve
    vx "You are very resilient... and your body is strong like a predator."
    scene ch6sc02_1029 with dissolve
    vx "*Clears throat* S-So..."
    scene ch6sc02_1030 with dissolve
    mc "What is it, Vex?"
    scene ch6sc02_1029 with dissolve
    vx "I have kept my eye on you..."
    vx "And I’ve come to the conclusion that..."
    scene ch6sc02_1031 with dissolve
    vx "For now, I deem that you’re not a direct threat to the tribe or our people."
    vx "You have been honest and respectful."
    scene ch6sc02_1030 with dissolve
    mc "Thank you. I’m glad you joined me for the walk."
    scene ch6sc02_1029 with dissolve
    vx "So am I..."
    vx "I’ll continue my patrol. Goodnight, Outsi... [mc]."
    scene ch6sc02_1032 with dissolve
    mc "Goodnight, Vex."
    vx "..."
    mc "I may use your name, right?"
    "Vex nods at you and smiles, but she cannot bring herself to lock eyes with you again before she walks off."
    scene ch6sc02_1033 with dissolve
    mct "{i}*Chuckles* Seems like she warmed up to me by the end of our walk.{/i}"
    mct "{i}Good. I don’t need any of them siding with Marah and her beliefs. It would be annoying for me and... dangerous for Pearl.{/i}"
    scene ch6sc02_1034 with dissolve
    mct "{i}It seems that completing the first Trial of A'khans has done a great deal to win their respect and interest.{/i}"
    mct "{i}I think Echo said there are three, no, four trials in total? One for each of their ancient temples...{/i}"
    scene ch6sc02_1035 with dissolve
    mct "{i}The one I completed was the Temple of A’nai. Which leaves the trials in the temples of Malanthe, Maia and Gaia for me to complete.{/i}"
    mct "{i}What happens if I do manage to pass all the Trials? Do I become their A’khan?{/i}"
    mct "{i}Based on what they've told me, it seems like I would.{/i}"
    scene ch6sc02_1036 with dissolve
    mct "{i}*Chuckles* From commoner to King of the Jungle? Now that’s a story to tell back home.{/i}"
    mct "{i}The Chambers of Malanthe? Didn’t realize they'd be open this late at night.{/i}"
    scene ch6sc02_1037 with dissolve
    mct "{i}But then again... night is when most people like to unwind and seek pleasure.{/i}"
    mct "{i}Huh? Isn’t that the... Mistress of Malanthe? Sakari, I believe her name was.{/i}"
    scene ch6sc02_1038 with dissolve
    "Your eyes meet as you pass, and she beckons to you with a soft bend of her wrist."
    scene ch6sc02_1039 with dissolve
    mc "Hey... Sakari, was it?"
    sk "Mmh."
    scene ch6sc02_1040 with dissolve
    sk "Outsider, I did not expect to see you again."
    sk "Your good health is... surprising to me."
    scene ch6sc02_1039 with dissolve
    mc "Oh? Why is that?"
    scene ch6sc02_1040 with dissolve
    sk "Marah has been gloating about how she protected the tribe from a great evil by getting rid of you."
    scene ch6sc02_1041 with dissolve
    sk "It pleases me that her boasting was premature."
    scene ch6sc02_1042 with dissolve
    sk "She means well, but by the goddesses... can she be annoying when she feels self-righteous."
    scene ch6sc02_1041 with dissolve
    sk "I’m glad you persevered. That’ll hopefully take her down a few notches."
    scene ch6sc02_1039 with dissolve
    mc "I’ll happily take her down a few more."
    scene ch6sc02_1043 with dissolve
    sk "*Scoffs lightly* Hmph... I’ll have to keep my eye on you. I wouldn’t want to miss that."
    sk "So, what’s all this gossip I hear about you from my maidens?"
    scene ch6sc02_1044 with dissolve
    sk "Did you truly escape Marah’s death trap and conquer our ancient ruins?"
    sk "Did you complete our ancestor's Trial of A'khans and emerge unscathed wearing an artifact of the gods themselves?"
    scene ch6sc02_1045 with dissolve
    sk "If I wasn’t aroused before... I'm certainly getting there now. Mmh..."
    mc "The gossip you heard is true. Seems that information spreads like wildfire in your tribe."
    scene ch6sc02_1044 with dissolve
    sk "When it’s as exciting as this... Mmh... of course news will travel quickly."
    scene ch6sc02_1043 with dissolve
    sk "Outsider, you have caused Marah to look foolish, and you stand before me as a... potential hero."
    scene ch6sc02_1041 with dissolve
    sk "As such, I believe it should be celebrated..."
    scene ch6sc02_1039 with dissolve
    mc "Oh? You have my attention."
    scene ch6sc02_1046 with dissolve
    sk "Behind me, in the main chamber of Malanthe... there is a reward fit for a hero..."
    scene ch6sc02_1047 with dissolve
    sk "Something I believe you will find... {b}very{/b}... appealing."
    sk "Something no man alive has ever had."
    scene ch6sc02_1048 with dissolve
    mc "I’m intrigued."
    mc "When a woman like you makes such a claim... I think any man would be."
    scene ch6sc02_1049 with dissolve
    sk "I'm not concerned what other men want, but you..."
    sk "You are the guest of our A'nu, and you walk the path of A'khan."
    sk "Now... come."
    scene ch6sc02_1050 with dissolve
    sk "This way, Hero... follow me."
    mc "Hero? Not outsider?"
    sk "I have a feeling about you. And if my instincts are correct, it would be silly to call you an outsider."
    scene ch6sc02_1052 with dissolve
    sk "Tonight, you will be pleasured beyond your imagination."
    mc "Will I now? That’s a bold claim."
    sk "Is it? My maidens are devoted to Malanthe, the goddess of pleasure, lust, and desire."
    scene ch6sc02_1053 with dissolve
    sk "Their purpose in life is seeking her favor through offerings of pleasure... and as you know, they’ve never had a man."
    sk "They've never been able to make proper offerings to Malanthe the way she intended it."
    sk "Malanthe craves a man, a warrior... and quite honestly, so do my maidens."
    sk "There is only so much pleasure and desire they can provide to each other. They have been longing for a man."
    scene ch6sc02_1054 with dissolve
    sk "And going by their chatter... they'll certainly be happy to see you."
    mc "*Chuckles* I’m honored."
    mc "Nice butterfly, by the way."
    sk "Oh? You noticed it? Thank you..."
    sk "Continue to impress me, and I might let you see it up close."
    scene ch6sc02_1055 with dissolve
    sk "We’re here... I hope you enjoy your reward."

    if tat_path == True:
        sk "But based on what Tatiana has told me about your time with her..."
        sk "I think you will most definitely enjoy tonight's menu..."
        sk "It's quite exciting having a man in our midst after all this time, I've prepared a special delight for you."

    else:
        pass


    sk "But remember, if you do not wish it, there is no shame in rejecting them. Malanthe will not accept impure offerings."
    scene ch6sc02_1056 with dissolve
    mc "Impure?"
    scene ch6sc02_1055 with dissolve
    sk "Yes. For an offering to be pure..."
    sk "It needs to be consensual, and everyone involved must achieve pleasure and have their desires fulfilled."
    sk "So, if you aren’t interested in the maidens, then it would be pointless to continue and better to reject them."
    scene ch6sc02_1057 with dissolve
    sk "But I'm sure they will appeal to a man such as you. Go on... they're awaiting you inside."
    sk "I’ll leave you to it... {b}enjoy the night, Hero{/b}."
    scene ch6sc02_1056 with dissolve
    mc "Thank you, Mistress."
    scene ch6sc02_1058 with dissolve
    mc "Let’s see what they have in store for me."
    mc "It doesn't hurt to look. As she said, I can just reject them if I'm not feeling it."
    scene ch6sc02_1059 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "Hey ladies..."
    mct "{i}Sakari really wasn't kidding... they're gorgeous.{/i}"
    scene ch6sc02_1060 with dissolve
    mm1 "Greetings... handsome outsider."
    scene ch6sc02_1061 with dissolve
    mm2 "Welcome, Champion... are you here to join us in our desires?"
    scene ch6sc02_1060 with dissolve
    mm1 "When we first heard about you, we were curious about the strange man in our midst..."
    mm1 "But since we heard you conquered the Trial of A'khans... well, we’ve been hoping you’d visit us."
    scene ch6sc02_1059 with dissolve
    mct "{i}First hero, now champion? I could get used to this...{/i}"

    ####Choice####
    menu:
        "Join the Maidens in a night of pleasure.":
            scene ch6sc02_1059 with dissolve
            mc "I won’t lie to you, I wasn’t sure what to expect when your Mistress said she had something special waiting."
            mc "But I’m pleasantly surprised at the sight of you two."
            scene ch6sc02_1060 with dissolve
            mm1 "Oh? Are you calling us beautiful, Hero?"
            scene ch6sc02_1061 with dissolve
            mm2 "I believe he is. He seems to find us just as attractive as we find him... Mmm."
            mm2 "Our desire has been growing for you rapidly... we hope yours will grow just as quickly."
            scene ch6sc02_1060 with dissolve
            mm1 "Neither of us has been with a man."
            mm1 "Nobody in A’nai has, except the Elders..."
            if tat_path == True:
                mm1 "We've heard great thigs about you... from Tatiana..."
                mm1 "You're all she's been talking about ever since you... filled her."
                scene ch6sc02_1061 with dissolve
                mm2 "It's true... hearing her talk about how she's never felt pleasure that matches your cock..."
                mm2 "We want to experience that... we want... you."

            else:
                pass

            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc02_1062 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            mm1 "Ohh... Fuu-... Mmm!"
            mm2 "Allow us to warm up before... you take us."
            mm1 "Ahhhgh... w-warn me next time! I almost climaxed from that surprise squeeze!"
            scene ch6sc02_1063 with dissolve
            mm2 "You'll have to forgive her, Champion. She has been on the edge all day, hoping you’d come to claim her."
            mc "She'll be forgiven once she has satisfied me, and not a moment before..."
            scene ch6sc02_1064 with dissolve
            mm2 "Did you hear that? You’ll have to earn his forgiveness tonight."
            mm1 "Mmh!! Yes... I’ll do whatever it takes!"
            mm2 "Let us show him how tender we can be with each other."
            scene ch6sc02_1065 with dissolve
            mm1 "Oohh..."
            mm1 "Your touch is so delicate, but its intent is as clear as the night sky! Mmm..."
            scene ch6sc02_1066 with dissolve
            mm2 "Does her body entice you, Hero? Does it stir your spear to awaken?"
            scene ch6sc02_1065 with dissolve
            mc "Yeah... your hands know their way around her petite body."
            scene ch6sc02_1066 with dissolve
            mm2 "They certainly do... you may undress. We’d love to see your spear while you watch us."
            mm1 "Aaah... yes, please let us see you."
            scene ch6sc02_1067 with dissolve
            mm1 "Champion... please stroke yourself while you look upon us- Mmm..."
            scene ch6sc02_1068 with dissolve
            mm2 "How handsome he is. He surely must be the one who was promised."
            scene ch6sc02_1069 with dissolve
            mm1 "L-Look how big he is ... we’ve only ever had our fingers inside... how will it fit?"
            scene ch6sc02_1068 with dissolve
            mm2 "It's a wonder indeed. But his spear belongs inside us... sending offerings to Malanthe through our pleasure."
            mm2 "C’mon, let’s show him how full of desire you are."
            scene ch6sc02_1069 with dissolve
            mm1 "Looking at his spear... my body understands it belongs inside me- Mmm..."
            scene ch6sc02_1070 with dissolve
            mm1 "*Moans* G-Gentle... I’m so-... Mmm... sensitive right now."
            scene ch6sc02_1071 with dissolve
            mm2 "The anticipation of his spear is keeping your body on the edge..."
            scene ch6sc02_1070 with dissolve
            mm2 "My fingers aren’t even inside you, but I feel the warmth and wetness coming from your flower."
            scene ch6sc02_1071 with dissolve
            mm2 "Tonight we’ll both be claimed by him, our flowers will bloom with his powerful spear inside them."
            scene ch6sc02_1070 with dissolve
            mm1 "Ooh... Ohh... MMm!"
            scene ch6sc02_1072 with dissolve
            mm1 "Champion... are you enjoying the view? Do our curves build your desire?"
            scene ch6sc02_1073 with dissolve
            mc "My desire is about to reach its peak..."
            mc "You ladies are really devoted to pleasure."
            scene ch6sc02_1074 with dissolve
            mm1 "Our purpose in life is to appease Malanthe. To release the tensions building in our bodies in honor of her."
            scene ch6sc02_1075 with dissolve
            mm2 "Maidens of Malanthe are supposed to be fully devoted to sharing their pleasures with their A’khan."
            mm2 "I'm sure you've heard by now how that tradition was broken to appease relations with outsiders."
            scene ch6sc02_1074 with dissolve
            mm1 "The maidens of the previous generation were given away by the A'khan to please the outsiders ..."
            mm1 "It was a controversial choice, not one that any maiden would have embraced on her own."
            scene ch6sc02_1075 with dissolve
            mm2 "Luckily we were only babes and children at the time. No maiden alive today has been corrupted."
            mm2 "So we haven't experienced any man. Not since the desecration of our temple and the death of our last A’khan."
            scene ch6sc02_1074 with dissolve
            mm1 "We’ve had to settle for each other, making impure and pitiful offerings to Malanthe. And she isn’t happy with us."
            scene ch6sc02_1073 with dissolve
            mc "Your Mistress mentioned something about that..."
            scene ch6sc02_1075 with dissolve
            mm2 "You’re on the path... completing the first trial has proven this."
            mm2 "So for tonight, we’ll be devoted to you, Champion. Just as Malanthe willed it in the old days."
            scene ch6sc02_1074 with dissolve
            mm1 "But you’ll have to continue to prove yourself if you wish to gain our devotion permanently."
            scene ch6sc02_1075 with dissolve
            mm2 "Yes, you’ll have to tread the path of A’khan... and conquer it."
            scene ch6sc02_1076 with dissolve
            mm2 "Once you do..."
            scene ch6sc02_1077 with dissolve
            mm2 "This..."
            mm1 "Aaahh..."
            scene ch6sc02_1076 with dissolve
            $ renpy.pause(1)
            scene ch6sc02_1077 with dissolve
            $ renpy.pause(1)
            scene ch6sc02_1076 with dissolve
            $ renpy.pause(1)
            scene ch6sc02_1077 with dissolve
            $ renpy.pause(1)
            scene ch6sc02_1076 with dissolve
            mm2 "The flower of every Maiden here will belong to you and only you."
            scene ch6sc02_1077 with dissolve
            mc "Damn... you make a compelling case."
            scene ch6sc02_1076 with dissolve
            mc "The two of you are already driving up my desire already..."
            mc "I can’t imagine having all the Maidens devoted to me."
            scene ch6sc02_1077 with dissolve
            mm2 "Tonight, you’ll get a taste of what your future holds... should you become our A'khan."
            mm2 "Come, she is ready for you."
            scene ch6sc02_1078 with dissolve
            mm2 "Her flower is dripping at the sight of you."
            scene ch6sc02_1078
            $ renpy.pause()
            mct "{i}Mmmh... she's juicy.{/i}"
            mc "Brace yourselves, I won’t hold back simply because you're virgins."
            "You move in and effortlessly pick up the young maiden from the altar."
            scene ch6sc02_1079 with dissolve
            mm1 "*Gasps* Aaahh... h-his touch is so manly. Mmm... his hands are rough and filled with desire."
            mm1 "Mmmh! S-Sorry but... I already prefer his touch to yours... Aah..."
            scene ch6sc02_1080 with dissolve
            mm2 "There’s nothing to be sorry for. This is how it’s meant to be."
            mm2 "A woman’s body in a man’s hands. Tell me, Champion... how does her young virgin body feel?"
            scene ch6sc02_1081 with dissolve
            mc "She feels firm... tight... Mmm... soft and perky... and... she’s filled with desire."
            mc "Her body is quivering at the slightest touch."
            mm1 "Ohh... g-gentle, Hero... Mmm..."
            scene ch6sc02_1080 with dissolve
            mm2 "Champion... I want to watch you thrust your spear inside her as I touch myself... Mmmh."
            mm2 "Deflower her before my eyes."
            scene ch6sc02_1082 with dissolve
            mm1 "*Moans* Ahhh! I feel him!! I-I feel his tip against my flower! Mmm!"
            with vpunch
            mc "*Whispers* You’re about to feel a whole lot more."
            scene mm_lewd5 with dissolve
            $ renpy.pause()
            mm1 "*Moans* Aiiihh-Ayyhh! O-Owh-mmm!"
            mm2 "That’s it! By the jungle... you’re really spearing her! Mmmm..."
            mc "Fuu... you’re a tight little thing... Mmm..."
            mm1 "Y-You’re too biiiighh for me! AhhH! T-Take me! Champion! Take me!"
            with vpunch
            mm1 "I-I can’t believe this feeling! Ahhh!! It’s incredible!! Malanthe is truly blessing us! Mmm!"
            scene ch6sc02_1080 with dissolve
            mm2 "MMmh... I’m getting jealous over here... the sound of her moans."
            mc "Don’t you worry, I’m not stopping until both of you have been thoroughly blessed."
            mm1 "Ahh-Ahh! C-Champion... you’re too much for me- MMhh!! I-I need to lie down for a moment..."
            with vpunch
            scene ch6sc02_1083 with dissolve
            mm2 "You should lie down too, Hero... I'll take care of you and make you relax."
            mc "Sounds lovely."
            mm1 "Mmmh... he was soooo goood... *Giggles* His spear is unbelievable..."
            scene ch6sc02_1084 with dissolve
            "As you get on the altar to join them, the maiden eagerly mounts you."
            mm2 "Here you go, get a good whiff of them... Mmm..."
            scene mm_lewd6 with dissolve
            $ renpy.pause()
            mc "*Inhales* Mmm... you’ve got a strong scent..."
            mm2 "While you were fucking her, I rubbed the nectar of my flower onto my breasts... Mmm..."
            mm2 "I hoped it would stir something within you... Aahh... it seems I was right."
            mc "What a naughty maiden... *Lick* mmm... you really do know how to increase my desire."
            mm2 "Ohh... Mmm... Y-Yes! Keep tasting my breasts..."
            mm2 "I’ve been aching to feel your mouth on them since you stepped in here... let me just..."
            scene mm_lewd7 with dissolve
            $ renpy.pause()
            "As your full attention is on her large and delicious breasts, her grinding back and forth against you results in her flower inviting you in."
            with vpunch
            mm2 "Ahh! Oh Malanthe!! *Moans* Aiiiih!"
            mm1 "*Giggles* He feels amazing, doesn’t he?"
            mm2 "MMMM... I-I’ve never experienced anything even close to this! AHhh ..."
            mc "Mmmh ... f-fuck you’re tight ... your flower is perfectly warm and wet for me ..."
            mm2 "*Moans* How could it not be? We’re meant to be together ... Champion - Mmm ..."
            scene mm_lewd8 with dissolve
            $ renpy.pause()
            mm2 "Ahhh! You’re so deep! Mmm ... I’m going to ride you until you give me what I want!"
            mm1 "Don’t you mean until he gives Malanthe what she wants?"
            with vpunch
            mm2 "*Moans* Yes! Yes ... Ss-sure! Mmm!! {b}AHH!!{/b} Hero! Fill my flower!!"
            mm1 "By the jungle, your spear has already corrupted her!"
            mm1 "*Giggles* She’s more devoted to pleasuring you and herself than offering Malanthe the pleasure."
            mc "Ahhh ... our desires melt together with every movement ... Mmm! I’m going to -"
            with vpunch
            mm2 "I feel you! Your spear is throbbing - AHhh! Give it to me, {b}CHAMPION!! AHH!!{/b}"
            with vpunch
            scene ch6sc02_1085
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            mm2 "Aiiihh! Aiiihh!! {b}YESS!!{/b}"
            scene ch6sc02_1086
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            mm2 "He’s filling me up! *Moans loudly* Ahh!! {b}OH FUUU!! MMM!!{/b}"
            mc "*Panting* Fuck ... you really know how to drain a man ..."
            mm2 "Mmmm ... it is a simple thing, all I had to do was follow my own desire - Mmm ..."
            scene ch6sc02_1087 with dissolve
            mm1 "Hero, please ... will you fill me up as well?"
            mm1 "My flower desires to bloom like hers, with your spear deep inside it."
            mc "If you’re ready for another round, then stand in front of the altar."
            "The maiden eagerly does as you ask, presenting herself to you."
            scene ch6sc02_1088 with dissolve
            $ renpy.pause()
            mm1 "Is this how you want me, my champion?"
            mm1 "I-I feel so exposed without you inside me ..."
            scene ch6sc02_1089 with dissolve
            mc "Then I won’t keep you waiting. Brace yourself, this time I won’t be stopping until I fill that tight little pussy of yours."
            mm1 "Mmh! He’s speaking so lewdly! I’m dripping already - Mmm ..."
            scene ch6sc02_1090 with dissolve
            mm2 "He is speaking to you exactly as a man should talk to his woman. MMm ... Champion, bring her to divinity."
            mm2 "I wish to watch as you fill her flower while my nectar is still covering your spear."
            scene mm_lewd9 with dissolve
            $ renpy.pause()
            mm1 "Ahhh! Y-Yes! Take me, Hero! Make me yours! {b}MMM!!{/b}"
            mm2 "How does his spear feel now? Can you handle the pleasure?"
            mm1 "Ahh-Ah! I-I can! Mmm! It’s so warm and hard - Nnghh!"
            scene mm_lewd10 with dissolve
            $ renpy.pause()
            with vpunch
            mm1 "Ahhh! His spear is truly blessed by Malanthe! Mm-MM!! Yes!"
            with vpunch
            mm1 "You’re bringing me closer to the goddess with every thrust Champion! Aiiih!"
            mm2 "Fuck her harder, Champion. Make her feel truly connected to the goddess."
            scene mm_lewd11 with dissolve
            $ renpy.pause()
            mm1 "Aiiyhh! Ahhh! T-This is too much! I-I can’t take it!! {b}MMM!!{/b}"
            with vpunch
            mm2 "Don’t stop, Hero. Her offering will be the purest we’ve ever presented to Malanthe!"
            mm2 "Keep penetrating her and make her cum all over your spear!"
            with vpunch
            mm1 "{b}AHH!! *Moans loudly* AIIIYHH!! YES!! I’M- I’M CUMMING!!{/b}"
            scene mm_lewd12 with dissolve
            $ renpy.pause()
            mm2 "That’s it, Champion! Fuck her through her orgasm and send her to Malanthe!"
            with vpunch
            mm1 "{b}AHHH!!! I CAN’T!!! MMM! YES!! FUCK ME! HIS SPEAR IS DIVINE!!{/b}"
            with vpunch
            mm1 "He's so deep! I feel him pounding against my ass! {b}MMHH!{/b}"
            mc "Fuu... your flower is so wet and tight, mmm! I can’t hold it much longer..."
            mm1 "Don’t! Don’t you dare hold it! Fill my flower with your seed! {b}AHHH!{/b} I want it!!"
            "Hearing her plead for your cum, the sensation of her pussy sucking your cock sends you to the highest heavens."
            scene ch6sc02_1091 with dissolve
            $ renpy.pause(0.5)
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            mc "*Moans* AHhh! MMmm..."
            mm1 "*Panting* By the goddess, I can’t believe how much he gave me... Mmm!"
            mm1 "My flower is overflowing with-... with his seed, mmm... it's running down my legs."
            mm1 "Thank you, Champion... Mmm... you’ve blessed me."
            mc "Trust me... I feel just as blessed by the two of you."
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc02_1092 with dissolve
            play music explore_2 fadein 1.0
            #stop music fadeout 1.0
            mm2 "Then it’s clear... you must return to us again."
            mm2 "We will accept nothing less... Mmm."
            scene ch6sc02_1093 with dissolve
            mm1 "Yes! You must..."
            mm1 "You’ve fulfilled our desires beyond words... we... we crave you now."
            mm1 "Our bodies now know what it feels like to be with you. Our desire will only grow from here..."
            scene ch6sc02_1092 with dissolve
            mm2 "She is right, Champion... I hope you will live up to our expectations. That you truly are the savior of our people."
            mm2 "Now that you’ve claimed us, we will crave you and your spear for the rest of our lives..."
            mm2 "You must become the A'khan so that you can rightfully claim us as yours."
            scene ch6sc02_1094 with dissolve
            mc "*Chuckles* It’s a good thing I work best under pressure."
            mc "But with motivation like you two beautiful and exotic ladies..."
            mc "I may just have to become the next A’khan."
            scene ch6sc02_1095 with dissolve
            mm2 "Did you hear that? He will ascend to become the next A’khan so that his claim on us will be permanent."
            mm1 "My desire swells at the thought. I will pray to Malanthe that he will succeed."
            mc "Thank you, ladies. With your prayers I’m sure I’ll finish the remaining trials without breaking a sweat."
            scene ch6sc02_1096 with dissolve
            mm2 "How bold... Mmm."
            mm2 "I like a man with confidence if he is able to back it up..."
            scene ch6sc02_1097 with dissolve
            mc "Goodnight, Maidens ... and thank you for giving me a night I won’t soon forget."
            scene ch6sc02_1096 with dissolve
            mm2 "Goodnight, Champion. Thank you for blessing us with your heroic spear."
            scene ch6sc02_1098 with dissolve
            "As you’re about to exit the Chamber of Malanthe, you feel something against your back... a soft touch."
            mm2 "*Quietly* Wait..."
            scene ch6sc02_1099 with dissolve
            mm2 "In here... we are nameless, but... I desire to know your name."
            scene ch6sc02_1100 with dissolve
            mc "[mc]... and you?"
            mm2 "..."
            scene ch6sc02_1099 with dissolve
            mz "*Quietly* Maze, my birth name is Maze..."
            scene ch6sc02_1100 with dissolve
            mc "Maze? That’s a unique name."
            scene ch6sc02_1101 with dissolve
            mc "But I like it, it suits you. You're a unique woman."
            mz "*Giggles softly* ..."
            "Maze likes that you complimented her name, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ mz_trust += 3
            scene ch6sc02_1099 with dissolve
            mz "T-Thank you for saying that. [mc], I like your name too."

            ####Choice####
            menu:
                "Suggest that next time it's only the two of you. ({color=#ff8cdd}Maze Path{/color})":
                    scene ch6sc02_1100 with dissolve
                    mc "Next time, let's just make it the two of us?"
                    scene ch6sc02_1101 with dissolve
                    mz "..."
                    scene ch6sc02_1099 with dissolve
                    mz "Just... you and me?"
                    mc "Yes, just the two of us."
                    scene ch6sc02_1101 with dissolve
                    mc "I'm not going to lie, this was amazing, but you're a woman who deserves my full attention."
                    mz "..."
                    scene ch6sc02_1099 with dissolve
                    mz "[mc], I... I would love that."
                    mz "Let's make it so."
                    $ mz_path = True
                    scene ch6sc02_1101 with dissolve
                    mc "I'm pleased you feel the same, I'll look forward to seeing you again."
                    $ mz_trust += 3
                    "Maze is pleasantly surprised that you've singled her out, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

                "Don't suggest anything and just enjoy the maidens as they are. (Neutral Path)":
                    scene ch6sc02_1099 with dissolve
                    mc "Thanks."

            scene ch6sc02_1102 with dissolve
            mz "Sweet dreams, [mc]... Mmm. *Mwah*"
            mc "You too, Maze. Sweet dreams."
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)

        "Decline the Maidens and go to bed.":
            scene ch6sc02_1059 with dissolve
            mc "I’m sorry ladies, it’s been a long day and what I truly desire right now is some rest."
            scene ch6sc02_1060 with dissolve
            mm1 "Awwhh... here we were hoping you’d turn us into your playthings."
            scene ch6sc02_1061 with dissolve
            mm2 "We understand, Champion... may you rest well. I hope you’ll decide to visit us another time."
            mm2 "Your feats have ignited our desire for you. I do not doubt that it will keep increasing..."
            scene ch6sc02_1059 with dissolve
            mc "I like the sound of that. Goodnight, and enjoy the night."
            scene ch6sc02_1060 with dissolve
            bth "*Giggles* We will! Night, night!"
            scene black with Dissolve(1.5)
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(1)


    scene ch6sc02_883 with Dissolve(1.5)
    $ renpy.pause(1)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}There's only a couple of hours left until dawn... time to get some rest.{/i}"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_813 with Dissolve(1.5)
    mct "{i}Completing the trials... becoming the A’khan... Is that really something I want to deal with?{/i}"
    mct "{i}I admit I'm curious about everything here: the magic suppression, the two tribes, their past with outsiders...{/i}"
    mct "{i}The ancient ruins and deep history here... their connection to several gods and goddesses."
    mct "{i}This is what being an adventurer is all about.{/i}"
    mct "{i}I can see why Dalen was gone from the capital for so many years. It’s easy to get caught up in everything out here.{/i}"
    mct "{i}I suppose completing the trials could lead to more artifacts or other interesting discoveries.{/i}"
    mct "{i}And if the ambassador is being held by the other tribe, Echo might have to get involved to open negotiations.{/i}"
    mct "{i}All of which could take time, depending on how friendly they are with each other. So, I might as well do the trials while I'm waiting.{/i}"
    mct "{i}*Exhales* For now, I’ll see how things go.{/i}"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1103 with Dissolve(1.5)
    $ renpy.pause(1)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    pl "[mc]?"
    pl "Pssst, you up?"
    scene ch6sc02_1104 with dissolve
    pl "Helloooo? ... wakey! wakey!"
    mc "Hnngh..."
    scene ch6sc02_1105 with dissolve
    mc "Pearl?"
    mc "Why are you poking me? Quit it..."
    scene ch6sc02_1106 with dissolve
    pl "Then rise and conquer the day! *Snickers*"
    scene ch6sc02_1105 with dissolve
    mc "Why are you up already? Did I sleep in or something?"
    scene ch6sc02_1106 with dissolve
    pl "You sure did!"
    scene ch6sc02_1107 with dissolve
    pl "You were snoring. So, out of the kindness of my heart, I decided to let you sleep a bit longer."
    mc "*Chuckles* Your kindness is much appreciated..."
    scene ch6sc02_1109 with dissolve
    mc "So, what have you been up to?"
    scene ch6sc02_1108 with dissolve
    pl "I was out exploring the village! This nice girl, Miyo, took it upon herself to show me around."
    scene ch6sc02_1109 with dissolve
    mc "Miyo? I don’t think I’ve met her yet."
    scene ch6sc02_1110 with dissolve
    pl "Yeah, she’s really kind and welcoming! We’re besties."
    mc "*Chuckles* Besties?"
    pl "Uh-huh, uh-huh!"
    scene ch6sc02_1108 with dissolve
    pl "At least, while we’re here! If we’re staying here a while, we might as well make friends, right?"
    scene ch6sc02_1109 with dissolve
    mc "*Sighs* You sound like Eliza..."
    scene ch6sc02_1111 with dissolve
    pl "Knowing how highly you think of her, that is definitely a compliment."
    mc "Yeah, it was."
    scene ch6sc02_1108 with dissolve
    pl "You wanna meet Miyo? I can introduce you."
    scene ch6sc02_1109 with dissolve
    mc "Sure, but could I get a minute to wake up before we go befriending the tribe?"
    scene ch6sc02_1112 with dissolve
    pl "No! Come on, you’ll be wide awake as soon as you start moving!"
    mc "*Exhales* Alright, alright..."
    mc "After you."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1113 with Dissolve(1.5)
    $ renpy.pause(1)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    "The two of you wander around A'nai while Pearl looks for Miyo."
    pl "There they are!"
    pl "Miyo is the one with black hair and the red dress. The other one is-"
    mc "Vex. I’ve already had the pleasure."
    pl "Right! I forgot you were charming the villagers before I even got here!"
    scene ch6sc02_1114 with dissolve
    mc "Charming them? Then how did I end up thrown down some ancient ruins?"
    pl "*Giggles* Jealousy! Duuh!"
    pl "It’s bound to happen when there’s a lot of female attention on a single male."
    mc "Right..."
    scene ch6sc02_1115 with dissolve
    mi "Pearl! Hi. I see you managed to wake up your friend?"
    pl "You bet! Nobody can withstand an assault of my pokeys!"
    scene ch6sc02_1116 with dissolve
    mc "Hey..."
    mc "It’s nice to meet you. Miyo, is it?"
    scene ch6sc02_1117 with dissolve
    mi "Hi, I see you’re already familiar with my birth name."
    mi "It’s a pleasure to meet you too, [mc]."
    scene ch6sc02_1116 with dissolve
    mc "*Chuckles* Seems you’re familiar with mine as well."
    scene ch6sc02_1118 with dissolve
    pl "Heh-heeeh..."
    mc "I think we know who has been gossiping..."
    scene ch6sc02_1119 with dissolve
    mi "I hear Pearl and you are companions?"
    mc "It’s true, we’re good friends."
    scene ch6sc02_1120 with dissolve
    mi "Marvelous! Pearl is very kind."
    mi "So, if she likes you, then I too will give you a chance!"
    scene ch6sc02_1121 with dissolve
    mc "I appreciate it. It’s nice not to be judged just because of what’s between my legs."
    mi "..."
    scene ch6sc02_1122 with dissolve
    vx "......"
    scene ch6sc02_1123 with dissolve
    pl "........."
    scene ch6sc02_1124 with dissolve
    mc "Girls?"
    evr "..."
    scene ch6sc02_1125 with dissolve
    evr "Hmmh?"
    mc "You're ridiculous..."
    scene ch6sc02_1126 with dissolve
    mi "R-Right! This is Vex!"
    mc "I’ve already had the pleasure of meeting her."
    scene ch6sc02_1127 with dissolve
    mc "Good morning, Vex. It’s good to see you."
    mc "I enjoyed our walk."
    scene ch6sc02_1128 with dissolve
    vx "Y-Yeah, me too..."
    vx "It’s good to see you as well... g-good morning."
    scene ch6sc02_1129 with dissolve
    mi "*Gasps* Wait, are you blushing?!"
    mi "Do you have a crush on the handsome and heroic outsider, Vex?"
    scene ch6sc02_1130
    with vpunch
    vx "I’m not blushing!"
    vx "Take it back! I’m not crushing on anyone! Especially some handsome and mysterious outsider!"
    with vpunch
    mi "*Laughing* Hahhah! Sorry, Vex, but your cute, rosy cheeks say otherwise!"
    vx "You be quiet! Or... or I'll challenge you to a duel! Hnngh!"
    scene ch6sc02_1131 with dissolve
    pl "Oh, yeah. Echo was looking for you earlier. I’m not sure where she went, though."
    mc "Oh? Maybe I should go see what she wanted."
    scene ch6sc02_1132 with dissolve
    ec "You need not search for me. I am here."
    mc "Ah, good morning Echo."
    scene ch6sc02_1133 with dissolve
    ec "I’m glad to see you’re here already."
    scene ch6sc02_1134 with dissolve
    mc "Hmh?"
    scene ch6sc02_1133 with dissolve
    ec "We’ve much to discuss."
    scene ch6sc02_1134 with dissolve
    mc "I’m listening."
    scene ch6sc02_1135 with dissolve
    ec "I believe I have an idea about how to find this ambassador of yours."
    ec "As well as share more of our culture with you. If such a thing interests you?"
    scene ch6sc02_1136 with dissolve
    mc "You already had my interest at ambassador, but throwing in some of your culture too?"
    mc "You know how to pique a man’s interest. What did you have in mind?"
    scene ch6sc02_1137 with dissolve
    ks "Greetings, A'nu."
    scene ch6sc02_1138 with dissolve
    ec "Greetings, Kisha."
    ec "It’s good to see you."
    scene ch6sc02_1139 with dissolve
    ks "Greetings, everyone."
    ks "Outsiders..."
    scene ch6sc02_1140 with dissolve
    pl "Good morning! *Giggles*"
    pl "I hope us being here isn't a bother to you?"
    scene ch6sc02_1139 with dissolve
    ks "I shall adjust to it."
    scene ch6sc02_1140 with dissolve
    pl "We're not here to step on anyone's toes. So, please tell us if we act out of order."
    scene ch6sc02_1141 with dissolve
    ks "A’nu, forgive me for interrupting..."
    ks "But I require Vex."
    scene ch6sc02_1142 with dissolve
    ks "Vex, it is time... we must begin your training."
    ks "I hope your focus is unwavering today."
    scene ch6sc02_1143 with dissolve
    vx "Really? But..."
    vx "We usually only train once the sun has passed midday?"
    scene ch6sc02_1144 with dissolve
    ks "Yes, but I have much to teach you."
    ks "As you know, your graduation hunt is coming up and we have much to prepare."
    scene ch6sc02_1143 with dissolve
    vx "My graduation hunt? I didn’t think I would have one for at least another two moons?"
    scene ch6sc02_1144 with dissolve
    ks "You have been improving rapidly. However... whether I deem you ready or not..."
    ks "Will depend on today's performance during training. I won’t go easy on you."
    ks "Prepare yourself to be drenched in sweat and covered in dirt. You will not be comfortable today."
    scene ch6sc02_1145 with dissolve
    vx "Y-Yes, Head-Huntress!"
    vx "I won’t disappoint!"
    scene ch6sc02_1146 with dissolve
    ks "Good, we’ll take our leave then."
    ks "May Gaia bless you all today."
    scene ch6sc02_1147 with dissolve
    ec "And you, Kisha."
    ec "May the goddesses look upon your training with satisfaction."
    ks "Thank you. Your words fills us with encouragement, A’nu."
    scene ch6sc02_1148 with dissolve
    ec "Vex, as Kisha said, you are doing well... one of the best young aspiring huntresses I’ve seen."
    ec "You will do well, of that I am certain."
    scene ch6sc02_1149 with dissolve
    vx "A-A’nu! Thank you... I'll give it all I have!"
    vx "I will make the tribe proud."
    ks "Vex!"
    scene ch6sc02_1150 with dissolve
    ec "Okay, back on topic and our preparations..."
    ec "You and Pearl will join Miyo on a small excursion into the jungle to forage for food."
    scene ch6sc02_1151 with dissolve
    ec "Miyo here is one of our best herbalists, despite her youth."
    ec "I dare say she knows every little plant the jungle has to offer."
    scene ch6sc02_1152 with dissolve
    mi "A’nu, your words honor me."
    mi "But to claim that I know every plant is bold!"
    scene ch6sc02_1151 with dissolve
    ec "I wouldn’t praise you if you hadn’t earned it."
    ec "The tribe is lucky to have a promising young herbalist such as you."
    scene ch6sc02_1153 with dissolve
    ec "I will have Suji and Zyra accompany you on this excursion."
    ec "They will serve as your guides and protectors."
    ec "It will also be an opportunity for you to look for clues about this ambassador while you’re out there."
    scene ch6sc02_1154 with dissolve
    mc "Gathering food and getting to know the area better sounds good."
    mc "Besides, who knows what we might stumble upon...?"
    scene ch6sc02_1153 with dissolve
    ec "Exactly."
    ec "I doubt you will encounter any of the Arugoh tribe on this trip, as their territory is further north."
    scene ch6sc02_1155 with dissolve
    ec "Suji and Zyra know already, of course."
    ec "But you should also be aware. Our two tribes tolerate each other but-"
    scene ch6sc02_1153 with dissolve
    ec "We are not on friendly terms either."
    ec "We usually avoid contact or trespassing on each other’s territories."
    scene ch6sc02_1154 with dissolve
    mc "Makes sense."
    scene ch6sc02_1155 with dissolve
    ec "Come, let’s all make our preparations."
    ec "You’ll set out in a couple of hours."
    scene ch6sc02_1156 with dissolve
    ec "Miyo, teach Pearl a little about our edibles and non-edibles."
    scene ch6sc02_1152 with dissolve
    mi "Yes, A'nu!"
    mi "I'll show her the basic edibles we most often encounter."
    scene ch6sc02_1153 with dissolve
    ec "[mc], you’re with me."
    ec "We’ll stop by the huntresses' camp on the way to the temple to inform Suji and Zyra."
    scene black with Dissolve(1.5)
    "Everyone did as instructed and began preparing for the excursion."
    scene ch6sc02_1157 with Dissolve(1.5)
    "Miyo showed Pearl a selection of various edibles fruits and berries to look for."
    scene ch6sc02_1158 with dissolve
    pl "..."
    pl "......"
    scene ch6sc02_1157 with dissolve
    $ renpy.pause()
    scene ch6sc02_1159 with dissolve
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_1160 with Dissolve(1.5)
    $ renpy.pause(1)
    "Meanwhile Suji and Zyra prepared for venturing into the jungle."
    "Seeking good fortune from their goddess, Gaia."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch6sc02_1161 with Dissolve(1.5)
    $ renpy.pause(1)
    "Meanwhile, you and Echo discussed some of the nearby areas of interest."
    "She emphasized the importance of going out in groups because the jungle is ever-changing."
    scene ch6sc02_1162 with dissolve
    "Heavy mists roll in at random times that alter the vegetation and the paths themselves..."
    "Making it near impossible for even the best huntresses to navigate."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch4sc15_066 with Dissolve(1.5)
    $ renpy.pause(1)
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_008 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    br "Did ye see that recent quest that was put up on t' noticeboard at t' guild?"
    scene ch6sc02_009 with dissolve
    el "Yeah. I was thinking about taking it, actually. Putting down some bandits sounds like a good workout."
    scene ch6sc02_010 with dissolve
    br "Wha! I’ll help!"
    scene ch6sc02_011 with dissolve
    el "Hmmmh? Are you offering to help because you’re worried about me, or..."
    el "Because you need the coin for gambling?"
    scene ch6sc02_012 with dissolve
    br "Ye know about me fondness o'cards, eh?"
    el "*Nods* Mmh-hmm..."
    br "*Sighs* Alright... ye got me. I may owe a teeny tiny sum t' some locals..."
    scene ch6sc02_014 with dissolve
    el "Borri... *Sighs* Fine, we can team up for this quest and share the bounty."
    br "Thank ye, lass! I shan’t soon forget this!"
    scene ch6sc02_015 with dissolve
    el "*Giggles* You can thank me by paying for the first round of ales tonight."
    br "*Chuckles* Hah! I’ve said it before, and I’ll say it again, ye truly have t' spirit of a fine dwarven woman!"
    bth "*Laughing* Heheheheh-Hahah!"
    uk "Beware! The soulless bloodsuckers of the night are here!"
    scene ch6sc02_1163 with dissolve
    uk "We of the {b}First Dawn{/b} are in need of your aid! We seek able warriors to take up arms against the bloodsuckers!"
    uk "Vampires, people. Vampires! Their ranks have been increasing and they aren’t confined to Nerzir anymore!"
    uk "Nay, I tell you! They walk amongst us, right here in Luxeron! Right here in Luxenford, even!"
    uk "Join the {b}First Dawn{/b} and end their miserable existence before they sink their teeth into your loved ones!"
    scene ch6sc02_1164 with dissolve
    el "*Quietly* {size=-10}{b}First Dawn?{/b}{/size}"
    el "*Quietly* {size=-10}{b}Wasn't the guy [mc] shared a cell with from that faction? Or used to be, at least?{/b}{/size}"
    scene ch6sc02_1163 with dissolve
    br "Aye... they’re a faction based in Nerzir."
    br "They've dedicated themselves t' fight creatures of t' night."
    br "Such as undead, ghosts, darachs, werewolves-"
    scene ch6sc02_1164 with dissolve
    el "And vampires..."
    scene ch6sc02_1163 with dissolve
    br "Aye, them too."
    br "Best not get caught up in their war... They might not be religious, but they are borderline zealots."
    scene ch6sc02_014 with dissolve
    el "*Sighs* C’mon, let’s get out of here."
    scene ch6sc02_015 with dissolve
    br "Aye, we’ve got a bountiful quest awaiting us! Heh!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1165 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mc "Really? A fruit shaped like a dick?"
    scene ch6sc02_1166 with dissolve
    pl "Uh-huh! And it was big too!"
    pl "Like, real big."
    scene ch6sc02_1167 with dissolve
    mc "And you’re sure it wasn’t just a banana? Or squash or cucumber?"
    scene ch6sc02_1166 with dissolve
    pl "Yes! It was purple and- and... shapely!"
    scene ch6sc02_1167 with dissolve
    mc "Shapely?"
    scene ch6sc02_1166 with dissolve
    pl "Yes! Very... shapely!"
    scene ch6sc02_1168 with dissolve
    pl "I can see why Miyo is into being a herbalist... *Snickers*"
    mc "You’re not suggesting..."
    scene ch6sc02_1166 with dissolve
    pl "Am so! Think about it! A tribe with no men for over two decades?"
    pl "Speaking from experience... we women can get just as... horny as you menfolk!"
    scene ch6sc02_1167 with dissolve
    mc "*Chuckles* Oh, I know..."
    scene ch6sc02_1165 with dissolve
    mc "But you really think she'd... use that to..."
    mc "Pleasure herself?"
    scene ch6sc02_1166 with dissolve
    pl "I would! *Snickers*"
    scene ch6sc02_1169 with dissolve
    zy "Outsiders, there you are."
    zy "The others are waiting for us at the gate."
    scene ch6sc02_1170 with dissolve
    mc "I guess we'd better get to it."
    scene ch6sc02_1171 with dissolve
    zy "Yes, keeping the A’nu and others waiting will reflect poorly on you outsiders."
    zy "Come, follow me."
    scene ch6sc02_1172 with dissolve
    pl "Do you think we’ll find the ambassador when we’re out there?"
    pl "Could they even survive alone out there?"
    scene ch6sc02_1173 with dissolve
    mc "I doubt it, but I’m hoping we’ll find some clues or signs that they've been in the area."
    mc "Either way, it'll be good to get to know the area better."
    scene ch6sc02_1174 with dissolve
    pl "*Nods* Mhm... I’m relieved we’re going with a group."
    mc "You’re going to help Miyo with the foraging?"
    pl "Yeah, she showed me a whole bunch of edibles we can collect, and some to avoid."
    scene ch6sc02_1175 with dissolve
    pl "I wish Kira was here with us... she could learn this stuff too."
    mc "You miss her, don’t you?"
    pl "*Nods* Mhh."
    mc "Look on the bright side..."
    mc "When we see her again, you’ll have a whole bunch of adventurous stories to share with her."
    scene ch6sc02_1176 with dissolve
    pl "R-Right! I’m going to talk her ear off about everything! *Giggles*"
    mc "That’s the spirit. C’mon, we don’t want to keep them waiting."
    scene ch6sc02_1177 with dissolve
    zy "A’nu, sorry to keep you waiting..."
    zy "I brought the outsiders as you asked."
    scene ch6sc02_1178 with dissolve
    ec "Worry not, Huntress... we haven’t lingered long."
    mc "Sorry for the wait."
    scene ch6sc02_1179 with dissolve
    sj "You should be. Making the A’nu wait is an insult."
    sj "Normally you’d be strung upside down from a banana tree for two days..."
    sj "Naked. *Snickers*"
    scene ch6sc02_1180 with dissolve
    mc "I mean... if you're offering?"
    "Stunned by your reply the huntress is lost for words."
    scene ch6sc02_1178 with dissolve
    ec "*Sighs* Goddesses..."
    ec "Don’t listen to her, [mc]. She didn't mean it."
    scene ch6sc02_1179 with dissolve
    sj "A joke, to lighten the mood..."
    sj "Isn’t that so, Outsider?"
    scene ch6sc02_1180 with dissolve
    mc "Don’t worry, Echo. I’ve come to understand that Suji has a sharp tongue."
    sj "..."
    scene ch6sc02_1181 with dissolve
    zy "*Snickers* It is known."
    zy "A tongue like a spear."
    scene ch6sc02_1182 with dissolve
    sj "Hush!"
    sj "You'd better be quiet or you’ll feel a real spear."
    zy "*Scoffs* ..."
    scene ch6sc02_1178 with dissolve
    ec "I’m glad to see everyone is getting along."
    ec "Shall we begin?"
    scene ch6sc02_1183 with dissolve
    mc "Sure, go ahead, Echo. We’re ready whenever you are."
    scene ch6sc02_1184 with dissolve
    ec "You have two objectives for today's excursion."
    ec "The first is to gather a decent supply of food and medicinal herbs for the tribe."
    scene ch6sc02_1185 with dissolve
    ec "Miyo will show [mc] and Pearl which ones to gather. Together, they will harvest what we need."
    mi "It’ll be an honor to show them our ways, A’nu."
    ec "It brightens my spirit to see you eager to share your knowledge with them."
    scene ch6sc02_1184 with dissolve
    ec "Meanwhile, Suji and Zyra. You will keep watch."
    ec "Our second objective today is to find clues about their missing ambassador."
    ec "Any sign that they have been in the area. The two of you are our most experienced huntresses-"
    ec "But please, do not let yourselves be over-confident out there. You know very well the dangers of the jungle."
    scene ch6sc02_1186 with dissolve
    sj "A’nu! We will remain vigilant."
    zy "We will watch over the outsiders and ensure their safety."
    scene ch6sc02_1184 with dissolve
    ec "Thank you... this means a lot to me."
    scene ch6sc02_1187 with dissolve
    ec "[mc], what can you tell us about this ambassador? Anything that can help us find her?"
    scene ch6sc02_1188 with dissolve
    mc "I’m afraid I can’t be of much use. All I know is they are an ambassador, an envoy of Arazalia."
    mc "So she's probably more exotic looking compared to Pearl and me."
    scene ch6sc02_1189 with dissolve
    ec "Exotic? How do you mean?"
    scene ch6sc02_1188 with dissolve
    mc "More akin to your people: dark hair, sun-kissed skin and such."
    mc "We were tasked to find and bring the ambassador home safely to avoid political fallout and a potential war."
    mc "The one who set us this task has our friends captive... Pearl’s sister, even."
    scene ch6sc02_1189 with dissolve
    ec "Goddesses... I’m sorry."
    ec "It is a good thing you shared this with us... now everyone present will understand the importance."
    scene ch6sc02_1190 with dissolve
    sj "Hey... I’ll keep my eyes out for anything while we’re out there."
    sj "I promise, if my eyes scout anything, you will know it."
    scene ch6sc02_1191 with dissolve
    mc "Suji... thank you."
    sj "*Nods* Mmh."
    scene ch6sc02_1187 with dissolve
    ec "[mc], why did you not tell me this sooner?"
    ec "How important this... ambassador is to you?"
    scene ch6sc02_1188 with dissolve
    mc "Because, just as your tribe was wary about me, I too had to know I could trust you before I shared everything."
    mc "And being shoved down into those ancient ruins by your second in command didn’t exactly bolster my trust."
    scene ch6sc02_1189 with dissolve
    ec "I... I understand."
    scene ch6sc02_1188 with dissolve
    mc "Also, it’s my friends' lives that are on the line. It is my duty to protect them."
    scene ch6sc02_1189 with dissolve
    ec "Mhm, this I understand."
    scene ch6sc02_1192 with dissolve
    ec "Your role amongst your friends is that of a leader, a provider, a protector."
    ec "It may not officially be your title, but your actions speak for themselves. And so do Pearl's."
    ec "She reveres you... and I’m beginning to see why."
    scene ch6sc02_1193 with dissolve
    ec "Anyway... let’s get back on topic."
    ec "As you know, today you’ll be accompanied by Suji and Zyra."
    scene ch6sc02_1195 with dissolve
    mi "Oooh! Marvelous!"
    scene ch6sc02_1195 with dissolve
    mi "If you’re lucky, you might get to see them in action. They’re our best huntresses!"
    mi "The first time I saw them take down some prey, I was in awe!"
    scene ch6sc02_1193 with dissolve
    ec "Miyo’s excitement is full of pride, but for good reason. Hopefully you won’t need to see them in action, though."
    ec "Their primary purpose today is to keep lookout and protect you on your journey."
    scene ch6sc02_1192 with dissolve
    ec "They know the jungle very well. At least, as well as can be expected given it’s ever-changing nature."
    ec "Their eyes are those of sunhawks, their footsteps of shadowpanthers. They will likely notice things you do not."
    scene ch6sc02_1196 with dissolve
    mc "I see they are well respected and that you hold them in high regard."
    mc "I believe that wouldn’t be so, unless they earned it."
    scene ch6sc02_1197 with dissolve
    zy "The outsider is wise."
    sj "Mhm, he is. Don’t worry, we’ll protect the two of you and keep an eye out for signs of this ambassador."
    scene ch6sc02_1196 with dissolve
    mc "Thank you. I feel better knowing I have two capable huntresses with me."
    scene ch6sc02_1187 with dissolve
    ec "I think we’ve covered everything, then. Was there anything I’ve overlooked, [mc]?"
    mct "{i}She’s looking to me to give the final go? I must have gained quite a bit of her respect.{/i}"
    scene ch6sc02_1188 with dissolve
    mc "No. I believe you’ve covered everything, Echo."
    mc "I do however want to tell everyone something before we depart."
    ec "*Nods*"
    scene ch6sc02_1192 with dissolve
    ec "Go ahead, the reins are yours."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mc "Very well."
    scene ch6sc02_1198 with dissolve
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    mc "Listen, ladies..."

    if leadership >= 12:
        scene ch6sc02_1199 with dissolve
        mc "I know that Pearl and I are outsiders here, and that you are taking a risk by helping us."
        mc "You have nothing to gain by assisting us in this mission, but you still deem it worthy to do."
        scene ch6sc02_1198 with dissolve
        mc "One of the people who will be helped by finding this ambassador is Pearl’s sister, Kira."
        mc "We’re grateful for you opening your home to us and for your willingness to assist."
        mc "I’m grateful."
        $ leadership += 1
        "Everyone seems smitten by the way you talk... by the way you move... your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
        scene ch6sc02_1200 with dissolve
        mi "*Quietly* {size=-10}{b}Is he always this... sexy?{/b}{/size}"
        scene ch6sc02_1201 with dissolve
        pl "*Quietly* {size=-10}{b}Mhm-Hm... always.{/b}{/size}"
        scene ch6sc02_1200 with dissolve
        $ mi_trust += 6
        mi "*Quietly* {size=-10}{b}Interesting... mmh, cute, handsome, not afraid to lead... mmh.{/b}{/size}"
        "Miyo feels attracted to your assertiveness, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."

    else:
        scene ch6sc02_1199 with dissolve
        mc "I know that Pearl and I are outsiders here, and that you are taking a risk by helping us."
        mc "You have nothing to gain by assisting us in this mission, but you still deem it worthy to do."
        scene ch6sc02_1198 with dissolve
        mc "One of the people who will be helped by finding this ambassador is Pearl’s sister, Kira."
        mc "We’re grateful for you opening your home to us and for your willingness to assist."


    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_1192 with dissolve
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    ec "[mc], we do have something to gain by helping you..."
    ec "Your trust and respect. Just like you seek to earn ours, I wish for us to earn yours too."
    scene ch6sc02_1188 with dissolve
    mc "Thank you. I appreciate that."
    scene ch6sc02_1189 with dissolve
    ec "[mc]... you needn't thank me. We’ve been set in our ways for too long."
    scene ch6sc02_1187 with dissolve
    ec "If we stay shut off from the wider world, we’ll just end up like the Arugoh tribe."
    ec "The last thing I want is for our tribe to grow bitter and hateful."
    ec "You being here is solid proof that not all outsiders wish us harm."
    scene ch6sc02_1188 with dissolve
    mc "Believe me, not everyone will want to cause you harm."
    mc "But being careful and wary of outsiders is a good thing on your part."
    mc "I don't want you to relive the trauma of the past..."
    mc "And there are definitely people out there who would try to take advantage."
    scene ch6sc02_1190 with dissolve
    sj "We are lucky, then, that you are not like that."
    sj "But we still cannot trust you blindly... at least not yet."
    scene ch6sc02_1191 with dissolve
    mc "I understand."
    mc "I’ve been thinking about these trials... I might give it a go and attempt to complete them."
    scene ch6sc02_1190 with dissolve
    sj "If you prove yourself in such a way..."
    sj "Not a single member of the tribe could deny your allegiance to us."
    scene ch6sc02_1184 with dissolve
    ec "You all know your roles and what to do."
    ec "Given how late in the afternoon it is, the excursion will not be too far from A’nai."
    scene ch6sc02_1185 with dissolve
    ec "I do not suspect any trouble, but do remain alert."
    ec "Even having Suji and Zyra with you, it never hurts to be cautious."
    scene ch6sc02_1197 with dissolve
    zy "Let us not remain idle."
    sj "You heard the A’nu."
    sj "We haven’t got many hours of daylight left. Let’s make use of what we have."
    scene ch6sc02_1192 with dissolve
    ec "Indeed. Huntresses at the ready."
    ec "I will pray to Gaia that you find something that can potentially lead you to your ambassador."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1202 with Dissolve(1.5)
    $ renpy.pause(1)
    "And so, your little group set out: the gates of A’nai behind you, and the dense jungle ahead."
    "The two huntresses keep silent for the most part, remaining vigilant and observant."
    scene ch6sc02_1203 with dissolve
    "While Miyo and Pearl eagerly discuss about every little detail they can think of."
    "Everyone seems excited for this little outing."
    scene ch6sc02_1204 with dissolve
    uk "So, this is where they snuck off to... *Scoffs*"
    uk "I don’t see her among them... he’s probably keeping my baby locked up! Tsk!"
    scene ch6sc02_1205 with dissolve
    uk "Don’t worry, baby... I won’t allow this... boy... to put his filthy hands on you."
    uk "He will regret the day he took you from me!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1206 with Dissolve(1.5)
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mh "Goddesses... grant me wisdom."
    mh "Hear my prayers..."
    scene ch6sc02_1207 with dissolve
    mh "The outsider... Tsk!"
    mh "He has begun to corrupt the tribe..."
    if mh_charm == True:
        mh "He almost had me fooled by his venomous tongue!"
        mh "I need to be careful around him... he's incredibly handsome- no! Tsk!"
        mh "He's nothing but a fiend! A devil! No matter how beautiful he is..."

    else:
        pass
    scene ch6sc02_1208 with dissolve
    mh "His shadowy tendrils have taken hold of their young minds..."
    mh "Echo knows not what horrors lie ahead if she continues to entertain this... man."
    scene ch6sc02_1209 with dissolve
    mh "Goddesses... Malanthe... Gaia... Maia..."
    mh "Give me a sign that I am just in my beliefs, that this outsider... must be stopped."
    mh "..."
    scene ch6sc02_1210
    with vpunch
    mh "I knew it... you do agree with me."
    scene ch6sc02_1211 with dissolve
    mh "Of course you do, he’s a filthy outsider."
    mh "Don’t worry, Goddesses. I will take care of it... I know what must be done"
    scene ch6sc02_1212 with dissolve
    mh "Hmh... yes, yes... that will do it."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mh "That should work just fine indeed."
    scene ch6sc02_1213 with dissolve
    play music dark_1 fadein 1.0
    #stop music fadeout 1.0
    "Indistinct cackling in the flames..."
    scene ch6sc02_1213a with dissolve
    of "*Insidious cackling* Hmh-hnh-hmh..."
    scene ch6sc02_1214 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_1215 with dissolve
    $ renpy.pause(1)
    "..."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    "After an hour of trekking through the jungle, your group pauses for a moment."
    scene ch6sc02_1216 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    mc "So, how is everyone holding up? Anybody need a rest, or see anything of interest?"
    scene ch6sc02_1217 with dissolve
    pl "Hmh..."
    pl "My feet are a little sore, they aren’t used to walking on the uneven terrain."
    pl "But its not something we need to take a break for."
    scene ch6sc02_1218 with dissolve
    mi "I am doing great."
    mi "In fact, I’ve already spotted several edibles we can collect."
    scene ch6sc02_1219 with dissolve
    zy "We haven’t spotted any dangers, predators usually don’t come too close to the village."
    zy "And there’s no sign of the mist either."
    scene ch6sc02_1220 with dissolve
    sj "But also, no sign of the ambassador..."
    sj "Sorry..."
    scene ch6sc02_1221 with dissolve
    mc "Yeah... I haven’t noticed anything either."
    mc "What is the mist you mentioned? Echo also said something about it earlier, but only briefly."
    scene ch6sc02_1219 with dissolve
    zy "The mist is... mysterious."
    zy "The jungle is already like a labyrinth... but the mist can make it impossible to navigate."
    scene ch6sc02_1220 with dissolve
    sj "It is known."
    sj "You see, the mist creeps through the jungle slowly. But wherever it touches... the jungle changes."
    scene ch6sc02_1221 with dissolve
    mc "Changes? ... how?"
    scene ch6sc02_1219 with dissolve
    zy "The paths... the vegetation... all... shift. And if you're caught inside it, you lose all sense of direction."
    scene ch6sc02_1220 with dissolve
    sj "The mist has claimed many good huntresses over the years."
    scene ch6sc02_1219 with dissolve
    zy "If we encounter it, we’ll hunker down until it passes, walking through it is pointless."
    scene ch6sc02_1221 with dissolve
    mct "{i}Hmh... this mist sounds magical if its able to alter the jungle itself...{/i}"
    mct "{i}Could it be the mist that blocks other magic on the island?{/i}"
    mc "I’m not too worried. If this mist comes, I’m sure we’ll easily find our way with two great huntresses such as you."
    mc "I'm counting on you to guide us to a safe location."
    scene ch6sc02_1222 with dissolve
    sj "*Scoffs* Hear that Zyra? He thinks he can just assign us tasks?"
    scene ch6sc02_1223 with dissolve
    zy "And we’d just accept it? He probably expects us to bend over for him too."
    scene ch6sc02_1221 with dissolve
    mct "{i}*Chuckles* Are they even hearing themselves?{/i}"
    mc "Ladies, I didn’t mean to offend-"
    scene ch6sc02_1222 with dissolve
    sj "Let me guess, you want us to kneel down before you?"
    scene ch6sc02_1223 with dissolve
    zy "What then? Close our eyes and open our mouths?"
    scene ch6sc02_1221 with dissolve
    mc "Hey- that's not-"
    scene ch6sc02_1224
    with vpunch
    bth "*Laughing* At ease, [mc]... we are just teasing you."
    mc "I had a feeling you were pulling my leg."
    scene ch6sc02_1219 with dissolve
    zy "Pulling your leg? We did no such thing."
    scene ch6sc02_1221 with dissolve
    mc "No, it’s not meant literally."
    mc "It’s a figure of speech for when you mess with someone."
    scene ch6sc02_1220 with dissolve
    sj "Ahh, the outsider is humorous."
    scene ch6sc02_1217 with dissolve
    pl "I’d really prefer it if we don’t encounter the misty mist..."
    pl "Being lost out here wasn’t a nice feeling even without it."
    scene ch6sc02_1225 with dissolve
    mi "Do not worry, Pearl..."
    mi "We're in capable hands with Suji and Zyra."
    scene ch6sc02_1226 with dissolve
    mi "As long as you’re with us, you won’t be alone."
    mi "Even if the mist comes, we’ll wait it out together, then find our way back."
    scene ch6sc02_1227 with dissolve
    pl "Really?"
    pl "You promise you won't just abandon us out here?"
    scene ch6sc02_1225 with dissolve
    mi "Yes, your fears are valid but totally unnecessary."
    scene ch6sc02_1226 with dissolve
    mi "Suji and Zyra are the best Huntresses in A’nai. And we have both of them with us!"
    scene ch6sc02_1228 with dissolve
    sj "*Scoffs lightly* ..."
    sj "You seem to have been taught well, young one."
    scene ch6sc02_1229 with dissolve
    mi "I can’t take all the credit. It’s mostly because I listen to Vex sing your praises."
    mi "At least once or twice a day she talks about how great the two of you are."
    scene ch6sc02_1230 with dissolve
    zy "Oh? And what is little Vex saying?"
    scene ch6sc02_1229 with dissolve
    mi "Nothing bad. I’ll leave it at that."
    scene ch6sc02_1231 with dissolve
    mi "I’ve already said too much."
    mi "*Quietly* If she found out, it’d be the end of me. Certain doom."
    mct "{i}Hmh, it sounds like Vex idolizes these huntresses... makes sense given she’s training to become one.{/i}"
    scene ch6sc02_1230 with dissolve
    zy "Hmm, Vex..."
    zy "Isn’t she the one training with Kisha at the moment?"
    scene ch6sc02_1229 with dissolve
    mi "Y-Yes! That’s her."
    mi "She hopes to become a great huntress."
    mi "And one day, ascend to become a war-maiden."
    scene ch6sc02_1228 with dissolve
    sj "I haven’t seen her train personally, but I’ve heard great things about little Vex."
    sj "She has great potential, despite her youth."
    scene ch6sc02_1216 with dissolve
    mc "I watched Vex spar with Kisha, she was great... very agile."
    mc "Has Kisha trained all of you?"
    scene ch6sc02_1219 with dissolve
    zy "Yes, Kisha is the head-huntress."
    zy "Her duty is to direct and oversee all the huntresses."
    scene ch6sc02_1221 with dissolve
    mc "Hmmh..."
    scene ch6sc02_1220 with dissolve
    sj "What is it, outsider? Speak your mind."
    scene ch6sc02_1221 with dissolve
    mc "It’s nothing."
    scene ch6sc02_1220 with dissolve
    sj "We do not keep secrets. If you wish to gain our trust, then tell us."
    scene ch6sc02_1221 with dissolve
    mc "Well, I just noticed that the two of you seem more..."
    mc "Open to my presence here? Kisha, though... she has been quite aloof since I got here."
    scene ch6sc02_1220 with dissolve
    sj "What do you mean by this?"
    scene ch6sc02_1219 with dissolve
    zy "Tell us, outsider... we wish to know."
    scene ch6sc02_1216 with dissolve
    mc "I’m just saying, you’re both friendlier than her."
    scene ch6sc02_1222 with dissolve
    sj "Are you complimenting us, or insulting her?"
    scene ch6sc02_1221 with dissolve
    mc "Complimenting the two of you, definitely. It’s just that, you’re her two greatest huntresses..."
    mc "So, I guess I kind of expected you to be... more like her? To share her attitudes towards me and Pearl?"
    scene ch6sc02_1219 with dissolve
    zy "We may be her most esteemed huntresses, but despite that -"
    scene ch6sc02_1223 with dissolve
    zy "We are still ourselves. Kisha’s beliefs and attitudes are not ours."
    scene ch6sc02_1222 with dissolve
    sj "Zyra and I don’t always agree on everything, either."
    scene ch6sc02_1219 with dissolve
    zy "It is known."
    sj "..."
    scene ch6sc02_1224 with dissolve
    bth "*Laughing* We may be sisters, but even so... we disagree often!"
    mct "{i}Ahh, so my suspicion was correct, they are sisters.{/i}"
    scene ch6sc02_1232 with dissolve
    pl "[mc]! I can’t believe you just assumed that."
    pl "If anyone should know that people aren’t the same as their mentors, it should be you."
    scene ch6sc02_1233 with dissolve
    mc "What do you mean?"
    scene ch6sc02_1232 with dissolve
    pl "You know that Kira and I are nothing like our father... and-"
    pl "I'm sure you aren’t like your mentor, Oren, either..."
    scene ch6sc02_1233 with dissolve
    mc "Not anymore... but I was for a time."
    mc "Until... I met Eliza."
    mc "Before I met her, the world was black and white, now... now it’s beginning to fill with color."
    mc "She has taught me a great deal about appreciating the little things."
    scene ch6sc02_1234 with dissolve
    mc "You’re right, though. I shouldn’t be so hasty to assume things."
    "Pearl nods at you, pleased that you acknowledged her point."
    scene ch6sc02_1221 with dissolve
    mc "Suji, Zyra... I’m sorry for assuming you’d be like Kisha."
    mc "Not that there would be anything wrong with that, either. Kisha is definitely not wrong to be cautious."
    scene ch6sc02_1219 with dissolve
    zy "Outsider, thank you... admitting to a mistake takes courage."
    scene ch6sc02_1220 with dissolve
    sj "We appreciate it."
    scene ch6sc02_1218 with dissolve
    mi "Most people would just shrug off being mistaken."
    mi "But not you. You own up to it... Hmm."
    scene ch6sc02_1216 with dissolve
    mc "Well, I’ve often been judged in the past ..."
    mc "So, I’d like to not judge others until I get an understanding of who they are."
    mc "Which is why I should not have assumed things about you."
    scene ch6sc02_1219 with dissolve
    zy "You need not apologize. We are still just getting to know each other. It’s easy to assume things."
    scene ch6sc02_1220 with dissolve
    sj "Zyra is right, we also assumed plenty of things about you when you first arrived."
    sj "Many of those assumptions were clearly wrong, as you have shown through your actions."
    scene ch6sc02_1221 with dissolve
    mc "I’d like to earn your trust."
    bth "..."
    scene ch6sc02_1222 with dissolve
    sj "We... we’ll see, Outsider."
    scene ch6sc02_1223 with dissolve
    zy "We’d like to give it. But our bad experiences are still fresh."
    zy "They still hold a powerful grip on many inhabitants of A’nai"
    scene ch6sc02_1225 with dissolve
    mi "Maybe it’s because I'm young and naive, but I feel like we can trust [mc]."
    mi "He seems genuine and kind..."
    scene ch6sc02_1229 with dissolve
    mi "And his strength can't be denied since he passed the first trial."
    scene ch6sc02_1230 with dissolve
    zy "Your words carry wisdom, young one."
    zy "Completing the first Trial of A'khans proves that he is a capable warrior."
    scene ch6sc02_1232 with dissolve
    pl "Trust me girls, he is very capable... much more than you can imagine."
    scene ch6sc02_1234 with dissolve
    mc "Thank you for the vote of confidence, Pearl. But I understand why they can’t blindly trust us yet."
    scene ch6sc02_1228 with dissolve
    sj "Miyo, you said you’ve already seen edibles in the area? If so, then you guys should begin collecting."
    scene ch6sc02_1229 with dissolve
    mi "Yeah, this area is plentiful."
    scene ch6sc02_1218 with dissolve
    mi "What do you say? Up for a little gathering?"
    mc "Ready as I’ll ever be. Let’s get to work, girls."
    scene ch6sc02_1216 with dissolve
    mc "Suji, Zyra, keep a lookout for anything of interest."
    mc "Meanwhile, the girls and I will collect food for the tribe."
    scene ch6sc02_1221 with dissolve
    bth "..."
    scene ch6sc02_1222 with dissolve
    sj "Did he just... command us? Again?"
    scene ch6sc02_1223 with dissolve
    zy "Mhm, it sounded like it."
    scene ch6sc02_1221 with dissolve
    mc "Yes, I did. Now, get to work."
    scene ch6sc02_1235 with dissolve
    bth "..."
    "The two huntresses turn red and share a bewildered look."
    scene ch6sc02_1236 with dissolve
    sj "C-Come on Zyra, you heard [mc]."
    sj "We'd better get to it."
    scene ch6sc02_1237 with dissolve
    zy "Y-Yeah, let’s see what we can find."
    zy "We shall not disappoint."
    scene ch6sc02_1238 with dissolve
    mct "{i}*Chuckles* Is it me, or did they turn red when I gave them a command?{/i}"
    mct "{i}They seemed to like it, though.{/i}"
    "You feel something soft and gentle"
    scene ch6sc02_1239 with dissolve
    mc "Huh?"
    mi "Come, Hero... let’s begin."
    scene ch6sc02_1240 with dissolve
    mi "I’ve been eager to show you what I can do. *Giggles*"
    mc "Sure, we’ll follow your lead."
    scene ch6sc02_1241 with dissolve
    pl "*Quietly* Hmmrrhhmm..."
    pl "*Quietly* Miyo was totally flirting with you."
    scene ch6sc02_1242 with dissolve
    mc "I’m well aware."
    scene ch6sc02_1243 with dissolve
    pl "*Snickers* Such a ladies man. Before long, I bet you’ll have the entire tribe on their knees for you."
    scene ch6sc02_1242 with dissolve
    mc "Let’s not get ahead of ourselves..."
    mc "But if I manage to complete the other trials, I could see them starting to open up to us more."
    scene ch6sc02_1243 with dissolve
    pl "Starting? That’s an understatement, plenty of them are already warming up to you."
    pl "If you complete the other trials, they'll be eating out of your palm..."
    scene ch6sc02_1244 with dissolve
    pl "You’ll have an entire tribe of gorgeous and sexy warrior women at your beck and call. Your own personal army."
    pl "You’d be their leader, their A’khan."
    pl "You could call upon them, if needed, or you could use A’nai as a hideaway."
    pl "*Squeezes arm gently* Or as your personal getaway sanctuary for vacations."
    scene ch6sc02_1245 with dissolve
    mct "{i}She makes great points... there’s no denying the potential of this place and the benefits of being their leader...{/i}"
    mct "{i}Should we ever need it, A’nai would make a great hideout.{/i}"
    mct "{i}And... each and every one of them has basic combat training, even their priests and herbalists.{/i}"
    scene ch6sc02_1246 with dissolve
    mi "C’mon, you two! We’re burning daylight!"
    mc "Miyo, what in the five hells are you up to? Get down."
    mc "You’re not a monkey... you’ll fall on your ass."
    scene ch6sc02_1247 with dissolve
    mi "I’ve spent years studying the Moon-monkeys! It’s easy once you get the hang of it."
    mi "All the best fruit grows at the top of the trees. Don’t worry I’m experienced-"
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_1248
    play music darknight_4 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    mi "*Gasps* Auuuuaaahhh!!"
    scene ch6sc02_1249
    with vpunch
    pl "Miyo!"
    pl "[mc], catch her!"
    scene ch6sc02_1250 with dissolve
    mc "*Sighs* ..."
    scene ch6sc02_1250a with dissolve
    $ renpy.pause()
    scene ch6sc02_1250b
    with vpunch
    $ renpy.pause()
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_1251
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    with vpunch
    mi "*Gasps* Y-You caught me?"
    scene ch6sc02_1252 with dissolve
    mc "I wasn’t about to let you fall on your ass."
    scene ch6sc02_1251 with dissolve
    mi "Y-You... *Quietly* really are a Hero."
    scene ch6sc02_1253 with dissolve
    mi "Thank you, [mc]..."
    mi "You’re really strong... incredible."
    scene ch6sc02_1254 with dissolve
    mi "Your chest, it’s so... firm. Hard, even. Very unlike a woman's..."
    mc "Right, you’ve never seen a man before... we’re different in several ways."
    scene ch6sc02_1255 with dissolve
    mi "Oh? I quite like it. You're different..."
    scene ch6sc02_1254 with dissolve
    mi "A little strange, perhaps. But you feel really warm and solid."
    scene ch6sc02_1255 with dissolve
    mi "Your chest is hardened, like armor, while mine is soft... but they’re both warm."
    scene ch6sc02_1254 with dissolve
    mi "My stomach is flat and soft, while yours is outlined with muscles and scars..."
    scene ch6sc02_1253 with dissolve
    mi "I wonder what else is different between us?"

    ####Choice####
    menu:
        "Flirt with her. ":
            scene ch6sc02_1252 with dissolve
            mc "Maybe I’ll show you some time."
            scene ch6sc02_1253 with dissolve
            mi "I... I think I’d like that... very much."
            mi "Especially if you hold me like this while... showing me."
            scene ch6sc02_1252 with dissolve
            mc "I think that can be arranged."
            $ mi_trust += 2
            "Miyo enjoys that you took the chance to flirt with her, trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch6sc02_1254 with dissolve
            mc "Are you good to stand?"
            mi "Y-Yeah, I wasn’t hurt... thanks to you."

        "Put her down.":
            scene ch6sc02_1252 with dissolve
            mc "I’m sure you’ll find out some day. Here, let me put you down."

    scene ch6sc02_1256 with dissolve
    mi "So... uh... t-thank you for catching me..."
    mi "I should've been more careful, I was just eager to show you -"
    scene ch6sc02_1257
    with vpunch
    pl "Miyo!"
    mi "I am okay..."
    mi "Thanks to [mc]... you need not worry."
    scene ch6sc02_1258 with dissolve
    mi "Believe it or not, this is not the first time I’ve fallen trying to get to the ripe fruits."
    scene ch6sc02_1259 with dissolve
    pl "You really should be more careful!"
    pl "So, you’re not hurt or anything?"
    scene ch6sc02_1258 with dissolve
    mi "No, no... worry not. I am fine."
    scene ch6sc02_1260 with dissolve
    mc "I’m glad you didn’t hurt yourself."
    mc "Did we manage to get any fruit, at least?"
    scene ch6sc02_1261 with dissolve
    mi "Yeah, a few... we’ve gathered all we need from here."
    mc "Are you sure?"
    scene ch6sc02_1262 with dissolve
    mc "I can see more fruit up there in the canopy. Shouldn’t we collect more?"
    scene ch6sc02_1263 with dissolve
    pl "Nuh-uh. They aren’t ripe yet."
    pl "Miyo taught me it’s bad to take them too early."
    scene ch6sc02_1264 with dissolve
    mi "Your friend is correct. We don't take more than we need."
    mi "Some of what the jungle provides must be left alone."
    scene ch6sc02_1262 with dissolve
    mc "What if they were ripe?"
    scene ch6sc02_1264 with dissolve
    mi "Even so. The other inhabitants of the jungle also need food."
    mi "It’s important that the animals can also eat."
    scene ch6sc02_1263 with dissolve
    pl "I get it. For the whole ecosystem to thrive, everything should be done in moderation."
    mi "Correct. You understood what I told you perfectly."
    scene ch6sc02_1264 with dissolve
    mi "The jungle is not ours alone."
    mi "We share it with all living creatures here."
    scene ch6sc02_1262 with dissolve
    mc "So, to keep the jungle in balance, you can’t just be greedy and take everything."
    scene ch6sc02_1264 with dissolve
    mi "Exactly! There needs to be balance between all living things."
    mi "If we care for the jungle, then it will care for us in return."
    mi "Such is the will of Gaia."
    scene ch6sc02_1262 with dissolve
    with vpunch
    mc "*Calls out* Everyone, gather up!"
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch6sc02_1216 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    $ renpy.pause(1)
    if leadership >= 12:
        mc "Alright girls, we've foraged for edibles and have acquired a decent amount."
        mc "It's time to turn our attention to our next objective, the ambassador."
        evr "*Nods in agreement* Mhm-hm!"
        mc "We'll keep a keen eye on our surroundings, anything that seems out of place."
        mc "And scan the ground for possible footprints."
        evr "*Nods in agreement* Mhm-hm!"
        $ leadership += 1
        "The girls seem to enjoy you taking the lead, they've listened to you attentively."
        "Your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
        scene ch6sc02_1218 with dissolve
        mi "Great idea [mc], I'll keep my eyes peeled for anything of interest!"
        $ mi_trust += 2
        "Miyo liked seeing you take charge, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        mi "Hopefully we can find something that will lead you to them."

    else:
        mc "Okay, so..."
        mc "If we’ve got the fruit we need, then how about we look around for possible clues about the ambassador?"
        "The girls look at you, clearly not too impressed with your lack of assertiveness."
        $ leadership -= 2
        "Your {b}{color=#ffee54}Leadership{/color}{/b} has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."
        scene ch6sc02_1218 with dissolve
        mi "*Sighs* I suppose we could?"
        mi "Hopefully we can find something that will lead you to them."


    scene ch6sc02_1219 with dissolve
    zy "There are still a few hours of daylight left."
    zy "If you wish, we can continue to look around the area for any sign."
    scene ch6sc02_1220 with dissolve
    sj "I suppose we can stay out here a little longer..."
    scene ch6sc02_1221 with dissolve
    mc "Thank you girls, follow me."
    scene ch6sc02_1232 with dissolve
    pl "Where are we going?"
    scene ch6sc02_1233 with dissolve
    mc "I’ve been sensing a weak trace of magic out here. I want to see what it could be."
    scene ch6sc02_1231 with dissolve
    mi "*Quietly* M-Magic...?"
    scene ch6sc02_1223 with dissolve
    zy "What is this magic you speak of?"
    scene ch6sc02_1222 with dissolve
    sj "Did you eat something you weren’t supposed to?"
    sj "The priestesses and shamans of A’nai have lost their magic..."
    scene ch6sc02_1223 with dissolve
    zy "We lost access to magic during the great desecration..."
    zy "How is it that you sense anything?"
    scene ch6sc02_1221 with dissolve
    mc "It’s a long story..."
    mc "Just, follow me."
    scene ch6sc02_1218 with dissolve
    mi "Let’s do as he says."
    mi "I believe he is being truthful."
    scene ch6sc02_1225 with dissolve
    mi "If he really can sense magic, that is truly a special gift!"
    mi "Maybe it could help our people gain it back?"
    scene ch6sc02_1228 with dissolve
    sj "Young Miyo has a point."
    sj "Gaining the favor of the Goddesses again would be of great importance to our people."
    scene ch6sc02_1229 with dissolve
    mi "Exactly! A'nu believes in him- and so do I."
    mi "If she is right and he is the one who has been promised, then he will mend our bond with the goddesses."
    scene ch6sc02_1230 with dissolve
    sj "Fine, fine..."
    sj "Let’s see if he’s all talk or not."
    scene ch6sc02_1232 with dissolve
    pl "Lead on. We’ll follow you."
    scene black with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    "Leaving the foraging area... you follow the faint trace of magic in the air."
    scene ch6sc02_1203 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    $ renpy.pause(1)
    mi "I think it’s pretty neat you can sense magic. Can all men do this where you’re from?"
    mc "*Chuckles* No, I’m... an outlier."
    mi "What is that?"
    scene ch6sc02_1204 with dissolve
    pl "It means that he’s special, unique, one of a kind."
    mi "Huh... interesting."
    scene ch6sc02_1238 with dissolve
    mc "Suji, Zyra... halt."
    scene ch6sc02_1241 with dissolve
    pl "Can you sense something?"
    scene ch6sc02_1242 with dissolve
    mc "Mhm... the feeling is getting stronger."
    scene ch6sc02_1244 with dissolve
    pl "I knew you could do it!"
    scene ch6sc02_1265 with dissolve
    mc "That clearing over there... that’s where it’s coming from."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc02_1266 with Dissolve(1.5)
    $ renpy.pause(1)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    "As your group emerges from the thick undergrowth, you find yourself in disbelief."
    scene ch6sc02_1267 with dissolve
    mi "Woah! I’ve never seen anything like it..."
    pl "It does look pretty cool... and, very old."
    scene ch6sc02_1268 with dissolve
    mi "Suji, Zyra! Have you ever seen anything like this?!"
    sj "We have not..."
    scene ch6sc02_1269 with dissolve
    zy "The jungle keeps surprising us even after all these years..."
    sj "[mc] was right... I wonder what it is?"
    scene ch6sc02_1270 with dissolve
    mc "It’s some sort of magical artifact."
    mc "Look, it’s levitating and giving off light..."
    scene ch6sc02_1271 with dissolve
    zy "Outsider, you... you were able to feel this thing?"
    zy "From all the way back at the foraging area?"
    mc "Yeah. There was only a very faint trace... I could barely feel it."
    mc "But now that we’re standing here, the feeling is intense."
    scene ch6sc02_1272 with dissolve
    mi "You really are special..."
    mi "I wish I could feel it too!"
    mi "It’s incredible that you could lead us here just following a feeling."
    scene ch6sc02_1273 with dissolve
    sj "The mist has claimed the jungle..."
    zy "*Exhales* I was hoping we’d be able to avoid it today..."
    scene ch6sc02_1274 with dissolve
    sj "Me too. We’ll have to hunker down here until it passes."
    sj "We’ll stay near this shrine and wait out the mist."
    scene ch6sc02_1275 with dissolve
    pl "Psst, [mc]..."
    mc "Pearl? What is it?"
    pl "I don’t like it here... can’t we go back to the village?"
    scene ch6sc02_1276 with dissolve
    mc "We’ll have to stay here until the mist is gone. You heard them, the mist changes the jungle."
    mc "There’s no telling what else it’s capable of."
    mc "But don’t worry... you know I won’t let anything happen to you."
    scene ch6sc02_1275 with dissolve
    pl "*Nods* Mhm, thank you."
    scene ch6sc02_1277 with dissolve
    mc "Hmh... what is the purpose of this thing?"
    mc "It’s surrounded by some purple mist... could it be related to the mist in the jungle?"
    scene ch6sc02_1278 with dissolve
    mc "The necklace... it’s humming the closer I get..."
    mc "Are they connected somehow, or is it just reacting to the magic?"
    scene ch6sc02_1279 with dissolve
    zy "Strange isn’t it?"
    scene ch6sc02_1280 with dissolve
    zy "We’ve lived in A’nai, surrounded by the jungle our entire lives..."
    zy "And yet..."
    scene ch6sc02_1281 with dissolve
    zy "There are still things we have yet to discover, such as this."
    mc "Yeah, the world is filled with lost secrets like this."
    zy "Is that one of the reasons you walk the Adventurer’s path?"
    mc "Yeah, it’s one of the reasons."
    scene ch6sc02_1280 with dissolve
    zy "Fascinating."
    scene ch6sc02_1282 with dissolve
    mc "Do you know what it could be?"
    scene ch6sc02_1281 with dissolve
    zy "There is a tale from our ancestors..."
    zy "But there’s no way for me to verify its truth."
    scene ch6sc02_1282 with dissolve
    mc "What is the tale?"
    scene ch6sc02_1283 with dissolve
    zy "Centuries ago, when the temples and trials were created, they also made a number of shrines..."
    scene ch6sc02_1281 with dissolve
    zy "Each shrine contains a keystone that is needed to complete its corresponding trial."
    zy "Or perhaps it is used to gain entry to the corresponding temple?"
    zy "But we've never confirmed it."
    scene ch6sc02_1283 with dissolve
    zy "I believe this could be one such shrine, and the artifact at the center could be its keystone."
    scene ch6sc02_1280 with dissolve
    mc "Does that mean... one of the temples could be nearby?"
    scene ch6sc02_1281 with dissolve
    zy "Possibly. But as I said... I have no way to be sure."
    zy "They are just old stories..."
    scene ch6sc02_1283 with dissolve
    zy "Our ancestors were closely connected to the gods, who gave them magic to use for constructing the temples."
    scene ch6sc02_1284 with dissolve
    sj "But ever since the outsider arrived, the old tales have revealed themselves to be true."
    sj "The talisman around his neck is solid proof of that."
    scene ch6sc02_1285 with dissolve
    zy "Hmmh. I agree."
    zy "Some of our old tales could be true, after all."
    mc "Huh? There are footprints here."
    scene ch6sc02_1286 with dissolve
    pl "Footprints? Could they be ours?"
    scene ch6sc02_1287 with dissolve
    mc "No, these are at least one or two days old."
    scene ch6sc02_1286 with dissolve
    pl "Wait... are you suggesting that someone else was here recently?!"
    scene ch6sc02_1284 with dissolve
    sj "We didn’t even know this place existed."
    sj "Who could possibly have been here?"
    scene ch6sc02_1285 with dissolve
    mc "Hmm..."
    mc "By the size of them, I’d say the footprints belongs to a woman."
    scene ch6sc02_1288 with dissolve
    sj "You can tell just by looking? Unexpected for an outsider..."
    sj "We spend years learning how to track the various animals of the jungle."
    scene ch6sc02_1289 with dissolve
    zy "Tracking is a valuable skill, and hard to master. It is known."
    zy "You possess that knowledge? Hmm."
    scene ch6sc02_1290 with dissolve
    mc "I may not have as much experience with it as the two of you, but I didn’t grow up in a city either."
    mc "I’ve spent most of my life on the move..."
    mc "Tracking food was essential if I wanted to eat."
    scene ch6sc02_1289 with dissolve
    zy "I see."
    zy "You’re a survivor... just like us."

    if charisma >= 8:
        scene ch6sc02_1290 with dissolve
        mc "Yeah, I suppose we’re quite alike in that regard."
        mc "That's quite the compliment coming from adept huntresses such as yourselves."
        scene ch6sc02_1288 with dissolve
        sj "A compliment you seem to be earning by every passing moment."
        scene ch6sc02_1289 with dissolve
        zy "Huntresses do not compliment freely, it is known."
        $ sj_trust += 2
        scene ch6sc02_1288 with dissolve
        sj "It is known."
        scene ch6sc02_1290 with dissolve
        $ zy_trust += 2
        mc "Neither do I, I can clearly tell the two of you are formidable women."
        "You had enough {color=#87e1fa}Charisma{/color} to successfully compliment them, their trust in you has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

    else:
        pass



    scene ch6sc02_1288 with dissolve
    sj "If someone has been here recently, they could still be nearby."
    scene ch6sc02_1291 with dissolve
    mc "I’m going to check it out. See where they lead."
    mc "You guys stay put and remain alert."
    scene ch6sc02_1292 with dissolve
    pl "[mc]!"
    pl "We shouldn’t split up!"
    scene ch6sc02_1293 with dissolve
    pl "You could get lost out there in the mist..."
    pl "I don't like it."
    scene ch6sc02_1294 with dissolve
    zy "Your friend has a point. The mist is hard to navigate and you could easily lose your way."
    zy "Don’t go too far. We’ll have to return to A’nai as soon as the mist clears."
    scene ch6sc02_1292 with dissolve
    pl "Hnngh... I still don’t like this."
    scene ch6sc02_1295 with dissolve
    zy "His will is strong, he has a survivor's spirit, and he successfully overcame the Trial of A'khans."
    zy "Believe in him."
    scene ch6sc02_1293 with dissolve
    pl "Mmm... I do!"
    pl "I’m just worried... we don’t know what else is out here."
    scene ch6sc02_1291 with dissolve
    mc "Pearl, you don’t need to worry. Besides, if I get lost, I can follow the magic to get back."
    scene ch6sc02_1294 with dissolve
    zy "Go on. We’ll remain here as long as the mist lingers."
    zy "Once it clears, we’ll head back to A’nai. If you aren’t back by then, you’ll have to return on your own."
    scene ch6sc02_1296 with dissolve
    mc "I understand. See you later, girls."
    scene ch6sc02_1297 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_1298 with dissolve
    $ renpy.pause(1)
    scene ch6sc02_1299 with dissolve
    $ renpy.pause()
    scene black with Dissolve(2)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    stop music fadeout 1.0
    jump ch6sc3

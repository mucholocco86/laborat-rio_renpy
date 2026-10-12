label ch6sc10:

    window hide dissolve
    scene black with Dissolve (1.0)
    $ renpy.pause(0.1)
    scene ch6sc08_319 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Don’t mind if I do, you know how I like the comforts of your bed."
    scene ch6sc08_320 with dissolve
    mc "Normally fancy beds aren’t my thing, they’re too soft for my liking."
    scene ch6sc08_321 with dissolve
    mc "But the ones your tribe has seem to have the right amount of comfort and stiffness."
    scene ch6sc08_322 with dissolve
    riv "I Agree, if it were any softer I doubt I could fall asleep."
    riv "I expect I’d be twisting and turning just to find a comfortable position."
    scene ch6sc08_323 with dissolve
    riv "*Sighs* Which is a lot less interesting when you’re on your own."
    scene ch6sc08_324 with dissolve
    riv "Hnngh, make some room for your Grandhuntress."
    mc "I’ll always have room for you, Grandhuntress."
    scene ch6sc08_325 with dissolve
    riv "..."
    scene ch6sc08_326 with dissolve
    riv "So, what brings you to my chambers in the middle of the night?"
    scene ch6sc08_325 with dissolve
    mc "I was on my way back to my own chambers to get some rest, then I saw your door cracked open."
    mc "I decided I’d check on you before I went to sleep."
    scene ch6sc08_326 with dissolve
    riv "You… you were concerned about me?"
    scene ch6sc08_325 with dissolve
    mc "Well, yeah?"
    mc "You’re about to uproot your whole life, all you’ve known for the last 20 years."
    scene ch6sc08_327 with dissolve
    riv "Honestly? It’s a relief…"
    scene ch6sc08_328 with dissolve
    riv "Most of us are eager to be reunited with A’nai."
    riv "We split off on our own because our elders at the time didn’t see eye to eye."
    scene ch6sc08_326 with dissolve
    riv "I simply went with them because the elders believed it would be best if I went."
    riv "They claimed it was the only way for me to fulfill my mother’s wish."
    scene ch6sc08_325 with dissolve
    mc "Your mother?"
    mc "I don’t think I’ve met her?"
    scene ch6sc08_326 with dissolve
    riv "You wouldn’t have… she is long dead."
    riv "She died the night of us overthrowing the outsiders."
    scene ch6sc08_325 with dissolve
    mct "Hmm, I'm sure several lives were lost that night, but it almost sound like it could be...?"
    mc "Who-"
    scene ch6sc08_326 with dissolve
    riv "My mother was the previous A’nu."
    scene ch6sc08_325 with dissolve
    mc "Wouldn’t that mean… you’re-"
    scene ch6sc08_326 with dissolve
    riv "That Echo is my sister? Yes."
    scene ch6sc08_328 with dissolve
    riv "Mother was only able to bear two children. Her pregnancy with Echo was a rough one."
    riv "The priestesses said she would likely die if she attempted to have another."
    scene ch6sc08_325 with dissolve
    mc "That means… Echo is your younger sister?"
    "Riven nods gently."
    mc "Then how come she is the A’nu and not you? Why were you sent away?"
    scene ch6sc08_326 with dissolve
    riv "Because of my strength… my power."
    riv "Our elders wanted to ensure the tribe who split off could have a leader with good morals."
    scene ch6sc08_328 with dissolve
    riv "Since I was older than Echo, and had unmatched strength, due to Maia's blessing."
    riv "I was a better fit for this task."
    scene ch6sc08_325 with dissolve
    mc "I know what it feels like to lose your parents and home at a young age."
    mc "I found my parents killed in our home, when I was 10."
    mc "Then, immediately, I was taken away from all I knew."
    scene ch6sc08_326 with dissolve
    riv "You mentioned this during our trial, but I did not wish to pry..."
    riv "Just 10? That is horrendous… I was 12 as you know, we share such… similar pasts."
    riv "I… I wish we didn’t have to go through that."
    scene ch6sc08_329 with dissolve
    mc "Yeah, its weird how the most awful thing I’ve had to endure has also led to the greatest things in my life."
    mc "I wouldn’t have met a lot of the people I care about today…"
    "Riven gently combs her hand through her hair, pushing it behind her ear as she listens attentively."
    scene ch6sc08_330 with dissolve
    mc "I wouldn’t have arrived here on Aruna, discovered your people, met… you."
    mc "So while we've had to endure unspeakable hardships in life, it has also led to something good."
    scene ch6sc08_331 with dissolve
    riv "I didn’t think of it that way, that’s actually a lovely way of seeing it."
    scene ch6sc08_333 with dissolve
    riv "*Sighs* I doubt anything will ever mend the wounds we carry from losing our loved ones."
    riv "But we endure… we find the strength to continue on… and eventually, the wounds harden and turn to scars."
    scene ch6sc08_331 with dissolve
    riv "Like when you arrived here and as I got to know you… my scars didn’t trouble me as much."
    riv "I began to feel new sensations within my body, new feelings… feelings that helps me endure the scars."
    scene ch6sc08_332 with dissolve
    mc "I know what you mean."
    scene ch6sc08_330 with dissolve
    mc "Nothing can erase our scars, but the people around us can help ease their pain."

    if riv_relationship == True:
        mc "I share your feelings Riven, you too have helped ease my pain."
        $ riv_trust += 3
        "Riven looks at you with a warm smile, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

    else:
        pass

    mc "Will you share how you gained Maia’s blessing? I've been curious to learn this."
    scene ch6sc08_331 with dissolve
    riv "Mhm, I will."
    riv "You’ve been nothing but patient with me."
    scene ch6sc08_333 with dissolve
    riv "As you know, I obtained her blessing the year of the great desecration, when I was 12."
    riv "I was out in the jungle, training to be huntresses with a friend, but we ventured too far…"
    scene ch6sc08_338 with dissolve
    riv "Before we knew it, we were running for our lives… being chased by a large beast."
    riv "The huntress I was with pushed me out of the way just as the beast pounced on us."
    riv "She-... she and the beast went over the cliff. I ran screaming towards the cliff-"
    scene ch6sc08_340 with dissolve
    riv "-I saw her, hanging off the edge but her grip was slipping, with no time to think my body just acted."
    riv "All I knew was I had to hold on to her with everything I had in me."
    scene ch6sc08_338 with dissolve
    riv "But-... she was older than me, I couldn’t hold her weight and I slipped."
    riv "I managed to grab the ledge at the last second, and she was hanging from my other hand."
    scene ch6sc08_340 with dissolve
    riv "I’ve never felt so much strain on my body, holding up the weight of two people with our lives on the line."
    riv "But it only lasted a few moments then my grip weakened and as I closed my eyes, embracing our fate."
    scene ch6sc08_333 with dissolve
    riv "That’s when it happened… the most incredible warmth I’ve ever felt."
    riv "Suddenly my grip was no longer weakening, the opposite in fact."
    scene ch6sc08_337 with dissolve
    riv "I felt strong, stronger than I could imagine, I was able to pull us both up with ease."
    riv "The relief I felt in that moment… having saved my friend and mentor from falling to her death."
    scene ch6sc08_340 with dissolve
    riv "She didn’t question what happened to me, she just smiled and said, the goddesses have smiled upon me."
    scene ch6sc08_339 with dissolve
    mc "Maia saw you willing to put your life on the line for another, to risk everything for them."
    mc "She decided you were worthy of her blessing and bestowed you with power and abilities to keep doing what you did that day."
    scene ch6sc08_336 with dissolve
    mc "To protect your people."
    scene ch6sc08_337 with dissolve
    riv "[mc]... yes, I believe you are right."
    riv "And I intend to do so, our people will always be under my protection."
    scene ch6sc08_334 with dissolve
    mc "{b}‘Our’{/b} people, I like the sound of that."
    scene ch6sc08_336 with dissolve
    riv "..."
    scene ch6sc08_331 with dissolve
    riv "Good, cause there’s no changing that at this point."
    riv "Tomorrow you will go through the {b}Ceremony of Khans{/b}, and we’ll all become your people, your women."
    scene ch6sc08_332 with dissolve
    mc "Ceremony of Khans? What does that entail?"
    scene ch6sc08_330 with dissolve
    "Riven giggles softly at your question."
    scene ch6sc08_331 with dissolve
    riv "I wouldn’t dare spoil your fun."
    riv "But I believe you will find it most… {b}pleasing{/b}."
    scene ch6sc08_336 with dissolve
    mc "That’s a bold claim, but then again… you know me well enough to make such a claim."

    if riv_relationship == True:
        scene ch6sc08_331 with dissolve
        riv "Mmmh... I know you well enough to be confident about that claim."
        riv "I very much look forward to the ceremony myself... but that is for tomorrow."

    else:
        pass

    scene ch6sc08_340 with dissolve
    riv "[mc]... *Sighs* I… I hate to say this but, you should go to your chambers and rest."
    scene ch6sc08_341 with dissolve
    riv "There’s only about three hours until dawn and I haven’t even finished packing yet."
    scene ch6sc08_342 with dissolve
    riv "I’m pleased I was able to see you, that you… cared to check on me."
    mc "Of course, I couldn’t rightfully walk past your door and not see how you were doing."

    if riv_relationship == True:
        scene ch6sc08_343 with dissolve
        mc "Especially knowing what an incredible ass was hiding in here."
        riv "*Snickers* I can feel your gaze… as much as I enjoy your admiration for my ass… you can admire it tomorrow."
        mc "Hmm, I much prefer to-"
        scene ch6sc08_344 with dissolve
        with vpunch
        mc "*Laughs* H-Hey!"
        riv "*Snickers* Do not finish that sentence!"
        scene ch6sc08_345 with dissolve
        mc "Why not? You know you love it when I-"
        scene ch6sc08_344 with dissolve
        with vpunch
        riv "*Squeezes thighs* No! I don’t want to hear it! If you say it, we won’t get any rest…"
        mc "*Chuckles* Okay, okay… I promise I won’t say it."
        scene ch6sc08_345 with dissolve
        riv "Thank you… I’m already on edge longing for you again… so don’t tempt me."
        riv "Not with such horrible timing."
        scene ch6sc10_001 with dissolve
        riv "*Gasps* AhHh… [mc], I just said-"
        mc "*Kiss* Mmh, relax… I’m just saying goodnight to your lovely thigh."
        mc "You know how I love them… Mmh…"
        scene ch6sc08_345 with dissolve
        riv "R-Right… I remember now… Mmmh… we better get up."
        scene ch6sc08_344 with dissolve
        with vpunch
        mc "*Chuckles* Hey?! Didn’t you just say-"
        riv "In a moment… my thighs wanted to say goodnight to their man as well. *Snickers*"
        riv "*Squeezes thighs* Are you going to behave, my A’khan?"
        scene ch6sc08_345 with dissolve
        mc "I promise… c’mon, I’ve kept you busy for too long already."
        scene ch6sc10_002 with dissolve
        mc "Goodnight gorgeous, I’ll see you in the morning."
        riv "..."
        scene ch6sc10_003 with dissolve
        with vpunch
        riv "[mc]! Wait!"
        "You feel Riven’s delicate hands embrace your arm, desperately clinging to it."
        scene ch6sc10_004 with dissolve
        "But she does not follow up with words, instead you feel her pulling you to her in a warm, intimate embrace."
        riv "*Whispers softly* {size=-7}{b}Please, don’t ever leave me without kissing me.{/b}{/size}"
        scene ch6sc10_005 with dissolve
        riv "Mmgh… Nngh…"
        mc "Mmh… what was I thinking… neglecting my Grandhuntress like this…"
        scene ch6sc10_004 with dissolve
        riv "She does not like being neglected… not by her lover."
        scene ch6sc10_005 with dissolve
        "She eagerly embraces you in another kiss, gently sucking your lips in between her licking your tongue."
        riv "Mmmgh… *Licks* I love feeling your hands on my ass while we embrace… Nnnhh…"
        scene ch6sc10_006 with dissolve
        mc "I can’t help it… I enjoy it too much."
        mc "A perfectly plumb, and firm ass such as yours… I can’t contain myself."
        scene ch6sc10_004 with dissolve
        riv "*Whispers softly* {size=-7}{b}It's a good thing it belongs to you then.{/b}{/size}"
        riv "Now go my love… go before I beg you to toss me on the bed and ravage me until the sun rises."
        mc "Goodnight Riv-"
        scene ch6sc10_005 with dissolve
        riv "Mmhm! Mmhm… *Sucks gently* Nnnh… Goodnight [mc], may your dreams be lovely."
        scene ch6sc10_004 with dissolve
        mc "After this embrace? I have a feeling I’ll be dreaming of you and nothing but you."
        riv "Good… that is how I prefer your dreams to be."
        riv "I can’t wait for your ceremony tomorrow… goodnight."

    else:
        scene ch6sc08_342 with dissolve
        mc "Goodnight then."
        riv "Goodnight my A’khan… see you at dawn."

    scene black with Dissolve(2.5)
    $ renpy.pause(1)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    #$ renpy.pause()
    scene ch6sc10_007 with Dissolve(2.5)
    $ renpy.pause(0.5)
    "As you enter your room, ready to pass out you notice a couple of occupants in your bed."
    mct "*Chuckles* Look at these two…"
    mct "They’ve probably been missing me while I was doing the trials."
    scene ch6sc10_008 with dissolve
    mct "They better not move around too much, I only a have few hours of rest until dawn."
    mct "It’ll be a tight fit, but we should be able to make it work."
    scene ch6sc10_009 with dissolve
    "You let out a long sigh of exhaustion, finally you have a moment of peace and quiet."
    mct "Tomorrow should be interesting, given how many people are moving back to A’nai it won’t be a swift journey..."
    mct "But as long as we don’t have to deal with the mist, we should make it within 5-6 hours I’d guess."
    scene ch6sc10_010 with dissolve
    tz "*Sleepy mumble* Nngh… hi… I’m glad you’re back… Mmhm, ZzZz…"
    "You feel Taz’s soft warm breast squishing against you and her leg embrace yours."
    scene ch6sc10_011 with dissolve
    pl "*Sleepy* Mhm… I missed you sharky… nnh… I knew you would succeed… ZzZz…"
    "Pearl like Taz, shuffles herself onto you seeking comfort, swiftly falling back asleep."
    mct "*Chuckles* I could imagine worse sleeping conditions…"
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss39 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_012 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Little by little, as the tribe awakens they begin to emerge from the temple below."
    sew "Alyze! We're actually going back!"
    sew "Who knew the outsi- no, [mc], would truly be our chosen one?"
    scene ch6sc10_013 with Dissolve(1.5)
    $ renpy.pause()
    tu "We're going home... after two decades."
    ria "Exciting isn't it? Our lives are about to change, for the better."
    tu "I certainly look forward to the ceremony tonight, I have not had the pleasure of meeting our A'khan yet."
    scene ch6sc10_014 with Dissolve(1.5)
    $ renpy.pause()
    siv "Ahh... my legs aren't what they used to be..."

    if siv_path == True:
        siv "I can barely walk straight today."
        sih "*Giggles* That's because you played with daddy all night!"
        siv "*Sighs happily* I couldn't hold back, as soon as he looked at me, I knew... he is your new father."

    else:
        pass

    scene ch6sc10_015 with Dissolve(1.5)
    $ renpy.pause()
    rivt "*Relieved sigh* Mmmmhh... I love the scent of the jungle in the mornings."
    ori "Come on you guys, we don't want to be late for this momentous occasion."
    scene ch6sc10_016 with Dissolve(1.5)
    $ renpy.pause()
    "As you exit the depths of the temple below, you notice the caravan of Arugoh has begun to depart."
    pl "*Inhales deeply* Hnnghh! Yes! Fresh air!"
    tz "I know right? As pleasant as the temple was, it could do with some better airflow."
    scene ch6sc10_017 with dissolve
    ori "Good morning, champion."
    scene ch6sc10_018 with dissolve
    mc "Good morning, Ori."
    mc "I see we’re the last ones to arrive, it looks like most of the tribe has already set forth."
    scene ch6sc10_017 with dissolve
    ori "Mhm-hm. We have quite a few wagons filled with our belongings, I imagine the trek to A’nai will take a while."
    ori "Riven will lead the front of the Caravan, and she suggested you take the rear."
    scene ch6sc10_018 with dissolve
    mc "Makes sense, having our strongest cover the front and back in case anything happens."
    scene ch6sc10_017 with dissolve
    ori "She used those exact words herself, you two really are of a similar mind."
    scene ch6sc10_019 with dissolve
    ori "Shall we? I wanted to wait for you before departing."
    mc "Let’s do it."
    ori "I believe you have quite the ceremony awaiting you back in A’nai."
    scene ch6sc10_020 with dissolve
    mc "What can you tell me about it?"
    ori "Not much, I don’t wish to spoil it for you… but you will need a great amount of stamina. *Snickers*"
    mc "*Chuckles* Is that so? That’s something I’ve got plenty of."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "And so you leave Arugoh and the temple of Maia behind, the caravan keeps a steady pace through the jungle."
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc10_021 with Dissolve(1.5)
    $ renpy.pause(0.5)
    siv "Hey handsome…"
    scene ch6sc10_022 with dissolve
    mc "Hey Sivir."
    mc "How are you holding up? I don’t imagine priestesses often venture through the jungle."
    scene ch6sc10_021 with dissolve
    siv "I’m managing, everyone goes through basic huntress training before we divide into our life paths."
    siv "But I must admit, today's journey has me a little fatigued."

    if siv_path == True:
        scene ch6sc10_023 with dissolve
        siv "But it is not the walking that has me fatigued… I think you know the reason… intimately."
        siv "Don’t you? Handsome…"
        scene ch6sc10_024 with dissolve
        mc "Mmh… I believe I know why you’re having a hard time walking."
        siv "*Moans softly* My love… you have me dripping just at the thought of our next mating."
        mc "I remember your taste vividly, I'd love to enjoy your juices every day of my life."
        scene ch6sc10_025 with dissolve
        siv "*Moans* Here… taste my nectar."
        $ siv_trust += 2
        "Feeling you lick her fingers clean, Sivir enjoys you matching her boldness, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        "You suck her fingers, until every last drop of her juices are cleaned off."
        scene ch6sc10_023 with dissolve
        siv "Mmh… just a little appetizer to keep you hard until the ceremony later. *Giggles*"

        if harem_path == True:
            siv "You're about to have a full island of exotic beauties worshiping you."
            siv "I wouldn't want you to forget me... mmh."
            mc "Then you better give me another taste... just to remind me of who deserves my attetion."
            scene ch6sc10_024 with dissolve
            siv "*Snickers* MMmh- Ohh... another taste you say? How can I deny my sweet A'khan."
            scene ch6sc10_024 with dissolve
            siv "Here baby... drink up, I want my taste to be etched into your mind for tonight."
            mc "*Sucks fingers* Mmffhh... so good... I love that mature taste your flower has."
            scene ch6sc10_023 with dissolve

        else:
            pass

        siv "Come, we better not fall too far behind."

    else:
        scene ch6sc10_022 with dissolve
        mc "I believe we’re about halfway now, you’ll just have to endure a bit more."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "The caravan continues at a steady pace for several hours."
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc10_022 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "Hey, Sivir?"
    mc "I was wondering, what happened to the guy you had kept alive in the dungeons?"
    scene ch6sc10_021 with dissolve
    siv "He is of no use to us anymore, we haven’t even used him for breeding, he wasn’t worthy."
    siv "It will be up to you to decide what happens to him once you become the A’khan."
    siv "Until then he will be put into the cells at A’nai."
    scene ch6sc10_022 with dissolve
    mc "Hmm… I haven’t really thought about what I want to have happen to him."
    mc "We also have a man captive back at A'nai."
    scene ch6sc10_021 with dissolve
    siv "You better give it some thought, as our leader, such decisions fall to you."
    siv "If you want my advice?"
    siv "I’d have him killed, keeping him alive wastes our precious resources."
    scene ch6sc10_022 with dissolve
    "You can hear women calling out from ways up ahead, it seems the front of the caravan has reached the gates of A’nai."
    scene ch6sc10_021 with dissolve
    siv "Finally, home after two decades…"
    siv "I am rather anxious to see everyone, come my love, we're home."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "As the gates open and the caravan little by little enters A’nai, everyone is greeting each other and getting familiar."

    scene ch6sc10_028a with Dissolve(1.5)
    $ renpy.pause(0.5)
    riv "Mmhhphh..."
    ec "I knew he wouldn't fail! I knew he would bring you home!"
    riv "Sister... he did it, he really did it... we're finally together again."
    ec "He's amazing isn't he?"
    riv "He really is... the things I've seen him accomplish..."
    ec "I know, I've seen it with my own eyes... *Giggling* I'm so happy you're back!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_028b with Dissolve(1.5)
    $ renpy.pause(0.5)
    tu "Miyo! You're in good health? How you've grown over the years! Truly blessed by the goddesses I see!"
    mi "*Snickers* I couldn't stop them from growing... suddenly they just decided to get bigger and bigger!"
    bth "*Laughing* ..."
    scene ch6sc10_028c with Dissolve(1.5)
    mi "Tuhi... is there any word of Aiyo? I didn't see my sister amongst you?"
    tu "*Sighs* Aiyo has been missing for a while..."
    mi "*Gasps* Tuhi! Tell me everything!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc06_079 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mh "*Groans* Ugh…"
    scene ch6sc06_078 with dissolve
    mh "They’re back… {b}he’s{/b}… back."
    with vpunch
    mh "Not to mention that {b}insufferable cow!{/b} Sivir… Tsk!"
    scene ch6sc06_077 with dissolve
    mh "There’s only room for {b}one{/b} High-Priestess in A’nai."
    mh "She’s going to snake her way into his mind and twist him against me."
    scene ch6sc06_078 with dissolve
    with vpunch
    mh "Over my dead body!"
    mh "I’ve finally begun to accept his presence amongst us…"
    scene ch6sc06_072 with dissolve
    mh "Finally begun to… enjoy the thought of becoming {b}‘his’{/b}."
    mh "I’m his High-Priestess, and {b}he belongs to me!{/b}"
    scene ch6sc06_073 with dissolve
    mh "I’ll have to keep my eye on that {b}curvaceous cow!{/b}"
    mh "I can't let her steal him from me... not when I've finally started to accept him."
    scene ch6sc06_070 with dissolve
    mh "Time to go meet everyone…"
    scene ch6sc06_069 with dissolve
    mh "That should do it… I wonder…"
    mh "Does he… favor me in this dress?"
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_026 with Dissolve(2.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ec "How does this work? You can just create it out of nowhere with your hands?"
    mc "Essentially, yes."
    mc "When I first acquired Malpheon’s Talisman I gained access to Earth-affinity magic, by absorbing the essence within."
    mc "I’ve been getting used to it during my time here and I know how to create shapes to my will now."
    siv "Echo, sweetheart."
    siv "Do not worry, our Champion is capable of {b}true greatness.{/b}"
    scene ch6sc10_027 with dissolve
    ec "Do not presume to lecture me about his capabilities."
    ec "{b}I know him much better than you{/b}."
    siv "Of course, A’nu."
    siv "I meant no offense."
    mct "There’s still quite a bit of tensions between the two tribes… as expected."
    mct "Two decades of separation won’t just instantly merge smoothly, it will take work on both ends."
    scene ch6sc10_028 with dissolve
    siv "Deepest apologies, A’nu."
    siv "I have recently come to know his strength and it captivates me."
    siv "I truly meant no disrespect to you."
    scene ch6sc10_029 with dissolve
    ec "Your apology is accepted, and allow me to give you the same courtesy…"
    ec "I was a little aggressive in my response."
    scene ch6sc10_030 with dissolve
    siv "Curious…"
    siv "you truly have your mother’s heart, her spirit lives on in you."
    scene ch6sc10_029 with dissolve
    ec "Mother always spoke highly of you Sivir, despite your youth during the desecration, you remained strong."
    ec "You became a renowned leader of the Arugoh branch."
    ec "I look forward to having our people joined once more."
    scene ch6sc10_030 with dissolve
    siv "As do I, sweet Echo."
    siv "I believe it is time we mend our old wounds."
    siv "And I believe [mc] is just the man and leader we need for that to happen-"
    scene ch6sc10_031 with dissolve
    mh "*Hissing* What is the meaning of this?!"
    scene ch6sc10_032 with dissolve
    ec "Marah, great. I was going to send for you but that isn’t needed I see, [mc] is about to create our new shrine."
    siv "Marah! Darling!"
    siv "How lovely to see you haven’t withered away… like a {b}snake{/b}."
    scene ch6sc10_031 with dissolve
    mh "{b}Tsk!{/b} Sivir…"
    mh "I’m surprised you could handle the journey here through the jungle, I know how our hips feel past {b}40{/b}."
    scene ch6sc10_033 with dissolve
    mh "And I can’t imagine how your poor back must feel…"
    mh "Carrying those… {b}exaggerated coconuts{/b} of yours around."
    mct "*Chuckles* Do I sense a rivalry here? They sure like jabbing at each other."
    scene ch6sc10_032 with dissolve
    siv "You needn’t worry about my back, with a strong and handsome A’khan by my side, I find myself stronger than ever."
    ec "That’s enough you two, Marah come join us."
    ec "As High-Priestesses, I wish for both of you to witness this."
    scene ch6sc10_034 with dissolve
    mh "Very well then, I can’t deny that I am eager to see [mc] in action for myself."
    mh "Since he has succeeded in all the trials unlike any A’khan of the past generations… he must truly be worthy."
    scene ch6sc10_035 with dissolve
    "You feel Echo’s soft touch and with her signature gentle voice, she asks you to begin."

    if ec_path == True:
        ec "Please... proceed my love."
        ec "I'm counting on you, we all are."
    else:
        pass

    mc "Everyone take a few steps back, it’s going to be a sizable shrine."
    scene ch6sc10_036 with dissolve
    "The three women do as you command, and with them out of the way you proceed to channel Earth-magic into your palm."
    scene ch6sc10_037 with dissolve
    "As you feel the energy gather, you begin to release it, letting your imagination morph it."
    mh "*Gasps* Incredible…"
    mh "To witness this… to feel such energy..."
    siv "I’ve felt this since I first met him… he truly is the chosen one."
    scene ch6sc10_038 with dissolve
    ec "Marah… Sivir… bear witness… [mc], your rightful A’khan…"
    ec "Is about to change the fate of our people."
    scene ch6sc10_039 with dissolve
    siv "Words escape me…"
    mh "I almost can’t believe my own eyes…"
    "You take a few steps back and join the women while the shrine finishes its construction."
    scene ch6sc10_040 with dissolve
    $ siv_trust += 3
    siv "[mc]... you truly have earned the favor of the goddesses… and the title of A’khan."
    mh "On this matter… we agree."
    $ mh_trust += 3
    "Sivir and Marah both feel strongly about you being the rightful A'khan, their trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."


    if harem_path == True:
        siv "Mmh... I love the idea of being his High-Priestess."
        mh "Tsk! I'm his High-Priestess, you wouldn't even know how to begin worshiping him!"
        siv "*Snickers* Oh I know how to worship him alright, you have much to catch up on."
        mh "Hnnnghh...."
    else:
        pass

    scene ch6sc10_041 with dissolve
    mc "It’s complete."
    mc "The shrine of A’nai, connecting you to Gaia, Malanthe and Maia."
    mc "I have infused each of their communion stones into the statue itself, as such nobody can ever remove them."
    scene ch6sc10_042 with dissolve
    siv "On behalf of our people... now, your people… {b}thank you{/b}."
    siv "Echo said it perfectly… you’re carving a new fate for all of us, the only one who can."
    scene ch6sc10_043 with dissolve
    mh "Marvelous… this material… I’ve never felt its equal."
    ec "It's beautiful."
    mc "I’ve infused it with some of the strongest materials known to me, it should easily last centuries."
    mh "Hear that Echo? Centuries… *Giggles happily*"
    scene ch6sc10_044 with dissolve
    ec "With this order of business settled, it's finally time… come everyone."
    ec "Let us commence the {b}Ceremony of Khans{/b}."
    mh "I can’t believe I find myself speaking these words but… {b}you’ve earned it [mc]{/b}."
    $ mh_trust += 5
    "If Marah had any lingering doubts about you, they were just erased, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "All of you head out together and word of the ceremony spreads like wildfire, while people eagerly begin to gather."
    "Echo leads you to her chambers where she slips into her ceremonial regalia while you head outside and overlook A'nai."
    scene ch6sc10_045 with Dissolve(1.5)
    play music drums_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "The tribe has begun to gather beneath you, you notice the sound of drums filling the city with anticipation."
    mct "Damn... what a feeling."
    scene ceremony_ani4 with dissolve
    "The crowd of women outside begins chanting rhythmically, while Echo exit her chambers, overlooking the crowd."
    "You can’t quite make out the exact words but the chant and steady rhythm is enough to fill the entire village."
    mc "Woah… I’ve never felt anything like this… Echo-"
    ec "Life-changing, isn’t it?"
    ec "They’re chanting for you, for their future."
    "You feel a sense of great importance wash over you, the fate of an entire people now rests on you."
    ec "Let's greet them, as A'khan and A'nu."
    scene ceremony_ani1 with dissolve
    $ renpy.pause(20.7, hard=True)
    scene ch6sc10_045 with dissolve
    $ renpy.pause(0.5)
    "After about 15 minutes the chanting subsides."
    "The crowd of women stand in silence, looking upon you and Echo."
    scene ch6sc10_046 with dissolve
    ec "{b}Daughters of A’nai!{/b} Tonight is a night we’ve all been eager for."
    ec "Tonight we have been reunited as one tribe, tonight families and friends have reconnected."
    scene ch6sc10_047 with dissolve
    ec "Tonight we have gathered in honor of {b}[mc]{/b}, the man whom we’ve all grown to respect and love."
    "{b}The crowd cheer eagerly.{/b}"
    scene ch6sc10_048 with dissolve
    ec "The man who has conquered the trials of our ancestors, who has succeeded as champion of our goddesses."
    "{b}The crowd cheer eagerly.{/b}"
    ec "A few weeks ago he was but an outsider, who miraculously found himself within our precious A’nai.."
    scene ch6sc10_046 with dissolve
    ec "Now, he stands before you, a great hunter… an even greater man, as your leader, your {b}A’khan{/b}!"
    with vpunch
    "{b}The crowd cheer excitedly{/b}."

    if leadership >= 20:
        ec "[mc] has displayed remarkable traits of leadership during his time at A'nai and Arugoh!"
        ec "He will lead us into a future where we're loved, taken care of and protected!"
        "{b}The crowd cheer excitedly{/b}."

    else:
        pass

    scene ch6sc10_047 with dissolve
    ec "Just an hour ago, he restored our connection to the goddesses, by creating a shrine right in our midst."
    ec "High-Priestess Sivir and High-Priestess Marah have both confirmed it, they’ve felt the connection restored."
    "{b}The crowd cheer excitedly.{/b}"
    scene ch6sc10_048 with dissolve
    ec "Tonight we celebrate [mc], his ascension as A’khan and the future of A’nai!"
    ec "{b}Eat! Drink! Dance! Follow your hearts!{/b} [mc] will now speak to all of you and then we will begin the {b}Ceremony of Khans!{/b}"
    "{b}The crowd cheer happily.{/b}"
    scene ch6sc10_049 with dissolve
    ec "They’re all yours."
    ec "Go on, speak to them… they long to hear from you."
    ec "I’ll await you in my chambers."
    "You feel Echo gently squeeze your bicep before she retires to her chambers."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_050 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "{b}Daughters of A’nai.{/b}"
    mc "I did not complete the trials of your ancestors on my own, I had help from several of you."
    scene ch6sc10_051 with dissolve
    mc "It allowed me to see how you support each other, it showed how you respect the ways of the ancestors."
    mc "It showed me that you’re all women capable of greatness in each your own right."
    "{b}The crowd cheer happily.{/b}"
    scene ch6sc10_050 with dissolve
    mc "I have met each of your goddesses, and they each saw something in me that made them put their faith in me."
    mc "A couple of weeks ago I didn’t know of your existence, and now… now I find myself caring about you."
    scene ch6sc10_051 with dissolve
    mc "About your culture, about your past… and most of all… about your future."
    mc "A future which we’ll all contribute to, a future where each and every one of you needn’t fear the past repeating."
    "{b}The crowd cheer happily.{/b}"
    scene ch6sc10_050 with dissolve
    mc "As your A’khan, this I promise you."
    scene ch6sc10_052 with dissolve
    mc "Should any outsider dare harm a single one of us, no… even just think about harming one of us-"
    with vpunch
    mc "We will show them no mercy! {b}You hear me!?{/b}"
    with vpunch
    "{size=+10}{b}The crowd cheer excitedly!{/b}{/size}"
    scene ch6sc10_053 with dissolve
    with vpunch
    mc "If they do… they will not only have to deal with the fiercest women I know."
    mc "They will face my wrath."

    if eye_beam == True:
        scene ch6sc10_054 with dissolve
        with vpunch
        mc "The wrath of {b}YOUR A’KHAN!{/b}"
        "You release your eye beams far into the sky."
        "The crowd becomes silent as you display your devastating power before their eyes."

    else:
        scene ch6sc10_055 with dissolve
        with vpunch
        mc "The wrath of {b}YOUR A’KHAN!{/b}"
        "You release some of your mana and manipulate it to swirl around your body."
        "The crowd becomes silent as you display your power before their eyes."

    scene ceremony_ani4 with dissolve
    "After a momentarily silence, the women below you begin chanting once more."
    "This time however, you can clearly hear them, as they only chant one word."
    "[mc]... [mc]... [mc]... [mc]... [mc]..."
    scene ch6sc10_051 with dissolve
    mc "Think no more of the past…"
    scene ch6sc10_050 with dissolve
    mc "Look toward {b}our{/b} future."
    mc "{b}Your A’nu and A’khan wills it so{/b}. Drink, eat, rejoice, dance, cheer, and celebrate until the morning rays bathe your skin."
    with vpunch
    "{size=+10}{b}The crowd of women cheer loudly in agreement.{/b}{/size}"
    scene ch6sc10_056 with dissolve
    mct "What a feeling…"
    mct "I’m starting to see the appeal of leadership."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "You head inside Echo’s chamber with the chanting and cheering of the crowd in the background."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_057 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    "Upon entering her chamber, you feel a strong tension in the air."
    "An allure unlike anything you’ve felt prior."
    scene ch6sc10_058 with dissolve
    "Your eyes do not waver from the goddess standing near her bed."
    "Your… A'nu."
    "You notice she has already let her hair down and removed her gilded crown."
    scene ch6sc10_059 with dissolve
    ec "Alone at last…"
    ec "Now that you've become the A'khan, it's time for your crowning ceremony."
    ec "Lay down on the bed, naked... and we'll begin."


    if ec_relationship == True:
        ec "Will you help me with my dress, [mc]? I fear… it's much too difficult for me to remove by myself."
        "You chuckle at her obvious playfulness."
        scene ch6sc10_060 with dissolve
        mc "Mmh… I’ve missed you."
        "You begin to undo her dress right below her breast."
        scene ch6sc10_061 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        ec "I’ve missed you too, [mc]."
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        ec "*Moans softly* By the goddess… your touch is magical."
        ec "Please… get me out of this dress."
        scene ch6sc10_062 with dissolve
        "As you pull the last string from her waist, her dress slips right off her incredible body."
        ec "Aahh… it feels so good to be near you again, my love."
        mc "Mhm, it does."
        scene ch6sc10_063 with dissolve
        ec "*Whispers sensually* {size=-10}{b}Take me to bed.{/b}{/size}"
        mc "As you desire, my Queen."
        ec "*Giggles* I like it when you call me that."
        scene ch6sc10_064 with dissolve
        ec "Ready to begin your crowning ceremony, my A’khan?"
        mc "I wouldn’t want to start my ceremony off with anyone but you, Echo."
        mc "My A’nu, my Queen, my Goddess."
        scene ch6sc10_069 with dissolve
        "Hearing your titles for her she eagerly climbs on top of you, guiding you between her dripping lips with her hand."
        ec "Are you ready baby? Are you ready to mate with your Queen?"
        mc "Mhm… I’m ready."
        scene ec_lewd50 with dissolve
        ec "*Moans* I feel you- Mmh… I finally feel you again. Aahh…"
        $ renpy.pause()
        mc "Nnghh… I love how soaking wet you already are for me… Mmh… and just as tight as I remember."
        ec "I love you… [mc], I love you!"
        mc "And I love you… Mmh…"
        "As she rides you, you feel her fidgeting with your wrists behind your back, then you feel her tightening a rope."
        mc "Echo, what are you-"
        scene ec_lewd51 with dissolve
        $ renpy.pause()
        ec "*Moans* {b}AhhH!{/b} You’re so deep! Mmh!"
        ec "This is how I want you tonight- Mmghh! Unable to stop our breeding! Aiiyhh!"
        mc "{b}Fuck! Mmmgh!{/b} I can’t hold it back much longer, not with how good your little pussy feels sucking me!"
        with vpunch
        ec "My flower will suck you dry! Mmh! Let it happen! {b}Let me satisfy you and breed you!{/b}"
        with vpunch
        ec "{b}I feel you pulsating my love! AhHh!! I’m going to bloom with you!! Fill me with your seed!!{/b}"
        scene ch6sc10_070 with dissolve
        with vpunch
        "Unable to stop her riding, she keeps pushing you deeper and deeper while you release your cum."
        with vpunch
        ec "{b}Give it to me!{/b} Mmh! Let me bloom with your seed!! {b}Ah-AhhH!{/b}"
        scene ch6sc10_071 with dissolve
        with vpunch
        ec "{b}[mc]!!! Baby!! Aiiyhh!! Yes! I love this!! I love feeling you this deep!!{/b}"
        with vpunch
        "Her lustful moans continue to echo throughout her chambers as you send another full load deep inside her."
        ec "*Giggles happily* Ahh… so much just for me? Mmgh… you truly know what I desire."
        scene ch6sc10_069 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        mc "Fuck… that was incredible… being tied up added another level of pleasure to this."
        ec "*Panting softly* Mhm… it was kind of naughty, I’d definitely like to tie you up again some time."
        scene ch6sc10_066 with dissolve
        ec "For now, I just gotta make sure you’re properly tied up."
        mc "*Chuckles* You want to keep me tied up?"
        ec "Mhm-hm, it is important for your ceremony."
        scene ch6sc10_067 with dissolve
        ec "Now that we have finished our mating as A’nu and A’khan…"
        ec "The tribe will now visit you, one by one and reveal themselves to you as nature intended it."
        ec "If you desire them, accept them and they will breed you tonight, as you become one with your women-"
        scene ch6sc10_066 with dissolve
        ec "You will form an everlasting bond, unbreakable… unwavering… unyielding."
        mc "Sure but why the need to keep me tied up-"
        ec "Shh, my love. You have the rest of your life to take them as you please."
        "You feel Echo tightening the rope around your hands, tying them firmly."
        ec "Tonight is not about that, it's not about you claiming them or taking them."
        scene ch6sc10_067 with dissolve
        ec "They’re already yours, tonight is about them."
        ec "About them being accepted by you, about their desire to breed you, about their contribution to the future of our people."
        ec "It’s about them, choosing to give themselves to you, willingly. Not bound by duty."
        ec "There we go… now you’re ready to be mated."
        scene ch6sc10_066 with dissolve
        ec "Remember, you have to accept each woman. If you do not desire them tonight, you’re free to deny them."
        ec "You can always mate with them another time if your desire for them changes."
        mc "Got it. *Chuckles* This is wild…"
        scene ch6sc10_068 with dissolve
        ec "This is what it means to be {b}A’khan{/b}, to have all your women desiring you, every waking moment of their lives."
        ec "I believe they have begun forming a line at the stairs, I will send them to you one by one my love."
        mc "Mhm… I love you, you know that?"
        scene ch6sc10_072 with dissolve
        ec "Uh-Huh… I do, and I love you, [mc]."
        ec "I’ve never known love like this, but it fills every moment of every day."
        ec "I cannot wait for my future with you."
        scene ch6sc10_068 with dissolve
        ec "*Sighs* But for tonight, my time with you is up… as much as I hate that I must leave you."
        ec "It is my duty to allow this… to allow our people the chance to satisfy you and receive your seed."
        mc "Don’t worry, I get it. It’s not what you wish for but it’s the way of our people."
        scene ch6sc10_072 with dissolve
        ec "Mhm-hm, enjoy the ceremony my love, you have earned it. I will see you in the morning."
        ec "I will serve you breakfast in bed, I imagine you will be famished after completing the ceremony. *Giggles softly*"

        if harem_path == True:
            scene ch6sc10_068 with dissolve
            ec "Enjoy your harem night, my love."
            ec "I have a feeling it'll be one that will burn itself into your memory through desire."
            mc "Starting out my harem night with that ass of yours, was a foolproof way of making sure I'll remember it."

        else:
            pass


    else:

        scene ch6sc10_065 with dissolve
        mc "Echo…"
        ec "I know, as much as my heart desires you to feel the same as I do, you don’t…"
        ec "I would never want you to be with me out of obligation, so I will not partake in your ceremony tonight."
        scene ch6sc10_064 with dissolve
        ec "The tribe will now visit you, one by one and reveal themselves to you as nature intended it."
        ec "If you desire them, accept them and they will breed you tonight, as you become one with your women-"
        scene ch6sc10_066 with dissolve
        ec "You will form an everlasting bond, unbreakable… unwavering… unyielding."
        mc "What are you-"
        ec "Shh, my love. You have the rest of your life to take them as you please."
        "You feel Echo wrapping rope around your hands, tying them firmly."
        ec "Tonight is not about that, it's not about you claiming them or taking them."
        scene ch6sc10_067 with dissolve
        ec "They’re already yours, tonight is about them."
        ec "About them being accepted by you, about their desire to breed you, about their contribution to the future of our people."
        ec "It’s about them, choosing to give themselves to you, willingly. Not bound by duty."
        ec "There we go… now you’re ready to be mated."
        scene ch6sc10_066 with dissolve
        ec "Remember, you have to accept each woman. If you do not desire them tonight, you’re free to deny them."
        ec "You can always mate with them another time if your desire for them changes."
        mc "Got it. *Chuckles* This is wild…"
        scene ch6sc10_068 with dissolve
        ec "This is what it means to be A’khan, to have all your women desiring you every waking moment of their lives."
        ec "I believe they have begun forming a line at the stairs, I will send them to you one by one my love."
        mc "Sounds good."


    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Echo slips back into her dress and leaves her chambers… while you remain tied up, waiting in anticipation."
    scene ch6sc10_073 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "This is crazy… but at least she has gotten a comfortable bed, they must’ve transported it from Arugoh."
    mct "Probably as a gift to make amends."
    scene ch6sc10_074 with dissolve
    "The first woman to enter the chamber is Riven."
    "She smiles warmly at you before she proceed to undress."
    scene ch6sc10_075 with dissolve
    "Standing before you, naked as nature intended… she gazes upon you as you lay naked before her eyes."
    "You notice how she teases her hardened nipple between her fingers as she enjoys your gaze."
    scene ch6sc10_076 with dissolve
    riv "Will you… accept me? My A’khan."
    riv "Will you allow me to become one with you and claim your seed?"

    if riv_relationship == True:
        scene ch6sc10_075 with dissolve
        mc "We both know I have no desire to decline you."
        mc "You’re a woman who I can’t resist… a woman who cause all my desires to reach new heights."
        scene ch6sc10_076 with dissolve
        riv "Mhmm… I am most pleased with your answer."
        riv "I've been thinking about tonight... about you... since sunrise."
        scene ch6sc10_077 with dissolve
        riv "Your words fill me with joy, your naked body fills me with desire… I am a blessed woman to be accepted by you."
        riv "Please know… I’ve been craving you deeply since last time we were as one…"
        riv "I will not be able to stop myself once we begin… not until your warm seed fills every inch of my flower."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_078 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        mc "I wouldn’t want you to stop, I remember how juicy your flower is… I’ve been eager to feel it around me again."
        riv "Feel it you shall, just like I will savor every inch of your beautiful, hardened spear."
        riv "It’s a good thing we were at opposite ends of the caravan… otherwise I would’ve pulled you behind a tree and sucked you."
        scene ch6sc10_079 with dissolve
        riv "Tonight I will not claim your seed with my mouth… tonight we are breeding. I want your seed deep within my flower, okay?"
        mc "Mhh… I can’t stop you, can I?"
        riv "*Snickers lightly* No, you cannot deny me this pleasure any longer… with your hands tied you’re powerless to stop our breeding."
        riv "I desire to ride you as if I have been possessed by Malanthe herself! {b}Mmghh!{/b}"
        scene riv_lewd17 with dissolve
        $ renpy.pause()
        "Just as she said, as soon as your cock begins sliding inside her wet pussy, she can’t contain herself and begins riding you wildly."
        mc "{b}Fuck! Mmgh!{/b} You really are possessed tonight- Ahh! Fuck that’s good."
        with vpunch
        riv "*Moans loudly* Do you feel this?! Do you feel how tight my flower has become for you? {b}AHHh! AhH!!{/b}"
        with vpunch
        riv "{b}[mc]!! I’m cumming!! AiiiyhH!! YES!! Make me cum all over you!!{/b}"
        scene riv_lewd18 with dissolve
        $ renpy.pause()
        with vpunch
        riv "{b}I CAN’T STOP!! I REFUSE TO STOP!! AHHH!!{/b}"
        riv "*Moans* I love how deep you are inside of me! {b}AHH!!{/b} My flower can’t take it!! {b}Cum with me!!{/b}"
        with vpunch
        mc "Mmgh! Keep riding me like this and you’ll get what you desire- {b}AhhH!{/b}"
        with vpunch
        riv "Yes! I feel you pulsating! Give yourself to me!! {b}Let me breed you! AhhH!!{/b} My A’khan!! {b}I’m cumming again!!{/b}"
        scene ch6sc10_080 with dissolve
        with vpunch
        "Feeling Riven’s already tight and soaking wet pussy reaching another orgasm, sends you over the edge as well."
        with vpunch
        riv "*Orgasmic moan* Baby- {b}Ahhh!! Yes!!{/b} Fill me- {b}Aiiiyhh!{/b} Your spear and seed is melting my {b}miiiiiind-AiiiyhhH{/b}!"
        with vpunch
        mc "Mmh!! Riven- Fuck!! Your pussy is too good- Mmmgh!"
        scene ch6sc10_081 with dissolve
        riv "*Whimpers while kissing* Mmh-Mmh-nngh!! So good… so unbelievably good…"
        mc "As incredible as always… mmh."
        riv "*Shares saliva* Thank you… for allowing me to follow my desire and breed you fully."
        "Riven gently sucks your tongue while enjoying your cum inside her before she finally gets up."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_082 with Dissolve(1.5)
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        riv "Oh no… *Gasps* your seed is already beginning to leak?!"
        riv "I’m sorry my A’khan, but I must find a place to lie down… I want it inside me as long as possible."
        mc "Go on, enjoy my seed."
        scene black with Dissolve(1.5)
        "Riven scurries off while holding a hand to her little flower, trying to keep your cum inside of her."

    else:
        scene ch6sc10_075 with dissolve
        mc "I do not desire you tonight, Riven, beautiful as you are."
        scene ch6sc10_076 with dissolve
        riv "I understand, my A’khan. I will send the next one to you."
        scene black with Dissolve(1.5)


    scene ss1 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    scene ch6sc10_083 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    da "Any word on the missing adventurers? Any news from the village of Loboten?"
    sy "Nope! Nuh-uh! Not one bit!"
    sy "It’s been a couple of days at this point, you think they gave up on the quest?"
    da "It’s hard to say-"
    scene ch6sc10_084 with dissolve
    el "Hey guys! Those adventurers still haven’t returned?"
    sy "Eliza! Hi!"
    da "I’m afraid they haven’t, no."
    scene ch6sc10_085 with dissolve
    sy "But this is perfect! I just had a great idea!"
    sy "You’re a total badass Eliza, you could easily find them!"
    scene ch6sc10_086 with dissolve
    el "About that… I was going to see if Borri and myself could find them."
    scene ch6sc10_087 with dissolve
    el "*Sighs* But… I no longer think that’s an option."
    sy "What? Why not? You’d be perfect-"
    scene ch6sc10_086 with dissolve
    el "I feel my hunger increasing…"
    el "It’s not unbearable as of yet, but I feel it…"
    el "I can’t… I can’t risk being out there and have it overwhelm me."
    scene ch6sc10_087 with dissolve
    el "I could hurt Borri… or the very adventurer’s we’re looking for… or someone innocent."
    el "It’s been about a week since I drank my last vial of blood from [mc]."
    scene ch6sc10_086 with dissolve
    el "I-... I don’t know what to do? I don’t trust myself…"
    el "I may have been purified but there's no telling what would happen…"
    scene ch6sc10_088 with dissolve
    da "I was afraid this would be the case…"
    da "This mission he is on is not a simple one, it never is when politics are involved."
    da "Which is why I have prepared something for you."
    scene ch6sc10_089 with dissolve
    el "You have? What is it?"
    da "Follow me, we’re heading downstairs."
    da "Sylph, take care of the front desk."
    sy "Aiyh-Aiyh Cap’n!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_090 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    da "Now, I want you to keep an open mind…"
    el "An open mind? Dalen what are you talking about-"
    scene ch6sc10_091 with dissolve
    with vpunch
    el "A Coffin?!"
    el "Dalen, you’re not serious?! If you think this is funny because I’m a vampire…"
    with vpunch
    el "There’s absolutely no way I’m getting into some dusty old coffin! No way! {b}Nuh-uh!{/b}"
    scene ch6sc10_092 with dissolve
    da "First of all, I’ve had Sylph clean it for you, it isn’t dusty."
    da "Secondly, one of two things will happen next, you will either give in to the bloodlust and hurt someone."
    da "Or you will resist the urge to feed, which means you will begin to desiccate and mummify."
    scene ch6sc10_091 with dissolve
    el "Yes-... I know! But… it’s a coffin."
    el "{b}A COFFIN!!{/b}"
    scene ch6sc10_092 with dissolve
    da "You’ll get over it, we both know that you feeding is not an option without [mc]."
    da "Which is why I have prepared this for a situation like this."
    da "Now, the coffin itself is nowhere near powerful enough to hold you, but Sylph will enchant it to reinforce it."
    da "As soon as [mc] is back, you’ll be released."
    scene ch6sc10_091 with dissolve
    el "I don’t know… I understand what you’re saying and it makes sense…"
    el "But the thought of being trapped in a coffin, left to mummify… ew!"
    scene ch6sc10_092 with dissolve
    da "*Sighs* Get in the damn coffin before I throw you in myself."
    scene ch6sc10_093 with dissolve
    el "Promise me that you will come get me as soon as [mc] returns."
    da "I’ll do you one better, I’ll have him come get you himself."
    el "O-Okay… I’d like that very much."
    scene ch6sc10_094 with dissolve
    el "*Exhales deeply* You could’ve at least put a pillow in here or something…"
    da "I’ll remember that for next time."
    scene ch6sc10_095 with dissolve
    with vpunch
    el "{b}NEXT TIME?!{/b}"
    scene ch6sc10_096 with dissolve
    with vpunch
    el "Dalen I swear by all the gods! What do you mean next time?!"
    scene ch6sc10_097 with dissolve
    with vpunch
    el "*Muffled* {b}DALEN!!{/b}"
    da "Conserve your energy, the more you spend, the faster you’ll mummify."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    #play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch6sc10_073 with Dissolve(2.5)
    play music explore_2 fadein 1.0
    $ renpy.pause(0.5)
    "You notice something disturb the curtains."
    mc "Enter."
    scene ch6sc10_098 with dissolve
    "To your surprise, the woman who enters is none other than Kisha."
    mc "Kisha… you don’t look too pleased? And what's with the knife?"
    ks "..."
    scene ch6sc10_099 with dissolve
    ks "Do you accept me? My A’khan."
    "You can tell she is swallowing her pride as she asks you."
    scene major_choice with Dissolve(1.5)
    ####Choice####
    menu:
        "I accept you, Kisha. ({color=#ff8cdd}Romance Lock-in{/color})":
            scene ch6sc10_098 with dissolve
            mc "I accept you. You’re one of the strongest women of our tribe, and you’re my Head-Huntress."
            scene ch6sc10_100 with dissolve
            $ ks_trust += 5
            mc "I gained great respect for you as a fighter during our sparring, and…"
            mc "I desire you. I’ve desired you since our sparring."
            $ ks_relationship = True
            "Hearing that your desire is matching her own for you, pleases her. Kisha's trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            "Kisha brings her blade to the straps of her top, with one swift cut she opens it and it falls to the floor."
            scene ch6sc10_101 with dissolve
            #play music explore_1 fadein 1.0
            stop music fadeout 1.0
            ks "..."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            $ ks_path = True
            "She then moves the blade around her back and you see it slide up between her pantie and her hip, once more she cuts the fabric."
            scene ch6sc10_102 with dissolve
            ks "I too have felt our attraction grow, despite not having spent any time together since our one on one match."
            ks "My attraction to you… continues to grow, I find myself thinking about you when I should be training…"
            scene ch6sc10_103 with dissolve
            ks "I won’t be needing this anymore…"
            mc "Five hells… you brought the dagger just to cut yourself free from your garments?"
            scene ch6sc10_104 with dissolve
            ks "Mhm, I did."
            ks "Are you not pleased with finally seeing my body?"
            scene ch6sc10_105 with dissolve
            mc "I am… if anything it was quite a turn on, seeing how dedicated you were to revealing yourself to me."
            scene ch6sc10_104 with dissolve
            ks "You’re about to find out just how dedicated I am… to you."
            scene ch6sc10_105 with dissolve
            mc "Then what was with the look when you first entered?"
            scene ch6sc10_106 with dissolve
            ks "How could I not be upset? I always knew our first time would be here, during your crowning ceremony."
            ks "*Sighs* But after sparring with you… a part of me hoped we’d have another match, which-..."
            scene ch6sc10_107 with dissolve
            ks "Which led to your spear finding its way inside my flower… no matter how wrong it would be… neither of us would stop."
            ks "We would be exhausted and drenched in sweat from our match… but our adrenaline would keep us mating for hours."
            mct "*Chuckles* Sounds like she's been having fantasies about us while I was gone."
            scene ch6sc10_108 with dissolve
            ks "I am pleased to be here with you tonight, that we finally get to breed."
            ks "I was simply annoyed that my… desire did not come true."
            ks "I want to hear you say it."
            scene ch6sc10_107 with dissolve
            ks "Tell me that you desire me…"
            ks "Tell me how my naked body on top of you is what has stirred your spear to become this hard."
            scene ch6sc10_108 with dissolve
            mc "Fuck Kisha… every single inch of my body is on fire right now…"
            mc "Ignited by having you on top of me."
            ks "Mmmh… I’m going to breed you well, my A’khan."
            scene ks_lewd1 with dissolve
            $ renpy.pause()
            ks "*Moans* {b}Ah-AhH!{/b} Oh I see… I see why everyone is so obsessed with you…"
            ks "And your- Aiiyhh... heroic spear- {b}Ahh!{/b}"
            mc "Fhhh… you’re tight! Hnngh… so fucking tight…"
            ks "Do you like my flower?"
            ks "How my wet lips sucks onto your shaft? How tight I become the deeper you penetrate me?"
            mc "Y-Yeah… fuck… you feel incredible… Mmh… not to mention the view you’re giving me."
            ks "*Moans* It is a view you will have to- Mmmh… get used to, this might be our first breeding- Ahh…"
            with vpunch
            ks "But it won’t be our laaaaast- {b}Aiiyh! OH!! OH- I’m going to- AiiiyHH!{/b}"
            with vpunch
            mc "Me too! Mmh! Kisha prepare yourself! {b}AhH!{/b}"
            with vpunch
            ks "That’s it!! {size=+3}{b}Spear me!{/size} {size=+6}Hunt me!!{/size} {size=+9}AhhH!!{/size} {size=+12}Breed me!! AH!!{/b}{/size}"
            scene ch6sc10_109 with dissolve
            with vpunch
            ks "{b}By Gaia’s will [mc]!! AHhH!! I feel your seed!! Mmghh!{/b} My flower has never felt anything it’s equal!"
            mc "{b}Mmh!{/b} Your tight little pussy is divine!"
            scene ch6sc10_110 with dissolve
            ks "*Sucks eagerly* {b}Mmgh! Nnghh! Oh my! MmghH!{/b} Your seed mixed with my nectar has quite the flavor!"
            "She eagerly licks and sucks your cock until she has cleaned every inch of it."
            mc "Mmh… you truly live up to your title as Head-Huntress."
            ks "*Sucks intimately* Mmhh... I intend to hunt you often, my handsome A'khan."
            scene ch6sc10_111 with Dissolve(1.5)
            mc "Mmmh... I like seeing my cum drip out of that juicy pussy of yours."
            ks "You’re such a bold man…"
            ks "Next time I won’t settle for just one filling."
            scene black with Dissolve(1.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)
            "Kisha takes her leave, as she exits, you notice her smiling, a rare occurrence."

        "Not interested. (Neutral)":
            scene ch6sc10_098 with dissolve
            mc "I accept you as a strong member of the tribe, my Head-Huntress, but I am not interested in Mating with you tonight."
            ks "..."
            scene ch6sc10_099 with dissolve
            ks "*Nods* Very well then, I will do my best as your Head-Huntress then."
            scene black with Dissolve(1.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)

    scene ch6sc10_073 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Hmm, I wonder who’s next? So far it’s been high-ranking women only, do they have priority?"
    mc "I suppose a hierarchy like that would make sense."
    mc "If that’s the case, I’m guessing Sivir, Marah or Sakari."
    "You won’t be waiting long, as you notice the curtains begin to shuffle."
    scene ch6sc10_112 with dissolve
    mc "Now there’s a beauty I haven’t seen in a while."
    mc "I was thinking you might’ve been the one to make her entrance next."
    scene ch6sc10_113 with dissolve
    sk "Mmh-hm, thank you for the sweet compliment, my A’khan."
    sk "Will you accept me?"
    sk "As your mate, your lover, your woman, your mistress of Malanthe?"
    scene major_choice with Dissolve(1.5)
    ####Choice####
    menu:
        "I accept you, Sakari.({color=#ff8cdd}Romance Lock-in{/color})":
            scene ch6sc10_113 with dissolve
            mc "Sakari, I accept you as mine."
            scene ch6sc10_114 with dissolve
            sk "My heart flutters at the thought… I am most pleased with your choice."
            sk "Seeing you like this… naked… raw… bound… it greatly stirs my desire… which makes my decision difficult."
            scene ch6sc10_115 with dissolve
            mc "Your decision?"
            $ sk_path = True
            sk "*Whispers* {size=-10}{b}Mhm-hm, I’ve decided you won’t be enjoying me tonight.{/b}{/size}"
            sk "*Whispers* {size=-10}{b}I won’t wrap my big juicy lips around your incredibly alluring spear…{/b}{/size}"
            sk "*Whispers* {size=-10}{b}I won’t be mounting you, allowing you to slide inside the warmth of my dripping flower…{/b}{/size}"
            scene ch6sc10_116 with dissolve
            sk "But I will give you this."
            $ sk_relationship = True
            "You feel her big, soft lips merge with yours, in a gentle and intimate kiss."
            sk "Mmmh…"
            "While her lips gently rests on yours, barely moving, you feel the warmth of her breasts resting on your chest."
            scene ch6sc10_115 with dissolve
            sk "My first kiss with a man… that is what I have given you tonight, [mc]."
            mc "It felt… incredibly intimate."
            sk "Yes, yes it did…"
            sk "I know you long for more, as do I… believe me. But we will not engage in breeding tonight."
            scene ch6sc10_114 with dissolve
            mc "No pressure, but I gotta admit, I’ve been looking forward to finally claiming you, fully."
            sk "It warms me to my core, hearing you say such things… which is exactly why I desire to wait."
            scene ch6sc10_113 with dissolve
            sk "I will not be pleased with just a quick breeding… no, I will not be pleased with that at all."
            sk "I want you to claim me in a moment of privacy, between man and woman, between Mistress and A’khan."
            scene ch6sc10_114 with dissolve
            sk "Where we won’t be disturbed, where we won’t have to stop breeding, mating, fucking, loving… Mmh."
            mc "Five hells… I can’t believe I’m saying this but… now I’m excited we’re choosing to wait."
            scene ch6sc10_115 with dissolve
            sk "Good, I had a feeling you would match my desire."
            sk "Trust me, I’ll be worth the wait."
            scene ch6sc10_116 with dissolve
            sk "Mmmh… just once more for my own pleasure."
            "Sakari rests her lips once more against yours, she keeps them pressed gently against you for over a minute."
            $ sk_trust += 5
            "Sakari appears to have grown feelings for you, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch6sc10_115 with dissolve
            sk "Goodnight, [mc]."
            mc "Goodnight, Sakari."
            scene black with Dissolve(2.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)

        "Not interested. (Neutral)":
            scene ch6sc10_113 with dissolve
            mc "I accept you as an important member of the tribe."
            mc "You’re Mistress of Malanthe, and it's a role I wish for you to continue fulfilling."
            mc "But I am not interested in Mating with you tonight."
            scene ch6sc10_114 with dissolve
            sk "..."
            sk "*Nods* Very well then, I will do my best as your Mistress of Malanthe then."
            sk "You will not find my servitude lacking, my maidens will be offering their lust to Malanthe even more now."
            scene ch6sc10_113 with dissolve
            $ sk_path = False
            sk "Enjoy the rest of your ceremony, my A’khan… you have a great many women lined up beneath the temple."
            scene black with Dissolve(2.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)


    scene ss8 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc13_216 with Dissolve(2.5)
    play music intro_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch5sc13_217 with dissolve
    gd "Lord Admiral, we’ve received word from Luxenford."
    scene ch5sc13_218 with dissolve
    di "Go on."
    scene ch5sc13_217 with dissolve
    gd "They wish to know the status of the Ambassador and our progress here at Looter’s Bay."
    scene ch5sc13_218 with dissolve
    di "Send a raven, detailing our progress here. Looter’s Bay is under King Bennen’s jurisdiction now."
    di "And report that the Ambassador has been secured, safe and sound."
    scene ch5sc13_217 with dissolve
    gd "Lord Admiral-"
    scene ch5sc13_218 with dissolve
    with vpunch
    di "{b}Do it!{/b}"
    scene ch5sc13_219 with dissolve
    gd "As you command, Lord Admiral."
    gd "A raven will be sent at first light."
    scene ch5sc13_216 with dissolve
    di "..."
    dit "Why… why did I do that?"
    dit "I’ve only met him once… yet, I believe he will succeed in bringing back Ambassador Orianna safely? "
    dit "*Sighs* Falsifying a report under royal command… he better prove my faith in him to have been well placed."
    dit "*Exhales* [mc]..."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss1 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc13_220 with Dissolve(2.5)
    play music tavern_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    fy "I’ve become quite the dueler, fencer extraordinaire is what they call me at the tavern."
    scene ch5sc13_221 with dissolve
    al "Flynn… nobody calls you that."
    scene ch5sc13_220 with dissolve
    fy "They will."
    scene ch5sc13_221 with dissolve
    al "*Sighs* Right…"
    scene ch5sc13_222 with dissolve
    al "I’m glad your training is going well, I wasn’t sure how you’d take to it."
    scene ch5sc13_223 with dissolve
    fy "Alice, please… you know I’m a man of many talents."
    fy "I simply can’t be boxed in."
    scene ch5sc13_222 with dissolve
    al "Flynn, you need to take this seriously, okay?"
    al "It’s important we learn how to defend ourselves, both in general but especially because Taron is up to no good."
    scene ch5sc13_223 with dissolve
    fy "I am taking it seriously, I show up for all of Dalen’s lessons and I even beat Milton last time!"
    fy "Trust me, that little bugger is quick on his feet!"
    scene ch5sc13_224 with dissolve
    al "I suppose that’s good…"
    al "Eliza has been drilling me and the girls through rigorous training as well."
    scene ch5sc13_222 with dissolve
    al "I’m not particularly fond of combat either, but… it feels good knowing I will be able to help [mc] if he needs me."
    scene ch5sc13_223 with dissolve
    fy "Oh? I knew it! You’re not training just to defend yourself, you’re really doing it to defend him."
    al "..."
    fy "You’re such a little sweetheart, Alice."
    scene ch5sc13_222 with dissolve
    al "I’m-..."
    al "*Sighs* So what if I’m doing it for [mc], I want to participate in his life, be of use to him."
    scene ch5sc13_223 with dissolve
    fy "There’s nothing wrong with that being your motivation, Alice."
    fy "You know me, I was just poking fun at your reluctance to say it out loud."
    scene ch5sc13_222 with dissolve
    al "I know… anyways, didn’t you say Sabrina was going to meet us here?"
    scene ch5sc13_224 with dissolve
    al "Ah! There she is."
    scene ch5sc13_225 with dissolve
    al "Sabrina, hi!"
    fy "Hey sis! Finally, must’ve been a long day at the bakery?"
    scene ch5sc13_226 with dissolve
    sa "Hey guys, yeah… work keeps me busy, but I honestly like it."
    scene ch5sc13_228 with dissolve
    sa "The old lady I’m working for is really sweet and she's great at teaching me the ins and outs of baking."
    scene ch5sc13_229 with dissolve
    al "Well! You-... you better bring me some cupcakes soon, okay?! I haven’t had any in forever now!"
    scene ch5sc13_226 with dissolve
    sa "*Giggles* My bad, my bad! I’m actually working on a recipe for muffins, I’ll bring you some once I get it just right."
    al "Great! The cookies you gave [mc] were so yum-yum!"
    scene ch5sc13_227 with dissolve
    fy "Hold up! You… gave [mc] your cookies?!"
    fy "Sis! He’s our cousin! Have you no sham-"
    scene ch5sc13_228 with dissolve
    sa "Get your head out of the gutter, Flynn. Alice is talking about actual cookies I made."
    sa "Besides, it’s none of you business if I want to give my cookies to [mc]."
    sa "In fact… *Giggles* he can have {b}MY{/b} cookie whenever he wants."
    scene ch5sc13_229 with dissolve
    al "H-Hey!"
    al "Enough about giving cookies to [mc]! Weren’t we going to grab ales at the tavern!"
    scene ch5sc13_226 with dissolve
    sa "Sounds good to me! I can easily drink two full mugs after today's workload!"
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_073 with Dissolve(2.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "Let’s see who's next… according to my theory it should be Sivir or Marah?"
    scene ch6sc10_117 with dissolve
    "Your assumption is spot on as Sivir appears through the curtain."
    siv "Finally… Greetings, my love."
    scene ch6sc10_118 with dissolve
    mc "I had a feeling you would be next."
    scene ch6sc10_117 with dissolve
    siv "I’m not surprised. You're a man of great intuition after all."
    siv "Do you accept-"
    scene ch6sc10_119 with dissolve
    siv "*Giggles* Oh! Oh my… would you look at that."
    siv "How clumsy of me! I must’ve been so eager to see you that I didn’t notice I hadn’t properly tucked my breast away."
    mc "*Chuckles* No complaints here."
    scene ch6sc10_120 with dissolve
    siv "*Giggles* Oh? I guess I don’t mind leaving it out then… for your eyes only."
    siv "Where was I? Oh, that’s right… will you accept me, my love?"

    ####Choice####
    scene major_choice with Dissolve(1.5)
    ####Choice####
    menu:
        "I accept you, Sivir. ({color=#ff8cdd}Romance Lock-in{/color})":
            scene ch6sc10_119 with dissolve
            mc "I accept you, I’m powerless to do anything less, with your breast revealing itself to me."
            siv "*Giggles lightly* Good… I hoped it would stir your desire."
            $ siv_trust += 5
            "Sivir likes that seeing her breast delights you, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

            if siv_path == True:
                scene ch6sc10_120 with dissolve
                siv "I have been unable to walk properly all day since our incredible mating session last night…"
                siv "But if you think that means I will go easy on you tonight… you’d be wrong."
                scene ch6sc10_121 with dissolve
                siv "So wrong…"

            else:
                pass

            siv "*Unties strings* My body has been aching for you all day… walking side by side with you during the caravan…"
            siv "It was torture, my love… being so close to you, without being able to mate with you…"
            siv "I’ve never felt such torture."
            $ siv_relationship = True
            mc "Just like I’ve been hard all day… knowing what a lustful woman was right beside me."
            scene ch6sc10_122 with dissolve
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            $ siv_path = True
            siv "*Giggles lightly* Lustful woman huh? You’ve seen nothing yet, my sweet A’khan."
            siv "Oh? I see you’ve been tied down already? Good…"
            siv "That means I will able to breed you to my fullest desire, without you being able to stop me."
            scene ch6sc10_123 with dissolve
            siv "I’m going to love this… how I will enjoy having my way with you. *Snickers*"
            mct "She seems to enjoy the idea of roleplaying, let’s play into her desires then."
            mc "Sivir- no… you shouldn’t breed me like this, when I can’t touch you-"
            scene ch6sc10_124 with dissolve
            siv "Shhh, my love. Just… let it happen."
            "Sivir grasps your cock gently, and as she begins massaging you, she puts her palm over your mouth."
            siv "Mmmh… that’s my sweet boy. Let your High-Priestess take care of you… let me worship you."
            scene siv_lewd13 with dissolve
            $ renpy.pause()
            mc "*Muffled* Mmmh… MmgnhH…"
            siv "Such a good A’khan… there’s nothing you can do to stop me… just let it happen."
            siv "Let me satisfy your beautiful spear… let me make you feel good… it is my duty."
            siv "Mmmh… good, that’s good… you’re pulsating now, mmh… that means you’re ready for more."
            scene ch6sc10_125 with dissolve
            siv "Here, let me just get into a better position."
            "Sivir pushes herself onto your face, keeping you submerged between her juicy cheeks as she gently push herself against you."
            scene siv_lewd14 with dissolve
            $ renpy.pause()
            siv "*Moans* Aiiih-Ah… I knew it! I knew you were desperate to taste me! Ahhh…"
            siv "I’m only supposed to come in here and breed you, but… how can I deny us this pleasure?"
            mc "*Muffled licking* Nnghh… Mmgh! Mmmh…"
            with vpunch
            siv "You’re tongue is revealing everything I need to know- Mmgh! {b}Deeper{/b} my love! Penetrate my flower! {b}AiiyHH!!{/b}"
            with vpunch
            siv "I’m going to- {b}AhhH!!{/b} I’m going to bloom with your tongue inside me!! {b}Ah!! D-Don’t stop!!{/b}"
            scene ch6sc10_125 with dissolve
            with vpunch
            "Sivir's orgasmic moans fill the chamber as she overflows from being penetrated by your tongue."
            scene ch6sc10_126 with dissolve
            with vpunch
            "You drink her delicious juices as she keeps herself pressed against you."
            siv "*Panting* Goddess, I needed that. Now… now it’s time for you to impregnate me!"
            scene ch6sc10_127 with dissolve
            siv "We both know you can’t resist my mature pussy that rivals the tightness of the young huntresses."
            with vpunch
            siv "My pussy is what you crave, the feeling of my juices soaking your spear as we breed- {b}AhhH!{/b}"
            scene siv_lewd15 with dissolve
            $ renpy.pause()
            mc "Mmgh… Sivir- this isn’t… this isn’t right- AahhH… not like this…"
            siv "*Moans* My love! Ahh! Don’t you feel how right this is? How right we are for each other?"
            siv "Don’t you feel how my flower embraces your spear? How good I make you feel? Ahhh, let me have you."
            mc "Mmgh… we shouldn’t- Ahhh…"
            siv "Shh… your moans betray your words… {b}you want me{/b}… {b}you need me{/b}… just like I need you…"
            with vpunch
            siv "I’m not getting off you until you have filled me with your seed, until I’ve fully satisfied you! {b}AhhH!{/b}"
            with vpunch
            siv "{b}YES!! I FEEL YOU!! I FEEL YOU PULSATING INSIDE ME!! Aiiiyh!{/b}"
            with vpunch
            siv "Give yourself to me my sweet A’khan! Let me breed you fully! {b}AhhH! Cum with meeee!!!{/b}"
            with vpunch
            $ renpy.pause(0.5)
            with vpunch
            $ renpy.pause(0.5)
            scene ch6sc10_127 with dissolve
            "Her roleplay mixed with her loud moans and incredible tight feeling of her pussy forces you to pump her full."
            siv "*Panting* Such a fine young man… your young and potent seed will take hold within me soon, I feel it."
            siv "And when it does… Sivah will finally have a sibling, our child of love."
            scene ch6sc10_128 with dissolve
            siv "*Giggles happily* And when you impregnate me, you know what happens right?"
            siv "My large breasts which you already love to suck on, will fill with warm, delicious milk, just for you."
            mc "Mmh… I like the sound of that."
            scene ch6sc10_129 with dissolve
            siv "I better get back out there… I’ve already taken a lot longer than the others. *Giggles softly*"
            siv "We’ll continue our breeding another time… when there’s less of a crowd waiting their turn."
            scene ch6sc10_128 with dissolve
            siv "Goodnight my sweet love, my handsome and powerful A’khan."
            mc "Goodnight Sivir, it was a pleasure to be bred by you."
            scene ch6sc10_129 with dissolve
            siv "I’m still sitting with your godly spear buried inside of me, aren’t I?"
            mc "Mhm… you are."
            scene ch6sc10_130 with dissolve
            siv "Fine… I guess I can’t be greedy… at least not tonight."
            siv "But! You better fuck me again, real soon… otherwise I might lose my mind."
            siv "You may be the same age as Sivah, young enough to be my… son."
            siv "But you will become the father of my future children… you will become Sivah’s daddy."
            scene ch6sc10_131 with dissolve
            mc "*Chuckles* I look forward to it, and to getting to know Sivah better as well."
            $ siv_trust += 5
            siv "As do I… I know she is very intrigued by you, and she usually never cares about anything."
            siv "Goodnight my sweet boy... my love... my... one true god."
            "Sivir's feelings for you have taken root deep inside of her, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            mc "Goodnight gorgeous."
            scene black with Dissolve(2.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)

        "Reject Sivir. (Neutral)":
            scene ch6sc10_119 with dissolve
            $ siv_relationship = False
            mc "As gorgeous as you are, I do not desire you, at least not tonight."
            scene ch6sc10_117 with dissolve
            $ siv_path = False
            siv "*Sighs* How unfortunate… for my desire is overflowing for you."
            siv "But if both parties desires are not well matched… it would only sour the experience."
            siv "I wish you a wonderful night and ceremony, my A’khan."
            scene ch6sc10_118 with dissolve
            mc "Thank you, Sivir. I’m glad you’re taking my choice well."
            scene ch6sc10_117 with dissolve
            siv "Your will is absolute, no one can deny that. I will always be at the mercy of my A’khan’s will."
            scene black with Dissolve(2.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)

    "Sivir takes her leave, and as she closes the curtain you begin to ponder if it really is Marah who’s up next."
    scene ss52 with Dissolve(1.5)
    $ renpy.pause()
    scene ch5sc03_147 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch5sc03_148 with dissolve
    al_t "Pheew! A few ales with Flynn and Sabrina always turn into a gossip fest."
    al_t "But the warm baths here at the dormitories perks me right up."
    scene ch5sc03_149 with dissolve
    al_t "It really sounds like Sabrina has found her calling with this whole bakery thing."
    al_t "She’s always been rather outgoing, so it's no surprise she’s good at selling the goods either."
    scene ch5sc03_150 with dissolve
    al_t "It’ll be good for her to know some basics of cooking, she’s a woman after all."
    al_t "She can’t expect to find a man, let alone hold onto him if she can’t make him a proper meal."
    scene ch5sc03_151 with dissolve
    al_t "Great… now I sound like my mother of all people."
    al_t "I guess I do agree with some of what she taught me, she forced me to learn how to cook early."
    scene ch5sc03_152 with dissolve
    al_t "Hnnghh! Maybe… maybe I’ll make something for [mc] some time?"
    al_t "I know he’s a big foodie! I honestly don’t know how he keeps his… developed physique."
    scene ch5sc03_153 with dissolve
    al_t "With his appetite he should be rolling down the streets like a barrel of mead! *Giggles*"
    scene ch5sc03_154 with dissolve
    al_t "Maybe its a perk of him being a Nephilim? Or maybe he is just blessed with a good body."
    al_t "Definitely blessed with a body that has every woman he comes across salivating…"
    scene ch5sc03_155 with dissolve
    al_t "Stop it, I need to stop thinking about his… body… it gets me all riled up."
    al_t "*Sighs* But I’m just a girl… how can I deny myself his appeal?"
    scene ch5sc03_155a with dissolve
    al_t "The last batch of elixirs came out great, they’re potent enough to sedate even Eliza."
    al_t "I hope he’ll be impressed with me."
    scene ch5sc03_156 with dissolve
    al_t "*Giggles happily* Maybe even so impressed that he will pat me on the head?"
    al_t "I know he does that to Eliza sometimes…"
    al_t "He used to do it to me as well... when we were little."
    scene ch5sc03_157 with dissolve
    al_t "And if he’s close enough to pat me on the head…"
    scene ch5sc03_158 with dissolve
    al_t "He’d be close enough to touch me in other places as well… mMmh."
    scene ch5sc03_159 with dissolve
    al_t "He could unleash his desires on me… right-"
    scene ch5sc03_160 with dissolve
    al_t "-Here! AhHh… ohh…"
    scene ch5sc03_161 with dissolve
    al_t "*Moans* That- that’s so lewd! Mmmgh… yes… I like it when you touch me like this- AhHh…"
    al_t "*Moans* Don’t-... don’t stop-..."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_132 with Dissolve(2.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Hey… I had a feeling you’d be next."
    mc "You good? You look like you’re not eager to be here?"
    mh "..."
    scene ch6sc10_133 with dissolve
    mh "..."
    mc "*Sighs* Talk to me."
    scene ch6sc10_134 with dissolve
    mh "What you did… back in the Divination hut."
    scene ch6sc10_133 with dissolve
    mh "..."
    scene ch6sc10_134 with dissolve
    mh "It was… I-Incredible, okay?!"
    mh "I’ve never witnessed something like that, not once… you created a whole new shrine for us in less than an hour."
    mh "You-... you reconnected us to our goddesses… you… you completed the trials…"
    scene ch6sc10_132 with dissolve
    mc "So why do you look upset with me?"
    mh "..."
    scene ch6sc10_134 with dissolve
    mh "It is not you who I find myself upset at."
    scene ch6sc10_135 with dissolve
    mh "It’s… myself."
    mh "Hnngh… I-... I was wrong."
    scene ch6sc10_132 with dissolve
    mc "Wait… did you just say that?"
    mh "..."
    scene ch6sc10_135 with dissolve
    mh "Yes, I admit it… I was wrong about you."
    scene ch6sc10_134 with dissolve
    mh "I thought you were a venomous outsider… but you turned out to be the man we’ve waited decades for."
    mh "The chosen one that was prophesied by our elders."
    scene ch6sc10_136 with dissolve
    mh "I have… been foolish to resist you."
    mh "I desire to make amends, to correct myself under your guidance, as my A’khan, as my man."
    mh "I know there is no quick fix to the wounds I’ve caused… but, will you accept my attempt at earning your forgiveness?"
    mh "Will you..."
    scene ch6sc10_137 with dissolve
    mh "Accept me?"
    mh "As I stand before you, naked and vulnerable, willing to become yours."
    scene major_choice with Dissolve(1.5)
    ####Choice####
    menu:
        "I accept you, Marah. ({color=#ff8cdd}Romance Lock-in{/color})":
            scene ch6sc10_137 with dissolve
            mc "I know apologizing like this is probably the hardest thing you’ve had to do."
            scene ch6sc10_138 with dissolve
            mc "I believe you are being genuine, so yes."
            mc "I will accept you as my woman, my High-Priestess, and as my lover."
            mh "..."
            $ mh_path = True
            scene ch6sc10_139 with dissolve
            mh "Then, you are pleased with what you see? [mc]."
            scene ch6sc10_138 with dissolve
            mc "Very much so… your figure is striking."
            scene ch6sc10_139 with dissolve
            mh "I too… am pleased with what I see, your naked body is… marvelous."
            mh "Since the desecration… I’ve not felt any attraction towards a man… not until you arrived."
            scene ch6sc10_140 with dissolve
            mc "Come… your body is a work of art, and I desire to see it up close."
            mh "[mc], what you desire… shall be yours."
            $ mh_relationship = True
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc10_141 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            mh "We have less time tonight than what I desire… especially for our first time."
            mh "But I will do my best to satisfy you, to breed you as I desire."
            mc "Get on top of me, I’m craving to find out how your mature flower feels."
            scene ch6sc10_142 with dissolve
            mh "Mmh… so this is what a man’s spear feels like…"
            mh "You’re warm… hard… firm… yet, so… lively? Pulsing… beautiful."
            scene ch6sc10_143 with dissolve
            mh "Feeling you… touching you… knowing you’ve accepted me…"
            mh "Almost makes me feel wrathful that we do not have time to fully enjoy one another."
            mc "This’ll just be an appetizer for the future, our future."
            scene ch6sc10_142 with dissolve
            mh "Mmh… lovely way to see it as."
            mh "Yes, tonight is just a small appetizer of what my future with you holds."
            $ mh_trust += 5
            "Marah likes knowing you consider her a part of your future, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch6sc10_143 with dissolve
            mh "I’m going to breed you now, please… bless me with your seed as I become yours."
            scene ch6sc10_144 with dissolve
            "As Marah climbs on top of you, both of you feel a little awkward with your history."
            "But any awkwardness either of you may feel is swiftly pushed aside as you feel each other, naked, pressed together."
            "She lets out a gentle moan as she carefully push herself down onto your cock, feeling it slide between her wet lips."
            scene mh_lewd1 with dissolve
            "She carefully begins mating you, a woman in her 40's losing her virginity to you, this means the world to her."
            $ renpy.pause()
            mh "*Moans softly* Mnngh… [mc]... you slide between my lips so easily… Ahhh…"
            mc "That feels good… Mmmh… you’re dripping wet, Marah. Just for me?"
            mh "*Moans* Just for you, and no one else… Mmmh… this is how my body reacts to you…"
            mh "Just feeling how big you are… how you pulsate between my lips- AhHh… I can’t believe it’s happening."
            mh "I need you deeper… [mc], will you grant me permission to push you deeper?"
            mc "Mmh… do it… I’m eager to know what it feels like to be deep inside you."
            scene mh_lewd2 with dissolve
            $ renpy.pause()
            "With your permission, she begins pushing herself further down onto you at a quicker pace, allowing you fully inside her."
            mh "*Moans* OhHhh! We’re-... {b}we’re mating! AhhH! My A’khan!{/b}"
            with vpunch
            mc "Fuck… you’re- Mmgh! {b}You’re tight!{/b} Even when you’re dripping wet, I still feel your little pussy squeezing me."
            mh "{b}Ahh-AhH!{/b} I needed this! I needed you! I’ve waited my entire life for this moment- {b}Mmh!{/b}"
            with vpunch
            mh "I’ll be patient no longer… I’m finally {b}breeding with my man!{/b} {b}AiiyhH!{/b}"
            with vpunch
            "Marah begins to orgasm as your cock reach new depths and her orgasm brings forth yours as well."
            mc "{b}MMH! Marah! I’m cumming!{/b}"
            with vpunch
            mh "{b}Meeeee toooo! AHh! I feel it!! I feel your seed! MMh! Fill me my A’khan! Fill me with your godly spear!{/b}"
            scene ch6sc10_145 with dissolve
            with vpunch
            mh "*Squeals* {b}AiiyyyhH!!{/b}"
            "The shock and new sensation of your combined orgasm deep inside her, makes her lose balance while your orgasm is still going."
            mh "*Gasps* {b}[mc]!! AhhH!{/b}"
            scene ch6sc10_146 with dissolve
            with vpunch
            mh "Hnngh…"
            mc "You okay?"
            $ mh_trust += 5
            mh "Y-Yeah… what was that… that feeling inside of me?"
            mc "We both had an orgasm at the same time, it can be quite overwhelming to your senses if you aren’t prepared."
            mh "Y-Yeah… overwhelming is one way to describe it, it felt like I was levitating and then suddenly I lost balance."
            mh "I’ll… I’ll go clean up, this is a little embarrassing… thank you though, next time I’ll be better prepared, I promise."
            "Despite the embarrassing end to her orgasm, she is incredibly pleased you chose to accept her. Her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)
            "Before you can reassure her, she scurries off to get her dress and leave the chamber."

        "Not interested. (Neutral)":
            mc "No, I don’t accept you, you tried to kill me.... and turn the tribe against me."
            scene ch6sc10_133 with dissolve
            mc "It’s going to take a whole lot more than just seeing you naked to make me want you around."
            mc "For now, I suggest you make amends with the others. Maybe then I will be willing to let bygones be bygones."
            mc "Now, get out of here before I throw you out."
            scene ch6sc10_134 with dissolve
            mh "As you wish, my A’khan. I will continue to seek my redemption."
            scene black with Dissolve(1.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            $ renpy.pause(0.5)

    scene ss1 with Dissolve(1.5)
    $ renpy.pause()
    scene ss13 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch5sc07_231 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    bn "Sweetheart, I understand you’ve invited the adventurer’s guild to a banquet?"
    scene ch5sc07_232 with dissolve
    am "Uh-...  yeah, I have."
    scene ch5sc07_231 with dissolve
    bn "Marvelous! I have something I wish to discuss with [mc]"
    scene ch5sc07_238 with dissolve
    am "No."
    bn "No?"
    with vpunch
    am "Absolutely not!"
    scene ch5sc07_237 with dissolve
    bn "Sweetheart, I should very much like to talk to him. I have business with him."
    scene ch5sc07_238 with dissolve
    am "I said no. If you want to talk business with him, you can invite him for a meeting."
    am "This is my banquet, for him- for all of them. You are not disturbing my evening, you hear?"
    scene ch5sc07_239 with dissolve
    am "Mother! Tell him!"
    qm "Bennen, you know this is her first time having a party for her friends."
    scene ch5sc07_231 with dissolve
    bn "*Sighs* Fine, fine… I will arrange a meeting with him another time then."
    scene ch5sc07_230 with dissolve
    qm "As for your event, young lady…"
    qm "Do you need my help with arrangements?"
    scene ch5sc07_233 with dissolve
    qm "I know how cumbersome it can be to make sure everything is in order."
    qm "I honestly don’t know what to do with myself as of late… it’d be nice having something to occupy me."
    scene ch5sc07_234 with dissolve
    am "Uhh…"
    scene ch5sc07_235 with dissolve
    am "Hmmh…"
    amt "I could use some help… and she does have a great deal of experience with these sort of things."
    amt "But what if she tries to hijack [mc] from me?! Hmmh…"
    scene ch5sc07_234 with dissolve
    am "O-Okay… you can help, mother."
    scene ch5sc07_236 with dissolve
    am "But only with preparations!"
    am "You will not partake in the festivities themselves!"
    scene ch5sc07_240 with dissolve
    qm "Oh… okay, I guess that would be… acceptable."
    qm "I understand, you must think your mother too old to enjoy herself and make friends."
    scene ch5sc07_235 with dissolve
    amt "Heavens! Why did she have to put it like that!"
    amt "........."
    scene ch5sc07_239 with dissolve
    am "Mother, I do not believe you are too old, if-..."
    am "-If it would make you feel better, I’d allow you to partake."
    scene ch5sc07_235 with dissolve
    qm "Oh honey! Thank you, that is mighty sweet of you."
    qm "I know how much you look forward to seeing [mc] again, don’t you think he will be so handsome at the event?"
    scene ch5sc07_241 with dissolve
    "Amelia's cheeks turn bright red at the thought of seeing you."
    am "............"
    scene ch5sc07_242 with dissolve
    am "I-... I suppose?"
    scene ch5sc07_241 with dissolve
    qm "I’m sure he has been on your mind a great deal, I know you were just getting used to having him around."
    qm "I’m sure he’ll have missed you too sweetie."
    scene ch5sc07_242 with dissolve
    am "Uhh… you… you believe so?"
    scene ch5sc07_241 with dissolve
    qm "Absolutely, I’m certain he will be happy to embrace you upon his return-"
    scene ch5sc07_243 with dissolve
    with vpunch
    am "*Gasps* Mother!"
    am "Don’t-... don’t say such ridiculous things!"
    am "I’m going to bed!"
    bn "*Chuckles* Goodnight sweetheart."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_073 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "I wonder who’s next?"
    mct "By my count, all the high ranking members have been here, so it’s a toss up really on who appears next."
    scene ch6sc10_147 with dissolve
    mc "Sivah?"
    sih "Hi."
    mc "I’m a little surprised, didn’t expect you to partake."
    scene ch6sc10_148 with dissolve
    sih "The others… said you were bound in bed…"
    sih "I was curious."

    if siv_path == True:
        sih "Mother isn’t here to make me leave this time. *Snickers*"
    else:
        pass

    scene ch6sc10_149 with dissolve
    sih "Does my body appeal to you?"
    ####Choice####
    menu:
        "Your body is incredible. ({color=#ff8cdd}Romance{/color})":
            mc "Your body is outrageous for your youth… your mother said you’re 19?"
            $ sih_path = True
            sih "Mhm-hm. Just turned 19."
            scene ch6sc10_151 with dissolve
            $ sih_trust += 5
            sih "Does this appeal to you? That I’m much younger… tighter… than mommy?"
            mc "Mhm… it does. Your mother maintains an incredible figure as well."
            scene ch6sc10_152 with dissolve
            mc "But we both know that comparing her to you… isn't fair to her."
            sih "She does have me beat in a few areas… such as breast size… but mine are far more perky, don’t you think?"
            mc "Your breasts are making me salivate."
            "Sivah thoroughly enjoys your flirting and compliments. Her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch6sc10_153 with dissolve
            sih "*Snickers* I like how you look at me."
            sih "Like I’m a little treat that you can’t wait to sink your teeth into. *Giggles*"
            scene ch6sc10_154 with dissolve
            mc "Mhm… you certainly look tasty."
            scene ch6sc10_153 with dissolve
            sih "Do you want to taste me, daddy?"
            scene ch6sc10_154 with dissolve
            mc "Daddy?"
            sih "*Giggles* …"
            scene ch6sc10_153 with dissolve
            sih "Mommy says you’re my new daddy."
            mct "Right, I suppose her real father died before she was even born, I guess I could roleplay as her daddy."
            scene ch6sc10_154 with dissolve
            mc "Your mother’s right, you’re my little girl now, Sivah."
            scene ch6sc10_153 with dissolve
            sih "Would it make you happy daddy, if I let you taste me?"
            scene ch6sc10_155 with dissolve
            "Before you answer, she shuffles to her back and her delicate hand runs down her smooth stomach into her panties."
            sih "*Moans softly* Daddy-... mmh… it feels really good… when you’re near me."
            mc "You enjoy being naughty around daddy?"
            scene ch6sc10_156 with dissolve
            sih "*Giggles* Yes, Daddy! I like playing with you."
            sih "You make me feel excited… do I excite you too, daddy?"
            mc "Mhm, you do-"
            scene ch6sc10_157 with dissolve
            mc "*Muffled* Mmnh…"
            sih "My fingers got a little sticky, lick them for me?"
            "Sivah puts her juice-covered fingers between your lips and you happily open your mouth, letting her inside."
            scene ch6sc10_158 with dissolve
            "After you getting a taste of her nectar, she moves her fingers to her own mouth, sucking them gently."
            sih "*Sucks* Mmmh… your saliva with my juices… yum."
            sih "You’re so good to me daddy… *Licks*"
            scene ch6sc10_159 with dissolve
            "Having cleaned her fingers, she gets up from the bed and begins to head for the exit."
            mc "Hey… where you going?"
            sih "I’m going to bed, daddy. Night night!"
            sih "We’ll play more next time! *Giggles*"
            $ sih_trust += 5
            "Sivah is intrigued by your willingness to play with her, Sivah's trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            mct "*Chuckles* Such a little tease… but she’s certainly interesting."

        "Not interested. (Neutral)":
            scene ch6sc10_150 with dissolve
            mc "Your body is average, I can’t say I'm particularly interested in it."
            sih "Boring."
            $ sih_trust -= 5
            "Sivah finds your lack of interest bland, her trust has decreased by {size=+3}{b}{color=#f00}5{/color}{/b}{/size}."

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_160 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    sj "Hey…"
    sj "[mc], will you… accept me?"

    if sj_relationship == True:
        mc "Don’t be silly, we both know I’ll never turn you down."
        mc "Now, undress yourself and come ride me."
        scene ch6sc10_161 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        sj "*Giggles* Bold as ever I see… good."
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        sj "Means you’re as eager to be inside me as I am."
        scene ch6sc10_162 with dissolve
        sj "Your spear is as bold as I remember I see… and hard- Mmgh… and big- AhhH."
        mc "It's been too long since we’ve mated… don’t hold back, ride me with all you’ve got, little huntress."
        scene sj_lewd18 with dissolve
        $ renpy.pause()
        "Upon hearing your command, and with full agreement on the fact it's been way too long, she begins eagerly bouncing on you."
        sj "*Moans* {b}Ah-AiiH!! YES!!{/b} This is exactly how I remember your heroic spear feeling- {b}AHhH!{/b}"
        with vpunch
        sj "*Moans passionately* {b}I love you!{/b} Mmgh! I love how you stretch my little flower- {b}Aiiyh!!{/b}"
        with vpunch
        mc "F-Fuck! Mmgh… you’re cumming already?! {b}MMgh! Fuck you’re tight!{/b}"
        with vpunch
        sj "{b}I can’t- I CAN’T STOP! AH! [mc]! YOU’RE TOO DEEP! AHH!!{/b}"
        scene ch6sc10_162 with dissolve
        "You barely manage to withstand the incredible pleasure of her orgasm, and she shifts her position."
        scene ch6sc10_163 with dissolve
        sj "Holding back are we? I know you’re tied up but-"
        mc "Of course I’m holding back the best I can, do you think I want our breeding to stop?"
        mc "We both know how much I love being inside you at this point."
        sj "I love the feeling as well, but tonight we do not have the time sadly… I will ride you until you cum inside me!"
        scene sj_lewd19 with dissolve
        $ renpy.pause()
        with vpunch
        sj "*Moans loudly* I’m not stopping! Not until you fill me with your delicious seed! {b}Not until you impregnate me! Ahh!!{/b}"
        mc "Nngh! Five hells you’re tight and soaking wet- AhhH…"
        sj "I know how you love my pussy sucking you dry! I’m not leaving until you give me what I desire- {b}Ahh!{/b}"
        with vpunch
        sj "You’re my A’khan! {b}It is your right to breed me!{/b} Ahhh! And tonight- tonight it’s my right to breed you! {b}Aiiiyh!!{/b}"
        with vpunch
        mc "Suji- I’m going to- {b}AHH!! I’m cumming!{/b}"
        with vpunch
        sj "{b}Yes!! Love me! Mate me! Breed me!{/b} Ahh-Nnghh! By the jungle you’re {b}biiiiig!!{/b}"
        scene ch6sc10_163 with dissolve
        "You send load after load deep inside her young huntress pussy while her moans fills the room with ease."
        scene ch6sc10_164 with dissolve
        with vpunch
        sj "{b}[mc]-Aiihh!!{/b} By the goddess you filled me!!"
        mc "*Out of breath* I’m not even the one who’s doing the work and you still exhaust me…"
        sj "I would say I’m sorry… but that’d be a lie. *Giggles* Feeling your seed within me… its all I ever want."
        scene ch6sc10_165 with dissolve
        sj "[mc]... I love you."
        mc "I love you too, Suji."
        scene ch6sc10_166 with dissolve
        sj "*Mwah* Nnnh…"
        "Hearing that you love her, she leans down and engages you in an intimate kiss while resting herself on your chest."
        mct "Mmh… I love the way she kisses, always so full of passion and intimacy, not to mention her lips are both soft and tasty."
        sj "I’m so excited for our future together… a future where I’m only yours and I never have to fear outsiders again."
        mc "I’ll protect you, Suji. No matter what, you’re my woman."
        scene ch6sc10_165 with dissolve
        sj "That’s all I want to be. Your woman, your huntress, your lover."
        $ sj_trust += 10
        "Suji is fully in love with you. Her trust has increased by {size=+10}{b}{color=#2bff8b}10{/color}{/b}{/size}."
        "She giggles happily before she climbs off you and takes her leave."

    else:
        mc "Hey, Suji… sorry, I’m not interested in you tonight, but yes. I do accept you as a huntress of our tribe."
        sj "Thank you, enjoy the rest of the ceremony… my A’khan."

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_167 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Your ceremony continues, women of the tribe keep entering…"
    "Hoping to be accepted by their new leader."
    scene ch6sc10_168 with dissolve
    "One after the other, the women eagerly enter Echo’s chambers…"
    "Seeking to breed with you, their A’khan."
    scene ch6sc10_169 with dissolve
    "And one by one, you make the choice whether to allow them to fulfill their desires or reject them for the night."
    "Whatever your choice is, the women respect your wishes happily."
    scene ch6sc10_170 with dissolve
    "You soon realize, just how many women serve under you now…"
    "Just how many lives you’re in charge of… how many lives that are counting on you to lead them."
    scene ch6sc10_171 with dissolve
    "A responsibility you did not intend on taking upon yourself when you first arrived amongst these women."
    "But, little by little, they have made their way into your heart…"
    scene ch6sc10_172 with dissolve
    "Be it love… respect… faith… morals… culture… achievements… promises…"
    "No matter how it happened, with each woman entering the chamber, you realize…"
    scene ch6sc10_173 with dissolve
    "They matter to you… they are yours… your women… your tribe… your people."
    "You care about them, their wellbeing, their future, their history, you will do anything to protect them."
    scene ch6sc10_174 with dissolve
    "A part of you wish you could remain here amongst them, lead a simple life away from everything."
    "But deep down, you know that is not what fate has in store for you…"
    scene ch6sc10_175 with dissolve
    "You feel at peace knowing that you will be able to visit them whenever you desire it."
    "Thanks to Maia’s gift, teaching you Dimension door."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "The ceremony continues long into the night, with well over 70 women in A’nai now that the tribes have been merged."
    scene ss1 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_176 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ri "Three."
    ri "Three of them this week."
    scene ch6sc10_177 with dissolve
    ri "Aggressive."
    ri "Bounty on me must have increased."
    ri "*Exhales* Can’t remain, much longer... city, not safe."
    scene ch6sc10_176 with dissolve
    ri "But-... [mc] has not returned yet."
    ri "Need to see [mc]."
    scene ch6sc10_177 with dissolve
    ri "He needs to know…"
    scene ch6sc10_178 with dissolve
    ri "He's... only one I can trust."
    ri "For now, I’ll hide."
    scene ch6sc10_179 with dissolve
    ri "The shadows of the city... will be my companion."
    ri "[mc]..."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch5sc09_189 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    fy "You’re the carpenter’s daughter, right? The one who’s located just outside Luxenford?"
    scene ch5sc09_190 with dissolve
    wo "Yes… but what does that have to do with my missing panties-"
    scene ch5sc09_191 with dissolve
    fy "Everything!"
    fy "Trust me, fair maiden. This thief targeted you specifically for an obvious reason."
    scene ch5sc09_190 with dissolve
    wo "Uhh… what would that be?"
    scene ch5sc09_189 with dissolve
    fy "Your beauty of course!"
    fy "You’re a very attractive female, that is why the thief desired your panties, I’m certain of it."
    scene ch5sc09_190 with dissolve
    wo "O-Okay…? Still, you didn’t answer my question."
    wo "Have you made any progress on catching the thief? Or possibly recovering my panties?"
    scene ch5sc09_191 with dissolve
    fy "*Scoffs* Oh my sweet summer child, catching a thief as impressive as this is no simple task."
    fy "But worry not, for I, Flynn, will get my hands on your used panties."
    scene ch5sc09_189 with dissolve
    fy "Err- to return them to you, of course."
    scene ch5sc09_190 with dissolve
    wo "Uhh-... great."
    wo "I think I may just see if some of the local guards can discover anything."
    scene ch5sc09_191 with dissolve
    fy "Ah, you needn’t pester them with such issues. They are busy protecting the city."
    fy "Worry not, I have made good progress already... the thief will be caught soon."
    wo "*Sighs* …"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss39 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)

    if ec_relationship == True:
        mct "Mmmh… this sensation… one I’m all too familiar with- Nnnhh…"
        scene ec_lewd52 with Dissolve(1.5)
        $ renpy.pause()
        "As you open your eyes, you see none other than your gorgeous wife, enjoying her breakfast."
        ec "*Sucks gently* Mmmh… delicious… *Licks* Nnghh…"
        mc "*Moans* Mmh- Echo… I knew it couldn’t be a dream… not when it felt this good- Mmmh…"
        ec "Morning, my love… *Sucks* Mmgh… you don’t mind me enjoying my breakfast a little early, do you? *Licks*"
        mc "Certainly not… Mmh… as my woman, my wife… you will have anything you desire."
        with vpunch
        ec "*Sucks gently* You’re pulsating- Mmmh… let me have your seed… feed me, baby."
        scene ch6sc10_181 with dissolve
        with vpunch
        "Echo pushes you as deep as she can handle, you feel her convulsing as she gags and sucks when you enter her throat."
        scene ch6sc10_182 with dissolve
        with vpunch
        "She feels you’re right at the edge, so she stops moving and just focus on tightening her big juicy lips around your cock."
        mc "*Moans* Ahh! Echo- Mmh! Here you go-"
        with vpunch
        ec "*Muffled sucking and gagging* MMGH!! GhhHGH!! Ghh-Mmgh!!"
        scene ch6sc10_183 with dissolve
        with vpunch
        "Not able to handle your full load whilst your cock remains in her throat, she begins choking and releases you."
        ec "*Gags and swallows* Mmgh! gGhH!! Mmmh!!"
        "To your surprise, she does not fully release you, just enough that she stops choking, then she continues to suck and swallow."
        scene ch6sc10_184 with dissolve
        ec "Mmmh… thank you baby."
        ec "I always wondered what it would be like to have breakfast in bed. *Giggles softly*"
        scene ch6sc10_185 with dissolve
        mc "No, thank you. That was an incredible way to wake up."
        mc "I love you, Echo."
        scene ch6sc10_184 with dissolve
        ec "As I love you, [mc]."
        ec "Mmmh… I’m going to go get your breakfast now."
        scene ch6sc10_185 with dissolve
        mc "*Chuckles* You’re not my breakfast?"
        ec "*Kisses* Mmh."
        scene ch6sc10_186 with dissolve
        ec "Sorry my love, but after your ceremony last night…"
        ec "I need to make sure you get some actual food in you. *Giggles*"
        mc "Good call actually, I’m starving."
        mc "Especially having to look at a tasty little thing like you."
        scene ch6sc10_187 with dissolve
        ec "*Giggles* I look appetizing to you?"
        ec "Good… As your wife, I will have you salivating day and night."
        scene ch6sc10_188 with dissolve
        mc "You don’t have to worry about that… even when you’re clothed, I can’t help but drool a little."
        ec "*Giggles lightly* Charmer…"
        ec "But for now, I’d prefer if you drool over the breakfast I’ve made for you."
        scene ch6sc10_189 with dissolve
        mc "Oh I’m drooling alright."
        ec "What would you-"
        scene ch6sc10_190 with dissolve
        ec "Oh? You’re still tied up?"
        mc "*Chuckles* You’re the one who tied me last night…"
        scene ch6sc10_191 with dissolve
        ec "*Giggles* Oops! I didn’t even think to check when I entered this morning…"
        ec "I was a little… eager for my breakfast. *Snickers softly*"
        scene ch6sc10_190 with dissolve
        ec "Hmmh… since you’re still tied up…"
        scene ch6sc10_189 with dissolve
        ec "I suppose I’ll have to feed you."
        scene ch6sc10_192 with dissolve
        mc "I can think of worse ways to have breakfast than being fed by my beautiful wife."
        ec "*Giggles softly* Beautiful wife? For such compliments I’ll definitely give you a treat afterwards."
        scene ch6sc10_193 with dissolve
        ec "Here, have a Tintoberry!"
        ec "They don’t look like much, but they’re juicy and surprisingly filling."
        scene ch6sc10_194 with dissolve
        "You open your mouth with anticipation of tasting this ‘Tintoberry’ she has been hyping up."
        scene ch6sc10_195 with dissolve
        mct "Mmh… damn… she wasn’t kidding, they are juicy…"
        ec "*Giggles* Baby! You’re sucking my fingers so eagerly… you really like it that much?"
        scene ch6sc10_193 with dissolve
        ec "Here, have another."
        mc "Echo, what was that? Something tasted very familiar about that."
        scene ch6sc10_194 with dissolve
        ec "Oh?"
        ec "Maybe it's the fact I’m feeding you with the fingers that were just inside of me moments ago, when I sucked you."
        scene ch6sc10_195 with dissolve
        mc "MMffhh! Mmhh… *Sucks*"
        ec "Knowing how much you enjoy my juices, I thought I’d feed you with this hand."
        mc "*Muffled* Mmgh… good call… delicious."
        scene ch6sc10_194 with dissolve
        ec "Open wide baby. I got a juicy one coming now."
        "You follow her command and eagerly anticipate the next berry combined with her delicate fingers."
        scene ch6sc10_196 with dissolve
        "It takes her a bit longer than usual to pop the berry into your mouth but you don’t question it."
        ec "*Muffled* Here weh go… yuh ready babyh?"
        scene ch6sc10_197 with dissolve
        mc "Ready-"
        "You feel Echo’s warm and tender body rest on you…"
        "Her hand gently grasps your shoulder and her soft breast squished against your chest, while the tip of her nose caresses yours."
        "You know exactly what’s coming your way, something you enjoy very much."
        scene ch6sc10_198 with dissolve
        "Echo leans further into you, and as her soft upper lip makes contact with yours, she guides the berry with her tongue."
        "You take in every second of this moment, as your wife is feeding you in the most intimate way imaginable."
        scene ch6sc10_199 with dissolve
        ec "*Moans softly* Mmmh-Nnghh… I love you."
        "She bites the berry between your mouths, making its juices flow between both of your tongues."
        scene ch6sc10_200 with dissolve
        mc "Mmh… I love you too."
        "The two of you intimately share the berry juices by licking each other’s tongues, caressing each other with each lick."
        scene ch6sc10_199 with dissolve
        ec "*Kisses passionately* Mmgh… can you feel my heart baby?"
        mc "I can- Mmmh… you’re incredibly happy right now."
        scene ch6sc10_200 with dissolve
        ec "*Licks* Happier than I’ve ever felt."
        ec "All because of the man I love, who is now my husband, my A’khan."
        scene ch6sc10_191 with dissolve
        "Echo leans back gently."
        ec "*Giggles warmly* That was…"
        mc "Amazing. Any kiss with you tends to turn out that way."
        scene ch6sc10_190 with dissolve
        ec "Y-Yeah… I think so too. Your kisses are incredible… tasty… warm… intimate."
        ec "I think it's time we untie you…"
        scene ch6sc10_201 with dissolve
        ec "You have a big day ahead of you, now that you’re our A’khan."
        "You feel her delicate hands trace your forearm, then she unties the rope."
        scene ch6sc10_202 with dissolve
        ec "You should go see Suji and Zyra, I believe they are awaiting you in Suji’s hut."
        scene ch6sc10_203 with dissolve
        mc "Oh?"
        scene ch6sc10_202 with dissolve
        ec "I’m not going to spoil the surprise, my love."
        ec "Just go, and they’ll take care of you."
        scene ch6sc10_203 with dissolve
        mc "*Chuckles* Alright, now you’ve gotten me curious."
        scene ch6sc10_202 with dissolve
        ec "*Giggles* Go, if you keep lying naked and handsome before my eyes…"
        ec "I… I will not be able to stop myself from mating with you again."
        scene ch6sc10_203 with dissolve
        mc "You realize saying things like that makes me not want to get out of bed?"
        scene ch6sc10_204 with dissolve
        with vpunch
        ec "Shush! *Giggles* Get out of our bed and let me rest!"
        ec "Otherwise… I’ll tie you up again and ride you for hours!"
        mc "*Chuckles* Alright, alright. I’m going."
        $ ec_trust += 5
        "Echo loves when you're playful with her, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
        scene ch6sc10_205 with dissolve
        mc "Suji’s hut, you say?"
        scene ch6sc10_206 with dissolve
        ec "Mhm-Hm!"
        ec "You have a sexy ass! *Giggles*"
        scene ch6sc10_205 with dissolve
        mc "Do you want me to come back there and spank you?"
        scene ch6sc10_206 with dissolve
        ec "Yes! I mean- No!"
        ec "*Giggles* Go, but keep my spanking in mind… for later."
        scene ch6sc10_207 with dissolve
        ec "Meanie! You didn’t have to put on pants before you were outside, you know?!"
        mc "*Chuckles* You’ve seen plenty this morning."
        ec "I’m your wife! I’ll never get tired of seeing you!"
        mc "See you later, Wife."
        scene ch6sc10_208 with dissolve
        ec "I love you!"
        mc "I love you."
        ec "With how I woke you up, you better! *Giggles*"
        mc "*Chuckles* I’ll return the favor next time."
        scene ch6sc10_207 with dissolve
        ec "Yes! I look forward to being awoken by the feeling of your tongue… inside of me."
        mc "You’re insatiable."
        ec "Mmh-hmm! Say hi to Suji and Zyra!"

    else:
        $ renpy.pause(0.5)

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss53 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_209 with Dissolve(2.5)
    $ renpy.pause()
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_210 with dissolve
    mal "Gaia, honey… didn’t you summon her?"
    gai "I did."
    mal "Then what’s taking her so long?"
    scene ch6sc10_211 with dissolve
    mal "I’ve been receiving some very… pleasurable offerings over the last couple of days."
    mal "I don’t want to miss out."
    scene ch6sc10_212 with dissolve
    gai "You’ll have plenty of time to enjoy your offerings later."
    gai "There’s other things to enjoy in life than just receiving our offerings."
    scene ch6sc10_211 with dissolve
    mal "As if you haven’t felt it too?"
    mal "You must’ve felt our connection restored and… deepened."
    scene ch6sc10_213 with dissolve
    mal "It’s like it has been magnified…"
    mal "Such intensity… it’s buzzing all over my body with each offering."
    scene ch6sc10_212 with dissolve
    gai "Mhm… I have."
    scene ch6sc10_214 with dissolve
    gai "Offerings from my followers have felt… pure, untainted… better than ever before."
    mal "Nothing like a couple of decades with impure offerings to really appreciate them."
    gai "Mhm, when [mc] built the shrine yesterday, I felt it."
    scene ch6sc10_213 with dissolve
    mal "Me too, as did Maia I’m sure."
    mal "[mc]... he’s doing this to me on purpose… he’s trying to rile me up."
    scene ch6sc10_211 with dissolve
    mal "Looks like he has succeeded. *Snickers*"
    mal "My body tingles constantly at the thought of him..."
    scene ch6sc10_214 with dissolve
    gai "Get yourself together, we’ve called upon Maia today to discuss the soulbinding… it was your idea."
    gai "If you keep acting like a lovestruck succubus, she’s not even going to let you present your idea."
    scene ch6sc10_215 with dissolve
    mal "Speaking of… here she comes."
    mal "She’s only kept us waiting over an hour."
    scene ch6sc10_216 with dissolve
    $ renpy.pause()
    scene ch6sc10_217 with dissolve
    $ renpy.pause()
    scene ch6sc10_218 with dissolve
    $ renpy.pause()
    scene ch6sc10_219 with dissolve
    $ renpy.pause()
    scene ch6sc10_220 with dissolve
    $ renpy.pause()
    scene ch6sc10_221 with dissolve
    $ renpy.pause(0.5)
    mal "She… doesn’t look happy to see us."
    gai "*Scoffs* More like she does not look happy to see {b}you{/b}."
    scene ch6sc10_222 with dissolve
    mal "S-Sister! Good of you to come."
    mal "There is much we need to discuss-"
    mai "Malanthe, come. We shall speak alone."
    mal "S-Sure… whatever you want sweet sister."
    scene ch6sc10_223 with dissolve
    gai "Maia-"
    scene ch6sc10_224 with dissolve
    mai "I do not want to hear it, okay?"
    mai "I’m going to speak to Malanthe, one on one."
    scene ch6sc10_223 with dissolve
    gai "*Sighs* Okay… don’t be too hard on her, we mean well."
    scene ch6sc10_224 with dissolve
    mai "I’m sure you do, Gaia… but Malanthe? We both know she loves to stir the pot."
    mai "I will not have the two of you gang up on me and convince me to do something I don’t believe is right."
    scene ch6sc10_223 with dissolve
    gai "I understand…"
    scene ch6sc10_224 with dissolve
    mai "I will speak to each of you individually, and then I will make my decision."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_225 with Dissolve(1.5)
    mal "Sweet sister…"
    mai "..."
    mai "*Angrily* You’re right, there is much we need to ‘discuss’..."
    scene ch6sc10_226 with dissolve
    mai "Let’s start with how your lustful scent was all over [mc] when I finally reunited with him?"
    with vpunch
    mai "Or how you’ve made him your champion? What are you up to? {b}Speak!{/b}"
    scene ch6sc10_227 with dissolve
    mal "I’ll get straight to the point then."
    mal "Here’s what we wish to discuss with you-..."
    scene ch6sc10_225 with dissolve
    "Malanthe begins to discuss what she and Gaia have been talking about in regards to the soulbinding."
    "About her wishes for you, about the consequences of doing it and not doing it."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "An hour passes."
    scene ch6sc10_228 with dissolve
    gai "You lasted longer than I expected."
    mal "Ugh… she refuses to listen to me, no matter how reasonable my argument."
    mal "Your turn, she usually listens to you."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_229 with Dissolve(1.5)
    $ renpy.pause(0.5)
    gai "Maia… hey, hey… what’s this?"
    mai "*Sobs* …"
    scene ch6sc10_230 with dissolve
    gai "You’ve been crying?"
    gai "Talk to me."
    scene ch6sc10_231 with dissolve
    gai "Tell me everything you’re feeling."
    gai "Every last little bit."
    "Gaia gently wipes the last of Maia’s tears."
    scene ch6sc10_232 with dissolve
    mai "Is it true, what she said?"
    mai "Do you really intend to take him from me?"
    scene ch6sc10_233 with dissolve
    gai "Honey, no… is that what you believe will happen?"
    gai "Nobody is going to take [mc] from you. *Sighs* I knew letting Malanthe present the idea was a bad call."
    scene ch6sc10_232 with dissolve
    mai "I love him, Gaia."
    mai "I love him more than I could ever describe, more than you could ever imagine."
    scene ch6sc10_233 with dissolve
    gai "I know you do. As does Malanthe-"
    scene ch6sc10_232 with dissolve
    mai "Then why?! Why would the two of you- my own sisters suggest that I share the love of my life?"
    mai "I thought the two of you called upon me to explain yourselves as to why you made him your champion…"
    scene ch6sc10_233 with dissolve
    gai "Oh… I can see how this came as quite the gut punch then."
    gai "Do not blame Malanthe, you know she isn’t the best at delivering news… but you also know her heart to be genuine."
    scene ch6sc10_232 with dissolve
    mai "I do… but this? This is too much!"
    mai "How am I supposed to respond to a suggestion like this?!"
    scene ch6sc10_230 with dissolve
    gai "How about you and I talk about it, hmm? Then you can respond afterwards."
    "Maia nods."
    scene ch6sc10_233 with dissolve
    gai "We all know how much you care about [mc], we all know you were destined to be his and he, yours."
    gai "You were fated to be lovers, you were soulbound. And then you lost it all due to his father."
    scene ch6sc10_234 with dissolve
    gai "You didn’t deserve that, and for the last two decades, Malanthe and I have been forced to watch you-"
    gai "-Going through the worst heartbreak we’ve ever seen or felt."
    scene ch6sc10_235 with dissolve
    gai "You’re a goddess of love, and yet… you’ve never felt or had love. Not until [mc] was born."
    gai "You’re right, I cannot begin to imagine how that would feel, to have that taken away against my will."
    scene ch6sc10_234 with dissolve
    gai "But something I do know, from seeing it first hand… is that I never want you to experience that again."
    gai "You’ve finally gotten [mc] back in your life, something none of us thought would be possible."
    scene ch6sc10_233 with dissolve
    gai "Our suggestion of this threesome… threeway soulbinding, it comes not out of desire for [mc]-"
    gai "-It comes out of love for you, sister."
    scene ch6sc10_234 with dissolve
    gai "I will not deny, both Malanthe and myself, we do feel attracted to him."
    scene ch6sc10_235 with dissolve
    gai "He fascinates us, he has impressed us, he has earned our respect and interest."
    gai "But neither of us can claim to love him, not yet."
    scene ch6sc10_232 with dissolve
    mai "Then why… why do you want to create this new soulbinding with all three of us?"
    scene ch6sc10_233 with dissolve
    gai "Three reasons."
    gai "Firstly, we wish to restore your soulbinding which was shattered."
    scene ch6sc10_235 with dissolve
    gai "Secondly, it is a chance for Malanthe and I to have him in our lives, to get to know him-"
    gai "-a chance for us to possibly experience this incredible love, which you feel."
    scene ch6sc10_234 with dissolve
    gai "Thirdly, you know the uncertainty his future holds."
    gai "Do you not believe that having three goddesses in his corner will be a tremendous aid to him?"
    scene ch6sc10_229 with dissolve
    mai "I-..."
    mai "*Sighs heavily* I know Gaia… what you’re saying… it all makes sense."
    mai "So why? Why does it hurt my heart so much?"
    scene ch6sc10_233 with dissolve
    gai "Sweetie, it hurts because it is sudden and beyond what you had expected."
    scene ch6sc10_235 with dissolve
    gai "But when you think about it for a bit, truly think about it…"
    gai "[mc] is not going to care any less about you, his feelings for you are not going to weaken."
    scene ch6sc10_234 with dissolve
    gai "He will simply gain more people to care about, and in-turn care about him."
    gai "We both know that is something he is going to need if he hopes to keep the darkness within him at bay."
    scene ch6sc10_233 with dissolve
    gai "A threeway soulbinding has never been created before, Malanthe and I believe it will be powerful enough-"
    gai "-To even withstand a sundering by his father."
    scene ch6sc10_232 with dissolve
    mai "*Gasps* You cannot be serious?! Y-You know how powerful his father is!"
    mai "He probably wouldn’t even break a sweat, we’d only incur his wrath."
    scene ch6sc10_233 with dissolve
    gai "You know how powerful soulbindings are, and one with [mc]?"
    gai "Means that our soulbinding will grow stronger and stronger as [mc] grows stronger."
    scene ch6sc10_234 with dissolve
    gai "Before we know it, even his father will not be able to do anything about it."
    gai "Nobody will ever break your heart again, Maia."
    scene ch6sc10_235 with dissolve
    gai "Nobody will be able to take [mc] from you again."
    gai "I know this isn’t what you had wanted initially, but can you at least admit, it is the best course of action for all of us."
    scene ch6sc10_229 with dissolve
    mai "I-..."
    mai "Okay…"
    mai "I will agree to it, it is the best way to protect [mc]... and it does fill me with confidence knowing we’ll be in it together."
    mai "But you know what happens if he dies, if you’re soulbound to him-"
    scene ch6sc10_233 with dissolve
    gai "{b}We all die{/b}."
    gai "It’s a risk Malanthe and I are willing to accept."
    scene ch6sc10_232 with dissolve
    mai "Why? Why would you risk it?"
    scene ch6sc10_233 with dissolve
    gai "We wish to know what it means to love, to feel alive."
    scene ch6sc10_235 with dissolve
    gai "The three of us have been sisters for over {b}three millennium{/b} at this point."
    gai "Yet none of us have truly lived, truly loved… not until you gained [mc]."
    scene ch6sc10_234 with dissolve
    gai "We do not wish to live only to fulfill the tasks of deities, to lead hollow lives… we believe truly living is worth the risk."
    scene ch6sc10_229 with dissolve
    mai "I see…"
    mai "Good, I wasn’t going to allow it, not if you only did it for me, but knowing how I’ve felt since [mc] was born…"
    mai "It would be incredibly selfish of me to not allow my sisters a chance to experience that."
    mai "But… none of this matters, not until we discuss it with [mc], if he does not accept, then all of it is for naught."
    scene ch6sc10_234 with dissolve
    gai "Come, let us talk everything over with Malanthe, then we’ll summon [mc]."
    mai "*Nods* Mhm."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_236 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "I don’t think I’ve ever actually visited Suji’s hut as of yet."
    mct "Echo said they had a gift for me… or something like that."
    scene ch6sc10_237 with dissolve
    mc "Hey ladies."
    sj "[mc], please… take a seat in the chair."
    mc "Ominous, but okay."
    scene ch6sc10_238 with dissolve
    "You take a seat as requested, and Zyra begins fidgeting at the table while Suji remains by your side."
    mc "So, what are we doing today? Echo said you had something for me."
    sj "Oh, we do. *Giggles*"
    scene ch6sc10_239 with dissolve
    sj "Tell me [mc], when was the last time someone took care of this bird's nest you’ve got going on here?"
    mc "*Chuckles* Bird’s nest? You're insulting me first thing in the morning?"
    scene ch6sc10_240 with dissolve
    sj "I wouldn’t dare. *Giggles*"
    sj "You look mighty cute, but today is a big day for you."
    sj "Your first day as our A’khan."
    scene ch6sc10_239 with dissolve
    mc "Mhm, I suppose..."
    scene ch6sc10_240 with dissolve
    sj "We’re just going to tidy you up a bit, okay?"
    scene ch6sc10_239 with dissolve
    mc "I don’t know… I’m kinda used to my hair the way it is."
    sj "Pretty please with a jungle-jingle on top?"
    scene ch6sc10_240 with dissolve
    sj "I promise we’ll take good care of you."
    scene ch6sc10_239 with dissolve
    mc "*Sighs* Fine, I’ll trust in yours and Zyra’s taste."
    mc "Worst case I can just let it grow back."
    scene ch6sc10_240 with dissolve
    sj "Exactly! Prepare yourself to look like the sexiest A’khan in the history of Khans!"
    scene ch6sc10_241 with dissolve
    mc "A blindfold, really?"
    sj "Just trust us. It’ll protect your eyes from stray hairs as we cut and…"
    zy "And it'll increase the sensation of being given a haircut by… us."
    "You feel Zyra gently tie the knot whilst Suji’s delicate touch tilts your head upwards."
    scene ch6sc10_242 with dissolve
    "Zyra begins to embrace you, letting your head rest against her soft breasts whilst Suji begins to cut."
    mc "I see what you mean about increasing the sensation…"
    sj "Mhm, we had a feeling you would prefer it this way, hold still."
    scene ch6sc10_243 with dissolve
    sj "That’s good Zyra, hold him just like that."
    mc "You guys have done haircuts before… right?"
    sj "Sure! Just… not on men, obviously."
    scene ch6sc10_244 with dissolve
    sj "Hold him still, I’m almost done, it would be a shame if I accidentally cut him at the finish line."
    zy "Okay. Just rest on me, [mc]."
    "You feel Zyra’s soft fingers rest on your chin, gently pressing your head against your warm, soft breasts."

    if zy_path == True:
        sj "Zyra, could you turn his head a bit more towards you? I need a better angle."
        scene ch6sc10_244a with dissolve
        "Zyra gently turns your head and positions herself further onto you while Suji moves on to the back."
        zy "Is this how you want him?"
        sj "Yes, this is perfect. Keep him like this, okay?"
        scene ch6sc10_244b with dissolve
        zy "*Heavy breaths* O-Okay…"
        "Feeling your hot breath on her nipple as she rests it on your lips, Zyra gently caresses your chest and chin."
        scene ch6sc10_244c with dissolve
        zy "*Moans softly* Hnngh…"
        scene ch6sc10_244b with dissolve
        sj "What was that? Did you say something?"
        scene ch6sc10_244c with dissolve
        zy "N-No! I just had something I needed to get out."
        scene ch6sc10_244b with dissolve
        sj "Uh… okay? Anyways, keep him still, this might take a while back here, I don’t want to mess it up."
        scene ch6sc10_244c with dissolve
        zy "We’ll-... we’ll do our best, won’t we, [mc]?"
        scene ch6sc10_244b with dissolve
        mc "Mhm-hm… our very best."
        scene ch6sc10_244c with dissolve
        "She continues to run her perky nipple back and forth between your lips, teasing you… inviting you to play."
        scene ch6sc10_244b with dissolve
        mct "This naughty little huntress… let’s show her what happens when she teases me like this."
        scene ch6sc10_244c with dissolve
        zy "*Gasp softly* Aiih…"
        "Zyra lets out a small gasp, surprised that you’re bold enough to lick her nipple with Suji right behind you."
        scene ch6sc10_244b with dissolve
        sj "Zyra! You startled me… why are you whimpering out of nowhere?!"
        scene ch6sc10_244c with dissolve
        zy "Uh-... uh… uh, I just remembered that I-... uhm… that I hadn’t bathed this morning!"
        scene ch6sc10_244b with dissolve
        sj "Yeah? What’s the big deal about that?"
        scene ch6sc10_244c with dissolve
        zy "*Moans softly* Ohh… you know… we’re awfully close to [mc]... he might think I’m dirty…"
        mct "Haven’t bathed huh? No wonder her nipple is a little salty mmh… *Inhales* her breasts are covered in pheromones."
        "Overwhelmed with excitement and desire from your tongue running across her sensitive nipple-"
        scene ch6sc10_244d with dissolve
        "-Zyra grasps you gently but firmly, pressing you further into her breast. Her intention is clear, she wants you to begin sucking."
        scene zy_lewd11 with dissolve
        $ renpy.pause()
        "With her perky nipple now inside your mouth, your desire to suck it is in overdrive and you begin giving her what she craves."
        zy "*Moans quietly* Ohh… mmH…"
        sj "Seriously Zyra, hold him still!"
        zy "Ahh… I’m trying-... our A’khan is a little unruly… Ahhh…"
        sj "Again with the noises? What is up with you today?"
        zy "Ohh… N-Nothing- aah… I just… stubbed my toe on the chair, yeah… just that…"
        with vpunch
        mct "*Sucks* Mmmgh… nice save… she’s loving this, I can feel her rubbing herself against my arm… she’s soaking wet."
        $ zy_trust += 3
        scene ch6sc10_244d with dissolve
        "As you feel Zyra begin to tremble, you stop sucking her nipple, knowing she won’t be able to keep quiet if she orgasms."
        scene ch6sc10_244c with dissolve
        $ renpy.pause(1)
        scene ch6sc10_244b with dissolve
        $ renpy.pause(1)
        scene ch6sc10_244a with dissolve
        zy "Ahh…"
        "Zyra is pleased you dared to suck her nipple in front of Suji, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."


    else:
        scene black with dissolve

    scene ch6sc10_245 with dissolve
    sj "There we go! All done! That’s much better!"
    mc "Girls… why do I feel naked?"
    sj "*Giggles* Oh please, we didn’t take off that much."
    sj "Right Zyra-"
    scene ch6sc10_246 with dissolve
    with vpunch
    sj "Zyra! Why is your tit out!"
    zy "*Snickers* Oh? I didn’t even notice… how did that happen."
    sj "Yeah right… you were pressing him against your breasts the whole time…"
    sj "P-Put it away before we untie his blindfold!"
    scene ch6sc10_247 with dissolve
    zy "There, happy?"
    sj "Mh-Hm. Here you go [mc]."
    scene ch6sc10_248 with dissolve
    mc "So… what’s the verdict?"
    sj "You look like a new man! Reborn as our A’khan."
    sj "I like it, and no, I do not say that just because I was the one who cut it."
    scene ch6sc10_249 with dissolve
    sj "It goes really well with your stubble."
    sj "I’m going to go check if they are ready for you."
    scene ch6sc10_250 with dissolve
    mc "Ready for me?"
    sj "Yes, you have an audience planned, to determine what happens to our two captives."
    "Suji leaves her hut, leaving you and Zyra alone."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0

    if zy_path == True:
        scene ch6sc10_251 with Dissolve(1.5)
        zy "She’s right, you know?"
        zy "You look mighty handsome with this haircut."
        mc "I don’t know… it feels a little short-"
        scene ch6sc10_252 with dissolve
        with vpunch
        "Zyra pushes you back against the support beam, tracing her nails across your abs while she presses the other hand onto your crotch."
        zy "Lock your hands behind the beam."
        mc "Zyra what are you-"
        scene ch6sc10_253 with dissolve
        "As she slides her hand down into your pants, you comply with her command."
        zy "If you do not believe my words when I tell you how handsome you are…"
        zy "Then I will speak with my body."
        scene ch6sc10_254 with dissolve
        zy "Do you hear me, [mc]?"
        mc "Mmh… I’m hearing something…"
        zy "You really think you could get away with letting me breed you last night and not… follow through in the morning?"
        scene ch6sc10_255 with dissolve
        "Zyra begins to slide herself down your body, with your leg between hers, you feel her soaked through her panties-"
        "-She begins to kiss your nipple while she gently squeezes your cock."
        zy "Do you hear me, [mc]? Do you hear how attractive I find you with your new hairstyle?"
        mc "You’re getting louder- Ahh…"
        scene ch6sc10_256 with dissolve
        zy "Louder huh? I better make sure you hear me without any doubts… Mmmh."
        zy "Since I told you to keep your hands locked, I’ll do the same. Just my wet mouth against your heroic spear."
        mc "Mmh… let's see if you can defeat me with that little mouth of yours."
        scene ch6sc10_257 with dissolve
        zy "*Licks* Mmmh… I can’t believe I didn’t have time to taste you last night…"
        zy "Your spear is so delicious… so warm… so hard… just for me. *Licks*"
        scene ch6sc10_258 with dissolve
        mc "*Moans* Mmgh… that’s a naughty little tongue you have… fuck…"
        zy "Do you remember this feeling? Does it feel as good as last time, when I first sucked you during yours and Vex’s hunt?"
        scene zy_lewd10 with dissolve
        $ renpy.pause()
        mc "Ahh… no, it feels better… Mmh… you’re more eager this time, not as timid."
        zy "That time was my first time… now, now there’s no reason to hold back any longer…"
        zy "*Sucks* You’re my A’khan, my lover, my hunter… but today, I’m hunting you. *Sucks*"
        mc "Mmgh! You’re my naughty little huntress, and I love how you wield your mouth like a proper weapon."
        with vpunch
        mc "Fuck- Zyra… the way your lips are keeping a tight hold on my cock while your tongue rubs all the way in and out- {b}Mgh!!{/b}"
        with vpunch
        zy "{b}Unleash your desire into my mouth!{/b} Fill me! Let me savor the taste of your seed!"
        with vpunch
        "Zyra continues to eagerly suck you with a ferocious appetite as you begin to shoot load after load down her throat."
        scene ch6sc10_259 with dissolve
        with vpunch
        $ renpy.pause(1)
        with vpunch
        mc "{b}Fuck! Zyra- AhhH!!{/b}"
        scene ch6sc10_260 with dissolve
        with vpunch
        zy "*Gasps* {b}AhHh! So much!! MMhh!{/b}"
        zy "Did you hear me, [mc]? Did you hear just how much I love your new hairstyle? *Licks*"
        mc "*Chuckles* Five hells… you know… I think this is my favorite hairstyle I’ve had. Period."
        "Zyra’s feelings for you have grown, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
        $ zy_trust += 5
        scene ch6sc10_261 with dissolve
        with vpunch
        sj "Hey are you two ready for the audience- {b}Aahhh!{/b}"
        sj "{b}I knew it!{/b} I knew you didn’t accidentally have your tit out earlier!"
        scene ch6sc10_262 with dissolve
        sj "*Snickers* You’re such a little slut, {b}Zyra!{/b}"
        zy "*Giggles* Someone had to show him how delicious he looks now."
        mc "This won’t be the last time I’ll let the two of you give me a haircut. *Chuckles*"
        sj "Glad you enjoyed it… now get dressed you two! People are gathering for your audience."
        sj "We need to get you cleaned up… you’re a total mess."
        zy "*Giggles* Okay… thank you for breakfast, [mc]."
        mc "*Chuckles* Thank you for the haircut. I’ll go ahead, see you girls at the audience."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        "A’nai not having an audience hall, you notice a gathering of the tribe near the duel platform in the training area."

    else:
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        "Upon Suji’s return, the three of you head out."

    scene ch6sc10_263 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    "As you make your way through the crowd of women, you notice Kisha standing atop of the platform, with one of the prisoners."
    mct "I see they’ve already brought out one of the prisoners for me to judge."
    scene ch6sc10_264 with dissolve
    ks "Sisters!"
    ks "Your A’khan has arrived to place his judgement upon these lowly men we have in our midst!"
    cwd "Kill them! Hang them from a tree! Bury them alive! Let them swim out at sea to feed the sharks!"
    scene ch6sc10_265 with dissolve
    ks "His will shall bring these filthy outsiders to justice!"
    cwd "Cheering!"
    scene ch6sc10_264 with dissolve
    ks "{b}His word!{/b}"
    scene ch6sc10_265 with dissolve
    cwd "{b}Our will!{/b}"
    scene ch6sc10_266 with dissolve
    ks "My A’khan, blessed be your morning."
    mc "Good morning Kisha, I see we’re starting out wasting no time?"
    ks "The stage is all yours. We trust in your judgement."
    scene ch6sc10_267 with dissolve
    with vpunch
    ed "Bastard! Brainwashing and kidnapping my sweet Kelly wasn’t enough?!"
    ed "Now you’ve done the same to a whole tribe of women! You’re nothing but a dirty bastard who will be hanged for treason!"
    mc "Lord Edward… pleasure as usual."
    scene ch6sc10_268 with dissolve
    with vpunch
    ed "Bastard! Just wait til I get back to Luxenford and tell everyone what you’ve been up to!"
    "Kisha, visibly upset at the mans remarks, looks to you for your judgement."
    mct "I’ve just about had it with him and his stupidity."
    mct "If I were here alone with him, I’d snap his neck in a heartbeat… yet, none here would blink if I sentenced him to death."
    mct "He’s Kelly’s father… but last I spoke with her, she had no love for him or interest in ever seeing him again."
    mct "Getting rid of him, permanently, seems like the best option. Especially since he just threatened to-"
    mct "Reveal everything here to the outside world, that’s something I can’t allow to have happen."
    mct "So, that leaves me with two options… keep him locked up as a prisoner here, or… end his miserable existence."
    ####Choice####
    menu:
        "Keep Lord Edward as a prisoner of war. ({color=#87e1fa}Light Path{/color})":
            scene ch6sc10_269 with dissolve
            mc "Kisha, we’ll spare his life… for now."
            $ light += 2
            mc "Escort Lord Edward to the cells, he can be of value to us down the line as a potential hostage."
            scene ch6sc10_270 with dissolve
            ks "As you command, my A’khan."
            ks "I shall choose a cell most fitting for his behavior."
            "You chose to spare Lord Edward despite his threats, your {color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            "You nod, and Kisha removes Lord Edward from the stage."
            scene black with Dissolve(1.5)
            $ renpy.pause(0.5)
            "After a while Kisha returns to the stage with the next prisoner, the man that was held captive at Arugoh."

        "Have Kisha execute Lord Edward. ({color=#f00}Dark Path{/color})":
            scene ch6sc10_269 with dissolve
            mc "Execute him."
            scene ch6sc10_268 with dissolve
            "Kisha nods in agreement."
            $ dark += 2
            ed "{b}WHAT?!{/b} You bastar-"
            scene ch6sc10_271
            with vpunch
            "With zero hesitation, Kisha pierces the back of his skull with her spear, thrusting it straight through."
            $ ed_alive = False
            mc "Well done, I was getting tired of his yapping."
            scene ch6sc10_269 with dissolve
            mc "Remove his corpse before he stains our stage."
            scene ch6sc10_270 with dissolve
            ks "Yes, my A’khan."
            ks "I shall bring the next prisoner out for you to judge as well."
            "You chose to excute Lord Edward for his crimes, your {color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            $ renpy.pause(0.5)
            "After a while Kisha returns to the stage with the next prisoner, the man that was held captive at Arugoh."

    scene ch6sc10_272 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "Right… this guy."
    ks "Here’s our last order of business for today."
    scene ch6sc10_273 with dissolve
    ks "A captive from Orianna’s crew, who’s been kept alive at the mercy of the Arugoh tribe."
    ks "What is your judgement, regarding this outsider… this… man."
    scene ch6sc10_274 with dissolve
    uk "Please! Spare me good sir!"
    uk "I-... I won’t tell anyone about this place! About what I’ve seen! I swear it on me life!"
    mct "Hmm, this one is tricky."
    mct "He was a steward on Orianna’s crew before they shipwrecked here and got captured."
    mct "But who’s to say being held captive here hasn’t caused wear and tear on his mind? Caused him to build resentment?"
    mct "If I let him go, it could appease Orianna and my alliance with her… but it is a risk."
    mct "He could be playing us for fools and as soon as he gets on the mainland, spread the word about A’nai."
    mct "If that were to happen… I’d have let them all down, my people… my safe haven…"
    scene ch6sc10_273 with dissolve
    ks "What is your judgement my A'khan?"
    ####Choice####
    menu:
        "Allow the man to be released as Orianna’s steward. ({color=#87e1fa}Light Path{/color})":
            scene ch6sc10_274 with dissolve
            mc "This man was a steward under Orianna’s command, we will let him resume his duties as such."
            $ ori_captive = True
            uk "T-Thank you! Oh thank you good sir!"
            "You chose to spare Orianna's steward to earn her favor, your {color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch6sc10_273 with dissolve
            $ light += 2
            ks "I do not think it a wise choice, but your command is my will."
            mc "Keep him in a cell until we depart from A’nai. I don’t want him walking around freely."
            ks "Wise decision, my A’khan. He will be released upon Orianna’s departure from A’nai."

        "Execute him, I won’t take any chances on an unknown captive. ({color=#f00}Dark Path{/color})":
            scene ch6sc10_273 with dissolve
            mc "Execute him. We will not allow any outsiders, men especially, to leave A’nai with the knowledge to tell the world about us."
            scene ch6sc10_274 with dissolve
            with vpunch
            uk "{b}WHAT?!{/b} No! {b}PLEASE!{/b}"
            $ ks_trust += 3
            scene ch6sc10_275 with dissolve
            with vpunch
            "In one swift motion, Kisha slices the man’s throat with the tip of her spear."
            $ ori_captive = False
            "You chose to excute Orianna's steward in cold blood, your {color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch6sc10_276 with dissolve
            mc "Well done, my sweet Kisha."
            $ dark += 2
            mc "You serve me without hesitation, something I value highly."
            "Kisha enjoys the embrace of your palm and nods at you, smiling."
            "Kisha feels proud to have served you well, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            mc "Go, I’ll make sure to reward you later."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "As the audience concludes, a huntress comes up to you, requesting you meet Echo and Orianna in your chambers."
    scene ch6sc10_277 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    "As you arrive in your chamber, you notice Echo and Orianna looking at maps."
    "As you approach them, you hear they are discussing the ship repairs to your ship."
    scene ch6sc10_278 with dissolve
    ec "So, the repairs on [mc]’s ship are almost complete?"
    ori "Correct, the women I put on it just returned, they say it's basically ready and just need to wait for the rising tide tonight."
    mc "Hey ladies. Sounds like everything is going well with the ship?"
    scene ch6sc10_279 with dissolve
    ec "[mc]! Yes, come join us!"
    ori "As Echo said, please join us, we have much to discuss."

    if ec_relationship == True:
        scene ch6sc10_280 with dissolve
        mc "Just a moment, Ori. I need to take in my gorgeous wife…"
        ec "*Giggles* Stop it… we have a guest present!"
        "Echo loves that you aren’t afraid to flirt with her in front of others."
        scene ch6sc10_281 with dissolve
        mc "Right, so what do you have for me, Ori?"

    else:
        scene ch6sc10_281 with dissolve
        mc "Alright, what do you have for me?"


    ori "I’ve got great news!"
    scene ch6sc10_282 with dissolve
    ori "The women I appointed to do repairs on your ship have reported that it is ready to set sail."
    ori "We just have to wait for the tide coming in tonight and we can finally go home."
    ec "..."
    mc "Echo? What is it?"
    scene ch6sc10_283 with dissolve
    mct "Reality is starting to set in for her, that I will be leaving soon."
    ec "*Sniffles* …"
    mc "Hey… it’s going to be alri-"
    scene ch6sc10_284 with dissolve
    with vpunch
    "Echo desperately hugs you and wraps her arms around your neck tightly, her whole body is shaking."
    mc "Echo… we’ve talked about this. You knew I was going to have to return to the mainland."
    ec "Ngh-nhh…"
    mc "You know I will come visit, you’re my A'nu, and the women of A’nai are my people now."
    scene ch6sc10_285 with dissolve
    ec "......."
    mc "I know this is sooner than you had hoped, honestly I would love to stay longer and really dive into your culture."
    mc "But you know that I have loved ones back home who care for me just as you do."
    scene ch6sc10_284 with dissolve
    ec "Mmmh."
    mc "We made a promise, remember?"
    ec "*Nods*"
    scene ch6sc10_285 with dissolve
    mc "You’re going to come visit me when things here settle down."
    mc "And I’ll take you to my favorite place with the apple trees."
    scene ch6sc10_284 with dissolve
    ec "*Nods gently*"
    mc "Look at me, there’s something I have to tell you. Something that will ease your mind."
    scene ch6sc10_283 with dissolve
    "Reluctantly she releases her arms from your neck and steps back."
    mc "Listen…"
    scene ch6sc10_286 with dissolve
    mc "When I met with Maia, she gave me more than just the communion stone."
    "Echo’s face lights up, she listens attentively."
    mc "She gifted me the ability to produce a Dimension Door, to create a portal."
    scene ch6sc10_287 with dissolve
    ec "A portal? One you can travel through?"
    scene ch6sc10_286 with dissolve
    mc "Yes, that is the purpose of portals."
    mc "It’s a specific kind of portal, it is tied to the infused shrine I created here."
    scene ch6sc10_287 with dissolve
    ec "Oh, I see. How does it work?"
    scene ch6sc10_286 with dissolve
    mc "At the cost of a significant amount of mana, I can create a portal that links from wherever I am, directly to A’nai."
    mc "So, that means…"
    scene ch6sc10_287 with dissolve
    ec "That means!"
    scene ch6sc10_288 with dissolve
    ec "You can visit us freely?!"
    ec "That you won’t be bound by weeks at sea to reach us!"
    mc "Exactly, even if I’m halfway across the world, I can reach you instantly."
    ec "I’ll go tell the others at once!"
    scene ch6sc10_289 with dissolve
    ec "A great deal of them have been distraught since they learned that you were leaving."
    ec "Ori, you’re free to discuss what you need with [mc]."
    ori "Sounds good, your A'khan will be in good hands."
    scene ch6sc10_290 with dissolve
    ori "Alone at last… you’re a busy man."
    mc "Been hoping to get me alone?"
    ori "*Snickers* Mhm-Hm."
    scene ch6sc10_291 with dissolve
    ori "Going by these maps we’ve scavenged from shipwrecks, Looter’s Bay should be about 2 days at sea from here."
    ori "We’ll be spending quite a bit of time together…"
    scene ch6sc10_292 with dissolve
    mc "Yeah, being confined to a ship together has a way of getting people to know one another."
    ori "*Giggles softly*"
    scene ch6sc10_293 with dissolve
    ori "Are you saying you’re hoping to get to know me better?"
    scene ch6sc10_292 with dissolve
    mc "Yeah, I am."
    scene ch6sc10_293 with dissolve
    ori "Oh? I suppose it doesn’t sound horrible to spend a little time with the man who rescued me. *Giggles*"

    if ori_captive == True:
        scene ch6sc10_295 with dissolve
        ori "I was watching your audience from up here… I saw how you spared my steward even though you didn’t have to."
        ori "You’re a man… a real man."
        "Orianna is pleased you spared her stewards life, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
        $ ori_trust += 3
        scene ch6sc10_296 with dissolve
        ori "You care about people, you protect them, you rescue them… you rescued me."
        ori "I can’t help but feel extremely… thankful."
        scene ch6sc10_297 with dissolve
        ori "How will I ever find a way to thank you…"
        mc "I’m sure you’ll find a way to show me."
        scene ch6sc10_298 with dissolve
        ori "You know… I think you might be right…"
        scene ch6sc10_299 with dissolve
        ori "Mmmh…."
        "Just before her lips meet yours she gently tilts your head and plants her shapely exotic lips half on yours and half on your cheek."
        scene ch6sc10_298 with dissolve
        ori "I think a few days at sea with such a handsome man will give me plenty of ideas on how to show my appreciation."
        mc "I look forward to seeing what you come up with."
        scene ch6sc10_297 with dissolve
        ori "*Snickers* I bet you do."
        ori "I’m going to go tell your companions that we’re setting sail tonight."
        mc "Sound good, I’m just going to rest up a bit."
        scene ch6sc10_294 with dissolve
        ori "As you should, Captain."
        ori "See you tonight, handsome."
        mc "I’ll see you tonight, Ori."

    else:
        scene ch6sc10_291 with dissolve
        ori "I watched your audience from up here... you... you killed my steward."
        "Orianna is in disblief over your decision, her trust has decreased by {size=+3}{b}{color=#f00}3{/color}{/b}{/size}."
        mc "Ori... I couldn't risk letting him live, he's spent weeks in the Arugoh dungeons."
        ori "*Sighs* I know... still, I do not believe you should have chosen to execute an innocent man."
        $ ori_trust -= 3
        scene ch6sc10_294 with dissolve
        ori "Playing judge, jury and executioner never ends well, keep that in mind going forward."
        ori "I’ll go inform your companions that we’re leaving tonight."
        ori "Until then, Captain."
        mc "Sounds good, I’ll see you tonight."
        mct "That went about as well as I imagined, she was upset as expected but..."
        mct "It had to be done, I vowed to everyone that I wasn't going to let the past repeat."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc10_300 with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    mct "*Sighs* A few days at sea… and then we’ll be at Looter’s Bay, setting Kira and Kelly free."
    mct "I’ll hand over Orianna to Diana, let her deal with the politics and I’ll run across the sea back to Luxenford."
    mct "I haven’t been able to reach Eliza through the Arcano crystal… I’m sure it's nothing but it's keeping me on edge."
    mct "She has it on her, I can sense her vital signs, she's healthy but... her pulse is low."
    mct "Lucid said if a vampire doesn't drink blood regularly, they'll desiccate, going into a sort of slumber."
    mct "That's probably what is happening, her body is going into a suspended sleep state until she is fed blood."
    scene ch6sc10_301 with dissolve
    mct "Hmh?"
    mct "That’s-..."
    scene ch6sc10_302 with dissolve
    mct "One of Maia’s portals?"
    mct "I guess she wishes to speak to me, she probably felt that I finished the shrine and restored their connection."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss53 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_303 with Dissolve(2.5)
    play music relax_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch6sc10_304 with Dissolve(2.5)
    $ renpy.pause(0.5)
    "As you arrive through Maia’s portal, you immediately notice this isn’t her usual garden you’ve been at."
    "The atmosphere is warm, almost like you’re being embraced with a warm blanket after a cold swim."
    scene ch6sc10_305 with dissolve
    mct "There she is."
    mct "I wonder why she wanted to see me again so soon?"
    mct "Not that I have any objections… I enjoy being near her."
    scene ch6sc10_306 with dissolve
    mct "The water in that basin is definitely enchanted, not just due to its pinkish color but I can feel it teeming with magic."
    mc "Maia, hey… what’s going on?"
    scene ch6sc10_307 with dissolve
    "Upon hearing you, she gently turns towards you."
    scene maia2 with dissolve
    $ renpy.pause(9.6, hard=True)
    scene ch6sc10_308
    $ renpy.pause(0.5)
    "A warm smile surfaces as she sees you, she gently beckons you closer with her hand."
    mai "Join me? My sweetling."

    if mai_relationship == True:
        scene ch6sc10_309 with dissolve
        mc "Beautiful as ever I see."
        mai "..."
        "You slide your hand down her smooth forearm and into hers."
        scene ch6sc10_310 with dissolve
        "As you rest the surface of your hand against her soft thigh, the two of you attentively caress each other's fingers."
        mc "Missed me already?"
        scene ch6sc10_309 with dissolve
        mai "*Nods* …"
        mc "I missed you too."

    else:
        scene ch6sc10_309 with dissolve
        mc "So…"

    mc "I have a feeling you didn’t summon me just because you missed me though?"
    scene ch6sc10_311 with dissolve
    mai "Your intuition is as always, impeccable."
    mai "But no, you aren’t here just because I missed you…"
    scene ch6sc10_312 with dissolve
    mc "I actually had a few things I’d like to ask you as well, nothing major just some stuff I’m curious about."
    mai "Oh? Then you go first, what I wish to discuss is a more… in-depth topic."
    scene ch6sc10_313 with dissolve
    mai "Ask me anything, my sweet."
    mc "Okay, firstly I was wondering if you knew what is going on at Aruna? When I first arrived I felt my abilities diminished."
    mc "But gradually they returned and now I feel normal?"
    scene ch6sc10_314 with dissolve
    mai "I do not know the source of this magic dampener."
    mai "But it is likely to have affected you initially due to being a new experience to your body."
    scene ch6sc10_313 with dissolve
    mai "But due to the nature of what you are, your body likely adapted to the dampening and overcame it gradually."
    mc "I see… how come it's ineffective against me?"
    scene ch6sc10_314 with dissolve
    mai "I’m sure you’re already aware, your magic is not the same as what a mage would wield."
    scene ch6sc10_315 with dissolve
    mai "Yes, you can wield the magic of mortals, rather easily as I’m sure you’ve discovered by now."
    mai "However, that is not the same as the magic that flows through your veins, that exist in each and every cell within your body."
    scene ch6sc10_316 with dissolve
    mc "I never really thought about it like that, so the dampener was most likely placed on the island to affect mortals?"
    scene ch6sc10_315 with dissolve
    mai "That is what I would assume, for what purpose I do not know."
    scene ch6sc10_316 with dissolve
    mc "This is also why Riven and Kisha with yours and Gaia’s blessings can wield their magic despite the dampener?"
    scene ch6sc10_315 with dissolve
    mai "Correct, our blessings as you know are soul-magic, too powerful for the dampener to affect."
    scene ch6sc10_313 with dissolve
    mc "Okay, my second question is about the mist that seems to change the jungle at random?"
    mai "Gaia’s creation."
    scene ch6sc10_314 with dissolve
    mai "She created it long ago as a protection to the people that reside on the island."
    scene ch6sc10_313 with dissolve
    mc "It is definitely effective, but… it also inhibits them to some degree."
    mai "[mc], we are deities, all things must have balance."
    scene ch6sc10_314 with dissolve
    mai "Especially in nature, which is Gaia’s domain."
    scene ch6sc10_315 with dissolve
    mai "Nature does not discriminate or take sides, nature isn’t good, nor is it evil."
    mai "It just… is."
    scene ch6sc10_316 with dissolve
    mc "Honestly, it's something I enjoy about nature, so I’m not going to complain about that."
    mc "Besides, the people living on the island have done pretty well at adapting to it over the years."
    scene ch6sc10_315 with dissolve
    mai "You care a great deal about them, don’t you?"
    mc "Mhm. I do."
    scene ch6sc10_317 with dissolve
    mai "They’re your people now, my sweet."
    mai "Your very own followers."
    scene ch6sc10_313 with dissolve
    mc "I’ll do anything to protect them."
    mai "That is one of the great many values that you have, which I find so endearing."
    mai "Once you care about someone or something, you will protect it at any cost."
    scene ch6sc10_314 with dissolve
    mai "Do you have any other questions before we proceed?"
    scene ch6sc10_313 with dissolve
    mc "Just one for now, it’s one that should be right up your alley."
    mc "I passed your trial of fertility, but I’ve never gotten anyone pregnant? That I know of…"
    mai "*Giggles softly* …"
    scene ch6sc10_317 with dissolve
    mai "You wish to talk to me about… getting other women pregnant?"
    scene ch6sc10_313 with dissolve
    mai "*Giggles* …"
    mc "Well, you are the goddess of fertility. So even if it's a little awkward, could you help me come to understand it?"
    scene ch6sc10_314 with dissolve
    mai "Of course, I don’t mind."
    mai "The reason is both simple and complicated."
    scene ch6sc10_315 with dissolve
    mai "You aren’t able to impregnate a mortal female."
    mai "Have you ever wondered why women are eager for your seed?"
    scene ch6sc10_316 with dissolve
    mc "Well, not really?"
    mai "*Snickers* …"
    scene ch6sc10_317 with dissolve
    mai "Your seed is filled with magic, it makes it taste incredible, and it will feel incredible when released inside a woman."
    mai "However, all this magic seeping into your seed also changes its ability to impregnate mortals."
    scene ch6sc10_315 with dissolve
    mai "Their bodies cannot accept it as ‘natural’ and therefore it won’t take hold."
    scene ch6sc10_314 with dissolve
    mai "But… this won’t always be the case."
    scene ch6sc10_313 with dissolve
    mc "Hmm? How come?"
    mai "In the future, when you gain further mastery over your own abilities and magic-control."
    mai "You will be able to stop your magic from seeping into your seed, thus it simply becomes normal, able to impregnate a mortal."
    mc "That means I could control whenever I would want to impregnate someone or not?"
    scene ch6sc10_314 with dissolve
    mai "Yes sweetie, you would have full control."
    mai "But it will be quite awhile before you’re that adept at managing your magic to that level."
    scene ch6sc10_315 with dissolve
    mai "Magic-control that precise is very difficult and could take a lot of training."
    scene ch6sc10_317 with dissolve
    mai "Does that answer all your questions, honey?"
    scene ch6sc10_318 with dissolve
    mc "Yeah, thank you for taking the time to answer them."
    mc "I know you didn’t call upon me to do so, so I appreciate it."
    scene ch6sc10_317 with dissolve
    mai "Don’t be silly, we are not in a rush today… I’m happy to discuss anything you’d like."
    scene ch6sc10_318 with dissolve
    mc "Great, I’ll let you know if I think of anything else."
    scene ch6sc10_313 with dissolve
    mc "Now, what caused you to summon me?"
    mc "You said it was ‘in-depth’?"
    mai "*Sighs heavily* …"
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    mai "It’s-... it’s nothing. Let us forget about it."
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0

    if mai_relationship == True:
        scene ch6sc10_319 with dissolve
        mc "Hey… I’m right here."
        mc "I’m not going to push you to talk about it, but I’m here to listen whenever you’re ready."
        mai "Sweetie… mmh."
        scene ch6sc10_320 with dissolve
        mai "*Sighs* [mc]... thank you, but I’m just postponing the inevitable…"
        mai "I brought you here today to discuss it, so I will."
        mct "Whatever it is that she wish to talk to me about, it's clearly deeply affecting her."
        mc "I have an idea, come. Join me at the balcony."
        $ soulbinding = True
        scene ch6sc10_321 with dissolve
        "You keep your arms wrapped around her as the two of you make your way to the railing of her terrace."
        mai "What are we looking at?"
        mc "Whatever you like, the skies, the sun, the ocean of blue above the clouds, the mountains below us."
        scene ch6sc10_322 with dissolve
        mc "Looking at me while discussing whatever it is is clearly hard on you."
        mc "So instead, I’m just going to hold you while you look at something else."
        scene ch6sc10_323 with dissolve
        mai "[mc]-... that’s…. that’s really thoughtful of you."
        mai "*Inhales* Okay, I can do this."
        mai "With your arms around me, I feel invincible."
        mc "You are."
        scene ch6sc10_324 with dissolve
        mai "Very well then."
        "With you caressing her forearm and stomach, she finds the comfort and strength to tell you."
        scene ch6sc10_325 with dissolve
        mai "Remember how we previously discussed our soulbinding and that it was shattered?"
        scene ch6sc10_326 with dissolve
        mc "Mhm, and that my father was the one who shattered it."
        mai "Yes…"
        scene ch6sc10_324 with dissolve
        mai "That is why I summoned you here today, I had accepted that we would never get to experience our soulbinding."
        mai "But my sisters, Gaia and Malanthe… they recently approached me, with an idea… it’s far-fetched really."
        scene ch6sc10_325 with dissolve
        mai "But they seem to think that we can possibly restore our soulbinding."
        mai "They believe if all three of us pour our essence into the soulbinding, we can rebuild it from scratch."
        scene ch6sc10_326 with dissolve
        mc "All three of you?"
        mc "I thought a soulbinding was like marriage between gods?"
        mc "Something very… intimate?"
        mai "It is… why do you think I have a hard time broaching this subject with you?"
        scene ch6sc10_324 with dissolve
        mai "I’m not pleased with the idea of being in a threeway marriage, but…"
        mai "They made some excellent points in favor of it."
        scene ch6sc10_326 with dissolve
        mc "I’m all ears, to have you even slightly considering this… it must’ve been some strong points."
        scene ch6sc10_327 with dissolve
        mai "It was."
        mai "They believe if we create this new threeway soulbinding, something which has never been attempted before…"
        scene ch6sc10_324 with dissolve
        mai "That we’ll create something quite powerful, and with it being linked to you, it would grow in strength as you do."
        mai "Which means eventually, nobody, not even your father could sunder it."
        scene ch6sc10_325 with dissolve
        mai "Gaia and Malanthe have been very impressed by your actions as their champion."
        mai "They want a chance, a proper chance to get to know you personally."
        scene ch6sc10_326 with dissolve
        mc "Okay, sure… but I could just get to know them as is? I don’t need to essentially marry them to do that."
        mai "I know, but it is one of the reasons for them to want this."
        scene ch6sc10_327 with dissolve
        mai "However, even if you aren’t interested in them… it’s not like anything would be forced upon you."
        mai "You can deny their affections if you desire to do so and the soulbinding still holds."
        scene ch6sc10_326 with dissolve
        mc "Okay, that’s something at least. So the soulbinding at first is merely a bond between all of us and a title."
        mc "But it doesn’t mean that I ‘have’ to engage them in their desires?"
        scene ch6sc10_327 with dissolve
        mai "Exactly sweetling."
        mai "You need only do what you desire. You need only follow your heart, if you do that-"
        mai "Then none of us could be displeased with that."
        scene ch6sc10_324 with dissolve
        mai "Another point they made is that being connected to all three of us, will provide you with great options down the road."
        mai "Having three goddess instead of one watching over you could prove worthwhile."
        scene ch6sc10_325 with dissolve
        mai "Especially with what we know lies ahead of you in life."
        mai "You have many tough mountains to overcome."
        scene ch6sc10_326 with dissolve
        mc "*Sighs* Great…"
        mai "But we would love to help you manage them, help guide you, if you let us."
        scene ch6sc10_327 with dissolve
        mai "The greatness you’ve shown all of us whilst here on Aruna, we wish for that to continue throughout your life."
        mai "It has inspired Malanthe and Gaia to wish to commit themselves in a soulbinding with you."
        scene ch6sc10_326 with dissolve
        mai "As you know, that is an eternal commitment. No gods are capable of breaking a soulbinding."
        mc "Only one of the seven divines."
        scene ch6sc10_325 with dissolve
        mai "Correct, that’s how powerful these soulbindings are, and this one will be even more so."
        mct "Having three goddesses in my corner is certainly more than I dared hope for."
        mct "Just having Maia is already an incredible feat and I care about her deeply."
        mct "So if she can find the strength to even suggest this, it means she truly believes its the best course of action."
        mct "Even if she personally would’ve wanted me to herself."
        scene ch6sc10_326 with dissolve
        mai "[mc], what do you… what do you think?"
        mc "I think you’re one of the strongest women I’ve ever met."
        scene ch6sc10_327 with dissolve
        mai "T-Truly so?"
        mc "I’m glad you decided to tell me all of this. That you didn’t keep it from me, even though I know it must’ve been hard on you."
        mai "[mc]..."
        mc "I accept the threeway soulbinding."
        scene ch6sc10_328 with dissolve
        with vpunch
        mai "*Gasps* Sweetling!"
        mai "This is a big decision! It'll bind all four of us, for eternity."
        mc "I’m well aware, and I’ve made my choice."
        mc "I’ve longed for us to have that feeling back, that warmth I always felt, that I now only feel when near you."
        scene ch6sc10_329 with dissolve
        mai "Mhm… me too, but-"
        mc "No buts, I know how much our soulbinding meant to you, I want nothing more than for you to have that again."
        mc "I’m happy to accept Gaia and Malanthe to regain what we lost Maia."
        scene ch6sc10_330 with dissolve
        "Out of sheer joy, Maia kisses you with an intimacy that only she can provide."
        mai "Mmmh… mmh…"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_329 with dissolve
        play music relax_1 fadein 1.0
        #stop music fadeout 1.0
        mai "I love you, [mc]."
        mc "I love you too, my gorgeous goddess."
        mai "*Giggles* [mc]... my sweet, kiss me again."
        scene ch6sc10_330 with dissolve
        mai "MMgh-nngh… just like last time we let our lips merge… I cannot get enough of you."
        mc "Me neither… kissing you is electrifying."
        "Maia gently caresses the back of your head as she engages you passionately, resting herself against you."
        scene ch6sc10_329 with dissolve
        mai "My sweet boy… my sexy man…"
        mc "Sexy hmh? *Chuckles*"
        scene ch6sc10_331 with dissolve
        mai "Outrageously sexy… *Giggles softly*"
        mai "Come, my sweet."
        scene ch6sc10_332 with dissolve
        mc "What are you up to?"
        mai "*Giggles* You’ll see."
        scene ch6sc10_333 with dissolve
        "You notice Maia’s dress is starting to dissipate."
        mct "I love magic…"
        scene ch6sc10_334 with dissolve
        mai "Do you remember what I told you last time we were together?"
        mc "Vividly."
        scene ch6sc10_335 with dissolve
        mai "Undress yourself, my love. And join me in the water."
        mai "We have been patient… I desire to wait no longer."
        scene ch6sc10_336 with dissolve
        mc "Nothing can stop me from getting in that water with you."
        mai "*Giggles* Good… for I have an idea of how to initiate our soulbinding."
        scene ch6sc10_337 with dissolve
        mai "*Gasps softly* Oh… I see that I have been blessed."
        mai "Blessed to spend an eternity with a man so well… equipped."
        mc "You’re one to talk… just looking upon you, I know I’m the luckiest man to have walked on Midomir."
        scene ch6sc10_338 with dissolve
        mai "Mmmh… I’m pleased you feel this way, but your words won’t satisfy my needs today."
        mc "You’re right, the time for compliments is over, we already know how each other feel."
        mai "Mhm-hm… it’s time for us to become one, my sweet. As we were always meant to be."
        scene ch6sc10_339 with dissolve
        mc "Becoming one with you is something I’ve craved since I first met you… the craving has only magnified since then."
        mai "Mmh, reveal to me your purest desire, my love. And it will be yours."
        mc "I desire to know what it feels like to have my cock sucked by a goddess."
        scene ch6sc10_340 with dissolve
        mai "Such naughty words… yet, I cannot deny that I desire the same."
        mai "I’ve been longing to taste you."
        scene ch6sc10_341 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mai "*Kisses gently* Nnh… mmh… you’re so hard sweetie…"
        mai "MMgh… so hard and warm… so lively… mmh…"
        mc "Mmh… fuck… just as I expected… the tingling when we kiss and touch, also applies to this- Ahh…"
        scene mai_lewd4 with dissolve
        $ renpy.pause()
        "Enjoying the electric tingling between your cock and her wet lips, Maia intimately begins sucking you."
        mai "*Muffled* Mmh… simply delicious… *Licks* Mmhh…"
        mc "Fuck… I’m already ready to burst- Mmmh… keep moving your tongue like that."
        mai "I love sucking your cock sweetling- Mmmh… I love making you happy."
        mai "The goddess of purity... enjoying your big cock- mmhh... you like corrupting me my sweet?"
        mc "Fffhhh... I love corrupting you... mmhh... your mouth is magical."
        scene ch6sc10_340 with dissolve
        mai "Yum… what an incredible taste. *Giggles*"
        mc "That felt unbelievable… the energy between us is unmatched."
        mai "Sit down for me, I wish to try something."
        scene ch6sc10_342 with Dissolve(1.5)
        "As you sit down, Maia wraps her arms around you, pressing her naked body against yours."
        mai "*Moans* Aah… baby…"
        mai "You’re holding me so firmly… mmh, I’m highly sensitive you know?"
        mc "It can’t be helped… my desire for you is too strong to not hold on tight."
        scene ch6sc10_343 with dissolve
        mai "Mmh… *Kisses* such a lustful man you’ve grown up to be- *Kiss* Mmh… I like it."
        mai "I like how naughty you make me feel… I’ve never experienced such emotions."
        scene ch6sc10_342 with dissolve
        mc "Then it’s a good thing you’re mine now, I’ll make you feel all sorts of ways."
        mai "I-... mmh, I believe you."
        mai "I have something for you baby… something I know you enjoy very much… let me just-"
        scene ch6sc10_344 with dissolve
        "Maia adjusts herself while she remains on top of you."
        mc "Eager to breastfeed me again, are you?"
        "Maia nods excitedly."
        scene ch6sc10_345 with dissolve
        mai "Will you? I’d really like to."
        scene ch6sc10_344 with dissolve
        mc "I’ll never say no to you, especially when it comes to your breasts."
        scene ch6sc10_345 with dissolve
        mai "My sweet, you may begin."
        scene ch6sc10_346 with dissolve
        mai "*Moans softly* Aiih… g-gently honey… you know how- ahhh… how sensitive my breasts are."
        scene mai_lewd5 with dissolve
        $ renpy.pause()
        "You begin caressing her nipples with your tongue as you suck them gently."
        mc "Mmgh… you taste heavenly…"
        mai "Aahh… sweetie… just like that… keep sucking just like that- Mnnhhiiih…"
        "You feel her soft smooth thigh rest against your cock, pushing it back and forth as she enjoys breastfeeding you."
        mai "You make me so happy… you know that? Being in your arms… having you suck my breasts… mmmh…"
        mai "You’re stimulating both my breasts at once- Mmmh… such a good boy… mmhm…"
        mai "AahH… I can’t hold back my milk any longer… sweetling, do you want honey flavor like last time?"
        scene ch6sc10_346 with dissolve
        mc "Mmmh… *Licks* cherry, Nnhh… *Sucks*"
        scene ch6sc10_347 with dissolve
        mai "*Moans* Aiih… then cherry you shall have- Mmmh… just like that baby, keep licking my nipple."
        "You feel an increasing tingling rushing towards her nipple, as her breastmilk begins to flow."
        scene ch6sc10_348 with dissolve
        mai "*Moans intimately* Ohh-Aiih… my sweet, drink up."
        mc "Mmh… delicious, warm with sweetened cherry flavor."
        scene ch6sc10_349 with dissolve
        mai "*Moans* Ahhh… that’s it, my sweet boy… my handsome boy… drink up, don’t let any of my milk go to waste."
        mc "Mmh… never. This is too delicious to waste a single drop."
        scene ch6sc10_348 with dissolve
        mai "Ohh honey… you make me really happy when you breastfeed, you know that?"
        mai "Drink up, mmmh… drink as much as you desire."
        scene ch6sc10_349 with dissolve
        mai "Let your goddess feed you."
        scene ch6sc10_347 with dissolve
        mai "{color=#ff8cdd}*Melodic Gasps*{/color} {b}Aiiiyh!!{/b} Such a greedy boy… *Giggles softly* Drink up baby, drink up."
        "You suck her nipple intimately, making sure you get every last drop out of her delicious breast before you relent."
        scene ch6sc10_346 with dissolve
        mai "{color=#ff8cdd}{size=+10}{b}*Melodic Moans*{/b}{/size} Aahhhnhh… I feel like I’m levitatiiiiing…{/color}"
        mct "Mmh... I love listening to her moans, they're like a sweet melody of her pleasure."
        scene ch6sc10_344 with dissolve
        mc "Mmh, you are absolutely delicious."
        mc "My very own delicious and gorgeous goddess."
        scene ch6sc10_345 with dissolve
        mai "You’re so good to me, sweetie."
        mai "I’m all yours… in fact, I think it’s time you fully claim me, don’t you?"
        scene ch6sc10_346 with dissolve
        mc "*Kiss* Mmh… I do."
        mai "Then allow me to reposition myself- Ahhh…."
        scene ch6sc10_345 with dissolve
        mai "Naughty boy…"
        scene ch6sc10_343 with dissolve
        "Maia gently repositions herself, and she keeps herself slightly propped up, resting her juicy little lips on your tip."
        mai "MMmh… we’re about to initiate the soulbinding honey, are you still certain this is what you want?"
        mc "There weren’t any doubts in me before, and our intimacy has not allowed room for any doubt since then."
        mc "How will it work?"
        mai "When we… climax, together. Your… seed and my juices will contain a small amount of our essence."
        mai "You will absorb my essence and I will absorb yours, thus bonding us for eternity."
        scene ch6sc10_342 with dissolve
        mc "*Moans* Mmh… eternity sounds too short…"
        mai "*Moans softly* Nnnh… charmer… make love to me, sweetling?"
        mc "As you wish, Maia."
        scene mai_lewd6 with dissolve
        $ renpy.pause()
        "With your hands on her perky ass and smooth thigh, you help guide her as she pushes herself gently up and down."
        "Maia's lips teasingly grace yours with each moan as the two of you are becoming one."
        mai "{color=#ff8cdd}*Melodic Moans*{/color} Oohh-Ohhnnh… this is… oh… this is incredible…"
        mc "MMgh… it is… I’ve never felt anything it’s equal… the electrifying tingling our bodies create when we touch-"
        mc "-AhHh… is even more intense now that I’m inside you- Mmmh!"
        mai "We’re making love… Mmh… we’re finally making love- Aiiihh…"
        mai "I feel you baby… we’re one… nnngh… you’re so big- Ahhh…"
        scene mai_lewd7 with dissolve
        $ renpy.pause()
        "Completely in a state of blissful pleasure as you stretch her little wet pussy, she pushes you deeper."
        with vpunch
        mc "*Moans* Fuck- Mmgh! You’re tight- Ahhh… incredibly tight!"
        with vpunch
        mai "I feel it too! {b}Mm-Nngh! Yes baby!{/b} I love feeling you this deeply inside of me- {b}Aiiiyh!{/b}"
        mct "Mmmfffhh... I love feeling her breasts being squished against me like this as she's riding me..."
        with vpunch
        mai "I’m going to- Aiiih! Sweetling I’m going to come with you inside me!! {b}AhhHH!{/b}"
        with vpunch
        mc "*Moans* NNgh! Me too! The way you’re sucking onto my cock each time you press down- {b}Mmgh!{/b}"
        with vpunch
        mai "{color=#ff8cdd}{b}{size=+10}*Melodic moans*{/size} Fill me baby! Fill me with your seed! Aiiyhh-Ahh!{/b}{/color}"
        with vpunch
        "Maia's gentle and incredibly intimate riding as you're making love sucks every ounce of cum out of you."
        scene ch6sc10_350 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        mai "We’re one my love- Mmh! Do you feel it?"
        mc "Mmgh I do… my cum and your juices are intertwining… merging."
        mc "Mmgh… what a sensation."
        scene ch6sc10_351 with dissolve
        with vpunch
        mai "{color=#ff8cdd}{b}{size=+10}*Melodic moan*{/color}{/size} AaHh!{/b} It’s happening… Feel me sweetling, feel me become bound to you!"
        mai "Mmgh… we’re becoming soulbound- Ahhh…"
        "The most intense pleasure you’ve ever felt surges through your cock, as well as Maia’s pussy, your essences are being linked."
        with vpunch
        mc "{b}NNngh! I feel you- Mmmh!{/b}"
        $ maia_trust += 15
        "You've given Maia what she was longed for, she has fallen deeply in love with you, her trust has increased by {size=+3}{b}{color=#2bff8b}15{/color}{/b}{/size}."
        scene ch6sc10_352 with dissolve
        mai "*Giggles out of breath* We did it… we actually managed to create the soulbinding first try."
        mc "*Panting* Hnnh… I guess that just goes to show, we’re meant to be."
        scene ch6sc10_342 with dissolve
        mai "*Moans softly* I love you… so much."
        mc "As I love you, Maia. My little goddess."
        mai "Prove it! Mmh… by kissing me."
        scene ch6sc10_353 with dissolve
        "You don’t hesitate for even a second, you pull her close and embrace her soft tasty lips."
        scene ch6sc10_354 with dissolve
        "She passionately responds to your lips meeting by opening her mouth to you, inviting you inside with her wet tongue."
        scene ch6sc10_353 with dissolve
        "She completely intertwines herself with you, her thighs locked around your waist, her arms tightly wrapped around your neck."
        scene ch6sc10_354 with dissolve
        "As your lips remain connected and your tongues massage each other, she instinctively begins moving her waist again."
        scene ch6sc10_353 with dissolve
        mai "Mmmgh… my sweet… my love… my man. *Licks*"
        scene ch6sc10_354 with dissolve
        mc "My goddess… *Kiss* my woman… mmh…"
        scene ch6sc10_353 with dissolve
        mai "Make love to me again baby, I need to feel your seed within me once more.*Licks*"
        scene ch6sc10_354 with dissolve
        mai "[mc], let me ride you… let me blossom again… *Sucks lip* mmmh."
        mc "I wouldn’t dream of denying you anything."
        scene ch6sc10_355 with dissolve
        mai "Saying these things… you make me incredibly happy."
        mai "I’ve never felt happy like this, it’s such an intimate form of happiness. I feel fulfilled."
        scene ch6sc10_356 with dissolve
        mc "Mhm, I feel it too."
        mc "Being with you is quite overwhelming to all of my senses, in the best way possible."
        scene ch6sc10_355 with dissolve
        mai "How so, my sweet?"
        scene ch6sc10_356 with dissolve
        mc "My sense of touch, whether I’m touching you, or you’re touching me… it’s electrifying."
        mc "My sense of smell, whenever you’re near me and I get a whiff of your scent, I can’t help but become hard."
        scene ch6sc10_355 with dissolve
        mai "Oh my… *Giggles* I certainly feel that currently."
        scene ch6sc10_356 with dissolve
        mc "My sense of sight, whenever I look upon you, I feel mesmerized… like I’m looking upon the reason the word beauty was invented."
        mc "My sense of hearing, whenever you speak… your soft melodic voice calms my entire body."
        mc "Not to mention how your moans of pleasure sound."
        scene ch6sc10_355 with dissolve
        mai "Sweetie! *Giggles* You’re being naughty…"
        scene ch6sc10_356 with dissolve
        mc "Last but not least, my sense of taste, I’ve never tasted anything or anyone like you-"
        mc "-Your big soft lips tastes so enticing that I just want to keep kissing them."
        mc "Your perky, shapely breasts and small nipples taste heavenly, not to mention your breastmilk… Mmh."
        scene ch6sc10_355 with dissolve
        mai "Gosh! Honey… I felt you pulsate inside me when you thought about that… *Giggles softly*"
        mai "I love you, [mc]."
        scene ch6sc10_356 with dissolve
        mc "And I love you."
        scene ch6sc10_355 with dissolve
        mai "Let me make love to you my sweetling, just lean back and let me satisfy you."
        scene mai_lewd8 with dissolve
        $ renpy.pause()
        "She begins moving, pressing herself down onto you, deeper and faster paced than previously."
        "Her body is filled with desire, filled with lust and love… for you."
        mai "Oh sweetie… oh you’re so-... mmmh… so deep…"
        mc "MMgh… damn, Maia… mmh… you’ve had me inside you this entire time and yet you’re still so tight."
        mai "I know our waists are below water but- Aahh… can you feel how wet you make me?"
        mc "Mmgh… I can, your juices tingles all around my cock every time you press down on me- Mmmh fuck…"
        mai "I never want this feeling to end... the feeling of you inside of me..."
        mai "MMmhh! The feeling of us being one as fate would have us- Aah-Mmh!"
        with vpunch
        mai "You’re pulsating honey- Aiihh! come with me!"
        mai "I’m ready to blossom- Aiiih… I’m ready to feel our love being combined inside of {b}meee-ahh!!{/b}"
        with vpunch
        "Maia’s tight little pussy sucks itself firmly onto your cock, massaging you as she rides you while you begin to fill her up."
        scene ch6sc10_357 with dissolve
        with vpunch
        mai "{size=+10}{b}*Moans loudly* AHhHH!! AiiiHH!! BABY!! YES!! I FEEL YOU!{/b}{/size}"
        with vpunch
        mai "Y-Your cock is amazing!! {b}AiiihhH!!{/b}"
        mai "{b}I love it!{/b} I love your big, beautiful cock inside of me!! {b}AiiyhHH!{/b}"
        with vpunch
        scene ch6sc10_358 with dissolve
        "As the sensation of your combined orgasm begins to subside, she realizes what she just said."
        mai "*Shy* {b}{size=-10}Uh-Uhh… forget I said that!{/size}{/b}"
        mct "*Chuckles* We just made love twice and she is shy about admitting to liking my cock?"
        mct "I suppose she is the goddess of purity… and was a virgin until an hour ago, cute."
        mc "Hey… look at me."
        scene ch6sc10_359 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music relax_1 fadein 1.0
        #stop music fadeout 1.0
        mai "Mmhp…"
        "Maia timidly looks at you, her delicate hand slightly covering her face in embarrassment."
        mct "Heaven’s she’s cute…"
        mc "You’re my little goddess, aren’t you?"
        scene ch6sc10_360 with dissolve
        $ renpy.pause(0.5)
        scene ch6sc10_359 with dissolve
        mai "*Nods* Mmh."
        mc "We love each other very much, don’t we?"
        scene ch6sc10_360 with dissolve
        $ renpy.pause(0.5)
        scene ch6sc10_359 with dissolve
        mai "*Nods* Mmh."
        mc "You’re sitting with me deep inside you, whilst naked, in your very own bath, it's something you’ve desired for a long time isn’t it?"
        scene ch6sc10_360 with dissolve
        $ renpy.pause(0.5)
        scene ch6sc10_359 with dissolve
        mai "*Nods* Mmhhhh!"
        mc "Then you needn’t feel shy about admitting to liking it."
        scene ch6sc10_361 with dissolve
        mai "I know it’s silly… but didn’t you hear how I said it… I just blurted out that your {b}{size=-10}cock is amazing…{/size}{/b}"
        mai "It’s something a naughty and lewd maiden would say…"
        scene ch6sc10_342 with dissolve
        "You pull her close by grabbing her ass firmly."
        mai "*Gasps softly* Sweetling! Mmh!"
        mc "I like that I’m able to bring this side out of you."
        mc "After all, you are my naughty and lewd maiden."
        mai "Heavens… you really like it when I’m like this? You don’t think less of me?"
        mc "Kiss me and find out."
        scene ch6sc10_353 with dissolve
        "Maia eagerly unites her soft warm lips with yours, and her body calms immediately."
        scene ch6sc10_354 with dissolve
        mc "Mmh… feel that?"
        mc "That’s how much I’m loving both your pure, innocent side and your naughty side."
        mai "*Sucks lip* Mmh-nnh… I feel it… you are being honest with me… your lips could never lie to me."
        scene ch6sc10_353 with dissolve
        mc "Mmmh… if you keep moving like this… I can’t hold back."
        mai "Maybe I don’t wish for you to hold back… not with me… not ever. *Licks*"
        scene ch6sc10_354 with dissolve
        mai "*Whispers whilst kissing* {b}{size=-6}Fuck me, baby. Take me however you want… mmmh.{/size}{/b}"
        scene ch6sc10_353 with dissolve
        mc "Bend over at the edge of the bath..."
        mc "Mmh… I want to look upon that gorgeous ass of yours."
        scene ch6sc10_354 with dissolve
        mai "As my man desires, I will provide- Mmh… *Sucks gently*"
        scene ch6sc10_362 with Dissolve(1.5)
        "Maia leans over at the edge of the bath, propping up her ass for you to look upon."
        mai "Is this how you want me, sweetling?"
        scene ch6sc10_363 with dissolve
        mc "Your ass is perfection… just like your breasts… mmh."
        mc "Its soft yet firm, smooth yet perky."
        scene ch6sc10_362 with dissolve
        mai "*Giggles softly* Not only are you touching me so intimately… but I feel your cock resting on me… Mmh."
        scene ch6sc10_363 with dissolve
        mc "I look forward to being inside it… mmh… but that’s for another time, for now I’ll settle for your juicy pussy."
        "Maia let’s out a soft whimper at the thought of you being inside her ass."
        scene ch6sc10_362 with dissolve
        mai "Take me, baby… I want you deep inside me."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch6sc10_364 with dissolve
        with vpunch
        mai "*Squeals* {b}Aiiyyh! Baby!{/b}"
        scene ch6sc10_364a with dissolve
        mai "*Whimpers softly* Ohh… you’re… you’re so {color=#ff8cdd}{size=+10}{b}deep!{/b}{/size}{/color}"
        mai "{size=+10}{color=#ff8cdd}{b}*Melodic moan*{/color}{/size}{/b} Nnh-nnghhH! Sweetling! Nngh! {b}I'm yours!{/b}"
        scene ch6sc10_364 with dissolve
        mc "Mmh… there’s that warm tightness again… I love this little pussy of yours."
        scene ch6sc10_365 with dissolve
        mai "You love my little pussy? *Moans* Nnngh… I happen to love your hard cock as well!"
        mai "Fuck me sweetling! Make me yours again!"
        scene mai_lewd9 with dissolve
        $ renpy.pause()
        mai "*Moans* Ahh! Just like that! Take me just like that!"
        mc "Fuck… mmgh… seeing you like this while fucking you is incredible- Mmh!"
        mai "You enjoy seeing me bent over for you my love? Ahhh… I love the feeling of it… such a naughty position."
        scene mai_lewd10 with dissolve
        $ renpy.pause()
        mc "Mmh... I love seeing you bent over for me… gives me a great view and angle."
        mai "I love knowing your eyes are glued to my body-"
        mai "{b}Aiih! Harder baby! Fuck me harder!{/b}"
        scene mai_lewd11 with dissolve
        $ renpy.pause()
        "Hearing Maia beg you to be fucked harder, you decide to give her what she craves."
        with vpunch
        mai "{size=+10}{color=#ff8cdd}{b}*Moans loudly*{/size}{/b} Aiiyh-Aiih! This! is! Exactly! What! I! {b}Neeeeeded-AiiiHyhh!!{/b}{/color}"
        with vpunch
        mai "{b}I love you! I love your big cock! I love being taken from behind by you!! Aiiyhh! I’m coming!!{/b}"
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        $ renpy.pause(0.5)
        with vpunch
        mai "Ahh! AiiyhH! Yes! {b}YES!!!{/b} Don't stop! {b}DON'T STOP!!!{/b}"
        with vpunch
        mai "Grab my hips just like that! {b}Take my pussy!! AiiyHHH!!{/b} I'm going to bloom agaiN!!! {b}AHHH!!"
        mc "{b}Fuck! hnnghH! Me too! Brace yourself!{/b}"
        scene ch6sc10_366 with dissolve
        with vpunch
        "Maia filled with your cum and her juices forces your cock to slide out and the suction from her pussy pulls another load from you."
        with vpunch
        scene ch6sc10_367 with dissolve
        mc "*Moans* {b}AhhHh!{/b}"
        mai "*Panting softly* Mmmh… I feel you baby… I feel your essence within me and… covering my back."
        mc "Sorry about the mess… I didn’t plan on pulling out."
        mai "You’ve marked me… as yours. *Giggles softly* I love it."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_345 with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        mai "I can’t believe we just did that…"
        scene ch6sc10_344 with dissolve
        mc "What, you didn’t expect to be taken from behind when you summoned me here?"
        scene ch6sc10_345 with dissolve
        mai "*Snickers softly* Certainly not… I knew we would be making love… considering what happened last time."
        mai "But I couldn’t have imagined it would be like this… we’ve been so intimate, yet also so lustful."
        scene ch6sc10_344 with dissolve
        mc "I can’t help myself when I’m with you… as I mentioned, all my instincts are in overdrive near you."
        scene ch6sc10_345 with dissolve
        mai "As are mine… the way you described it earlier, made my heart skip quite a few beats. *Giggles*"
        mai "Submitting to you like that… letting you fill me and even cover me in your seed… I’ve become so lustful."
        scene ch6sc10_344 with dissolve
        mc "*Chuckles* I enjoy your lustful side, so don’t ever attempt to hide it from me."
        "Maia nods with a warm smile."
        mc "Speaking of covering you… what happened to my cum? We didn’t wash it off but it disappeared?"
        scene ch6sc10_345 with dissolve
        mai "I’m sure you can already tell this bath is enchanted."
        mai "I imbued the water to be cleansing and invigorating. So, your seed being a foreign substance, dissipates in the water."
        scene ch6sc10_344 with dissolve
        mc "Hmh, that’s clever."
        mc "And I definitely feel the invigorating effect as well, despite how we went at it-"
        mc "-I don’t feel exhausted in the slightest."
        scene ch6sc10_345 with dissolve
        mai "*Giggles* That was my intention behind the enchantment."
        mai "I don't know your endurance and I did certainly not intend to have it become a hinderance."
        scene ch6sc10_346 with dissolve
        mc "*Sucks gently* Oh yeah? Mmh…"
        mc "Such a naughty goddess I have married."
        mai "*Moans softly* Ohh… mmh.. baby… say it baby, I long to hear you say it."
        mc "*Sucks gently* Maia... my goddess... my {b}wife.{/b}"
        mai "{color=#ff8cdd}{b}*Melodic moans*{/size}{/b} Nnnhh-mmhh! My sweetling, my precious boy, my handsome lover, my... {b}husband.{/b}"
        scene ch6sc10_344 with dissolve
        mc "Speaking of my seed, earlier you were rather specific to point out I couldn’t get ‘mortals’ pregnant."
        mc "What about you then?"
        mc "Being a goddess, your body would be capable of accepting my seed, no?"
        scene ch6sc10_345 with dissolve
        mai "Mhm-hm, you’re putting two and two together."
        scene ch6sc10_368 with dissolve
        mai "Yes, your seed would easily take hold within me."
        mai "If I allow it to."
        scene ch6sc10_369 with dissolve
        mc "I see, so you can basically control whether or not to allow it to impregnate you?"
        scene ch6sc10_368 with dissolve
        mai "Correct, and you needn’t worry."
        mai "I have no intentions of allowing it to take hold, not yet."
        scene ch6sc10_369 with dissolve
        mc "*Chuckles* Are you saying that you have no faith in me as a father?"
        scene ch6sc10_370 with dissolve
        "You feel Maia’s delicate touch, caressing your chin."
        mai "That is not my reason."
        mai "I believe you will become a great father to our children, my love."
        scene ch6sc10_368 with dissolve
        mai "But I do not believe we are in a rush."
        mai "We have only just reunited and rebuilt our soulbinding."
        scene ch6sc10_370 with dissolve
        mai "We have so much to experience together, so much joy to provide each other before we make babies."
        scene ch6sc10_369 with dissolve
        mc "I couldn’t agree more."
        mc "With all that’s going on in my life currently, I don’t think I’d make a great father as of yet."
        scene ch6sc10_370 with dissolve
        mai "You would, trust me."
        scene ch6sc10_371 with dissolve
        mai "When we’re ready, we will shower our children with all the love they could wish for."
        mai "I dream of seeing our children run around in my gardens, playing in the water fountains, climbing the bushes"
        scene ch6sc10_369 with dissolve
        mc "Sounds amazing, I happen to think you would make an incredible mother."
        scene ch6sc10_368 with dissolve
        mai "You think so, my sweet?"
        scene ch6sc10_369 with dissolve
        mc "Mhm, having felt your presence when I was a kid, I know intimately how caring and loving you are."
        scene ch6sc10_370 with dissolve
        mai "There you go again, making my heart flutter as if I were a teenage girl. *Giggles*"
        scene ch6sc10_372 with dissolve
        mc "I was wondering, this talk about children… what would our children be? Would they be like me?"
        scene ch6sc10_371 with dissolve
        mai "Sort of, but not entirely."
        mai "They would be demigods."
        scene ch6sc10_372 with dissolve
        mc "Demigods?"
        scene ch6sc10_370 with dissolve
        mai "Yes, that is the definition for the offspring between gods, between gods and mortals, and such."
        mai "There’s various subsets of demigods, but they all have in common that at least one parent is a god."
        scene ch6sc10_369 with dissolve
        mc "I see… that means, I’m a demigod?"
        mai "Mhm-hm."
        scene ch6sc10_368 with dissolve
        mai "But unlike you, pretty much all demigods are born with some variation of their parent or parents powers."
        mai "But their power is static from birth, they don’t grow stronger or gain new abilities over time."
        scene ch6sc10_370 with dissolve
        mai "Which is what sets you apart from other demigods, Nephilim’s are the highest tier of demigods."
        mai "You are born with no powers, a blank slate, however… you continue to grow in all aspects throughout your life."
        scene ch6sc10_371 with dissolve
        mai "Which makes you incredibly unique, even gods and deities such as myself, our power is static."
        mai "Sure, we can acquire more souls up to a certain threshold, and that gives us temporary power."
        scene ch6sc10_372 with dissolve
        mc "While my power is dynamic, it keeps growing as I absorb souls or essences of living beings."
        mc "I’ve also felt myself getting stronger when I’m pushed to my limits and beyond."
        scene ch6sc10_370 with dissolve
        mai "It is certainly not how I recommend you to grow, pushing beyond your limits is dangerous."
        mai "But yes, that would cause your body to respond by getting stronger, faster, and durable."
        scene ch6sc10_371 with dissolve
        mai "Once you reach certain thresholds, you will undergo an Ascension."
        mai "It is not a direct power-up in and of itself, however it will allow your body to continue to reach new heights."
        scene ch6sc10_372 with dissolve
        mc "Hmm, so for a lack of a better analogy, if we say my body is a bucket of water."
        mc "Once the bucket is filled to the brim with water, it undergoes this ascension and becomes a bigger bucket?"
        scene ch6sc10_370 with dissolve
        mai "Exactly! A little simplification of the process but essentially that is the case."
        mai "You’ll become a bigger bucket capable of holding more water, i.e more power."
        scene ch6sc10_369 with dissolve
        mc "Will my body change?"
        scene ch6sc10_368 with dissolve
        mai "You’re very intuitive, sweetie. Yes, your body is likely to change."
        mai "How it changes or if it even changes at all is completely unknown."
        scene ch6sc10_371 with dissolve
        mai "Your change will be in accordance with the magic essences or souls you’ve absorbed."
        scene ch6sc10_372 with dissolve
        mc "So if I go around absorbing a bunch of elf souls I’ll grow elf ears?"
        scene ch6sc10_373 with dissolve
        with vpunch
        mai "*Giggles warmly* Heavens! Sweetling…"
        mai "Pretty much!"
        mc "*Chuckles* Good to know."
        scene ch6sc10_345 with dissolve
        mai "I love you, my sweet [mc]."
        scene ch6sc10_344 with dissolve
        mc "And I love you, my beautiful goddess."
        scene ch6sc10_345 with dissolve
        mai "Could you… prove it by kissing my nipple?"
        scene ch6sc10_346 with dissolve
        "Maia moans throughout her garden as you suck her nipple into your mouth, caressing it with your tongue."
        scene mai_lewd5 with dissolve
        mai "*Moans* Aahh… my sweet baby… mmh… I’m yours."
        mai "Keep sucking my breast- Nnhh… you’re so good to me honey."
        mc "*Sucks intimately* Mmh… your breasts are perfect for sucking… soft and shapely, small perky nipples."
        mai "*Moans softly* Ohhh my sweet… I’m gonna- Mmmh… here you go-"
        scene ch6sc10_348 with dissolve
        mai "{color=#ff8cdd}*Melodic whimpers*{/color} Drink up baby… mmmh… drink as much as you need."
        scene ch6sc10_349 with dissolve
        mc "Incredible… mmh…"
        mc "I could get used to this cherry-flavored milk… mmh."
        scene ch6sc10_348 with dissolve
        mai "AhhHh… you will have my milk and my breasts whenever you desire them."
        scene ch6sc10_347 with dissolve
        "You passionately suck the last drops of her delicious warm milk."
        scene ch6sc10_346 with dissolve
        mai "You make me so happy… Aahh."
        scene ch6sc10_345 with dissolve
        mai "*Giggles softly* Thank you sweetling. I really needed that."
        scene ch6sc10_344 with dissolve
        mc "You know better than to thank me for this, I love doing it for you."
        scene ch6sc10_343 with dissolve
        "She shifts herself on top of you, wrapping herself around you."
        mai "*Whispers softly* It’s time for us to get out, my love."
        mc "I have no desire to leave this bath, or you."
        mai "You must… you have to visit Gaia and Malanthe now, to complete the soulbinding."
        mc "*Sighs deeply* Fine… I suppose it’s important we get this completed properly."
        scene ch6sc10_353 with dissolve
        mai "*Kisses intimately* Mmgh… I already miss you, and you’re in my arms."
        scene ch6sc10_354 with dissolve
        mc "I’m already excited for our next time."
        mai "*Sucks lip gently* Mmh… me too, I can’t wait… {color=#ff8cdd}{b}I love you.{/b}{/color}"
        scene ch6sc10_353 with dissolve
        mc "I love you too, Maia."
        scene ch6sc10_355 with dissolve
        mai "Oh, before you go… now that we’re soulbound, you can utilize the dimension door I taught you to-"
        mai "-to visit me whenever you desire it."
        scene ch6sc10_356 with dissolve
        mc "Oh? Now I’m really glad we decided to restore our soulbinding."
        scene ch6sc10_355 with dissolve
        mai "Me too, we’re connected in a special way now, linked. We’ll always be able to feel each other."
        mai "My warmth will never disappear from you again."
        scene ch6sc10_356 with dissolve
        mc "Neither will my love for you. You will have to endure it for eternity."
        scene ch6sc10_355 with dissolve
        mai "I’ll only endure it if you kiss me, right now."
        scene ch6sc10_354 with dissolve
        mai "*Muffled moan* MMmh-nnh… my sweetling."
        scene ch6sc10_353 with dissolve
        mc "You’re making it hard to leave…"
        mai "I feel something else is hard as well… Mmh… I’m sorry sweetie, we must wait until next time."
        scene ch6sc10_342 with dissolve
        mc "Something to look forward to."
        mai "Definitely…"
        mai "Come, I’ll send you to Gaia."
        scene ch6sc10_355 with dissolve
        mai "Wait... before we part ways..."
        mai "I need to ask something of you, I know this might come difficult as you've grown close to a lot of good people."
        mai "But our soulbinding... our union, you should keep this between us."
        scene ch6sc10_356 with dissolve
        mc "You mean..."
        scene ch6sc10_355 with dissolve
        mai "For a while, you shouldn't tell anyone back home about this."
        mai "I know you trust them, I feel it in your heart... it's not a matter of trust."
        mai "Our soulbinding needs time to grow and mature, to solidfy and strengthen."
        scene ch6sc10_356 with dissolve
        mc "And if I go blabbing about it to everyone I know, it could put them in the crosshairs?"
        "Maia nods gently."
        scene ch6sc10_355 with dissolve
        mai "Firstly, what happens between us is a matter between deities, it does not concern mortals."
        mai "But more than that, as you said... they could become collateral damage if there's a fallout."

        if eliza_relationship == True:
            mai "I feel how deep your love runs for this girl... Eliza."
            mai "I feel within you a strong urge to share anything and everything with her."
            scene ch6sc10_356 with dissolve
            mc "*Exhales* But this is something I'll have to keep to myself for a while..."
            scene ch6sc10_355 with dissolve
            mai "I know it's a lot to ask... it would be best to hold off on telling her until after you've ascended."
            mai "Your ascension should strengthen our soulbinding sufficiently that we needn't worry."
            mai "Then you could potentially share it with her and others should you deem it necessary."
            scene ch6sc10_356 with dissolve
            "Maia looks at you lovingly for a few moments."
            scene ch6sc10_355 with dissolve
            mai "But I also know you... you might end up telling her, just by an impulsive subconscious act."
            mai "If that happens... I will not be angry with you, I'll do my best to keep it untraceable."
            mai "Just... I'm not all powerful, so if you do end up telling her or anyone, it's a risk."
        else:
            scene ch6sc10_356 with dissolve
            mc "I'll do my best Maia."
            "Maia looks at you lovingly for a few moments."
            scene ch6sc10_355 with dissolve
            mai "But I also know you... you might end up telling someone, just by an impulsive subconscious act."
            mai "If that happens... I will not be angry with you, I'll do my best to keep it untraceable."
            mai "Just... I'm not all powerful, so if you do end up telling her or anyone, it's a risk."

        scene ch6sc10_356 with dissolve
        mc "I know... I'll try to keep it to myself as best I can."
        mc "Now..."
        mc "I'm going to need another kiss before you send me off."
        "Maia giggles softly, clearly likes the sound of that."
        scene ch6sc10_356 with dissolve
        mai "You better kiss-"
        scene ch6sc10_353 with dissolve
        with vpunch
        "You pull Maia close and the two of you eagerly wrap yourselves together in another intimate embrace."
        mai "*Caresses tongue* Mmfh-mfhh! Mmgh! Mmhhhh... nnh..."
        scene ch6sc10_354 with dissolve
        mai "I love you [mc]."
        mc "I love you... Maia I- mmmh..."
        scene ch6sc10_353 with dissolve
        "Each lick of Maia's tongue cover yours with her cherry-tasting saliva."
        "You begin to doze off as she begins to send you off to see Gaia."

        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ss54 with Dissolve(1.5)
        $ renpy.pause()
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc03_325 with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        mct "There she is."
        scene ch6sc03_327 with dissolve
        mct "According to what Maia told me earlier."
        mct "I have a choice ahead of me, I can either accept Gaia’s and Malanthe’s part of the soulbinding as-"
        scene ch6sc03_328 with dissolve
        mct "-as a symbolic gesture and friendship, or with the intention of being it the real deal."
        mct "They have agreed to do it either way, although she did say they wish for it to be a romantic soulbinding."
        mct "They wish to experience falling in love, and they believe I am the one who can make them experience it."
        scene ch6sc03_329 with dissolve
        gai "My Champion, approach."
        scene ch6sc03_335 with dissolve
        mc "Hey Gaia, I’m sure you know why I’m here."
        "She nods gently."
        scene ch6sc03_337 with dissolve
        gai "You’ve made your decision then, my champion?"
        scene ch6sc03_338 with dissolve
        gai "You truly wish to bind yourself to us? To me?"
        gai "For all eternity?"
        scene ch6sc03_336 with dissolve
        mc "I do, if I said I’m doing it for you, I’d be lying… I’m doing this for Maia."
        mc "I don’t know you well enough, yet. However that is something I’d like to change, I have a good feeling about you."
        scene ch6sc03_337 with dissolve
        gai "You do? Oh that is… that is lovely to hear."
        scene ch6sc03_338 with dissolve
        gai "I share that feeling, [mc]. I too would like the chance to get to know you better."
        gai "I too would be lying if I said I was only doing it for you, I'm mostly doing it for Maia, to help her regain what she lost."
        scene ch6sc03_337 with dissolve
        gai "However, a part of me… is pleased that I am doing this, for I too, would love to experience… love."
        scene ch6sc03_338 with dissolve
        gai "I’m not saying that we’ll fall in love, but… I-... I wouldn’t be opposed to it."
        scene ch6sc03_339 with dissolve
        gai "You’re a great man… you have great qualities…"
        "You feel her sharp nail, gently run across your chest."
        gai "You have proven yourself capable and worthy… restoring our connection to our followers."
        scene ch6sc03_340 with dissolve
        gai "That alone is enough… to make me feel… something."
        gai "I do not know if this is what the beginning of love feels like? But it’s definitely attraction."
        scene ch6sc03_341 with dissolve
        gai "*Sighs* Sorry, I kinda lost my head there…"
        mc "It’s alright, you didn’t do anything wrong."
        scene ch6sc03_343 with dissolve
        gai "I’m attracted to my sister’s partner, it’s definitely wrong."
        gai "And yet, it feels incredibly right… why is that?"
        scene ch6sc03_344 with dissolve
        mc "We don’t choose who we are attracted to, or who we love."
        mc "Sure, we can choose to love someone and stick by that choice, but feeling it blossom?"
        mc "That is only something you’ll experience if it’s genuine."
        scene ch6sc03_345 with dissolve
        gai "Curious."
        gai "You are certainly wise beyond your years, champion."
        scene ch6sc03_346 with dissolve
        gai "Does this mean that such feelings have begun to take root within me?"
        mc "It does sound like it, but only time will tell what it grows into."
        gai "Hmh, interesting."
        scene ch6sc03_347 with dissolve
        gai "What about you?"
        gai "Do you… *Clears throat* Feel something, in my presence?"
        scene ch6sc03_345 with dissolve
        mct "I knew this question was going to come up, it’s time I decide how I want us to proceed."
        mct "Do I just want this to be a friendship, or do I want to pursue something more intimate with Gaia?"
        scene major_choice with Dissolve(1.5)
        ####Choice####
        menu:
            "I feel a growing attraction to you as well. ({color=#ff8cdd}Romance Lock-in{/color})":
                scene ch6sc03_345 with Dissolve(1.5)
                mc "I can’t lie to you… I have felt attracted to you since we first met."

                if gaia_path == True:
                    mc "Ever since our lips met when I became your champion..."
                    mc "I have thought about you... quite a lot."

                else:
                    pass

                scene ch6sc03_346 with dissolve
                gai "You… you have?"
                gai "Truly so?"
                $ gaia_path = True
                scene ch6sc03_349 with dissolve
                mc "Mhm, I have. And that attraction has grown since then, seeing you today… I feel it."
                scene ch6sc03_350 with dissolve
                gai "Oh… this is… most pleasing to hear."
                gai "I-... I wasn’t sure if what I felt was one-sided… I’m pleased it isn’t."
                scene ch6sc03_349 with dissolve
                $ gaia_relationship = True
                mc "Trust me, the attraction you feel isn’t one-sided."
                scene ch6sc10_375 with dissolve
                gai "This is most exciting!"
                gai "Honestly, in my 3.000 years, I’ve never felt this excited about anything."
                scene ch6sc10_376 with dissolve
                mc "Is that so?"
                mc "I like knowing that I stir such excitement within you."
                scene ch6sc10_375 with dissolve
                gai "Not as much as I enjoy feeling it! *Giggles lightly*"
                scene ch6sc10_377 with dissolve
                gai "And since you’ve brought me to such an elevated mood, I will give you a choice."
                gai "You’ll have two options."
                scene ch6sc10_378 with dissolve
                gai "Option one."
                $ soulbinding = True
                gai "We’ll exchange our essences with a kiss, solidifying our soulbinding and linking us."
                scene ch6sc10_377 with dissolve
                gai "Or… option two."
                gai "I will put my lips to use somewhere more… intimate. *Giggles softly*"
                scene ch6sc10_376 with dissolve
                mc "Option two."
                mc "As much as I’d love to enjoy kissing you, I’m sure we’ll get plenty of chances for that."
                scene ch6sc10_377 with dissolve
                gai "Option two it is then."
                gai "A man who knows his own desire. *Quietly* {b}{size=-10}and also mine.{/size}{/b}"
                scene ch6sc10_375 with dissolve
                gai "Take off your pants and sit on the wall and I’ll begin our soulbinding."
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0
                scene ch6sc10_379 with Dissolve(1.5)
                play music lewd_1 fadein 1.0
                #stop music fadeout 1.0
                "You do as instructed, as you lean back Gaia sits herself beside you, studying your cock."
                gai "Mmh… you’re definitely attracted to me, I see that now. *Giggles*"
                scene ch6sc10_380 with dissolve
                "Gaia runs her nails along your shaft, sending waves of pleasure through your cock and body."
                scene ch6sc10_379 with dissolve
                gai "I had no idea my champion was so… well equipped."
                scene ch6sc10_380 with dissolve
                mc "Mmh… fuck…"
                scene ch6sc10_379 with dissolve
                gai "You need me, don’t you? My handsome champion."
                scene ch6sc10_380 with dissolve
                mc "Aahh… I need you… mmh…"
                scene ch6sc10_379 with dissolve
                gai "Good… then I will take care of you, just the way you need."
                scene ch6sc10_381a with dissolve
                gai "I will use my mouth to make your powerful cock burst with your seed."
                gai "In doing so, the essence in my saliva and the essence in your seed will merge, linking us."
                mc "Do it… begin the soulbinding."
                scene ch6sc10_381 with dissolve
                gai "I see you’re as eager to be in my mouth as I am to taste you. *Snickers*"
                gai "I'm going to extract your seed directly from the source."
                scene ch6sc10_382 with dissolve
                gai "Mmmgh! Mmmh! *Sucks gently*"
                scene gai_lewd1 with dissolve
                $ renpy.pause()
                "Gaia eases herself into the feeling of having you inside her mouth, gently twisting her head side to side-"
                "-While she runs her warm tongue covered in saliva all over your tip, gently massaging you."
                mc "Fuck-... Gaia that feels… Mmh… your mouth is a sanctuary…"
                gai "*Sucks and licks* MMmgh… Ssohh goodh… mmgh… I need more."
                scene gai_lewd2 with dissolve
                $ renpy.pause()
                "Loving the taste of your cock, she pushes you further inside her mouth, sucking and licking intimately."
                mc "Aaahh… that’s it… mmgh, that’s how you suck a cock."
                with vpunch
                gai "*Muffled sucking* Nngh-Gghh… I love it… Nngh… I’m pleased with your taste- Nngh!"
                with vpunch
                mc "Fffh… I’m going to- Aahh… I’m going to burst."
                with vpunch
                gai "*Sucks intensely* {b}Do it! Mmghh! Fill my mouth, [mc]! Let your seed blossom within me!{/b}"
                scene ch6sc10_382 with dissolve
                with vpunch
                gai "*Gags and sucks* {b}Gghhrh! Mmgh! Ggh-Nngh!!{/b}"
                scene ch6sc10_383 with dissolve
                with vpunch
                gai "{b}MMffhhp!{/b}"
                scene ch6sc10_383a with dissolve
                "As Gaia swallows your cum the soulbinding takes hold."
                mc "Mmgh… you really know how to put that mouth to good use… mmh."
                scene ch6sc10_383 with dissolve
                gai "*Gulps* Mmmh..."
                scene ch6sc10_384 with dissolve
                gai "*Licks* Anything for my champion… nngh."
                gai "My delicious champion."
                mc "You will be sucking my cock a lot throughout our eternity together. Mmmh."
                scene ch6sc10_385 with dissolve
                gai "*Licks* Mmgh, yes… yes I will."
                mc "Fuck… you’re incredible Gaia."
                mc "Normally tongues are warm, but yours is cold, it's a new and rather pleasurable experience... mhh."
                scene ch6sc10_384 with dissolve
                gai "I was able to please you then? My champion?"
                scene ch6sc10_385 with dissolve
                mc "Fully so."
                gai "Mmgh… nngh… your seed is heavenly… I could enjoy it all day, every day."
                scene ch6sc10_384 with dissolve
                mc "We’ve just become soulbound, you’re my goddess now."
                gai "Mmgh… I like it when you say that."
                gai "Does this mean you will allow me to enjoy your cock whenever I desire it?"
                scene ch6sc10_385 with dissolve
                mc "Yes. Mmh…"
                scene ch6sc10_386 with dissolve
                gai "*Mwah* All cleaned up, my champion."
                gai "Thank you… for this generous gift."
                mc "No, thank you… finally getting to feel the wetness of your little mouth was incredible."
                scene ch6sc10_381a with dissolve
                gai "I am pleased that you enjoyed it."
                gai "It's a sensation you will grow familiar with, I'll make sure of it."
                scene ch6sc10_381 with dissolve
                gai "Next time I will not settle for just sucking your delicious cock."
                "Gaia giggles as she ponders what will transpire during your next meeting."
                scene ch6sc10_380 with dissolve
                gai "But I’m afraid I must conclude your visit for today."
                scene ch6sc10_379 with dissolve
                mc "Really? Shame…"
                gai "Yes… it is. But we took a big step in the direction I hoped we would grow… towards intimacy between us."
                scene ch6sc10_380 with dissolve
                gai "I believe our desire to be one will only continue to grow until our next meeting."
                mc "Mmh… I believe you’re right."
                gai "Come, my handsome champion, it’s time I send you to Malanthe."
                scene ch6sc10_379 with dissolve
                gai "You will have to finish the last soulbinding and thus completing the link between all of us."
                mc "Yeah… until next time then."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0

            "I feel a growing friendship between us. ({color=#2bff8b}Friendly{/color})":
                scene ch6sc03_345
                mc "Gaia, I can’t say that I feel the same attraction towards you."
                mc "But I do feel something else growing between us, the foundation for a solid friendship."
                scene ch6sc03_346 with dissolve
                gai "Friendship? I see…"
                gai "It is not what I had hoped for, but I will happily accept that you feel this way."
                scene ch6sc03_347 with dissolve
                $ gaia_path = False
                gai "As a goddess, I do not exactly have a great many friends, except for my sisters."
                scene ch6sc03_348 with dissolve
                gai "I suppose having you in that circle, would be lovely after all."
                scene ch6sc03_349 with dissolve
                mc "Friends then?"
                scene ch6sc03_350 with dissolve
                gai "Mhm, friendship it is."
                gai "Stand with me, my champion. And we’ll link our essences together."
                scene ch6sc03_356 with dissolve
                mc "We did something similar before didn’t we?"
                gai "Mhm, we did. When you become my champion."
                gai "This time we’re doing it to create and solidify our soulbinding, hold your hands up to mine."
                scene ch6sc10_374 with dissolve
                $ soulbinding = True
                gai "Do you feel it? Do you feel us being linked?"
                mc "I feel it… the soulbinding I have with Maia is becoming more potent as well."
                gai "Yes, with each of us adding our essence to the link, it will grow stronger and stronger."
                gai "Once it’s complete, I will send you to Malanthe, so that you may finalize the link between all of us."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0
                "Upon completion of the soulbinding link, Gaia opens a portal for you to visit Malanthe."

        scene ss55 with Dissolve(1.5)
        $ renpy.pause()
        scene ch6sc06_411 with Dissolve(2.5)
        $ renpy.pause(0.5)
        play music mmm_elven_forest fadein 1.0
        #stop music fadeout 1.0
        mct "There she is."
        scene ch6sc06_412 with dissolve
        mct "I remember this feeling well."
        scene ch6sc06_412a with dissolve
        mct "She has an incredible aura…"
        mct "I can feel her all the way from over there."
        scene ch6sc06_413 with dissolve
        mct "Her presence is unmatched."
        mct "Confident… flirtatious… the air itself around her is filled with desire."
        scene ch6sc06_414 with dissolve
        mal "Hmh?"
        scene ch6sc06_415 with dissolve
        mal "Approach my Champion."
        mal "I see you’ve finally decided to pay me a visit."
        scene ch6sc10_387 with dissolve
        mal "I would be offended, but what is that catchy saying of mortals?"
        mal "Ah, right. {b}Saving the best for last{/b}? *Snickers*"
        mal "I guess I should feel flattered then, afterall… now I won’t have to send you away in a hurry."
        scene ch6sc10_388 with dissolve
        mal "Yes, you heard me right…"
        mal "We have all the time we… desire, tonight."
        scene ch6sc10_389 with dissolve
        mal "I’d almost forgotten how magnificently handsome you are."
        mal "But only almost. *Giggles*"
        scene ch6sc10_390 with dissolve
        mc "Your beauty didn’t escape my mind either."
        mal "Oh? He flirts?"
        scene ch6sc10_391 with dissolve
        mal "What a… pleasant surprise."
        mal "If you’re trying to entice me to forgive you for taking so long to return to me…"
        scene ch6sc10_388 with dissolve
        mal "{b}{color=#ff4f64}*Whispers sensually*{/color}{/b}  {size=-10}{b}It’s working.{/b}{/size}"
        mal "Mmh… I love how defined your muscles are, truly a champion who puts in the work."
        scene ch6sc06_421 with dissolve
        mc "I don’t imagine a goddess such as yourself need to do much to keep your body in impeccable shape?"
        "Malanthe giggles lightly."
        scene ch6sc06_422 with dissolve
        mal "My champion believes his goddess has an impeccable body, does he?"
        scene ch6sc06_421 with dissolve
        mc "It would be pointless to deny it."
        scene ch6sc06_422 with dissolve
        mal "I’ve missed your sweetened words, thank you."
        mal "And no, I needn’t do a single thing to keep my body as you see it."
        scene ch6sc06_424 with dissolve
        mal "Benefit of being a deity."
        mal "Upon creation, our bodies remain in their shape for eternity."
        scene ch6sc06_425 with dissolve
        mc "Damn… that’s quite a neat side-effect."
        scene ch6sc06_426 with dissolve
        mal "I suppose?"
        mal "It can get a little monotone, always knowing what you’ll look like."
        scene ch6sc06_425 with dissolve
        mc "Can’t you change anything? You’re a goddess afterall."
        scene ch6sc06_424 with dissolve
        mal "I suppose we can change our outfits as we see fit, as well as imbue our hair magically into a different shape or color."
        mal "But our bodies? That’s sealed and done."
        scene ch6sc06_423 with dissolve
        mc "Hmmh."
        scene ch6sc06_425 with dissolve
        mc "You said, upon creation? How does that work?"
        scene ch6sc06_426 with dissolve
        mal "Picked up on that, did you?"
        mal "I suppose I’ll tell you, since we’re not in a rush tonight."
        scene ch6sc06_427 with dissolve
        mal "Come, my sweet champion…"
        mal "Sit with me."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc10_392 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mal "*Giggles* Isn’t this nice? Just the two of us, relaxing… enjoying each others company?"
        mc "Enjoying my company? Who’s flirting now."
        scene ch6sc06_437 with dissolve
        mal "*Snickers* How could I not? You’re {b}my{/b} champion, [mc]."
        scene ch6sc06_439 with dissolve
        mal "As my champion, you will have to endure my flirting… afterall… I have not had anyone of interest to flirt with…"
        scene ch6sc06_437 with dissolve
        mal "Not once… in all of my 3,000 years."
        scene ch6sc06_438 with dissolve
        mc "Five hells… I’ll endure your flirting then, my goddess."
        "Malanthe giggles, she clearly enjoys your banter."
        scene ch6sc06_431 with dissolve
        mal "So…  you desire to know about deities and their creation?"
        mc "Mhm, if you don’t mind telling me. I have limited knowledge about deities in general."
        scene ch6sc06_432 with dissolve
        mal "In that case, I’m happy you’ve chosen to seek knowledge from me."
        mal "Where should I begin?"
        scene ch6sc06_433 with dissolve
        mal "Hmh, let’s start with what I mentioned earlier, our creation."
        scene ch6sc06_432 with dissolve
        mal "You see, there are several ways for a god or deity to come into existence."
        scene ch6sc06_433 with dissolve
        mal "Firstly, and most commonly is being created by one of The Seven Divines."
        scene ch6sc06_434 with dissolve
        mal "If they find that there is a need or space available for a deity, they conjure a body and fill it with our life-essence."
        scene ch6sc06_436 with dissolve
        mc "Damn… they can just create a god or goddess, just like that?"
        scene ch6sc06_435 with dissolve
        mal "*Nods* Mhm-hm."
        scene ch6sc06_434 with dissolve
        mal "Secondly a deity can come into existence by being born to another deity."
        mal "Demigods, as they are called."
        scene ch6sc06_436 with dissolve
        mc "Maia actually discussed demigods with me, shortly. But in brief they aren’t fully gods? More like half gods?"
        scene ch6sc06_433 with dissolve
        mal "Correct."
        mal "They are not fully born gods, and most of them never will be."
        scene ch6sc06_432 with dissolve
        mal "But in some cases, a demigod will be elevated to godhood by one of The Seven Divines."
        mal "Typically if their parent dies, their offspring is a prime candidate to fill their role."
        scene ch6sc06_433 with dissolve
        mal "However they could also be elevated to godhood for other reasons."
        scene ch6sc06_434 with dissolve
        mal "And finally, the last way for a god to be born is…"
        mal "In rare cases, a mortal may achieve godhood."
        scene ch6sc06_436 with dissolve
        mc "Really? That’s possible for a mortal?"
        scene ch6sc06_434 with dissolve
        mal "Yes, if the Divines are impressed with them. They have been known to elevate an individual from mortal, to godhood."
        mal "However, it is rare… it might happen once or twice in a millennium."
        scene ch6sc06_437 with dissolve
        mal "The individual has to display great strength of character, they have to have many feats under their belt."
        mal "The Divines are not easily impressed, nor do they take such an act lightly."
        scene ch6sc06_438 with dissolve
        mc "Yeah, I don’t imagine something like creating a god should be taken lightly."
        mc "I guess they are on a whole other level, if they can just create powerful beings such as yourself, that easily."
        scene ch6sc06_437 with dissolve
        mal "They are, [mc]. Nothing in creation even comes close to them."
        mal "To put it into perspective, for a fighter such as yourself…"
        scene ch6sc06_439 with dissolve
        mal "It would likely take 50 deities of my caliber to create a blast powerful enough to slightly pushback a Divine."
        scene ch6sc06_438 with dissolve
        mc "What… 50 gods just to push back a single Divine?"
        scene ch6sc06_437 with dissolve
        mal "Mhm-hm. Probably 80-100 to actually hurt them in the slightest."
        scene ch6sc06_434 with dissolve
        mal "So yes, they are on a whole different level, they play by different rules."
        mal "To categorize any of the Divines as ‘gods’ would be an insult to them."
        scene ch6sc06_433 with dissolve
        mal "But enough about them, you will learn more of such beings when the time is right."
        mal "Now you know the three ways for gods and deities to come into existence."
        scene ch6sc06_442 with dissolve
        mc "Thank you for indulging me, I appreciate it Malanthe."
        scene ch6sc06_433 with dissolve
        mal "You’re welcome my sweet champion."
        scene ch6sc06_442 with dissolve
        mc "I feel like there’s a whole other world out there, that I’m somehow a part of, but barely know anything about."
        mc "So getting to learn a little of it from one who is a part of it… it’s something I value greatly, Malanthe."
        scene ch6sc06_441 with dissolve
        mal "*Bites lip* Nnhh… [mc], you’re sweet."
        mal "*Quietly* And you look so… {size=-10}{b}yummy.{/b}{/size}."
        scene ch6sc06_439 with dissolve
        mal "I think it’s time for us to merge our essences and become one, don’t you?"
        scene ch6sc06_438 with dissolve
        mc "Mhm, that is what I’m here for afterall."
        scene ch6sc06_439 with dissolve
        mal "Is that… the only reason you’ve come to see me? My champion?"
        scene major_choice with Dissolve(1.5)
        ####Choice####
        menu:
            "No, not the only reason. ({color=#ff8cdd}Romance Lock-in{/color})":
                scene ch6sc06_438 with Dissolve(1.5)
                mc "Honestly? The soulbinding is just a happy excuse to see you."
                scene ch6sc06_439 with dissolve
                mal "That’s a bold thing to say… even for you."
                $ mal_trust += 5
                "Malanthe enjoys your bold compliments, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                $ soulbinding = True
                scene ch6sc06_438 with dissolve
                mc "I’ve been looking forward to feeling your presence ever since last time I saw you."
                mc "It’s a feeling I’m rapidly becoming addicted to, I feel like my body is igniting all over with a desire to be near you."
                $ mal_path = True
                scene ch6sc06_441 with dissolve
                mal "*Bites lip* Nnghh… [mc]-... speaking to me like that…"
                mal "You’re not the only one who feels like this… I share your desire."
                scene ch6sc06_440 with dissolve
                mal "From the moment I laid eyes upon you, I knew what I wanted."
                $ mal_relationship = True
                scene ch6sc06_430 with dissolve
                mal "What do you say, my champion?"
                mal "Do you desire to bind yourself to me? To your goddess? Intimately?"
                mc "There’s nothing I desire more at this moment."
                scene ch6sc06_442 with dissolve
                mc "I’m going to make you mine, Malanthe."
                mal "*Snickers happily* Mmhm…"
                scene ch6sc06_441 with dissolve
                mal "Speak to me like that again, and I will make all your desires come true."
                mc "You’re going to become {b}mine{/b}, right now, right here-"
                scene ch6sc10_393 with dissolve
                "In an instant, Malanthe has you strapped down, caressing you intimately."
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0
                $ renpy.pause(0.5)
                play music lewd_1 fadein 1.0
                #stop music fadeout 1.0
                mal "I warned you… now, {b}your desires will become reality{/b}."
                mc "Oh no… the horror..."
                scene ch6sc10_394 with dissolve
                mal "*Snickers* You think you can handle me, do you?"
                mal "I have been waiting for you for {b}3.000 years{/b}… I have no shortage of pent up urges to unleash."
                mc "I believe you promised me something, last we met?"
                scene ch6sc10_395 with dissolve
                mal "{b}{color=#ff4f64}*Whispers sensually*{/color}{/b} {size=-10}{b}I did, didn’t I?{/b}{/size}"
                mal "I will never break a promise, not to you."
                scene ch6sc10_396 with dissolve
                mal "Mmh… do you have any idea how enticing your lips look?"
                mal "How much I long for them?"
                mc "You’re one to talk… I’ve been fantasising about those cherry-red lips of yours and what they would taste like."
                scene ch6sc10_397 with dissolve
                mal "Mmh… *Licks intimately*"
                "She runs her naughty little tongue across your bottom lip, covering it in her warm saliva."
                scene ch6sc10_398 with dissolve
                "You grab her hips and hold her firmly as you engage her lips."
                mal "*Moans while licking* Mmgh-Nngh! So bold…"
                scene ch6sc10_397 with dissolve
                mal "Your lips do not disappoint… mmh."
                scene ch6sc10_398 with dissolve
                mc "Neither does yours- Mmh… I can’t pinpoint the flavor, but it’s fruity and sweet."
                scene ch6sc10_397 with dissolve
                mal "I’ll make you experience tastes you never thought possible- Mmgh…"
                scene ch6sc10_398 with dissolve
                "Malanthe keeps slipping her tongue into your mouth, teasing yours and sharing her delicious saliva."
                scene ch6sc10_399 with dissolve
                "As she gently pulls away, her tasty saliva still connects your tongues."
                mct "Mmh… I’ve never experienced a taste such as this… but I want more."
                scene ch6sc10_398 with dissolve
                mc "Mmgh… delicious."
                scene ch6sc10_397 with dissolve
                mal "Nnngh… can’t get enough? *Licks*"
                scene ch6sc10_398 with dissolve
                mal "Mmh… my handsome champion, it’s time you taste something else…"
                scene ch6sc10_399 with dissolve
                mal "Something I’ve noticed your eyes can’t help but gaze at."
                scene ch6sc10_400 with dissolve
                mal "*Giggles softly* Now that was a kiss worth waiting 3.000 years for."
                mc "Tell me about it… you taste… I can’t even describe it, but I love it."
                scene ch6sc10_401 with dissolve
                mal "Mmmh… I think it’s time we get me out of this dress, don’t you?"
                mc "I was just about to suggest the very same."
                scene ch6sc10_402 with dissolve
                mal "[mc]..."
                mal "What do you think? Do I stir your desires?"
                scene ch6sc10_403 with dissolve
                mal "*Moans* Aiiyh!"
                "You respond by pressing your cock up between her juicy ass cheeks."
                mal "Nnaughty chhampiion! Aahh… when did you… pull this magnificent cock out? Mmh…"
                scene ch6sc10_404 with dissolve
                mc "Just now, when you were removing your dress."
                mc "I lost any and all desire to remain clothed."
                scene ch6sc10_405 with dissolve
                mal "*Giggles softly* You’re trouble..."
                mal "Spending the rest of eternity being soulbound to such a naughty man… how thrilling!"
                scene ch6sc10_404 with dissolve
                mc "I have a feeling we’re going to have no shortage of ideas on how to pass eternity together."
                "She giggles, clearly agreeing with that statement."
                scene ch6sc10_405 with dissolve
                mal "In that case, I desire to start our eternity as lovers by…"
                mal "Riding you until you unleash your warm essence deep within me."
                scene mal_lewd1 with dissolve
                $ renpy.pause()
                "Feeling you adjust your cock between her dripping wet lips, she presses herself down, gently riding you."
                "Each time she presses down, you thrust upwards, causing her to bounce slightly."
                mal "Ohh…ohh! What a feeling!"
                mc "Nngh… fffhh… you’re almost too tight- Aahh…"
                mal "Mmgh… I can’t believe my sexy champion is letting me use his cock- Aahiiyh…"
                mal "[mc]- AhH!"
                mal "I want you {b}deeper!{/b} MMh!"
                mal "I want you to stretch my juicy little pussy!"
                mal "I'm going to ride you! With passion {b}unmatched!{/b}"
                scene mal_lewd2 with dissolve
                $ renpy.pause()
                "After having finally adjusted to your cock, her lust takes over and she begins to ride you, pressing you deeper inside of her."
                with vpunch
                mal "{b}{color=#ff4f64}*Sensual moans*{/color} Aiiyh-Aih! {size=+10}[mc]!! You’re mine!{/size} Ahh! You’re finally mine!!!{/b}"
                mc "Fhh-Nngh! You’re tight Malanthe! {b}Mmgh! Fuck!!{/b}"
                with vpunch
                mal "*Moans* {b}AHH!{/b} Let me ride you! Let me enjoy your cock! {b}Let me satisfy your desires!{/b} Aiiiyhh!"
                with vpunch
                mc "I’m going to- {b}AhhH!{/b}"
                with vpunch
                mal "{b}{color=#ff4f64}*Orgasmic moan*{/color}{/b} {b}Me toooo!! Fill me! {size=+10}Unleash your warm cum deep within me [mc]!!{/size}{/b}"
                scene ch6sc10_406 with dissolve
                with vpunch
                mal "{b}AhhH-Ahh! I feel it! I feel your cum inside of me!!{/b}"
                scene ch6sc10_407 with dissolve
                mc "Mmgh! I can feel the magic of your juices- Ff… we’re linking- Mmgh!"
                mal "{b}We’re eternally bound now{/b}, our desires has made sure of it-"
                mal "Aiiyhh... what an incredible feeling... I've finally been claimed- NnnhhH!"
                $ mal_trust += 5
                "Malanthe's feelings for you has grown, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
                scene ch6sc10_406 with dissolve
                mal "*Moans* {b}Mmm-mmh! What a feeling!{/b} My body is full of excitement combined with a {b}deep{/b} desire."
                scene ch6sc10_403 with dissolve
                mal "This is… Nngh! {b}This is heavenly!{/b}"
                mal "Your cock not only looks like a work of art, it feels as one too- {b}Mmhppfh!{/b}"
                scene ch6sc10_404 with dissolve
                mc "Don’t get me started on that little pussy of yours, you’re literally choking my cock in pleasure as we speak…"
                mal "*Snickers* …"
                scene ch6sc10_405 with dissolve
                mal "Maybe… I should be the one {b}choking?{/b}"
                mal "After all... I have yet to taste you..."
                scene ch6sc10_402 with dissolve
                mal "*Giggles* I’m juuuuust… gonna have a little look."
                scene ch6sc10_408 with dissolve
                mal "*Snickers* My… it’s even better up close. Your cock belongs to me now, mmhh!"
                mal "Tell me baby… tell me that you want me to suck this big cock of yours."
                mc "Mmgh… five hells Malanthe, I need you… I crave feeling that delicious mouth of yours make out with my cock."
                scene ch6sc10_409 with dissolve
                mal "Like this baby? Is this what my champion wants to feel? *Sucks intimately*"
                mc "Ffuck… yeah that’s what I was hoping it would feel like… just like when we kissed earlier."
                mc "Show me how much you enjoy sucking my cock."
                scene mal_lewd3 with dissolve
                $ renpy.pause()
                "As asked, she immediately begins to devour your cock, pushing you as deep as she can handle, rubbing her tongue along your shaft."
                mc "Mmh… that’s my naughty goddess… Mmh… that tongue of yours is magical."
                mc "Fuck... feeling your large, warm and supple breasts surround my thigh as you devour me... incredible."
                with vpunch
                mal "*Muffled sucking* {b}Nngh-MMh!{/b} I’m going to suck this delicious cock of yours any time you desire it- {b}Mmgh!{/b}"
                mal "*Gags and sucks* {b}Ghrh-Mmghrh! So good! Mmgh! I{/b} love tasting your cum and my juices all over your cock baby!"
                with vpunch
                "She passionately massages your tip and shaft with her saliva-covered tongue, sending magic pulses into your cock."
                with vpunch
                mc "Five hells- {b}Hnngh!{/b} If you don’t quit that- Mmh! I’m going to fill your throat with cum!"
                with vpunch
                "Hearing your warning she presses you further into her throat, forcing you to start cumming."
                with vpunch
                $ renpy.pause(0.5)
                with vpunch
                $ renpy.pause(0.5)
                with vpunch
                $ renpy.pause(0.5)
                scene ch6sc10_410 with dissolve
                with vpunch
                "Choking on your cock as you fill her throat she grabs it firmly and pulls it out while your orgasm is still going."
                with vpunch
                mal "{color=#ff4f64}*Gags and moans*{/color} {size=+10}{b}Ghrgh-Mghh! Hnn-mghh!{/b}{/size}"
                scene ch6sc10_411 with dissolve
                mal "*Moans* {b}AiiiyHh!{/b} [mc]... you understand how much I desire your cum I see. *Giggles softly*"
                mc "I would apologize for the mess, but I’m really not sorry. You were incredible and you earned the facial."
                scene ch6sc10_412 with dissolve
                mal "MMgh… I’m grateful that you rewarded my sucking- *Licks* Mmhh… so good."
                mal "This was my first time tasting cum… so many of my followers complain about it’s taste? I don’t get it, you’re simply delicious."
                scene ch6sc10_411 with dissolve
                mc "*Chuckles* Well, I’m a unique case… Maia explained to me that my cum contains small traces of my essence."
                scene ch6sc10_412 with dissolve
                mal "Aahh… no wonder, I didn’t think of that. No wonder I find it so appetizing… *Giggles*"
                mal "I hope you have another load for me?"
                mc "Five hells… you haven’t had enough?"
                scene ch6sc10_411 with dissolve
                mal "3.000 years, [mc]. You have 3.000 years of fulfilling my desires to catch up on. *Snickers*"
                scene ch6sc10_413 with dissolve
                "Malanthe positions herself for another ride."
                mal "But for tonight, I will settle for one last load… to make me happy, will you make me happy, my sweet champion?"
                mal "I'm your wife now, it's your duty to ensure my happiness... mhh..."
                mal "Will you fulfill your goddess’s desire?"
                mc "Mhm, I will. Ride me like you mean it."
                scene mal_lewd4 with dissolve
                $ renpy.pause()
                "Hearing you desire another ride, she eagerly begins bouncing herself on your cock, pushing you as deep as her pussy allows."
                with vpunch
                mal "{b}{color=#ff4f64}*Screams in pleasure*{/color} AHH!! F-FUCK YOU’RE SO {size=+10}DEEEP!!{/size} AYYHH!!{/b}"
                with vpunch
                mal "That’s it! Mmgh!! {b}Let your goddess satisfy you!{/b} Let me take care of your needs! {b}AHH!!{/b}"
                mal "{b}You need me! MMH!!{/b} As I need you! Baby! You need my pussy to suck your cock dry!"
                with vpunch
                mc "{b}Ffuck! Malanthe- Mmgh! I need you! Squeeze every drop out of me- MMh! Five hells I love this little pussy of yours!{/b}"
                mal "{b}{color=#ff4f64}*Screams in pleasure*{/color} AHH!! I love the feeling of my tits bouncing as we fuck!{/b}"
                with vpunch
                mal "{b}I feel you baby!{/b} I feel your cock pulsating!! Unleash all you have inside of me! {b}Give it to me! AHH!!{/b}"
                with vpunch
                scene ch6sc10_413 with dissolve
                mal "{b}Yes!!{/b} Fill me again my champion! Give me what I’m craving!! What my pussy has been longing for!! {b}AiiiyhhH!!{/b}"
                scene ch6sc10_414 with dissolve
                "Upon having reached yet another orgasm with your cock deep within her, she collapses onto you."
                mal "*Out of breath* Oh my sweet champion… thank you."
                mal "Being held like this by you… with you still inside me? You’re spoiling me. *Giggles softly*"
                mc "You deserve to be spoiled… you’ve worked hard tonight."
                scene ch6sc10_415 with dissolve
                mal "Mmh… thank you. I’m pleased you appreciate my efforts to link us."
                mc "I do… you ensured our soulbinding will forever be a special event in my soul."
                mal "Naughty champion… trying to make your goddess fall in love with you? Mmh…"
                mal "{b}Give me your tongue{/b}, I desire to taste you while you're touching me."
                scene ch6sc10_416 with dissolve
                "She engages your tongue with hers, rubbing it gently while she shares her saliva with you."
                scene ch6sc10_416a with dissolve
                mal "{b}{color=#ff4f64}*Shares saliva*{/color}{/b} Nnnh... baby... do you enjoy my saliva? I've never granted it to anyone."
                mc "Mmgh... it's delicious... you're delicious... I can taste the magic your saliva carries."
                mal "Mmmh… I could fall in love with you one day… Mmmh…"
                scene ch6sc10_416 with dissolve
                mc "I’ll be a lucky man the day that it happens… mh-hhmm."
                scene ch6sc10_415 with dissolve
                mal "Yes… yes, you would be."
                mal "*Giggles happily* My handsome husband... you're so good to me."
                mc "After our first meeting, I knew I wanted you... but I didn't think you'd become my wife."
                scene ch6sc10_416 with dissolve
                mal "*Licks* I'm pleased you decided on fully commiting to the soulbinding, in a romantic way."
                mc "There's no way I'd settle for only befriending the goddess of desire herself."
                scene ch6sc10_415 with dissolve
                mal "*Sighs* Come, it’s time I send you back to A’nai, my sweet champion."
                mal "Your companions are awaiting you, to depart from A'nai."
                scene ch6sc10_416 with dissolve
                mal "Mmmgh- Nngh… *Licks* next time, you will be the one fucking me. {b}I want to be fucked until I can’t stand for days{/b}."
                mc "Mmgh… deal. *Licks*"
                scene ch6sc10_416a with dissolve
                $ mal_relationship = True
                mal "Nnh… I love how you can’t keep your hands off me… *Licks*"
                mc "*Licks* I can't help it... your breasts are outrageous... as is the rest of your body."
                scene ch6sc10_415 with dissolve
                mal "Come, let’s get dressed. When you’re ready stand before me."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0
                "The two of you get dressed, although it takes a while since you can’t help glancing at each other."
                scene ch6sc10_387 with Dissolve(1.5)
                $ renpy.pause(0.5)
                play music mmm_elven_forest fadein 1.0
                #stop music fadeout 1.0
                mal "*Snickers* It seems I’m not the only one with an everlasting desire."
                mal "You enjoy your goddess that much?"
                scene ch6sc10_388 with dissolve
                mal "I enjoy you too, [mc]."
                scene ch6sc10_389 with dissolve
                mal "Especially now that {b}I’m yours{/b}…"
                mal "And {b}you're mine{/b}."
                scene ch6sc10_390 with dissolve
                mc "I wouldn’t have it any other way."
                mal "Me neither… you’re now my champion… my lover… and my soul-partner."
                mal "My... husband."
                scene ch6sc10_391 with dissolve
                mc "From what I understand, our soulbinding, it’s essentially marriage for gods?"
                mal "Correct, although it isn’t just something society has created."
                scene ch6sc10_388 with dissolve
                mal "A soulbinding is far more… intimate, as you know well by now."
                scene ch6sc10_389 with dissolve
                mal "And I do not mean the sexual intimacy we just had."
                mal "Our souls have become bound, we’re linked. For all eternity."
                scene ch6sc10_390 with dissolve
                mc "Mhm, after we linked, I feel you. Differently than before, before I could easily sense your aura."
                mc "But now, I don’t just sense it, I feel it. I feel your emotions…"
                scene ch6sc10_391 with dissolve
                mal "As I feel yours."
                mal "My handsome champion."
                scene ch6sc10_388 with dissolve
                mal "No matter where either of us are, we will feel each other."
                scene ch6sc10_389 with dissolve
                mal "Maia gifted you the ability to use Dimension door, correct?"
                scene ch6sc10_390 with dissolve
                mc "She did, at first to be able to reach A’nai, but after the soulbinding she mentioned I can use it to reach her as well."
                mal "This is true, which means what?"
                scene ch6sc10_391 with dissolve
                mc "That I will be able to use it to reach you and Gaia as well? Now that we’re linked."
                mal "Both handsome and smart… yes, you will simply have to focus on one of us when you cast Dimension door."
                scene ch6sc10_388 with dissolve
                mal "So if you ever need me, don’t hesitate to come see me."
                mal "Now, we better get you back to your companions."
                scene ch6sc06_443 with dissolve
                mal "Place your hand in mine, champion."
                scene ch6sc06_444 with dissolve
                "You place your palm against hers, feeling the warmth and delicate touch of her fingers."
                mc "This feels familiar… like when I became your champion."
                "As the two of you lock eyes, you feel a warmth beginning to surface between your palms."
                scene ch6sc06_445 with dissolve
                mc "Incredible… you put a whole new meaning to having a magical touch."
                $ mal_path = True
                "Malanthe giggles softly as she focuses on the sensation between the two of you."
                scene ch6sc06_446 with dissolve
                mal "[mc]... thank you, you’ve given me the most special night I’ve ever had."
                mal "You have truly made me excited for our future together."
                mc "I’m right there with you, I look forward to seeing you again."
                scene ch6sc06_447 with dissolve
                mal "As do I, my delicious [mc]. Take care until we meet again."
                scene ch6sc06_446 with dissolve
                mal "Oh, since you're leaving A'nai, you might want to disguise Malpheon's talisman, simply infuse it with your essence."
                mal "While infusing it, focus on making it vanish, you will have its effects without it being seen on you."
                mc "Ah, that's great, it suits me out here, but back home I doubt it will fit my regular clothing."
                scene ch6sc06_447 with dissolve
                "Your body is overwhelmed with a warmth, you feel yourself starting to drift off."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0

            "Yes, I only came to finish the soulbinding. ({color=#2bff8b}Friendship{/color})":
                scene ch6sc06_438 with dissolve
                mc "Mhm, I’m just here to finish linking the soulbinding."
                scene ch6sc06_437 with dissolve
                mal "I can’t pretend I’m not disappointed to hear this…"
                mal "But I was prepared for it, very well then."
                scene ch6sc06_434 with dissolve
                $ mal_path = False
                mal "Stand with me, [mc]. And we will begin linking our essences."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                scene ch6sc06_443 with Dissolve(1.5)
                $ renpy.pause(0.5)
                mal "Put your hand in mine."
                $ soulbinding = True
                mal "Just as when you became my champion."
                scene ch6sc06_444 with dissolve
                "You place your palm against hers, you feel the warmth and soft touch of her fingers."
                "You push forth your essence, and as it merges with hers, it lights up as the link is being formed."
                scene ch6sc06_445 with dissolve
                mal "There we go… we’re now soulbound, my champion."
                mc "Incredible… I feel the link between all of us, more powerful than ever."
                mal "Me too, it seems my idea of the threeway soulbinding was on point."
                scene ch6sc06_446 with dissolve
                mc "Hnnh… wh-what’s happening…"
                mal "I’m sending you back to A’nai. You don’t wish for your companions to set sail without you, do you?"
                mc "Right… hnngh… see you another time then."
                mal "Until next time, my champion."
                scene ch6sc06_447 with dissolve
                mal "Oh, since you're leaving A'nai, you might want to disguise Malpheon's talisman, simply infuse it with your essence."
                mal "While infusing it, focus on making it vanish, you will have its effects without it being seen on you."
                mc "Ah, that's great, it suits me out here, but back home I doubt it will fit my regular clothing."
                scene black with Dissolve(1.5)
                $ renpy.pause(0.5)
                #play music summon_3 fadein 1.0
                stop music fadeout 1.0


    else:
        scene ch6sc10_313 with dissolve
        mct "Huh? Did she have a change of heart about whatever it was?"
        mc "Okay, I won’t press the matter, if you want to discuss it another time we can."
        scene ch6sc10_314 with dissolve
        mai "[mc]... thank you."
        mai "You should return to A’nai, I believe you need to get ready for your departure?"
        scene ch6sc10_313 with dissolve
        mc "Right, I almost forgot about that."
        mc "I’ll see you another time then, and thank you for answering my questions… as I said, I appreciate it."
        scene ch6sc10_314 with dissolve
        mai "You’re welcome… now please, I wish to be alone."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Upon returning to A’nai, you begin to make the rounds, saying your goodbyes to everyone."
    scene ch6sc10_417 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ec "You promise you’ll be back?"
    mc "I promised you, didn’t I?"
    ec "You did… *Hugs tightly*"
    mc "Then you know I’ll be back."
    mc "You better keep things tidy until I return."
    ec "Commanding me now, are you? *Giggles* It’ll be just as you remember it!"
    ec "Maybe with a few extra huts for Arugoh members, and we might look into making some-"
    ec "-living quarters within the temple, just like they did with Maia's temple."
    mc "Good idea, they had a nice setup back there, definitely something I would encourage here."
    scene ch6sc10_417a with Dissolve(1.5)
    ec "I want you to have this... you told me as an adventurer you discover treasures."
    ec "You can display this at your guild."
    mc "Echo... this feather has great meaning to you."
    ec "{b}You{/b} have great meaning to me."
    ec "And I'd like you to have this, let's call it a union gift between the A'khan and his A'nu. *Giggles*"
    mc "Thank you. I'll make sure it gets a prime spot back at the guild."

    if ec_relationship == True:
        scene ch6sc10_417 with Dissolve(1.5)
        ec "Mmhhhp! I don't want you to leave..."
        ec "You're my husband... I wish for you to stay here and live by my side..."
        ec "Make love to me day and day out... mate me lustfully and caress me lovingly..."
        mc "We both know I would love if that could be the case."
        ec "I love you so much."
        mc "As I love you, my sweet and beautiful wife."
        mc "The first thing I'll do upon my return, is find you and make love to you for several hours."
        ec "Mmhhffhh! O-Okay... I know you always keep your word, so don't forget!"
        mc "*Chuckles* I'd never forget you."
        $ ec_trust += 3
        "Echo finds comfort in your arms and trusts your in word, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

    else:
        pass

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_418 with Dissolve(1.5)
    $ renpy.pause(0.5)
    siv "Mmh… I can’t believe you’re leaving us."
    siv "My handsome A’khan… you realize you will be missed greatly?"
    mc "I’ll return when possible."
    siv "You better… you have a great number of women here who need you."
    siv "I shall think fondly of you until you return, and ensure our people keep good faith with the goddesses."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_419 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mh "I guess this is goodbye then? Tsk!"
    mc "Mhm, for a while at least."
    mh "And what about us? We’re your people now… Hmpfh."
    mct "Things sure have taken a turn with her, now she’s upset that I’m leaving?"
    mc "You giving me attitude now? You know I will return, until then… I expect you to assist Echo in keeping the tribe healthy."
    scene ch6sc10_420 with Dissolve(1.5)
    mh "Tsk! Of course I shall, I’m your High-Priestess."
    mh "*Sighs* But… I’m glad you asked. Just… hurry back."
    mc "I’ll be back when possible, I’m counting on you Marah."
    mh "I won’t let you down, my A’khan."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc07_301 with Dissolve(2.5)
    $ renpy.pause(0.5)
    mc "There they are."
    scene ch6sc07_302 with dissolve
    mc "If it isn’t my favorite hunting partner and A’nai’s most promising herbalist."
    scene ch6sc07_303 with dissolve
    vx "[mc]! Hi!"
    vx "You look handsome today."
    scene ch6sc07_305 with dissolve
    mi "Look at you Vex! Being all forward and stuff. *Giggles*"
    with vpunch
    vx "I’m going to punch you!"
    scene ch6sc07_304 with dissolve
    mi "She’s right though, you do look mighty handsome today."
    scene ch6sc07_307 with dissolve
    vx "Y-Yeah… he does."
    mc "*Chuckles* You’re cute when you get all shy."
    scene ch6sc07_306 with dissolve
    vx "I am?! Uh… good! I’m glad my nervousness is appreciated."
    vx "I’m really glad you’ve become our A’khan, and that you brought Arugoh here to unite us."
    scene ch6sc07_311 with dissolve
    mi "Yeah, there has been a few headbutts over the logistics of housing everyone but…"
    mi "They seem to be settling in alright, we just have to construct more huts so everyone has proper space."
    scene ch6sc07_312 with dissolve
    mi "But Aiyo, my sister… she wasn’t amongst the ones who returned."
    mct "Her sister? Hmm, she could be one of the huntresses that went missing, scouting the northern section of the island."
    scene ch6sc07_313 with dissolve
    vx "She didn’t? I wasn’t aware."
    vx "Miyo… I’m so sorry, I promise I will keep my eyes peeled when I’m out on hunts."
    scene ch6sc07_321 with dissolve
    mi "Vex… thank you."
    mi "I truly appreciate that."
    scene ch6sc07_319 with dissolve
    mi "You really are an amazing friend, you know that?"
    scene ch6sc07_308 with dissolve
    mc "Miyo, when I was at Arugoh, they mentioned a few huntresses having gone missing whilst out scouting."
    mc "It’s not much to go on, but you can bring this to Echo’s attention and she will decide the best course of action."
    scene ch6sc07_304 with dissolve
    mi "Thank you, [mc]. I will do just that."
    mi "She always knows what to do, or at least she is great at figuring out solutions."
    scene ch6sc07_308 with dissolve
    mc "If your sister has not returned or been found upon my return to A’nai, I will personally go search for her."
    scene ch6sc07_321 with dissolve
    mi "[mc]... that’s… thank you."
    mi "Thank you so much, I pray that won’t be necessary."
    scene ch6sc07_332 with dissolve
    vx "You’re here to say goodbye, aren’t you?"
    vx "I’ve seen Pearl running around packing stuff and saying goodbye all day."
    scene ch6sc07_333 with dissolve
    mc "That’s right, I stopped by to see the two of you and say goodbye."
    scene ch6sc07_334 with dissolve
    vx "Not permanently, right? … please?"
    scene ch6sc07_335 with dissolve
    mc "You needn’t beg, you know full well that it is just a “until I return” goodbye."
    scene ch6sc07_336 with dissolve
    vx "G-Good…"
    vx "I don’t think I could handle it… if I never saw you again."
    scene ch6sc07_337 with dissolve
    mc "Shh… my little huntress."
    mc "I don’t want you thinking like that."
    vx "*Nods gently* Mmh."
    scene ch6sc07_338 with dissolve
    vx "O-Okay… I promise I will think happy thoughts… about your return."
    scene ch6sc07_339 with dissolve
    vx "About us… hunting together."
    scene ch6sc07_340 with dissolve
    mc "That’s right, you’re my hunting partner, so prepare yourself to be taken hunting next time."
    scene ch6sc07_339 with dissolve
    vx "P-Promise?"
    scene ch6sc07_340 with dissolve
    mc "I promise."

    if vx_path == True:
        scene ch6sc07_339 with dissolve
        vx "*Whispering* {size=-10}{b} Maybe... you could even hunt me?{/b}{/size}"
        vx "*Whispering* {size=-10}{b} I miss feeling you... inside me.{/b}{/size}"
        scene ch6sc07_340 with dissolve
        mc "*Whispering* {size=-10}{b}Oh I'm going to hunt you alright... you naughty little thing.{/b}{/size}"

    else:
        pass

    scene ch6sc07_323 with dissolve
    vx "I feel much better now, excited even! I’m going to go see if anyone of our new members need help settling in."
    mc "Sounds great, little one. Take care."
    scene ch6sc07_324 with dissolve
    mc "As for you, my little herbalist."
    mi "Yay, am I finally going to get some attention?"
    scene ch6sc07_325 with dissolve
    mi "I like it when it’s just the two of us. *Giggles*"
    scene ch6sc07_326 with dissolve
    mi "Don’t you? My A’khan."
    mc "I do, you’re great company."
    mi "I’m going to miss you, you know?"
    mc "I’ll miss that cheeky little smile of yours."
    mi "You promised Vex that you’d be back… you better keep it."
    mc "*Chuckles* Just for her sake?"
    mi "Nnh-Nhh… not just for her… I just didn’t want to sound selfish."
    mc "Until I see you again, Miyo."
    mi "Bye-bye! I look forward to our future under your leadership."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_421 with Dissolve(2.5)
    $ renpy.pause(0.5)
    sk "*Sighs* If I had known you would leave us this soon…"
    sk "I… I wouldn’t have held myself back as I have…"
    scene ch6sc10_422 with Dissolve(1)
    mc "I’ll return Sakari, and when I do…"
    mc "You’ll have your chance."
    scene ch6sc10_423 with Dissolve(1)
    sk "Mh-hm… I look forward to that."
    sk "I won’t let my chance to show you my affections go to waste twice."

    if harem_path == True:
        scene ch6sc10_421 with Dissolve(1)
        sk "This... 'Harem' you've built... it's truly a feat for a king."
        sk "However... when you return, I aim to stand out amongst all your beautiful women."
        sk "I will win your heart, and your desire."

    else:
        pass

    scene ch6sc10_422 with Dissolve(1)
    mc "I’m looking forward to seeing what you come up with."
    mc "Farewell, Mistress Sakari."
    scene ch6sc10_421 with Dissolve(1)
    sk "F-Farewell, my A’khan."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_424 with Dissolve(2.5)
    $ renpy.pause(0.5)
    sj "MMmh!! I’m going to miss you big time, you know?!"
    mc "*Chuckles* I know, Suji… I’ll miss you too."
    sj "I demand Jungle-Jingles upon your return! Hm-Hm!"
    scene ch6sc10_425 with dissolve
    mc "Fine, I’ll grant you one Jungle-Jingle when I return."
    scene ch6sc10_424 with dissolve
    sj "Three!"
    scene ch6sc10_425 with dissolve
    mc "One."
    scene ch6sc10_424 with dissolve
    sj "Two!"
    scene ch6sc10_425 with dissolve
    mc "*Sighs* … Two."
    scene ch6sc10_424 with dissolve
    sj "*Hugs tightly* Yay!"
    sj "Goodbye [mc]! Please don’t forget us while you’re out there adventuring in the great world."
    mc "Goodbye Suji, you don’t have to worry, you have etched your way into my mind and heart."

    if sj_relationship == True:
        scene ch6sc10_425 with dissolve
        sj "I love you!"
        mc "*Chuckles* I love you too. My sexy little huntress."
        scene ch6sc10_424 with dissolve
        sj "*Hugs tightly* I wish I could go explore the world with you!"
        sj "Like when we explored Gaia's temple!"
        scene ch6sc10_425 with dissolve
        mc "Maybe one day... I'll take you on an adventure outside of the island."
        sj "YES! I'd love that! *Giggling* A great adventure while we mate like animals!"
        mc "*Chuckles* Deal."

    else:
        pass

    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_426 with Dissolve(2.5)
    $ renpy.pause(0.5)
    zy "Mmhhhpfh!"
    mc "Zyra…"
    zy "No!"
    scene ch6sc10_427 with dissolve
    zy "Two more weeks! At least!"
    mc "You know I can’t… not at this moment."
    mc "My friends and loved ones back home are counting on me to return."
    scene ch6sc10_426 with dissolve
    zy "Mmhfp! But I miss you!"
    mc "*Sighs* You know I will miss you too, you have really grown on me."
    zy "I have? I mean… of course I have!"
    scene ch6sc10_427 with dissolve
    zy "I’m a great huntress!"
    mc "*Chuckles* One of my very best huntresses."
    zy "And beautiful too! *Giggles*"
    mc "And beautiful as well."
    scene ch6sc10_426 with dissolve
    zy "Alright, alright… I suppose I will let you off the hook."
    zy "But you better bring more compliments with you upon returning!"
    mc "*Chuckles* I’ll see what I can do. Take care Zyra."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_428 with Dissolve(2.5)
    $ renpy.pause(0.5)
    riv "I know it’s pointless to ask you to stay… but…"
    riv "I would never forgive myself if I didn’t at least ask, so… please, won’t you stay?"
    mc "Despite us both knowing the answer, I’m glad you asked."
    scene ch6sc10_429 with dissolve
    riv "As I said, If I hadn’t I would have been asking myself every day if it would have changed the outcome."
    riv "But you’ve told me about your loved ones back home, so I knew very well you couldn’t stay for long."
    riv "And I know you, I know you count us amongst your loved ones as well now. I know you will return to us whenever possible."
    scene ch6sc10_430 with dissolve
    mct "Damn, she does know me well."
    mct "I suppose we have gotten rather close during my time here."
    mc "I’ll come visit whenever I can, I’m glad you understand that."
    scene ch6sc10_428 with dissolve
    with vpunch
    riv "Mmmffh!"
    riv "Until then, I will do my best to train our huntresses, and help construct new huts for the rest of the tribe."
    mc "That’s what I like to hear, I’m counting on you Riven."

    if riv_relationship == True:
        riv "[mc]-... I want to tell you that I... I lo-"
        mc "Shh, I know Riven. I know."
        mc "Don't tell me now, tell me upon my return. That way you know I'll have to come see you again."
        riv "R-Right! That's so cute! Mmfffhh! Thank you... you always know how to ease my mind."

    else:
        pass

    "Riven hugs you tightly before the two of you part."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_276 with Dissolve(2.5)
    $ renpy.pause(0.5)
    mc "There she is, my strong and beautiful Head-Huntress."
    "Kisha can’t help but giggle as you caress her chin and cheek."
    "The once cold and harsh facade of hers now instantly melt whenever you look upon her."
    mc "You’ll watch over everyone with Riven whilst I’m away, won’t you?"
    scene ch6sc10_431 with dissolve
    ks "I will, My A’khan."
    ks "We have a great deal of work ahead of us to provide all the returning members shelter, starting with huts."
    scene ch6sc10_432 with dissolve
    mc "What else?"
    scene ch6sc10_431 with dissolve
    ks "We will also have to integrate them into our way of living, assign them to their respective duties."
    ks "And of course, training everyone will continue. We may have a strong A’khan to protect us now-"
    ks "-But we should all be able to pull our weight should a battle find itself upon us."
    scene ch6sc10_432 with dissolve
    mc "I couldn’t have said it better myself, Kisha. I’m glad to be leaving A’nai in your capable hands."
    "Kisha nods happily, she appreciates you acknowledging her."
    scene ch6sc10_276 with dissolve
    mc "Take care of yourself and everyone, Head-Huntress."
    ks "Mhm-hm."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    "On your way towards the main gate, you hear Pearl’s soft voice call out to you."
    scene ch6sc10_433 with Dissolve(2.5)
    $ renpy.pause(0.5)
    pl "[mc]! There you are!"
    mc "Hey, I was just about to come look for you."
    pl "You found me! *Giggles* Had I known, I would’ve hid… make you work for it."
    scene ch6sc04_516 with Dissolve(1.5)
    pl "Where have you been all day?"
    pl "I may have been getting ready to leave but I definitely noticed your absence."
    scene ch6sc04_517 with dissolve
    mc "You’re perceptive as ever, you’re right, I wasn’t here in A’nai."
    scene ch6sc04_518 with dissolve
    pl "*Giggles* Your mermaid does rather well on land, don’t you think? Wait-"
    scene ch6sc04_516 with dissolve
    pl "What do you mean you weren’t in A’nai? Did you venture into the jungle?"
    scene ch6sc04_517 with dissolve
    mc "No, I actually met with Maia. She had a proposition for me."
    scene ch6sc04_516 with dissolve
    pl "Hmh, how ominous…"
    pl "But I won’t ask what it’s about, you will tell me if I need to know."
    scene ch6sc04_517 with dissolve
    mct "I love how understanding she is, and I know she is curious by nature, yet she chooses to respect my privacy."
    mc "Correct, it was a personal meeting. Thank you for not prying."
    scene ch6sc04_518 with dissolve
    pl "Of course, Sharky!"
    scene ch6sc04_516 with dissolve
    pl "So, are you ready to get the hell on out of here?"
    pl "Not that I mind it, A’nai has grown on me actually, but I really want to go see Kira."
    scene ch6sc04_517 with dissolve
    mc "You bet, I’m sure she is losing her mind worrying about us."
    scene ch6sc04_519 with dissolve
    tz "There you are!"
    tz "Where in all of Midomir have you been all day? We’re supposed to depart in a few moments."
    scene ch6sc04_520 with dissolve
    mc "*Chuckles* Sorry boss, I was a little preoccupied with being summoned by a goddess."
    scene ch6sc04_522 with dissolve
    tz "Oh! Huuuh?!"
    scene ch6sc04_523 with dissolve
    tz "I can’t believe I missed such an opportunity!"
    tz "I could’ve written great things about such an event."
    scene ch6sc04_521 with dissolve
    tz "*Mumbles* {size=-5}{b}Hmmh, the Nephilim was summoned personally by one of Midomir’s goddesses.{/b}{/size}"
    tz "*Mumbles* {size=-5}{b}What she had in store for him is yet unknown, but a step in the right direction it certainly seems to be.{/b}{/size}"
    scene ch6sc04_520 with dissolve
    mc "Think you got everything? *Chuckles*"
    scene ch6sc04_522 with dissolve
    tz "Sorry, yeah… you know how I get when something happens."
    tz "I don’t want to risk forgetting it."
    scene ch6sc04_520 with dissolve
    mc "Taz, it’s fine. I would go into details about it but it was more of a personal meeting."
    "Tazzy nods understandingly."
    scene ch6sc04_523 with dissolve
    tz "It looks like the sun is starting to set."
    tz "I’m going to miss the beauty of nature out here."
    scene ch6sc04_524 with dissolve
    mc "Yeah, me too."
    mc "I’ve been out in the wilds more often than not over the last decade…"
    mc "But Aruna and A’nai have been something else… it has grown on me quite a bit."
    scene ch6sc04_525 with dissolve
    pl "I’m sure having 70ish women all drooling over you as their handsome and powerful leader has nothing to do with it?"
    scene ch6sc04_524 with dissolve
    tz "*Giggles* Pearl! You really have no filter, do you?"
    mc "She really doesn’t, which I’ve grown to like about her. *Chuckles*"
    scene ch6sc04_525 with dissolve
    pl "What? By all means, correct me if I’m wrong! *Snickers*"
    scene ch6sc04_524 with dissolve
    "Neither you or Taz attempts to correct her."
    mc "We’ve had quite the adventure out here, huh girls?"
    scene ch6sc04_525 with dissolve
    tz "Certainly so! Remember when you found me passed out in the jungle?"
    pl "Or when we got separated upon arriving here by eating those blacknip berries!"
    scene ch6sc04_524 with dissolve
    tz "Or when we managed to successfully make it through the cave with that filthy beast?"
    pl "I’ll admit, it truly has been quite the adventure. *Giggles*"
    scene ch6sc04_526 with dissolve
    tz "C’mon, we better head to the main gate, I believe Orianna should be waiting for us."
    tz "She seems really sweet, we shouldn’t make her wait."
    scene ch6sc04_527 with dissolve
    mc "I agree, Orianna seems genuine, which took me by surprise… being a diplomat and all."
    mc "So far she has my trust, so yeah, let’s not keep her waiting."
    scene ch6sc04_530 with dissolve
    tz "*Mumbles* {size=-5}{b}The Nephilim has begun making allies across the kingdoms.{/b}{/size}"
    tz "*Mumbles* {size=-5}{b}Maybe he is planning a conquest?{/b}{/size}"
    mc "Taz…"
    scene ch6sc04_531 with dissolve
    tz "*Snickers* Sorry! Sorry! But who knows?"
    tz "L-Let’s go!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "The three of you meet up with Orianna at the gate and you set out with directions from the huntresses of the beach."
    scene ss4 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_434 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    pl "Mmgh! Nothing like a nighttime swim!"
    pl "And nobody got eaten by sharks! *Giggles*"
    scene ch6sc10_435 with dissolve
    pl "Now, if you’ll excuse me, I’m going to wash off the salt water."
    pl "We have roughly two days at sea depending on the winds, until we reach Looter’s Bay, so make yourselves comfortable!"
    scene ch6sc10_436 with dissolve
    tz "Uhh… she was kidding about the sharks, right?"
    tz "Right???"
    ori "*Giggles* …"
    scene ch6sc10_437 with dissolve
    tz "Oh! Hell no!"
    tz "I-... I need to go lay down for a bit, before I have a heart attack."
    mc "There’s a comfortable bed in the captain's quarters, you can rest in there."
    tz "Thank you, I’ll see you guys later."
    scene ch6sc10_438 with dissolve
    mc "And then there were two."
    mc "How are you holding up?"
    mc "The trek through the jungle to the beach took almost two hours and then one hour to swim to the ship."
    scene ch6sc10_439 with dissolve
    ori "Sure, it was a little rough, but I managed."
    ori "I had a rather capable man looking out for me afterall."
    scene ch6sc10_440 with dissolve
    ori "Thank you by the way, for assisting me during the swim…"
    ori "I’m not a strong swimmer as you noticed."
    scene ch6sc10_441 with dissolve
    mc "You’re most welcome, Ori."
    mc "I couldn’t exactly let you down, your safety is the whole reason we came out here in the first place."
    scene ch6sc10_440 with dissolve
    ori "Right! I suppose you did it just for the mission…"
    ####Choice####
    menu:
        "Reassure her.":
            scene ch6sc10_442 with dissolve
            mc "I think we both know…"
            scene ch6sc10_443 with dissolve
            mc "The mission was the last thing on my mind after I met you."
            ori "Nnhh… I see…"
            ori "I-... I had hoped that would be the case."
            $ ori_trust += 2
            "Orianna enjoys your flirtation, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Just for the mission.":
            scene ch6sc10_441 with dissolve
            mc "Mhm, the mission comes above all."
            mc "Nothing will happen to you under my watch."
            scene ch6sc10_439 with dissolve
            ori "That’s… good."


    scene ch6sc10_439 with dissolve
    ori "This is one thing I love about my job, I travel quite often, usually at sea."
    ori "The air out here is so fresh, and the ambiance of the waves brushing against the ship,  with the occasional seagull."
    scene ch6sc10_440 with dissolve
    ori "It brings peace and quiet to one's mind, which is sorely needed in the world of politics."
    scene ch6sc10_441 with dissolve
    mc "Yeah, I can imagine… as you know, I’m not too keen on politics, I don’t have the temperament for it."
    scene ch6sc10_444 with dissolve
    ori "Oh you’d totally end up strangling some sophisticated aristocrat on the first day! *Snickers*"
    mc "*Chuckles* That sounds about right."
    scene ch6sc10_441 with dissolve
    mc "Although, you’re a politician… yet I seem to enjoy your company."
    scene ch6sc10_440 with dissolve
    ori "[mc], I-... I rather enjoy yours as well, I must admit."
    ori "I’m certainly glad you don’t feel the need to strangle me every time I utter a sentence. *Giggles*"
    scene ch6sc10_444 with dissolve
    mc "Well…"
    with vpunch
    ori "*Laughs* Stop! Don’t you start!"
    scene ch6sc10_439 with dissolve
    ori "*Belly growls* Uh…"
    ori "I think I’ll go look if there’s anything we can cook up for dinner in the ship's storage."
    scene ch6sc10_441 with dissolve
    mc "There should be, the storage on these ships have been enchanted with cooling magic by their Admiral."
    scene ch6sc10_440 with dissolve
    ori "Great, I’ll attempt to whip something up for dinner that we can all enjoy."
    scene ch6sc10_444 with dissolve
    ori "*Giggles lightly* Just… don’t judge my cooking, okay? I’ll have to make do with whatever we have."
    scene ch6sc10_440 with dissolve
    ori "But when you arrive in Arazalia, and I’m showing you around… we could have dinner at my place?"
    scene ch6sc10_441 with dissolve
    mc "I’d like that, Orianna."
    scene ch6sc10_440 with dissolve
    ori "Perfect! Then I’ll be able to do my cooking justice, and you’ll get to taste the local cuisine."
    scene ch6sc10_445 with dissolve
    ori "Join me in the dining area in about an hour, okay?"
    mc "Sure thing."
    ori "Oh! And tell the others as well. They must be famished from the jungle trek and swim."
    mc "Will do, and thank you, for making us all dinner."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_447 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    "You decide to head to the bath area below deck to check on Pearl."
    pl "Who’s there?"
    mc "Just your favorite sharky."
    pl "My sharkiiie! *Giggles*"
    scene ch6sc10_448 with dissolve
    pl "I’m glad you stopped by, I could actually use your hands."
    pl "Help a girl out? *Giggles* It’s hard to reach certain areas…"

    if pearl_relationship == True:
        mc "I can’t rightly refuse my mermaid when she needs my aid, can I?"
        scene ch6sc10_449 with dissolve
        pl "No, refusing your mermaid when she needs you…"
        pl "Is not something I’d advise, especially for my sharky."
        pl "Come, help me wash off?"
        scene ch6sc10_450 with dissolve
        "As you approach her, you carefully trace your fingers down her back and onto her hips."
        pl "*Giggles* T-That tickles! Mmh…"
        scene ch6sc10_451 with dissolve
        mc "This body of yours… should never be neglected."
        mc "I’ll have to be thorough."
        scene ch6sc10_452 with dissolve
        pl "*Gentle moan* Please… Ahh… I need you to be thorough…"
        pl "So… so thorough- Ahh…"
        scene ch6sc10_453 with dissolve
        pl "*Gasps* S-Sharky! Mmmh… you’re so deep between my… Aahhh."
        scene ch6sc10_452 with dissolve
        mc "Between your juicy cheeks… Mmh… I love this plump ass of yours."
        scene ch6sc10_453 with dissolve
        pl "My peachy… mmgh… is yours… only yours…"
        scene ch6sc10_452 with dissolve
        mc "It’s a good thing I stopped by, otherwise your peachy wouldn’t have gotten washed properly."
        scene ch6sc10_453 with dissolve
        pl "I’m so lucky- Aahh… I love how attentive you are with me."
        scene ch6sc10_451 with dissolve
        pl "Nooo! Why? Why did you stop?"
        mc "*Chuckles* Desperate for more?"
        pl "Uh-huh!"
        scene ch6sc10_450 with dissolve
        mc "Sorry, my little mermaid will have to wait, I came here to tell you that Orianna is making us all dinner."
        mc "It’s almost time and I’ve still got to go wake up Taz."
        pl "Nnngh! … *Sighs* Fine… but you better not think a little peachy rubbing is getting you off the hook."
        scene ch6sc10_452 with dissolve
        with vpunch
        pl "*Moans* {b}AahhhH! Mmmh!{/b}"
        "Sliding your hand between her cheeks, you penetrate her dripping wet pussy with just the tip of your index finger."
        scene ch6sc10_453 with dissolve
        mc "Don’t worry, I know you well enough to know that this will only drive you wild for later."
        scene ch6sc10_452 with dissolve
        pl "*Moans* Nnngh… you’ll be fucking my brains out later! Mmh!"
        scene ch6sc10_451 with dissolve
        mc "*Chuckles* Count on it. I’ll see you at dinner in ten."
        pl "Ten minutes?! But I have to dry off and everything!! Get out of here!"


    else:
        mc "No can do, dinner is about to be ready, I’m just gathering the troops."
        pl "Awwh… I was hoping I had at least another hour to bathe in!"
        mc "You have ten minutes, or I’m eating your portion."
        pl "Meanie!"

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "You head to the captain’s quarters to see if Taz has awoken yet."
    scene ch6sc10_454 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    mct "There she is."
    mct "*Chuckles* As expected, the jungle traversing and the swim really took it out of her."
    scene ch6sc10_455 with dissolve
    mct "I almost feel bad waking her up."
    mct "But she needs food in her system, otherwise she’ll be out of it for days."
    scene ch6sc10_456 with dissolve
    mc "She looks so peaceful, I wonder what she’s dreaming about?"
    mc "*Chuckles* Probably sweetrolls."
    scene ch6sc10_457 with dissolve
    mc "Hey… Taz? It’s time to wake up."
    tz "Hnngh…"
    mc "Taz, Orianna is making us all dinner, you’re hungry… aren’t you?"
    scene ch6sc10_458 with dissolve
    tz "*Groans softly* Mmh… [mc]? Am I still dreaming?"
    mc "It’s not a dream, I’m here to get you. We’re having dinner in a few."
    tz "Dinner? Mmgh… o-okay… that sounds lovely."
    scene ch6sc10_459 with dissolve
    tz "Almost as lovely as your touch…"
    tz "I’ll never get over how incredibly warm and comforting your hands feel."
    "Holding on to your hand, Taz begins to pull herself up and to her surprise, you pull her all the way."
    scene ch6sc10_460 with dissolve
    with vpunch
    tz "*Gasps* Aiiyh! [mc]!"
    tz "You’re so bad! *Giggles*"
    mc "What? Assisting a maiden out of bed is considered bad?"
    tz "*Giggles lightly* No… but making her feel certain ways just as she awakened… that is bad… very bad."
    tz "Lifting a woman straight out of bed and into your manly arms as if she weighs nothing… it stirs all sorts of feelings."
    scene ch6sc10_461 with dissolve
    mc "*Chuckles* Get your ass to the dining area, or I’ll toss you back into bed."

    if tz_relationship == True:
        tz "*Giggles* Is that a promise or a threat?"
        tz "Either way… I think I might like it!"
        mc "*Sighs* You’re hopeless."
        tz "Hopelessly in love with you! *Smiles warmly*"
        scene ch6sc10_460 with dissolve
        mc "I love you too, now let’s get your belly filled with a hearty meal."
        tz "Aye, aye! Captain!"

    else:
        tz "Okay, okay… let’s go!"

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "Orianna has set up the table in the Captain’s dining area, and you all gather around."
    scene ch6sc10_446 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    pl "This looks delicious, Orianna!"
    mc "*Gulp, gulp* Mmh… It’s been a hot minute since I’ve had ale."
    ori "Eat to your heart's desires everyone!"
    ori "With all we've been through as of late and with today's journey, our bodies need to be replenished."
    tz "Pearl’s right, this is amazing Orianna, how in all of Midomir did you manage this?"
    scene ch6sc10_462 with dissolve
    ori "[mc] told me there was a good deal of food in storage here, mostly vegetables but if you know how to utilize them-"
    ori "-You can manage to make a fulfilling meal, and they were kind enough to give us a few supplies for the journey from A’nai."
    tz "Truly amazing! I’m happy we found you."
    scene ch6sc10_463 with dissolve
    pl "{b}Mffhpfh!{/b}"
    tz "Seriously though, I can feel my energy returning with every bite. And I feel the flavors burst in my mouth!"
    ori "It’s nothing, really-"
    mc "She’s right, Ori. It tastes incredible, you’re a great chef."
    scene ch6sc10_464 with dissolve
    ori "[mc]..."
    ori "It pleases me that you like it."
    ori "I’m fully aware vegetables do not make the most exciting meal for a man."
    ori "So knowing that you enjoy it, it makes it worth it."
    scene ch6sc10_465 with dissolve
    mc "I’m enjoying it alright, like Taz said, it’s like a burst of flavor with each bite."
    mc "You really understand how to mix ingredients together to get the most out of them."
    mc "And the fact you’re downplaying cooking something this delicious?"
    mc "Makes me excited to see what you'll make for me in Arazalia."
    scene ch6sc10_466 with dissolve
    ori "*Giggles* I look forward to fulfilling your needs."
    ori "I mean-... fulfilling your hunger, yeah."
    scene ch6sc10_465 with dissolve
    mc "*Chuckles* As do I, Ambassador."
    scene ch6sc10_466 with dissolve
    ori "This is merely a small token of my thanks, for you guys rescuing me."
    ori "Sure, I didn’t live like a slave, but I was still a captive at the end of the day."
    scene ch6sc10_467 with dissolve
    pl "*Muffled* Kira’s life depends on your safe return… Mggh."
    pl "Leaving you on the island was not an option, I’d have killed every last one of them to bring you back."
    scene ch6sc10_468 with dissolve
    ori "Awh, you’re sweet Pearl..."
    ori "I know you don’t mean that literally, but I understand the sentiment."
    pl "..."
    mct "*Chuckles* Ori has no idea, Pearl literally would have slain every last one of them for Kira."
    scene ch6sc10_469 with dissolve
    tz "You’re cute Orianna! *Giggles*"
    tz "I say we let Orianna handle our meals, enroute to Looter’s Bay!"
    pl "*Stuffed mouth* Nnghh… agreed!"
    scene ch6sc10_462 with dissolve
    ori "I’d be happy to do so, I saw plenty of ingredients to make a delicious breakfast for us in the morning."
    ori "It’s the least I can do."
    ori "So don’t be shy about asking for anything in regards to food."
    scene ch6sc10_463 with dissolve
    ori "I have a great deal of experience with cooking in various parts of the world as I travel a whole bunch."
    ori "It kind of forces you to be versatile in the kitchen and pushes you outside your comfort zone."
    scene ch6sc10_469 with dissolve
    tz "It certainly has made you one helluva chef, Orianna! Mhm-hm!"
    tz "And you know what they say, the way to your lover's heart is through their stomach! *Giggles*"
    scene ch6sc10_470 with dissolve
    tz "Your husband must feel like he has won in life!"
    tz "Not only is his wife outrageously gorgeous but also a master chef!"
    ori "Oh! That’s-... that’s kind of you to say…"
    ori "But I’m afraid I have yet to find the man who will claim my heart and cooking."
    scene ch6sc10_465 with dissolve
    mc "The men in Arazalia don’t know what they are missing out on."
    mc "A woman like you shouldn’t be taken for granted."
    "You notice Orianna smiling happily at your remark."
    scene ch6sc10_466 with dissolve
    ori "[mc]... I-... thank you."
    $ ori_trust += 2
    ori "Your words mean a lot."
    "Orianna appreciates your sentiment about not taking her for granted, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
    scene ch6sc10_470 with dissolve
    tz "Well, If not a husband, then you must have a wife?! There’s no way you can be single!"
    ori "*Giggles* Taz! By the sands! I’m afraid I am as single as you can be."
    scene ch6sc10_471 with dissolve
    ori "Now, if you’re done reminding me how single I am, I need some ale!"
    tz "S-Sorry! *Snickers*"
    mc "Great, you’ve driven her to drinking. *Chuckles*"
    tz "I didn’t mean to!"
    scene ch6sc10_472 with dissolve
    pl "Nuuhh… it’s gone!"
    tz "That’s what happens when you eat it."
    pl "But… it was yumyum."
    scene ch6sc10_473 with dissolve
    tz "How about the three of us clean up?"
    tz "We shouldn’t allow Orianna to do so, not after making us this meal."
    pl "O-Okay… let’s clean up."
    mc "Sounds good, let’s get to it."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Pearl, Taz and yourself proceed to clean up and allow Orianna a moment of rest."
    scene ch6sc10_474 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "*Exhales* That was great, you really have no idea how hungry you are until the scent of a proper meal is nearby."
    mc "Orianna is a surprisingly great cook, a quality I value in a woman."
    scene ch6sc10_475 with dissolve
    mc "Speaking of what I value… it’s starting to bother me that I can’t reach Eliza through the Arcano-crystal."
    mc "I’m not worried per se, when I left we were about equal in physical strength, and she’s faster and more agile than me."
    mc "She can handle anything back home, it’s just… I guess I can’t help but still be a little concerned about her."
    scene ch6sc10_476 with dissolve
    mc "She’s my kitten after all, no matter how powerful she grows to become."
    mc "It’ll only be a few days until I see her again…"
    scene ch6sc10_475 with dissolve
    mc "To say I feel excited is an understatement."
    mc "I’m even looking forward to her overzealous hugs."
    mc "She probably has stored a whole bunch in her affection-vault..."
    scene ch6sc10_474 with dissolve
    mc "*Inhales deeply* The air really is magnificent out here on the open water."
    mc "I better go see what the girls are up to."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss57 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_477 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    "After having searched all over the ship, you finally find them in the Captain’s quarters."
    mc "Hey girls, what are you up to?"
    tz "[mc]! Lovely, you’re just in time! We were about to come get you."
    tz "We’re about to play a game that Pearl found stashed away under the Captain’s bed."
    scene ch6sc10_478 with dissolve
    mc "*Gulp* So, what are we playing?"
    tz "It's called {b}Shuffle-Showdown!{/b}"
    mc "Shuffle-Showdown? Hmm, I think my friend Borri likes to play this at taverns."
    tz "According to the rule set, each card has a different strength and weakness, and we will battle each other."
    tz "After each round, there is a penalty to the loser. Usually a loss of personal coin-"
    scene ch6sc10_479 with dissolve
    pl "-But since none of us actually have any coin out here, we’ve decided to spice up the penalty a tad! *Snickers*"
    mc "I have a feeling I know where this is going-"
    pl "-Loser strips one article of clothing per round!"
    scene ch6sc10_480 with dissolve
    pl "At the end of this game, you’re going to be butt naked! I’ll make sure of it! *Giggles*"
    tz "*Gasps* Pearl! You’re so naughty!"
    ori "*Snickers* Or maybe you’ll be the one with your butt out!"
    scene ch6sc10_479 with dissolve
    mc "*Chuckles* Challenge accepted, you little tease."
    scene ch6sc10_478 with dissolve
    tz "Okay, so I believe we will mix the cards upside down, and each take a turn to pick one for our deck."
    tz "Then we are supposed to choose an opponent amongst the players and you each put forth a card."
    tz "Then the card’s strength will determine the winner, sounds simple enough."
    scene ch6sc10_479 with dissolve
    pl "What do you say? Ready to get naked?"
    scene ch6sc10_481 with dissolve
    mc "Let’s do it."
    ori "Okay, first we’ve got to flip all the cards and mix them together."
    tz "Then we’ll take turns adding one to our decks!"
    mc "Who starts picking?"
    scene ch6sc10_482 with dissolve
    ori "I’ll go first."
    mc "Sounds good to me."
    pl "I wanted to go first…"
    mc "You can go second."
    scene ch6sc10_483 with dissolve
    pl "Great!"
    pl "{b}My turn!{/b}"
    pl "*Snickers* I got a good one!"
    scene ch6sc10_484 with dissolve
    tz "My turn!"
    tz "Uh-uh! Pearl I think I’ve got you beat!"
    tz "Get ready to get naked!"
    mct "*Chuckles* These girls talking smack before we have even gotten all our cards."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Everyone continues taking turns and trying to sus each other out until eventually all the cards have been dealt."
    scene ch6sc10_485 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "Okay, let’s see what I’m working with."
    mct "‘The Devil’ Seems like a powerful card to have, what else… hmm, ‘Justice’ that one could prove handy as well."
    mct "Next I have ‘The World’ that one could have a wide range of meanings, won’t really know until I play it."
    mct "And lastly, I’ve got ‘Death’ that has to be the strongest card? What can evade death?"
    mc "Alright, girls. Let’s start this battle for our clothing."
    scene ch6sc10_486 with dissolve
    pl "Very well then! I Challenge you, {b}[mc]!{/b}"
    pl "Think you can handle me, tough guy?"
    pl "*Snickers* Loser loses an article of clothing as you well know, and you {b}only{/b} have pants on."
    mc "I look forward to watching you strip while you eat your own words, game on."
    scene ch6sc10_487 with dissolve
    pl "I play Temperance, I feel like this is a fitting card against you. *Snickers*"
    mc "*Chuckles* That was a horrendous joke, and just for that I’m going to play…"
    scene ch6sc10_488 with dissolve
    mc "The Devil."
    with vpunch
    pl "*Gasps* You got {b}The Devil!?{/b}"
    pl "Taz, you have the rule scripture, how are we matched?"
    scene ch6sc10_489 with dissolve
    tz "Sorry Pearl, he’s got you beat."
    tz "The Devil manipulates and deceives Temperance, into indulging their deepest, darkest self."
    ori "Sounds like he got you good! *Giggles*"
    pl "Ugh! I can’t believe Temperance is so weak! Hnngh…"
    mct "Playing one of my most powerful cards early… worth it. *Chuckles*"
    mc "Pearl, it’s time to get naked."
    scene ch6sc10_490 with dissolve
    pl "[mc]! This-... this was just a warm up, right?!"
    pl "Mercy? I plea for mercy!"
    scene ch6sc10_491 with dissolve
    mc "Your plea for mercy might’ve worked a little better if I didn’t know how good your little innocent act is."
    pl "Hnnnfh!"
    mc "Get. Naked."
    scene ch6sc10_492 with dissolve
    pl "F-Fine!"
    pl "I won’t let it be known that I will go back on a challenge."
    scene ch6sc10_493 with dissolve
    pl "I can’t believe you had ‘The Devil’ *Snickers* You are a {b}devil!{/b}"
    pl "But… you beat me."
    pl "You want to see tits, I will show you tits…"
    scene ch6sc10_494 with dissolve
    pl "Here you go… you’ve earned them, at least they make the winner smile…"
    mc "*Chuckles* Obviously."

    if harem_path == True:
        pl "*Giggling* Do they manage to stir something in your pants? Even after claiming a whole island?"
        pl "You're the harem king, what's the verdict of a man who sees as many tits as you?"
        mc "You know they do... your breasts are in a league of their own."
        mc "Now sit your peachy down so we can get you fully naked."

    else:
        pass


    scene ch6sc10_495 with dissolve
    mct "Okay, I’ve got Justice, The World and Death left."
    ori "Pearl, I challenge you."
    pl "It’s on! *Giggles* I’ve never seen a woman from Arazalia naked before!"
    scene ch6sc10_496 with dissolve
    ori "You didn’t learn anything from talking smack to [mc]? It’ll only make beating you that much more rewarding."
    tz "Girls, play your cards already! I want to challenge [mc]!"
    scene ch6sc10_497 with dissolve
    ori "I play The Star."
    pl "And I play The Hanged Man!"
    pl "Which one beats who, Taz?"
    tz "Hmm, let me see… The Star is a potent card-"
    ori "*Snickers* I knew it! Lose those panties Pearl."
    tz "Hold on, you didn’t let me finish… The Star is potent but ineffective against the dead. The Hanged Man wins."
    scene ch6sc10_498 with dissolve
    pl "Boasting too early? Shame on you Orianna."
    pl "Time to show us those exotic breasts of yours!"
    scene ch6sc10_499 with dissolve
    ori "I’ll get you in the next round…"
    pl "Yada-yada, get naked! *Snickers*"
    ori "You think I won’t do it?"
    scene ch6sc10_500 with dissolve
    ori "You want to see my breasts that badly?"
    $ renpy.pause()
    scene ch6sc10_501 with dissolve
    $ renpy.pause()
    ori "{b}Here!{/b}"
    scene ch6sc10_500 with dissolve
    pl "{b}H-Hey!{/b}"
    scene ch6sc10_501 with dissolve
    ori "*Snickers* What, you’ve seen them? Once wasn’t enough?"
    scene ch6sc10_500 with dissolve
    pl "You better keep them out!-"
    scene ch6sc10_501 with dissolve
    ori "Hmmm!"
    ori "Fine. I guess I will keep you company in being naked."
    scene ch6sc10_502 with dissolve
    ori "Let’s get this thing off."
    mc "By all means… take your time. *Chuckles*"
    pl "Don’t stare at her tits! Look! I’ve got mine out as well!"
    scene ch6sc10_503 with dissolve
    ori "Don’t be jealous Pearl, you said it yourself, I’m exotic to you guys."
    ori "You can’t fault him for having a look."
    mc "You look stunning, Ori."
    ori "*Giggles* Thank you… I’m glad I didn’t strip for nothing."
    tz "Stop showing off your perfectly perky breasts! It’s my turn to challenge [mc]!"
    scene ch6sc10_504 with dissolve
    mct "Tazzy is eager to challenge me, she must have a card she believes can beat me."
    mct "I’m sure my strongest card is Death, but do I really want to play it this early?"
    mct "The World seems like a more all purpose card and Justice seems like it would counter specific cards."
    mct "Fuck it, I have no idea what she’ll play anyway, it’s a gamble at this point."
    mc "Okay, I’m ready."
    scene ch6sc10_505 with dissolve
    tz "Great! I’ll play The Emperor."
    tz "Don’t worry girls, I’m about to strip [mc] naked and we’ll finally get something to enjoy! *Snickers*"
    pl "Get him Taz!"
    ori "That would be lovely… I’m… rather curious."
    scene ch6sc10_506 with dissolve
    mc "Hmm, I’ll play Justice."
    mc "To tip the scales in my favor and bring your Emperor to heel."
    pl "Uh-oh! What does this mean Taz?! Did he beat you?"
    scene ch6sc10_507 with dissolve
    tz "Hold on, I need to check our match-up."
    tz "Hmmh… Emperor… Justice… okay here it is!"
    tz "The mighty Emperor is above the law and as such, he is able to avoid Justice, instead he wields Justice as his personal tool."
    scene ch6sc10_508 with dissolve
    ori "*Giggles* Sounds like she’s got you beat."
    pl "Totally! Strip!"
    tz "Emperor blows Justice out of the water, how unfortunate… for you. *Snickers*"
    mc "*Sighs* Alright… alright."
    scene ch6sc10_509 with dissolve
    mc "You won fair and square."
    mct "I knew I should’ve gone with Death, I could have killed her Emperor with ease."
    pl "{b}Strip! Strip! Strip!{/b}"
    scene ch6sc10_510 with dissolve
    mc "Happy?"
    pl "Yes! *Snickers* {b}Very big and happy!{/b}"
    ori "*Gasps* Ohh… mmh… you’re… {b}beautiful{/b}."
    tz "*Giggles* He sure is! You can thank me later girls! I’ll take as many sweetrolls as you can bring me!"

    if tz_relationship == True:
        mc "*Chuckles* Oh you’re getting something later Taz, and it won’t be a sweetroll."
        scene ch6sc10_511 with dissolve
        tz "*Bites lip* Mmh… there’s only one thing that matches sweetrolls…"
        tz "And I’m looking at it, Nnngh."
        mc "Alright girls, let’s continue."

    else:
        mc "Alright, let’s continue."

    scene ch6sc10_512 with dissolve
    "And so, with everyone in high spirits and more comfortable being naked with each other…"
    "The game continues… the girls enjoy talking smack across the table as they duel."
    scene ch6sc10_513 with dissolve
    "And so, one by one…"
    "Match after match…"
    scene ch6sc10_514 with dissolve
    $ renpy.pause()
    "The girls continue to lose a piece of clothing."
    "With each mug of ale, they are less and less timid about stripping in front of everyone."
    "Instead they start taking pride in showing off their bodies, especially as you praise them."
    scene ch6sc10_515 with dissolve
    "With nothing left to lose on your end, you challenge Taz to another match."
    "This time, her card was no match against yours and as such it was finally time for her to strip for you."
    scene ch6sc10_516 with dissolve
    $ renpy.pause()
    "She does not object to this matter, in fact she seems pleased to finally reveal her large shapely breasts to you."
    "With the biggest breasts in the group, she feels at ease having them out in front of the others, enjoying your gaze."
    scene ch6sc10_517 with dissolve
    "Orianna loses to Pearl and as such…"
    "The time for her skirt to come off has arrived, she shyly moves herself behind her chair."
    scene ch6sc10_518 with dissolve
    "But she follows through, if it weren’t for the dim lighting, you would be able to notice a blush across her cheeks."
    "Taz, sensing how nervous Orianna is about being fully naked in front of you for the first time, asks her to sit down."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_519 with Dissolve(1.5)
    play music action_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "The time for the final round has arrived… the match-up is Taz against you."
    "The battle for her panties or you climbing the mast of the ship, naked."
    mct "We’ve each only got one card left."
    mct "I can’t lose this… over my dead body will I be climbing the mast whilst naked, with all of them watching…"
    scene ch6sc10_520 with dissolve
    tz "Final match of the evening, I’ll go first."
    tz "I play… The High Priestess."
    mc "Not bad…"
    mc "I'm sure she is well protected by the gods..."
    scene ch6sc10_521 with dissolve
    mc "But I doubt she beats Death. After all, even gods can't protect against such an entity."
    tz "{size=+10}*Gasps* {b}!!{/b}{/size}"
    ori "You had Death?! You really have had a stacked deck [mc]."
    pl "{b}Who wins?!{/b}"
    scene ch6sc10_522 with dissolve
    tz "*Sighs deeply* [mc] wins."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    tz "Shame, I was hoping I could’ve beaten him a 2nd time."
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc10_523 with dissolve
    mc "*Chuckles* Go on, be a good little chronicler and strip."
    tz "Sorry girls, I really hoped we’d get to see him climb the mast… but instead…"
    scene ch6sc10_524 with dissolve
    $ renpy.pause()
    tz "He gets this."
    mc "Now that’s what I call a prize."
    scene ch6sc10_525 with dissolve
    tz "You like your prize?"
    mc "I’m pleased with my prize, yes."
    scene ch6sc10_526 with dissolve
    ori "I must say… despite this being a little outside my comfort zone, it was quite fun!"
    ori "It’s healthy to have a few boundaries pushed once in a while, especially if you’re amongst people you trust."
    mc "I fully agree, you girls definitely have a way of making things interesting."
    scene ch6sc10_527 with dissolve
    ori "I shall retire for the evening, a full night’s rest is what I’m craving."
    mc "You’ve earned it, Sweet dreams."
    ori "[mc], thank you… I’ll see you all in the morning then."
    evr "Goodnight Ori!"
    $ renpy.pause()
    scene ch6sc10_528 with dissolve
    pl "Mhm-hm, I think I’ll retire as well."
    pl "The journey here… my bath earlier… Ori’s feast… the ales… I’m about to pass out."
    mc "Go on, little mermaid. If you end up sleeping in, in the morning… I’ll come get you when breakfast is ready."
    scene ch6sc10_529 with dissolve
    pl "*Giggles* You’re so good to me… thank you."
    pl "I’ll go up to the helm and make sure we’re still on course for Looter’s Bay, then I’ll head to bed as well."
    mc "Yeah… sounds good… goodnight Pearl."

    if tz_relationship == True:
        scene ch6sc10_530 with dissolve
        tz "Hey… she might have a great ass..."
        tz "But you still have one naked woman in the room with you."
        scene ch6sc10_531 with dissolve
        tz "I think… she deserves your attention, don’t you?"
        mc "Mhm, she definitely does."
        mc "I was merely waiting for her to leave to turn my attention to you… knowing full well what happens when I do."
        scene ch6sc10_532 with dissolve
        tz "*Moans* Aahh… how I’ve been hungering for your touch…"
        tz "Getting to see you strip for me… presenting us all with that big cock of yours… only increased my desire."
        mc "How do you think I felt… having to gaze upon this gorgeous woman across the table from me…"
        mc "Constantly out of arm's reach… yet always within my sight… serving only to keep me hard through the entire evening."
        tz "Now that I am within your reach… what are you going to do about it? Mr.Nephilim."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch6sc10_533 with dissolve
        with vpunch
        tz "*Squeals* Aiiyh! [mc]! Mmh!"
        "You grab her firmly and pull her on top of you, she squeals in pleasure as your hard cock enters her tight, wet pussy."
        tz "*Moans* Mmh… you promised I’d get a treat later… I’m enjoying my treat very much-Aahh…"
        tz "I was jealous during your crowning ceremony… all of the women got a chance to breed with you if you desired…"
        tz "Yet I had to wait, since I was not a part of the tribe… I’m done waiting, [mc]."
        tz "It's my turn to breed you now! And I will breed you fully!"
        scene tz_lewd23 with dissolve
        "Taz lives up to her words, she does not hesitate to begin riding you swift as the wind."
        $ renpy.pause()
        tz "*Moans* Oh gosh-dolly! {b}OH!!{/b} This is- Ahh! This is sooooo much better than the juicest sweetrolls!"
        mc "Mmgh-Nngh! Fuck I had almost forgotten just how tight and juicy your little pussy is- Mmgh!"
        with vpunch
        tz "Tell me [mc]- ahh! Tell me my pussy is better than a sweetroll! {b}Aiiyhh!{/b}"
        with vpunch
        mc "Your pussy is better than any sweetroll I could possibly imagine- {b}Ahhh!{/b}"
        with vpunch
        tz "I’m going to- {b}Aiiiyh!! I’m cumming [mc]!! Your cock is amaaaazing!!{/b}"
        scene tz_lewd24 with dissolve
        $ renpy.pause()
        "Despite climaxing, she continues to ride you through her orgasm, forcing you to experience intense pleasure."
        tz "{b}Aahh! [mc]!{/b} Do you feel me?! Aiiyhh! Do you feel how tight and wet I am for you?"
        with vpunch
        mc "Hnngh! Yeah- {b}fuck! Mmgh! Taz!{/b}"
        with vpunch
        tz "That’s it! You’re on the edge! {b}AhH!!{/b} Cum inside me! Claim my pussy as you have before!"
        scene ch6sc10_534 with dissolve
        with vpunch
        "Her intense riding and juicy pussy works perfectly together with her moans to send you far over the edge, filling her up completely."
        scene ch6sc10_535 with dissolve
        with vpunch
        tz "{b}*Moans loudly* AAHH! AiiYHYH!! [mc]!!{/b} You’re filling me!! I love having you inside me!!"
        mc "Fuck you’re incredible Taz… Mmgh! Such a tight and warm pussy."
        scene ch6sc10_536 with dissolve
        tz "*Panting* I can’t believe we haven’t been intimate since sharing a bed in Arugoh…"
        tz "Breed me on the table!"
        tz "You’re not leaving this room until you have filled me with your delicious cum at least three times!"
        scene ch6sc10_533 with dissolve
        mc "You’ve become wild with lust… I can’t blame you, I’ve been eager to fuck you again as well."
        scene ch6sc10_537 with Dissolve(1.5)
        $ renpy.pause(0.7)
        with vpunch
        tz "{b}*Moans* AiiyhH! Yes! Take me right here on the table baby!{/b}"
        scene tz_lewd25 with dissolve
        $ renpy.pause()
        tz "{b}Ooh-OH!! Fffuu!!{/b} Oh this is exactly what I hoped it would feel like- Ahhh! To be fucked by the man I love on a table!"
        mc "Mmgh! You’re already on the verge of another orgasm? {b}Fucking hell Taz! Mmgh!{/b}"
        with vpunch
        tz "That’s it! Mmh! Make me cum all over that big cock of yours! Make me fall in love with you all over again!"
        with vpunch
        "You penetrate her further and her body gives itself over to your cock, reaching another orgasm."
        with vpunch
        tz "*Moans* {b}Aahh!! Yes!! Oh sweetest sweetroll!! AHhH!{/b}"
        scene ch6sc10_537 with dissolve
        mc "Mmmgh… get on your side, we’re not done with the table yet."
        scene ch6sc10_538 with dissolve
        tz "*Moans* Aahh… like this my love? Is this how you want your chronicler?"
        mc "Yeah.. mmh… this is perfect."
        scene tz_lewd26 with dissolve
        $ renpy.pause()
        tz "{b}*Moans* Aah-aahh!{/b} Oh you’re so deep like this! Mmmh!"
        tz "I can’t believe you’re breeding me right here on the table… on top of all our playing cards!- {b}Aahhyh!!{/b}"
        mc "Five hells… how you can be this tight whilst being soaking wet is beyond me… but I love it- Ahhh…"
        with vpunch
        tz "Only for you baby! Ahh! {b}{size=+10}OH MY!!{/b}{/size} Your cock is too hard- AHh! I’m going to cum again! Please {b}{size=+10}CREAMPIE ME!{/b}{/size}"
        scene ch6sc10_538 with dissolve
        with vpunch
        mc "{b}Fffuu! MMgh! I can’t hold back- Mmmh!{/b}"
        scene ch6sc10_539 with dissolve
        with vpunch
        tz "Oh I feel you!! Mmgmh! {b}I feel all of you!!{/b}"
        tz "*Panting happily* You just creampied my sweetroll for the 2nd time in a row."
        mc "Sweetrolls are best when filled after all. *Chuckles*"
        tz "Mmh… totally agree! I’m afraid my pussy has had all that it can handle tonight…"
        tz "So why don’t you fuck my mouth?"
        scene ch6sc10_540 with dissolve
        tz "It too deserves to be filled with your cum, wouldn’t you agree?"
        mc "I would… we don’t want to neglect that naughty mouth of yours."
        tz "Mmmh... [mc]... fuck my mouth while your cum leaks from my pussy!"
        scene tz_lewd27 with dissolve
        $ renpy.pause()
        tz "*Muffled sucking* {b}Mmgh-Nngh!{/b} I can taste your cum and my juices on your cock- {b}Mmgh!{/b}"
        mc "Be a good chronicler and clean my cock before I fill your throat."
        tz "*Muffled sucking* {b}Nngh-Nngh!{/b} Of course! Mmgh… I love feeling your warm cum leaking out of my pussy as I suck your cock."
        with vpunch
        tz "Mmgh… fill my mouth baby… send me to bed with a pussy and mouth filled with your cum! {b}Mmgh!{/b}"
        scene ch6sc10_541 with dissolve
        with vpunch
        mc "Aahh! As you wish- Fuck! Mmgh! I’m going to-"
        scene ch6sc10_542 with dissolve
        with vpunch
        tz "*Choking and sucking* {b}Gghh-mmgh! Hhghhr!! Mmh!!{/b}"
        tz "Tthhank you babhyy… mmmgh!"
        mc "Mmgh… you’re most welcome."
        scene ch6sc10_543 with dissolve
        tz "*Panting* Mmmgh… you’re certainly better than a sweetroll! *Giggles happily*"
        mc "We really made a mess… *Chuckles*"
        tz "I’m too happy and exhausted to be bothered… our sex sweat is all over the cards at this point."
        tz "You go rest baby… I’m gonna take a moment to enjoy your cum before I go wash off."
        scene ch6sc10_544 with dissolve
        mc "I’ll see you in the morning then, goodnight Taz."
        tz "*Giggles* Goodnight [mc], I love you."
        mc "I love you too."
        $ tz_trust += 5
        "Tazzy feels herself falling more and more in love with you, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."

    else:
        scene ch6sc10_530 with dissolve
        tz "I think the others are on point, we should probably go get some rest as well?"
        mc "Yeah, I’m longing to lie down and just drift off."
        tz "Y-Yeah… me too. I’ll see you in the morning, Mr.Nephilim."
        mc "Yeah, sweet dreams, Taz."

    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss39 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_545 with Dissolve(2.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ec "Listen up everyone."
    ec "Kisha and I summoned you this morning due to recent news unfolding."
    scene ch6sc05_350 with dissolve
    ec "We have several huntresses that are missing."
    scene ch6sc05_352 with dissolve
    ec "Young Vex here and Miyo have informed me of this."
    ec "Miyo’s older sister Aiyo and several others from the previous Arugoh members went missing within the last couple of weeks."
    scene ch6sc05_351 with dissolve
    sj "Missing? Sure one huntress could get lost in the mist and possibly fall injured."
    zy "But if several have gone missing, that suggest something larger is at play."
    scene ch6sc05_361 with dissolve
    vx "Wait… are you saying someone could have done this to them?!"
    vx "Who would even do such a thing? Or even be capable of taking down several huntresses?!"
    scene ch6sc05_362 with dissolve
    ks "Vex! You’re a huntress now, act like one."
    ks "Do not let your emotions interfere with the information you are being presented with."
    scene ch6sc05_363 with dissolve
    sj "Kisha speaks true, Vex."
    sj "We do not know what has happened, we shouldn’t jump to conclusions."
    scene ch6sc05_364 with dissolve
    sj "But we will discover their fate."
    sj "This I promise you."
    vx "*Nods* Mhm."
    scene ch6sc05_365 with dissolve
    vx "*Sighs* O-Okay… I’m just worried about them."
    vx "What if it was Jimun? If they crossed paths with him before [mc] took him down, they wouldn’t have stood a chance."
    scene ch6sc05_352 with dissolve
    ec "It is impossible to know as of yet."
    ec "Remember young one, we lived our entire lives without encountering Jimun."
    scene ch6sc05_350 with dissolve
    ec "Sure, they could have… but I suspect something else is going on."
    scene ch6sc10_545 with dissolve
    ec "I have inquired about this matter with Sivir and Riven."
    ec "They have both been open about what went on, Aiyo led a group of three huntresses into the northern section of Aruna."
    ec "Near the great fire mountain."
    ec "It’s a mostly undiscovered location, especially to us here at the south."
    ec "But even the Arugoh up at the north knew little about what lies north of their previous location."
    ec "They reported that the mist appears at more frequent intervals and remains for longer as well."
    ks "Which means the area would not only be dangerous but also near impossible to navigate within."
    scene ch6sc05_352 with dissolve
    ec "This is why the four of you will be mounting an expedition, with Kisha as your leader."
    ec "Your objective is to scout the area of the Arugoh tribes previous camp and to the north."
    scene ch6sc05_350 with dissolve
    ec "But let me be clear, if you encounter the mist to the north, you do not press on."
    ec "This expedition is to search for clues, and hopefully find the missing huntresses."
    scene ch6sc05_352 with dissolve
    ec "But you all know that if the tribe were to lose the four of you, the tribe would be but a shadow of its former self."
    scene ch6sc05_351 with dissolve
    sj "We won’t let you down, A’nu."
    zy "We will be alert and bring back anything we find."
    vx "T-Thank you! A’nu!"
    scene ch6sc10_545 with dissolve
    ks "None of us has ever ventured that far north."
    ks "I expect all of you to be at your best."
    ec "You will use the Arugoh village as your base of operations, set up camp there and work your way forward from it's location."
    ec "Go on, pack your supplies for the journey and grab a fulfilling breakfast before you set out."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss29 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)

    if pearl_relationship == True:

        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        "You feel something… warm…"
        scene ch6sc10_546 with Dissolve(2.5)
        $ renpy.pause(0.5)
        "A feeling you’re intimately familiar with…"
        "*Soft moans* {size=-10}{b}Aahh…{/b}{/size}"
        scene ch6sc10_547 with dissolve
        "A sensation of pleasure surrounding you."
        "*Soft moans* {size=-10}{b}Aahh…{/b}{/size}"
        scene ch6sc10_548 with dissolve
        "The citrusy scent of a woman who you care deeply for is filling the air."
        "*Soft moans* {size=-10}{b}Aahh-ahh…{/b}{/size}"
        scene pl_lewd68 with Dissolve(1.5)
        $ renpy.pause()
        mc "*Moans quietly* {size=-10}Mmh… Pearl?{/size}"
        pl "*Moans quietly* {size=-10}Shh- Aah… we don’t want to wake up Tazzy… Nnghh…{/size}"
        mc "*Moans quietly* {size=-10}She’s next to us? Aah-... fuck…{/size}"
        pl "*Moans quietly* {size=-10}I wanted to give you some nice dreams… Mmmgh… did it work?{/size}"
        mc "*Moans quietly* {size=-10}Fuck… yeah… mmh… feeling you ride me slowly like this… perfect way to awaken.{/size}"
        scene pl_lewd69 with Dissolve(1.5)
        $ renpy.pause()
        mc "*Moans quietly* {size=-10}Pearl-... hnngh… this is too risky, she could easily wake up-{/size}"
        pl "*Moans quietly* {size=-10}Shh… ahh… just let it happen.{/size}"
        pl "*Moans quietly* {size=-10}Let me enjoy you- Mmmh… while you enjoy me.{/size}"
        mc "*Moans quietly* {size=-10}Mmgh… you feel amazing… what a way to wake up…{/size}"
        scene pl_lewd70 with Dissolve(1.5)
        $ renpy.pause()
        mc "*Moans quietly* {size=-10}Fuck…"
        pl "*Moans quietly* {size=-10}Do you like this? Making love like this? Aahh…{/size}"
        pl "*Moans quietly* {size=-10}It feels so intimate to me… Mmh…{/size}"
        mc "*Moans quietly* {size=-10}Y-yeah- fuck… I’m loving every second of this… the way you’re taking your time massaging me into your pussy…{/size}"
        mc "*Moans quietly* {size=-10}It sends ripples of pleasure through my entire body… mmh…{/size}"
        pl "*Moans quietly* {size=-10}I’m not stopping until you fill me with your delicious cum… Aah…{/size}"
        pl "*Moans quietly* {size=-10}You’re pulsating… Sharky, give it to me. I-mmmgh! I’m about to cum with youuu-Aahh...{/size}"
        scene ch6sc10_549 with dissolve
        mc "*Moans quietly* {b}{size=-10}Fffuuh-... Pearl- Aahh… I’m going to-{/b}{/size}"
        scene ch6sc10_550 with dissolve
        with vpunch
        pl "{b}*Moans softly* {size=-10}Aahh… yes… I feel it… be a good sharky and fill your mermaids pussy-Aah…{/b}{/size}"
        with vpunch
        pl "*Moans quietly* {b}{size=-10}Fill me as Tazzy is sleeping right beside us- Aah… fill me at the thought of me making love to you while you sleep… Ahh…{/b}{/size}"
        mc "*Moans quietly* {b}{size=-10}Mmmgh… fuck Pearl… you’re unreal…{/b}{/size}"
        scene ch6sc10_551 with dissolve
        pl "Mmmh… so are you…"
        pl "Mmh… my handsome sharky. I love you… so much."
        scene ch6sc10_552 with dissolve
        "With your cock still deep inside of her, Pearl leans down and merges her soft lips with yours, kissing you intimately."
        pl "Mmh-mmh… {b}I love you, [mc].{/b}"
        mc "I love you too, Pearl. Mmmh…"
        scene ch6sc10_551 with dissolve
        pl "*Speaks softly* Orianna is making breakfast at the moment, I’ll go see if she needs a hand."
        pl "You continue to rest, I’ll come wake you and Tazzy when it’s ready."
        scene ch6sc10_552 with dissolve
        pl "*Kisses* Mmmh… just one more to make you have nice dreams… nnnh…"
        mct "Mmh… I love how she rests her breasts on my chest while leaning on me."
        mc "You always know how to provide me with the best dreams… my sexy little mermaid."
        scene ch6sc10_551 with dissolve
        pl "See you soon… Sharky. You can dream of how your warm cum will run down my thighs as I assist Ori in the kitchen."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        "With that vivid imagery, Pearl takes her leave, and you drift back to sleep."
        "After a good thirty minutes of rest, Pearl comes to get you and Taz as breakfast is ready."

    else:
        scene black

    scene ch6sc10_553 with Dissolve(2.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    tz "Mh! This is just as delicious as what you cooked for us last night, Ori!"
    pl "{b}Mhm-hm!!{/b}"
    ori "Awh, I’m glad you guys like my cooking, even with the limited supplies here."
    ori "I had help this morning though, Pearl assisted me in the kitchen."
    scene ch6sc10_554 with dissolve
    ori "We agreed it was best to allow you and Tazzy to sleep in."
    ori "Tazzy isn’t used to all this traveling and you have been through so much recently."
    scene ch6sc10_555 with dissolve
    mc "*Chuckles* Thank you, Ori. That’s very thoughtful of you."
    mc "But honestly, I feel on top of the world as of late… the company of you girls has a way of elevating me."
    scene ch6sc10_554 with dissolve
    ori "Awwh, that’s sweet of you to say."
    ori "I’m glad our presence can lift your spirits."
    scene ch6sc10_555 with dissolve
    mc "You do, as you well know traveling can often be rather a lonesome affair."
    mc "But being able to travel with a group of people I enjoy being around? That is something I haven’t had much of in life."
    scene ch6sc10_556 with dissolve
    ori "I look forward to when your travels bring you to Arazalia…"
    ori "I intend to do my best to make it an enjoyable and unforgettable experience for you."
    scene ch6sc10_557 with dissolve
    mc "I have the utmost faith that a woman of your caliber will manage to do just that."
    "Orianna giggles warmly, clearly happy with you believing in her ability to impress you."
    scene ch6sc10_556 with dissolve
    ori "I have no intentions of disappointing my rescuer and hero."
    scene ch6sc10_554 with dissolve
    ori "How are you liking breakfast? It’s not too salty?"
    scene ch6sc10_555 with dissolve
    mc "No, it’s great."
    mc "Maybe a bit more pepper would’ve been welcome but that’s just nitpicking."
    scene ch6sc10_554 with dissolve
    ori "I’m afraid we used up the last bit of pepper for the meal last night."
    ori "I attempted to substitute it with a few other spices, but you seem to have a keen sense of taste."
    scene ch6sc10_555 with dissolve
    mc "Mhm, I do. It can be both a curse and a blessing at times."
    scene ch6sc10_556 with dissolve
    ori "Oh? I better try extra hard when you visit me then, I won’t have my cooking lacking then."
    ori "And I look forward to experiencing just how advanced your sense of taste is…"
    scene ch6sc10_557 with dissolve
    ori "*Snickers* …"
    mct "*Chuckles* I have a feeling I know what she is insinuating."
    scene ch6sc10_553 with dissolve
    ori "So, what is the plan today? We still have one day left before we reach Looter’s Bay, correct?"
    pl "Mhm-hm! Correct!"
    pl "By my estimates and if the wind remains steady, we’ll arrive tomorrow morning."
    tz "Awesome! I look forward to meeting your sister, Pearl."
    pl "She’s great! You’ll love her."
    mc "I guess we can just hang out today, there’s no point doing maintenance on the ship as we’ll be returning it tomorrow."
    pl "Agreed, we’ve earned a relaxing day!"
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss4 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_558 with Dissolve(2.5)
    play music happy_1 fadein 1.0
    $ renpy.pause(0.5)

    #stop music fadeout 1.0
    pl "I’m going for a swim!"
    pl "Feel free to join me! But only if you can keep up with the pace of the ship!"
    scene ch6sc10_559 with dissolve
    ori "Is she always this…"
    tz "Impulsive? Oh definitely!"
    tz "She knows how to get the most joy possible out of any situation she seems to be in."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "As Pearl enjoys a good dive, you join Orianna by the helm."
    scene ch6sc10_560 with Dissolve(2.5)
    $ renpy.pause(0.5)
    mc "You look great behind the wheel."
    ori "*Giggles* Are you saying I make a hot captain?"
    ####Choice####
    menu:
        "A smoking hot captain.":
            scene ch6sc10_561 with dissolve
            mc "A hot captain would be a grave understatement."
            $ ori_trust += 3
            "Orianna enjoys your compliment, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

        "You make a competent captain.":
            scene ch6sc10_561 with dissolve
            mc "You definitely make for a competent captain."
            $ ori_trust += 1
            "Orianna enjoys your compliment, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

    mc "You look like you’ve done this before?"
    scene ch6sc10_562 with dissolve
    ori "Once or twice."
    ori "When you spend as much time on ships as I do, it’s nice to understand how they operate."
    scene ch6sc10_561 with dissolve
    mc "Yeah. I agree, I just recently learned how to steer a ship myself."
    ori "In that case…"
    scene ch6sc10_562 with dissolve
    ori "Why don’t you help me steer for a little?"
    ori "A girl can only handle a wheel for so long before her arms give out… *Giggles*"
    mct "*Chuckles* Playing the innocent ‘help a girl out’ card?"
    mct "I could play along or I could dodge her attempt at flirting."
    ####Choice
    menu:
        "Sure, I’ll help you out. ({color=#ff8cdd}Romance{/color})":
            mc "Your arms are getting tired you say?"
            scene ch6sc10_563 with dissolve
            mc "What kind of a man would I be if I didn’t help ease your burden. Here, I’ll lend you my hands."
            $ ori_path = True
            ori "*Gasps* Oh! T-That would work I believe."
            scene ch6sc10_564 with dissolve
            ori "Being assisted by you really is invigorating my body…"
            scene ch6sc10_563 with dissolve
            mc "Mmh… you’re doing well, just keep her nice and steady."
            scene ch6sc10_564 with dissolve
            ori "L-Like this? Ohh… you like my steering?"
            scene ch6sc10_563 with dissolve
            mc "Yeah… you’re great at sailing."
            scene ch6sc10_565 with dissolve
            ori "I know you liked what you saw last night…"
            mc "Do you now? What makes you say that?"
            scene ch6sc10_566 with dissolve
            ori "You enjoy exotic women…"
            ori "Your eyes lit up when I revealed myself from underneath my clothes."
            scene ch6sc10_565 with dissolve
            ori "Aahh… your cock was hard unlike any I’ve ever seen… as it is now."
            mc "Mmh… I can’t deny your words…"
            scene ch6sc10_566 with dissolve
            ori "I was hoping that would be the case… Mmh…"
            mc "When are you going to stop teasing me and let me have what I desire?"
            ori "When you come to Arazalia… Nghh… I want to ensure you will visit me."
            scene ch6sc10_565 with dissolve
            mc "You want to be claimed in your own bed?"
            ori "I promise it’s a lovely bed. *Giggles*"
            scene ch6sc10_566 with dissolve
            mc "It better be… but I have a feeling you’re the type of woman who is worth the wait."
            ori "I can assure you that I am… mmh… women in Arazalia are highly valued, a woman of my position? Even more so."
            scene ch6sc10_564 with dissolve
            ori "I’ve had to fend off countless suitors in my time, none of them appealed to me in the slightest."
            ori "I had almost given up hope to find a partner…"
            scene ch6sc10_563 with dissolve
            ori "And then you waltzed right into my life… mmgh… showing me what a real man is."
            ori "Rescuing me… uniting a whole people, earning their respect and admiration."
            scene ch6sc10_564 with dissolve
            ori "It’s taking all my- Aahh… all my self control not to drag you downstairs and let you have me right here and now."
            mc "Mmh… I know how you feel, but I don’t mind waiting, as I said… I believe you are worth it."
            scene ch6sc10_562 with dissolve
            "You release her waist from your grasp."
            ori "That was lovely… I appreciate your help."
            scene ch6sc10_561 with dissolve
            mc "Any time, captain."
            "Orianna enjoys your company, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ ori_trust += 3
            mc "Looks like Pearl is back from her swim, I’ll go join her and Taz downstairs, shout if you need anything."
            scene ch6sc10_562 with dissolve
            ori "Awh, that’s sweet of you but I’ll manage."

        "Sorry Ori, I’m going to join Taz on the deck. ({color=#2bff8b}Friendly{/color})":
            mc "Ah, sorry to leave you hanging, but I just wanted to come say hi, I still want to go check on Taz."
            ori "Oh, that’s too bad… I’ll endure a little while longer then."

    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_567 with Dissolve(2.5)
    play music chill_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    pl "Nicely done Taz! I see you’ve gotten everything out of storage just for the day?"
    tz "Hey, as women we should not lack for comforts, am I right?"
    pl "Totally! I’m so glad I didn’t kill you after you ate my berries during the hunting ceremony!"
    tz "I know right?! W-Wait… what?!"
    pl "Joking! *Giggles*"
    scene ch6sc10_568 with dissolve
    mct "They look to be getting the most of today's sun."
    mct "Must be nice for them to finally have a day to relax with all we’ve been through."
    scene ch6sc10_569 with dissolve
    pl "Tell me this isn’t the best you’ve ever felt?"
    tz "I’m starting to see the appeal of living on the open water."
    pl "It’s the best! It’s so freeing being out here."
    scene ch6sc10_570 with dissolve
    mc "Hey you two, you enjoying our last day of peace and quiet on the water before things get hectic again?"
    pl "[mc]! Hi!"
    pl "You bet we are! *Giggles*"
    tz "[mc], hi! Are you here to join us?"
    scene ch6sc10_571 with dissolve
    pl "Please join us Sharky! Pretty pleeeaaase!"
    pl "There’s plenty of room for you, right between us! *Giggles*"
    mc "How can I refuse my cute little mermaid and my lovely chronicler?"
    pl "You can’t! Now sit!"
    scene ch6sc10_572 with dissolve
    "As you lay down next to Pearl and Taz, Pearl runs her fingers teasingly across your thigh."
    pl "Sharky… I feel like you would be a lot more comfortable without these on."
    tz "*Gasps* Pearl! You’re so bold!"
    scene ch6sc10_573 with dissolve
    mc "*Chuckles* Nice try."
    mc "But my naughty little mermaid will have to keep dreaming."
    scene ch6sc10_572 with dissolve
    pl "*Snickers* And dream I shall."
    scene ch6sc10_573 with dissolve
    mc "Was it a nice dip you had earlier?"
    scene ch6sc10_572 with dissolve
    pl "Very much so! You could’ve joined me, you're just as strong of a swimmer as I am."
    scene ch6sc10_573 with dissolve
    mc "Even if I weren’t, I could just surface from the water and run to the ship. *Chuckles*"
    scene ch6sc10_574 with dissolve
    pl "*Giggles* Sharky! That’s cheating!"
    pl "But yes, I suppose we’ll never have to worry about you drowning!"
    scene ch6sc10_575 with dissolve
    tz "I’ve never seen you run on water?"
    mc "Add it to my growing list of abilities."
    tz "How does it work?"
    mc "Well, I channel energy into whichever part of my body is touching the water's surface."
    mc "Which creates a sort of energetic micro barrier between my skin and the water, essentially making it act like a solid surface."
    scene ch6sc10_576 with dissolve
    tz "Gosh-dolly! That’s actually pretty clever!"
    tz "But something like that must require a lot of energy? You’d have to constantly generate more to keep the barrier?"
    scene ch6sc10_577 with dissolve
    mc "Correct, you need a great amount of energy or mana as mages like to call it."
    mc "Which I just so happen to have… but you also need to understand how to create and maintain the barrier."
    scene ch6sc10_576 with dissolve
    tz "Oh? It’s not just like a simple barrier a mage would conjure?"
    scene ch6sc10_577 with dissolve
    mc "Not exactly, with this type of barrier, you are pushing forth your energy but if you push it too far it dissipates."
    mc "So you need proper control otherwise you will just go straight through the water after a few seconds."
    scene ch6sc10_576 with dissolve
    tz "Who taught you all this?"
    scene ch6sc10_577 with dissolve
    mc "A girl I met half a lifetime ago… Rin."
    mc "She had an affinity for wind magic and essentially taught me the ropes of how magic functions."
    scene ch6sc10_576 with dissolve
    tz "Oh that was kind of her, I’m sure she is dear to you?"
    scene ch6sc10_577 with dissolve
    mc "She was-... is."
    mc "I just haven’t seen her in over two years."
    mc "When I turned 18, my mentor discovered that we had been compromised in the village we sought refuge in."
    mc "So we had to leave, abruptly."
    mc "I haven’t seen Rin since…"
    scene ch6sc10_576 with dissolve
    tz "If you met her half a lifetime ago, and it’s been two years now…"
    tz "You must’ve spent a great many years together?"
    scene ch6sc10_577 with dissolve
    mc "Mhm, we did. About five years give or take."
    mc "I know she has been in Luxenford recently, everything has just been happening one after another."
    mc "But once things quiet down, I intend to find her and see how she’s doing."
    scene ch6sc10_576 with dissolve
    tz "You should… speaking as a woman in your entourage…"
    tz "I am certain she cares deeply for you, as we all do. She will be nothing but happy to reunite with you."
    scene ch6sc10_577 with dissolve
    mc "I hope that is the case… I certainly long to see her again."
    scene ch6sc10_575 with dissolve
    mc "But enough talk of the past… let’s catch some shuteye before the sun sets."
    tz "Ooh! I was meaning to nap before you and Pearl arrived! Let’s do it!"
    scene ch6sc10_574 with dissolve
    pl "Seas yes! Nappy time! *Giggles*"
    scene ch6sc10_572 with dissolve
    pl "If you happen to snuggle up to me while I’m napping, I won’t complain."
    scene ch6sc10_573 with dissolve
    mc "*Chuckles* I’m sure you won’t."
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_578 with Dissolve(2.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "It doesn’t take long for the three of you to doze off."
    "Basking in the warm rays of the afternoon sun, the three of you enjoy the cool breezes from the ocean."
    scene ch6sc10_579 with dissolve
    "The gentle swaying of the boat as it is embraced by calm waves soothes your bodies."
    "The sounds of seagulls flying above as well as the waves gently crashing into the hull of the ship…"
    scene ch6sc10_580 with dissolve
    "Combines to a unique lullaby that calms mind and body."
    "In less than 12 hours you’ll arrive in Looter’s bay, you’re all determined to get the most out of the time you have left."
    scene ch6sc10_578 with dissolve
    "Minutes become an hour."
    "An hour becomes two..."
    scene ch6sc10_581 with dissolve
    mct "Mmh…"
    mct "This is what an adventurer’s life is supposed to be."
    scene ch6sc10_582 with dissolve
    mct "A split second decision to come aid my friends, turning into an elaborate quest to rescue an Ambassador of a foreign kingdom."
    mct "To discovering an unknown civilization and getting to know its people and history…"
    mct "To becoming their leader and uncovering ancient mysteries lost to time…"
    scene ch6sc10_583 with dissolve
    mct "To a relaxing day on the ocean with people I care about…"
    mct "This is what it’s all about… this is an adventurer’s life."
    mct "But with all adventures comes the longing for home… I may not have a home, yet."
    scene ch6sc10_582 with dissolve
    mct "But that is something I intend to create with Eliza, when time allows it."
    mct "*Sighs* It would appear we’ve at least napped for an hour… maybe two?"
    mct "Okay, enough resting."
    scene ch6sc10_584 with dissolve
    mct "I’m getting restless not having done anything active all day."
    scene ch6sc10_585 with dissolve
    mct "Time to rectify that."
    scene ch6sc10_584 with dissolve
    mct "I could go for a swim like Pearl did, but I’ll just get in a quick workout while the girls finish their nap."
    scene ch6sc10_585 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_584 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_585 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_586 with dissolve
    $ renpy.pause(1)
    pl "Mmmh! *Giggles*"
    scene ch6sc10_587 with dissolve
    pl "Hhnh?"
    pl "*Giggles* …"
    scene ch6sc10_588 with dissolve
    pl "*Whispers* {size=-10}{b}Psst! Taz… wakey-wakey!{/b}{/size}"
    pl "*Whispers* {size=-10}{b}You don’t want to miss this. *Giggles*{/b}{/size}"
    pl "*Whispers* {size=-10}{b}Sexy man working up a sweat next to gorgeous girls in bikini’s alert.{/b}{/size}"
    scene ch6sc10_589 with dissolve
    tz "A-Are you saying… if I turn my head right now I will see [mc], all sweaty whilst working out???"
    pl "*Snickers* That’s exactly what I’m saying!"
    tz "I-I couldn’t-... could I? … maybe just a peak?"
    scene ch6sc10_590 with dissolve
    $ renpy.pause(1)
    with vpunch
    tz "*Gasps* Goodness-golly!"
    tz "T-That should be illegal!"
    pl "It’s definitely making me want him to do illegal things to me… *Snickers*"
    scene ch6sc10_591 with dissolve
    tz "It looks so effortless for him…"
    scene ch6sc10_592 with dissolve
    tz "How long has he been at it?"
    scene ch6sc10_591 with dissolve
    pl "I only just woke up as well."
    scene ch6sc10_592 with dissolve
    pl "I doubt a simple pushup is much of a challenge for him though, when we sailed to Aruna-"
    scene ch6sc10_591 with dissolve
    pl "-I sat on his back while he did pushups… and it was still effortless for him."
    scene ch6sc10_592 with dissolve
    tz "Mmgh… there’s really nothing quite like a handsome man working up a sweat, is there?"
    scene ch6sc10_591 with dissolve
    tz "Just look at how his muscles glistens in the sun."
    scene ch6sc10_592 with dissolve
    pl "I know what you mean… mmh-hm… it makes it tingle in all the right places."
    scene ch6sc10_591 with dissolve
    pl "Hey, handsome… you need a hand? *Giggles*"
    scene ch6sc10_592 with dissolve
    mc "*Chuckles* Not particularly."
    scene ch6sc10_591 with dissolve
    pl "Awwh! C’mon! Let us help you workout?"
    scene ch6sc10_592 with dissolve
    pl "We both know you need more resistance than your own body weight… you’re much too strong for that."
    scene ch6sc10_591 with dissolve
    mc "*Sighs* … fine."
    pl "Yay! *Giggles* C’mon Taz! This our chance! Mount him!"
    scene ch6sc10_593 with dissolve
    tz "*Gasps* Uuaahh! L-Like this?!"
    pl "*Snickers* Exactly like this! Show us what you’ve got [mc]!"
    scene ch6sc10_594 with dissolve
    tz "Oh! Oh my! This will require some balance!"
    scene ch6sc10_593 with dissolve
    pl "Uh-huh! You’ll get used to it after a few reps."
    scene ch6sc10_594 with dissolve
    tz "You weren’t kidding… he still seems to be able to continue as if we weren’t even here."
    scene ch6sc10_593 with dissolve
    pl "Aren’t you happy we’re assisting you, sharky?"
    scene ch6sc10_594 with dissolve
    mc "Totally…"
    pl "Let’s try another workout! I’m just going to do my hair real quick, I feel it getting dry."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "As soon as Pearl finishes doing her hair, they whisper to each other giggling for a brief moment before they charge you."
    with vpunch
    scene ch6sc10_595 with Dissolve(1.5)
    $ renpy.pause(0.3)
    with vpunch
    pl "*Giggles* We got him!"
    tz "Sure did! Show us how strong you are Mr.Nephilim!"
    mc "*Sighs* You girls are ridiculous…"
    scene ch6sc10_596 with dissolve
    "You feel the girls tightly wrapping themselves around you, clinging onto you as if their lives depended on it."
    pl "Go on sharky! Continue your workout with us!"
    tz "Yeah, don’t mind us! *Giggles* We’re just making sure you get the proper… resistance."
    mct "..."
    scene ch6sc10_597 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_596 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_597 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_596 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_597 with dissolve
    $ renpy.pause(1)
    pl "That’s it sharky! You’re doing it! You’re doing us! *Snickers*"
    scene ch6sc10_596 with dissolve
    tz "I was already impressed with the other exercise… but gosh-dolly… your arms aren’t even shaking!"
    scene ch6sc10_597 with dissolve
    pl "Duh! Don’t you remember how you saw him hold back Jimun’s jaws with his bare hands, when it tried to eat Vex?"
    scene ch6sc10_596 with dissolve
    pl "Compared to that, holding the weight of two women is literally like if you and I were to lift a mug of ale or something."
    scene ch6sc10_597 with dissolve
    tz "Oh! When you put it like that… it does seem silly to not think he could handle us like this. *Giggles*"
    scene ch6sc10_596 with dissolve
    pl "*Snickers* Oh he’s handling us alright…"

    if pearl_relationship == True:
        scene ch6sc10_597 with dissolve
        pl "If he’s lucky, I might just let him handle me later. *Giggles*"
        scene ch6sc10_596 with dissolve
        tz "P-Pearl! You’re so naughty!"
        scene ch6sc10_597 with dissolve
        "You feel Pearl rub herself onto your ribs, letting you feel her panties and how they’re soaked through."

        if tz_relationship == True:
            scene ch6sc10_596 with dissolve
            tz "Y-You can’t just claim him for the night!"
            scene ch6sc10_597 with dissolve
            tz "What if… I wanted him to handle me?!"
            scene ch6sc10_596 with dissolve
            "You feel Tazzy pressing her breasts into the side of your chest and squeezing your neck gently."
            scene ch6sc10_597 with dissolve
            pl "You can’t have him! *Giggles* I need his firm handling tonight!"
            scene ch6sc10_596 with dissolve
            mct "*Chuckles* Five hells… they’re both horny today."
            scene ch6sc10_598 with dissolve
            ori "Hey, guys. Can someone take over steering? The sun is setting so I’d like to get started on dinner."

        else:
            scene ch6sc10_598 with dissolve
            ori "Hey, guys. Can someone take over steering? The sun is setting so I’d like to get started on dinner."

    else:
        scene ch6sc10_598 with dissolve
        ori "“Hey, guys. Can someone take over steering? The sun is setting so I’d like to get started on dinner."


    scene ch6sc10_598
    ori "Also, I could really use someone to aid me in the kitchen, it’s our last night, we might as well go all out."
    scene ch6sc10_599 with dissolve
    pl "I’ll be happy to steer for a while, I’m horrible in a kitchen and I’m a captain after all."
    ori "That would be great, Pearl. Thank you."
    pl "Of course! I look forward to seeing what you guys come up with!"
    scene ch6sc10_600 with dissolve
    ori "I guess that just leaves the two of you."
    ori "Which one of you is the lucky volunteer who gets to join me in the kitchen? *Giggles*"
    scene ch6sc10_601 with dissolve
    tz "Oh… I was actually hoping I’d get a chance for a bath, I haven’t had one since we left A’nai."
    tz "And I’ve never cooked anything in my life…"
    scene ch6sc10_602 with dissolve
    tz "But! I’ll be happy to set the table once I’m done with my bath!"
    ori "That would be lovely, and yes, you really should go have a bath if you haven’t already."
    ori "We were all sweating after the jungle trek yesterday and then a long swim in salt water."
    scene ch6sc10_601 with dissolve
    tz "Oh thank you for being so understanding, Ori!"
    tz "I promise I will set the table and help clean up afterwards as well."
    ori "Lovely! Go on, enjoy your bath."
    ori "We’ll see you at dinner then."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc10_603 with Dissolve(2.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Orianna gently caresses your arm."
    ori "I guess that leaves you with me?"
    ori "[mc]?"
    scene ch6sc10_604 with dissolve
    mc "Hmm? Oh, Ori."
    mc "Sorry, I was lost in thought."
    ori "Yeah, I could tell."
    ori "Talk to me about it?"
    scene ch6sc10_605 with dissolve
    mc "Sure."
    mc "I was thinking about home."
    scene ch6sc10_606 with dissolve
    ori "Home?"
    scene ch6sc10_605 with dissolve
    mc "Mhm, at first I was thinking about my childhood home, Riverside, and moments with my parents before they passed."
    mc "Then my thoughts drifted to where I consider home to be now… Luxenford."
    scene ch6sc10_606 with dissolve
    ori "Oh? You have a house in Luxenford?"
    scene ch6sc10_605 with dissolve
    mc "No, not quite… I currently stay at one of it’s taverns, The Drunken Rooster."
    mc "But I have acquired some land with a woman, Eliza. About ten miles outside of Luxenford."
    mc "We’re currently planning on building a proper homestead there, we had just brought supplies out the night I left."
    mc "I kind of left everything in a hurry to get out here, to assist Pearl and her sister, Kira."
    scene ch6sc10_606 with dissolve
    ori "Right, Pearl told me that you came to their rescue, and then… you also came to my rescue."
    ori "I know I didn’t ask for you to rescue me or anything…"
    scene ch6sc10_604 with dissolve
    ori "But, I feel a little bad that you had to leave something that important."
    mc "It’s alright… I’ll continue the project with Eliza when I return."
    scene ch6sc10_606 with dissolve
    ori "You must really look forward to seeing her again?"
    ori "Your eyes light up when you mention her."
    scene ch6sc10_605 with dissolve
    mc "Mhm… I do. I miss her a great deal."
    "You feel Orianna caress your arm."
    scene ch6sc10_606 with dissolve
    ori "I am certain she misses you just as much."
    ori "I know I would."
    scene ch6sc10_603 with dissolve
    mc "Thank you… it's nice to have someone to talk to about these things."
    ori "I’m happy to listen, I do not have any family and my friends can be counted on a few fingers."
    ori "But… I’m glad to now be counting you amongst that group."
    ori "So if you ever need me or just would like to talk, please do."
    scene ch6sc10_604 with dissolve
    mc "I appreciate that, Ori."
    ori "Now, how about you come join me in the kitchen?"
    scene ch6sc10_606 with dissolve
    ori "We’ll get your mind off missing home with some great cooking! *Giggles*"
    scene ch6sc10_605 with dissolve
    mc "*Chuckles* Sounds good, lead on."
    scene ch6sc10_607 with dissolve
    ori "*Giggles happily* C’mon then!"
    "Orianna gently takes your hand and begins leading you to the kitchens."
    ori "I’m sure everyone is starving and it’ll be a while before we finish cooking."
    scene ch6sc10_608 with dissolve
    mc "I know I am… as chefs, do we get to enjoy an appetizer whilst cooking?"
    ori "*Snickers* An appetizer? Hmm…"
    ori "You may get an appetizer if you do well."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "Orianna leads you down to the middle deck, where the storage and kitchen is located."
    scene ch6sc10_609 with Dissolve(2.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ori "Kitchen is over here, I did prep most of what we would need when I made breakfast this morning."
    ori "Although we may get inspired and find something in storage… you never know when cooking. *Giggles*"
    scene ch6sc10_610 with dissolve
    mc "Yeah, we never know."
    mc "Seems like you have prepared a great deal of ingredients for tonight's dinner?"
    ori "It’s our last night here, and it isn’t our ship."
    ori "We might as well go all out, no? *Giggles* Stand by the table."
    scene ch6sc10_611 with dissolve
    mc "As you command, Chef."
    ori "*Giggles lightly* What a lovely assistant I’ve gotten myself, in the kitchen a Chef’s command is to be obeyed… fully."
    mc "*Chuckles* I’m not used to taking orders… but I could be persuaded."
    scene ch6sc10_612 with dissolve
    ori "Oh could you now? I’ll have you know I can be a very… rewarding chef."
    ori "If my assistant listens and obeys… he’s sure to earn a reward."
    ori "*Giggles* Now cut these carrots!"
    mc "*Sighs* Yes, Chef."
    scene ch6sc10_613 with dissolve
    mc "I see how it is… luring me down into your kitchen to put me on the bothersome tasks."
    ori "Hush… you’re here to assist me. *Giggles*"
    ori "I’ll prepare the pot for the stew while you work on the vegetables."
    scene ch6sc10_614 with dissolve
    mc "Complaining won’t get these orange bastards chopped… might as well get to it."
    scene ch6sc10_615 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_614 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_615 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_614 with dissolve
    $ renpy.pause(1)
    mc "I’ve only really cooked stuff on the campfire while traveling, it’d be nice to understand how to fully cook a meal."
    scene ch6sc10_615 with dissolve
    mc "I guess it can be pretty relaxing to just focus on a simple task…"
    scene ch6sc10_616 with dissolve
    "You feel a delicate touch run along your forearm as well as your abs."
    mc "Hmh? Ori?"
    ori "This simply won’t do…"
    scene ch6sc10_617 with dissolve
    ori "Will you forgive me? It seems I have failed as your teacher, not having taken the time to teach you how to properly hold the knife."
    "You feel her gently caress your chest while she moves her other hand onto yours."

    if ori_path == True:
        mc "I’m liking this hands-on way of teaching."
        scene ch6sc10_618 with dissolve
        ori "I had a feeling this would be the best way to get your attention and make you focus."
        scene ch6sc10_617 with dissolve
        ori "See how you’re holding the blade?"
        scene ch6sc10_618 with dissolve
        mc "Mmgh… yeah?"
        "You feel her delicate fingers run across your nipple while her breasts are squished against your back."
        scene ch6sc10_617 with dissolve
        ori "You’re holding it as if it’s a sword… it’s a terrible angle for the blade to be cutting."
        ori "You may not feel it at first, but eventually it will begin to annoy your wrist."
        scene ch6sc10_618 with dissolve
        ori "And as your chef, I’m responsible for you… I won’t have you hurting yourself on my watch, okay?"
        mct "*Chuckles* She’s fully aware of what she's doing… touching me like this… pressing herself against me…"
        mc "Then what do you suggest, Chef?"
        scene ch6sc10_619 with dissolve
        ori "Like this… mmgh… your index goes here, following the edge of the blade."
        mc "I see…"
        ori "Holding it like this you will be able to guide the blade with precision… mmgh."
        scene ch6sc10_620 with dissolve
        mc "I’m glad you're such an attentive teacher, not just letting me get away with bad technique."
        ori "Oh I simply wouldn’t have been able to sleep tonight if I knew I had let this go on…"
        ori "I’m pleased you take my instructions to heart… cooking can be a very… intimate experience."
        ori "Please continue. I will monitor your technique from time to time."

    else:
        mc "I’m perfectly fine cutting it this way, you can focus on your own task for now."
        scene ch6sc10_616 with dissolve
        ori "I see… I apologize for intervening."
        scene ch6sc10_615 with dissolve
        "Orianna leaves you to cut the carrots your way."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_621 with Dissolve(1.5)
    $ renpy.pause(0.5)
    ori "Oh gosh, would you look at that?"
    mc "*Chuckles* Trust me… I’m looking."
    ori "No, silly! We forgot the parsnips!"
    scene ch6sc10_622 with dissolve
    ori "Don’t put the knife away just yet, the stew won’t be as fulfilling if we skip out on these."
    mc "*Sighs* Great."
    mc "Ori that’s a lot of parsnips…"
    ori "We’re four people! A chef always cooks more than necessary to avoid people holding themselves back."
    scene ch6sc10_623 with dissolve
    mc "*Sighs* Fine, I won’t have any of you saying you’re still hungry after tonight's dinner."
    ori "That’s the spirit! I’ll just see if we have any flour leftover, it would be nice if we could make some fresh bread."
    scene ch6sc10_625 with dissolve
    ori "I’ll just be a moment. Don’t cut yourself!"
    mc "If I do, it will just regenerate anyways."
    ori "Right! I forgot you could do that."
    scene ch6sc10_624 with dissolve
    ori "Uhh…"
    ori "[mc], could you come in here for a moment?"
    mc "Sure, hold on."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)

    if ori_path == True:
        scene ch6sc10_626 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ori "[mc]?"
        mc "What is it?"
        ori "I’m afraid the only flour we have left has been stored up high… I simply cannot reach it on my own."
        ori "Would you give me a hand? I think we can reach it together."
        scene ch6sc10_627 with dissolve
        mc "Let’s see… hm, yeah I think we can manage."
        scene ch6sc10_628 with dissolve
        mc "With a little bit of effort…"
        ori "Come closer, you won’t be able to reach from back there."
        scene ch6sc10_629 with dissolve
        ori "It’s a little tight in here… hnngh."
        mc "Yeah… mmgh…"
        scene ch6sc10_630 with dissolve
        ori "I’m having flashbacks to when you helped me steer the ship… nngh…"
        scene ch6sc10_629 with dissolve
        mc "It seems we have a habit of finding ourselves in this position."
        scene ch6sc10_630 with dissolve
        ori "Aahh… yeah… I wonder what that means? *Giggles*"
        scene ch6sc10_629 with dissolve
        mc "I think we both know what it means… Mmh…"
        scene ch6sc10_630 with dissolve
        ori "See if you can reach the flour… aah… I’d love to show you how to make bread."
        scene ch6sc10_631 with dissolve
        ori "*Moans* Hnngh-Aah…"
        "You grab her shoulder firmly as you lean further against her, forcing her to support herself on the shelves."
        scene ch6sc10_632 with dissolve
        ori "Nnnh… do you- ahh… do you have it?"
        scene ch6sc10_631 with dissolve
        mc "Mmh… almost… just a little further."
        scene ch6sc10_632 with dissolve
        ori "D-Do what you have to- Mmh… just get the flour."
        scene ch6sc10_631 with dissolve
        ori "Aahh… that’s it… I can feel you- I mean I can feel you've reached the flour."
        scene ch6sc10_632 with dissolve
        ori "*Moans* Mmgh-ahh… grab me! I-I mean grab it!"
        scene ch6sc10_631 with dissolve
        mc "Got it! Mmgh…"
        ori "G-Good job, mmh… you’re such a diligent assistant."
        ori "Come… let us bring it to the table, I’ll show you how to make bread."
        scene ch6sc10_633 with dissolve
        ori "So, my lovely and incredibly handsome assistant."
        ori "Do you know anything about making bread?"
        mc "Not in the slightest."
        scene ch6sc10_634 with dissolve
        ori "*Giggles* Good… that means I get to be fully hands on with you, teaching you from start to finish."
        mc "I do like a hands on approach."
        ori "I know you do, if your knife technique taught me anything… it’s that I’ll have to be very attentive with a student such as you."
        ori "Now grab a little more flour and we’ll begin."
        scene ch6sc10_635 with dissolve
        "As you grab some more flour, Ori begins instructing you how to handle it."
        ori "Now just do as I, and we’ll begin kneading it to combine the other ingredients."
        mc "Like this?"
        ori "Yes-"
        scene ch6sc10_636 with dissolve
        ori "Here, let me show you how to knead it."
        "You feel her soft floury hands keep brushing against yours, she is more interested in physical touch than mixing the flour."
        "Her soft supple breast rests against your arm as her scent entices you."
        ori "The proper hand technique is important otherwise it-"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_637 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        ori "*Gasps* Aah!"
        ori "[mc]-... mmh… this isn’t how you make bread… ahh…"
        mc "Oh? Forgive me… I’m new."
        scene ch6sc10_638 with dissolve
        with vpunch
        ori "*Gasping moan* {b}Aaiiyh! [mc]!{/b} What are you-"
        mc "I’m improvising… *Inhales deeply* Mmmh... what a scent..."
        ori "*Giggles* You’re a naughty student… smelling my hair… stripping me…"
        ori "Pressing your rock-hard desire against me…"
        scene ch6sc10_639 with dissolve
        mc "You really have incredible breasts Ori… they drive me crazy… mh."
        ori "*Moans* Aahh… ohh… I’m happy you enjoy them-"
        ori "Mmmh… I loved how you gazed upon them last night during the Shuffle-Showdown."
        mc "I couldn't help it… as the girls said, you're exotic... beautiful... mesmerizing."
        mc "Now, let’s begin making this bread."
        scene ch6sc10_640 with dissolve
        with vpunch
        ori "*Moans* {b}Aiiyh-ahh! Gosh [mc]!!{/b}"
        mc "You wanted to mix flour? Well let’s mix this flour properly then."
        "You press Orianna firmly down against the table, squishing her breasts into the flour."
        scene ch6sc10_641 with dissolve
        ori "You’re really going to- Aahh… use my breasts to make the dough? Mmh!"
        mc "Mhm, that’s exactly what I’m going to do… but first, we’ll need to fully prep you, chef."
        scene ch6sc10_642 with dissolve
        ori "Aah! I see you’ve paid attention to my lessons… prepping is paramount in cooking!"
        mc "Mmh… how could I not pay attention with such a gorgeous teacher… you’re dripping wet for your student."
        ori "*Moans* Oohh… that… that is just because I- aahh… because I am excited to have an assistant."
        scene ch6sc10_643 with dissolve
        ori "*Gasps* [mc]! Nngh… you promised!"
        mc "And I intend to keep my promise… just trust me."
        ori "O-Okay… mmh… use my body as your tool to- aahh…  make the dough."
        scene ori_lewd1 with dissolve
        $ renpy.pause()
        "She intimately presses herself back against you, moaning as your cock is being pressed between her exotic cheeks."
        mc "*Moans* Ffuck… you have incredible breasts but damn Ori… your ass is just as enjoyable."
        ori "*Moans* Nnnh-mmh… you like my ass? You like feeling it surround your hard cock?"
        ori "Aahh… use me! Use your chef to make bread! Aaiihh…"
        ###Skills-check###
        if persuasion >= 13:
            ori "We-... mmh... we should probably stop... you're pulsating- Aahh..."
            mc "Ffuck Ori... I don't want to stop... mmhh... your ass is heavenly... I want to cover you in my cum."
            mc "May I? Chef? Mmhh..."
            ori "*Moans softly* Ohhh.... mmhh... I can't deny you... not when you feel so good... do it... cover me!"
            "You had enough {color=#2bff8b}Persuasion{/color} to make Orianna feel excited about being covered in your cum."
            ori "Cum for me! Mmh! I want to feel your warm cum cover my ass and my back! Aiiyhh!"

        else:
            pass

        with vpunch
        "She continues to firmly squeeze your cock as it slides between her cheeks, the scent of her dripping pussy is just below."
        with vpunch
        mc "Mmh! Ori- {b}Aahh!{/b}"
        with vpunch
        ori "{b}That's it!{/b} Be a good student and- {b}Aiiyhh!{/b} Prove to your chef that you are fully committed! {b}AhhH!!{/b}"
        scene ch6sc10_643 with dissolve
        mc "Fuck- {b}Ahh!!{/b} Your ass is too fucking perfect- {b}Ahh!{/b}"
        scene ch6sc10_644 with dissolve
        with vpunch
        "Orianna keeps a firm squeeze with her cheeks enclosed around your cock as she feels you orgasm."
        with vpunch
        scene ch6sc10_645 with dissolve
        ori "*Moans* Ohh… mmh… you had this much for me? Mmmh… what a diligent assistant I have."
        mc "*Chuckles* Now this is what I call cooking with passion."
        ori "*Giggles* You have opened my eyes to a new way of cooking… one I look forward to continue exploring with you."
        mc "Mmh… you know not only how to entice a man… but to satisfy him as well, count me in for more cooking lessons."
        scene ch6sc10_646 with dissolve
        ori "If only we had been at my place in Arazalia right now… we wouldn’t have to hold back…"
        ori "*Sighs* Let me just go clean up and we’ll finish the bread."
        mc "*Chuckles* I look forward to tasting it later… knowing that your breasts are what made the dough."
        scene ch6sc10_647 with dissolve
        ori "You’re so naughty… *Giggles*"
        mc "Mhm… what a sight, there’s nothing like seeing a woman bent over and covered in my cum."
        ori "Oh? You enjoy seeing me like this? I will be sure to remember that for our next cooking session. *Giggles*"
        scene ch6sc10_648 with dissolve
        ori "But for now, I’ll have to wash it off."
        ori "Continue working on the flour and we’ll have a dough at the ready when I return."
        mc "Aye, aye, Chef."
        scene ch6sc10_649 with dissolve
        "Orianna walks over to a bucket with water and a cloth, while you continue to mix the flour."
        mc "How am I supposed to mix flour when you walk around looking like that?"
        ori "*Giggles* {b}Focus!{/b}"
        $ ori_trust += 5
        "Orianna loves that you can’t take your eyes off her, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
        scene ch6sc10_635 with dissolve
        "Upon returning, all cleaned up and having gotten dressed, the two of you continue cooking."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0

    else:
        scene black

    scene ch6sc10_635
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    "Together, the two of you easily make a good chunk of dough that can now be put on the fire to make a loaf of bread."
    scene ch6sc10_650 with dissolve
    $ renpy.pause(1)
    "Orianna makes sure to praise you on each accomplishment."
    "She may never have had a student in the kitchen before, but she seems to enjoy having someone to share her passion with."
    scene ch6sc10_651 with dissolve
    "Everytime you think you’re done, Orianna finds a new thing for you to take care of."
    "One prep at a time, the two of you make your way through the many ingredients for tonight’s feast."
    scene ch6sc10_652 with dissolve
    "One hour quickly consumes the next as the two of you find enjoyment in each others company."
    "Not a single ingredient is wasted, Orianna ensures that you put everything to use."
    scene ch6sc10_611 with dissolve
    "And just as you think it’s time to finish up…"
    scene ch6sc10_612 with dissolve
    "She drops another batch of ingredients in front of you…"

    if ori_path == True:
        scene ch6sc10_620 with dissolve
        "However, she makes a point of ensuring that your motivation remains elevated."
        "Her hands often finds their way onto your body, and her soft voice encourages you to do your best."
        scene ch6sc10_623 with dissolve
        "As the two hour mark approaches, she finally relents and announces you’re all done."

    else:
        scene ch6sc10_623 with dissolve
        "However, as the two hour mark approaches, she finally relents and announces you’re all done."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_653 with Dissolve(2.5)
    $ renpy.pause(0.5)
    mc "Ori… this is incredible, did we really make all this just now?"
    ori "*Giggles happily* You bet!"
    ori "You can safely be proud of what we accomplished in the kitchen today, you did so well."
    mc "I did have an attentive teacher. *Chuckles*"
    ori "And she is very… {b}proud of you{/b}."
    "You feel her squeezing your bicep."
    scene ch6sc10_654 with dissolve
    ori "I didn’t know what to expect but seeing a proper man cook with passion… that does something to a woman."
    ori "I already long to have you in my…"
    scene ch6sc10_655 with dissolve
    ori "Kitchen."
    mc "I’m already intrigued to see what we manage to cook up."
    scene ch6sc10_654 with dissolve
    ori "C’mon handsome, I’m sure the others are eagerly awaiting us by now."
    scene ch6sc10_655 with dissolve
    "You feel Orianna give your bicep one last squeeze before she lets go and the two of you can proceed to bring the food to the dining area."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "As the two of you arrive in the dining area, Pearl and Taz eagerly await and you proceed to join them."
    scene ch6sc10_462 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    tz "Again you whip out a lavish feast for us, Ori."
    ori "I can’t take all the credit, I had a great assistant today as you well know."
    scene ch6sc10_463 with dissolve
    ori "A feast like this wouldn’t have been done before midnight if it weren’t for [mc]’s hands."
    tz "I believe you, this much food would take ages to prepare alone."
    pl "*Noms* Mh-mh."
    scene ch6sc10_464 with dissolve
    ori "You’re right, it would’ve taken ages if it weren’t for my diligent assistant. *Giggles*"
    ####Skill-check###
    if charisma >= 15:
        mc "*Chuckles* I had a great time cooking, it wasn’t as much of a chore as I expected, especially, when the company is great."
        scene ch6sc10_466 with dissolve
        ori "Such a charmer!"
        ori "But I shall agree, the company was immaculate."
        scene ch6sc10_464 with dissolve
        mc "Yeah... I enjoyed the company... thoroughly so."
        $ ori_trust += 2
        "Orianna enjoys your flirtation, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."


    else:
        pass


    scene ch6sc10_465 with dissolve
    mc "Orianna is a great tutor, I learned quite a bit about cooking tonight."
    tz "*Gulp* I bet! Nothing better than a teacher who is attentive to their student."
    mc "Oh she was attentive, alright."
    scene ch6sc10_466 with dissolve
    ori "*Giggles* I’m pleased you think so!"
    ori "It was my first time teaching another how to cook, so I just did what felt natural."
    scene ch6sc10_467 with dissolve
    pl "*Nods* Mmh, the bread is saltier than yesterday."
    ori "Oh… *Giggles* Yeah, it might have a slightly different flavor today."
    pl "Hmmh? *Noms*"

    if ori_path == True:
        scene ch6sc10_656 with dissolve
        ori "We changed the recipe slightly."
        ori "You see, [mc] had a brilliant although unorthodox method of kneading the dough."
        scene ch6sc10_657 with dissolve
        pl "Oh, I see! *Noms*"
        ori "He really took me by surprise… *Giggles softly*"
        scene ch6sc10_656 with dissolve
        ori "But his technique proved… {b}effective{/b}."
        scene ch6sc10_657 with dissolve
        ori "But I believe it may have left the bread slightly saltier than usual."
        scene ch6sc10_656 with dissolve
        mc "Yeah… it was a very… hands-on technique, so we accidentally spilled a bit of salt."
        scene ch6sc10_467 with dissolve
        pl "Oh, I see! Mmh, it’s not bad though… enhances the flavor, really. *Noms*"
        scene ch6sc10_468 with dissolve
        mc "I’m glad you like it, it took some effort getting the dough done properly."
        mc "Especially being my first time, but Ori managed to keep me focused on the task."
        $ ori_trust += 2
        "Orianna enjoys your flirtation, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

    else:
        mc "We accidentally spilled a bit of salt into the dough after we had already salted it."
        pl "Oh! Mmh, it’s not bad though… enhances the flavor, really. *Noms*"
        scene ch6sc10_468 with dissolve
        mc "I’m glad you like it, it took some effort getting the dough done properly."

    scene ch6sc10_469 with dissolve
    tz "Gosh-Dolly! I shan’t believe I missed out on such a cooking experience!"
    tz "You two make it sound so passionate!"
    scene ch6sc10_470 with dissolve
    ori "*Giggles* Cooking and passion go hand in hand."
    ori "You seem like a passionate woman yourself, Tazzy. I believe you would do well in a kitchen."
    tz "Right?! I don’t recall if I know how to cook but it sounds like something I would enjoy!"
    scene ch6sc10_471 with dissolve
    ori "*Gulps* I shall be happy to teach you sometime, otherwise just attempt it with basics and go from there."
    tz "Yeah, we may not see each other for a long time after we deliver you, but I could always attempt some simple dishes."
    ori "*Gulp* That’s the spirit Tazzy, cooking can be very fulfilling and enjoyable."
    scene ch6sc10_469 with dissolve
    tz "Now that [mc] has become well versed in the art of cooking, he can be my tutor."
    tz "I too desire a passionate hands-on experience!"
    scene ch6sc10_467 with dissolve
    pl "*Noms* I wanna learn too."
    pl "[mc], I want your hands and your passion as well."
    scene ch6sc10_468 with dissolve
    mc "*Chuckles* You got it."
    scene ch6sc10_466 with dissolve
    ori "*Giggles* Seems like you’re going to be a busy man."
    scene ch6sc10_465 with dissolve
    mc "It sounds like it."
    mc "Thank you for teaching me the ropes, really. It’s nice knowing my way around a kitchen."
    scene ch6sc10_466 with dissolve
    ori "You’re most welcome, I really enjoyed having you as my assistant and being able to share my passion with you."
    scene ch6sc10_464 with dissolve
    ori "You still have a great many things to learn, but today we managed to cover quite a few of the basics."
    ori "You should be able to handle most vegetables now and how they go together in a stew."
    scene ch6sc10_462 with dissolve
    ori "Tazzy, how was your bath? Did you manage to get rid of all the dried salt from the ocean?"
    tz "Oh my bath was absolutely spectacular!"
    scene ch6sc10_463 with dissolve
    pl "*Noms* …"
    tz "I put in a great amount of soap and the sweat and salt came off easily after soaking for a good fifteen minutes."
    ori "That sounds so pleasant, you’re making me desire a bath as well after dinner."
    scene ch6sc10_465 with dissolve
    mc "You should, you’ve earned it."
    mc "I believe there should be enough coals to heat up the water for another bath."

    if ori_path == True:
        "Orianna locks eyes with you and gently smiles."
        scene ch6sc10_656 with dissolve
        ori "Oh I don’t know [mc]..."
        scene ch6sc10_657 with dissolve
        ori "I don’t think I would feel right in doing so…"
        scene ch6sc10_656 with dissolve
        ori "You haven’t bathed yet either."
        scene ch6sc10_657 with dissolve
        ori "I would simply feel greedy to claim the last bath."
        scene ch6sc10_656 with dissolve
        mc "We’ll go check how much coal is left after dinner, then we can decide who gets the bath."
        scene ch6sc10_657 with dissolve
        ori "Great idea… I’m sure we’ll find a solution… together."
        scene ch6sc10_465 with dissolve
        mc "*Chuckles* I believe we will."
        $ ori_trust += 2
        "Orianna likes your suggestion, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

    else:
        scene ch6sc10_466 with dissolve
        ori "Fantastic! I shall make the most of it then."

    scene ch6sc10_469 with dissolve
    tz "I suppose this means no game of cards tonight?"
    scene ch6sc10_470 with dissolve
    ori "*Giggles softly* I’m afraid so."
    ori "Although I will admit, I thoroughly had a great time playing with you guys last night."
    tz "Right?! I had so much fun as well!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_446 with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Everyone continues to enjoy dinner and the ale that accompanies it."
    "Friendly chatter and banter fills the room as everyone has become friends."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_472 with Dissolve(1.5)
    $ renpy.pause(0.5)
    pl "Huuuhh… it’s gone…"
    tz "*Giggles* Yeah, we really devoured all of it."
    scene ch6sc10_473 with dissolve
    tz "You can’t still be hungry? We ate enough to fill three people each!"
    pl "But-... yummy!"
    scene ch6sc10_472 with dissolve
    pl "Now there is no more yum…"
    mc "Don’t look so defeated, we still get to enjoy breakfast in the morning."
    pl "True… hnngh, okay. I suppose I better get started with the dishes."
    scene ch6sc10_473 with dissolve
    tz "I’ll help! I promised Orianna that I would set the table and help clean up afterwards."
    tz "Then we can let these two figure out the bathing situation."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "You and Orianna head to the deck for some air while Pearl and Taz take on the duty of cleaning up."
    scene ch6sc10_438 with Dissolve(1.5)
    play music mmm_elven_forest fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Nothing like fresh air after a meal like that."
    "Orianna giggles happily."
    scene ch6sc10_439 with dissolve
    ori "I couldn’t agree more."
    ori "I’m going to miss this."
    scene ch6sc10_440 with dissolve
    ori "[mc], I-... I’m going to miss you."
    scene ch6sc10_441 with dissolve
    mc "As I will you."
    mc "You have been great company, Ori. We’ve become friends quickly."
    scene ch6sc10_440 with dissolve
    ori "We really have, haven’t we?"
    scene ch6sc10_439 with dissolve
    ori "*Sighs* I suppose that will make parting ways with you even harder…"
    scene ch6sc10_438 with dissolve
    mc "It’s not goodbye, it’s until we meet again."
    mc "You know that."
    scene ch6sc10_439 with dissolve
    ori "I know… but when you finally find a genuine friend…"
    ori "You want to be around them, you know?"

    if ori_path == True:
        scene ch6sc10_440 with dissolve
        ori "Be close to them…"
        scene ch6sc10_441 with dissolve
        mc "I know what you mean."
        scene ch6sc10_442 with dissolve
        mc "Being close to someone you care about…"
        scene ch6sc10_443 with dissolve
        mc "There really is no feeling that matches the intimacy of the presence of a loved one."
        ori "*Moans softly* Ohh… [mc], I-... I agree."
        scene ch6sc10_444 with dissolve
        ori "Gosh! You really know how to make me feel lightheaded."
        mc "I think it’s time we get you into that bath."
        scene ch6sc10_445 with dissolve
        ori "Us… get us into that bath."
        mc "Oh? *Chuckles* You’re willing to share?"
        ori "*Snickers* Hurry, before I change my mind and get greedy!"
        mc "Right behind you and your perky ass."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc10_658 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ori "Mmh… I’ve been waiting for the chance to do this since we got onboard yesterday."
        ori "What do you think, [mc]? Think it’ll fit two?"
        scene ch6sc10_659 with dissolve
        ###Skill-check###
        if leadership >= 20:
            mc "Oh I believe we’ll manage to fit just fine."
            mc "Even if it's a tight squeeze, you'll just have to get on top of me."
            ori "*Giggles* There’s that confidence I enjoy."
            $ ori_trust += 2
            "Orianna finds your confidence attractive, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        else:
            mc "Sure, I think we should be fine."

        ori "Could you be a gentleman and get my skirt while I put my hair up?"
        scene ch6sc10_660 with dissolve
        mc "You needn’t ask me twice."
        ori "Nnh… I knew I could count on you."
        scene ch6sc10_661 with dissolve
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        with vpunch
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        "You rip off her skirt, ensuring she fully feels how much you desire to see her naked."
        ori "*Gasps* Aiyh! [mc]... I love how bold you are with me…"
        mc "Mmh… once more we find ourselves in this situation… 3rd time today?"
        ori "*Moans softly* Nngh… 4th, actually."
        scene ch6sc10_662 with dissolve
        ori "But you’re not the only one here who’s feeling bold tonight."
        "You feel her hand trace the waistline of your pants, gently toying with the edge as she caresses your arm with the other."
        ori "I too can be bold… let me show you just how bold I’m feeling in your presence.."
        scene ch6sc10_663 with dissolve
        ori "*Gasps* Ohh… I saw it last night at the game... I felt it earlier between my cheeks..."
        ori "But up close like this... in my hand... mmh... you're mine now."
        ori "You have a handsome cock, you know?"
        mc "*Chuckles* So I’ve been told."
        scene ch6sc10_664 with dissolve
        ori "I’ve never held a cock before… it’s so warm… so alive."
        ori "Would it… be okay for me to suck it a little? Just a small taste of what awaits me?"
        scene ch6sc10_663 with dissolve
        mc "You won’t lose your virginity by sucking it, so yes. Follow your desire."
        ori "Very well then… *Giggles softly* I will suck your cock, [mc]."
        scene ch6sc10_665 with dissolve
        "Orianna opens wide and begins to allow you entry into the warmth of her mouth, surrounding your cock with her full and exotic lips."
        mc "Ffuu… Ori your mouth is something else… those big lips of yours feel amazing."
        scene ori_lewd2 with dissolve
        $ renpy.pause()
        ori "*Muffled sucking* Nnh-mmgh… tasty… you cock is so delicious."
        ori "As the chef it is my duty to taste the inventory of the kitchen… *Sucks* Yet I missed out on this…"
        ori "I shall not let that happen twice- Mmh… nngh…"
        scene ori_lewd3 with dissolve
        $ renpy.pause()
        "Instead of the usual in and out motion of a typical blowjob, Orianna’s inexperience in the matter makes her different-"
        "-She keeps your tip and upper part locked between her big soft lips as she both sucks and intimately rubs her tongue all over you."
        mc "Mmgh… fuck… your intimate sucking is certainly making up for any lack of experience- Ahh…"
        with vpunch
        ori "Mmgh… I will gain experience- *Sucks and licks* experience by being with you… mmgh!"
        scene ch6sc10_666 with dissolve
        with vpunch
        mc "Aahh… Ori, I’m going to- Mmmgh! Your wet mouth is incredible- Ahh…"
        scene ch6sc10_667 with dissolve
        with vpunch
        "She holds your cock locked in her mouth as she feels your cum shoot down her throat and fill her mouth."
        with vpunch
        ori "{b}MMgh!! MMH!! GGHH!{/b}"
        "She does her best to contain all of your warm cum but she struggles and chokes slightly, finally having to release you."
        scene ch6sc10_668 with dissolve
        ori "*Gasps* Hnngh-Gghh… mmgh…"
        ori "Sorry… I couldn’t handle all of it… *Panting*"
        mc "Look at me."
        scene ch6sc10_669 with dissolve
        "She does as you ask, locking eyes with you."
        mc "Ori, what you just did was incredible, you managed to please me greatly with nothing but your mouth."
        mc "I don’t care if you can swallow it all as I orgasm or not, just seeing you try and actually enjoy it, that is enough."
        scene ch6sc10_670 with dissolve
        ori "You really mean that? That it’s enough that I was enjoying your cock?"
        scene ch6sc10_669 with dissolve
        mc "Of course. Just like I enjoyed your mouth, you did amazingly for your first time sucking a cock."
        scene ch6sc10_670 with dissolve
        ori "Had I known you would taste this great, I might have seduced you back in Arugoh. *Giggles*"
        scene ch6sc10_669 with dissolve
        mc "Had I known your mouth felt like this… I might’ve let you. *Chuckles*"
        scene ch6sc10_670 with dissolve
        ori "I will teach you cooking, in return you will teach me how to suck your cock to perfection. *Giggles softly*"
        ori "Deal?"
        scene ch6sc10_669 with dissolve
        mc "Five hells, Ori… yes, that’s a fucking deal."
        scene ch6sc10_670 with dissolve
        ori "That’s what I like to hear! I’ll just wipe my face off, I’ll join you in the bath in a moment."
        scene ch6sc10_671 with dissolve
        "Orianna proceeds to grab a spare cloth and wipe off the leftovers of your orgasm while you lean back and enjoy the view."
        mc "*Chuckles* You barred the door as well?"
        ori "Mhm-hm, I have no intention of letting the others interrupt our bath."
        scene ch6sc10_672 with dissolve
        ori "I’m feeling… a little greedy tonight."
        ori "After all, they got to enjoy relaxing with you earlier today… while I just had to watch as I steered the ship."
        mc "*Chuckles* Well, it worked in your favor in the end… cooking together and now bathing together."
        scene ch6sc10_673 with dissolve
        ori "*Snickers* I am a politician after all, I knew I just had to bide my time and play my cards right."
        ori "Pearl told me whilst assisting with breakfast she doesn’t like cooking and Tazzy told me how she longed for a bath."
        mc "Clever… you used that information to ensure I was the one who’d be assisting you in the kitchen."
        scene ch6sc10_674 with dissolve
        ori "Exactly… and with a little mention of not having had a bath yet, knowing they’d feel guilty about how we cooked for them…"
        mc "You ensured that they would volunteer to clean afterwards so we could have a bath."
        mc "I typically don’t particularly care for politics… but when used like this… I approve."
        ori "I’m glad you approve of my social maneuvering skills, I fully intend to use them when it comes to spending time with you."
        scene ch6sc10_675 with dissolve
        ori "But we have a situation that needs to be dealt with, my handsome assistant."
        mc "Oh yeah? Do tell, and I will ensure it’s dealt with."
        ori "That’s what I hoped you would say… Mmh, I have tasted you… but you have yet to taste me."
        scene ch6sc10_676 with dissolve
        "She delicately guides you to her dripping flower by wrapping her leg around your neck."
        "The enticing scent of her exotic little pussy which is dripping her juices right in front of you makes you harder than ever before."
        ori "Mmmgh… make me happy, [mc]."
        scene ch6sc10_677 with dissolve
        "She guides you further towards her until your lips makes contact with hers, and your tongue instinctively begin teasing her."
        ori "*Gasps* Ohh-ohh… what a feeling-Nnhh! Who would’ve thought having you taste me would be so…"
        scene ch6sc10_678 with dissolve
        ori "{b}So life-changing! Aiiyh! [mc]!{/b} I feel your tongue! You really enjoy my taste, don’t you?"
        scene ori_lewd4 with dissolve
        $ renpy.pause()
        mc "*Licks* Mmgh… the moment I caught a whiff of your exotic scent, I knew I wouldn’t want anything else for dessert."
        with vpunch
        ori "Aahh… I’m your dessert? Ohh… oh my! I love this! {b}I love being eaten by you!{/b}"
        mc "Mmgh… and I love eating you, Ori. Mmgh… if you don’t contain yourself you will climax in a moment."
        with vpunch
        ori "*Moans softly* Nothing would make me- Ahh… make me happier than to fill your mouth as you just did to me- Mmh!"
        with vpunch
        ori "*Moans loudly* {b}AHH! OH [mc]! Y-YOUR TONGUE!!!{/b} Aiiyhh, yes! Make out with my pussy! Ahh!"
        scene ch6sc10_678 with dissolve
        mct "Mmmh… here it comes."
        scene ch6sc10_679 with dissolve
        with vpunch
        ori "*Squeals* {b}Aiiyh-Ahh! What?! Aiiiyhh!! By all the gods!!{/b}"
        with vpunch
        "In an ecstasy of pleasure unlike any she’s ever felt, she erupts into your mouth, squirting uncontrollably."
        "She instinctively holds your head in place with her leg and foot as she overflows directly into your mouth."
        mct "Five hells she’s delicious… mmmgh… I can barely drink it all- Mmgh!"
        scene ch6sc10_680 with dissolve
        "Before you have time to react, she mounts you, and you hear her soft whisper."
        ori "A chef should always taste the goods that she delivers…"
        scene ch6sc10_681 with dissolve
        ori "*Muffled moan* Nngh… mmh! Mmh!"
        "She merges her big, soft and tasty lips with yours, intimately she slips her tongue onto yours, tasting her juices from you."
        mc "Mmgh… you’re an incredible kisser..."
        scene ori_lewd5 with dissolve
        $ renpy.pause()
        "Hearing that you are enjoying your first kiss together just as much as she is, she passionately keeps engaging you."
        ori "Mmgh… you’re not half bad yourself *Licks* Mmh… lots of practice?"
        mc "*Licks* A little here and there… Mmmh… but nothing that compares to you, these big full lips of yours feels incredible."
        ori "Mmgh… yours are amazing too, I would like to enjoy them every day… Mmh… keep licking my tongue like that."
        mc "You like sharing spit? Mmgh… you certainly seem eager to do it, mmmh."
        ori "How could I not enjoy that? Tasting myself on you combined with your saliva is… an experience I won’t forget."
        mct "An experience she won’t forget… after we part ways tomorrow, there’s no telling when we will see each other again."
        scene ch6sc10_681 with dissolve
        mct "I better give her something she’ll remember until we meet again."
        scene ch6sc10_682 with dissolve
        $ renpy.pause()
        "You firmly grab her firm and perky ass, lifting her up to your mouth and the surprise makes her arch backwards."
        scene ch6sc10_683 with dissolve
        with vpunch
        ori "*Squeals* {b}Aaiiiih! [mc]! What are you- Ahh!{/b}"
        scene ori_lewd6 with dissolve
        $ renpy.pause()
        "You answer her by sliding your tongue between her wet pussy lips and entering her."
        with vpunch
        ori "*Moans* Aah-AhH! Oh!! I see! Mmmgh! You want more dessert- {b}Aiiyhh!{/b}"
        "As her pussy juices keep running down onto her ass, you keep switching between licking her pussy and her ass."
        ori "Aahhh... licking my ass as well? Ohh-mmhmm... you're so thorough... so... attentive."
        with vpunch
        ori "[mc]- Aiiyh! *Gasps* I’m- I’m going to! {b}Aiiiiyhh! MMH!!{/b}"
        mct "*Sucks* Mmgh! She already came again?"
        mct "I guess the intimacy of our kiss as we pressed our bodies together kept her on the edge."
        scene ch6sc10_681 with dissolve
        "Upon drinking every last drop of her orgasm, you release her and she immediately clings on to you, embracing you in another kiss."
        scene ori_lewd5 with dissolve
        $ renpy.pause()
        ori "Mmmgh… you’re so naughty… share the dessert with me… *Licks*"
        ori "Nnh… I can’t believe you just did that to me… so brazenly handling me like that… Mmh."
        mc "You loved it… mmh…"
        ori "*Licks intimately* It would be pointless to deny it… after that orgasm. Mmgh…"
        scene ch6sc10_684 with dissolve
        "With her naked body fully pressed against you, your cock slides effortlessly between her ass cheeks."
        ori "*Licks tongue* Mmh… I’m going to show you- Nngh… what happens to naughty assistants that teases their chefs."
        scene ori_lewd7 with dissolve
        $ renpy.pause()
        "She begins rubbing herself against your cock, making sure to squeeze you as you slide between her exotic cheeks."
        mc "Fffhh… mmgh… that’s good… mmh…"
        ori "You already showed me how much you love my perky ass earlier- Mmgh… I will put that information to use- Aahh…"
        ori "A politician should always use information to their advantage- Mmh! Yes… lick my tongue just like that- Nngh…"
        with vpunch
        $ renpy.pause(1)
        with vpunch
        mc "{b}Ori- Mmgh! I’m going to- ffhh!{/b}"
        scene ch6sc10_684 with dissolve
        "She stops moving and instead focuses on squeezing and massaging your cock which is firmly lodged between her cheeks."
        with vpunch
        ori "*Moans* {b}Yes [mc]!{/b} I feel your cock pulsating- Oohh! Show me how much you enjoy me! Ahh!!"
        scene ch6sc10_685 with dissolve
        with vpunch
        mc "{b}Fuck!!{/b}"
        ori "*Moans* {b}Aiiyhh!{/b} Yes! Grab my ass like you own it! Mmh! Cover me in your delicious cum!"
        scene ch6sc10_686 with dissolve
        ori "*Panting softly* That’s twice… mmgh… twice you’ve covered my back in your warm cum."
        mc "A mans got to stake his claim."
        mc "Clearly the men of Arazalia have no idea what an incredible woman they are missing out on."
        mc "But I won’t make that mistake, Mmmh."
        scene ch6sc10_687 with dissolve
        ori "*Giggles* That is most pleasing to hear."
        ori "To think I had to travel all the way to Luxeron to find a man of your caliber-... so worth it though."
        scene ch6sc10_688 with dissolve
        ori "I’ll have to make sure I obtain more diplomatic missions to Luxenford in the future."
        ori "Knowing you will be here… will certainly make for much more ‘Enjoyable’ foreign relations. *Snickers*"
        scene ch6sc10_689 with dissolve
        mc "I like the sound of that."
        mc "I’ll be happy to entertain a wonderful diplomat such as yourself."
        scene ch6sc10_688 with dissolve
        ori "Hmm… I believe she would like that…"
        ori "But-... just to be absolutely certain, maybe you should show her more of what she can… expect from such a promise."
        scene ch6sc10_689 with dissolve
        mct "It’s a good thing she barred the door, we’ve already been at it over an hour… and she isn’t ready to stop yet."
        mc "Ambassador Orianna, allow me to show you exactly what you can expect from your future diplomatic missions to Luxenford."
        scene ch6sc10_690 with dissolve
        ori "*Whimpers softly* Nnnh-Nngh! Ohh… this is- nngh… certainly enticing!"
        "With your grasp on her firm ass, you begin moving her up and down..."
        "Rubbing her onto your cock, sliding it between her pussy lips and ass cheeks."
        scene ori_lewd8 with dissolve
        $ renpy.pause()
        ori "Oh [mc]... I can see how you managed to mesmerize a whole village now… mmmh."
        ori "You truly know how to read a woman’s desire and take advantage- Ahhh… yes… mmh."
        mc "It’s easy to read you, as I share your desire… I love how your little pussylips cover me in your juices even in the water."
        ori "*Moans softly* Ohh… I love how you guide me up and down by holding my ass- Mmmgh…"
        with vpunch
        ori "You handle me so well- Aahh… your touch… you cock rubbing against me… Nngh- I’m going to- {b}Aaiiyh!{/b}!"
        with vpunch
        ori "{b}I’m cumming [mc]! Aiiyhh! YES!!{/b} Rub me onto you just like that! AiiYyHH!!"
        scene ch6sc10_690 with dissolve
        with vpunch
        ori "*Moans* {b}AhhH!!{/b}"
        scene ch6sc10_688 with dissolve
        ori "*Panting softly* That was incredible… I {b}loved{/b} that!"
        scene ch6sc10_689 with dissolve
        mc "I had a feeling you would, I felt how you were quivering when you were doing it."
        mc "But having someone else control your movement, allows you to surrender yourself to the pleasure even more intimately."
        scene ch6sc10_688 with dissolve
        ori "Ahh… that explains why it felt even better, not to mention how you caressed my ass… I really enjoyed that."
        scene ch6sc10_687 with dissolve
        ori "*Giggles* Well, it seems like you managed to convince me!"
        ori "I shall take any and all diplomatic missions that would send me to Luxenford."
        scene ch6sc10_689 with dissolve
        mc "That’s what I like to hear. I look forward to reminding you exactly why you choose those missions."
        ori "*Bites lip* Nngh…"
        scene ch6sc10_687 with dissolve
        ori "As do I. I will require a lot of attention and reminding."
        scene ch6sc10_688 with dissolve
        ori "But I have faith that you will deliver on that."
        scene ch6sc10_681 with dissolve
        ori "*Kisses intimately* Mmmgh… I’m afraid our time is up here, I will have to wash off your cum before bed."
        mc "*Licks* Nnh… I wouldn’t mind if you kept it on."
        ori "*Kisses* You may be a king, but I am not yours… not yet."
        scene ch6sc10_686 with dissolve
        with vpunch
        ori "*Moans* Aiiyh!"
        "You grab her ass firmly."
        mc "You were saying?"
        ori "*Giggles* I-... I already forgot."
        scene ch6sc10_691 with dissolve
        ori "*Squeals* AhHh!"
        mc "I could drop your juicy ass onto my cock and claim you right this moment."
        ori "Aahh… [mc]-... d-don’t tempt me like this…"
        scene ch6sc10_686 with dissolve
        mc "Mmh… you’re lucky you’ve already satisfied me twice tonight."
        ori "Kiss me, King [mc]."
        scene ch6sc10_681 with dissolve
        ori "Mmmgh… as a King, it is of great importance you keep relations with foreign nations in high standing."
        ori "*Licks tongue* Nnghh… important that you… mmgh… keep me happy."
        mc "*Kisses intimately* You shall have anything you desire, Ambassador."
        scene ch6sc10_686 with dissolve
        ori "Careful… my desires run deep, as you’ve come to learn."
        scene ch6sc10_691 with dissolve
        ori "*Gasps* Aahh! Mmh… I love how you grab my ass as if it belongs to you already."
        mc "An exotic ass like yours… It’s mine already, we just haven’t made it official yet."
        scene ch6sc10_692 with dissolve
        ori "You’re so bold…"
        ori "Well, if my ass is yours already… then this is mine."
        scene ch6sc10_693 with dissolve
        "Orianna grabs you and turns you around, before you can react her tongue has already made contact with your cock."
        mc "Ffuu… Ori that’s… mmgh…"
        ori "Say it. *Licks intimately* Say that your cock belongs to me."
        mc "Mmmgh… it’s yours, whenever you crave it."
        $ ori_trust += 2
        "Orianna likes the idea of you and your cock being hers, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
        scene ch6sc10_694 with dissolve
        ori "*Licks* I’ll just clean off the leftovers…"
        ori "I would hate for it to go to waste. Mmmgh… such delicious cum."
        scene ch6sc10_693 with dissolve
        mc "Fuck Ori… I love having an Ambassador such as you in my corner."
        ori "*Licks* I have a feeling you will gain a great many benefits from our relations… Mmgh…"
        scene ch6sc10_694 with dissolve
        ori "As will I… *Sucks* Nngh… I am already envisioning a future where we can do this to our hearts content."
        scene ch6sc10_695 with dissolve
        mc "That’s what I like to hear… MMgh…"
        ori "It seems we got you all cleaned up… what a shame."
        ori "I will savor the taste of your cock until you fill my mouth again."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_696 with dissolve
        ori "Be a darling and put a towel out for me as well?"
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        mc "You got it, enjoy the rest of your bath."
        ori "*Giggles* Oh I will, I’m just going to soak a bit longer before I wash off the evidence of our… diplomatic relations."
        scene ch6sc10_697 with dissolve
        mct "*Chuckles* Our relationship has taken an interesting turn after setting off from A’nai."
        mct "Having an affair with a foreign diplomat could both be incredibly useful but also volatile."
        mct "She knows about A’nai… and at this point I have little interest in the world knowing about the tribe or my position as their leader."
        mct "Yet, I trust her… she has been genuine with me thus far."
        scene ch6sc10_698 with dissolve
        mct "Us being intimate… that’ll only strengthen our desire to support each other."
        mct "Aruna island is also located at a prime location for Arazalia to establish more trade routes with Luxeron."
        mct "Just like Looter’s Bay, if I decide to open Aruna to trade at some point, that will be an incredibly valuable asset to have."
        scene ch6sc10_697 with dissolve
        mct "But I won’t make such a decision lightly, for now the tribe needs time to rebuild themselves after the reunion."
        mct "But if I were to make that choice one day, Orianna would be a key player in making it a reality."
        mct "She knows the tribe, she knows me, and she is closely connected to the Queen of Arazalia."
        scene ch6sc10_698 with dissolve
        mct "For now, I will enjoy her company and get to know her better."
        mct "In the future I will be able to rely on her, be it directly through her role as an Ambassador or indirectly as an advisor to me."
        mct "With my limited experience in politics… having a woman such as her backing me will go a long way."
        scene ch6sc10_699 with dissolve
        mct "Princess Amelia… Queen Merida… Ambassador Orianna…"
        mct "King of A’nai, owner of a larger piece of land, bodyguard of the Princess… fuck, am I becoming a noble?!"
        mct "Fuck me…"
        scene ch6sc10_700 with dissolve
        mct "I need to rest…"
        mct "Yeah, definitely need rest."

    else:
        scene ch6sc10_441 with dissolve
        mc "I know… now, go enjoy your bath. Otherwise I will claim it."
        scene ch6sc10_440 with dissolve
        ori "You wouldn’t dare!"
        scene ch6sc10_439 with dissolve
        ori "*Sighs* I guess I better get to it. Goodnight [mc]."
        scene ch6sc10_445 with dissolve
        mc "Goodnight Ori, enjoy the bath."
        ori "I will, my body is aching to be soaked in warm water."

    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss39 with Dissolve(1.5)
    $ renpy.pause()
    scene ch4sc10_021 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch6sc10_701 with Dissolve(1.5)
    $ renpy.pause(0.5)
    "About an hour or so post dawn, you finally arrive in Looter’s Bay."
    scene ch6sc10_702 with dissolve
    di "It appears your prayers have been answered at long last, Red."
    ki "I told you he would succeed!"
    scene ch6sc10_703 with dissolve
    di "Yes… I suppose you did tell me, once or twice."
    ki "You know what this means right? He wouldn’t have returned without your Ambassador."
    scene ch6sc10_704 with dissolve
    di "Let’s hope for all your sakes that he is as capable as you believe him to be."
    di "I won’t intrude on your reunion, I’ll send for him later."
    ki "Thank you! I’ll be sure to tell him to report to you!"
    di "..."
    scene ch6sc10_705 with dissolve
    ki "*Excitedly* I can’t believe they’re finally back!"
    ki "[mc]... Pearl… I’m going to hug them til they suffocate! *Giggles happily*"
    scene ch6sc10_706 with dissolve
    with vpunch
    ki "Sis!"
    pl "*Giggles happily* Hi…"
    scene ch6sc10_707 with dissolve
    with vpunch
    ki "[mc]! Mmgh!"
    mc "Hey, Red. *Chuckles*"
    scene ch6sc10_706 with dissolve
    ki "I was so worried about you! You’re not hurt, are you?"
    pl "No, I’m perfectly healthy as you can see."
    scene ch6sc10_707 with dissolve
    ki "[mc]... thank you so much… thank you for keeping my sister safe."
    mc "You know I wouldn’t have let anything happen to her."
    scene ch6sc10_706 with dissolve
    pl "Seas sis! You’re such a worry bug! You know I can handle myself."
    ki "I’m just so glad you’re okay… we’ve never been separated this long before."
    scene ch6sc10_707 with dissolve
    ki "And you! I wasn’t too worried about you… having seen you in action myself."
    ki "Buuut… maybe a teeny tiny bit of me was worried for you as well."
    mc "Pearl, I think we need to find a spot for Kira to lay down, she’s talking nonsense. *Chuckles*"
    scene ch6sc10_708 with dissolve
    ki "*Whispers* {size=-10}{b}I’d love for you to lay me down- I mean, speak to you in private.{/b}{/size}"
    mc "*Chuckles* C’mon, let's find somewhere to talk, I’m sure you’ve got a ton of questions."
    ki "One moment, just need to embrace my sister one more time before we go."
    scene ch6sc10_706 with dissolve
    pl "*Giggles* H-Hey! You don’t have to be so affectionate, you know?"
    ki "I know… but I want to."
    ki "I’m going to catch up with [mc] for a bit, go find Kelly, she has been eager for your return to hear about your adventure."
    pl "Sure thing! I have quite a few stories to tell! *Snickers*"
    scene ch6sc10_709 with dissolve
    ki "So… we can talk at the tavern, or-..."
    ki "We can talk in my room… choice is yours."
    ####Choice####
    menu:
        "Your room, definitely. ({color=#ff8cdd}Kira Romance{/color})":
            scene ch6sc10_710 with dissolve
            mc "I don’t think I’ve ever actually been in your room as of yet?"
            $ kira_relationship = True
            scene ch6sc10_709 with dissolve
            ki "Right! That settles it then… we’re going to… {b}‘talk’{/b} in my room. *Giggles*"
            scene ch6sc10_710 with dissolve
            $ kira_path = True
            mc "I look forward to hearing your {b}moans{/b}- I mean, hearing what you have to say."
            scene ch6sc10_709 with dissolve
            ki "*Snickers* Let’s not waste any more time out here…"
            ki "I’m so desperate to… talk to you."

        "Let’s go to the tavern. ({color=#2bff8b}Kira Friendship{/color})":
            scene ch6sc10_710 with dissolve
            mc "I’m thinking the tavern will be a good place to catch up."
            $ kira_relationship = False
            mc "Plus, I’d love some ale."
            scene ch6sc10_709 with dissolve
            $ kira_path = False
            ki "I couldn’t agree more, no reunion is proper without ale! *Giggles*"
            ki "C’mon, let’s go see if Creed has a table for us."


    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss15 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_083 with Dissolve(2.5)
    $ renpy.pause(0.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    sy "Dalen, are you sure keeping Eliza in a coffin is the best course of action?"
    sy "I can’t imagine that it’s very pleasant."
    da "Sylph, we’ve been over this."
    scene ch6sc10_711 with dissolve
    da "Neither of us want her to be sealed in a coffin."
    da "But as we don’t know what her cravings and eventual bloodlust will surmount to, this is the safest for everyone."
    da "You know how deeply it would affect her if she accidentally hurt one of us or gods forbid it, an innocent."
    scene ch6sc10_712 with dissolve
    sy "You’re right… as usual."
    sy "I still think we should’ve given her a pillow and a blanket though!"
    sy "A wooden coffin on it’s own sounds horrendously uncomfortable."
    scene ch6sc10_711 with dissolve
    da "If we find ourselves in a similar situation in the future, we will prepare for it better."
    da "I was hoping [mc] would’ve returned by now, he’s been gone for several weeks."
    scene ch6sc10_712 with dissolve
    sy "He’ll be back soon-ish! Mhm-hm! Trust in your friendly fae, she senses these things!"
    da "*Sighs* We both know you have no such senses… but I will believe it nonetheless."
    sy "Great! Now what are we doing today-"
    scene ch6sc10_713 with dissolve
    da "Hmm?"
    sy "Borri! My favorite dwarf in all of Midomir!"
    scene ch6sc10_715 with dissolve
    br "G'day t’ yer."
    br "How are things with the lass?"
    scene ch6sc10_713 with dissolve
    sy "She’s been quiet, I believe she has fallen into a deep slumber as she desiccates."
    da "Hey Borri, good thing you’re here this early. I could use your help today."
    scene ch6sc10_715 with dissolve
    br "Eh? Yer need me help?"
    scene ch6sc10_714 with dissolve
    da "Yes, I’m currently in the process of renovating our old courtyard out back."
    da "It has been used for storage and left in disarray, but I want to restore it and repurpose it to a training area for adventurers."
    scene ch6sc10_715 with dissolve
    br "Aye, that sounds like something we could make great use of, what ye need of me?"
    scene ch6sc10_714 with dissolve
    da "You and I will be going shopping, we’ll need basic tools and some target dummies."
    scene ch6sc10_715 with dissolve
    br "Heh! Normally I’d moan about going shoppin but fer tools and equipment? Count me in!"
    scene ch6sc10_716 with dissolve
    sy "Shopping? Heck yeah!"
    da "You’re not coming, someone has to tend to the guild."
    sy "One of these days I’m going to make you levitate upside down! For at least two hours!"
    scene ch6sc10_715 with dissolve
    br "Heh… that would be a sight!"
    br "Yer ready t’ head out now then?"
    scene ch6sc10_714 with dissolve
    da "Hold on, I want to show you the courtyard first, to give you an idea of what we’re working with."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_717 with Dissolve(1.5)
    $ renpy.pause(0.5)
    br "Bloody-eh! Yer weren’t kidding when ye claimed it was left in disarray!"
    da "Yeah… when it went downhill for the guild, we didn’t have enough members to warrant a maintained courtyard."
    da "But now that things are turning around and with everyone training together, I thought it was time we restore it."
    br "Aye… it certainly would be great t’ have such a place te hang out and train with the others."
    br "I had no idea the guild had this much space?"
    da "Currently only one section of the guild is being used, as you know, Sylph recently restored the dormitories for you and Milton."
    br "Aye… the lass did great with that."
    da "As for the rest of the buildings, they came with the lot when I purchased it. I got a discount though."
    da "When I revealed to King Bennen that I wanted to form a guild, he suggested this lot as the buildings had been abandoned."
    da "It previously belonged to a wealthy noble, but their lineage ended as no children were born to carry on their name."
    br "Heh! Their loss, our gain!"
    da "It’s certainly better to use it as a guild headquarters than just for personal living, seems too wasteful of the space."
    da "C’mon, let’s go buy some supplies… as you can see, we’ll be busy for the coming days."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ss8 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)

    if kira_relationship == True:
        scene ch6sc10_718 with Dissolve(2.5)
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause()
        scene ch6sc10_719 with Dissolve(1.5)
        $ renpy.pause()
        mc "Huh… so this is your room."
        ki "Do you… like it?"
        scene ch6sc10_720 with dissolve
        mc "*Chuckles* Yeah, it’s cool. That brings back memories…"
        mc "How did you-"
        scene ch6sc10_721 with dissolve
        ki "There’s a painter here in Looter’s Bay, all I had to do was explain the situations I was in and he was able to paint it."
        mc "Impressive… you’ve been very descriptive."
        scene ch6sc10_722 with dissolve
        mc "This is us…"
        mc "When we warmed by the fire in the cave on Inmortui."
        scene ch6sc10_723 with dissolve
        mc "I remember it like it was yesterday… you kept ogling me as I undressed."
        ki "S-Shut up! It was my first time seeing a man naked… and-... you’re incredibly attractive you know?!"
        scene ch6sc10_724 with dissolve
        mc "*Chuckles* Compliment accepted."
        ki "*Scoffs lightly* And I remember something about that as well…"
        ki "How your eyes were glued to my breasts when I took off my wet shirt!"
        mc "You’ll never catch me apologizing for enjoying seeing your perky breasts for the first time."
        scene ch6sc10_725 with dissolve
        ki "G-Good! I wouldn’t have wanted you to apologize for seeing my breasts!"
        ki "In fact-... I was really happy that you enjoyed watching me be naked in front of you! Hmpfh!"
        mc "*Chuckles* This one is a little dark, but it’s definitely from when you were all excited about exploring the tunnels."
        scene ch6sc10_726 with dissolve
        ki "I had a great deal to be excited about…"
        ki "I was out on my own, exploring uncharted caves with a man who filled every inch of my body with excitement."
        mc "I felt it too… it was hard not to be excited with a fiery woman keeping me on my toes."
        scene ch6sc10_727 with dissolve
        mc "This one, ah yeah…"
        mc "I had to carry you all the way out of the cave after you had been weakened by that Necromancer’s gas."
        ki "It was the first time I ever had a man carry me…"
        scene ch6sc10_728 with dissolve
        ki "Mmgh… your hair was longer back then."
        "You feel Kira’s delicate touch as she runs her fingers through your hair and to your surprise you feel naked breasts squished against your back."
        mc "Yeah… I got a haircut on the island where I’ve spent the last couple of weeks."
        ki "I like it…"
        scene ch6sc10_729 with dissolve
        ki "*Whispers softly* {size=-10}{b}[mc]...{/b}{/size}"
        scene ch6sc10_730 with dissolve
        ki "*Whispers softly* {size=-10}{b}Do you remember this feeling?{/b}{/size}"
        scene ch6sc10_729 with dissolve
        mc "Mmgh… it’s a feeling I’ll never forget… I first felt it when you slept on top of me in the cave."
        scene ch6sc10_730 with dissolve
        ki "And then later, when I washed you in the rejuvenation pools, after you had risked your life to protect me."
        scene ch6sc10_729 with dissolve
        mc "It was a lovely bath… mmgh."
        scene ch6sc10_730 with dissolve
        ki "*Whispers softly* {size=-10}{b}One I will remember for the rest of my life…{/b}{/size}"
        scene ch6sc10_729 with dissolve
        mc "I remember how your breasts explored my back as you rubbed the water over my wounds."
        scene ch6sc10_730 with dissolve
        ki "MMmgh… [mc]-"
        scene ch6sc10_731 with dissolve
        with vpunch
        ki "*Squeals* {b}Aiiyh! Finally!{/b}"
        ki "I’ve been waiting for you to do something reckless and irresistibly hot. *Giggles happily*"
        mc "Oh have you now… you have no idea what I’m about to unleash on this gorgeous little body of yours."
        ki "Oh I can imagine a fe-"
        scene ch6sc10_732 with dissolve
        with vpunch
        ki "*Squeals* {b}Feeeeeew! Aiiiyh!{/b}"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_733 with dissolve
        with vpunch
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        "Immediately upon her landing on the bed, you dive between her juicy thighs and proceed to hold up her waist."
        ki "*Moans* {b}AaahhH! [mc]{/b}- Y-Yes! Taste me! Inhale the scent of my wet kitty!"
        "You feel her fingers slide through your hair and grasp the back of your head, together with her thigh, she locks you in place."
        scene ki_lick3 with dissolve
        $ renpy.pause()
        ki "*Moans* Aaiiyh… ahh! Ohh I’ve been so eager for this you have no idea- Mmh…"
        ki "Feeling your warm tongue slide between my wet lips and tease my entrance- {b}AhhhH!{/b}"
        mc "*Inhales deeply* Mmmgh… I can’t get enough of your taste and scent… *Licks intimately*"
        with vpunch
        $ renpy.pause(1)
        with vpunch
        ki "{b}Ahhh! [mc]!{/b} If you keep doing that- Aiiiyh! I’m going to- {b}AHH!!{/b}"
        scene ch6sc10_733 with dissolve
        with vpunch
        ki "{b}YES!!{/b} K-Keep licking me while I overflow into your mouth- Aiiyhh! My pussy belongs to you!"
        scene ch6sc10_734 with dissolve
        mc "*Slurps and licks* Mmgh! Mmmgh! So good."
        with vpunch
        ki "*Squeals and moans* {b}Aiiyh-AhhH!!{/b} [mc]- K-Keep tasting me like that! Aiiyhh! I love feeling your tongue!"
        scene ki_lick4 with dissolve
        $ renpy.pause()
        "Hear her moans begging for you to continue enjoying her pussy, you decide to keep at it."
        mct "Mmmgh… she’s already close again, we haven’t been intimate since our way back from Inmortui."
        mct "She’s been longing for this moment, and so have I- Mmmgh… damn she’s delicious."
        with vpunch
        ki "*Moans* {b}Aiiyh! Y-Yess! My pussy belongs to you!{/b} Ah-Aah! And so does the rest of me!"
        with vpunch
        "Kira begins to shake and her pussy overflows once more, allowing you to drink her sweet juices."
        scene ch6sc10_734 with dissolve
        ki "{b}Aiiyhh! Drink me baby!{/b} Aiiyhh! Drink as much as you want- AhnH!"
        scene ch6sc10_735 with dissolve
        ki "*Moans* {b}[mc]! Nnghh! I need your cock in my mouth!{/b}"
        ki "Fuck my mouth like you mean it!"
        scene ch6sc10_736 with dissolve
        ki "Mmgh- Mmmh… *Licks* No wonder you licked me to two orgasms… I taste pretty good! *Licks*"
        mc "Mmh… that you do."
        ki "Now put that big cock of yours in my mouth… I miss it."
        "Kira caresses your tongue with hers a few more times before you stand up and proceed to undress for her."
        scene ch6sc10_737 with dissolve
        ki "That’s what I like to see… mmh."
        ki "It’s been so long since I’ve seen you naked… I miss it… I miss you."
        scene ch6sc10_738 with dissolve
        mc "I’ve missed you too, Red."
        mc "Ready to have your throat filled and your mouth fucked?"
        ki "*Giggles happily* Yes!"
        ki "Fill my mouth, you already know it’s yours."
        scene ch6sc10_739 with dissolve
        ki "*Moans* Ghh-Mmh! Just as big as I remember- Mmgh-Nngh! *Sucks*"
        mc "There’s that warm tight mouth of yours I’ve missed… mmh… and that eager tongue working your saliva all around me."
        scene ki_lewd1 with dissolve
        $ renpy.pause()
        mc "*Moans* MMh… fuck- Kira… you’re such a good little slut… mmgh… you know how to work that mouth for me."
        ki "*Moans and chokes* Nngh!! {size=+5}{b}GghhgH!{/b}{/size} MmghH! *Sucks and licks* {b}MMH! MMhh!{/b}"
        mc "That’s it… mmh… you’re getting used to the feeling of my cock sliding down your throat… mmgh…"
        with vpunch
        ki "*Choking* {b}Nnghh!{/b} Mmmh! {b}Fillhh me!{/b} Mmghh! {b}GghH!{/b} Fillhh my thhroat! {b}AgghhH!{/b}"
        scene ch6sc10_739 with dissolve
        with vpunch
        mc "Five hells! Mmmgh! Here it comes- {b}AahH!{/b}"
        scene ch6sc10_740 with dissolve
        with vpunch
        ki "*Muffled choking* {size=+3}{b}MMH! GGHH!! MHGH!!{/b}{/size}"
        "As you begin shooting loads of warm cum down her throat, she does something you didn’t expect."
        "She holds on to you firmly, you even feel her nails dig into your skin as she chokes and swallows your cum."
        with vpunch
        mc "*Moans* Fffuu! Kira what are you- Mmh!!"
        scene ki_lewd2 with dissolve
        $ renpy.pause()
        ki "Gghgh! Mmgh… I told you to fuck my mouth- {b}Mmmg-Gghh! Fill it again!{/b}"
        with vpunch
        mc "Fuck… Mmgh! One choking of cock and cum wasn’t enough for my little pirate slut? Nngh!"
        with vpunch
        ki "More! *Sucks harder* MMghh! *Gags* {b}Ggghrh! GhHH! Fillhh my throat again!{/b}"
        with vpunch
        "The sensation of her tongue passionately rubbing her saliva onto your cock-"
        "-As she pulls and pushes herself onto you sends you over the edge."
        with vpunch
        ki "*Gags* {b}Mmghh-Ggghh!{/b} That’s it! Satisfy your sluts cravings! While she eats your cockhh! {b}Mmghh!!{/b}"
        scene ch6sc10_740 with dissolve
        mc "{b}AhhH!{/b} You want more? Here you go- Fffh!!"
        scene ch6sc10_741 with dissolve
        with vpunch
        "With her mouth stuffed with your hard cock and her throat filling with your cum-"
        "-It begins to overflow from her mouth, running down her neck."
        ki "*Chokes* Hhghh-Ghgghh… ghhh… mmh…"
        scene ch6sc10_742 with dissolve
        "After having swallowed your cum, you feel her hand in yours, softly squeezing as she catches her breath."
        ki "[mc]... I-... I love you."
        scene ch6sc10_743 with dissolve
        mc "*Chuckles* I love you too, Kira."
        scene ch6sc10_742 with dissolve
        ki "You… you liked it, right?"
        scene ch6sc10_743 with dissolve
        mc "Five hells… you really have to ask after receiving two loads? Fuck… yeah, I loved that."
        "She giggles while she rests her soft cheek against your cock."
        scene ch6sc10_742 with dissolve
        ki "I loved it as well… your cock is just as delicious as I remember it being."
        ki "Now that we’ve tasted each other… we’re ready for the main event. *Giggles*"
        scene ch6sc10_743 with dissolve
        mc "Seeing these paintings of us back on Inmortui has gotten me feeling nostalgic…"
        mc "I want you to ride me like you did back in the cave on Inmortui… I long to watch those perky breasts of yours bounce again."
        scene ch6sc10_742 with dissolve
        ki "*Giggles softly* Mmmh… that is something I’m happy to provide you with. Lie down for me baby."
        ki "I'll just go wipe off your cum and I'll join you."
        scene black with Dissolve(1.5)
        "Kira finds a cloth and wipes off your leftover cum, then she mounts you in bed."
        scene ch6sc10_744 with Dissolve(1.5)
        ki "*Moans* Aaiih-ahh… someone is eager for me… mmmh!"
        "As Kira mounts you, she rests herself back against your cock-"
        "-While she guides your head to her breasts and you wrap your arms around her."
        "She is your woman and you have no intention of letting her feel any different."
        ki "*Moans softly* [mc]... I love being held by you… especially when you’re enjoying my breasts."
        scene ki_lewd3 with dissolve
        $ renpy.pause()
        "The intimacy of your naked embrace makes Kira rub herself against you, allowing your cock to slide between her plump cheeks."
        ki "Aahh… I love feeling you… your strong hands… your hard cock… your tender lips around my nipples… Ahhh…"
        mc "*Sucks* As I love feeling you… mmh… your delicate caress… your soft curvy body… mmh… the happiness in your voice as you moan."
        ki "How could I not be happy… mmgh… I’m in the arms of the man I love above all else."
        scene ki_lewd4 with dissolve
        $ renpy.pause()
        ki "*Moans softly* Aahh… I love how you suck my breasts… it makes me feel so close to you baby…"
        mc "Mmmh… They’re as incredible as I remember them to be, and as tasty… mmh. *Sucks*"
        ki "*Moans* Aahh… they’re all yours… all of me is yours… I’m yours, [mc]."
        scene ch6sc10_744 with dissolve
        ki "[mc]-... I… I need you inside of me… lean back and let me ride you… let me satisfy the man I love."
        scene ch6sc10_745 with dissolve
        mc "Fuck Kira… you know how to make me enjoy every moment of us to the fullest."
        "Kira’s soaking wet pussy easily opens for you as she presses herself down onto you."
        ki "*Moans softly* [mc]... I'm going to make love to you now... mmhh..."
        scene ki_lewd5 with dissolve
        $ renpy.pause()
        ki "*Moans* Mmmh… you belong inside me- Nnnh… I love you."
        mc "Ffhh… I love you too. Mmmh…"
        ki "Just enjoy me as I make love to you baby… mmh… let me take care of you."
        ki "*Moans softly* Mmmh- [mc]... I love riding you slowly like this... I get to feel every inch of you."
        mc "Y-Yeah... fuck... and I'm getting to experience just how tight and wet you are... mhHh..."
        mc "Mmmh… you really know how to take care of a man’s needs."
        ki "Only yours… mmh… your needs are the only ones I will ever fulfill- Aahh… I’m going to go faster now baby… {size=+3}{b}I need you deeper{/b}{/size}."
        scene ki_lewd6 with dissolve
        $ renpy.pause()
        with vpunch
        ki "*Squeals* Aiiyh! Mmh! {b}Oh-OHH!{/b} I had forgotten how it feels to have you stretching me deep inside! {b}AiiiiHH!{/b}"
        mc "Fuck you’re tiiiiight- Ahh!"
        ki "You’re pulsating baby! MMh! I’m not going to be able to stop- Aiiiyhh! {b}I’m going to cum!{/b}"
        with vpunch
        mc "{b}Ffhh! Me too! Ahh!{/b}"
        scene ch6sc10_745 with dissolve
        with vpunch
        ki "*Moans loudly* {b}Aiiiyh- [mc]!! YES!! I feel your cum inside me! Keep filling me!{/b}"
        scene ki_lewd5 with dissolve
        "As she feels your orgasm and her own combine inside of her, she falls to your chest, but she keeps making love to you."
        $ renpy.pause()
        ki "*Panting softly* Nngh… you’re so good to me… mmmh..."
        mc "Mmh… you’re the one who’s showering me with affection right now- mmmh…"
        ki "I love feeling you inside me, especially when we climax together… ahh…"
        scene ch6sc10_746 with dissolve
        with vpunch
        ki "*Giggles* ohh… it seems like you gave me more than my pussy could contain."
        ki "Mmmgh… our love combined within my little pussy… deep inside me. I love it…"
        mc "Seems like our lovemaking left a bit of a mess… *Chuckles*"
        ki "*Giggles* That’s how I prefer it… shows me you didn't hold back with me."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_747 with dissolve
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        ki "I’ll just go wipe off and then I want to snuggle!"
        mc "With an ass like that… you can have anything you want."
        ki "Stop it… *Giggles* You’re being bad."
        scene ch6sc10_748 with dissolve
        ki "That should be all of it… what do you think baby?"
        mc "You look perfect… come here."
        mc "And walk slowly."
        scene ch6sc10_749 with dissolve
        ki "*Giggles* Oh? You wish to see me approach you in bed?"
        mc "I love watching you walk towards me… especially while you’re naked."
        scene ch6sc10_750 with dissolve
        ki "Then I better be a good girl and… provide you with what you desire."
        mc "Mmh, I love you…"
        scene ch6sc10_751 with dissolve
        ki "Nnnh… it makes me so incredibly happy when you tell me that… I love you as well, baby."
        "Kira slips her tongue into your mouth, caressing yours with her warm saliva before she proceed to snuggle up next to you."
        scene ch6sc10_752 with dissolve
        ki "MMhh… this is all I want, [mc]. All I want in life."
        mc "It feels good, doesn’t it?"
        scene ch6sc10_753 with dissolve
        ki "Naked in your arms… making love… not worried about anything… being petted by the man I love and adore."
        ki "I feel… happy."
        scene ch6sc10_752 with dissolve
        ki "Happier than I’ve ever felt."
        scene ch6sc10_754 with dissolve
        ki "*Moans softly* Aahh…"
        mc "There’s no woman I’d rather have in my arms right now, Kira."
        mc "No woman’s scent I’d rather enjoy… or breasts I’d rather caress."
        ki "Nnnghh… you know how I love when you touch my breasts… *Giggles softly*"
        scene ch6sc10_753 with dissolve
        ki "Thank you…"
        ki "You always know how to make me feel really special."
        scene ch6sc10_752 with dissolve
        mc "I’m glad I can make you feel that way, you deserve it."
        ki "[mc]... I know I’ve said it several times today… but I love you."
        scene ch6sc10_754 with dissolve
        ki "*Gasps* Aahhh- Mmmh…"
        mc "I’ll never get tired of hearing it… I love you too, Red."
        mc "You’re my little pirate. Nothing will change that."
        scene ch6sc10_755 with dissolve
        ki "Mhm, I’m yours and only yours."
        ki "[mc]... will you tell me about your adventure?"
        mc "I’ll be happy to."
        ki "*Giggles* And don’t even think to stop touching me… it keeps me… engaged in the story!"
        scene ch6sc10_754 with dissolve
        with vpunch
        ki "*Squeals* Aiiyhh!"
        "You give her breast a gentle squeeze in agreement."
        mc "I wouldn’t dare to stop caressing you, now listen up…"
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You begin sharing your tale of what had transpired over the last three weeks since you and Pearl set out for Aruna."
        scene ch6sc01_341 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "About how you and Pearl made short work of the trip to the island."
        scene ch6sc02_042 with dissolve
        "You went over how you were shipwrecked by an unknown inhabitant of the island."
        scene ch6sc02_064 with dissolve
        "How you and Pearl had to swim miles to reach the shore."
        scene ch6sc02_155 with dissolve
        "About foraging for berries and munching of them despite their unknown effects."
        scene ch6sc02_239 with dissolve
        "You tell her about how you got separated from Pearl and whilst looking, you were tranq’d."
        scene ch6sc02_278 with dissolve
        "You share about meeting Echo, the A’nu of A’nai for the first time, and how she opened her home to you."
        scene ch6sc02_547 with dissolve
        "You tell her about how you got intertwined in their life and were set upon an ancient path."
        scene ch6sc02_565 with dissolve
        "A path of ancient civilizations, mysteries and gods."
        scene ch6sc02_581 with dissolve
        "How you faced challenges and trials, as you uncovered ancient artifacts."
        scene ch6sc02_596 with dissolve
        "One such relic you still wear to this day."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc10_752 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ki "*Gasps* An artifact of the Divines?"
        ki "Just like… the Chalice of Vitality we were after on Inmortui?"
        mc "Correct, the necklace or talisman if you will, that I’m wearing is an artifact created by the Divine, Malpheon."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc02_650 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You continue by telling how you came across Pearl in the jungle after having completed the temple."
        scene ch6sc02_731 with dissolve
        "How Echo’s hospitality also expended to Pearl and the two of you were well looked after."
        scene ch6sc02_1198 with dissolve
        "You tell her how you led a small expedition into the jungle to search for the Ambassador."
        scene ch6sc02_1296 with dissolve
        "How you encountered a strange mist which made navigation near impossible."
        scene ch6sc03_110 with dissolve
        "You share how you managed to unlock a 2nd temple with one of the locals."
        scene ch6sc03_201 with dissolve
        "About the challenges that you overcame within."
        scene ch6sc03_320 with dissolve
        "You tell her about how you met one of their goddess."
        scene ch6sc03_329 with dissolve
        "Gaia, the Maiden of Life, Nature and Balance."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc10_752 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ki "You met another goddess?!"
        scene ch6sc10_753 with Dissolve(1.5)
        ki "You also met one when you picked up the Chalice of Vitality, no?"
        mc "Mmh, I did."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc02_387 with Dissolve(1.5)
        $ renpy.pause(0.5)
        mc "Gaia was but one of three goddesses I encountered during this journey."
        scene ch6sc02_388 with dissolve
        mc "The other two being Malanthe."
        scene ch6sc02_389 with dissolve
        mc "And Maia."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You continue your tale of everything that had happened over the last three weeks."
        scene ch6sc10_755 with Dissolve(1.5)
        $ renpy.pause(0.5)
        ki "I almost can’t believe everything you’ve been entangled with in just a matter of a few weeks."
        ki "Now I’m even more grateful that you and Pearl made it back unscathed."
        scene ch6sc10_756 with dissolve
        mc "I would never let anything happen to her. *Kisses shoulder* I promised you."
        ki "*Giggles* Yes you did… and you fulfilled your promise like a real man."
        scene ch6sc10_757 with dissolve
        ki "Mmmh… I can’t believe you’re an A’khan? Or a King, if we’re to use proper terms."
        mc "It sort of just happened… *Mwah*"
        ki "*Giggles happily* Nnhh…"
        scene ch6sc10_756 with dissolve
        ki "You’re spoiling me… I like this side of you."
        mc "You’re worth exposing it to… but if you tell anyone, I may have to make you walk the plank."
        scene ch6sc10_758 with dissolve
        ki "K-Keep kissing me like that and I will keep your secret forever! *Giggles*"
        scene ch6sc10_759 with dissolve
        mc "Like this? *Mwah* Or…"
        scene ch6sc10_758 with dissolve
        mc "Like this? *Mmmh*"
        scene ch6sc10_759 with dissolve
        ki "*Moans* Oh… keep doing that… it’s hard to decide… mmh."
        scene ch6sc10_758 with dissolve
        "As you keep caressing her and showering her with kisses, she subconsciously rubs her ass back against you."
        scene ch6sc10_759 with dissolve
        "She clearly feels your hard cock sliding between her thighs and wet pussylips."
        scene ch6sc10_758 with dissolve
        ki "*Giggles* Oh [mc]... your secret is forever mine. Nnnh…"
        scene ch6sc10_759 with dissolve
        mc "Promise you won’t tell anyone I have a soft spot for gorgeous red-headed pirates?"
        scene ch6sc10_758 with dissolve
        ki "I-... mmgh… I promise baby."
        scene ch6sc10_757 with dissolve
        mc "*Mwah* That’s my girl."
        scene ch6sc10_760 with dissolve
        "Kira presents her tongue and as she licks your lips, you happily answer with yours."
        ki "Mmgh… here baby… taste me."
        ki "I’m your girl. *Licks* Mmh… I’ll always be your girl."
        scene ch6sc10_761 with dissolve
        mc "Your tongue is as tasty as ever… mmh…"
        ki "*Licks intimately* You like my tongue? Good… keep licking me then… nnh… share your saliva with me baby."
        "The two of you continue caressing each other while your cock is firmly locked between her thighs and your tongues eagerly share saliva."
        scene ch6sc10_760 with dissolve
        ki "Mmmh… that’s what I call making out. *Licks*"
        mc "How are we ever supposed to get out of this bed with you being this delicious… mmh."
        ki "I have no desire to leave this bed… not ever."

        if harem_path == True:
            scene ch6sc10_756 with dissolve
            ki "*Snickers* I can't believe you have a whole ass island filled with exotic women..."
            ki "All yours... all wanting to satisfy you... *Scoffs* They don't know you well enough to satisfy you!"
            scene ch6sc10_757 with dissolve
            mc "*Mwah* My little captain is jealous? Cute."
            ki "Nnhh... no... I don't get jealous... mmh..."
            scene ch6sc10_756 with dissolve
            ki "I'm the woman who's just made love to you... you're still hard and throbbing between my thighs."
            ki "I know how you feel about me... you're happy right now, with me."
            scene ch6sc10_757 with dissolve
            mc "*Mwah* Exactly... no amount of island women could change how you make me feel... mmhh."
            ki "Your tongue baby... give me your tongue."
            scene ch6sc10_760 with dissolve
            "Kira intimately meet your tongue with hers, she enjoys teasing you with her gently licks."
        else:
            pass

        scene ch6sc10_761 with dissolve
        ki "MMgh… lick me more baby-"

        if pearl_relationship == True:
            scene ch6sc10_762 with dissolve
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            play music forest_1 fadein 1.0
            #stop music fadeout 1.0
            pl "Finally, you’re done fucking!"
            pl "You guys were going at it for a while you know? Kira’s moans could be heard all the way down the hall."
            with vpunch
            ki "*Gasps* Pearl!? G-Get out! This is my reunion!"
            scene ch6sc10_763 with dissolve
            pl "You guys have been fucking for hours… I’m getting lonely… and bored."
            ki "That’s not my problem! As you can see we’re not done!"
            with vpunch
            ki "L-Leave!"
            scene ch6sc10_764 with dissolve
            pl "Nuh-uh! I want some attention as well!"
            pl "You can’t just hide him in here all to yourself, that’s greedy!"
            pl "Hi [mc]..."
            $ twins = True
            mc "*Chuckles* Hey…"
            with vpunch
            ki "You want to get stabbed?! {size=+3}{b}GET OUT!!{/size}{/b}"
            scene ch6sc10_765 with dissolve
            with vpunch
            ki "And you’re calling me greedy?! You’re the one who just spent several weeks with him! {size=+3}{b}SEVERAL WEEKS!{/size}{/b}"
            pl "*Giggles* But he’s so warm and cuddly!"
            mct "*Chuckles* Five hells… she really knows how to get under Kira’s skin… I better let them handle it."
            ki "Yes, he’s warm and cuddly, because he’s in {b}MY{/b} bed, with {size=+3}{b}ME!{/size}{/b}"
            scene ch6sc10_766 with dissolve
            pl "Kira, unclench please… I’m not even naked."
            pl "I’ve missed you lots and lots, but you just run off with [mc], leaving me all on my own."
            scene ch6sc10_767 with dissolve
            ki "I’ve missed you too, greatly so!"
            ki "But do you have to intrude on an intimate moment between [mc] and I?"
            ki "When he came to rescue us, I had one hug with him and then the two of you set off!"
            scene ch6sc10_766 with dissolve
            pl "Kira, it’s not like I spent the last three weeks in bed with him!"
            pl "I’m sure he has told you what we’ve been through, and on top of that any little amount of downtime we had…"
            pl "I literally had to compete with a whole tribe! Fifty or sixty women for his attention!"
            scene ch6sc10_767 with dissolve
            ki "I’d rather compete for his affections than be without him!"
            scene ch6sc10_766 with dissolve
            pl "Okay, shut up and listen."
            pl "I didn’t come here to fight with you or annoy you."
            scene ch6sc10_768 with dissolve
            pl "I came because I missed you, I wanted to see you and [mc] and spend time with the two of you."
            pl "We both love him, more so than we care to admit. And he loves both of us."
            ki "*Nods* …"
            pl "So what is the big deal if we spend some quality time together, either on our own with him or together with him."
            scene ch6sc10_769 with dissolve
            ki "Pearl… I’m sorry."
            ki "I didn’t think about it like that… I guess I was caught up in the moment and I was surprised."
            scene ch6sc10_768 with dissolve
            pl "It’s okay… I really tried to give you guys as long as I could manage… but it’s been a few hours."
            pl "I caught up with Kelly, had a drink with Creed, but after that… I felt lonely without the two of you."
            scene ch6sc10_769 with dissolve
            ki "I’m sorry, I can see why it wasn’t nice to just shut ourselves in privacy like this… but I really craved some intimacy with [mc]."
            scene ch6sc10_768 with dissolve
            pl "Understandable! I would’ve done the same thing. Just please don’t be upset with me for wanting to be near you guys."
            pl "You’re all I have… both of you."
            scene ch6sc10_770 with dissolve
            ki "You’re all I have as well, you and [mc]. I love you."
            scene ch6sc10_768 with dissolve
            pl "*Giggles* Love you too, sis!"
            scene ch6sc10_770 with dissolve
            ki "I know you do. From now on, I’ll try to balance our time together better."
            ki "How about you and I go looking for fishys in the bay tonight?"
            pl "R-Really?! Okay!"
            scene ch6sc10_771 with dissolve
            mc "This is what I like to see, my little pirates getting along."
            mc "I love spending time with both of you, both separately and together."
            "They both giggle happily as they caress you."
            scene ch6sc10_772 with dissolve
            bth "*In unison* We love you!"
            scene ch6sc10_771 with dissolve
            mc "*Chuckles* And I love the two of you."
            scene ch6sc10_772 with dissolve
            pl "I know Diana wants to speak to you, and Kelly is eager to see you as well… but how about we cuddle for a bit? The three of us."
            ki "I believe the others can wait…"
            scene ch6sc10_771 with dissolve
            mc "*Exhales* How can I refuse a cuddle session with my cute little mermaid and my fiery-hot captain."
            scene ch6sc10_772 with dissolve
            bth "*Laughs* You can’t! Nap time!"
            scene black with Dissolve(2.5)
            $ renpy.pause(0.5)
            "And so the three of you doze off for the better part of an hour."

        else:
            scene black with Dissolve(2.5)
            $ renpy.pause(0.5)
            "The two of you continue your make out and cuddle session for close to an hour before it’s time to get out and about."

    else:
        scene ch6sc10_773 with Dissolve(2.5)
        $ renpy.pause(0.5)
        mc "Go find us a table, I’ll grab us some ales."
        ki "*Nods in agreement* Mhm."
        scene ch6sc10_774 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "And with a couple of ales and a table secured, you begin sharing the adventurous tale of what you and Pearl have been through."
        "Kira listening attentively."
        scene black with Dissolve(2.5)
        $ renpy.pause(0.5)


    scene ss43 with Dissolve(2.5)
    $ renpy.pause()
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ch6sc10_775 with Dissolve(2.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    br "Ye think we got enuff fer t’ restoration of t’ courtyard?"
    da "Yeah this should at least cover the basics."
    da "For today we’ll just bring the supplies back to the guild and prepare everything."
    br "Aye… sounds good t’ me."
    scene ch6sc10_776 with dissolve
    da "We’ll start the restoration tomorrow, I’ve asked Flynn and Milton to meet us around noon."
    br "*Chuckles* Heh! Good thinking, ye had me worried yer wanted t’ do it just t’ two of us."
    da "Some manual labor will do those two some good."
    br "Hah! Aye, put some meat on their bones!"
    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    scene ss8 with Dissolve(2.5)
    $ renpy.pause()
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_777 with Dissolve(2.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "Ah, there she is."
    mct "Looks like she’s awaiting the sunset."
    scene ch6sc10_778 with dissolve
    mct "Let’s keep her company for a little while."
    mct "It doesn’t look like I’ll be heading back to Luxenford today, and it would be nice to catch up with her."
    scene ch6sc10_779 with dissolve
    mc "Hey, little one."
    mc "Mind if I join you for a bit?"
    kl "[mc]?? Please! Sit, sit!"
    scene ch6sc10_780 with dissolve
    kl "Will you watch the sunset with me?"
    mc "You bet, little one."
    scene ch6sc10_781 with dissolve
    kl "*Giggles* I like it when you call me that."
    scene ch6sc10_782 with dissolve
    kl "You know…"
    scene ch6sc10_781 with dissolve
    kl "I’m-... I’m happy you’re back."
    scene ch6sc10_782 with dissolve
    kl "And that you-... didn’t get hurt or anything."
    mc "Oh? You’ve been worrying about me?"
    scene ch6sc10_781 with dissolve
    kl "Duh! I mean-... of course I have…"
    scene ch6sc10_782 with dissolve
    kl "I saw your battle with Admiral Diana from below deck… how the two of you passed out in the water."
    scene ch6sc10_781 with dissolve
    kl "And then!-... then I didn’t get to see you again, not until now."
    mc "My bad, little one. I didn’t mean to worry you, everything just happened so fast."

    if kelly_path == True:
        scene ch6sc10_783 with dissolve
        kl "*Giggles* You’re forgiven!"
        mc "You’re too kind, little one."
        "Kelly giggles happily while she plays footsies with you."

    else:
        scene ch6sc10_781

    scene ch6sc10_784 with dissolve
    kl "[mc]! I’m not {b}THAT{/b} little you know? Haven’t you noticed? *Giggles softly*"
    mc "*Chuckles* Trust me, I’ve noticed."
    scene ch6sc10_785 with dissolve
    kl "Good…"
    kl "It’s important for a man to notice the women around him…"
    scene ch6sc10_784 with dissolve
    kl "To compliment them on their… features. *Giggles*"

    if kelly_path == True:
        scene ch6sc10_786 with dissolve
        mc "I wouldn’t dare neglect your… features, Kelly."
        mc "You’re one of the most beautiful women I’ve ever had the pleasure of being around."
        "Kelly giggles softly as you caress her cheeks while holding her."
        mc "You have a gorgeous shapely body that few women of your age can boast to have."
        mc "But more than that, you have incredible brown eyes, that have this innocent look with a hint of naughtiness behind them."
        scene ch6sc10_787 with dissolve
        kl "*Giggles* You really have paid attention to me…"
        kl "I enjoy looking into your eyes as well… I love how blue they are."
        scene ch6sc10_788 with dissolve
        mc "Let’s not forget these soft lips of yours, slightly wet with your saliva…"
        mc "I’ve missed them, the way they feel… the way they taste."
        "You caress her lips with your pinky, and she caresses you back with nibbles."
        scene ch6sc10_789 with dissolve
        "Kelly swiftly crawls into your arms, wrapping herself around you as she begins pressing her soft lips against yours."
        scene ch6sc10_790 with dissolve
        kl "Mmmgh! {b}I’ve missed you so much!{/b} *Mwah* So much! *Mwah*"
        scene ch6sc10_789 with dissolve
        mc "*Kiss* Mmh… I had a feeling this would happen the moment I caressed your lips."
        scene ch6sc10_790 with dissolve
        kl "And yet you caressed them anyways… mmmh… so you wanted me to kiss you… mmh…"
        scene ch6sc10_789 with dissolve
        mc "I won’t deny that… mmh. I’d almost forgotten what a good little kisser you are… so eager."
        scene ch6sc10_790 with dissolve
        kl "Allow me to remind you! *Mwah*"
        scene ch6sc10_791 with dissolve
        kl "*Giggles* Your beard is scruffy! I kind of like it… *Kisses*"
        mc "Mmgh… every kiss is getting me addicted to you Kelly…"
        scene ch6sc10_792 with dissolve
        kl "Then we better keep kissing… mmh… I love feeling your warm hands on my thighs."
        kl "Please… mmh… don’t stop caressing me."
        scene ch6sc10_791 with dissolve
        mc "I have no intention- Nnnh… of letting go."
        scene ch6sc10_792 with dissolve
        kl "I love being in your arms… tasting your lips… mmgh… feeling your touch…"
        scene ch6sc10_793 with dissolve
        kl "Closer… mmgh… I want us to be closer [mc]."
        kl "Hold me tighter… *Sucks lip* mmgh… feel my body-"
        scene ch6sc10_794 with dissolve
        with vpunch
        kl "*Squeals* {b}Aiiyh!!{/b}"
        "As Kelly attempts to pull you closer, the two of you lose balance and tumble into the water."
        scene ch6sc10_795 with dissolve
        with vpunch
        kl "*Gasps* {b}[mc]!!{/b}"
        mc "Don’t worry, I’ve got you."
        scene ch6sc10_796 with dissolve
        kl "Gosh… thank you for not letting go during the fall."
        kl "I suppose we got a little carried away…"
        scene ch6sc10_797 with dissolve
        mc "Yeah, I guess we did… happens when the attraction between two people is this strong."
        "Standing completely soaked before you, Kelly smiles warmly, as if totally unbothered by the accident."
        scene ch6sc10_796 with dissolve
        kl "At least this means that I’m not the only one… who’s wet now. *Giggles*"
        kl "And I fully agree… our attraction is unmatched, so I have an idea."
        scene ch6sc10_798 with dissolve
        kl "How about we toss our wet clothes up on the docks to dry… while-..."
        kl "While you fuck me right here? Below the dock."
        mc "*Chuckles* I say let’s have a proper reunion."
        kl "*Giggles* I had a feeling you would like my idea…"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_799 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        kl "Nobody is out at this hour, everyone is having meals and ales at the tavern."
        kl "I want you to make me moan, [mc]. Make me moan so loudly that all the fish in the bay hears my pleasure."
        scene ch6sc10_800 with dissolve
        kl "*Whispers* {size=-7}{b}Fuck me like I’m the only woman in the world.{/b}{/size}"
        kl "*Whispers* {size=-7}{b}Fuck me like only the man I love can. Fuck me right here in the sea like a mermaid.{/b}{/size}"
        mc "Have you been practicing with your fingers like I told you about?"
        scene ch6sc10_801 with dissolve
        kl "*Giggles* Every. Single. Night. I’ve kept myself ready for this moment."
        mc "That’s my girl, I won’t hold back today then."
        kl "Mmmh… you’re poking me with your big cock… stop being a meanie and fuck me with it already."
        scene ch6sc10_802 with dissolve
        with vpunch
        kl "*Moans* {b}AhhHh! Yes!!{/b}"
        "You swiftly bring her to one of the beams of the dock, your cock needs neither of your hands to find her slippery entrance."
        kl "*Moans softly* I feel you… I’m ready-Aahh… make me yours, {b}[mc]!{/b}"
        scene kl_lewd3 with dissolve
        $ renpy.pause()
        with vpunch
        kl "I already belong to you- {b}Ahhh!{/b} But I love being claimed again! {b}AiiiyhH!!{/b}"
        with vpunch
        mc "MMgh… fuck… you’re cumming already? {b}MMmh!{/b} Damn that makes you tight- Aahh…"
        kl "{b}Ahh-NNhh!{/b} S-Sorry! I’ve been waiting for you to fuck me for months- Ahhh! My body needed your {b}big cock to orgasm!{/b}"
        scene kl_lewd4 with dissolve
        $ renpy.pause()
        with vpunch
        mc "Hnngh! Fuck I’ve missed this little wet pussy of yours Kelly- Mmh!"
        with vpunch
        kl "And I’ve missed your big hard cock- {b}Aiiyhh!{/b} I can’t get enough of it! You’re deeper than last time- {b}AHH!{/b}"
        with vpunch
        kl "{b}Fuck me [mc]!! My body is yours!{/b} I’m the only woman in the world right now- Aiiiyh! And I need your warm cum inside of me!"
        with vpunch
        mc "{b}Fuck! Mmmgh! I’m going to- Ahhh!{/b}"
        with vpunch
        kl "{b}Yes! Mmmgh!! Fill me up! Aiiiyhh! You’re going to make me cum again!!!{/b}"
        scene ch6sc10_803 with dissolve
        with vpunch
        "The two of you fill the bay with moans as you reach an intense orgasm together."
        with vpunch
        kl "{b}*Moans loudly* AiiiyHhhH! YES!! YES!! I FEEL YOU!!{/b}"
        mc "Fuck Kelly! Mmmh… this is what I call a reunion… mmh!"
        kl "*Moans and giggles* I-I can’t believe you’re so deep!! Mmmh! This is my new favorite position!"
        scene ch6sc10_804 with dissolve
        with vpunch
        kl "{b}Kiss me! MMmgh!{/b}"
        "Kelly eagerly wraps herself tightly around you, rubbing her naked body against yours with you still inside her as she begins kissing you."
        kl "I love you! I love your cock! I love being fucked by you! Mmmgh! I love being touched by you!"
        mc "I love you too, little one."
        mc "You have a way of making me think of nothing else but being in the moment with you."
        kl "*Sucks lips* Mmmh… that’s what I want! When we’re together it’s just the two of us! *Kiss*"
        mc "Mmh… c’mon, let’s get dressed before everyone finishes dinner."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        scene ch6sc10_780 with Dissolve(1.5)
        play music relax_2 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        kl "*Giggles* So… how do you rate our reunion?"
        mc "Rate our reunion?"
        kl "Yes! On a scale from one to ten?"
        scene ch6sc10_781 with dissolve
        mc "You’re ridiculous…"
        scene ch6sc10_782 with dissolve
        kl "C’mon! Indulge me! *Giggles*"
        scene ch6sc10_781 with dissolve
        kl "Pleeease?"
        mc "*Sighs* Alright, alright…"
        scene ch6sc10_782 with dissolve
        mc "I guess I would rate it at an eight."
        scene ch6sc10_781 with dissolve
        kl "Huuuh? I was rating it at a ten out of ten!"
        kl "Why only eight? Did you not… like what we just did?"
        scene ch6sc10_782 with dissolve
        mc "Kelly… don’t even start thinking like that… I’ve enjoyed every second since I sat down with you."
        mc "And what we just did below the dock… cherry on top. I loved it."
        scene ch6sc10_781 with dissolve
        kl "Then why-"
        mc "More… I want more of it. And we don’t have time to enjoy each other fully today."
        scene ch6sc10_782 with dissolve
        kl "O-Oh! I see!"
        scene ch6sc10_783 with dissolve
        kl "You liked being with me so much that you’re disappointed we can’t do it as long as we want?"
        kl "That’s really sweet! *Giggles* Now I understand why it’s only an eight! I agree! No, a seven even!"
        mc "Definitely a seven. *Chuckles*"
        kl "I hope I can convince Pearl and Kira to swing by Luxenford more often, I’m sure they would love to visit you as well."
        scene ch6sc10_782 with dissolve
        kl "Then I could visit mother as well! And…"
        scene ch6sc10_783 with dissolve
        kl "And I could spend more time with you."
        mc "I’d like that."
        scene ch6sc10_782 with dissolve
        kl "Hey [mc]... Brenda, an old friend of Kira and Pearl mentioned she had been working with my father."
        scene ch6sc10_781 with dissolve
        kl "But she says he went rogue after Diana attacked Looter’s Bay."
        scene ch6sc10_782 with dissolve
        kl "And I know he’s been hellbent on bringing me back and believes you have kidnapped me."
        scene ch6sc10_781 with dissolve
        kl "So I was just wondering… have you… seen him at all?"
        mct "I knew I wouldn’t be able to avoid this question for long… he is her father after all, even if he’s a prick."

    else:
        scene ch6sc10_780 with dissolve
        mc "*Chuckles* With the amount of women I’ve come to have in my life, it can be hard to give the proper attention to each one."
        mc "Even though they deserve it."
        kl "I’m just glad I get to count myself as one of the women in your life."
        scene ch6sc10_781 with dissolve
        kl "Even if it is just as friends, I want you to be part of your life."
        scene ch6sc10_782 with dissolve
        mc "You are, little one. "
        "The two of you sit together for a few minutes gazing upon the setting sun in silence before Kelly speaks."
        kl "Hey [mc]... Brenda, an old friend of Kira and Pearl mentioned she had been working with my father."
        scene ch6sc10_781 with dissolve
        kl "But she says he went rogue after Diana attacked Looter’s Bay."
        scene ch6sc10_782 with dissolve
        kl "And I know he’s been hellbent on bringing me back and believes you have kidnapped me."
        scene ch6sc10_781 with dissolve
        kl "So I was just wondering… have you… seen him at all?"
        mct "I knew I wouldn’t be able to avoid this question for long… he is her father after all, even if he’s a prick."

    scene ch6sc10_781
    if ed_alive == False:
        mc "Yeah, he somehow tracked me and Pearl to Aruna island."
        mc "And he managed to get himself caught by the A’nai tribe after setting a fire in their village."
        scene ch6sc10_782 with dissolve
        kl "Ugh! Why does he do such extreme things?! Nobody was hurt, right?"
        mc "No, nobody was hurt, luckily."
        mc "After I became the A’khan, he was brought before me to be sentenced."
        scene ch6sc10_781 with dissolve
        kl "Oh! And what… did you decide?"
        mc "He’s dead Kelly."
        mc "I sentenced him to death for his actions."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        "Kelly remains silent. You can tell her heart is pounding rapidly."
        scene ch6sc10_805 with dissolve
        play music sad_1 fadein 1.0
        #stop music fadeout 1.0
        kl "..."
        mc "Kelly…"
        scene ch6sc10_806 with dissolve
        $ kelly_relationship = False
        mc "I know it’s not what you hoped to hear, I made the choice not just for his transgressions at A’nai…"
        mc "But for everything he has done, and would have continued to do-"
        scene ch6sc10_807 with dissolve
        with vpunch
        kl "{b}*Screams and sobs* B-Bastard!! *Smack* {size=+10}You executed my father!{/b}{/size}"
        kl "I can’t even look at you! *Sobs* {size=+3}{b}You’re just like all other men!{/b}{/size}"
        $ kelly_path = False
        scene ch6sc10_808 with dissolve
        with vpunch
        kl "*Sobs* {b}Don’t ever speak to me again! {size=+10}I HATE YOU!!{/b}{/size}"
        "Kelly leaves you at the dock, her trust and faith in you clearly broken."
        "Kelly’s trust has decreased by {size=+7}{b}{color=#f00}15{/color}{/b}{/size}."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc10_809 with Dissolve(1.5)
        play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        mct "That went just about as well as I expected it would…"
        $ kelly_trust -= 15
        mct "When I sentenced her father to death, I knew she wouldn’t take it well."
        mct "Whether or not she will come to understand, is up to her. I will give her time to come to terms with it."
        mct "But she likely won’t ever forgive it, as I would never forgive Taron. Even if the situations are vastly different."
        mct "Lord Edward was her father at the end of the day."
        scene ch6sc10_810 with Dissolve(1.5)
        mct "*Exhales* It’s time to go meet Diana…"
        mct "Hopefully that reunion will have a better ending."

    else:
        mc "Yeah, he somehow tracked me and Pearl to Aruna island."
        mc "And he managed to get himself caught by the A’nai tribe after setting a fire in their village."
        scene ch6sc10_782 with dissolve
        kl "Ugh! Why does he do such extreme things?! Nobody was hurt, right?"
        mc "No, nobody was hurt, luckily."
        mc "After I became the A’khan, he was brought before me to be sentenced."
        scene ch6sc10_781 with dissolve
        kl "Oh! And what… did you decide?"
        mc "I’ve sentenced him to prison in A’nai. At least for the time being until I decide what to do with him."
        scene ch6sc10_782 with dissolve
        kl "Good… I think father could use a timeout."
        scene ch6sc10_781 with dissolve
        kl "His actions not only hurt my mother and me, but he put others in harm's way in his false pursuit of bringing me home."
        scene ch6sc10_782 with dissolve
        kl "I trust your judgement."
        $ kelly_trust += 3
        "Kelly is happy with your decision to keep her father locked away, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
        mc "Thank you, little one. I’m glad you understand."
        "You and Kelly sit together for the better part of half an hour watching the sunset before it’s time to go meet Diana."

    scene black with Dissolve(2.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ch6sc10_811 with Dissolve(2.5)
    $ renpy.pause(0.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    dit "Should I go find him?"
    dit "I’m just sitting here doing paperwork while… everyone else gets to enjoy his company."
    scene ch6sc10_812 with dissolve
    dit "Ugh! Enjoy his company? What am I even saying…"
    dit "Focus! I have work to do."
    scene ch6sc10_811 with dissolve
    dit "..."
    dit "I even did my hair tonight… hoping he’d notice."
    scene ch6sc10_812 with dissolve
    dit "No, no… no, I didn’t do it for him."
    dit "That would be ridiculous… we’ve only spoken a few times."
    scene ch6sc10_812 with dissolve
    with vpunch
    dit "*Exhales* I don’t care about his opinion! Ugh!"
    dit "Stop caring about some man you barely know and get to work Diana! Hnnghh!"
    scene ch6sc10_815 with dissolve
    di "He’s not even going to notice my hair or bother complimenting it! "
    scene ch6sc10_814 with dissolve
    mc "I like what you did with your hair."
    scene ch6sc10_813 with dissolve
    with vpunch
    di "{b}[mc]!!!!!{/b}"
    di "*Gasps* H-How long have you been standing there?!"
    mc "Long enough to appreciate your hair. *Chuckles*"
    di "......"
    scene ch6sc10_815 with dissolve
    di "Not funny!"
    di "I-... I didn’t do it for you or anything…"
    ####Choice####
    menu:
        "Flirt with Diana.":
            scene ch6sc10_814 with dissolve
            mc "I’m not being funny, well… maybe a bit."
            mc "But I don’t hand out compliments to any beautiful woman I come across for the sake of it."
            scene ch6sc10_815 with dissolve
            di "B-Beautiful? You-... you think I’m beautiful?"
            scene ch6sc10_814 with dissolve
            mc "Mhm, I do. And your hair done like this only enhances your beauty."
            scene ch6sc10_816 with dissolve
            di "Oh… [mc]-... I-I, hnnh… thank you."
            di "I’m glad you like it."
            mct "Is she… blushing?"
            $ di_trust += 3
            "Diana is happy that you took notice of her hair, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch6sc10_815 with dissolve
            di "S-Stop looking at me!"
            di "A-Anyways…"

        "Don’t Flirt.":
            scene ch6sc10_814 with dissolve
            mc "Good, then my opinion on the matter doesn't hold any weight."
            scene ch6sc10_815 with dissolve
            di "Yeah… right. *Clears throat* Anyways…"

    scene ch6sc10_817 with dissolve
    di "I wasn’t sure you’d find the time to stop by tonight, but I’m glad you did."
    di "Ambassador Orianna has already given me a rundown of what has happened, at least from her perspective."
    scene ch6sc10_818 with dissolve
    di "But I would like to hear your side of everything, if you would be willing to share it?"
    di "It’s not that I don’t believe Orianna’s report, but she is a politician… she could have left things out or embellished some parts."
    scene ch6sc10_819 with dissolve
    di "But you…"
    di "At least from our clash on the water and our limited interactions thus far…"
    scene ch6sc10_818 with dissolve
    di "You’re honest… I trust you will tell me everything just as it happened."
    di "[mc], will you?"
    mc "Sure. I’ll start from the beginning."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "And so you begin recounting the events of the last three weeks. You leave out interpersonal relations but stick to the truth."
    scene ch6sc02_242 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_486 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_565 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_594 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_606 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_616 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc02_1203 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc03_121 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc03_146 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc03_328 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc05_027 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_130 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_172 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_180 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_252 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_322 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_343 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_401 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_412 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_719 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc06_805 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc07_224 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_007 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_025 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_054 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_082 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_120 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_219 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_251 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_288 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_400 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_407 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_416 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc08_537 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_041 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_101 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_112 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_158 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_177 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_201 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_203 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_222 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_311 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc09_349 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_018 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_045 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_242 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_263 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_434 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_446 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_612 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_701 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_820 with Dissolve(2.5)
    $ renpy.pause(0.5)
    "Diana remains silent for a few minutes, as if trying to fathom all that you’ve just been through."
    scene ch6sc10_819 with dissolve
    di "Thank you… it is clear that Orianna has mostly told the truth with a few embellishments as I expected."
    di "I value your honesty [mc]... now."
    scene ch6sc10_821 with dissolve
    "Diana proceeds to get up and begins walking around the desk, towards you."
    mc "Now?"
    scene ch6sc10_822 with dissolve
    "You feel her soft delicate touch strafe your hand as well as your cheek, and her scent of vanilla essence surrounds you."
    di "[mc]... I’m so sorry."
    di "Seeing your parents like that… used as a trick to deceive you… I’m sorry you had to endure that."
    scene ch6sc10_823 with dissolve
    "Suddenly she embraces you, hugging you tightly. It’s clear that her emotions are elevated."
    mc "Hey… it’s okay. I’m fine, really…"
    mct "Of everything I just told her, the thing with my parents is what she focuses on?"
    mct "She cares about me? Mhm, she does. Her body is trembling and she’s hugging me as if it’s the most important thing in the world."
    scene ch6sc10_824 with dissolve
    di "[mc]... I’m sorry."
    mc "Diana… you haven’t done anything to be sorry about."
    "You feel her embrace tighten."
    di "You forget… I too know the feeling of losing a parent… the feeling of being orphans."
    mct "Right, of course. No wonder she feels this strongly about what I told her I encountered."
    scene ch6sc10_823 with dissolve
    mc "Yeah… I guess we’re bound by our childhood trauma."
    di "It seems to be a strong binding agent…"
    scene ch6sc10_822 with dissolve
    di "[mc], I’m glad we have this in common… I know it’s a horrible thing we’ve had to endure."
    di "But-... this… it makes it less horrible somehow?"
    "You nod in agreement, Diana has a point that you can understand, finding something good in something horrible…"
    scene ch6sc10_823 with dissolve
    "It can help ease the pain that you must endure for the rest of your life."
    di "Sorry… I just need one more."
    mc "Take as long as you need."
    scene ch6sc10_824 with dissolve
    di "[mc]..."
    di "Thank you."
    di "I-..."
    scene ch6sc10_825 with dissolve
    "Diana releases you from her embrace, realizing she was about to reveal something she wasn’t ready for."
    di "*Clears throat* Ahem… this… this doesn’t leave this room, got it?"
    mc "*Chuckles* From hot to cold? Frosty."
    scene ch6sc10_826 with dissolve
    di "Really? Ice jokes?"
    di "Let’s continue our discussion. We still have a matter to settle."
    scene ch6sc10_827 with dissolve
    di "I expect you remember our deal?"
    scene ch6sc10_828 with dissolve
    mc "Mhm, I do."
    mc "You want access to Captain Blackheart."
    scene ch6sc10_827 with dissolve
    di "I believe you said the only means of accessing him is by an artifact that you have at your guild in Luxenford?"
    di "Correct?"
    scene ch6sc10_828 with dissolve
    mc "Yeah, it’s being kept safe and locked away at the guild. It’s even being concealed with magic."
    mc "You’re going to kill him, aren’t you?"
    scene ch6sc10_829 with dissolve
    di "Not that it’s any of your business, yes… I’m going to kill that vile bastard."
    di "I’m sure you would do the same if faced with that man you told me about? Taron?"
    scene ch6sc10_828 with dissolve
    mc "I would."
    scene ch6sc10_827 with dissolve
    di "Then you know what will happen if anyone tries to stop me from avenging my father."
    scene ch6sc10_828 with dissolve
    mc "I’m not going to stand in your way, Kira and Pearl has already told me they couldn’t care less if he lives or dies."
    mc "And I certainly won’t play morality police on other peoples vengeance when I am seeking my own."
    scene ch6sc10_829 with dissolve
    di "Thank you…"
    di "I don’t know what I expected, but I’m glad you once again understand me."
    scene ch6sc10_827 with dissolve
    di "Kira and the rest of her crew will be pardoned by royal decree, by me."
    scene ch6sc10_828 with dissolve
    mc "You can do that?"
    scene ch6sc10_827 with dissolve
    di "Mhm, I can."
    di "As Lord Admiral, the seas of Luxeron fall under my jurisdiction."
    scene ch6sc10_830 with dissolve
    di "I will be leaving for Luxenford at first light."
    di "I will meet you at your guild to collect what is owed to me."
    di "As for Looter’s Bay, it’s now a registered trading hub of the Cerulean sea, under the kingdom of Luxeron."
    scene ch6sc10_827 with dissolve
    di "I have spent the last three weeks setting up trade-route connections and finalizing the paperwork."
    di "I will leave it up to you to appoint an emissary of Looter’s Bay, who will oversee that everything stays in order."
    scene ch6sc10_828 with dissolve
    mc "You want me to make that decision?"
    scene ch6sc10_830 with dissolve
    di "I do… I trust your judgement."
    ###Skill-check###
    if leadership >= 20:
        di "You have shown remarkable leadership qualities."
        di "From what you've told me of the island, what Orianna has informed me and..."
        di "With how you and I met, you stood your ground for what you believed in, to defend your friends."
        $ di_trust += 2
        "Diana has grown to respect you, she views you as a genuine leader, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
    else:
        pass

    di "In fact, I hereby grant you official {b}Lordship of Looter’s Bay{/b}."
    scene ch6sc10_831 with dissolve
    mc "{b}What?!{/b} You can’t be serious-"
    di "I’ve already written it in this scroll right here and sent a copy of it to King Bennen."
    di "I know you’re an adventurer and won’t be tying yourself down here, it is more of a formality."
    scene ch6sc10_829 with dissolve
    di "But this means, you are the Lord and owner of Looter’s Bay."
    scene ch6sc10_827 with dissolve
    di "Which is why you should appoint someone capable as to oversee the day to day operations whilst you’re away."
    di "After all, you could make a great deal of coin if the bay prospers."
    scene ch6sc10_828 with dissolve
    mc "Diana… I don’t know what to say."
    scene ch6sc10_830 with dissolve
    di "You don’t have to say anything, just think about who you want to oversee and handle the logistics of Looter’s Bay."
    di "While you continue on with your life, but with an actual noble title and the paperwork to back it up."
    scene ch6sc10_828 with dissolve
    mct "Becoming nobility from peasant roots is incredibly rare… she makes a good point, this could be incredibly useful to have in my arsenal."
    mct "And she’s right, if I appoint someone capable to run it all, it’ll mostly be hands off for me while I reap the benefits."
    mc "Very well, I accept the Lordship you wish to grant me."
    scene ch6sc10_831 with dissolve
    di "Great! Here, take it."
    di "Bennen will have his copy stored in the royal archives should you lose this one. But do try to keep it safe."
    scene ch6sc10_832 with dissolve
    di "Now, with that out of the way…"
    di "I believe you have a great deal to think about, and I would like to get some rest."
    di "I’ll see you at the guild in a few days."
    scene ch6sc10_833 with dissolve
    mc "I’ll see you in a few days. And Diana?"
    scene ch6sc10_832 with dissolve
    di "Mhm? What is it [mc]?"
    scene ch6sc10_833 with dissolve
    mc "Thank you, I’m aware Lordship isn’t something that is being freely granted to just anyone."
    mc "It involves a bunch of paperwork and logistics, and you’ve undoubtedly put your name on the line in support of it."
    scene ch6sc10_832 with dissolve
    di "You have proven yourself by bringing back Ambassador Orianna safely and upholding your end of our deal."
    di "But you are right, I did have to put my name on the line in support of elevating a commoner to Lordship."
    scene ch6sc10_834 with dissolve
    di "Just… don’t change, okay?"
    di "I’ve met so many noble lords and they all rub me the wrong way… thinking they are better than everyone."
    di "And… I-... *Quietly* {size=-10}{b}I like you just the way you are.{/b}{/size}"
    scene ch6sc10_832 with dissolve
    di "What I’m saying is… please just remain honest and true to yourself."
    di "If you do that, then I am happy that I have put my name on the line for you."
    scene ch6sc10_833 with dissolve
    mc "I will do my best to honor your name. I appreciate you doing this for me."
    "Diana nods gently, she is happy that you understand what it took for her to do this."
    scene ch6sc10_834 with dissolve
    di "Now, go… I-... I don’t think I have the strength to ask you to leave a 3rd time."
    mct "*Chuckles* She clearly enjoys spending time together, but she’s right, this isn’t the time to get to know each other."
    scene ch6sc10_833 with dissolve
    mc "I’ll take my leave then, goodnight Diana."
    scene ch6sc10_832 with dissolve
    di "Goodnight, [mc]..."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)

    if harem_path == True:
        scene ch6sc10_812 with Dissolve(1.5)
        dit "*Exhales deeply* Hnnhh..."
        dit "He managed to win the affections of an entire island worth of hardened women?"
        dit "Women known as hostile towards outsiders? Men especially?"
        scene ch6sc10_811 with Dissolve(1)
        dit "He is quite remarkable... even I can't deny that."
        dit "He's achieved so much in such a short time... becoming this 'A'khan' ..."
        dit "He now has more than 70 beautiful women all eager for his attention."
        scene ch6sc10_812 with Dissolve(1)
        dit "*Exhales deeply* Hnnhh... why... why does this get me hot and bothered!?"
        dit "Am I jealous!? Is it the fact that he is man enough to command that amount of respect from women?"
        dit "I need a bath, a cold bath! I need him out of my mind! Hnngh... [mc]..."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)

    else:
        pass

    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    "With time not being on your side, you head for the docks to think about the decision that lies ahead."
    scene ch6sc10_835 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music mmm_elven_forest fadein 1.0
    #stop music fadeout 1.0
    mc "*Exhales* Lord of Looter’s Bay…"
    mc "King of A’nai…"
    mc "All in a matter of three weeks."
    mc "Dalen is going to lose his shit when he hears about all of this. *Chuckles*"
    scene ch6sc10_836 with dissolve
    mc "If he doesn’t promote me straight to S:Rank, I don’t know what will."
    mc "Granted I think Eliza and I are still just C:Rank or was it B:Rank? I haven’t paid it much attention."
    mc "She could even have earned a higher rank for herself while I’ve been away, although she didn’t mention it last we spoke."
    mc "And knowing her, she wouldn’t have been able to keep quiet about a promotion. *Chuckles*"
    scene ch6sc10_837 with dissolve
    mc "*Sighs* I can’t wait to see her tomorrow… I’ll set off first thing in the morning."
    mc "If I run at full-speed it should take between 3-4 hours at most. Diana’s ships are enchanted to be faster than average ships."
    mc "She will probably take roughly 2-3 days to reach Luxenford, whereas with Kira and Pearl’s ship it took about 7 days."
    mc "I have to appoint someone capable and trustworthy to rule Looter’s Bay in my name… easier said than done."
    scene ch6sc10_835 with dissolve
    mc "It’s not like I have great connections here or know the inner workings of seafaring operations."
    mc "I initially thought of Kira, she was the more hands-on leader and captain when I first met her."
    mc "Whereas Pearl was more laid back and nonchalant about being captain, but she knows just as much as Kira."
    mc "Then again, they have expressed a desire to travel the Cerulean seas and follow their own way."
    scene ch6sc10_836 with dissolve
    mc "If I appoint either of them they will be forced to remain here in Looter’s Bay."
    mc "Then there’s Kelly… she’s much too young and soft for a leadership position."
    mc "She still has much to learn while being a steward under Kira and Pearl."
    scene ch6sc10_837 with dissolve
    mc "Creed… hmm, the guy who runs the tavern here in the bay?"
    mc "I believe the twins told me they had him in mind to run the place in their place when they opposed Brenda."
    mc "But I don’t really know the guy… and he eats baby chickens."
    scene ch6sc10_835 with dissolve
    mc "*Sighs* Then again, I enjoy a good omelet… so I can’t really judge the guy on that."
    mc "If they believed he was capable and could be trusted to lead Looter’s Bay on their behalf…"
    mc "Shouldn’t I be able to as well? Especially if I have them supporting me in the matter."
    scene ch6sc10_836 with dissolve
    mc "As the tavern-keeper he would already have all the connections in place and know the place better than anyone."
    mc "Not to mention he would know something about running a business, even if this is on a bigger scale."
    mc "Diana had a good point, if this place gets up and running it could be quite lucrative."
    scene ch6sc10_835 with dissolve
    mc "Sure a great sum of it will go to King Bennen as it’s his kingdom, but a pretty amount should still line my pockets."
    mc "And given what I want to build with Eliza, we will need every coin we can get our hands on."
    scene ch6sc10_836 with dissolve
    mc "With this Lordship, our land outside of Luxenford will also be much better protected, politically."
    mc "If we were just a couple of commoners owning land, we could easily be evicted with no ramifications."
    scene ch6sc10_837 with dissolve
    mc "But as a Lord, the land is protected by a bunch of laws I don’t know too much about."
    mc "Only that it would be a logistic and political nightmare should anyone try."
    mc "*Chuckles* Not to mention, Eliza will slay anyone who even thinks about taking this away from us."
    scene ch6sc10_838 with dissolve
    "You feel a delicate touch as fingers gently run through your hair."
    ki "Hi… you look lost in thought?"
    mc "Mmh… Kira? Just a bit."
    scene ch6sc10_839 with dissolve
    "She proceeds to sit down next to you, just looking up at the sky in silence."
    scene ch6sc10_840 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_839 with dissolve
    $ renpy.pause(1)
    scene ch6sc10_840 with dissolve
    $ renpy.pause(1)
    "She clearly finds comfort in just being beside you."
    scene ch6sc10_841 with dissolve
    ki "I can see why you and Pearl enjoy stargazing so much."
    ki "It’s not just beautiful… but you can really get lost in the great sea of stars out there."
    scene ch6sc10_842 with dissolve
    mc "Yeah… it calms my mind."
    mc "I sometimes think about what could be out there… all those lights? They have to have meaning?"
    scene ch6sc10_841 with dissolve
    ki "Maybe a god put them there for us to look at and enjoy?"
    ki "Or maybe each light out there is the soul of a person?"
    scene ch6sc10_842 with dissolve
    mc "Mmh, could be…"
    mc "For now we’ll have to keep guessing, but one day…"
    scene ch6sc10_841 with dissolve
    ki "One day you will discover it."
    scene ch6sc10_843 with dissolve
    mc "How did you-"
    scene ch6sc10_844 with dissolve
    ki "You have that look in your eyes…"
    scene ch6sc10_843 with dissolve
    mc "I have a look?"
    scene ch6sc10_844 with dissolve
    ki "Mhm! A look of wonder, when you’re curious about something."
    ki "And when you put your mind to something, I know you will accomplish it."
    scene ch6sc10_841 with dissolve
    ki "So yes, I believe one day… you will discover the meaning of the stars."
    scene ch6sc10_842 with dissolve
    mc "*Chuckles* I appreciate the vote of confidence."
    scene ch6sc10_840 with dissolve
    ki "..."
    scene ch6sc10_842 with dissolve
    mc "Kira? Can I ask you something?"
    "Kira nods gently."
    mc "I’ve got a decision to make, about the fate of Looter’s Bay."
    scene ch6sc10_846 with dissolve
    ki "Your meeting with Diana brought this on?"
    scene ch6sc10_845 with dissolve
    mc "Mhm, it did."
    mc "She has granted me Lordship, over Looter’s Bay… in the name of King Bennen."
    scene ch6sc10_847 with dissolve
    with vpunch
    ki "*Startled* {b}She did what?!{/b}"
    ki "S-She gave you Looter’s Bay?! Just like that?!"
    ki "She’s been working night and day for weeks on end to get this place up and running under the new laws!"
    scene ch6sc10_848 with dissolve
    mc "Are you opposed to it? I know it’s your home…"
    mct "Uh-oh… I know that look."
    scene ch6sc10_850 with dissolve
    ki "How can you even think that I would be opposed to this?!"
    ki "First of all, you’re much more important to me than some place I grew up in…"
    ki "Secondly, Looter’s Bay is not my home, {b}The Bloody Banshee{/b} is."
    scene ch6sc10_848 with dissolve
    mc "I get it, I get it… sorry for thinking you’d dislike it. I know you want what’s best for me."
    scene ch6sc10_850 with dissolve
    ki "And you better remember it, or {b}I’ll stab you!{/b}"
    ki "I was just surprised at the news… how could I not be?"
    scene ch6sc10_848 with dissolve
    mc "Trust me, I was taken aback as well… Lordship isn’t granted freely to just anyone."
    scene ch6sc10_849 with dissolve
    "Kira smiles."
    scene ch6sc10_851 with dissolve
    ki "She likes you."
    scene ch6sc10_849 with dissolve
    mc "What? C’mon… be serious."
    scene ch6sc10_851 with dissolve
    ki "Oh I am. She has granted a commoner of questionable origin nobility?"
    ki "That means if you fuck up… her neck and reputation is on the line."
    ki "She likes you."
    scene ch6sc10_849 with dissolve
    mc "You have a point… *Sighs*"
    scene ch6sc10_851 with dissolve
    ki "It’s not hard to fathom as to why she would, she clearly feels she can trust you and has seen what kind of man you are."
    ki "As have we all."
    scene ch6sc10_852 with dissolve
    ####Skill-check###
    if leadership >= 20:
        ki "I believe Looter’s Bay will do well under your Lordship. You have great leadership qualities."
        ki "You’re composed under pressure, you’re straightforward, you aren’t afraid to speak your mind."
        ki "You inspire loyalty in those around you and make it easy to follow your lead."
    else:
        pass

    scene ch6sc10_851 with dissolve
    ki "I’m glad she has chosen you and not some prim and proper noble from the city."
    scene ch6sc10_849 with dissolve
    mc "Yeah, I imagine that wouldn’t sit well with most of the population here."
    scene ch6sc10_851 with dissolve
    ki "So, what did you want my opinion on?"
    scene ch6sc10_849 with dissolve
    mc "Oh, right. As you’re well aware I won’t be settling down here in Looter’s Bay…"
    mc "Diana suggested I appoint someone capable to run Looter’s Bay in my place."
    scene ch6sc10_852 with dissolve
    ki "Yeah… that makes a lot of sense."
    ki "Who do you have in mind?"
    scene ch6sc10_853 with dissolve
    mc "That’s what I was debating with myself before you arrived… I sort of landed on possibly Creed? The tavern-keeper."
    mc "I know you and Pearl want to explore more of the Cerulean seas now that you are free from your father."
    scene ch6sc10_852 with dissolve
    ki "I’m glad you suggested Creed on your own, you have been paying attention then."
    ki "He was our choice as well, he can be a little stubborn and set in his ways… but he is more than capable."
    scene ch6sc10_853 with dissolve
    mc "The remaining question is… can I trust him?"
    mc "He won’t revert to the old ways of piracy while I’m away?"
    scene ch6sc10_852 with dissolve
    ki "He won’t…"
    ki "Creed was never a pirate. He was a smuggler before he set up shop as tavern-keeper."
    scene ch6sc10_851 with dissolve
    ki "He doesn’t care about looting and pillaging or the pirate life, his only concern is that the money flows."
    ki "Diana has already laid the groundwork, he simply has to take the reins and keep to the new rules."
    scene ch6sc10_841 with dissolve
    ki "And if he doesn’t… Pearl and I will be checking in every so often to keep him in check."
    ki "If things aren’t in order, he’ll get an ass whooping or two."
    scene ch6sc10_842 with dissolve
    mc "*Chuckles* A couple of pretty enforcers making sure my holdings are in order?"
    scene ch6sc10_841 with dissolve
    ki "Smart choice to add pretty in there… given that you aren’t paying us. *Snickers*"
    scene ch6sc10_842 with dissolve
    mc "I know my audience. *Chuckles*"
    scene ch6sc10_853 with dissolve
    ki "*Giggles*..."
    scene ch6sc10_852 with dissolve
    ki "It’s almost midnight…"
    ki "I’m probably going to go find Pearl, she wanted to chat a bit before we go to sleep."
    scene ch6sc10_853 with dissolve
    mc "Sure thing, Red. I’m just going to stay a bit longer before turning in."
    scene ch6sc10_841 with dissolve
    ki "Don’t stay too long… I know you’ll want to rush home tomorrow."
    ki "You should be well rested for the journey."
    scene ch6sc10_838 with dissolve
    ki "Goodnight, [mc]."
    mc "Goodnight, Kira… this was nice."
    ki "Yes… I quite enjoyed stargazing with you. I can see why Pearl likes it so much, night night."
    scene ch6sc10_837 with dissolve
    mc "*Sighs* I guess that settles it. I will have Creed run the day to day operations here in Looter’s Bay."
    mc "It brings me some peace of mind knowing that Kira and Pearl will be checking in when they are in the area."
    scene ch6sc10_835 with dissolve
    mc "Time to find a bed and crash for the night…"
    mc "I guess I might as well talk to Creed as I grab a room at the tavern."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "You speak to Creed about the logistics of everything while you order a room for the night."
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc10_854 with Dissolve(2.5)
    $ renpy.pause(0.5)
    mct "I’ve been looking forward to this all day."
    mct "*Chuckles* I’m actually excited? Just the thought of seeing everyone back home again."
    mct "That wouldn’t have been me six months ago…"
    scene ch6sc10_855 with dissolve
    mct "I guess the people around you really can affect your perspective on things."
    mct "It took like an hour to discuss everything with Creed, but when I mentioned that Kira and Pearl were backing me-"
    mct "-He was fully onboard, I guess they had laid the initial groundwork with convincing him."
    mct "And Pearl did mention that they saved him from being tortured, he probably feels like he owes them."
    mct "Either way, having him as my operations manager here in Looter’s Bay, will make everything much smoother."
    mct "*Chuckles* I can already picture Eliza’s expression when she hears that I became King of A’nai and was granted Lordship as well."
    mct "Knowing her she will burst with excitement… I’ll have to tell her when we’re alone. I don’t want the world to know about A’nai."
    mct "Maybe someday… maybe."
    mct "*Exhales deeply* For now… rest."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss33 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_856 with Dissolve(2.5)
    play music mystery_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    bd "*Quietly* {b}{size=-10}Tsk… is this their way of treating you?{/size}{/b}"
    bd "*Quietly* {b}{size=-10}Typical.{/size}{/b}"
    scene ch6sc10_857 with dissolve
    bd "*Quietly* {b}{size=-10}Leaving him to sleep on his own… I knew they couldn't take care of a man.{/size}{/b}"
    bd "*Quietly* {b}{size=-10}A man has strong urges… urges that needs constant attention.{/size}{/b}"
    scene ch6sc10_858 with dissolve
    bd "*Quietly* {b}{size=-10}The evidence is clearly presented before me… a rather large piece of evidence…{/size}{/b}"
    bd "*Quietly* {b}{size=-10}He’s fully erect even when resting… the twins have been slacking off… tsk, tsk.{/size}{/b}"
    scene ch6sc10_859 with dissolve
    bd "*Quietly* {b}{size=-10}Their inexperience in satisfying him will work to my benefit though.{/size}{/b}"
    bd "*Quietly* {b}{size=-10}I’ll take care of him, show him what it means to be fully satisfied by a woman.{/size}{/b}"
    scene ch6sc10_860 with dissolve
    bd "*Quietly* {b}{size=-10}Once he’s felt how tight I am… how dripping wet the thought of riding him makes me…{/size}{/b}"
    bd "*Quietly* {b}{size=-10}He’ll never want to fuck the twins again… he’ll only crave me.{/size}{/b}"
    scene ch6sc10_861 with dissolve
    bd "*Quietly* {b}{size=-10}His cock makes my wooden tool of pleasure look pitiful.{/size}{/b}"
    bd "*Quietly* {b}{size=-10}Just the thought of this thick cock of his stretching me out… it has my pussy quivering.{/size}{/b}"
    scene ch6sc10_862 with dissolve
    bd "*Quietly* {b}{size=-10}Seas he’s so warm… no wonder he is sleeping on top of the covers.{/size}{/b}"
    bd "*Quietly* {b}{size=-10}He needs me… he needs my wet pussy… I know it… just like I need him.{/size}{/b}"
    scene ch6sc10_863 with dissolve
    bd "*Quietly* {b}{size=-10}He wouldn’t be this hard if he didn’t need me. Aahh…{/size}{/b}"
    bd "*Quietly* {b}{size=-10}The slightest movement and he’ll be inside me-{/size}{/b}"
    scene ch6sc10_864 with dissolve
    mc "Brenda I presume?"
    with vpunch
    bd "*Gasps* {b}Ah!{/b} You’re-... you’re awake?"
    ####Choice####
    menu:
        "Let her satisfy you. ({color=#87e1fa}Charisma{/color})":
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            mc "Hard not to be with a woman mounting me… and her juices running down my cock."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            scene ch6sc10_867 with dissolve
            mc "I was wondering how long it would take you to make your move."
            bd "I knew it… mmh… I knew you had been anticipating me."
            mc "Well? Go on… prove to me that your pussy is one I will crave above all others."
            scene ch6sc10_868 with dissolve
            bd "*Moans* Aaahhh… oh there it is… {b}AahHh!{/b}"
            "Brenda pushes herself down onto your hard cock, you feel the warmth of her soaking wet pussy enclose you."
            mc "Mmgh… you weren’t kidding, you do have a tight little pussy… mmh. Now ride me like you mean it."
            scene bd_lewd2 with dissolve
            $ renpy.pause()
            bd "Aahh! You’re stretching me! Mmh! So this is what a real cock feels like- {b}AyyhhH!{/b}"
            mc "Never had a cock before? Mmmh… you’re finally able to be a little slut then."
            with vpunch
            bd "I’ll be your- {b}Ahhh!{/b} I’ll be your slut! Whenever! {b}AHHH! Wherever you want!{/b}"
            with vpunch
            bd "I’m going to cream all over this big cock of yours- {b}Aiiiyhh! AH!!{/b}"
            mc "Mmmh… I love how tight a woman becomes when she orgasms with me inside her."
            bd "{b}AhhHh!{/b} I’ve never felt anything like this… how your cock slides in and out lubricated by my juices!{b} Aiiiihhh!{/b}"
            scene bd_lewd3 with dissolve
            $ renpy.pause()
            mc "MMmh… you’re certainly lubricated… I’ll give you that… fuck you’re tight."
            bd "I knew you would love my pussy! Nnghh! Isn’t it so much better than other women’s?"
            mc "We’ll know when you manage to make me cum- Nnnh…"
            with vpunch
            bd "Oh I’ll make you cum- Aahh… you’ll remain inside me until I feel you filling me with that warm cum of yours."
            "You feel Brenda pressing you further down into the bed, holding you in place while she enjoys the sensation of riding your cock."
            with vpunch
            bd "*Moans* {b}AHH! I love it! I love your cock! Mmh! I knew I was right about you! AhhH!!{/b}"
            with vpunch
            mc "Fuck- Mmh! If you climax again I can’t hold it back- {b}Aahh!{/b}"
            with vpunch
            bd "{b}Aiiiyhh! No holding back!! Give me what I want!! Ahhh! Let me use your cock! Aiiiyh!{/b}"
            with vpunch
            bd "Watch my perky tits bounce in your face as I make you cum! {b}Aiiyh-Ahh!{/b}"
            scene ch6sc10_869 with dissolve
            bd "*Moans* There it is… you couldn’t withstand the pleasure of my tight pussy after all."
            mc "Seems like you were right… I was craving a tight little pussy."
            bd "Now that you know what my pussy feels like, I expect you will come to crave it often."
            scene ch6sc10_870 with dissolve
            bd "But this is all you’re getting tonight, handsome."
            bd "I’ve got plenty in store for you in the future…"
            bd "Mmmh… your cum feels nice running down my thighs. I think I will savor this feeling and not bathe until the morning."
            mc "Savor it as much as you want, it’ll be a while before I’m back in Looter’s Bay."
            $ charisma += 1
            bd "Oh you’ll be back… your cravings for my tight pussy will only increase as you’re away."
            "Brenda is charmed by having enjoyed you tonight, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            $ renpy.pause(0.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            "Brenda takes her leave, not even bothering to get dressed… and you drift off into the night."

        "Turn her down politely. ({color=#87e1fa}Charisma{/color})":
            scene ch6sc10_867 with dissolve
            mc "Brenda... I'm not in the mood, I've had a long journey here."
            mc "You're beautiful, but tonight what I desire above all else is... rest."
            scene ch6sc10_864 with dissolve
            mc "Maybe another night... if our paths cross again."
            bd "*Sighs deeply* I... I understand, I will ensure our paths will align in the future."
            scene ch6sc10_866 with dissolve
            $ charisma += 1
            bd "Rest well, handsome... I'm going to go masturbate to the thought of our next encounter."
            mc "I never said I'd accept you..."
            bd "Oh you will... nobody turns down this ass twice. *Snickers*"
            "Brenda feels charmed by the thought of your next encounter, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            $ renpy.pause(0.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            "Brenda takes her leave, not even bothering to get dressed… and you drift off into the night."


        "Push her off. ({color=#fc584c}Intimidation{/color})":
            mc "Get the fuck off me, now."
            bd "But I want to-"
            scene ch6sc10_865 with dissolve
            with vpunch
            mc "{b}GET OFF!{/b}"
            bd "*Squeals* {b}Aah! Bastard!{/b}"
            $ intimidation += 1
            scene ch6sc10_866 with dissolve
            mc "If you ever try something like this again, I will kill you."
            bd "You’re a {b}pig!{/b} You don’t even know what you’re missing."
            mc "Not much by the looks of it. Now get the fuck out of my sight."
            "You managed to scare Brenda off, your {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene black with Dissolve(1.5)
            $ renpy.pause(0.5)
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            "Brenda scurries off and you return to your rest."

    scene ch6sc10_871 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_872 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_873 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_874 with Dissolve(1.5)
    play music dark_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    bd "That was exhilarating."
    bd "I think I will go masturbate in my room. *Snickers* That was some cock he had…"
    scene ch6sc10_875 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_876 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc10_877 with Dissolve(1.5)
    bd "Who’s there?!"
    bd "Whoever you are… this is my private room, I suggest you leave at once as I’m not in the mood for games!"
    scene ch6sc10_878 with Dissolve(1.5)
    pl "*Giggling* ..."
    scene ch6sc10_879 with Dissolve(1.5)
    pl "Not even a little game, Brenda?"
    pl "But… I’ve come all this way, just to play with you."
    bd "P-Pearl?!"
    scene ch6sc10_880 with Dissolve(1.5)
    pl "Ah, so you haven’t forgotten about little ol me?"
    pl "*Giggles* …"
    scene ch6sc10_881 with Dissolve(1.5)
    bd "P-Pearl! Please! You don’t have to do this-... I’ve changed!"
    bd "Y-Your sister! She’s forgiven me! She has!"
    bd "She says if I can make amends with you then-"
    scene ch6sc10_882 with Dissolve(1.5)
    pl "*Giggles* Make amends?"
    pl "But… I’m here to play with you. *Giggles*"
    bd "P-Pearl! Please! We’re friends! Remember?!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_883 with Dissolve(1.5)
    $ renpy.pause(0.5)
    with vpunch
    "*Agonizing screams*"
    with vpunch
    $ renpy.pause(1)
    with vpunch
    $ renpy.pause(1)
    with vpunch
    $ renpy.pause(0.5)
    "*Silence* …"
    scene ch6sc10_884 with Dissolve(1.5)
    $ renpy.pause(0.5)
    pl "*Giggling happily* …"
    scene ch6sc10_883 with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_885 with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene bd_death with dissolve
    $ renpy.pause(9.6, hard=True)
    scene black with dissolve
    $ renpy.pause(0.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene ss39 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_886 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "As you arrive on the docks, everyone has gathered to see you off."
    mct "*Chuckles* They weren’t going to let me just run off without a proper goodbye."
    scene ch6sc10_887 with dissolve
    mc "Hey Taz."
    tz "..."
    scene ch6sc10_888 with dissolve
    with vpunch
    mc "*Chuckles* Yeah… I expected as much."
    mc "You’ll be okay getting back on your own?"
    scene ch6sc10_889 with dissolve
    tz "If I say no, will you carry me in your arms all the way to Luxenford?"
    scene ch6sc10_888 with dissolve
    mc "No chance."
    scene ch6sc10_889 with dissolve
    tz "Shame on you! *Sighs* I’ll be fine."
    tz "Diana has offered me to sail with her as she is sailing directly to Luxenford."
    scene ch6sc10_888 with dissolve
    mc "Ah, you’ll be more than fine then. Diana is a capable captain from what I can tell."
    mc "I’ll see you back in Luxenford some time then."
    scene ch6sc10_889 with dissolve
    tz "Mhm-hm! Remember I do freelance work for the Explorer’s guild between your big adventures."
    tz "Just to have something to keep myself busy with and it’s quite fun! Stop by and see me anytime you want!"
    scene ch6sc10_888 with dissolve
    mc "Sure thing Taz, I’ll definitely visit you if I have some free time, otherwise I will let you know when a big adventure is coming up."
    "Taz squeezes you tightly, pressing herself against you before she reluctantly releases you."
    scene ch6sc10_890 with dissolve
    mc "Hey there… Ambassador."
    mc "You look beautiful this morning."
    scene ch6sc10_891 with dissolve
    ori "Oh please! You already working your charms on me first thing in the morning for some political gains? *Snickers*"
    scene ch6sc10_890 with dissolve
    mc "*Chuckles* I have no idea what you’re talking about… I simply think you’re a most wonderful woman, Ambassador."
    scene ch6sc10_891 with dissolve
    ori "*Giggles* Be quiet and give me a hug, silly."
    scene ch6sc10_892 with dissolve
    "Orianna embraces you warmly, wrapping her arms around you looking out over the ocean."
    ori "Thank you, for everything [mc]."
    mc "We’ve been over this, you don’t have to keep thanking me."
    ori "Wrong, I do. I get to live the rest of my life thanks to you."
    ori "I have a lot to be… grateful for."
    mc "*Chuckles* I look forward to seeing you again someday Ori."
    ori "Mhm, me too… that day can’t come soon enough."
    "Orianna releases you from her embrace and you continue on to the next familiar face."
    scene ch6sc10_893 with dissolve
    mc "Kira…"
    with vpunch
    ki "Hmpfh!"
    mc "You knew I was going to return to Luxenford."
    scene ch6sc10_894 with dissolve
    ki "..."
    mc "I know you and I didn’t get to spend much time together this time around, but we’ll make up for it next time-"
    scene ch6sc10_895 with dissolve
    mc "Hey… hey, Red… it’s going to be okay."
    "Kira wraps herself tightly around you, eager to be close to you."
    mc "You know we’ll see each other again."
    ki "Nngh! Promise me!"
    mc "*Chuckles* I promise, Red."
    scene ch6sc10_896 with dissolve
    mc "I will need my fiery captain to navigate the seas for me on future adventures."
    "Kira can’t help but smile at your remark."
    scene ch6sc10_897 with dissolve
    ki "Duh… you’re terrible at navigation. Of course you will need me!"
    scene ch6sc10_896 with dissolve
    mc "*Chuckles* Terrible? Really?"
    ki "*Snickers* …"
    scene ch6sc10_897 with dissolve
    ki "The worst!"
    ki "Fine… I will agree to navigate the seas for you on your future adventures… but only because I would feel guilty if you got lost."
    scene ch6sc10_896 with dissolve
    mc "That’s what I like to hear."
    mc "Enjoy your freedom with Pearl. I know you guys have been excited to let loose on the seas."
    scene ch6sc10_897 with dissolve
    ki "Mhm! If we find ourselves near Luxenford, we may dock and come visit you… if you’re lucky!"
    scene ch6sc10_896 with dissolve
    mc "*Chuckles* I have a habit of getting lucky…"
    scene ch6sc10_897 with dissolve
    ki "Go hug my sister you cheeky fucker. *Snickers*"
    "Kira releases you and heads off, as you turn your attention to Pearl."
    scene ch6sc10_898 with dissolve
    mc "Finally… my little mermaid."
    "Pearl giggles with a sly glint in her eyes… you know exactly what’s coming."
    scene ch6sc10_899 with dissolve
    with vpunch
    mc "*Chuckles* I had a feeling you were going to jump me…"
    pl "You saved me for last! Risky… I could’ve killed someone in jealousy."
    mc "I like keeping you on the edge."
    scene ch6sc10_900 with dissolve
    pl "*Giggles* Kira’s right… you’re a cheeky fucker!"
    pl "You should be more careful… edging a woman can make her burst spontaneously."
    scene ch6sc10_901 with dissolve
    mc "Life gets dull without a little excitement… wouldn’t you agree?"
    scene ch6sc10_900 with dissolve
    pl "You know I agree… you happen to bring a lot of excitement to my life."
    scene ch6sc10_901 with dissolve
    mc "Take care of your sister while you’re out there, okay?"
    scene ch6sc10_900 with dissolve
    pl "Mhm-hm! You know I will."
    scene ch6sc10_902 with dissolve
    pl "Mmmh! I’m going to miss you, Sharky!"
    mc "I’ll miss you too. I enjoyed having you along for this journey."
    pl "Mhm-hm! I want more adventures with you!"
    pl "If you take too long to launch a new adventure at sea… we’ll visit you, like Kira said!"
    mc "I wouldn’t have it any other way. Take care of each other."
    "Pearl reluctantly releases her arms and heads off to find Kira, leaving just you and Diana on the docks."
    scene ch6sc10_903 with dissolve
    mc "Hey… I didn’t expect you to come see me off."
    di "Don’t flatter yourself, I’m just overseeing the preparations of my fleet."
    mc "Shame… I would’ve liked it if you were here to see me off."
    scene ch6sc10_904 with dissolve
    di "You almost sound disappointed?"
    di "You were hoping for a hug? Wasn’t the embraces of the others enough?"
    scene ch6sc10_905 with dissolve
    mc "A hug from you? *Chuckles* Who’d hope for that? Sounds downright awful."
    di "..."
    "Diana approaches you, playfully."
    scene ch6sc10_906 with dissolve
    di "Hugging me sounds awful, huh? Would you like to repeat that?"
    "You feel Diana’s shapely breasts squished against you as she holds on to you tracing her nails teasingly across your lower back."
    scene ch6sc10_907 with dissolve
    mc "I surrender…"
    mc "The only awful thing about hugging you is that it is short lived."
    scene ch6sc10_906 with dissolve
    di "That is truly awful indeed…"
    di "*Soft whisper* {size=-10}{b}Maybe we should do something about that? When you’ve upheld your part of our deal.{/b}{/size}"
    scene ch6sc10_907 with dissolve
    mc "*Chuckles* You know how to keep a man in check."
    di "*Snickers* …"
    scene ch6sc10_906 with dissolve
    di "You know what this means to me, [mc]."
    di "I will not be able to let myself focus on anything but this until it has been resolved."
    scene ch6sc10_907 with dissolve
    mc "Trust me, in a few days you will have your vengeance."
    mc "I give you my word."
    scene ch6sc10_903 with dissolve
    "Diana turns to look at her ships."
    di "I look forward to seeing what your word is worth. My instincts tell me I won’t be disappointed."
    di "That’ll be all, Lord [mc]. I’ll see you in a few days."
    mc "Sure, take care Diana. And look out for Taz… she’s a close friend of mine."
    di "Nothing will happen to her on my watch, I promise you."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc10_908 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "Okay… the sun is barely over the horizon as of yet."
    mc "I should make it to Luxenford before noon if I run at full-speed."
    scene ch6sc10_909 with dissolve
    mc "Eliza… {b}I’m coming home{/b}."
    scene ch6sc10_910
    with vpunch
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6end with Dissolve(2.5)
    $ renpy.pause()
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    #"{color=#00ff00}End of v0.5.9! {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    #"{color=#00ff00}End of v0.5.9! {b}PLEASE SAVE YOUR GAME HERE! OR A FEW IMAGES BACK!{/b}{/color}"
    scene black with dissolve
    $ renpy.pause(0.3)
    stop music fadeout 1.0
    #jump endofversion
    jump ch7sc1

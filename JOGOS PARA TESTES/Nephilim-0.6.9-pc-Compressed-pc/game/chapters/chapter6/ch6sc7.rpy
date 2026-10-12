label ch6sc7:

    window hide dissolve
    #play music mmm_elven_forest fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (1.0)
    #$ renpy.pause(0.5)
    #scene black with Dissolve (1.0)
    $ renpy.pause(0.5)
    scene ss33 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve (1.0)
    $ renpy.pause(0.5)
    scene ch6sc07_001 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    mc "Hnnnghh! Morning everyone..."
    $ renpy.pause(0.5)
    scene ch6sc07_002 with dissolve
    ec "Good morning to you, [mc]."
    ec "It's lovely to see you in such high spirits."
    ec "Did our goddesses visit you in your dreams? *Giggles*"

    if tz_relationship == True:
        scene ch6sc07_003 with dissolve
        mc "Oh, I spent my night with a... goddess."
        tz "*Snickers lightly* ..."
        scene ch6sc07_004 with dissolve

    else:
        scene ch6sc07_004 with dissolve
        mc "Of course I’m in great spirits. We’ve achieved a lot over the past few days here."

    scene ch6sc07_004
    mc "I assume we’re heading back to A’nai today?"
    scene ch6sc07_005 with dissolve
    ec "Mh-hm. We’ll set out as soon as we've packed up camp and everyone’s had some breakfast."
    ec "Make sure you have some as well."
    ec "You may be well rested, but you still need food."
    scene ch6sc07_006 with dissolve
    ec "Once we get back to A’nai, you and I will discuss how to proceed..."
    ec "... concerning the Arugoh tribe and the last temple."

    if ec_relationship == True:
        scene ch6sc07_007 with dissolve
        "As Echo walks past you, she places her hand on your chest, clearly longing for your touch."
        "Which you answer in kind by placing your hand on her lower stomach."
        mc "*Quietly* {size=-10}{b}I look forward to discussing our plans with you, one on one.{/b}{/size}"
        ec "*Quietly* {size=-10}{b}Mmmh... Me too... I’ll make sure we won’t be disturbed during our- strategy meeting.{/b}{/size}"
        mc "I’ll help pack up the tents."
        scene ch6sc07_008 with dissolve
        ec "Are you in a hurry to get back to A’nai? *Giggles softly*"
        scene ch6sc07_009 with dissolve
        mc "You bet I am, desperate even."
        scene ch6sc07_008 with dissolve
        ec "Me too... I’ll help pack up as well. The sooner, the better."
        scene ch6sc07_009 with dissolve
        mct "*Chuckles* With the way she’s lightly digging her nails into my chest, she must also be desperate for our ‘meeting’."
        scene ch6sc07_008 with dissolve
        ec "C’mon, Champion... let's not delay any further."

    else:
        mc "Sounds good, I’ll help pack up the tents."
        ec "Great, I’m sure it will go swiftly with your help."


    scene black with Dissolve(1.0)
    $ renpy.pause(0.5)
    scene ss1 with Dissolve(1.0)
    $ renpy.pause()
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    $ renpy.pause(0.5)
    scene ch5sc07_063 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    am "{b}Frida?!{/b} Did you bring that dress I pointed out?"
    fr "Y-Yes! It should be around here somewhere..."
    scene ch5sc07_064 with dissolve
    am "By all means, take your time... it’s not like I’m completely exposed back here."
    fr "S-Sorry! Luckily, it’s only us in here."
    scene ch5sc07_065 with dissolve
    am "Benefit of being a royal, I suppose, they’ll close down the shop so you aren’t bothered."
    fr "It must be nice, Your Grace."
    am "*Sighs* How often do I need to ask you to address me by my name and not my title, Frida?"
    scene ch5sc07_064 with dissolve
    fr "At least once more, Your Grace."
    with vpunch
    am "{b}Frida!{/b}"
    fr "S-Sorry! Amelia..."
    am "Finally..."
    fr "Is that why you enjoy having [mc] around? Because he doesn’t treat you like a superior?"
    scene ch5sc07_065 with dissolve
    am "Mhm-hm."
    am "He treats me as an equal."
    am "I’m not just some fragile object to him, he actually lets me do stuff."
    am "Like, when we were out on our date- I mean when he took me outside the palace..."
    scene ch5sc07_063 with dissolve
    am "We ventured quite a distance into the wilderness and found this amazing cliff with a huge tree on top!"
    am "And he didn’t even offer to carry me up the large hill."
    fr "You sound excited about that. Wouldn’t you have wanted to be carried by him?"
    scene ch5sc07_064 with dissolve
    am "Yes, and no... I love that he lets me do things on my own. But I know if I had asked him to, he would’ve carried me up."
    am "To him, I’m just Amelia... a friend."
    scene ch5sc07_065 with dissolve
    am "I’m so thankful to him for that... he's giving me something I haven't had before."
    am "You’ve been my only genuine friend my entire life, but even that is limited by your service as my handmaiden."
    scene ch5sc07_064 with dissolve
    am "Whereas with [mc], he might be in service as my bodyguard, but he doesn’t give a hoot about that."
    am "If he resigned as my bodyguard tomorrow, it wouldn’t change how he is with me."
    scene ch5sc07_063 with dissolve
    fr "Y-Yeah... that’s the feeling I get from him as well. He sees everyone as having equal importance."
    scene ch5sc07_064 with dissolve
    fr "Sure, he understands when to be polite around people of high social standing..."
    fr "But I really believe he couldn't care less if someone has noble blood, or is a humble peasant."
    scene ch5sc07_065 with dissolve
    am "I believe that as well."
    am "It’s refreshing, to say the least."
    scene ch5sc07_064 with dissolve
    am "Frida! Seriously, though?! {b}MY DRESS?!{/b}"
    scene ch6sc07_010 with dissolve
    fr "H-here! Sorry! I got caught up in our talk. I've been holding it for a while..."
    scene ch6sc07_011 with dissolve
    am "*Exhales* You’re hopeless..."
    am "How do I look?"
    scene ch6sc07_012 with dissolve
    fr "Beautiful!"
    am "R-Really? It’s not too much with the flowery pattern?"
    fr "Nuh-uh! It is very feminine... and the dress flows nicely along your curves."
    scene ch6sc07_013 with dissolve
    am "Huh... you’re right. It does flow along my body quite well."
    scene ch6sc07_014 with dissolve
    am "And it’s incredibly soft... it must be made from Arazalian silk."
    scene ch6sc07_013 with dissolve
    fr "It is! We found it in the imported goods corner. You can really tell?"
    fr "You must have an impressive sense of touch to be able to feel it."
    scene ch6sc07_014 with dissolve
    am "It is quite simply, really."
    scene ch6sc07_013 with dissolve
    am "You just run your fingertips along the fabric."
    scene ch6sc07_014 with dissolve
    am "You can tell the difference because..."
    scene ch6sc07_013 with dissolve
    am "Silk from Luxeron feels smooth in only one direction, whereas Arazalian silk is smooth in every direction."
    fr "Impressive!"
    scene ch6sc07_015 with dissolve
    fr "Your Grace... Amelia, should I put in an order for this dress, then?"
    scene ch6sc07_016 with dissolve
    am "That would be lovely. Thank you, Frida."
    am "Add a few extra silvers for good measure. I want to ensure the dress is ready for when [mc] returns."
    scene ch6sc07_015 with dissolve
    am "Of course! I have a feeling he will be impressed."
    scene ch6sc07_017 with dissolve
    am "*Quietly* [mc], impressed by me?"
    am "Wouldn’t that be lovely? *Sighs* Knowing him, he won’t even notice the new dress."
    am "Even so, it feels nice to dress up for him... especially since the banquet is in honor of him and his friends."

    if amelia_relationship == True:
        scene ch6sc07_018 with dissolve
        am "Maybe... if I let him feel the silk?"
        am "While I’m wearing it... maybe he’d appreciate the dress then? *Quiet giggle*"
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)

    else:
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)

    scene ss11 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    scene ch6sc06_111 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "Looks like we’re ready to head out. Good job, girls."
    mc "Huntresses, keep your eyes sharp. If we see a chance to bring back food for the tribe, we shall do so."
    scene ch6sc06_112 with dissolve
    ec "Spoken like a true hunter... leadership suits you."
    ec "Suits you really well."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "After your time inside the hunting grounds, everyone is ready to return to the comforts of A’nai."
    scene ch6sc06_118 with dissolve
    pl "Uh-uh! I know the first thing I’m going to do once we reach A’nai."
    mc "What’s gotten you so excited?"
    scene ch6sc06_119 with dissolve
    pl "Guess!"
    scene ch6sc06_120 with dissolve
    mc "I would say food, but we just had breakfast..."
    mc "Given what a little mermaid you are..."
    mc "I’ll wager coin that it's the prospect of a bath that has you riled you up so much."
    scene ch6sc06_119 with dissolve
    pl "Bingo! *Giggles*"
    pl "I'm in need of the greatest bath ever! And the bath in A’nai has the best rejuvenating waters!"
    scene ch6sc06_121 with dissolve
    mc "I wish we had baths like theirs back on the mainland... but natural springs are few and far between there."
    vx "A’nu! I saw something move in the bushes behind us."
    vx "I do not believe it was an animal."
    scene ch6sc06_122 with dissolve
    ec "You are right in your observations, young huntress."
    ec "I saw them too. I believe it was a scout from Arugoh."
    scene ch6sc06_120 with dissolve
    mc "A scout? Maybe we should capture them and bring them back to A’nai?"
    mc "Find out if they really have the ambassador."
    scene ch6sc06_119 with dissolve
    pl "I second that idea! And if they don’t answer our questions, I get to stick 'em with the pointy end!"
    scene ch6sc06_122 with dissolve
    ec "We shall do no such thing. The Arugoh are our former tribeswomen."
    ec "We may have split after the desecration, but we still share Aruna Island together."
    ec "We will not take hostile action against them, not unless we are provoked."
    ec "Now, this area is well known for berries and mushrooms. See if you can gather some we can bring back with us."
    scene ch6sc06_121 with dissolve
    vx "You've got it! We'll bring a feast back with us!"
    mc "*Quietly* {size=-10}{b}I would’ve let you stick 'em with the pointy end.{/b}{/size}"
    pl "*Snickers*"
    scene ch6sc06_113 with dissolve
    "As per Echo’s suggestion, the group scatters and begins to forage."
    scene ch6sc06_123 with dissolve
    vx "Hmm, oh! Got some Juju berries here!"
    ec "Well done, Vex. There's also some Esha-shrooms over here."
    scene ch6sc06_124 with dissolve
    pl "*Sighs* I feel like I’ve been foraging nonstop since getting to this island..."
    pl "And being bent over like this isn't enjoyable compared to... how I'd like to be bent over."
    tz "*Laughs* I know what you mean! I too have a much preferred method of being bent over!"
    scene ch6sc06_125 with dissolve
    pl "Echo? I found this odd ball looking thingy near that tree over there."
    pl "Is it edible?"
    ec "Hold on, I’ll come take a look"
    scene ch6sc07_019 with dissolve
    ec "This tree over here?"
    pl "Uh-huh! Look at those thingies!"
    ec "*Scoffs lightly* Good find, Pearl. Those are coconuts. They’re very nutritious."
    scene ch6sc07_020 with dissolve
    pl "Coconuts -"
    scene ch6sc07_021 with dissolve
    with vpunch
    pl "*Squeals* {b}Auuuah!!{/b}"
    scene ch6sc07_022 with dissolve
    with vpunch
    pl "Owh!"
    ec "Pearl!"
    scene ch6sc07_023 with dissolve
    mc "Pearl?! Are you hurt?"
    pl "N-No... it's just my pride and dignity that took a thrashing."
    scene ch6sc07_024 with dissolve
    pl "Ugh...  I’m filthy!"
    pl "I’m all covered in dirt..."
    scene ch6sc07_025 with dissolve
    ec "There’s a small lake a few minutes north of here. Why don’t you and [mc] go wash up-"
    ec "- While the rest of us keep foraging until you return?"
    "Pearl nods at Echo’s suggestion."
    scene ch6sc07_026 with dissolve
    pl "O-Okay, that sounds nice... thank you."
    scene ch6sc07_025 with dissolve
    ec "Living out here, we are no strangers to getting dirty."
    ec "It's never pleasant to have to trek through the jungle covered in it."
    scene ch6sc07_027 with dissolve
    mc "C’mon, what do you say we go and get you cleaned up?"
    ec "[mc], I’ll leave it to you to take care of her."
    mc "Mmh. *You nod in agreement* We’ll be back soon."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Pearl reaches for your hand and doesn’t let go until you both reach the nearby lake."
    scene ch6sc07_028 with dissolve
    "Once you reach the shore of the little oasis in the jungle, you scan the area for potential threats."
    "While Pearl begins to wash off the dirt and grime from her tumble."
    scene ch6sc07_029 with dissolve
    pl "Ugh... I’m a total mess."
    pl "I can’t believe I tripped and fell head and tits-first onto the muddy ground."
    scene ch6sc07_030 with dissolve
    mc "Don’t worry, we’ve all had trouble with our footing out here."
    mc "You were just unlucky enough to fall on a patch of loose dirt and got smeared. Here, allow me to help clean you up."
    scene ch6sc07_031 with dissolve
    pl "*Whimpers* Mmhph..."
    mc "You’ll be back to your beautiful self in no time."
    scene ch6sc07_032 with dissolve
    pl "Thank you... I really appreciate your help."
    pl "Your touch feels... really good."
    scene ch6sc07_031 with dissolve
    mc "Enjoy it while it lasts, we’re almost done."
    pl "*Whimpers* Nnhh..."
    scene ch6sc07_033 with dissolve
    mc "There we go, all better."
    mc "Your beautiful and cute little mermaid face is all restored."

    if pearl_relationship == True:
        scene ch6sc07_035 with dissolve
        pl "Thank you..."
        scene ch6sc07_036 with dissolve
        pl "Mmmh... my hero."
        scene ch6sc07_033 with dissolve
        mc "Now, are you going to tell me why it is that you tripped over a rock?"
        mc "We both know you are way too surefooted to trip like that."
        scene ch6sc07_035 with dissolve
        pl "I... wanted to be alone with you."
        scene ch6sc07_037 with dissolve
        pl "You’ve been doing so much with all of the local women... while I’ve just sat back."
        pl "It’s so frustrating! I... I want to do things with you too! More than they do..."
        scene ch6sc07_038 with dissolve
        mct "{i}She’s... jealous?{/i}"
        mc "Pearl... could it be that you are... jealous?"
        scene ch6sc07_037 with dissolve
        pl "No... *Sighs* Maybe?"
        scene ch6sc07_035 with dissolve
        pl "So what if I am jealous? They’re all beautiful, exotic women..."
        scene ch6sc07_039 with dissolve
        pl "They’re all clearly lusting after you! You’re driving them mad with desire by being... all heroic and shit."
        scene ch6sc07_038 with dissolve
        mc "*Chuckles* All heroic and shit?"
        pl "..."
        scene ch6sc07_039 with dissolve
        pl "Yes! All the things you do: being brave, heroic, saving them, protecting them, connecting them with their goddesses..."
        pl "The more you do, the more they all desire you. And who can blame them? It’s fucking hot!"
        scene ch6sc07_040 with dissolve
        pl "It’s so fucking hot! Ugh! And now I have to share your time and affections with all of them!"
        with vpunch
        pl "If- If you don’t fuck me soon, I swear I’m going to stab someone out of pure frustration!"
        mct "{i}*Chuckles* Poor thing, she’s sexually frustrated...{/i}"
        mct "{i}*Chuckles* I have been neglecting her needs lately, with so much going on.{/i}"
        scene ch6sc07_033 with dissolve
        mc "You’re cute."
        mc "I’m sorry that you've felt neglected. I can understand the struggle with so many women around us."
        mc "But right now... it’s just you and me."
        pl "*Nods* Mmh."
        scene ch6sc07_035 with dissolve
        pl "That's why I tripped. I was craving your attention."
        scene ch6sc07_033 with dissolve
        mc "You little sneak. Well, now you have it."
        scene ch6sc07_037 with dissolve
        pl "Turn around and... don’t look."
        pl "I'm going to show you something..."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "You do as she says, turning to face the water while she shuffles around in the background."
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc07_041 with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        pl "Hey [mc]!"
        mc "Yeah what is it...?"
        scene ch6sc07_042 with dissolve
        mc "Wow."
        mc "You’re not allowed to be jealous of the locals... not with a body like that."
        scene ch6sc07_043 with dissolve
        pl "I'd almost forgotten how much you like it."
        mc "It's a crime that I made you feel undesired..."
        scene ch6sc07_044 with dissolve
        pl "It certainly is a crime..."
        pl "A crime which I won’t allow to go unpunished."
        pl "Luckily, I know just the punishment for a strong man like you."
        scene ch6sc07_045 with dissolve
        pl "Echo said... you had to take good care of me."
        pl "My body is still dirty..."
        scene ch6sc07_046 with dissolve
        pl "How about you come here and help me get clean?"
        pl "I need someone with strong hands... to help get this dirt off."
        pl "I’m powerless to do it by myself..."
        scene ch6sc07_047
        with vpunch
        "You appear in front of her in a flash."
        pl "*Gasps* Mmmh... there he is, the only man I’ll ever let touch me."
        scene ch6sc07_048 with dissolve
        mc "If another man laid his hands on you... I’d kill him without blinking."
        scene ch6sc07_049 with dissolve
        pl "You'd better... these breasts belong to you, and only you."
        pl "Like the rest of me."
        scene ch6sc07_048 with dissolve
        mc "Have I told you how amazing you are?"
        scene ch6sc07_049 with dissolve
        pl "You have... but you can tell me again."
        pl "I’ll never grow tired of your compliments."
        scene ch6sc07_048 with dissolve
        mc "*Chuckles* How about we get you cleaned up?"
        scene ch6sc07_049 with dissolve
        pl "How about we skip the cleaning and you take me right now?"
        scene ch6sc07_050 with dissolve
        with vpunch
        mc "Come here!"
        "You grab her firmly and lift her, as if she weighs nothing. She responds instinctively and wraps herself around you."
        scene ch6sc07_051 with dissolve
        pl "Mmmh... [mc]... you always know how to treat me."
        pl "I love being in your arms - mmmh..."
        scene ch6sc07_052 with dissolve
        pl "I’m your woman- Mmm..."
        mc "You’re all mine- mmghh."
        scene pl_lewd37 with dissolve
        $ renpy.pause()
        pl "Mmmm..."
        pl "Keep touching me like that. Your hands feel so... goood... Mmm..."
        mc "I wouldn’t be able to keep them off you. Your body is meant to be touched by me."
        pl "Yes... mmmh... it's for your hands and eyes only! Mmmgh..."
        pl "I love- Mmmgh... I love rubbing against you while I'm naked..."
        mc "Mmgh... luckily, I love how it feels when you do. Especially when your perfectly firm and supple breasts press against my chest."
        scene ch6sc07_053 with dissolve
        pl "Mmmh... please... baby, I need you."
        pl "Rubbing against you like this... mmh, it's removed most of the dirt, but there's one spot that still needs you."
        pl "I can't get it clean without you."
        mc "We can’t have that. Why don’t you show me where this spot is?"
        pl "Mmmgh... gladly."
        scene ch6sc07_054 with dissolve
        pl "Here..."
        pl "Please, [mc]... I can’t do it by myself. Won’t you help me?"
        scene ch6sc07_055 with dissolve
        mc "How could I refuse my little mermaid when she asks like that..."
        pl "*Giggles softly*"
        scene ch6sc07_056 with dissolve
        pl "Your mermaid loves that you can’t refuse her."
        pl "Please... I need your lips kissing my... lips."
        scene ch6sc07_057 with dissolve
        mc "Mmmh... you have the most beautiful little pussy a man could desire."
        pl "*Moans* Oohh... touching your woman like this... her breasts and pussy simultaneously?!"
        pl "You’re playing with - Mmmgh... with fire..."
        scene ch6sc07_058 with dissolve
        pl "*Whimpers* I need you- Mmh... I need you, [mc]."
        mc "You’re trembling with anticipation. I won’t keep you waiting, then."
        pl "T-Thank you... kiss my lips... please?"
        scene pl_lewd38 with dissolve
        $ renpy.pause()
        "As soon as your lips touch hers, her body relaxes and her moans fill the entire lake area."
        pl "*Moans* Aaaahhhh... oh, by the seas! Mmmh..."
        mc "*Muffled* Mmmgh... I love this sweet little pussy of yours... mmmh."
        pl "I love- Ahh! I love your mouth on it. I love your head between my legs! Mmgh!"
        mc "Mmmgh... you’re drenching my tongue in juices- Mmmffhh..."
        scene pl_lewd39 with dissolve
        $ renpy.pause()
        pl "I can’t help it- Ahhh! Your warm tongue feels amazing!"
        pl "Do you- Mmmm... like my little wet pussy?"
        mc "Mmmffh! Every lick is filled with your warm juices... increasing my desire for it even more."
        with vpunch
        pl "*Moans* Aahh! Yes! I love how much you enjoy eating me!"
        pl "I can’t believe we haven’t done this since we left the ship! Mmmgh!"
        mc "I should’ve been eating you every day... Mmmgh..."
        with vpunch
        pl "*Moans* Aiiyh- Mmgh! Yes! Yes you should! I will only forgive you if you make me - {b}AHHH!{/b}"
        with vpunch
        pl "{b}-CUUUUUMMM!!! MMGHH!!{/b}"
        scene ch6sc07_059 with dissolve
        with vpunch
        pl "{b}Aiiiyh!! YES!! F-FUCK YOU’RE SO DEEP!!{/b}"
        "She wraps her legs tightly around you, squishing your face between her plump thighs-"
        "Forcing your tongue to remain deep inside her pussy as she orgasms several times."
        with vpunch
        "You barely manage to swallow her juices in time for the next delivery."
        "Just when you think she needs to catch her breath after climaxing this intensely, you feel her grab your cock."
        scene pl_lewd40 with dissolve
        $ renpy.pause()
        pl "Mmmgh... I’m going to suck this hard cock of yours in a moment, but first... more of this, mmmh."
        mc "*Muffled* Mmmfh! Pearl- Mmmh... fuck you’re horny today."
        pl "It’s your fault. Aahhh... You've been driving me crazy with jealousy and desire... Mmmgh..."
        pl "This is what happens when you neglect a woman for too long... mmh, she will have to-"
        with vpunch
        pl "- take things into her own hands... Aahh! Yes! I’m going to- {b}AHHH!!{/b}"
        scene ch6sc07_060 with dissolve
        with vpunch
        "The combination of your tongue buried inside her, your hand squeezing her breast -"
        "- your hardened cock in her hand- it all stimulates her to reach another orgasm."
        scene ch6sc07_061 with dissolve
        pl "*Panting* I need your cock in my mouth... right now."
        pl "It’s not leaving the warmth of my mouth until I’ve been filled with your cum."
        mc "I’m going to love this."
        pl "Yes, you are... lie down for me."
        scene ch6sc07_062 with dissolve
        pl "I love how hard you are when we’re together."
        pl "It shows me that you love this as much as I do."
        scene ch6sc07_063 with dissolve
        mc "Fuck... trust me, I do."
        scene pl_lewd41 with dissolve
        $ renpy.pause()
        pl "*Mwaahh* Mmm..."
        pl "I’m going to suck you so good... I can't wait to feel your cock inside my mouth."
        mc "Fuck, Pearl... mmmh... with the way you’re salivating all over it... I believe you- Mmmgh..."
        pl "I can’t stop my mouth from watering when I taste you... it’s my body’s reaction to it."
        scene pl_lewd42 with dissolve
        $ renpy.pause()
        pl "MMmffhh..."
        mc "Fuck... you’re devouring me- Mmm... I love that slutty little mouth of yours."
        pl "*Glug* Mmmh! I could suck your cock for days..."
        pl "Even then, I wouldn’t get tired of it- *Slurp* MMmffhh..."
        plt "{i}His cock is making me so wet... *Glug* I can feel myself leaking down my thighs...{/i}"
        scene pl_lewd43 with dissolve
        $ renpy.pause()
        with vpunch
        plt "{i}*Suck* If I keep this up- Mmmfh... I’ll make myself cum just by sucking him! MmmH!{/i}"
        mc "You’re shaking. Mmmfh... fuck! I can’t hold it much longer. Mmmfh!"
        with vpunch
        "Hearing your moans, she sucks harder and seals her lips tightly around your cock, preparing herself."
        with vpunch
        pl "*Muffled* Mmh! Cum with me! Fill me! MMmfgh! {b}[mc]!!{/b}"
        with vpunch
        "As she feels your warm cum filling her throat, she rubs her thighs together, sending herself over the edge as well."
        scene ch6sc07_064 with dissolve
        with vpunch
        pl "Mmfgh! *Glug* MMmgH!! *Gasping* Mmmgghhhh!!"
        "Pearl struggles to contain everything as your warm cum and her saliva overflows."
        mc "Fuck... that was a lot, Pearl you don’t have to -"
        scene ch6sc07_065 with dissolve
        with vpunch
        pl "MHhh!"
        "She refuses to hear you out. Instead, she seals her mouth around your cock and swallows all of your cum."
        mc "Ahhh... that’s it... fuck... mmgh... that’s my little mermaid."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "As you blissfully close your eyes to the feeling of Pearl's mouth sucking you dry, you suddenly feel her shift position."
        scene ch6sc07_066 with Dissolve(1.5)
        mc "Mmmgh... Pearl what are you...?"
        scene ch6sc07_067 with dissolve
        pl "I can't take you teasing me with your hard cock any more..."
        pl "Fuck me, here and now!"
        pl "I need your cock inside me!"
        scene ch6sc07_068 with dissolve
        pl "*Moans as she presses down* {b}Aaahh!! F-Fuck!{/b}"
        with vpunch
        mc "MMmh! Five hells, you’re tight... all the divines know I’ve missed being inside you."
        scene pl_lewd44 with dissolve
        $ renpy.pause()
        pl "Oohhhh... finally! Mmmmh!"
        with vpunch
        pl "Your cock is so big - Mmmfh... it’s driving me insane! Ahhh!"
        mc "Mmm... is my slutty little Pearl enjoying her cock?"
        pl "Uufffhh! Yeaaa... I-I can’t get enough of you!"
        with vpunch
        pl "Fuck me harder, [mc]!"
        scene pl_lewd45 with dissolve
        $ renpy.pause()
        with vpunch
        pl "{b}AAAHHH!{/b}"
        pl "{b}YOU’RE SO DEEP! AH!!{/b}"
        mc "Mmmgh! Fuck! My cock might be driving you insane, but this tight pussy of yours is definitely doing the same to me- Mm!"
        with vpunch
        pl "Ahhh! Imagine if the others saw us like this... seeing me riding you like a little slut - {b}MMH!{/b}"
        pl "[mc]- Ahhh! I want you- Mmmgh! I want you to take my ass!"
        scene ch6sc07_068 with dissolve
        mc "You want your delicious plump ass conquered as well?"
        pl "*Moans* Nnnh! Yes! Fuck me in my virgin ass! Make it yours!"
        scene ch6sc07_069 with dissolve
        mct "{i}Damn... her jealousy has driven her horniness to new levels.{/i}"
        pl "Do you like it, baby? Mmm... I can feel you resting against my entrance."
        mc "Mmm... you know I do, I’ve been waiting to claim this delicious ass of yours."
        with vpunch
        pl "D-Don’t wait any longer, then! Take my ass’s virginity, just like you did with my mouth and pussy! Fuck me deep!"
        scene pl_lewd46 with dissolve
        $ renpy.pause()
        "You carefully enter her ass, giving her wet entrance time to open for you, then burying your cock in a blanket of her warmth."
        with vpunch
        pl "*Squeals* {b}Aiiyh!{/b} MmmH! Ahh! Oohhh... f-fuck you’re big!"
        mc "Five hells, your ass is incredible... even tighter than your pussy. MmmH!"
        pl "I-I know! Mmh! I’ve been fingering it for days because I wanted you to claim it the next time we made love."
        mc "Fuck... your mouth, your pussy... your ass, all in one session? You’re spoiling me."
        pl "N-No... I’m the one who’s getting spoiled. Mmmh! Deeper! I need you deeper!"
        scene pl_lewd47 with dissolve
        $ renpy.pause()
        pl "{b}AAHHHHH!!{/b}"
        with vpunch
        mc "This what you desire, huh? My cock buried deep in your tight ass? Mmmh!"
        pl "Fuuuu... yes! It stings a little but - Mmmfh! Fuck, I love it! I can take it..."
        mc "Of course you can- Mmm... you’re my slutty little mermaid, you will take whatever I give."
        pl "Aiiiyh! Yes, I am yours! Mmmh! I’ll always take what you give me! Mmmh!"
        with vpunch
        pl "Deeper, [mc]! I’m ready for more of you!"
        scene pl_lewd48 with dissolve
        $ renpy.pause()
        with vpunch
        pl "*Moans loudly* {b}AHH!!{/b} [mc]- Fuck my ass! {b}MMH!!{/b}"
        mct "{i}Mmmh! It's amazing to know I’m the only man who will ever know what fucking her feels like.{/i}"
        with vpunch
        pl "Harder! MMhh!"
        mc "Fuck! Mmghh, Pearl... your ass is perfect... you’re melting my mind with every thrust."
        with vpunch
        pl "*Moans* My mind is too far gone! AHhh! {b}D-Don’t stop!{/b}"
        mc "Mmgh! I’m gonna..."
        pl "Don’t pull out! MMMh!"
        with vpunch
        pl "Cum in my ass... force me to cum with you, fill me up! "
        with vpunch
        mc "AAhhh! MMmhh! Fuck!"
        scene ch6sc07_071 with dissolve
        with vpunch
        "The sound of Pearl begging for your cum, together with the sensation of her ass tightening around your cock, sends you both over the edge into release."
        with vpunch
        pl "*Squeals loudly* Aiiyh-Ahhh! Fhhh! {b}AHHHH!! SEAS!!{/b}"
        scene ch6sc07_072 with dissolve
        with vpunch
        pl "{b}AHHH!! [mc]!!{/b}"
        "Her body trembles and convulses as she climaxes and keeps quaking, overwhelmed by the sensation of your cock buried deep in her ass as she cums."
        with vpunch
        mc "Fuck... Hnngh! I can’t pull out. Mmmh... fuck you’re tight!"
        scene ch6sc07_073 with dissolve
        "Eventually, her orgasm settles down and she collapses onto the rock, completely spent."
        pl "*Whimpers softly* Mmmmffhh..."
        mc "*Chuckles* You okay? You look like you need to rest for a few days."
        scene ch6sc07_074 with dissolve
        pl "I’m..."
        pl "I’m in love with you."
        scene ch6sc07_075 with dissolve
        pl "My body... my mind... my soul... everything that I am, is all totally and utterly in love with you."
        mc "Guess what... I am in love with you too, Pearl."
        pl "Y-You promise?"
        mc "Mmmh, I promise."
        pl "Seal it with a kiss."
        scene ch6sc07_076 with dissolve
        pl "Mmmmhhh..."
        pl "I love you so much."
        mc "Mmmh... as I do you."
        pl "*Lick* Mmm- I know we’ve said it before... but it feels just as special this time."
        mc "Because what we have is special... Mmm..."
        scene ch6sc07_077 with dissolve
        mc "Go on, be a little mermaid and enjoy the water. We’ll head back once you’ve cleaned up."
        pl "Okay. *Giggles* I promise I won’t take too long!"
        pl "We’re lucky they haven’t come looking for us already..."
        mc "*Chuckles* Shame they didn’t, they could learn a thing or two from a lustful woman like you."
        scene ch6sc07_076 with dissolve
        pl "*Mwah* I’m not about to show them how to satisfy you... that is my knowledge only! *Mwah*"
        mc "Go on, you naughty little thing."
        scene ch6sc07_077 with dissolve
        pl "Thank you for making it up to me... I feel really happy right now."
        mc "You’re welcome. I’m sorry you didn’t feel seen lately."
        pl "You’re forgiven! *Giggles*"
        scene black with Dissolve(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)


    else:
        scene ch6sc07_034 with dissolve
        pl "Thank you, I’ll... I’ll do the rest myself, can you keep watch while I wash myself?"
        mc "You got it. Don’t take too long, though, the others are waiting on us."
        scene black with Dissolve(1.5)
        #play music forest_1 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    scene ch6sc06_047 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    tz "Oh! They’re back!"
    tz "Pearl, it’s good to see you all cleaned up."
    scene ch6sc06_053 with dissolve
    pl "Trust me, it feels good as well!"
    pl "I hope we didn’t keep you guys waiting too long?"
    scene ch6sc06_054 with dissolve
    ec "Not at all, and we’ve spent our time foraging while you were at the lake."
    ec "We’ll return to A’nai with a feast."
    scene ch6sc06_053 with dissolve
    pl "Oh! I love the sound of that. I’m sure we’ll all be famished by the time we get back."
    scene ch6sc06_047 with dissolve
    tz "I share that sentiment, but my back is about done with bending over for today."
    scene ch6sc06_048 with dissolve
    tz "You won’t catch me bending over anytime soon... unless there’s a sweetroll."

    if tz_relationship == True:
        tz "*Quietly* {size=-10}{b}Or... for [mc]. Those are the only two things that could make me want to bend over.{/b}{/size}"
    else:
        scene ch6sc06_042 with dissolve

    scene ch6sc06_042 with dissolve
    zy "Hey... I’m glad you’re back with us."
    scene ch6sc06_043 with dissolve
    sj "Yeah, we like having our first ‘Hunter’ around."
    scene ch6sc06_042 with dissolve
    zy "Suji speaks the truth, it is a title well-earned."
    scene ch6sc06_045 with dissolve
    ec "I'm also pleased you’re back."
    scene ch6sc06_046 with dissolve
    ec "Did everything go well?"
    scene ch6sc06_044 with dissolve
    mc "It's good to be back. And yeah, Pearl didn’t have any injuries, just thoroughly covered in mud."
    scene ch6sc06_053 with dissolve
    pl "Ugh! Don’t remind me!"
    scene ch6sc06_054 with dissolve
    ec "Fear not, you shall have a proper bath back at A’nai."
    ec "[mc] has shared how much you love water."
    scene ch6sc06_053 with dissolve
    pl "Oh, thank you... the lake felt great, but I am still looking forward to enjoying your temple pools."
    scene ch6sc06_017 with dissolve
    vx "Hey, Zyra?"
    zy "Hm? Young huntress?"
    scene ch6sc06_018 with dissolve
    vx "How far are we from A’nai?"
    zy "Oh, a couple of hours... give or take a few, young huntress."
    vx "Great! I can’t wait to tell Miyo that I’m a huntress now."
    scene ch6sc06_017 with dissolve
    zy "She will be thrilled on your behalf. You have been friends since childhood, right?"
    vx "Mhm, just like you and Suji."
    scene ch6sc06_022 with dissolve
    "You feel a gentle touch on your forearm."
    mc "Hmm?"
    scene ch6sc06_023 with dissolve
    mc "Echo, what is it?"
    scene ch6sc06_024 with dissolve
    ec "While you were gone, I found something..."
    scene ch6sc06_023 with dissolve
    mc "Oh? Do tell."
    scene ch6sc06_025 with dissolve
    ec "Nuh-uh! I have decided to share it with you during our strategy meeting."
    ec "Just wanted to give you something more to look forward to. *Giggles*"
    scene ch6sc06_023 with dissolve
    mc "Teasing me, are we? What a cheeky little A’nu."
    scene ch6sc06_026 with dissolve
    ec "..."
    mc "Hey... what’s with that look, all of a sudden?"
    scene ch6sc06_027 with dissolve
    ec "Nothing... *Sighs*"
    ec "It’s just that... I don't know what will happen next."
    scene ch6sc06_028 with dissolve
    mc "You’re worried about the Arugohs?"
    scene ch6sc06_029 with dissolve
    ec "Mmh, how could I not be?"
    ec "We are not overtly hostile towards each other, but we are not on friendly terms either."
    ec "And their stance on outsiders is harsh. Imagine a tribe full of ‘Marah’-minded people."
    scene ch6sc06_028 with dissolve
    mc "Sounds like I’ll have to win them over."
    scene ch6sc06_029 with dissolve
    ec "That’s what worries me. I do not know how to do such a thing..."
    scene ch6sc06_030 with dissolve
    mc "We’ll come up with a plan, and if we don’t... I’ll wing it."
    scene ch6sc06_031 with dissolve
    ec "How can you always be so... confident."
    scene ch6sc06_030 with dissolve
    mc "You believe in me, don’t you?"
    ec "*Nods* Mh-hm."
    mc "There’s your answer."
    scene ch6sc06_031 with dissolve
    ec "Me believing in you makes you feel confident?"
    scene ch6sc06_030 with dissolve
    mc "Yes. It’s hard to explain..."
    mc "But when a man cares about a woman, and she supports him and believes in him..."
    mc "It's a powerful feeling. It make him feel like he can conquer the world."
    scene ch6sc06_031 with dissolve
    ec "The A’khan of Midomir? *Giggles gently* It does have a nice ring to it."
    ec "But for now, I’d settle for you conquering the Arugohs and becoming our A’khan."
    scene ch6sc06_023 with dissolve
    mc "Then that’s what I’ll do."
    scene ch6sc06_025 with dissolve
    ec "Thank you... you've cleared the haze on the horizon, and made the future look bright again."
    scene ch6sc06_023 with dissolve
    mc "Any time you see haze on the horizon, come find me... I’ll banish it."
    scene ch6sc06_024 with dissolve
    ec "My champion."
    scene ch6sc06_032 with dissolve
    vx "A’nu, should we set out? We still have some distance to go."
    vx "I’m eager to get back to A’nai and share the news with Miyo."
    scene ch6sc06_033 with dissolve
    ks "We’ll go when the A’nu wills it, young huntress. Not a moment sooner."
    scene ch6sc06_034 with dissolve
    ec "Kisha... I know she was your student, but do not be so harsh on her."
    ec "She has learned a great deal from being out here. And being excited to see the people you care about?"
    ec "That's not something I will allow to be looked down upon."
    scene ch6sc06_035 with dissolve
    ks "*Sighs* You’re right..."
    ks "I suppose I am anxious about our return."
    scene ch6sc06_036 with dissolve
    ks "I know a lot of our tribeswoman will be thrilled to hear about the heroism of our champion."
    ks "But I do not know how Marah will react to the news."
    scene ch6sc06_034 with dissolve
    ec "She must accept it. With everything he has achieved in this hunt..."
    ec "Even she cannot deny that [mc] is worthy to undertake the trials."
    scene ch6sc06_035 with dissolve
    ks "I pray that you are right. She might be overzealous, but she is an important pillar in our tribe."
    scene ch6sc06_036 with dissolve
    ks "That is one challenge that still lies before you."
    scene ch6sc06_037 with dissolve
    ks "I can only hope that you are man enough to overcome it."
    scene ch6sc06_038 with dissolve
    mc "I understand your concerns, Kisha. It is a challenge I look forward to tackling."
    ks "You’re brave, I’ll give you that... brave and foolish."
    mc "*Chuckles* Thank you... I suppose?"
    scene ch6sc06_042 with dissolve
    zy "Head-huntress makes it sound like a backhanded compliment..."
    zy "But trust me, it is not meant like that. Bravery and folly go hand in hand as companions."
    scene ch6sc06_043 with dissolve
    sj "It is known."
    sj "To be brave, one must also be a little foolish. Situations that require bravery..."
    sj "... are often dangerous. Only a fool would choose to place themselves in such a position."
    scene ch6sc06_042 with dissolve
    zy "So you see, it is a compliment."
    scene ch6sc06_041 with dissolve
    ec "All right, everyone! Gather up everything we've foraged, and let’s return to A’nai."
    scene ch6sc06_054 with dissolve
    ec "We’ll let [mc] carry the camping stuff."
    evr "*Shouts* Great idea! I bet he’ll be sweaty! I love a man who works hard! Let’s do it!"
    scene ch6sc06_055 with dissolve
    mc "Thanks... now I have all of them to deal with."
    ec "*Snickers* Heh-heh."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss8 with Dissolve(1.5)
    $ renpy.pause()
    scene black with dissolve
    scene ch6sc04_486 with Dissolve(2.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    di "I wonder... has he managed to find the diplomat yet?"
    scene ch6sc04_487 with dissolve
    di "*Sighs* ..."
    scene ch6sc04_488
    with vpunch
    $ renpy.pause(0.5)
    scene ch6sc04_489 with dissolve
    di "..."
    scene ch6sc04_490 with dissolve
    $ renpy.pause(0.7)
    scene ch6sc04_489 with dissolve
    $ renpy.pause(0.7)
    scene ch6sc04_490 with dissolve
    $ renpy.pause(0.7)
    scene ch6sc04_491 with dissolve
    $ renpy.pause(0.5)
    ki "Sorry..."
    ki "I know you told me not to do that."
    scene ch6sc04_492 with dissolve
    di "Then why do you insist on doing it?"
    scene ch6sc04_493 with dissolve
    ki "I don’t know. Frustration? Habit? Dramatic effect? Pick one..."
    scene ch6sc04_492 with dissolve
    di "You’re ridiculous..."
    di "Tell me, how goes the effort back in the bay?"
    scene ch6sc04_491 with dissolve
    ki "Progress has been made, but it would go a hell of a lot faster if Brenda wasn’t bothering me constantly!"
    ki "Can’t you make her do something else?!"
    scene ch6sc04_492 with dissolve
    di "Certainly not. I have no desire to deal with her... she’s your friend, you deal with her."
    scene ch6sc04_493 with dissolve
    ki "We’re not friends."
    scene ch6sc04_492 with dissolve
    di "So you keep saying... but nobody is stopping you from killing her."
    di "I certainly don’t give two licks what happens to her. You’re the one [mc] cares about."
    scene ch6sc04_491 with dissolve
    ki "It’s... complicated."
    ki "We were friends, many years ago... we grew up together, learned to sail together..."
    ki "We’ve all made many mistakes since then. It's not as simple as just forgiving and forgetting."
    scene ch6sc04_493 with dissolve
    ki "A-anyways, I’m not here to confide in you!"
    ki "Just... just to report that all the goods in Looter’s Bay have been accounted for."
    scene ch6sc04_492 with dissolve
    di "What about the manifests for the ships currently deployed?"
    scene ch6sc04_493 with dissolve
    ki "That’s the next step. We’ll need to use some of your ravens to order the ships to return."
    scene ch6sc04_494 with dissolve
    di "My ravens? What is wrong with the ones you have in the bay?"
    scene ch6sc04_495 with dissolve
    with vpunch
    ki "Brenda killed them when she attempted her coup! If you aren’t gonna be helpful, so be it!"
    scene ch6sc04_496 with dissolve
    ki "I’ll see to it myself!"
    di "..."
    scene ch6sc04_497 with dissolve
    di "Kira, wait... do you still have the sphere I created for you?"
    scene ch6sc04_498 with dissolve
    with vpunch
    ki "I do! Wait! Did you sense something about Pearl?!"
    scene ch6sc04_499 with dissolve
    di "No, I just wanted to check on how they are doing."
    di "If you don’t mind?"
    scene ch6sc04_500 with dissolve
    ki "Sure, you did create it, after all..."
    scene ch6sc04_501 with dissolve
    ki "Here."
    di "Mmm... Pearl is in good health... still wandering Aruna island."
    ki "What about [mc]?"
    di "We could try... I've never done it without channeling someone related by blood."
    di "But... maybe if we both focus all our thoughts and energy towards [mc]... it could work."
    ki "Let's do it! Think about [mc]... feel him... visualize him..."
    di "Mmm... yes, he is- woah... I feel... he feels so..."
    di "Never mind. Just know they’re both doing well."
    scene ch6sc04_502 with dissolve
    with vpunch
    ki "Thank you! Thank you, Diana!"
    di "You’re hugging me... again..."
    scene ch6sc04_503 with dissolve
    with vpunch
    ki "Ah! Right! Sorry..."
    di "*Sighs* It’s fine... just, don’t make a habit out of it."
    scene ch6sc04_504 with dissolve
    ki "Obviously! I’m going to check on those manifests!"
    di "And send out some of my ravens. The faster those ships return, the better."
    ki "Got it!"
    scene ch6sc04_487 with dissolve
    di "*Sighs* ..."
    dit "He has gotten stronger... I felt it."
    dit "He’s... thriving out there."
    scene ch6sc04_486 with dissolve
    dit "*Giggles gently* Who would’ve thought..."
    dit "[mc]..."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause(0.5)
    "Your group arrives back in A’nai, and Echo informs everyone there will be a ceremony to honor you and Vex tonight."
    scene ch6sc05_124 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "We made it back before dark."
    mct "Although the sun has begun to set, the trip back took longer than expected due to all the foraging."
    scene ch6sc05_125 with dissolve
    "You spot Echo, leaning casually against a palm tree."
    scene ch6sc05_126 with dissolve
    mc "There you are. Hey..."
    scene ch6sc05_127 with dissolve
    ec "*Giggles* ..."
    scene ch6sc05_128 with dissolve
    ec "Here I am."
    ec "Ready for the ceremony?"
    scene ch6sc05_127 with dissolve
    mc "You bet. It’s been nice to see how excited Vex is about all this."
    scene ch6sc05_128 with dissolve
    ec "I’m pleased that you care about her, about all of us."
    scene ch6sc05_129 with dissolve
    ec "Ever since you arrived, you’ve been curious and wanted to learn more about us."
    ec "You’ve accepted our ways and traditions without hesitation. So, thank you."
    scene ch6sc05_131 with dissolve
    ec "I am very much looking forward to bestowing the title of A’nai’s first hunter on you."
    scene ch6sc05_130 with dissolve
    mc "What a coincidence, it just so happens that I'm looking forward to you bestowing it on me too."
    scene ch6sc05_131 with dissolve
    ec "*Snickers* Oh, are you?"

    if ec_relationship == True:
        scene ch6sc05_139 with dissolve
        ec "Perhaps I'll bestow a little something {b}extra{/b} if you visit me after the ceremony."
        scene ch6sc05_130 with dissolve
        mc "Nothing in this world could stop me."
        scene ch6sc05_131 with dissolve
        ec "Good. We don't have time for our strategy meeting before the ceremony, so we might have to do it tonight."
        scene ch6sc05_130 with dissolve
        mc "I’ll be there. While A’nai is asleep, we’ll... strategize."
        scene ch6sc05_147 with dissolve
        ec "*Giggles warmly* Yes... we will..."
        ec "Strategize. And we need to be thorough... {b}deeply{/b} thorough."
        scene ch6sc05_148 with dissolve
        mc "Oh, you better believe I intend to be."
        mc "Once we start... there’ll be no stopping until we’re both satisfied... with the result."
        scene ch6sc05_149 with dissolve
        ec "..."
        "She eyes you up and down slowly until you lock eyes."
        scene ch6sc05_150 with dissolve
        ec "..."
        scene ch6sc05_151 with dissolve
        ec "I’m expecting my champion, and the first hunter of A’nai, to put in a great... effort."
        scene ch6sc05_150 with dissolve
        mc "I’ll make sure my effort leaves you breathless."
        ec "*Giggles* ..."
        scene ch6sc05_151 with dissolve
        ec "I fully intend to leave you breathless as well."
        scene ch6sc05_131 with dissolve
        ec "Now, I must leave you. I have to prepare for the ceremony."
        scene ch6sc05_130 with dissolve
        mc "I look forward to seeing you tonight. Hopefully, in that dress you wore during the last ceremony."
        "Echo doesn't reply, she just offers you a gentle smile before she departs."
        scene ch6sc05_152 with dissolve
        "She quickly ascends the stairs to her chamber to prepare herself."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)

    else:
        scene ch6sc05_131 with dissolve
        ec "We do not have time for our strategy meeting today, I’m afraid. So, we’ll leave it to tomorrow morning."
        ec "Join me in my chambers at dawn, and we’ll discuss everything then."
        scene ch6sc05_130 with dissolve
        mc "At dawn, got it. I’ll be there."
        scene ch6sc05_131 with dissolve
        ec "Now, I must leave you. I have to prepare for the ceremony."
        scene ch6sc05_130 with dissolve
        mc "See you tonight."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)

    scene ch6sc05_124 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}Hmm. There's some time to kill before the ceremony, perhaps I should see what Miyo is up to?{/i}"
    scene ch6sc04_227 with dissolve
    mct "{i}Seems like the tribe's spirits are high since we returned.{/i}"
    scene ch6sc04_228 with dissolve
    mct "{i}The chamber maidens seem to be extra... thirsty.{/i}"
    mct "{i}They’ve been eyeing me even more than usual.{/i}"
    scene ch6sc04_229 with dissolve
    mc "Girls... you look great today."
    scene ch6sc04_230 with dissolve
    bth "*Shouts* So do you! Please visit us soon!"
    tai "Mmmh... I’m dripping just looking at him."
    mm1 "I know what you mean... my whole body tingles with the thought of being ravaged by him."

    if  tata_path == True:
        mm1 "*Quietly* {size=-10}{b}When you told me of what he did... to your ass...{/b}{/size}"
        mm1 "*Quietly* {size=-10}{b}I... I can't stop thinking about it, I want him inside of me like that as well.{/b}{/size}"
        tai "*Quietly* {size=-10}{b}Once you experience him like that... you'll never be satisfied with a pleasure tool again.{/b}{/size}"

    else:
        pass

    scene ch6sc04_231 with dissolve
    mct "{i}Miyo’s hut is the next one.{/i}"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc04_149 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mi "[mc]! Hi!"
    mi "Come in, come in!"
    scene ch6sc04_150 with dissolve
    mi "I must say, you’re looking good today..."
    mi "What brings you to my hut?"
    scene ch6sc04_151 with dissolve
    mc "You know... I had to see how my favorite herbalist is doing."
    mi "*Giggles gently*"
    scene ch6sc04_152 with dissolve
    mi "Sit with me and I'll tell you."
    scene ch6sc04_153 with dissolve
    mi "I’m glad you came by, I’ve been eager to see you."
    scene ch6sc04_154 with dissolve
    mc "Oh? Missed me?"
    scene ch6sc04_153 with dissolve
    mi "Very much! The others are singing your praises after everything that happened out there."
    mi "I wouldn’t be much of a woman if such tales didn’t... excite me to my very core."
    scene ch6sc04_154 with dissolve
    mc "*Chuckles* Good to know I have such an effect on you."
    scene ch6sc04_155 with dissolve
    mi "I must admit... I was a little worried after you guys were away so long."
    scene ch6sc04_156 with dissolve
    mi "If something bad had happened to you, to any of you, I'd have been miserable!"
    scene ch6sc04_160 with dissolve
    mi "But you... you handled everything, like a man."
    scene ch6sc04_161 with dissolve
    mi "A handsome... strong... brave man, protecting his entourage of women."
    scene ch6sc04_162 with dissolve
    mc "Now who’s singing my praises? I just did what felt right in the moment."
    mc "Did Vex already tell you how we completed our trial?"
    scene ch6sc04_163 with dissolve
    mi "She did."
    mi "She was very excited, to say the least... and with good reason."
    mi "This is a big milestone for her, you know?"
    scene ch6sc04_162 with dissolve
    mc "Yeah, I know. Her dream is to become a huntress the tribe can be proud of."
    scene ch6sc04_161 with dissolve
    mi "She also want to follow in her mentor’s footsteps, Kisha."
    mi "She wants to become Head-Huntress one day."
    scene ch6sc04_153 with dissolve
    mi "I believe she has what it takes, once she gains a few more years of experience."
    scene ch6sc04_162 with dissolve
    mc "She does. Right now, she has a lot to learn. As we all do in our youth."
    mc "I’m not much older than either of you, and I’m still learning as I go."
    scene ch6sc04_163 with dissolve
    mi "You may not be much older, but you have gained a lot of wisdom through experience."
    scene ch6sc04_164 with dissolve
    mi "And... a lot of scars too, proving what a formidable warrior you are."
    scene ch6sc04_163 with dissolve
    mi "Do you wish to know what my big dream is?"
    scene ch6sc04_162 with dissolve
    mc "Sure."
    scene ch6sc04_161 with dissolve
    mi "*Giggles* Guess."
    scene ch6sc04_162 with dissolve
    mc "Oh, come on... it could be anything."
    scene ch6sc04_161 with dissolve
    mi "C’mon, guess!"
    scene ch6sc04_162 with dissolve
    mc "Hmm... you’re a herbalist, maybe you dream to discover a new variety of plant that you can find uses for?"
    scene ch6sc04_161 with dissolve
    mi "A good guess, but no..."
    scene ch6sc04_160 with dissolve
    mi "To be a chamber maiden."
    mi "To pledge my life to fulfill my desires and that of the A’khan."
    scene ch6sc04_162 with dissolve
    mc "No way..."
    scene ch6sc04_161 with dissolve
    mi "You don't think I'm serious?"
    scene ch6sc04_162 with dissolve
    mc "Wait... really? But I thought once you choose a path, you follow it for life?"
    scene ch6sc04_161 with dissolve
    mi "That is our way, yes. But it doesn't change my secret dreams... or the fact that..."
    scene ch6sc04_160 with dissolve
    mi "I could live out my dream when I'm alone with... my A’khan."
    scene ch6sc04_161 with dissolve
    mi "If you still don't believe me, then I will show you."
    scene ch6sc04_163 with dissolve
    mi "We still have time before the ceremony... time for you to... treat me like your chamber maiden."
    scene ch6sc04_164 with dissolve
    mi "If that would be something you desire?"

    if mi_path == True:
        scene ch6sc04_165 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mi "Mmm..."
        "Miyo puckers her lips, signaling she wishes to taste yours."
        mct "{i}I can’t lie... I have missed those lips of hers.{/i}"
        scene ch6sc04_166 with dissolve
        mc "I desire you... chamber maiden or not."
        mc "But... in this moment..."
        mc "Show me what I can expect from my little personal chamber maiden, once I become A’khan."
        scene ch6sc07_078 with dissolve
        mi "Mmmgh- Mmmh..."
        mc "I’ve been eager for these lips... mmmh."
        mi "Since our last kiss, I can't stop thinking about kissing you... again and again- Mmmh..."
        mi "Treat me like a chamber maiden... use me however you want."
        mc "Stand up... I want to see you."
        scene ch6sc04_195 with dissolve
        mi "Like this?"
        mi "Does it please you when I undress for you?"
        mc "Fuck... yeah. It pleases me greatly."
        scene ch6sc04_195 with dissolve
        mi "My A’khan enjoys seeing my young, well-developed body presented before him?"
        mc "I love those outrageous breasts of yours... and how they remain perfectly shaped even when naked."
        scene ch6sc04_197 with dissolve
        mi "Mmm... what about my supple ass?"
        mc "Damn... I had forgotten what a naughty little creature you are."
        scene ch6sc04_198 with dissolve
        mi "That won’t do... I'd better remind you, then."
        mi "Approach me... with your heroic spear. I desire to feel it."
        scene ch6sc04_199 with dissolve
        mi "Ohhh... y-yes, I remember this sensation..."
        mi "The size... the shape... hardened by desire for... me."
        scene ch6sc04_200 with dissolve
        mi "So warm ... it’s like it perfectly understands what I need."
        mc "Why don’t you show me what a chamber maiden like you needs?"
        scene ch6sc04_201 with dissolve
        $ renpy.pause(0.5)
        with vpunch
        mi "Hnngh! This! This is what I need..."
        "Miyo leaps into your arms, resting herself on your cock and wrapping her legs and arms around you."
        mc "Mmmh... you’re soaking wet already..."
        scene ch6sc04_202 with dissolve
        mi "Because I need you inside me... fuck me."
        scene mi_lewd1 with dissolve
        $ renpy.pause()
        mi "*Moans and Gasps* Ahh! Ahh-You’re! You’re piercing me!! {b}Aiiiihh!!{/b}"
        mc "Damn... Miyo, you’re-"
        mi "I am what you desire! Ahh! Exactly what you’re craving!"
        mc "Fuck... you’re tight- Hnngh."
        mi "*Moans* I-Is that a bad thing? AHhH..."
        mc "*Moans* No... Nnghh... It’s an incredible thing to be as tight as you... Mmm!"
        mc "I can’t get enough of this tight, wet little pussy of yours."
        with vpunch
        mi "*Moans* F-Fuck me harder, then! Make everyone hear my moans of pleasure! {b}Aiiih!!{/b}"
        scene mi_lewd2 with dissolve
        $ renpy.pause()
        mi "Oohh!! Yes!- Yess... I love how you're going slow but so deep- Mmmh... it feels so intimate!"
        mi "*Gasps* Ahh... I love being your chamber maiden!"
        mi "D-Do not hold back! Ahhh! Your spear belongs to me at this moment! {b}Aiiiih!{/b}"
        with vpunch
        mc "Fuu... Miyo-Mmmh... This little flower of yours is soaking wet and still so fucking tight..."
        scene mi_lewd3 with dissolve
        $ renpy.pause()
        mi "*Moans* Ahh-ahiiih... Your spear is- Mmm, a weapon of pleasure! Ahhh!"
        mi "*Moans* I fingered myself several times a day while you were gone but -"
        mi "- it just doesn’t compare to you. Ahh! Not even close! {b}Aiiiyhh!{/b}"
        scene mi_lewd4 with dissolve
        $ renpy.pause()
        mc "MMnhgh! Your pussy is tightening and quivering, you’re on the verge of cumming."
        mi "*Moans* Aiiiih-aiih! I feel it! Keep filling me with your powerful spear! {b}AHH!{/b}"
        mi "{b}*Moans loudly* Let your desires overflow, Champion! Ahh!{/b}"
        with vpunch
        mi "D-Deeper! {b}I need you to fuck me deeper!{/b}"
        "Hearing her moans and pleas to be fucked as she's on the brink of cumming, you decide to fuck her properly."
        scene mi_lewd5 with dissolve
        $ renpy.pause()
        with vpunch
        mi "*Moans loudly* {b}Aahh! OHH!!{/b} Yes! Give it to me!"
        "You pick up the pace, fucking her little pussy harder and deeper than she has ever experienced, until she suddenly cums all over you."
        with vpunch
        mi "{b}*Moans loudly* Aiiiyyhh!! OHH!! I’m- I’m CUMMING!!{/b}"
        scene mi_lewd6 with dissolve
        $ renpy.pause()
        mi "MMmh!! D-Don’t stop! Hero, don’t stop fucking me!"
        mc "Fuck... Hnnghh! You’re so tight, Miyo! MMh!"
        with vpunch
        mi "I know! I can feel it as well as you! Mmghh! Fuck my little flower until you bloom! AHh!"
        scene mi_lewd5 with dissolve
        $ renpy.pause()
        with vpunch
        mc "I’m going to - MmmH!!"
        with vpunch
        mi "{b}YES!! FILL ME!{/b} I'm your chamber maiden, it is my duty and honor to make you cum! MMhh!"
        scene ch6sc04_203 with dissolve
        with vpunch
        mct "{i}Fuck! Is she cumming again?! {b}AHHH!{/b}{/i}"
        "As Miyo feels your warm seed filling her up, her body releases another orgasm, tightening around your cock."
        mi "*Squeals* {b}Aiiiyh-Ahh! MMmffhh!{/b}"
        scene ch6sc04_204 with dissolve
        mc "*Panting* Fuck... Miyo, you know how to satisfy me..."
        mi "*Giggles* As do you, hero. Feeling your warm seed inside me, it’s all I desire."
        scene ch6sc04_205 with dissolve
        mi "And this cock of yours... it’s the ultimate weapon of pleasure."
        mi "Whenever it’s not inside me, all I can think about is the next time that it will be."
        mc "Mmh... that little pussy of yours is a perfect fit."
        scene ch6sc04_208 with dissolve
        mi "*Giggles* Yes... it sure feels like we’re made for each other."
        scene ch6sc04_206 with dissolve
        mi "I hate to cut this moment short, but we'd better get ready for the ceremony."
        scene ch6sc04_207 with dissolve
        mc "Yeah, I know... but I had to see you."
        scene ch6sc04_208 with dissolve
        mi "It pleases me you did... [mc]- I..."
        scene ch6sc04_209 with dissolve
        mi "I like you a lot... if it weren’t obvious."
        mi "Like a whole lot... I pray you will become A’khan soon. My whole body aches for it."
        scene ch6sc04_210 with dissolve
        mi "Now, go... I’ll see you out there... once your warm seed is done leaking out of me. *Mwah*"
        mc "*Chuckles* See you soon."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    else:
        scene ch6sc04_162 with dissolve
        mc "Sorry Miyo... but I need to catch up with some of the others before the ceremony."
        scene ch6sc04_156 with dissolve
        mi "Oh! Of course! Sorry... this is a little embarrassing."
        scene ch6sc04_155 with dissolve
        mi "Please forgive my moment of weakness."
        mc "There’s nothing to forgive. I applaud you for going after what you want."
        scene ch6sc04_154 with dissolve
        mc "Miyo, don’t take this to heart... you’re incredibly beautiful and lovely to be around."
        mi "..."
        scene ch6sc04_153 with dissolve
        mi "Thank you... you’re always so good to me. You know just what to say to make me feel better."
        mi "You'd better get going. I need a moment to banish my embarrassment and get ready."
        mi "..."
        scene ch6sc04_154 with dissolve
        mc "Sure thing, I’ll see you at the ceremony."
        mi "*Nods* Mmh."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    scene ss43 with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc02_004 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    el "Borri! C’monnn... you’re, like, my favorite dwarf in the whole world!"
    br "Aye... maybe that’s because I'm the only dwarf y'know, lass?!"
    el "How about you just accept my compliment, then we can get straight to me asking you for a favor? *Giggles*"
    scene ch6sc02_007 with dissolve
    br "*Sighs* Alright, how many bundles of logs are we talking about this time?"
    el "Just three!"
    br "Three?! Lass, y'know I can only carry one at a time?"
    el "Perfect! You take one, I’ll take two! C’mon, we'd better hurry!"
    scene ch6sc02_004 with dissolve
    br "*Exhales* Yer killing an old dwarf..."
    el "Stop it... you aren’t even old! Besides, the others are bringing food and ale!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc02_008 with Dissolve(1.5)
    $ renpy.pause(0.5)
    br "Who’s joining us?"
    scene ch6sc02_011 with dissolve
    el "Flynn and Alice!"
    scene ch6sc02_014 with dissolve
    br "I swear... if those two gobble up all the ale before we arrive..."
    el "Then we’ll set Trouble to chasing them! *Giggles*"
    scene ch6sc02_015 with dissolve
    br "Ahh, Trouble... how is she faring out there?"
    el "She seems to be doing great. I’ve brought her food a couple of times, and she almost always visits when I’m there."
    scene ch6sc02_016 with dissolve
    el "She isn’t losing weight, so she is definitely eating plenty."
    br "Probably lots o' deer and hares nearby. Perfect meals fer a wolf."
    el "I’ve seen plenty around the area, so you're right about that. I just wish... *Sighs*"
    br "There was nothin ye could’ve done t' save her companion, lass."
    el "Let’s swing by the Drunken Rooster, real quick. I need an outfit change if we intend to work."
    br "Aye, I could do with a change as well, I believe I still have a shirt or two lying in my storage there."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ss44 with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc02_181 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "Hnngh! That’ll do... three more bundles of logs for when [mc] returns."
    al "You’re amassing a bunch of materials, It’s beginning to look the part."
    scene ch6sc02_182 with dissolve
    al "Have you told [mc] how much progress you’ve made?"
    el "Yes! He seemed quite impressed, more than I thought he would be."
    scene ch6sc02_181 with dissolve
    el "He just needs to get his bum back here so we can begin building!"
    scene ch6sc02_183 with dissolve
    fy "You’ve done really well. When you guys first started talking about this, I thought it was just a pipe dream."
    fy "But as Alice said, it’s really starting to look like something."
    el "Thank you, Flynn, that’s... surprisingly nice of you to say."
    fy "I’m always nice!"
    scene ch6sc02_182 with dissolve
    al "No, you ‘think’ you’re always nice..."
    el "*Giggles*"
    scene ch6sc02_184 with dissolve
    br "So, did ye bring food and ale? Or was I tricked?"
    al "*Snickers* Don’t you worry! I made sure Flynn didn’t drink even a sip of it!"
    el "Let’s set up for dinner and enjoy the last bit of sunlight that's left."
    br "Aye! Flynn, yer with me gathering firewood. Girls, ye set up the campsite."
    scene ch6sc02_182 with dissolve
    al "Sounds good to me, let’s get to work!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ss45 with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch4sc18_014 with Dissolve(1.5)
    play music dark_5 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(1)
    scene ch4sc18_015 with dissolve
    $ renpy.pause(1)
    scene ch4sc18_016 with dissolve
    $ renpy.pause(1)
    scene ch4sc18_017 with dissolve
    $ renpy.pause(1)
    scene ch4sc18_018 with dissolve
    $ renpy.pause(1)
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc07_080 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc07_081 with dissolve
    lx "Ihr... ruh... itoh... sehar..."
    scene ch6sc07_079 with dissolve
    lx "Ikh... rhul... etoh... zehkir..."
    scene ch6sc07_082 with dissolve
    lx "*Exhales* Another impure specimen..."
    scene ch6sc07_083 with dissolve
    lx "How... disappointing."
    scene ch6sc07_084 with dissolve
    lx "This is the third bloodline which has failed to produce the desired results."
    lx "Which means there’s only one -"
    scene ch6sc07_085 with dissolve
    ta "Only one bloodline left for you to investigate in Luxeron, the Kaze-ki clan."
    lx "Tsk!"
    scene ch6sc07_086 with dissolve
    ta "And it just so happens there’s only one living member left of their clan."
    ta "And I happen to know she’s right here... in Luxenford."
    scene ch6sc07_087 with dissolve
    lx "Let me guess... in return for this information...?"
    lx "Think carefully before words leave your mouth. You know what happens when you annoy me."
    ta "Lux... you know me better than that."
    scene ch6sc07_088 with dissolve
    ta "In return for helping you find the last living Kaze-ki clan member, I simply want a favor."
    lx "..."
    ta "Sometime soon, I will make a move that will force [mc] and his companions right into my hands."
    ta "That is when you will return the favor. I will need you in the battle that ensues."
    scene ch6sc07_089 with dissolve
    lx "You want me to fight for you...?"
    scene ch6sc07_088 with dissolve
    ta "I knew you weren’t all looks."
    ta "Yes, fight for me in the battle that is to come... and I shall bring you..."
    ta "{b}Rin Kaze-ki.{/b}"
    scene ch6sc07_089 with dissolve
    lx "Humans... such simple creatures."
    lx "Sure... I shall fight for you if it saves me the trouble of finding this... Rin."
    scene ch6sc07_090 with dissolve
    ta "Great! Lux, it is always a pleasure doing business with you."
    ta "I look forward to seeing you in action."
    lx "..."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc05_009 with Dissolve(1.5)
    play music relax_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "{i}Looks like people have begun to assemble for the ceremony.{/i}"
    scene ch6sc05_010 with dissolve
    mct "{i}Miyo and Vex are building quite the bonfire, they really seem to enjoy these ceremonies.{/i}"
    scene ch6sc05_011 with dissolve
    mct "{i}Can’t blame them. I enjoyed the last ceremony, after all.{/i}"
    scene ch6sc05_012 with dissolve
    mct "{i}I was surprised how much Suji and Zyra enjoyed the last ceremony.{/i}"
    mct "{i}But they definitely proved they know how to cut loose and have a good time.{/i}"
    scene ch6sc05_013 with dissolve
    mc "Hey huntresses."
    bth "*Giggles*"
    scene ch6sc05_014 with dissolve
    zy "Hey, hunter..."
    zy "I could get used to saying that, it rolls off the tongue."
    scene ch6sc05_015 with dissolve
    mc "*Chuckles* It does, doesn’t it?"
    mc "Although, soon you’ll be upgrading my title to A’khan."
    scene ch6sc05_014 with dissolve
    zy "Someone’s feeling confident..."
    zy "But I wouldn’t mind if that became reality."
    scene ch6sc05_016 with dissolve
    sj "He’s much more than just a hunter, that’s for sure."
    sj "Champion of the goddesses, hero of A’nai, hunter... and future A’khan."
    scene ch6sc05_017 with dissolve
    mc "Ladies... if I wasn’t feeling confident before, your support is all the boost I need."
    bth "*Giggles softly*"
    scene ch6sc05_018 with dissolve
    sj "I didn’t leave anything out, did I? Oh! Slayer of Jimun, conqueror of the trials..."
    sj "A man with a brave soul, warm heart, tough exterior, and handsome too..."
    scene ch6sc05_020 with dissolve
    zy "Sounds like somebody is in heat. *Snickers*"
    zy "How about a drink to celebrate his heroics?"
    scene ch6sc05_021 with dissolve
    sj "Sounds good. [mc], will you share a drink with us?"
    scene ch6sc05_022 with dissolve
    mc "You bet. We only live once right?"
    scene ch6sc05_023 with dissolve
    sj "*Giggles* That’s the spirit. We’ll drink to that."
    scene ch6sc05_024 with dissolve
    zy "Sounds good to me!"
    zy "This drink isn’t for the faint of heart, so... if you can keep it down, Suji and I will both visit your hut tonight."
    scene ch6sc05_025 with dissolve
    bth "Cheers to only living once! Cheers to [mc] becoming a hunter!"
    mc "Cheers!"
    scene ch6sc05_026 with dissolve
    mc "*Gulp, Gulp*"
    mct "{i}Wait... this tastes like -{/i}"
    scene ch6sc05_027 with dissolve
    with vpunch
    sj "*Snickers* Got him!"
    zy "*Laughs* A hunter, yes! But he still lacks training!"
    scene ch6sc05_028 with dissolve
    bth "*Mwah* Mmm... *Mwah* Nnnhh..."
    mct "{i}They got me... *Sighs* Again...{/i}"
    scene ch6sc05_029 with dissolve
    zy "Such a shame... *Mwah* looks like we won’t be visiting you tonight."
    sj "*Mwah* I know... what a night it could’ve been."
    scene ch6sc05_030 with dissolve
    mc "You’re cruel, cruel huntresses."
    bth "*Laughs lightly* Hehehe!"
    scene ch6sc05_031 with dissolve
    zy "If only you were able to keep that drink down..."
    scene ch6sc05_032 with dissolve
    sj "Imagine the night we could’ve had... I’m sure the three of us would never forget it."
    sj "As a hunter, you always need be ready for the unexpected."
    scene ch6sc05_031 with dissolve
    zy "You live and you learn. *Snickers*"
    scene ch6sc05_030 with dissolve
    mc "Girls... I swear, when I’m the A’khan, there’ll be no saving you."
    bth "You'd better hurry up and claim the title, then!"
    mc "Count on it. I’ll see you around the ceremony."
    bth "Bye, bye!"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc05_033 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}Even Kisha is here? I suppose that makes sense given that Vex is her protege.{/i}"
    scene ch6sc05_034 with dissolve
    "Sensing your approach, Kisha locks eyes with you."
    scene ch6sc05_035 with dissolve
    ks "Outsid... Champion."
    scene ch6sc05_036 with dissolve
    mc "Hey, Kisha... how about you just call me by my name?"
    ks "..."
    scene ch6sc05_035 with dissolve
    ks "I suppose that will do... we have gained some... familiarity, after all."
    scene ch6sc05_037 with dissolve
    mc "We have. I’m glad you’re acknowledging it."
    scene ch6sc05_038 with dissolve
    ks "Don’t get any ideas! Yes, you have proven yourself in some capacity, but -"
    scene ch6sc05_037 with dissolve
    mc "But you won’t acknowledge me as your ally until I finish the trials and become A’khan?"
    scene ch6sc05_038 with dissolve
    ks "Exactly... you still have a big challenge ahead of you."
    scene ch6sc05_039 with dissolve
    ks "Only one trial remains, but it is within the temple of Maia..."
    ks "And that is located in the heart of the Arugoh tribe's village. How you deal with them will show your worth."
    scene ch6sc05_037 with dissolve
    mc "How I deal with them?"
    scene ch6sc05_035 with dissolve
    ks "Yes, that is what I said."
    ks "They are our former tribeswomen, there is history and ancestry shared between us."
    scene ch6sc05_039 with dissolve
    ks "They are very hostile towards outsiders, but if you just waltz in there and try to kill them..."
    ks "That won’t be received well here, by their distant family or former friends."
    scene ch6sc05_038 with dissolve
    ks "The great desecration divided us two decades ago, but only because we differed on how to face our future."
    ks "Not because we harbor ill will towards each other."
    scene ch6sc05_037 with dissolve
    mc "I understand... I’ll have to win them over, somehow."
    scene ch6sc05_036 with dissolve
    "Kisha looks intrigued and surprised at your response."
    scene ch6sc05_035 with dissolve
    ks "Tomorrow morning."
    scene ch6sc05_036 with dissolve
    mc "What?"
    scene ch6sc05_035 with dissolve
    ks "You’re meeting with the A’nu at dawn to discuss how you'll proceed."
    ks "Before that, you will meet me at the combat area."
    scene ch6sc05_039 with dissolve
    ks "I shall test your worth and see if you have what it takes to win them over."
    ks "Now, leave me alone. And don’t be late."
    scene ch6sc05_037 with dissolve
    mc "I look forward to seeing what you’re made of, then. See you tomorrow."
    "Kisha scoffs at your remark, but a slight smile lifts the corners of her mouth."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc05_040 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}Sakari is here as well? Not surprising, she did tell me she enjoys these gatherings.{/i}"
    scene ch6sc05_041 with dissolve
    mc "Hey, Sakari, you look stunning tonight."
    scene ch6sc05_042 with dissolve
    sk "*Giggles softly* ..."
    scene ch6sc05_043 with dissolve
    sk "Champion... you look quite striking yourself."
    scene ch6sc05_044 with dissolve
    sk "I heard you had quite the adventure during the hunt?"
    scene ch6sc05_045 with dissolve
    sk "The others have been gossiping... but I’d love to hear the story from you..."
    sk "... under more intimate circumstances."
    ####Choice####
    menu:
        "Agree to share your version. ({color=#ff8cdd}Romance{/color})":
            scene ch6sc05_046 with dissolve
            mc "You know, I think you'd enjoy hearing my side of the story."
            $ sk_path = True
            mc "It’s definitely something we'd better keep intimate between us. I doubt the other women could handle such a tale."
            scene ch6sc05_047 with dissolve
            sk "Oh? And you believe me to be woman enough to handle your... tale?"
            scene ch6sc05_048 with dissolve
            sk "Mmm... yes, perhaps it'll be something I’ll need to hear... again and... again."
            scene ch6sc05_049 with dissolve
            mc "I believe you’re the only woman in A’nai who could handle it."
            sk "*Snickers* ..."
            scene ch6sc05_052 with dissolve
            sk "I’m pleased you can sense what caliber of woman I am."
            sk "I, too, believe I am the only woman in A’nai who can handle your heroic tale."
            sk "I shall prove it after you’ve dealt with the Arugoh tribe, and claimed the title of A'khan."
            sk "Then I will happily enjoy... your tale."
            scene ch6sc05_046 with dissolve
            mc "I look forward to sharing it with you, Sakari"
            scene ch6sc05_044 with dissolve
            sk "As do I..."
            sk "[mc], you... you fascinate me."
            $ sk_trust += 3
            scene ch6sc05_046 with dissolve
            mc "The feeling is mutual, Sakari... very much so."
            "Sakari is intrigued by you and she appreciates your boldness. Her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."

        "She’ll have to make do with the gossip. ({color=#2bff8b}Friendly{/color})":
            scene ch6sc05_046 with dissolve
            mc "I’m sure what they’re saying is true."
            $ sk_path = False
            scene ch6sc05_045 with dissolve
            sk "*Sighs* I’ll have to make do with what they tell me, then."

    scene ch6sc05_045 with dissolve
    sk "Enjoy the ceremony, handsome."
    scene ch6sc05_053 with dissolve
    mc "You too, enjoy yourself."
    scene ch6sc05_054 with dissolve
    sk "Thank you. I believe I shall."
    scene ch6sc05_055 with dissolve
    sk "I’ll spend some time with Kisha. I do not like her sitting alone."
    scene ch6sc05_056 with dissolve
    mc "I won’t keep you any longer, then. Enjoy the ceremony."
    mct "{i}There’s much more to Sakari than just being the Mistress of the maidens.{/i}"
    mct "{i}She’s actually very thoughtful and kind.{/i}"
    scene ch6sc05_057 with dissolve
    mct "{i}Let’s see how Vex and Miyo are doing with the bonfire.{/i}"
    scene ch6sc05_058 with dissolve
    mc "Hey, girls, you’re on bonfire task again?"
    scene ch6sc05_059 with dissolve
    mi "[mc]! Hi... yeah, we may be the tribe's youngest ..."
    mi "But we can handle wood like nobody else... *Giggles*"
    scene ch6sc05_061 with dissolve
    mc "And you look damn good doing it too."
    scene ch6sc05_060 with dissolve
    mi "Thank you!"
    scene ch6sc05_059 with dissolve
    mi "If you... need some wood handled, you should come to us."
    scene ch6sc05_061 with dissolve
    mc "*Chuckles* I’ll keep that in mind."
    scene ch6sc05_063 with dissolve
    vx "Are you ready for the ceremony?"
    scene ch6sc05_062 with dissolve
    mc "I believe so. I’m looking forward to it, last time was a great night."
    scene ch6sc05_063 with dissolve
    vx "Mmm, it was... tonight is for both of us."
    vx "So, don’t have too many Jungle-jingles with Suji and Zyra! You’ll fall asleep before A’nu arrives."
    scene ch6sc05_062 with dissolve
    mc "Oh? You were watching me?"
    scene ch6sc05_065 with dissolve
    vx "I... I was merely observing you!"
    vx "All of A’nai could hear them slap you! *Quietly* {size=-10}{b}And kiss you...{/b}{/size}"
    scene ch6sc05_066 with dissolve
    vx "..."
    mct "Sounds like our little huntress is jealous."
    scene ch6sc05_065 with dissolve
    vx "I’m just worried you’ll be drunk for the ceremony, we’re hunting partners..."
    vx "It’ll reflect poorly on both of us. No more Jungle-jingles, okay?"
    scene ch6sc05_066 with dissolve
    mc "Don’t worry, Vex, I have no intention of making you look bad."
    scene ch6sc05_065 with dissolve
    vx "[mc], I... thank you."
    scene ch6sc05_067 with dissolve
    mi "Hmmmmh... sounds like little Vex is prone to jealousy?"
    mi "You know full well there’s only a little alcohol in Jungle-jingles."
    mi "Sounds more like you don’t want him doing it because you don’t want their lips on him? *Snickers*"
    scene ch6sc05_068 with dissolve
    with vpunch
    vx "Miyo!! S-Shut up!"
    scene ch6sc05_069 with dissolve
    vx "Why do you say such things in front of [mc]?! You’re embarrassing me!"
    mi "*Giggles* Sorry! Sorry! You’re right to be concerned about him. You’re hunting partners, after all."
    mi "I’ll leave you two to chat."
    scene ch6sc05_070 with dissolve
    mi "*Whispers* It seems Vex likes you a lot more than I thought."
    mi "*Whispers* I think being your hunting partner... might be the best thing that could’ve happened to her."
    mi "*Whispers* [mc]... please take good care of her. She acts tough, but she is very sensitive."
    mc "I have no intention of hurting her. As her partner, I’ll have her back whenever she needs it."
    scene ch6sc05_071 with dissolve
    "Miyo leaves to finish the bonfire, and you approach Vex."
    mc "Hey... don’t worry about what Miyo said. She meant no harm."
    scene ch6sc05_074 with dissolve
    vx "I know... it’s just embarrassing when she calls me out like that... especially in front of you."
    scene ch6sc05_072 with dissolve
    mc "It’s okay to feel jealous. It’s human nature, and a sign that you care about the person."
    vx "*Nods* Mmm."
    scene ch6sc05_074 with dissolve
    vx "I do... care."
    scene ch6sc05_075 with dissolve
    vx "I’m really proud that you are my hunting partner and that we’re graduating together."
    scene ch6sc05_071 with dissolve
    mc "Me too, Vex. I’m lucky to have you as my huntress."
    scene ch6sc05_074 with dissolve
    vx "Sorry... for trying to stop you from having Jungle-jingles."
    vx "You can, of course .. enjoy as many as you like."
    scene ch6sc05_073 with dissolve
    mc "Thanks, but I’m good. They tricked me into it."
    scene ch6sc05_075 with dissolve
    vx "They’re often so serious, it can be surprising when they show their rebellious side."

    if vx_relationship == True:
        scene ch6sc05_074 with dissolve
        vx "How are you feeling? You know... after -"
        scene ch6sc05_072 with dissolve
        mc "*Quietly* After we mated in the temple?"
        vx "*Nods* Mmm."
        scene ch6sc05_073 with dissolve
        vx "..."
        scene ch6sc05_074 with dissolve
        vx "Y-Yes... after that."
        vx "How do you feel? About... me."
        scene ch6sc05_071 with dissolve
        mc "I feel good. No... that doesn’t even begin to cover it. I feel incredible."
        mc "Whenever I look at you, I just want to be closer to you... and when I catch your eye, I can’t help but smile a little."
        mc "*Quietly* Knowing that you’re {b}my{/b} little huntress now."
        scene ch6sc05_074 with dissolve
        vx "You... say such sweet things..."
        vx "Is that... really how you feel about me?"
        scene ch6sc05_071 with dissolve
        mc "It is, if it weren’t for everybody else here, I’d grab you by your slender waist and pull you in for a kiss."
        scene ch6sc05_074 with dissolve
        vx "I ... I really want that."
        scene ch6sc05_075 with dissolve
        vx "It pleases me ... to know you feel the same as I."
        scene ch6sc05_074 with dissolve
        vx "I... I was a little worried, since you... you haven’t touched or kissed me since."
        scene ch6sc05_071 with dissolve
        mc "You’re right, we can’t have that..."
        mc "Come, we’ll have to do something about it, right now."
        scene ch6sc05_075 with dissolve
        vx "*Quietly* [mc]?! What...? You’re crazy!"
        scene ch6sc05_071 with dissolve
        mc "*Quietly* I’m crazy about you. Now, follow me."
        vx "*Nods*"
        scene ch6sc07_091 with dissolve
        vx "I can’t believe we’re doing this... we’re really sneaking off from our own ceremony?"
        mc "We won’t be gone for long, we’re just getting a little privacy from the others."
        scene ch6sc07_092 with dissolve
        vx "O-Okay... this is quite exciting, actually."
        vx "I’ve never done something like thiiiiiiiiiiis-"
        scene ch6sc07_093 with dissolve
        with vpunch
        vx "*Gasps* Aahh! [mc]! What are you...?"
        mc "I’m taking what I want."
        scene ch6sc07_094 with dissolve
        vx "MMmghh! Mmmh... Nnnghh..."
        vx "Finally... you’re kissing me again."
        mc "You make it impossible not to... your lips are perfect for kissing."
        scene ch6sc07_095 with dissolve
        "Responding to your words, she pulls you closer for an even deeper kiss."
        vx "*Moans* Mmmh... your lips are the only ones I ever want to taste. Mmmh..."
        scene ch6sc07_096 with dissolve
        mc "They’re all yours, right now."
        scene ch6sc07_095 with dissolve
        vx "Mmmgh- I need them... mmmh... I need you."
        scene ch6sc07_096 with dissolve
        vx "My body needs you... Mmmh..."
        scene ch6sc07_097 with dissolve
        vx "*Shares tongue* Mmmhh... please... mate with me... *Licks* Right now..."
        mc "Mmmh... tempting, little one... but tonight we will have to settle for this."
        scene ch6sc07_098 with dissolve
        vx "*Moans gently* Aahhh... oohhh..."
        vx "That... ohh... that feels- Mmmh!"
        scene ch6sc07_099 with dissolve
        mc "Mmm... I had a feeling you were craving this."
        vx "Aahh... I can’t believe you’re touching me lik... out in the open- Mmm!"
        mc "You’re the one who’s been pressing your thighs against my cock since we began kissing."
        scene ch6sc07_100 with dissolve
        vx "*Moans* Like my hunter..."
        scene ch6sc07_101 with dissolve
        vx "I take what I want - mmgh, yes... touch me like this!"
        scene ch6sc07_100 with dissolve
        vx "Please [mc]... I need you, please mate with me?"
        scene ch6sc07_101 with dissolve
        mc "No."
        scene ch6sc07_100 with dissolve
        vx "W-Why not- Mmmhhh... have I done something wrong?"
        scene ch6sc07_101 with dissolve
        mc "Of course not. You’re perfect... MMm... I simply want to build up your desire further than you’ve ever felt before."
        scene ch6sc07_100 with dissolve
        mc "So that next time we mate, your body will experience an overwhelming orgasm as you bloom."
        scene ch6sc07_101 with dissolve
        vx "*Moans* Ahh- mmmh... I pray it will happen soon. My body is already trembling just from your touch. Mmm..."
        scene ch6sc07_100 with dissolve
        mc "For tonight, I will enjoy knowing your juices are running down your inner thighs during the ceremony."
        scene ch6sc07_101 with dissolve
        with vpunch
        vx "So naughty... aahh... *Whimpers* I’m almost there."
        scene ch6sc07_099 with dissolve
        "As you feel her little flower beginning to contract around your fingers, you slowly pull them out of her."
        vx "N-No... Mmgh... so mean..."
        scene ch6sc07_098 with dissolve
        vx "*Moans gently* You’re playing with fire .."
        mc "Kiss me."
        scene ch6sc07_097 with dissolve
        vx "Mmmgh... I love when you taste my tongue."
        mc "You’re delicious. I love how you eagerly present it to me, allowing us to exchange our saliva."
        scene ch6sc07_096 with dissolve
        vx "Mmgh! *Licks* It’s all yours. I’m all yours. *Kiss*"
        scene ch6sc07_095 with dissolve
        vx "Let’s keep kissing all night and not attend the ceremony... Mmgh..."
        scene ch6sc07_096 with dissolve
        mc "Ready to skip out on our own ceremony? *Kiss* Mmmgh..."
        scene ch6sc07_095 with dissolve
        vx "If only such a thing could be reality *Sighs* Mmmh..."
        scene ch6sc07_094 with dissolve
        vx "Okay... we better get back to the others... mmh, it’s starting soon."

    else:
        scene ch6sc05_075 with dissolve
        vx "Go on, enjoy the ceremony. I’ll help Miyo finish the bonfire."

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc05_076 with Dissolve(1.5)
    $ renpy.pause(0.5)
    "You spot Pearl and Tazzy chatting and giggling."
    mct "{i}Those two have really been hitting it off lately.{/i}"
    scene ch6sc05_077 with dissolve
    mct "{i}Makes sense, they are the only two ‘non’ tribal women out here.{/i}"
    mct "{i}*Chuckles* And they both can be a little aloof at times...{/i}"
    scene ch6sc05_078 with dissolve
    pl "Wait - seriously?! Fishys as big as buildings?!"
    pl "There’s no way! ... is there?"
    mc "Evening, ladies."
    scene ch6sc05_079 with dissolve
    pl "[mc], hi!"
    tz "*Giggles* Hey, [mc]..."
    pl "Hold on, let me sit before Tazzy continues her fishy revelations!"
    scene ch6sc05_080 with dissolve
    mc "*Chuckles* Fishy revelations? Oh boy..."
    mc "Don’t keep us in suspense, Taz... Pearl looks like she’s about to burst."
    scene ch6sc05_082 with dissolve
    tz "If I'd known how excited she would get, I probably wouldn’t have said anything."
    scene ch6sc05_083 with dissolve
    mc "Trust me, you’re better off giving her every last detail, now that you've begun."
    scene ch6sc05_082 with dissolve
    tz "Right you are! I was telling her about a story I heard from another Chronicler at the Scriptorium."
    tz "Apparently, the world she was observing had big ocean creatures, like... real big!"
    scene ch6sc05_083 with dissolve
    mc "I have not seen any myself, but I've heard tales of large creatures living in our oceans, as well."
    scene ch6sc05_082 with dissolve
    tz "That world is an ocean world, everything living there is underwater."
    tz "She said it has various biomes and the deeper you go, the bigger the creatures are."
    scene ch6sc05_083 with dissolve
    mc "Yikes... after Jimun, I’ll be happy not having to deal with large creatures anytime soon."
    scene ch6sc05_082 with dissolve
    tz "I second that! The chronicler I spoke with... she never made it back for her evaluation."
    tz "According to the Scriptorium, she had been... devoured. By one of those creatures."
    scene ch6sc05_083 with dissolve
    mc "*Chuckles* I know a little something about being eaten alive... I feel for your friend."
    scene ch6sc05_084 with dissolve
    pl "Speaking of eating... Miyo shared some Oranberries with me."
    pl "They taste like oranges, but they leave your tongue tingling for a few minutes."
    scene ch6sc05_085 with dissolve
    pl "Want one?"
    scene ch6sc05_086 with dissolve
    tz "Do I ever! I love oranges."
    scene ch6sc05_087 with dissolve
    tz "Mmffh!"
    scene ch6sc05_086 with dissolve
    tz "I’ll have one more."
    scene ch6sc05_087 with dissolve
    tz "Nnghh!! *Suck* mmm..."
    scene ch6sc05_086 with dissolve
    tz "One more won’t hurt..."
    scene ch6sc05_087 with dissolve
    tz "Mmffh! *Licks* nnnhh..."
    scene ch6sc05_088 with dissolve
    tz "I’m in heaven! It feels like my tongue is dancing! *Giggles lightly*"
    pl "......"
    scene ch6sc05_089 with dissolve
    pl "She... she ate all of them!"
    scene ch6sc05_090 with dissolve
    pl "*Growls* Hnnrrrhh..."
    tz "Pearl! You must try one! It’s like tiny orgasms on your tongue! *Giggles*"
    mct "{i}Taz is playing with fire... but then again, Pearl knows she’s a foodie. She only has herself to blame.{/i}"
    scene ch6sc05_088 with dissolve
    tz "[mc]... if only you could feel my tongue right now..."
    mc "You ate them all... so I’ll have to take your word for it."
    scene ch6sc05_082 with dissolve
    tz "Sorry... when I taste something delicious I tend to get carried away."
    scene ch6sc05_083 with dissolve
    mc "Well, you better go hassle Miyo for some more oranberries. You didn’t even let Pearl have one."
    scene ch6sc05_082 with dissolve
    tz "I’ll go do that right away! If there are any oranberries left in A’nai, they will become Pearl's!"
    scene ch6sc05_083 with dissolve
    mc "Glad that’s sorted. I’ll leave you two beauties to it, then."
    scene ch6sc05_080 with dissolve
    "The girls giggle as you continue to make the rounds."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "Everyone continues to converse around the ceremonial area as the sun sets and the bonfire is lit."
    scene ch6sc05_091 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}I wish Eliza and the others were here to enjoy this with us.{/i}"
    mct "{i}Maybe we should arrange for a bonfire at our homestead when I get back?{/i}"
    scene ch6sc05_092 with dissolve
    "After a while of everyone enjoying the warmth of the fire, everyone quiets down in anticipation."
    evr "*Chatting* She’s about to arrive. A’nu will be with us shortly. Look! Top of the temple!"
    scene ch6sc05_093 with dissolve
    "At the top of the temple a figure appears from Echo’s personal chambers."
    scene ch6sc05_094 with dissolve
    "A figure akin to that of a goddess."
    scene ch6sc05_095 with dissolve
    "The women around the bonfire gasp in awe at her appearance."
    scene ch6sc05_096 with dissolve
    mc "She really is a stunning woman."
    scene ch6sc05_097 with dissolve
    mc "She exudes a strong presence, confident, relaxed, intentional... beautiful."
    scene ch6sc05_098 with dissolve
    mi "Shh. The ceremony is starting."
    scene ch6sc05_099 with dissolve
    mh "Tsk. How dare they include the outsider in yet another ceremony?!"
    mh "Bestowing the title of hunter on him... they’ve all lost their minds to his corruption."
    mh "Tsk! They will be forced to see reason once I reveal the outsider we captured."
    scene ch6sc05_100 with dissolve
    "As Echo gently walks towards the crowd, everyone remains still, the only sound is of the fire cackling."
    scene ch6sc05_101 with dissolve
    ec "Sisters of A’nai."
    scene ch6sc05_104 with dissolve
    ec "Tonight, we welcome not one, but two new members to our ranks as huntress and hunter."
    scene ch6sc05_105 with dissolve
    ec "Tonight, we celebrate their birth as pillars of our community!"
    ec "They have proven their teamwork is unmatched by taking down Jimun, Gaia’s great serpent!"
    scene ch6sc05_104 with dissolve
    ec "For the first time in well over two decades, we now have a hunter among us!"
    scene ch6sc05_103 with dissolve
    ec "He has proven himself worthy of us, of all of you."
    scene ch6sc05_105 with dissolve
    ec "Sisters of A’nai, will you accept this man amongst you?"
    ec "Sisters of A’nai, will you accept [mc], slayer of Jimun, Gaia’s chosen, hero of A’nai?"
    scene ch6sc05_103 with dissolve
    evr "*Cheering* Yes! We accept him as one of us! He is chosen! He is our hunter!"
    scene ch6sc05_101 with dissolve
    ec "Sisters of A’nai, will you accept this young woman?"
    scene ch6sc05_104 with dissolve
    ec "Sisters of A’nai, will you accept Vex, as a huntress of A’nai?"
    scene ch6sc05_103 with dissolve
    evr "*Cheering* Yes! We accept her as one of us! She is fearless! She is our huntress!"
    ec "Then tonight, celebrate them as they deserve! As they have earned! May the goddesses smile upon them!"
    scene ch6sc05_102 with dissolve
    "As Echo turns about to take her leave, she stops mid-turn."
    scene ch6sc05_106 with dissolve
    "Her gaze meets yours, as if it were a warm embrace."
    scene ch6sc05_107 with dissolve
    ec "..."

    if ec_relationship == True:
        "No words are needed between you, her smile and eyes speak volumes."
        "She longs for your embrace, one which can’t come soon enough."
        scene ch6sc05_108 with dissolve
        mct "{i}I need to get out of this celebration... quickly.{/i}"
        mct "{i}I have no desire to keep a woman like her waiting.{/i}"

    else:
        "She shares a kind smile with you before she proceeds to turn around."

    scene ch6sc05_108 with dissolve
    "Echo retires to her chambers, leaving the rest of you to enjoy the night in celebration."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc05_109 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mi "[mc]! A’nai’s first hunter in my lifetime!"
    mi "Dance with me!"
    scene ch6sc05_110 with dissolve
    mi "*Giggles* I almost forgot how good of a dancer you are!"
    mc "I had a good teacher."
    scene ch6sc05_109 with dissolve
    mi "I’d love to meet her one day! She must be quite the woman!"
    scene ch6sc05_110 with dissolve
    mc "*Chuckles* How do you know it’s a woman who taught me?"
    scene ch6sc05_111 with dissolve
    mi "*Sensual* Only a woman can teach a man to dance... that seductively."
    mc "I’m dancing seductively?"
    mi "*Sensual* Mmm... very."
    scene ch6sc05_110 with dissolve
    mi "*Giggles* Don’t stop... let us enjoy having a proper man in our midst!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)

    if ec_relationship == True:
        scene ch6sc02_885 with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        play music explore_2 fadein 1.0
        #stop music fadeout 1.0
        "After an hour of being pulled around the bonfire, dancing with the girls, you take your leave to find Echo."
        "You make your way around the temple, to the back stairway opposite the celebrations."
        scene ch6sc02_886 with dissolve
        mct "{i}This will do, I’m not much of a fan of sneaking around like this...{/i}"
        mct "{i}But it’s for her sake. She doesn’t want the others to know until after I finish the trials.{/i}"
        scene ch6sc02_887 with dissolve
        "As you near her chamber, the air seems filled with anticipation, your body feels electric."
        scene ch6sc02_888 with dissolve
        mct "{i}Damn... just the thought of her is making me excited.{/i}"
        scene ch6sc07_102 with dissolve
        mc "I doubt there has ever lived a woman with a closer resemblance to a goddess."
        scene ch6sc07_103 with dissolve
        ec "I am as beautiful and alluring as a goddess?"
        ec "*Giggles softly* I must believe you... you have actually met several goddesses."
        scene ch6sc07_104 with dissolve
        mc "Mmh, trust me... you are a goddess."
        ec "..."
        mc "I can tell you’re smiling."
        scene ch6sc07_105 with dissolve
        $ renpy.pause(0.2)
        with vpunch
        ec "*Gasps gently* Oh... you can? Does my body betray me?"
        mc "It has a habit of doing that in my presence."
        scene ch6sc07_106 with dissolve
        ec "Mmmh... denying it would be futile..."
        scene ch6sc07_105 with dissolve
        ec "My champion... can you feel my heartbeat through my breast?"
        scene ch6sc07_106 with dissolve
        mc "I can."
        scene ch6sc07_105 with dissolve
        ec "Then you know what I desire."
        scene ch6sc07_106 with dissolve
        mc "You wore the dress again."
        scene ch6sc07_107 with dissolve
        ec "How could I not?"
        ec "The man I have fallen in love with told me he desired to see me in it."
        scene ch6sc07_106 with dissolve
        ec "I was powerless to resist his request... mmm..."
        scene ch6sc07_105 with dissolve
        mc "I’m pleased that you didn’t resist. This dress elevates your already impossible beauty to another level."
        scene ch6sc07_108 with dissolve
        ec "*Moans softly* Nnnh... undress me."
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch6sc07_109 with dissolve
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        ec "Mmmh... I love how you take in my body."
        ec "Watching your desire grow... feeling it press against me... mmmh."
        scene ch6sc07_110 with dissolve
        mc "Mmh, I love your body."
        mc "Everything about you is intoxicating... the way your breasts feel... the scent of cocoa and milk-leaves."
        scene ch6sc07_111 with dissolve
        ec "*Moans* Ohhh... the way your thumb is pressing my nipple- Mmm..."
        scene ch6sc07_110 with dissolve
        mc "I know how sensitive your breasts are, especially your nipples."
        scene ch6sc07_111 with dissolve
        ec "They become increasingly sensitive when you’re near me- Aahh..."
        scene ch6sc07_110 with dissolve
        mc "I couldn’t take my eyes off you at the ceremony... you were mesmerizing."
        scene ch6sc07_111 with dissolve
        ec "Oh, [mc]... as were you. My body has been trembling, waiting for you to join me."
        scene ch6sc07_110 with dissolve
        mc "Then let’s get this lovely dress off you and give your body the attention it deserves."
        scene ch6sc07_111 with dissolve
        ec "Y-Yes... please. Mmm..."
        scene ch6sc07_112 with dissolve
        ec "*Gasps* Ah! Oh-Mmm! S-Sucking my nipple - aahh... you take such good care of me. Mmm..."
        mc "*Sucks gently* How could I not? You’re my queen... my A’nu... my woman."
        scene ch6sc07_113 with dissolve
        ec "*Moans* Mmmh... that’s it... suck my nipple..."
        scene ec_lewd42 with dissolve
        $ renpy.pause()
        "You suck the hard nub of her nipple, and she runs her fingers through your hair, keeping your head close to her breast."
        mc "Mmmgh... so good... feeling your tight body within my grasp, teasing your nipple with my mouth... mmm."
        ec "D-Don’t stop... mmmghh... I need this, my breasts have been longing for your affection."
        ec "Aahhh... keep squeezing me with your hands- Ahhh! Champion..."
        with vpunch
        mc "*Sucks intimately* Mmh... you’re close already? Then allow me to- *Sucks intensely*"
        with vpunch
        ec "*Moans* Aiiyh! [mc]- Yes! K-Keep sucking like that... Oh! I’m- I’m going to-"
        scene ch6sc07_114 with dissolve
        "You can feel Echo is about to burst, her whole body trembles in response to the sensations of your mouth on her body."
        "You suck onto her nipple firmly, pulling upwards as she instinctively grasps your head and presses you into her breast."
        with vpunch
        ec "*Moans* {b}AHhh! OH MY!! [mc]!{/b} I’m blooming! AHhH! I'm cumming!! {b}Aiiiyh!{/b}"
        scene ch6sc07_113 with dissolve
        "Her whole body shakes as she climaxes from merely having her nipple sucked, then you gently ease up."
        ec "Ohh... my love... you know exactly what to do to me... mmm..."
        ec "Kiss me... I crave your lips -"
        "You grab her leg and hip, quickly lifting her up."
        scene ch6sc07_115 with dissolve
        with vpunch
        ec "*Gasps* Aah! You’re such a man..."
        ec "My man... *Giggles* I love you."
        mc "I love you."
        scene ch6sc07_116 with dissolve
        ec "Do you accept me? As your woman... your girl... your queen... your lover... your mate..."
        mc "*Nods* Mmh."
        ec "Then... kiss me now, and I’ll spend the rest of my life being your woman."
        scene ch6sc07_117 with dissolve
        mc "You grasp her ass firmly as the two of you embrace each other’s warm lips passionately."
        ec "Mmmgh..."
        scene ch6sc07_118 with dissolve
        "With each taste of each other's mouths, your kisses instinctively deepen and grow ever more intimate."
        scene ec_lewd43 with dissolve
        $ renpy.pause()
        ec "*Licks* Mmmh... so good... you’re so good with your tongue..."
        ec "It’s like... mmmh... we’re making love with our tongues. *Licks intimately* Nnnhh..."
        mc "You’re delicious... whenever you catch my eye, all I can think about is moments like these."
        ec "Oh, [mc]... me too. Enjoying your tongue like this- Mmmgh... is becoming my favorite thing in the world."
        ec "My heart longs for these moments with you... my body in your arms, my breasts resting on your chest..."
        ec "*Licks* Mmmh... our tongues taking turns in each other’s mouths... sharing our saliva- Mmmgh..."
        mc "Echo- Mmmgh..."
        ec "I need your spear... *Licks* Mmmgh... I need you inside me."
        scene ch6sc07_118 with dissolve
        "Hearing the husky need in her voice, you put her down... excited for what’s to come."
        scene ch6sc07_119 with dissolve
        "She immediately drops to her knees before you, her tongue eagerly seeking your cock."
        scene ec_lewd44 with dissolve
        $ renpy.pause()
        ec "Mmmh... your heroic spear has been away from my mouth for too long already..."
        ec "Do you not agree, my love?"
        mc "I couldn’t agree more... Mmmh... that tongue of yours..."
        mc "Take me in your mouth. Remind me how good you are at pleasuring me with those tasty lips of yours."
        ec "Mmmh... as you desire."
        ec "Your beautiful cock won't be leaving my mouth until I’ve tasted your seed."
        scene ch6sc07_120 with dissolve
        with vpunch
        "She claims your cock, sliding you as deep inside the warm wetness of her mouth as she can."
        ec "*Muffled gag* Mmfghh! Mmgghhrh..."
        scene ec_lewd45 with dissolve
        $ renpy.pause()
        mc "Mmmh... fuck that’s good... that’s it, relax your jaw."
        "Encouraged by your response, she follows your suggestion and manages to slide you even deeper."
        ec "*Muffled slurping* Mmmh- Sllrrhhh... big... mmmh... delicious..."
        mc "That’s my good girl... Mmmh... fuck... that wet tongue of yours is going to make me cum real quick."
        scene ec_lewd46 with dissolve
        $ renpy.pause()
        "This is a woman on a mission, and she has no intention of stopping until you fill her mouth."
        "Hearing your moans, she continues to force you as deep as she can while wrapping her tongue around you."
        mc "*Moans* Mmmh... if you keep this up... that little mouth of yours will soon be filled like you so desperately want."
        with vpunch
        mc "Five hells... you’re sucking cock like a true queen... Mmmgh... Echo- I’m going to- Mmmgh!"
        scene ch6sc07_120 with dissolve
        with vpunch
        ec "*Muffled gagging and sucking* {b}MMGH!! NNFGHH! HHRRHH!{/b}"
        scene ch6sc07_121 with dissolve
        with vpunch
        "You send load after load deep into the back of her throat. You can feel it flooding her mouth, surrounding your cock as it mixes with her saliva."
        with vpunch
        ec "*Muffled* Mmghh- Mmgh!"
        mc "MMghh! That’s it- Aahhh... drink all of it- Mmmgh!"
        scene ch6sc07_122 with dissolve
        "Barely able to contain it all, Echo eagerly swallows and sucks repeatedly."
        mc "Fuck... that’s my girl... don’t waste a single drop."
        ec "*Sucks intimately* Mmmgh... so good... my hero- Mmm..."
        scene ch6sc07_123 with dissolve
        ec "Your queen is pleased... mmh, very pleased."
        mc "So is your champion... I love that naughty mouth of yours."
        ec "I crave more... I desire to mate with you."
        mc "Lie down, and I will mate with you until your every desire has been fulfilled."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        #stop music fadeout 1.0
        $ renpy.pause(0.5)
        scene ch6sc07_124 with Dissolve(1.5)
        $ renpy.pause(0.5)
        "Echo proceeds to lie down before you, shifting to her side and allowing you to enter her from behind."
        ec "Aaahh... you’re teasing me... pressing your spear against my flower like this... mMm!"
        ec "Take me, my champion! Show me how wild and untamed your desire for me is! Mate with me!"
        scene ec_lewd47 with dissolve
        $ renpy.pause()
        ec "Ahhh! By the goddesses your spear is incredible! Mmmh! Take me, [mc], make me feel desired!"
        mc "Mmmgh... damn, you intend to be this tight for me every time? Mmmh... five hells."
        mc "It's like your tight, exotic pussy is sucking my cock with every thrust! Mmh!"
        scene ec_lewd48 with dissolve
        $ renpy.pause()
        with vpunch
        ec "*Moans loudly* {b}Aiiyh! Oh- OHH!! [mc]{/b} - Just like that! Mmmgh!"
        mc "Hnnghh... coming so soon? You really love having me inside you."
        ec "Ahh- Mmmgh! I do! Mating with you is the beeesstt feeeeeeling- AHhh!"
        with vpunch
        scene ec_lewd49 with dissolve
        $ renpy.pause()
        ec "Aiiyh! So deep! AHhh! My flower is being blessed- Mmmh!"
        with vpunch
        ec "Do not stop, my love! My flower craves your seed! Aaahh! Bloom within me!"
        mc "Mmmgh... I can’t hold it any longer... not with you being this wet and tight- Mmmgh!"
        with vpunch
        ec "Yess... enjoy my little wet flower- MMmh! Fill me with our combined nectars! {b}[mc]!!{/b}"
        scene ch6sc07_125 with dissolve
        with vpunch
        "Echo reaches another orgasm as she feels your cock throbbing, digging her nails into your thigh instinctively."
        "As you begin filling her up, you grasp both her thigh and her breast, squeezing both firmly."
        scene ch6sc07_126 with dissolve
        with vpunch
        ec "AHHH! [mc]! My body is yours!! {b}AHHH! I BLOOM WITH ME!!{/b}"
        with vpunch
        ec "*Moans* {b}More - Ahhh! Fill me up completely!! AHhiiiyhh!{/b}"
        scene ch6sc07_127 with dissolve
        with vpunch
        "Her body continues to convulse as she feels the warmth of your cum, her tight little pussy keeps squeezing you in pleasure."
        with vpunch
        ec "*Squeals* Aiiiyh- OOhh! Your touch- mmmgh! Your seed- Ahhh! Your love- Mmmh! I feel all of it!"
        scene ch6sc07_128 with dissolve
        ec "*Panting* Mmm... you’ve never... filled me this much before..."
        mc "Mmmh... we both knew that there would be no holding back tonight."
        ec "*Giggles* Are you saying you normally hold back with me?"
        scene ch6sc07_129 with dissolve
        mc "Not at all... I’m merely saying, our bodies knew our intentions... our shared desires."
        scene ch6sc07_128 with dissolve
        ec "Yes... I believe you are right, my love... my champion. My body knew how much I craved you."
        ec "And it made sure I got every last bit of essence you had to give. *Giggles softly*"
        scene ch6sc07_129 with dissolve
        mc "*Inhales* Mmmh... your scent is powerful, you fill the air with the most delicious pheromones after we’ve mated."
        ec "*Moans gently* Ohh... I love it when you smell me, especially when I still have you inside me."
        scene ch6sc07_128 with dissolve
        ec "I wish we could sleep like this tonight... but you must go."
        ec "After our ‘real’ strategy meeting tomorrow, you will be setting out for Arugoh."
        scene ch6sc07_129 with dissolve
        mc "*Inhales* Mmmh... I’m going to miss your scent."
        ec "As I shall miss yours. But you must be well rested for this journey, as I cannot accompany you."
        ec "Kiss me, share your tongue with me before you retire for the night."
        scene ch6sc07_130 with dissolve
        "She pulls you close with her fingers grasping the back of your hair gently."
        "She embraces your lips with an open mouth, inviting your tongue inside to taste hers."
        ec "Mmmh... I love you, [mc]."
        mc "And I love you, Echo."
        ec "Mmmgh... see you at dawn, my love."
        scene ch6sc07_129 with dissolve
        mc "Goodnight, my queen."
        ec "Your queen will fall asleep tonight... with your seed deep inside her. *Giggles*"
        scene ch6sc07_128 with dissolve
        ec "Go, rest well."
        mc "Mmmh... see you in the morning, my A'nu."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        "Echo whimpers softly as you pull out of her, clearly she does not like parting with you for the night."

    else:
        scene black with Dissolve(1.5)
        "After an hour of being pulled around the bonfire, dancing with the girls, you and Pearl retire to your hut, exhausted."
        scene ch6sc02_813 with dissolve
        pl "Mmmh... can’t believe you’re such a good dancer."
        pl "You’ll have to dance with me... one on one... ZzZz soon... zZz."
        scene ch6sc02_881 with dissolve
        "It doesn’t take long for the night to claim you both."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)

    scene ss43 with Dissolve(1.5)
    $ renpy.pause()
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc07_131 with Dissolve(1.5)
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    el "Night night, Borri! Thanks for the help today!"
    al "Sleep well!"
    br "Bah! I couldn’t resist yer offer o’free ale, could I now? Heh!"
    br "Get home safely, lassies!"
    scene ch6sc07_132 with dissolve
    al "Eliza, will you walk me home?"
    al "I’m not a fan of having to walk the streets alone at night... not with those kidnappings we’ve heard about."
    el "Of course I’ll walk you home!"
    scene ch6sc07_133 with dissolve
    el "I dare anyone to attack you when I’m around!"
    el "In fact, I double dare them! *Giggles*"
    al "With you as my escort, I pity anyone who tries!"
    scene ch6sc07_134 with dissolve
    el "Have you heard any news about the kidnappings? We heard about them when we arrived in Luxenford, but it’s been quiet since."
    al "Mmh, two days ago... a student from the Academy went missing."
    el "Oh? Did you know them?"
    al "Not exactly, she is in the advanced history class. Her name is Isabella, though."
    el "Isabella... I’ll keep my ears peeled at the guild in case we get a missing persons contract."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss52 with Dissolve(1.5)
    $ renpy.pause()
    scene ch6sc07_135 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "I’d love to get to the bottom of it. Abducting young women? Disgusting..."
    el "I can only imagine what they must be going through."
    scene ch6sc07_136 with dissolve
    al "Yeah... we’re in the target group as well. Makes me feel uneasy."
    el "Luckily, you’ve got a badass escort! *Giggles*"
    scene ch6sc07_137 with dissolve
    al "*Giggles* True! I feel much better with you around, especially at this hour."
    al "If those kidnappers pick us they’re in for a surprise-"
    scene ch6sc07_138 with dissolve
    el "Hm?"
    al "Eliza? What is it?"
    scene ch6sc07_139 with dissolve
    elt "{i}We must've been followed ever since we departed from the guild...{/i}"
    elt "{i}Good thing we made it to the Academy, I need to get Alice to leave and go to her room...{/i}"
    scene ch6sc07_140 with dissolve
    el "Alice, go to your room and rest... it’s been a long day."
    al "Aren’t you coming? Sabrina made a new recipe of cookies which we could taste-test."
    el "Alice, I don’t have time to taste cookies, my clothes needs a proper wash and I need to get it done."
    al "Oh... okay, I just thought you could finally see my room..."
    al "Maybe another time? Goodnight, and thanks for the escort."
    scene ch6sc07_141 with dissolve
    el "*Sighs* That was a bit mean of me... but I needed her to get out of here."
    el "I’ll make visiting her a priority tomorrow. She’s only shown her room to [mc] and Luna, it’s a big deal to her."
    scene ch6sc07_142 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    el "Time to find out who’s been stalking us."
    play music battle_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc07_142a
    $ renpy.pause(0.3)
    scene ch6sc07_142b
    with vpunch
    $ renpy.pause()
    scene ch6sc07_143 with dissolve
    rit "{i}She vanished.{/i}"
    rit "{i}Did she detect me? ... No, not possible.{/i}"
    scene ch6sc07_144 with dissolve
    with vpunch
    el "*Shouts* Who do you think you’re spying on?!"
    scene ch6sc07_145 with dissolve
    with vpunch
    el "You think you can abduct young girls, huh?! Think again!"
    scene ch6sc07_146 with dissolve
    with vpunch
    ri "*Groans* Unghh!"
    el "Prepare to meet your maker!"
    scene ch6sc07_147 with dissolve
    el "Wait... Rin?!"

    if eliza_relationship == True:
        ri "*Groans* Nnghh... [mc]’s concubine."
        scene ch6sc07_148 with dissolve
        with vpunch
        el "C-Concubine?!"
        el "Who are you calling a concubine?! I’m his girlfriend! Okay?!"
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0

    else:
        ri "*Groans* Nnghh... [mc]’s companion."
        scene ch6sc07_148 with dissolve
        with vpunch
        el "Companion?!"
        el "I’m much more than a ‘companion’! I’m... I’m his best friend and closest ally! Got it?!"
        #play music explore_1 fadein 1.0
        stop music fadeout 1.0

    scene ch6sc07_149 with dissolve
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    ri "*Nods* Mh, okay."
    el "Now, you better come clean and tell me exactly why you were shadowing me and Alice?!"
    scene ch6sc07_150 with dissolve
    ri "[mc]."
    scene ch6sc07_151 with dissolve
    el "Yeah? What about him? I already told him you were in Luxenford."
    ri "Oh."
    scene ch6sc07_150 with dissolve
    ri "[mc], I wish to find him."
    ri "He's adventurer, according to you."
    ri "So, I observe guild. But no [mc]."
    scene ch6sc07_151 with dissolve
    ri "I decide to... follow you. Maybe you lead me to him?"
    scene ch6sc07_152 with dissolve
    el "I see... *Sighs* The reason you haven’t seen him around the guild lately is because he isn’t in Luxenford, currently."
    ri "Where?"
    el "He’s out at sea, helping some friends who found themselves in trouble, and he also has to rescue an ambassador."
    scene ch6sc07_151 with dissolve
    ri "Oh, no [mc]..."
    el "Sorry... but I don’t know for certain when he will be back. Last we spoke, he was making good progress, though."
    scene ch6sc07_150 with dissolve
    ri "Y-You speak to him? How?"
    scene ch6sc07_152 with dissolve
    el "Through the Arcstone he gave me."
    ri "He... gave it to you?"
    el "Yeah? He said you gifted it to him years ago."
    scene ch6sc07_151 with dissolve
    ri "*Nods* Mh."
    scene ch6sc07_150 with dissolve
    ri "Move?"
    el "Oh! Right... sorry. Let’s get up."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc07_153 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "I hope I didn’t hurt you, jumping you like that?"
    ri "*Shakes head* Nh-nh. I am okay."
    ri "*Quietly* [mc]... gone, again."
    el "Hey... it’s going to be okay. He will be home soon, I know he will."
    scene ch6sc07_154 with dissolve
    ri "You, vampire... how?"
    elt "{i}She knows?{/i}"
    ri "Last time... you, not vampire."
    scene ch6sc07_155 with dissolve
    el "*Sighs* It’s a long story... but I am not an ordinary vampire. [mc] purified me and removed the bloodlust."
    scene ch6sc07_154 with dissolve
    ri "Purified vampire. Never known such a thing."
    ri "Certainly within his capabilities."
    scene ch6sc07_155 with dissolve
    el "You know about vampires, Rin? How?"
    scene ch6sc07_154 with dissolve
    ri "Recruited by shadow organization, met vampire."
    ri "Envy, her name."
    scene ch6sc07_156 with dissolve
    el "You speak a little funny."
    ri "*Nods* ..."
    el "I’m sorry, I didn’t mean to pry."
    scene ch6sc07_154 with dissolve
    ri "Mh."
    elt "{i}She’s been speaking in shortened sentences, why though?{/i}"
    scene ch6sc07_155 with dissolve
    el "You said you were in a shadow organization?"
    ri "Mh."
    el "What’s it called? Is it located here in Luxenford?"
    scene ch6sc07_154 with dissolve
    ri "*Shakes head* Nh-nh, Society of Shadows... Assassin’s guild."
    ri "Location, Red mountains."
    scene ch6sc07_156 with dissolve
    el "And they had a vampire as a member? Were you friends?"
    ri "Friends... maybe, not fully."
    ri "She was, somewhat... nice."
    ri "Somewhat, dangerous."
    scene ch6sc07_157 with dissolve
    el "I bet vampires make for excellent assassins?"
    ri "*Giggles lightly* Mh-mh!"
    el "Hey... it’s quite late, why don’t we head back to the tavern I’m staying at?"
    scene ch6sc07_158 with dissolve
    el "We could get some food and talk some more? I’d love to know more about you."
    ri "*Shakes head* Nnh-nh. Have to go."
    scene ch6sc07_159 with dissolve
    el "*Sighs* O-Okay..."
    el "Hey, Rin?"
    scene ch6sc07_160 with dissolve
    ri "Hmm?"
    el "It was nice seeing you again. I hope we can talk some more another time, or when [mc] returns."
    ri "*Nods* Mh."
    ri "Thank you, inviting me ... kind."
    scene ch6sc07_161 with dissolve
    with vpunch
    el "*Gasps* {b}HUH?!{/b}"
    ri "See you."
    scene ch6sc07_162 with dissolve
    el "She’s... so cool."
    scene ch6sc07_163 with dissolve
    el "*Sighs* I can’t believe I met her again, and before [mc] as well."
    el "I definitely prefer a run in with her over those women abductors... although I would’ve loved to kick their asses."
    scene ch6sc07_164 with dissolve
    elt "{i}Next stop, The Drunken Rooster, a warm bath, and my last bloodvial from [mc]...{/i}"
    elt "{i}That means he has to make it back within a week. Maybe a week and a half if I’m able to avoid expending any unnecessary energy.{/i}"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ss12 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc02_881 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "{i}Hmm? It’s not dawn yet...{/i}"
    pl "*Indistinct whimpers* Mngh-nhhh..."

    if pearl_relationship == True:
        scene ch6sc07_165 with dissolve
        pl "Oooohhh..."
        pl "Yes... please... mmh."
        mct "{i}*Chuckles* Sounds like she’s having quite the dream...{/i}"
        scene ch6sc07_166 with dissolve
        mc "Hey... Pearl?"
        pl "Mmmgh..."
        scene ch6sc07_167 with dissolve
        pl "[mc]- nnnghh..."
        pl "Why did you... stop? And why are your pants on?"
        mct "{i}*Chuckles* It’s not hard to figure out what kind of dream she was having...{/i}"
        mc "My pants are still on cause you were dreaming, I woke up to you whimpering."
        scene ch6sc07_168 with dissolve
        pl "Hnngh... just a dream? That’s... disappointing."
        pl "It was one of those dreams you wish were really happening..."
        scene ch6sc07_169 with dissolve
        mc "You’ve got my attention, what was it about?"
        scene ch6sc07_168 with dissolve
        pl "Uh... stuff."
        pl "I can’t remember much..."
        scene ch6sc07_169 with dissolve
        mc "Okay... now want to tell me again, truthfully?"
        pl "..."
        scene ch6sc07_170 with dissolve
        pl "It’s embarrassing..."
        pl "*Sighs* Promise you won’t tell anyone?"
        scene ch6sc07_169 with dissolve
        mc "You know me better than that. Of course I won’t tell anyone."
        scene ch6sc07_170 with dissolve
        pl "O-Okay..."
        scene ch6sc07_171 with dissolve
        pl "Oh! Maybe... instead of just telling it... maybe we could re-enact it?"
        scene ch6sc07_172 with dissolve
        mc "Re-enact it? Hmm... helping my cute little mermaid make her dreams reality?"
        mc "That’s a definite yes."
        pl "Awesome! *Giggles*"
        pl "Oh! And remember... don’t judge a woman by her dreams!"
        scene ch6sc07_173 with dissolve
        mc "You’re keeping me in suspense here..."
        pl "So... in my dream, I was asleep... after the ceremony, and then you came into our hut."
        scene ch6sc07_174 with dissolve
        pl "You saw me... deeply asleep, my body exposed for your viewing pleasure."
        pl "Then... you touched me... caressed my smooth skin, you removed my skimpy clothes..."
        scene ch6sc07_173 with dissolve
        pl "Revealing my naked body. Hardened with lust and the sight of me, you entered me gently."
        pl "And you began mating me carefully to avoid waking me, little by little getting deeper inside me."
        scene ch6sc07_174 with dissolve
        pl "Overcome with desire, and the feeling of my warm and wet little pussy, you eventually stopped holding back and began to fuck me in earnest."
        pl "Obviously, this woke me up... to the feeling of your rock hard cock pounding inside me."
        pl "I had no choice but to moan in pleasure."
        scene ch6sc07_175 with dissolve
        pl "You realized I'd woken up and I was just as excited as you, so we continued to fuck like animals."
        mc "Damn... that is one hell of a dream."
        pl "I know... so, go outside and give me five minutes to fall asleep again."
        pl "Then come back... and turn my dream into reality."
        mc "See you in five."
        scene ch6sc07_174 with dissolve
        pl "*Giggles* See you ..."
        scene black with Dissolve(1.5)
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        $ renpy.pause(0.5)
        "You wait outside for a few minutes before returning. When you enter, you’re greeted with a pleasant view."
        scene ch6sc07_176 with Dissolve(1.5)
        $ renpy.pause(0.5)
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        mct "{i}Damn... I could get used to re-enacting these dreams of hers.{/i}"
        mct "{i}She’s presenting herself perfectly... legs spread, ass perked up, arching her back... breasts squished into the bed.{/i}"
        scene ch6sc07_177 with dissolve
        mct "{i}Her feet are so tiny and cute...{/i}"
        mct "{i}It’s impressive how fast she is on land and in the water with such small feet.{/i}"
        scene ch6sc07_178 with dissolve
        mct "{i}But with thighs like that... it’s no wonder I was driven mad with lust in her dream.{/i}"
        mct "{i}Juicy, plump, smooth... mmh. Oh? Look at that, she loosened her panties enough to give me a glimpse.{/i}"
        scene ch6sc07_179 with dissolve
        mct "{i}What a naughty little mermaid...{/i}"
        mct "{i}Leaving herself exposed like that... her ass available for the first man who walks in here?{/i}"
        mct "{i}Such a little tease... enough to drive any man insane.{/i}"
        scene ch6sc07_180 with dissolve
        mct "{i}I'd better help her get these off... sleeping in her panties will only cause them to get worn-out sooner.{/i}"
        mct "{i}They’re... wet already. What a lustful little woman...{/i}"
        scene ch6sc07_181 with dissolve
        mct "{i}Mmmh... her scent is easy to pick up, almost citrusy.{/i}"
        mct "{i}After the bluekelp experience she gave me back on the ship... she must’ve found another plant to rub around her privates.{/i}"
        scene ch6sc07_182 with dissolve
        mct "{i}What a naughty little pussy she has... so soft and smooth to the touch.{/i}"
        "As Pearl feels your touch against the outer parts of her pussy, she whimpers softly."
        pl "Mmmh..."
        scene ch6sc07_183 with dissolve
        mct "{i}Good girl, keep dreaming your little dream.{/i}"
        "As you put pressure onto her clitoris, her whimper turns to a gentle moan."
        pl "Ohh..."
        mct "{i}Her pussy is dripping wet... her body is so eager to be mated.{/i}"
        scene ch6sc07_184 with dissolve
        mct "{i}But first... let’s get her fully ready, we still have to free her breasts.{/i}"
        mct "{i}What kind of bastard would allow his woman to sleep clothed?{/i}"
        scene ch6sc07_185 with dissolve
        pl "*Whimpers* Nnghh..."
        scene ch6sc07_186 with dissolve
        "You slide your hand under her breast, checking the state of her nipple."
        scene ch6sc07_187 with dissolve
        mct "{i}I love her supple breasts... so perfectly soft- Mmm...{/i}"
        scene ch6sc07_186 with dissolve
        mct "{i}Her nipples are harder than ever before.{/i}"
        scene ch6sc07_187 with dissolve
        pl "*Moans softly* Nnghh... mmmh..."
        scene ch6sc07_186 with dissolve
        mct "{i}I'm looking forward to making these delicious breasts bounce once we begin mating.{/i}"
        scene ch6sc07_188 with dissolve
        mct "{i}But... before we can get to that, I need a taste.{/i}"
        scene ch6sc07_189 with dissolve
        mct "{i}Mmmh... delicious... if any woman is a gourmet meal... it’s her.{/i}"
        "You inhale deeply, taking in the combination of her enticing pheromones and the citrusy scent."
        mct "{i}Just like in her dream... holding back is not an option... I need her.{/i}"
        scene ch6sc07_190 with dissolve
        "You follow her pheromone trail right between her soft cheeks, as they embrace your face with warmth."
        scene pl_lewd49 with dissolve
        $ renpy.pause()
        "With your face buried between her cheeks, there’s only one thing to do, begin tasting."
        "As your tongue reaches her ass, you caress her entrance and Pearl instinctively presses her cheeks against you with each lick."
        pl "*Whimpers* Mmmgh..."
        mct "{i}She's been rubbing her pussy juices all over her ass, mmh... she knows how to rile me up.{/i}"
        mct "{i}Fuck... I can’t get enough of her- Mmmh... what a tasty ass.{/i}"
        pl "*Moans* Ohh... mmmh..."
        scene ch6sc07_190 with dissolve
        "After having thoroughly tasted her juicy ass, it’s time to enjoy her dripping pussy."
        scene ch6sc07_191 with dissolve
        "With your face buried further down between her cheeks, your tongue reaches her lower lips."
        scene pl_lewd50 with dissolve
        $ renpy.pause()
        pl "*Moans gently* Yes... baby... mmh..."
        mct "{i}*Licks* Incredible... her juices mixed with the citrus flavor... she’s driving me crazy.{/i}"
        "Pearl’s body begins to slightly shake, signaling she is about to cum."
        scene ch6sc07_191 with dissolve
        mct "{i}Not yet... not until I’ve had my way with you.{/i}"
        scene ch6sc07_192 with dissolve
        "As you pull your tongue away from her pussy, she whimpers, longing for more."
        mct "{i}Just look at her juicy ass and little pussy... all mine...{/i}"
        mct "{i}It's time to ravage my little mermaid... just like her dream.{/i}"
        scene ch6sc07_193 with dissolve
        mct "{i}Slow penetration at first, careful not to wake her...{/i}"
        scene pl_lewd51 with dissolve
        $ renpy.pause()
        mct "{i}Mmh... just as- ahhh... just as tight as I remember her to be.{/i}"
        pl "*Moans softly* Mmmh... b-baby..."
        mct "{i}Five hells... every dip inside her is driving my desire up- I need more!{/i}"
        scene pl_lewd52 with dissolve
        $ renpy.pause()
        with vpunch
        pl "*Moans* Ohh! Mmm... so deep- mmm..."
        "Overcome with desire for her soaking wet little pussy, you thrust deeper and begin mating her."
        mct "{i}Fucking her like this is incredible... she knows how to position her ass perfectly.{/i}"
        scene pl_lewd53 with dissolve
        $ renpy.pause()
        pl "*Moans* Hnngh... w-what’s happening? Ahhh... I’m..."
        pl "*Moans* I’m being taken?! Aaiihh- Oh! A handsome and lust filled man is fucking me while I sleep! Ahh!"
        pl "*Gasps* I’m being held down?! Mmmgh! I-I can’t even stop him! Ahhh!"
        with vpunch
        mc "There’s no stopping, not until you give me what I want... Mmgh!"
        with vpunch
        pl "*Moans loudly* Yes!! I-I mean, no! Mmgh! Oh, baby!"
        with vpunch
        pl "I’m going to- Ahhh! I can’t believe I’m cumming while being ravaged by such a lewd man! {b}AHhH!{/b}"
        scene ch6sc07_194 with dissolve
        with vpunch
        pl "*Squeals in pleasure* Aiiyh-Ahh! Seas!! You’re deep! {b}MMHH!{/b}"
        scene ch6sc07_195 with dissolve
        pl "*Giggles* Look at that ... my night time intruder is none other than the man I love!"
        mc "You're my woman, it's my pleasure to make your dreams real."
        scene ch6sc07_196 with dissolve
        pl "*Moans softly* Mmmh... you certainly did."
        pl "From now on, I want you to fuck me whenever you desire ... okay?"
        pl "It doesn't matter if I’m bathing, eating, dancing, drinking, or sleeping. Fuck me whenever you want."
        pl "There’s nothing that turns me on more than waking up to being fucked by you."
        scene ch6sc07_197 with dissolve
        mc "I promise, nothing will hold me back from fucking you, not now... not ever."
        scene ch6sc07_196 with dissolve
        pl "Good... then seal it with a kiss."
        pl "Kiss me like only a man who loves his woman can kiss her."
        scene ch6sc07_198 with dissolve
        pl "Mmmghh! Mmmh..."
        mc "I love your perfect lips... so soft."
        scene ch6sc07_199 with dissolve
        pl "Baby... mmffhm... feels like your desire for me hasn't been quenched."
        pl "That won’t do... we need to get you inside of me, right away..."
        mc "Mmmh... get down on your knees and present me with your ass."
        scene ch6sc07_200 with dissolve
        pl "Like this? Is this how you want your little mermaid?"
        mc "That’s exactly how I want you."
        scene ch6sc07_201 with dissolve
        mc "Seeing you like this is increasing my desire like nothing else ..."
        scene pl_lewd54 with dissolve
        $ renpy.pause()
        pl "*Gasps* Ohh... I like this... I like the feeling of your big cock rubbing between my cheeks."
        mc "Mmmh... your cheeks are perfect for this: firm but still supple."
        pl "I know... Mmmh... I feel it just as you do- Mmmh... I want you, [mc]!"
        mc "You’re craving my cock again?"
        scene pl_lewd55 with dissolve
        $ renpy.pause()
        mc "Then you shall have it. Mmh..."
        pl "Y-Yes... Aahh... I crave it!"
        pl "Stop teasing me..."
        mc "I’ll stop when you tell me how badly you want it."
        with vpunch
        pl "I really want it!"
        mc "You’re begging for my cock?"
        with vpunch
        pl "Yes! Aahh... I’m begging for your big cock! Please! Go deeper!"
        pl "Fuck my wet little pussy like you own it! As you always do! MMm!"
        scene pl_lewd56 with dissolve
        $ renpy.pause()
        mc "Fuck that little pussy is good... a little slice of heaven- Mmmh..."
        pl "So... biiiiig... mmgh! I can’t believe we’ve been fucking so much on this trip! Mm!"
        pl "I need to thank Kira for suggesting I should go with you on this journey. Ahhh..."
        mc "We’ll both thank her... it wouldn’t have been the same without my mermaid."
        pl "[mc]... fuck my little pussy!"
        scene pl_lewd57 with dissolve
        $ renpy.pause()
        pl "*Whimpers* Seas... mmgh... you love how tight I am...?"
        mc "I do- MMmh... it’s driving me crazy."
        pl "Then fuck me harder! Fuck me like the little slut I want to be for you!"
        mc "Mmgh... I love when you’re like this... okay, no holding back."
        scene pl_lewd58 with dissolve
        $ renpy.pause()
        with vpunch
        pl "*Gasps* AAaHhh! Oh! {b}OH!!{/b}"
        pl "*Moans* Fuck yes! Fuck me! Hnngh!! Have your way with me!"
        pl "*Moans* Ahh-Ah! Aiiyh! Breed me like one of the natives! [mc]! Ah!"
        with vpunch
        pl "Aahhh! J-just like that... force me to cum all over your big cock- Aaahhh..."
        scene pl_lewd59 with dissolve
        $ renpy.pause()
        mc "*Moans* Mmgh... I’m getting close, if you keep sucking me with your pussy like this, I can’t hold back."
        with vpunch
        pl "I don’t want you to hold baaaack- Mmghh! Ahh! [mc]- I’m cumming!"
        with vpunch
        pl "{b}Creampie me!{/b} Ahhh! Fill me up! {b}OHH!!{/b}"
        scene ch6sc07_202 with dissolve
        mc "Five hells... that little pussy of yours sure knows how to drain me."
        pl "How do I look, baby? ... With your cum dripping out of my pussy?"
        mc "Like an incredibly rare piece of art."
        pl "*Giggles softly* Ohh... how I wish I could see what you see!"
        scene ch6sc07_203 with dissolve
        pl "I like feeling it inside me... a token of your love."
        pl "Mmmgh... give me a moment to get cleaned up."
        scene black with Dissolve(1.5)
        $ renpy.pause(0.5)
        "Pearl runs over to her bedding where she has a rag lying, she wipes herself off and approaches you once more."
        scene ch6sc07_204 with dissolve
        pl "Now..."
        pl "It’s time for round three."
        scene ch6sc07_205 with dissolve
        mc "*Chuckles* What?"
        mc "You can’t be serio-"
        scene ch6sc07_206 with dissolve
        pl "Round..."
        pl "Three."
        mc "*Chuckles* You’re crazy..."
        scene ch6sc07_207 with dissolve
        pl "*Moans* Mmmh... it's driving me crazy not having your cock inside me..."
        "As Pearl mounts you, she locks both of your legs in place, ensuring you won’t be able to stop her."
        mc "MMmh... be a good little slut and take what you want, then."
        scene ch6sc07_208 with dissolve
        pl "*Moans* Aahh... I will! I'm going to get every last drop out of you tonight- Mmmh!"
        mc "Aahhh... fuck..."
        scene pl_lewd60 with dissolve
        $ renpy.pause()
        mc "H-Haa... Damn, you’re so tight... and warm..."
        mc "This is-"
        pl "*Moans* Too good to handle? We’re both living out our dreams! Mmh..."
        pl "You’re not getting away from me... not tonight. Aahhh... your cock belongs to me!"
        scene pl_lewd61 with dissolve
        $ renpy.pause()
        mc "Aaaaahhh .... fuck ...."
        pl "Do you like seeing me all sweaty as I work your cock inside me? Mmm..."
        mc "Yeah ... Hnngh, I do ... seeing you covered in sweat from our mating is incredible."
        scene pl_lewd62 with dissolve
        $ renpy.pause()
        pl "Did you ever..."
        pl "In all of your life..."
        pl "Imagine a woman’s pussy could feel as good as mine? NNnghh..."
        mc "Never... mmh... but thanks to you, I’ve been able to experience such a divine pussy."
        scene pl_lewd63 with dissolve
        $ renpy.pause()
        pl "*Moans* Good... good."
        pl "You better remember... how divine my pussy feels. Mmmh!"
        pl "*Moans* Just like I'll remember how godly your cock feels inside of me!"
        pl "*Whimpers* Forever..."
        mc "Fuck... I will, I will think about this little juicy pussy of yours for the rest of my life."
        pl "You’re close... so am I... mmgh... let us climax together. Aaahhh..."
        scene pl_lewd64 with dissolve
        $ renpy.pause()
        pl "*Moans* Aaahh..."
        mc "Fuck... riding me like this... you’re not giving me a choice... mmmgh."
        pl "*Moans softly* I'm going to suck you dry with my little pussy. Nnnh-mmh... I'm going to empty your balls."
        with vpunch
        pl "Aaahh! Yes, that’s it! Fuck my pussy!"
        pl "You’re deeper than ever before. Aahhnhh... K-Keep fucking me!"
        pl "Fuck me hard! MMmh!"
        scene pl_lewd65 with dissolve
        $ renpy.pause()
        mc "*Moans* Hnngh... I’m as deep as I can go. Fuck... every thrust sends pleasure through my entire body..."
        pl "Mmm... good..."
        pl "*Moans* Oh, [mc]... I feel you... I feel-"
        with vpunch
        pl "{b}*Gasps loudly* AAHHH! YESS!! CUM WITH ME!!{/b}"
        with vpunch
        mc "*Moans* Hnngh! {b}Fuuuuck!{/b}"
        scene ch6sc07_209 with dissolve
        pl "MMgh! Yes! Fill me up with your warm cum!"
        mc "*Moans* Aaahh!"
        scene ch6sc07_210 with dissolve
        pl "*Panting softly* Nnnh... drenched in sweat... filled with your cum... you know how to treat a woman. *Giggles*"
        mc "I aim to please."
        pl "And please me you did... you treat me so well."
        scene ch6sc07_211 with dissolve
        pl "Mmmgh... I love you."
        scene ch6sc07_212 with dissolve
        pl "I love you so damn much!"
        scene ch6sc07_211 with dissolve
        mc "As I love you... Pearl, my little mermaid."
        scene ch6sc07_212 with dissolve
        pl "I’m so happy we’re together... being with you... it brings me joy..."
        scene ch6sc07_211 with dissolve
        pl "*Mwah* Nnnghh... I’ve never felt as happy to be alive as when we’re together."
        scene ch6sc07_212 with dissolve
        pl "Tongue. I want to taste your tongue while you're inside me."
        scene ch6sc07_213 with dissolve
        pl "Mmmgh... thank you- *Licks* for making me your woman."
        mc "Mmm... you’re welcome... *Lick*"
        scene ch6sc07_211 with dissolve
        pl "Mmmgh... we should probably... get some rest..."
        scene ch6sc07_212 with dissolve
        mc "Yeah... still a few hours until dawn."
        scene ch6sc07_213 with dissolve
        pl "*Licks* Mmmh... totally... sleep sounds good... *Lick*"
        scene ch6sc07_211 with dissolve
        pl "Good night baby... thank you for making my dream a reality."
        mc "Sweet dreams... and know that it wasn’t just your dream, it became mine as well."
        scene ch6sc07_212 with dissolve
        pl "You always know how to charm me..."
        pl "And remember... I belong to you. If you ever desire me when I’m sleeping, do whatever you want to me..."
        mc "I promise, I won’t hold back... same goes for you."
        scene ch6sc07_211 with dissolve
        pl "*Kiss* Mmm... noted! Mmm... o-okay, seriously... goodnight!"
        scene black with Dissolve(2.5)
        $ renpy.pause(0.5)
        "Pearl hops over to her own bed after cleaning up, and she falls asleep right away from exhaustion."
        scene ch6sc02_881 with Dissolve(2.5)
        $ renpy.pause(0.5)
        mct "{i}*Chuckles* My regeneration can barely keep up with her sexual appetite.{/i}"
        mct "{i}But I wouldn’t change her for anything, she’s amazing as she is.{/i}"
        mct "{i}I need to be up in a few hours to meet Kisha at the training area... better get some rest.{/i}"


    else:
        scene ch6sc02_881 with dissolve
        mct "{i}*Chuckles* Sounds like she’s having quite the dream... I'd better get some more rest as well.{/i}"
        mct "{i}I need to be up in a few hours to meet Kisha at the training area...{/i}"

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "A couple of hours of rest later..."
    scene ch6sc02_813 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "{i}Mmm...{/i}"
    mct "{i}It’ll be dawn soon, I better go meet Kisha for our one on one...{/i}"
    scene ch6sc02_883 with dissolve
    mct "{i}At least the fresh and cool air here makes it easy to wake up.{/i}"
    scene ch6sc02_885 with dissolve
    mct "{i}Echo asked me to stop by her chambers at dawn to discuss the Arugoh tribe.{/i}"
    scene ch6sc02_883 with dissolve
    mct "{i}Hopefully, whatever Kisha has in mind won’t take too long.{/i}"
    scene ch6sc07_214 with dissolve
    mct "{i}Great... doesn’t look like she’s even here yet.{/i}"
    scene ch6sc07_215 with dissolve
    $ renpy.pause(0.5)
    scene ch6sc07_216 with dissolve
    $ renpy.pause(0.5)
    mct "{i}She even made a big deal about me not being late at the ceremony last night.{/i}"
    mct "{i}And now she’s the one who’s late! *Chuckles* Women...{/i}"
    scene ch6sc07_217 with dissolve
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    mct "{i}Huh? Behind me!{/i}"
    scene ch6sc07_218 with dissolve
    play music battle_3 fadein 1.0
    #stop music fadeout 1.0
    ks "Pay better attention to your surroundings, hunter!"
    mct "{i}When did she arrive? I didn’t feel her presence at all when I got here.{/i}"
    scene ch6sc07_219 with dissolve
    ks "You noticed me too late..."
    scene ch6sc07_220 with dissolve
    ks "First male hunter in A’nai... slayer of Jimun... you’ll have to defeat me if you want such prestige!"
    mct "{i}Huh? She can infuse her weapon?"
    ks "*Quietly* {size=-10}{b}Javelin of Gaia, aim true as you always have.{/b}{/size}"
    scene ch6sc07_221 with dissolve
    ks "Champion, if you survive this battle, I will see you as a worthy hunter..."
    scene ch6sc07_222 with dissolve
    with vpunch
    ks "Hyyiiah!"
    mct "{i}Time to test the earth-affinity the necklace gave me.{/i}"
    scene ch6sc07_223 with dissolve
    mct "{i}*Inhales* Feel it... manifest it to my will... it’s now or never!{/i}"
    scene ch6sc07_224 with dissolve
    with vpunch
    $ renpy.pause(1)
    scene ch6sc07_225 with dissolve
    mct "{i}That was close.{/i}"
    mct "{i}Her spear pierced solid rock... Impressive.{/i}"
    scene ch6sc07_226 with dissolve
    mct "{i}It’s disintegrating? Hmm... when she infuses it, it probably loses its material form and becomes pure magic.{/i}"
    scene ch6sc07_227 with dissolve
    mct "{i}Which means she can most likely only infuse one at a time.{/i}"
    scene ch6sc07_228 with dissolve
    with vpunch
    ks "You should know to pay attention to your opponent during battle!"
    mc "Onyx, you’re up!"
    scene ch6sc07_229 with dissolve
    with vpunch
    ks "It was interesting having a man around again... but if you can’t defeat me, you aren’t fit to rule our people!"
    ###Skillscheck###
    if leadership >= 17:
        ks "You may have proven yourself a capable leader during the hunt-"
        ks "-But that is not enough to become the A'khan! Show me your worth!"

    else:
        pass

    scene ch6sc07_230 with dissolve
    with vpunch
    ks "Aaagh! W-What?!"
    scene ch6sc07_231 with dissolve
    ks "What manner of dark magic is this?!"
    ks "R-Release me, you demon!"
    mc "You really should keep your eyes on your opponent."
    scene ch6sc07_232 with dissolve
    $ renpy.pause(0.5)
    scene ch6sc07_233 with dissolve
    $ renpy.pause(0.5)
    scene ch6sc07_234 with dissolve
    with vpunch
    mc "This demon isn’t done with you just yet, pay attention!"
    mct "She’s incredibly agile."
    mct "She dodged my kick when she's still stuck in Onyx’s grasp...?"
    "Her unexpected agility, combined with the force of throwing herself backwards, allows Kisha to slip from Onyx’s grasp."
    scene ch6sc07_235 with dissolve
    ox "Master! I lost her!"
    "As your kick flies by Kisha, you hit the rock you conjured earlier, sending it flying into the jungle."
    scene ch6sc07_236 with dissolve
    ks "*Quietly* {size=-10}{b}He’s good...{/b}{/size}"
    ks "*Quietly* {size=-10}{b}He blocked my Javelin of Gaia, and even managed to stop my direct assault...{/b}{/size}"
    scene ch6sc07_237 with dissolve
    ks "*Quietly* {size=-10}{b}But can he handle me if I get close?{/b}{/size}"
    scene ch6sc07_238 with dissolve
    with vpunch
    mc "*Groans* Hnnrh?! Kisha we’re going to-"
    ks "Hniiiyah! You think you can defeat me with a single kick? Don’t insult me!"
    "With the advantage of surprise, and the force with which she jumps on you, you lose your balance and both of you go tumbling."
    scene ch6sc07_239 with dissolve
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    with vpunch
    mc "*Groans* Hnnghh... five hells, Kisha..."
    play music explore_2 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc07_240 with dissolve
    ks "Sorry... I... I got carried away."
    ks "As a huntress, letting my emotions get the better of me during battle like that... it is a great dishonor."
    scene ch6sc07_241 with dissolve
    ks "Huh?! Y-You’re grabbing my ass?!"
    mc "You’re the one who landed on top of me."
    scene ch6sc07_242 with dissolve
    with vpunch
    ks "You dare blame me for this... this seduction attempt?!"
    scene ch6sc07_243 with dissolve
    ks "Only the A’khan is permitted to touch me! To seduce me! Grrrh!"
    scene ch6sc07_242 with dissolve
    mc "I wasn’t trying to seduce you, you’re the one who jumped me!"
    scene ch6sc07_243 with dissolve
    ks "Your words are hollow, champion!"
    scene ch6sc07_242 with dissolve
    ks "Do you not find me attractive?"
    scene ch6sc07_243 with dissolve
    ks "Is my body not desirable to you?"
    ####Choice####
    menu:
        "You are... desirable. ({color=#ff8cdd}Romance{/color})":
            mc "You are desirable... incredibly so."
            mc "Your sleek and athletic body is a work of art."
            $ ks_path = True
            scene ch6sc07_239 with dissolve
            with vpunch
            "While she’s taken aback by your compliment, you grab her ass once more and pull her close."
            ks "*Gasps* Aahh!"
            ks "Touching me again...?"
            scene ch6sc07_240 with dissolve
            ks "How can you be so bold with me?"
            ks "I should kill you for this."
            mc "You can’t, and you won't attempt to do so, either."
            scene ch6sc07_239 with dissolve
            mc "Because we both believe I am the man who will become the A’khan. And you desire to belong to that man... to me."
            ks "Nonsense! Nnnh... I desire no man..."
            scene ch6sc07_240 with dissolve
            mc "Then why have you been rubbing yourself against me ever since we fell?"
            mc "Why else were you so eager to test my worth? It's because you desire me."
            mc "And you want to feel justified in that desire, even though I have not claimed the title yet."
            scene ch6sc07_245 with dissolve
            ks "S-Shut up! Mmghh!"
            "Kisha can’t take any more of it, so she hurriedly attempts to stop the flow of your words with her lips."
            scene ch6sc07_246 with dissolve
            ks "You’re such- Mmmh... such a... man."
            mc "You’re an incredible woman... mmmh... you’ve earned my desire."
            scene ch6sc07_245 with dissolve
            ks "Q-Quiet... mmmgh... stop speaking to me like this. Stop seducing me... Mmgh!"
            mc "You're the one with your tongue in my mouth- Mmmh..."
            scene ch6sc07_246 with dissolve
            mc "This perky ass of yours is driving me insane."
            $ ks_trust += 3
            ks "You like my ass? Mmmgh... I knew I had felt your gaze... Mmmh..."
            "Kisha enjoys your boldness with her, making her feel feminine. Her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            ###Skillscheck###
            if leadership >= 17:
                ks "*Licks eagerly* Mmgh... I've never known a man such as you..."
                ks "Bold-... mmh... confident... honesty... *Licks* a proper leader- Mmmh..."
                ks "Nobody's around to see us- Mmmgh... maybe... maybe it would be okay if-"
            else:
                pass

            scene ch6sc07_245 with dissolve
            "You feel Kisha pull back, her tongue leaving your mouth and her lips withdrawing as if suddenly realizing what she is doing."
            scene ch6sc07_244 with dissolve
            with vpunch
            ks "N-No! No more! G-Get up! My body is only for the A’khan!"
            ks "S-Stand up and wipe that smirk off your face!"

        "Get off me, woman! (Neutral)":
            scene ch6sc07_243 with dissolve
            mc "Will you get off me already!"
            scene ch6sc07_244 with dissolve
            with vpunch
            $ ks_path = False
            mc "I’m not interested in you."
            ks "As if I’m interested in you, either?! Get up!"

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc07_247 with Dissolve(1.5)
    $ renpy.pause(0.5)
    ks "..."
    mc "So, call it a tie?"
    scene ch6sc07_248 with dissolve
    ks "A tie... for now."
    scene ch6sc07_249 with dissolve
    ks "Come... join me, if you wish."
    "You follow Kisha over to the edge of the arena. To your surprise, she sits down and beckons you to join."
    scene black with Dissolve(1)
    $ renpy.pause(0.5)
    scene ch6sc07_250 with Dissolve(1)
    $ renpy.pause(0.5)
    ks "Looks like dawn is upon us..."
    ks "Ask your questions, you must be curious."
    ks "I shall be nothing but truthful, you have earned that much."
    scene ch6sc07_251 with dissolve
    mc "Okay, well... I’ll start with the obvious question, then..."
    mc "You’re not a mage or sorceress as far as I can sense, how come you’re able to infuse your spear with magic?"
    scene ch6sc07_252 with dissolve
    ks "Gaia."
    ks "I am blessed by our goddess."
    scene ch6sc07_253 with dissolve
    ks "As one of A’nai’s top huntresses, I earned her favor... I received her blessing the year before the great desecration."
    ks "*Sighs* But even with her blessing, I was not enough to fight off the outsider's relentless attacks."
    scene ch6sc07_251 with dissolve
    mc "Wait... you’re saying you were already a renowned huntress the year before the desecration?"
    mc "But that was two decades ago? You don’t look a day over 30?"
    scene ch6sc07_252 with dissolve
    ks "I was 26 summers when I received Gaia’s blessing."
    ks "Which makes me 46, today."
    scene ch6sc07_251 with dissolve
    mc "Has her blessing stopped you from aging? I thought blessings from gods were only temporary."
    scene ch6sc07_254 with dissolve
    ks "I do not know the rules, but my body has remained young and strong ever since that day."
    ks "I am not ageless, however, I do feel myself getting older. Just... much slower than my fellow huntresses."
    ks "Marah and I are actually the same age, but she looks like you'd expect a woman in her mid forties to look."
    scene ch6sc07_253 with dissolve
    ks "Whereas my body remains sleek, agile, filled with energy and everything else you associate with youth."
    scene ch6sc07_251 with dissolve
    mc "Interesting..."
    scene ch6sc07_255 with dissolve
    ks "According to the teachings of our ancestors, when great warriors arise, the goddesses will bless them."
    ks "And not the regular kind of blessings that we would usually receive, but something greater."
    scene ch6sc07_254 with dissolve
    ks "That is what was bestowed on me, after fighting off three beasts that had surrounded a child one night."
    ks "Gaia must’ve deemed me worthy, even though I only did what any other huntress would’ve."
    scene ch6sc07_252 with dissolve
    ks "Ever since then, my aging... my senses, and my ability to turn any object I hold into Gaia’s Javelin, have remained with me."
    scene ch6sc07_251 with dissolve
    mc "Putting yourself at risk to save one of A’nai’s children... she must’ve decided to permanently grant you that blessing."
    mc "From what I know about gods and blessings, they usually temporarily grant them to devotees."
    mc "But doing so takes away some of their personal power. When the blessing dissipates, that power returns to them."
    mc "So for you to be granted a permanent blessing is pretty huge."
    scene ch6sc07_255 with dissolve
    ks "Yes, it is not something I take lightly."
    scene ch6sc07_254 with dissolve
    ks "Using Gaia’s Javelin as I did just now, takes its toll on my body..."
    scene ch6sc07_255 with dissolve
    ks "I will probably need to rest and recover for a few days. That is the price of using it."
    scene ch6sc07_251 with dissolve
    mct "{i}She just revealed a crucial weakness? She must have decided to trust me.{/i}"
    scene ch6sc07_255 with dissolve
    ks "[mc]... champion. May I ask about your abilities as well?"
    ks "You defeated Jimun with such ease... you've completed some trials already, and just now you held your own duelling me."
    ks "Have you... also been blessed by the gods?"
    scene ch6sc07_251 with dissolve
    mc "Not quite..."
    mc "But I am not a regular man."
    scene ch6sc07_255 with dissolve
    ks "*Scoffs lightly* I think we are all aware of that fact."
    scene ch6sc07_256 with dissolve
    mc "What I mean is... I’m not fully human, only half."
    "Kisha's eyes widen, but she knows you're being truthful with her."
    mc "I am half angel... that heritage grants me a wide array of abilities."
    mc "And the more I battle and take down tough opponents, the stronger those abilities become."
    scene ch6sc07_254 with dissolve
    ks "Angel? ... I do not know of such a creature."
    scene ch6sc07_253 with dissolve
    ks "But I can’t deny their existence, not after seeing everything you have done."
    scene ch6sc07_255 with dissolve
    ks "So, did you grow stronger from our duel?"
    scene ch6sc07_251 with dissolve
    mc "Not really. Although I did learn a little about my newly gained earth-affinity and how to control it."
    scene ch6sc07_255 with dissolve
    ks "You only gained that ability recently?"
    scene ch6sc07_251 with dissolve
    mc "Yeah, when I wore Malpheon’s talisman for the first time, the essence within it infused me with it."
    mc "I could feel myself grow more powerful."
    mc "And I suddenly felt a new affinity for earth magic, and developed an understanding of your ancestors' language."
    scene ch6sc07_255 with dissolve
    ks "You’re becoming more interesting by the second..."
    ks "And you were born like this, and not blessed by the gods? Truly strange."
    scene ch6sc07_252 with dissolve
    ks "Perhaps... you really are the one who's destined to restore A’nai and lead our people..."
    ks "Echo certainly believes so."
    scene ch6sc07_251 with dissolve
    mc "I don’t really buy into the whole destiny thing... but I will become your A’khan."
    mc "That is something tangible I can relate to."
    scene ch6sc07_255 with dissolve
    ks "*Scoffs lightly* You're certainly confident... I’m almost starting to believe your words."
    scene ch6sc07_251 with dissolve
    mc "*Chuckles* I would love to win you over on faith alone, but I know a woman like you needs something... more."
    mc "That is why I don’t expect you to declare your allegiance until I become the A’khan."
    scene ch6sc07_252 with dissolve
    ks "You... seem to understand me."
    ks "Peculiar... refreshing."
    scene ch6sc07_253 with dissolve
    ks "Thank you for sitting with me, but..."
    scene ch6sc07_255 with dissolve
    ks "Now, you must go meet with Echo. I do not wish to delay you from your mission."
    scene ch6sc07_251 with dissolve
    mc "Thank you as well, Kisha... for trusting me and letting me get to know you a little better."
    ks "*Nods* Mh."
    scene ch6sc07_252 with dissolve
    ks "But if you tell anyone... I’ll hunt you."
    ks "Now, go, do not keep our A’nu waiting."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "On your way to see Echo, you come across Zyra and Suji."
    scene ch6sc05_124 with Dissolve(1.5)
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    mct "{i}Look who’s up already.{/i}"
    mct "{i}*Chuckles* They had quite a few of those Jungle-jingles last night, and still they’re up early.{/i}"
    scene ch6sc05_114 with dissolve
    mct "{i}Maybe I’ll go say hi. After all, I won’t see them for a while after I set out today.{/i}"
    scene ch6sc05_115 with dissolve
    "However, as you approach the two huntresses, you overhear them talking."
    zy "Did you hear? Another outsider..."
    sj "Mhm, I did... the nightshift guards were talking about it when they passed outside my hut last night."
    zy "I heard it’s another male... do you... do you believe they're going to try to compete with [mc] for the title of A’khan?"
    sj "It is unknown to me... but they will never be able to match [mc]. Never."
    zy "So many outsiders in such a short amount of time... what is the cause of this?"
    scene ch6sc05_116 with dissolve
    mc "*Clears throat* Morning ladies."
    sj "[mc]! Good morning to you too!"
    scene ch6sc05_117 with dissolve
    zy "H-Hey, [mc], yes... good morning to you as well."
    scene ch6sc05_118 with dissolve
    mc "What’s this I hear about another outsider? Another man?"
    mc "You think I’ve got competition?"
    scene ch6sc05_117 with dissolve
    zy "No! I-I do not believe any man could come close to you!"
    scene ch6sc05_119 with dissolve
    with vpunch
    mc "Then why do you look so worried?"
    zy "*Gasps* Aahhh! [mc]!"
    scene ch6sc05_120 with dissolve
    zy "*Whispers* {size=-10}{b}You’re so close... mmh...{/b}{/size}"
    scene ch6sc05_121 with dissolve
    sj "Keep tickling her! Get all her worries out of her system!"
    scene ch6sc05_122 with dissolve
    mc "You know... I think Suji is right, we need to get this out of your system."
    scene ch6sc05_123 with dissolve
    with vpunch
    zy "*Gasps and laughs* Aiiyh! Hahah! N-No!"
    scene ch6sc05_122 with dissolve
    mc "What do you know about this outsider?"
    scene ch6sc05_123 with dissolve
    zy "*Giggles* N-Nothing! Heheh! We only overheard guards talkiiiiii- "
    scene ch6sc05_122 with dissolve
    mc "And you’re worried they might want to compete with me?"
    scene ch6sc05_123 with dissolve
    zy "*Giggles* N-No more, I beg of you! Heheh! It was foolish of me to worryyyyy!"
    scene ch6sc05_122 with dissolve
    mc "There we go. Don’t you feel so much better now that we got that out of your system?"
    scene ch6sc05_120 with dissolve
    zy "*Whispers* {size=-10}{b}Mmm... so much better, my body feels at peace... in your hands.{/b}{/size}"
    scene ch6sc05_121 with dissolve
    sj "*giggles* Looks like we’ve finally found a way to reel Zyra in when she’s being outrageous."
    sj "We may just have to keep you around, Champion."
    scene ch6sc05_116 with dissolve
    mc "*Chuckles* Sounds good to me. Now, if you ladies will excuse me... I’ve got a meeting with Echo."
    sj "Good luck! I’m sure the two of you will come up with a great plan on how to proceed with the last trial."
    mc "I’m sure we will."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "You proceed up the many stairs to Echo’s personal chambers."
    scene ch6sc02_889 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mct "{i}There she is. Hopefully, I didn’t keep her waiting too long.{/i}"
    scene ch6sc02_890 with dissolve
    ec "*Quietly* {size=-10}{b}Intruding here... foolish.{/b}{/size}"
    scene ch6sc02_891 with dissolve
    mc "Hey-"
    scene ch6sc02_892 with dissolve
    with vpunch
    ec "Hyyah! Nobody sneaks up on the A’nu and lives!"
    mc "Echo! It’s me!"
    scene ch6sc02_893 with dissolve
    ec "[mc]?! You- you’re here?"
    ec "I... {b}I almost killed you!{/b}"
    ec "Again!"
    scene ch6sc02_894a with dissolve
    ec "W-What have I done? I attacked the man I lov-"
    ec "That was so reckless of me..."
    scene ch6sc02_895 with dissolve
    ec "*Exhales deeply* Sorry... I did not mean to charge you like that."
    ec "I’m a bit on edge this morning..."
    mct "{i}Looks like she’s heard about the other outsider as well.{/i}"
    scene ch6sc02_897 with dissolve
    mc "This is about the new outsider, isn’t it?"
    scene ch6sc02_898 with dissolve
    ec "Yes."
    scene ch6sc02_896 with dissolve
    ec "Wait- you know about that?"
    scene ch6sc02_897 with dissolve
    mc "Not much. I just heard something about the situation from Suji and Zyra."
    scene ch6sc02_898 with dissolve
    ec "Marah came to me this morning. She told me about a man that she caught snooping in here while we were gone."
    ec "Here... {b}in my personal chambers...{/b} rummaging in my stuff."
    scene ch6sc02_896 with dissolve
    ec "That is why I am on edge. I could not sleep after hearing another man had been in here!"
    ec "[mc], I’m so sorry."
    scene ch6sc02_899 with dissolve
    mc "Hey... don’t you dare apologize for defending yourself, especially at a time like this."
    ec "Mgh-mhm-mggh!"
    mc "I don’t want to hear it, okay? First of all, you can’t actually harm me with that little dagger."
    scene ch6sc02_900 with dissolve
    mc "Secondly, I expect my queen to be capable and fierce when I’m not around."
    mc "It calms my nerves, knowing you can handle yourself."
    scene ch6sc02_901 with dissolve
    ec "You... you always know what to say."
    ec "*Scoffs lightly* I suppose it does seem a bit silly charging you with a small dagger."
    ec "After everything I've witnessed you accomplish, my dagger wouldn't even tickle you..."
    scene ch6sc02_903 with dissolve
    mc "The only way for you to harm me, would be to betray my trust."
    scene ch6sc02_906 with dissolve
    ec "Please... don’t ever speak of such a thing."
    ec "I would rather forfeit my own life... than do that."
    scene ch6sc02_907 with dissolve
    mc "I know, we both know the bond we share."
    scene ch6sc02_905 with dissolve
    ec "It truly is an incredible bond we’ve built, isn’t it?"
    scene ch6sc02_904 with dissolve
    mc "It is... it’s a rare thing to connect with another human on such a level."
    scene ch6sc02_901 with dissolve
    ec "The goddesses truly do favor us then."
    ec "Come, join me for a drink?"
    scene ch6sc02_903 with dissolve
    mc "After nearly being mauled by my queen? A drink seems in order."
    scene ch6sc02_908 with dissolve
    ec "Keep teasing me, and you might get mauled again."
    mc "*Chuckles* Oh, the horror!"
    ec "*Snickers* Shut up..."
    scene ch6sc02_909 with dissolve
    ec "Sit down already and have a drink with me!"
    scene ch6sc02_910 with dissolve
    ec "This is an old bottle, from before the desecration. It came from the mainland."
    mc "Many alcoholic drinks actually get better with age."
    scene ch6sc02_911 with dissolve
    mc "Alcohol and women have that in common."
    ec "*Giggles* ..."
    scene ch6sc02_912 with dissolve
    ec "Is that so? Women get better with age as well?"
    ec "Good thing I’m older than you then. *Snickers lightly*"
    mc "Only by a few years."
    scene ch6sc02_913 with dissolve
    ec "It’s enough to make me your senior, and according to you, more attractive! *Giggles*"
    ###skill-check####
    if charisma >= 15:

        scene ch6sc02_914 with dissolve
        mc "No man could deny your attractiveness..."
        ec "Charmer."
    else:
        pass

    scene ch6sc02_916 with dissolve
    ec "Mmm, I’ve looked forward to tasting this one for years... now I finally have an occasion."
    scene ch6sc02_917 with dissolve
    ec "Hopefully I’m not just praising it and then it turns out to be a regular wine."
    scene ch6sc02_918 with dissolve
    mc "There’s only one way to find out."
    ec "I suppose you’re right."
    scene ch6sc02_919 with dissolve
    ec "What should we drink to, my champion?"
    mc "Let’s toast to us, the soon-to-be joint rulers of A’nai."
    scene ch6sc02_918 with dissolve
    ec "J-Joint rulers? I... I like that. Are you sure?"
    mc "Echo, I’m not here to claim some title just to remove you from power..."
    mc "If you are to become my queen, I’d want to rule together."
    mc "And you know I have to return to the mainland, so I need my queen to do what she does best in my absence."
    scene ch6sc02_919 with dissolve
    ec "You truly keep surprising me... a man willing to share power with a woman."
    ec "I will drink to that. Us ruling together."
    scene ch6sc02_920 with dissolve
    bth "Cheers! Mmmh..."
    scene ch6sc02_921 with dissolve
    mc "That’s... surprisingly sweet? I can barely taste the alcohol."
    scene ch6sc02_922 with dissolve
    ec "I am pleased with it, better than I dared hope for."
    scene ch6sc02_923 with dissolve
    mc "Yeah, sweet drinks are dangerous... it's too easy to get drunk on those."
    scene ch6sc02_924 with dissolve
    ec "What is life without a little danger? *Giggles*"
    scene ch6sc02_926 with dissolve
    ec "[mc], what you just said... I want you to know, it means a great deal to me."
    ec "It is tradition that the A’nu takes a back seat once an A’khan is elected."
    scene ch6sc02_922 with dissolve
    ec "Do you really wish to change that tradition? It's a tradition that favors you."
    scene ch6sc02_921 with dissolve
    mc "Echo, it’s not like I’m losing anything. I’m still going to be their leader, with you at my side."
    scene ch6sc02_923 with dissolve
    mc "This way, we get the best of both worlds."
    scene ch6sc02_922 with dissolve
    ec "You really are nothing like other men... you actually care."
    scene ch6sc02_921 with dissolve
    mc "I believe this approach gives A’nai the best of both sides."
    mc "Their current ruler will remain in charge. Someone they already respect and know is more than capable."
    mc "And they also gain the male leader that they have been longing for. A new protector and provider for the tribe."
    scene ch6sc02_922 with dissolve
    ec "I have longed for that... we all have."
    scene ch6sc02_926 with dissolve
    ec "I thank the goddesses every night for bringing you into our lives."
    scene ch6sc02_923 with dissolve
    mc "So, we agree? We’ll be joint rulers, equal partners?"
    scene ch6sc02_927 with dissolve
    ec "Yes! I accept you as my equal partner!"
    ec "I do not wish anyone else to be my partner... to be my A’khan."
    scene ch6sc02_928 with dissolve
    mc "And I would never accept anyone but you, Echo... as my queen and my A’nu."
    scene ch6sc02_929 with dissolve
    ec "I can’t believe we’re going to change an age old tradition..."
    scene ch6sc02_930 with dissolve
    ec "But together, I believe we can do anything."
    ec "A lot of things have already changed since you arrived."
    scene ch6sc02_931 with dissolve
    mc "True, what’s one little ruling tradition in comparison? *Chuckles*"
    scene ch6sc02_930 with dissolve
    ec "*Snickers* Exactly..."
    scene ch6sc02_932 with dissolve
    with vpunch
    ec "*Groans* Argh! I just know Marah is going to be a total monkeyturd about this!"
    scene ch6sc02_933 with dissolve
    ec "She already dislikes you, and she is all riled up about the new outsider."
    ec "When she hears this...?"
    scene ch6sc02_932 with dissolve
    ec "*Groans* By the goddesses! Why can’t she just untie her panties and let me be happy!"
    mc "*Chuckles* Does she even wear panties?"
    scene ch6sc02_934 with dissolve
    ec "*Snickers* I do not know. I just thought of that on the spot, out of frustration."
    mc "*Chuckles* ..."
    ec "Maybe you’ll find out when you become A’khan?"
    scene ch6sc02_931 with dissolve
    mc "*Chuckles* How so?"
    scene ch6sc02_930 with dissolve
    ec "As the A’khan, Marah will be committed to you."
    ec "She will likely seek you out to mate with you."
    scene ch6sc02_931 with dissolve
    mct "Great... I doubt that, though."
    mct "She is just as likely to pull out a blade and try to gut me."
    mc "Echo, I’ve heard that before, from the others... about the A’khan mating with the entire tribe."
    mc "How does that work?"
    scene ch6sc02_926 with dissolve
    ec "It is the highest honor for a woman of A’nai to mate with her A’khan."
    ec "And it is the A’khan’s right and privilege to mate with any female of his choosing."
    scene ch6sc02_922 with dissolve
    ec "It is, however, the A’nu who has first mating and breeding rights, for obvious reasons."
    scene ch6sc02_921 with dissolve
    mc "Yeah I kind of understood that part already. What I meant to know is... are you all sisters then?"
    mc "There’s some big age gaps amongst your people."
    scene ch6sc02_922 with dissolve
    ec "Some are sisters or cousins, but most aren’t."
    ec "You see, one A’khan breeding with all the women is how it was in the old days."
    scene ch6sc02_926 with dissolve
    ec "But my father... our most recent A’khan, the one who was killed in the great desecration..."
    ec "He wanted to build stronger ties to outsiders."
    scene ch6sc02_930 with dissolve
    ec "So, father decided to only mate with my mother."
    ec "He allowed outsiders to visit and potentially breed with our other women."
    scene ch6sc02_929 with dissolve
    ec "But only if our women accepted their interest."
    ec "Over time, this made the bloodlines of A’nai more diverse."
    scene ch6sc02_926 with dissolve
    ec "And for a while it seemed to be working well, our relationships and trade with outsiders grew."
    ec "But sometimes, our women would decline an outsider for whatever reason."
    scene ch6sc02_922 with dissolve
    ec "And this rejection caused resentment to build up amongst some of them."
    scene ch6sc02_926 with dissolve
    ec "Eventually, some outsiders became aggressive and forced themselves upon our women."
    ec "When father learned of this, he was furious and revoked the arrangement."
    scene ch6sc02_929 with dissolve
    ec "As you can imagine, this did not sit well with the outsiders."
    ec "They'd grown accustomed to having their ‘exotic’ women."
    ec "Soon after, the volume of trade reduced quickly, and we heard little more from the outsiders for a while."
    scene ch6sc02_926 with dissolve
    ec "Until they came back... and the great desecration happened. You know the rest."
    scene ch6sc02_925 with dissolve
    mc "Echo... I’m sorry, I wasn’t trying to pry or bring up old wounds."
    scene ch6sc02_927 with dissolve
    ec "You have not caused any wounds... my peoples past isn’t without tragedy."
    ec "But to never speak of it? To not remember them or what happened to them?"
    ec "That would be a dishonor to them and their memory."
    scene ch6sc02_929 with dissolve
    ec "So, there is your answer. Usually, the A’khan breeds with all of his women as he desires."
    ec "My father wanted to do something different, and attempted to brighten our future by doing so."
    scene ch6sc02_926 with dissolve
    ec "He could not have foreseen the horrors it would lead to... the greed and lust of the outsiders."
    ec "Once you're the A'khan, it will be up to you how you lead our people."
    scene ch6sc02_931 with dissolve
    mct "{i}Damn, I can definitely understand why they are so against outsiders.{/i}"
    mct "{i}Which means, once I become the A’khan... all of them will be mine.{/i}"
    mct "{i}I mean, I sort of knew this already... but it’s nice to have it fully explained.{/i}"
    scene ch6sc02_928 with dissolve
    mc "Don’t worry, Echo, I don’t intend to bring in outsiders or have your women breed with other men."
    mc "I haven't yet decided how I want to handle it. But just know, I won’t be throwing your people to the wolves."
    scene ch6sc02_927 with dissolve
    ec "I already had confidence you wouldn't."
    ec "But... it pleases me to hear you say it."
    ec "How do you think you'll lead us? The old way of breeding and mating all your women yourself?"
    ec "Or a similar way to my father? Single out the women you personally desire, and leave the rest?"
    scene ch6sc02_928 with dissolve
    mc "Hmm..."
    ####Choice####
    menu:
        "Ancestor's approach. ({color=#ff8cdd}Harem{/color})":
            mc "I feel like your ancestor's had a good thing going, your father changing that didn't go well."
            mc "Besides, I don't share my women, I'm greedy like that."
            $ harem_path = True
            scene ch6sc02_927 with dissolve
            ec "Once you become A'khan, you can be as greedy as you want, we'll all be yours."
            ec "I agree, the old way worked for centuries, I believe it is the best solution."
            $ ec_trust += 5
            "Echo favored your choice to include all of A'nai as your harem, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."

        "Farther's approach. ({color=#ff8cdd}Individual selection{/color})":
            mc "I feel like your father was on to something."
            mc "I'm not saying I'm going to open A'nai to outsiders and allow them to come here for mating anyone."
            mc "I will mate with those of you whom I care for and desire."
            mc "The rest, we'll see how to deal with once the time comes."
            scene ch6sc02_927 with dissolve
            ec "Mhm, I think that's a wise choice."
            ec "There's no rush on figuring the matter out, we can play it by ear."
            $ ec_trust += 2
            "Echo likes that you're willing to try her father's approach, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

        "Undecided. (Neutral)":
            mc "Hmmm... I'm honestly not sure as of right now."
            mc "I've just been focused on the task before me, completing the trials and finding the Ambassador."
            mc "I haven't given much thought as to what my role as A'khan would be."
            scene ch6sc02_927 with dissolve
            ec "It is definitely a cumbersome burden, the weight of a whole people, on your shoulders..."
            ec "Now you know what I feel on the daily. *Scoffs*"

    scene ch6sc02_934 with dissolve
    ec "I believe we’re heading into the dawn of a new age for A’nai."
    ec "An age of prosperity and good fortune."
    scene ch6sc02_931 with dissolve
    mc "You and I will do the best we can to brighten A’nai’s future."
    "Echo traces the tip of her finger across her soft lips, slightly wet from her drink."
    scene ch6sc02_939 with dissolve
    ec "Come, join me on my bed."
    scene ch6sc02_940 with dissolve
    mc "As my queen commands."
    ec "..."
    scene ch6sc02_941 with dissolve
    ec "It is time to strategize, I wish to do so comfortably."
    scene ch6sc02_942 with dissolve
    mc "I’m not one to argue against comfort."
    scene ch6sc02_495 with dissolve
    ec "Being comfortable is paramount to think clearly! *Giggles*"
    scene ch6sc02_496 with dissolve
    mc "Yeah... thank you for the drink, by the way."
    scene ch6sc02_497 with dissolve
    ec "There’s no one else I’d rather share it with."
    ec "Sit with me."
    scene ch6sc02_498 with dissolve
    mc "So, the Arugoh tribe... what should I know?"
    scene ch6sc02_510 with dissolve
    ec "As you know, they were once women of A’nai."
    scene ch6sc02_511 with dissolve
    ec "They harbor no love for outsiders. Imagine them as a tribe filled with Marahs."
    scene ch6sc02_512 with dissolve
    ec "It won’t be easy for you. I believe they have smaller factions."
    scene ch6sc02_513 with dissolve
    ec "Their tribe is generally more combat oriented and aggressive, as you’ve seen."
    scene ch6sc02_510 with dissolve
    ec "You will likely have to prove yourself. To display enough strength to make them submit."
    ec "They... they sometimes shipwreck sailors and capture any survivors."
    scene ch6sc02_509 with dissolve
    mc "Why would they capture the survivors?"
    mc "Oh..."
    scene ch6sc02_513 with dissolve
    ec "Yes. They will breed with the survivors until they become too weak and exhausted to continue."
    ec "Then they kill them and discard their bodies."
    scene ch6sc02_514 with dissolve
    ec "They’ve become so damn extremist! Ugh!"
    scene ch6sc02_510 with dissolve
    ec "In their eyes, this is what was done to us."
    ec "So, this is the consequences of that act and they feel justified in doing the same back to outsiders."
    scene ch6sc02_513 with dissolve
    ec "I know you can handle yourself... but it still worries me."
    ec "I know how they will treat you."
    scene ch6sc02_514 with dissolve
    ec "If they... If they dare touch you! I’m going to-"
    scene ch6sc02_509 with dissolve
    mc "Hey, they’re in for a rude awakening."
    scene ch6sc02_508 with dissolve
    ec "I suppose you will come as quite the shock."
    scene ch6sc02_507 with dissolve
    ec "I’m glad I’ve witnessed your greatness in action."
    ec "It eases the heaviness in my heart."
    scene ch6sc02_506 with dissolve
    mc "I’ll be back before you have time to miss me."
    scene ch6sc02_499 with dissolve
    ec "That is impossible... for I already miss you."
    scene ch6sc02_498 with dissolve
    mc "I promise, I have no intention of being gone for long."
    mc "Remember Eliza? The woman I told you about back home?"
    scene ch6sc02_500 with dissolve
    ec "I do! I hope to meet her one day!"
    ec "She sounds like a great woman."
    scene ch6sc02_498 with dissolve
    mc "She is. And her wellbeing is dependent on me getting back to her."
    mc "So, nothing will stop me from returning."
    scene ch6sc02_507 with dissolve
    ec "Then I will not delay you any further..."
    scene ch6sc02_508 with dissolve
    ec "Your best way to get into their village will be to let them capture you."
    ec "Let them believe you are just a regular man... until you decide it’s advantageous to educate them otherwise."
    scene ch6sc02_513 with dissolve
    ec "If you are captured by them, they'll think you're entering on their terms and their guard will be down."
    ec "Whereas, if you just bust down their gates, they will attack and you will be forced to kill them."
    scene ch6sc02_511 with dissolve
    ec "You know full well how I feel about that."
    scene ch6sc02_513 with dissolve
    ec "If your hand is forced, do what you must... but please, attempt to make them submit instead."
    ec "If we are able to bring them back under A’nai’s rule, it would strengthen us all."
    scene ch6sc02_506 with dissolve
    mc "Echo, I give you my word. I will do what I can to reunite the tribes."
    ec "*Nods* Mh."
    scene ch6sc02_507 with dissolve
    ec "O-Okay. Then you should probably head out."
    ec "It's roughly five hours travel through the jungle to the north."
    scene ch6sc02_508 with dissolve
    ec "I’m sorry, but I cannot send anyone to accompany you..."
    ec "They would know something is up if we do."
    scene ch6sc02_506 with dissolve
    mc "Don’t worry."
    mc "I’ll be fine... traverse north for five hours, get captured, and win them over with my charm."
    scene ch6sc02_500 with dissolve
    ec "Don’t charm them too much! Only a little, okay?"
    scene ch6sc02_498 with dissolve
    mc "*Chuckles* As my queen wishes."
    scene ch6sc02_516 with dissolve
    mh "*Clears throat* ..."
    scene ch6sc02_517 with dissolve
    mh "Isn’t this rich? A’nu, what are you doing letting this outsider into your chamber after what you learned this morning?!"
    mh "You’re really this blinded by him? You know they are conspiring to dominate us!"
    scene ch6sc02_520 with dissolve
    mh "That's right, your little innocent act is over. We have caught your friend and he was happy to talk."

    if mh_charm == True:
        mh "You may walk around here with your big cock and handsome body enslaving the minds of our youth..."
        mh "But I'm not falling for it, I know what hides behind your beautiful face! Tsk!"
        mct "*Chuckles* Does she realise she's complimenting me?"

    else:
        pass

    if harem_path == True:
        mh "I bet you even want to turn A'nai into your own personal harem, don't you!?"
        mh "Guess what, I'm part of the tribe, and I refuse to get on my knees and gag on that big cock of yours!"
        mh "Our youth might be easily impressed by you, but that isn't the case with me! Tsk!"

    else:
        pass

    scene ch6sc02_521 with dissolve
    ec "Marah, enough!"
    ec "I have warned you about this aggression towards [mc]. Do not make me repeat myself."
    mct "{i}If looks could kill. Fucking hag...{/i}"
    mct "{i}If she doesn't give up this idea of me being the enemy, I'll have to dominate her.{/i}"
    scene ch6sc02_523 with dissolve
    mh "The prisoner knew [mc] by name... how do you explain that?"
    mh "This is a repeat of the past... send in a few to win us over, and then dominate us when our guard is down!"
    scene ch6sc02_524 with dissolve
    mh "I will die before I let a man put me in chains again."
    scene ch6sc02_525 with dissolve
    ec "I do not know how he knows [mc]’s name... but [mc] is not here to repeat the past."
    scene ch6sc02_521 with dissolve
    mc "I only came here with Pearl."
    mc "I have no idea who this individual is, or how they know my name."
    scene ch6sc02_523 with dissolve
    mh "Yes, you would claim such a thing... wouldn’t you? Tsk!"
    mh "We shall find out, right now. You are not leaving A’nai before this is settled."
    scene ch6sc02_524 with dissolve
    mh "Both of you, come. We shall go see the prisoner."
    ec "*Sighs* I’m sorry, [mc]. Let’s just get this over with."
    mc "Whatever, I’ll be happy to clear this up."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    "You and Echo follow Marah down to the dungeons below the temple."
    scene ch6sc02_526a with Dissolve(1.5)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    mc "*Whispers* {size=-10}{b}If she tries anything this time... I’ll defend myself.{/b}{/size}"
    ec "*Whispers* {size=-10}{b}I know, but she’s promised not to do anything foolish after what happened last time.{/b}{/size}"
    mc "*Whispers* {size=-10}{b}Somehow, I find that hard to believe...{/b}{/size}"
    scene ch6sc02_527a with dissolve
    ec "*Whispers* {size=-10}{b}Shh, let us give her the benefit of the doubt.{/b}{/size}"
    ec "*Whispers* {size=-10}{b}Anyway, I am anxious to learn about how another outsider found A’nai.{/b}{/size}"
    ec "*Whispers* {size=-10}{b}Especially one who claims to know you.{/b}{/size}"
    scene ch6sc02_528 with dissolve
    mh "Isn’t it obvious? They’re in cahoots."
    mh "As soon as we let our guards down, we’ll be the ones locked up down here... again."
    scene ch6sc02_529 with dissolve
    mh "Tsk! I’ll be damned if I'll allow such a fate to happen again."
    mh "You hear me? ‘Champion’ ... your mind tricks won’t work on me."
    scene ch6sc02_532 with dissolve
    mh "Everything will be revealed to us, and your trickery will be no more."
    mc "I’m not trying to trick you... when will you get that through your thick skull?"
    scene ch6sc02_533 with dissolve
    mh "*Scoffs* As if I’d just take your word for it. The word of an outsider... of a man..."
    ec "Did you bring us down here for petty insults? [mc] is due to set out for Arugoh."
    scene ch6sc02_535 with dissolve
    mh "*Laughs* Arugoh? Him? Hahah!"
    mh "That would be a sight to see!"
    scene ch6sc02_536 with dissolve
    mh "Too bad I shan’t be there to witness your beheading... once they’re done... ‘using’ you. *Scoffs*"
    mh "But I shall sleep like a babe tonight, knowing your fate is sealed."
    scene ch6sc02_537 with dissolve
    mh "Now, come. It is time you and your friend are reunited."
    mh "I, for one, cannot wait to hear what excuses you will throw our way."
    scene ch6sc02_538 with dissolve
    mh "Even our lovely and naive A’nu won’t be able to deny your treachery."
    scene ch6sc02_541 with dissolve
    with vpunch
    ec "Enough! Marah, cease this behavior or-"
    mh "Or what? Are you threatening me over this outsider?"
    scene ch6sc02_542 with dissolve
    mh "Does this man’s corruption really run so deep?"
    scene ch6sc02_541 with dissolve
    with vpunch
    ec "[mc] is {b}not{/b} an outsider, he is one of {b}US!{/b} You will start treating him as such."
    ec "Should you continue with this inhospitable behavior and the snarky remarks towards either of us..."
    ec "I will remove you as High-Priestess. We have plenty of others that would love to take on such a role."
    scene ch6sc02_542 with dissolve
    mh "Echo... you can’t be serious? Over this outsider?"
    scene ch6sc02_540 with dissolve
    mh "[mc], or whatever your name is... come."
    scene ch6sc02_538 with dissolve
    mh "Your friend is in the cage back here."
    scene ch6sc02_526a with dissolve
    ec "Please... ignore her unpleasantries..."
    mc "Trust me, I learned to deal with unpleasant people a long time ago."
    scene ch6sc07_257 with dissolve
    mh "Here he is!"
    mh "I’m sure you can understand, you will not be granted any mercy once the truth comes out!"
    scene ch6sc07_258 with dissolve
    with vpunch
    ed "What have you done to my daughter?! Why have you brought her to these savages!"
    ed "I will kill you for this!"
    scene ch6sc07_259 with dissolve
    mc "Lord Edward?"
    with vpunch
    ed "Don’t look so dumbfounded! Where is my sweet Kelly?! What have you done to her?!"
    scene ch6sc07_260 with dissolve
    ec "[mc]? What is going on? You know this man?"
    scene ch6sc07_261 with dissolve
    mh "I told you... your friend here has told us all about how  you abducted his precious daughter!"
    mh "That is what you men like to do, imprison us and use us as you please. Imagine what he has done to this man’s daughter!"
    scene ch6sc07_262 with dissolve
    ec "You are only listening to one side of the story, the side of a completely unknown outsider."
    ec "Yet, you are so happy to take his word for this? I do not believe [mc] is guilty of that."
    scene ch6sc07_261 with dissolve
    mh "Then why doesn’t your precious ‘champion’ tell us his side?"
    ed "He kidnapped my daughter and has corrupted her against her own family! That’s what this man does!"
    scene ch6sc07_263 with dissolve
    ec "[mc], please, share your side with us?"
    ec "There’s no doubt in my soul that either this man is lying, or there has been a large misunderstanding."
    scene ch6sc07_264 with dissolve
    ec "He is clearly emotionally distraught and believes what he is saying, but I know you will be truthful with me."
    ec "So, please... let us get this cleared up."
    scene ch6sc07_265 with dissolve
    mc "*Sighs* Sure... I’m getting sick of this man following me."
    mc "So, this goes back a couple of months at this point..."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch4sc08_007 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mc "I had secured a voyage across the Cerulean Sea. The captains of this vessel turned out to be-"
    mc "-renowned pirates. Kira, and her twin sister, Pearl. Whom you’ve already gotten to know."
    ec "Oh? This is how you met Pearl?"
    scene ch4sc9_009 with dissolve
    mc "Yeah, and one of their crew, a young woman named Kelly, had gone missing just before we were due to depart."
    mc "So Kira and Pearl tasked me to find her and bring her back before we set sail."
    scene ch4sc9_013 with dissolve
    mc "So, I tracked down the man who had taken her."
    mc "And imagine my surprise when I learned-"
    scene ch4sc9_015 with dissolve
    mc "-that her kidnapper was none other than her own father. This man: Lord Edward."
    scene ch4sc9_035 with dissolve
    mc "So, I tracked down the location of their hideout and eliminated his guard."
    scene ch4sc9_036 with dissolve
    mc "Kelly quickly told me what had happened and said she was being held against her will."
    scene ch4sc9_044 with dissolve
    mc "I took her to her mother, to let her know her daughter was safe and unharmed."
    mc "After which, we both returned to the ship and set out. I thought that would be the end of it."
    scene ch4sc16_116 with dissolve
    mc "However, I underestimated how deranged her father is. He's convinced that we took Kelly against her will."
    mc "So, he joined forces with Kira and Pearl’s father to amass a small fleet to ambush us with."
    scene ch4sc16_138 with dissolve
    mc "After I had dealt with their ships, I assumed that would be the last we’d see of him."
    scene ch4sc16_177 with dissolve
    mc "But clearly, this man is both a fool and hard-headed."
    scene ch6sc07_265 with dissolve
    mc "How he ended up here on Aruna? I’ve got no idea."
    mc "He is the one who kidnapped his own daughter, but somehow he firmly believes I'm at fault."
    scene ch6sc07_264 with dissolve
    ec "I see... so it is all a big misunderstanding on this man’s behalf."
    ec "Thank you for sharing this with us."
    scene ch6sc07_266 with dissolve
    with vpunch
    mh "*Scoffs* Clearly a one-sided tale, conjured by a sick man who abducts women from their own families!"
    mh "This man told me everything, how you turned his own wife and daughter against him."
    mh "I’ve seen with my own eyes how easily women fall to your corruption!"
    scene ch6sc07_267 with dissolve
    ec "Marah! Cease this hostility at once! [mc] is not corrupting any minds."
    ec "If anyone has lost their mind, it is you! Clouded by your hatred of the past."
    mh "A’nu-"
    with vpunch
    ec "{b}NO.{/b} [mc] has just opened up to us about what really happened."
    ec "You will accept the truth, and you'd best start to put the past behind you."
    mh "Ugh!"
    scene ch6sc07_265 with dissolve
    mc "We’re done here. Echo, would you give us a moment? ... I’ll be out in a few."
    "Echo locks eyes with you, slightly surprised, but she nods in agreement."
    scene ch6sc07_264 with dissolve
    ec "I’ll wait for you outside, then."
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    scene ch6sc07_268 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mh "What? You wish to have your way with me without her present?"
    ####Choice####
    menu:
        "Threaten her. ({color=#fc584c}Intimidation{/color})":
            scene ch6sc07_269 with dissolve
            with vpunch
            mh "*Groans* Uurrghh! Nnghhrrhh!"
            mh "I knew you were an evil bastard!"
            scene ch6sc07_270 with dissolve
            with vpunch
            mc "I don’t give two fucks what you think I am. *Tightens grip*"
            mc "But let’s get one thing clear... Marah."
            scene ch6sc07_271 with dissolve
            mc "I just told you the truth about this man, and what actually transpired."
            mc "Whether or not you believe it, that is up to you."
            scene ch6sc07_272 with dissolve
            mh "*Groans* Hrrghh..."
            mc "So, I will only say this once."
            scene ch6sc07_271 with dissolve
            mc "I like it here. I’ve come to like many of the good people in A’nai."
            mc "My respect for them is the only reason I’ve allowed your antics to go on for as long as they have."
            scene ch6sc07_272 with dissolve
            mc "But that stops now."
            mc "You see, I have people back home who I care for... deeply."
            scene ch6sc07_271 with dissolve
            mc "And your attitude is delaying my reunion with them. This is the last time I'll allow you to delay me."
            mc "Next time? I will show you what real evil looks like."
            scene ch6sc07_272 with dissolve
            with vpunch
            mc "{b}AM I BEING CLEAR?{/b}"
            scene ch6sc07_273 with dissolve
            mh "*Coughs* hrrh... hrrh! Y-Yes!"
            scene ch6sc07_274 with dissolve
            mh "*Gasps* W-What?! Your eyes... you’re d-devil! A demon!"
            scene ch6sc07_275 with dissolve
            mc "Not quite... I’m something else entirely."
            scene ch6sc07_275a with dissolve
            mc "Something much worse."
            mc "So... for the sake of your people, do not delay me again."
            scene ch6sc07_276 with dissolve
            mc "Because, if you force my hand, I will descend upon your little village."
            mc "And the cute little horrors of your past, will pale in comparison to what I have in mind for you."
            scene ch6sc07_277 with dissolve
            mh "I... hrrgh... I won’t stand in your way again."
            mh "Just... don’t hurt any of our people, we’ve been through enough."
            scene ch6sc07_276 with dissolve
            mc "It seems we have come to an understanding... good."
            mc "I much prefer the diplomatic solution, where we’re allies."
            scene ch6sc07_277 with dissolve
            mh "Hrrh... you will only achieve such a thing... Hhhr... by becoming A’khan."
            scene ch6sc07_275a with dissolve
            mc "That is exactly what I intend to do."
            mc "Tell me, what do your instincts tell you in this moment?"
            mh "Hnngh... that you... that you will become our A'khan. Nnnh..."
            "You successfully made Marah submit to you by intimidating her into reason, your {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch6sc07_275 with dissolve
            mc "Good chat, Marah."
            scene ch6sc07_278 with dissolve
            mc "See you around."
            mh "*Coughs* hhrhgh... hhrh..."
            scene ch6sc07_279 with dissolve
            $ intimidation += 2
            mh "He... he spared me?"
            mh "Have I been terribly wrong in my beliefs? ... No, I couldn’t have! Could I?"
            scene ch6sc07_280 with dissolve
            mh "He’s terrifying... yet, when he held me just now... I could feel it."
            mh "He wasn’t really trying to hurt me... he... he was trying to protect A’nai by scaring me into submission."
            scene ch6sc07_279 with dissolve
            mh "He can’t possibly be the one our legends speak of? Can he?"
            mh "The savior of A’nai, the true leader and protector that we so desperately crave..."
            scene ch6sc07_280 with dissolve
            mh "Winning the trust of our people, protecting them from dangers, uncovering our lost temples..."
            mh "Meeting our goddesses, conquering their trials... even I... can’t deny his perseverance."
            scene ch6sc07_281 with dissolve
            mh "His touch... was warm, like the heat from a campfire... embracing my neck."
            mh "That was not the touch of a man trying to hurt me. I know that kind of touch all too well."
            mh "[mc]’s touch was different... his words stern and harsh, but his touch... powerful, yet kind?"
            mh "A powerful man like [mc] as our A'khan... we'd never have to fear outsiders again..."
            scene ch6sc07_282 with dissolve
            mh "What am I even saying? ... *Sighs* I must ask the goddesses for guidance."
            mh "My human mind is too weakened by his presence to make sense of this..."

        "Talk her down. ({color=#2bff8b}Persuasion{/color})":
            if persuasion >= 12:
                mc "Marah just listen-"
                mh "No! I won't hear your filthy lies! Your words are venom-"
                scene ch6sc07_269 with dissolve
                with vpunch
                mh "*Groans* Uurrghh! Nnghhrrhh!"
                mh "I knew you were an evil bastard!"
                scene ch6sc07_270 with dissolve
                with vpunch
                mc "Shut up for a minute..."
                mc "I'm not trying to hurt you, just calm yourself and fucking listen for once."
                scene ch6sc07_272 with dissolve
                mc "Are you ready to listen?"
                mh "Hhrhh! Speak then!"
                mc "Look at me."
                scene ch6sc07_273 with dissolve
                mh "Hrrrmm?"
                scene ch6sc07_275 with dissolve
                mc "Look at my eyes."
                scene ch6sc07_275a with dissolve
                mc "Now you know I'm being serious."
                scene ch6sc07_273 with dissolve
                $ renpy.pause(0.5)
                scene ch6sc07_274 with dissolve
                $ renpy.pause(0.5)
                mh "Hhhh?? W-What are you?"
                mc "What I am is an ally, I'm not here in A'nai with intent to harm anyone."
                mc "I have someone at home I care about, and in order to get back..."
                mc "I have to find this Ambassador, which landed me here in A'nai, now undertaking the trials."
                mc "I have proven myself time and time again, and I will finish the last trial, becoming your A'khan."
                scene ch6sc07_276 with dissolve
                $ renpy.pause(0.5)
                mc "You mean a great deal to Echo, so stop getting in my way, or I will be forced to hurt you."
                mc "If you don't like me, that's fine, but you will accept me as one of your own, once I claim the title."
                scene ch6sc07_274 with dissolve
                $ renpy.pause(0.5)
                "Marah has sensed something within you, she believes your words to be truthful... your {b}{color=#2bff8b}Persuasion{/color}{/b} was successful!"
                mh "I-... *Sighs* I understand."
                mh "You're not our enemy, I-... I was wrong about you."
                mc "I'm glad we cleared that up, I'm going to release you now."
                scene ch6sc07_278 with dissolve
                $ renpy.pause(0.5)
                mc "See you around Marah, I hope it will be as an ally going forward."
                mh "*Coughs* hhrhgh... hhrh..."
                scene ch6sc07_279 with dissolve
                mh "He... he spared me?"
                mh "Have I been terribly wrong in my beliefs? ... No, I couldn’t have! Could I?"
                scene ch6sc07_280 with dissolve
                mh "He’s terrifying... yet, when he held me just now... I could feel it."
                mh "He wasn’t really trying to hurt me... he... he was trying to protect A’nai by revealing himself to me."
                mh "He wanted me to feel him... feel that he was genuine."
                scene ch6sc07_279 with dissolve
                mh "He can’t possibly be the one our legends speak of? Can he?"
                mh "The savior of A’nai, the true leader and protector that we so desperately crave..."
                scene ch6sc07_280 with dissolve
                mh "Winning the trust of our people, protecting them from dangers, uncovering our lost temples..."
                mh "Meeting our goddesses, conquering their trials... even I... can’t deny his perseverance."
                scene ch6sc07_281 with dissolve
                mh "His touch... was warm, like the heat from a campfire... embracing my neck."
                mh "That was not the touch of a man trying to hurt me. I know that kind of touch all too well."
                mh "[mc]’s touch was different... his words stern and harsh, but his touch... powerful, yet kind?"
                mh "A powerful man like [mc] as our A'khan... we'd never have to fear outsiders again..."
                scene ch6sc07_282 with dissolve
                mh "What am I even saying? ... *Sighs* I must ask the goddesses for guidance."
                mh "My human mind is too weakened by his presence to make sense of this..."


            else:
                mc "Marah just listen-"
                "Your persuasion was too low to make Marah listen."
                mh "No! I won't hear your filthy lies! Your words are venom-"
                scene ch6sc07_269 with dissolve
                with vpunch
                mh "*Groans* Uurrghh! Nnghhrrhh!"
                mh "I knew you were an evil bastard!"
                scene ch6sc07_270 with dissolve
                with vpunch
                mc "I don’t give two fucks what you think I am. *Tightens grip*"
                mc "But let’s get one thing clear... Marah."
                scene ch6sc07_271 with dissolve
                mc "I just told you the truth about this man, and what actually transpired."
                mc "Whether or not you believe it, that is up to you."
                scene ch6sc07_272 with dissolve
                mh "*Groans* Hrrghh..."
                mc "So, I will only say this once."
                scene ch6sc07_271 with dissolve
                mc "I like it here. I’ve come to like many of the good people in A’nai."
                mc "My respect for them is the only reason I’ve allowed your antics to go on for as long as they have."
                scene ch6sc07_272 with dissolve
                mc "But that stops now."
                mc "You see, I have people back home who I care for... deeply."
                scene ch6sc07_271 with dissolve
                mc "And your attitude is delaying my reunion with them. This is the last time I'll allow you to delay me."
                mc "Next time? I will show you what real evil looks like."
                scene ch6sc07_272 with dissolve
                with vpunch
                mc "{b}AM I BEING CLEAR?{/b}"
                scene ch6sc07_273 with dissolve
                mh "*Coughs* hrrh... hrrh! Y-Yes!"
                scene ch6sc07_274 with dissolve
                mh "*Gasps* W-What?! Your eyes... you’re a d-devil! A demon!"
                scene ch6sc07_275 with dissolve
                mc "Not quite... I’m something else entirely."
                scene ch6sc07_275a with dissolve
                mc "Something much worse."
                mc "So... for the sake of your people, do not delay me again."
                scene ch6sc07_276 with dissolve
                mc "Because, if you force my hand, I will descend upon your little village."
                mc "And the cute little horrors of your past, will pale in comparison to what I have in mind for you."
                scene ch6sc07_277 with dissolve
                mh "I... hrrgh... I won’t stand in your way again."
                mh "Just... don’t hurt any of our people, we’ve been through enough."
                scene ch6sc07_276 with dissolve
                mc "It seems we have come to an understanding... good."
                mc "I much prefer the diplomatic solution, where we’re allies."
                scene ch6sc07_277 with dissolve
                mh "Hrrh ... you will only achieve such a thing... Hhhr... by becoming A’khan."
                scene ch6sc07_275a with dissolve
                mc "That is exactly what I intend to do."
                mc "Tell me, what do your instincts tell you in this moment?"
                mh "Hnngh... that you... that you will become our A'khan. Nnnh..."
                scene ch6sc07_275 with dissolve
                mc "Good chat, Marah."
                scene ch6sc07_278 with dissolve
                mc "See you around."
                mh "*Coughs* hhrhgh... hhrh..."
                scene ch6sc07_279 with dissolve
                mh "He... he spared me?"
                mh "Have I been terribly wrong in my beliefs? ... No, I couldn’t have! Could I?"
                scene ch6sc07_280 with dissolve
                mh "He’s terrifying... yet, when he held me just now... I could feel it."
                mh "He wasn’t really trying to hurt me... he... he was trying to protect A’nai by scaring me into submission."
                scene ch6sc07_279 with dissolve
                mh "He can’t possibly be the one our legends speak of? Can he?"
                mh "The savior of A’nai, the true leader and protector that we so desperately crave..."
                scene ch6sc07_280 with dissolve
                mh "Winning the trust of our people, protecting them from dangers, uncovering our lost temples..."
                mh "Meeting our goddesses, conquering their trials... even I... can’t deny his perseverance."
                scene ch6sc07_281 with dissolve
                mh "His touch... was warm, like the heat from a campfire... embracing my neck."
                mh "That was not the touch of a man trying to hurt me. I know that kind of touch all too well."
                mh "[mc]’s touch was different... his words stern and harsh, but his touch... powerful, yet kind?"
                mh "A powerful man like [mc] as our A'khan... we'd never have to fear outsiders again..."
                scene ch6sc07_282 with dissolve
                mh "What am I even saying? ... *Sighs* I must ask the goddesses for guidance."
                mh "My human mind is too weakened by his presence to make sense of this..."


    scene ch6sc07_283 with dissolve
    ed "H-Hey! Woman! What about my daughter?!"
    ed "You promised if I gave you dirt on [mc] you'd help me get her back!"
    scene ch6sc07_284 with dissolve
    mh "According to what [mc] said, your daughter is safe and sound, and better off far away from you."
    mh "We’ll decide your fate later."
    mh "Guards will be by once a day with a meal for you. It's more than you deserve."
    with vpunch
    ed "H-Hey! Lady! Let me out of here!"
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc07_285 with Dissolve(1.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    ec "So, what did you and Marah discuss in private?"
    ec "I can’t imagine the two of you would have a great deal in common?"
    scene ch6sc07_286 with dissolve
    mc "We just found some common ground."
    scene ch6sc07_287 with dissolve
    mh "A’nu, Champion..."
    mh "I am headed to one of our shrines to seek guidance."
    mh "Champion, may you have good fortune in dealing with the Arugoh."
    mh "If anyone can bring them to heel and reunite us, I believe [mc] will be the one."
    scene ch6sc07_288 with dissolve
    mh "I will say a prayer on your behalf."
    ec "......"
    scene ch6sc07_289 with dissolve
    mc "What?"
    "Echo stares at you in disbelief."
    scene ch6sc07_290 with dissolve
    ec "What in all of the jungle was that?!"
    ec "She... Marah was... nice to you?!"
    scene ch6sc07_291 with dissolve
    ec "Okay, I’m going to need to know exactly what you did. And more importantly, you need to teach me how to do it, as well."
    ###Choice###
    menu:
        "I threatened her.":
            scene ch6sc07_292 with dissolve
            mc "I threatened her."
            scene ch6sc07_293 with dissolve
            ec "You threatened Marah... of all people... into submission?"

        "I persuaded her a little.":
            scene ch6sc07_292 with dissolve
            mc "I just... persuaded her a little."
            scene ch6sc07_293 with dissolve
            ec "You managed to persuade Marah... of all people... no way?"


    scene ch6sc07_292 with dissolve
    mc "Well... yes."
    mc "I was tired of her shenanigans."
    scene ch6sc07_294 with dissolve
    ec "By all the goddesses! I would’ve loved to witness that! *Giggles*"
    mc "*Chuckles* I’ll keep that in mind the next time she gets on my nerves."
    scene ch6sc07_295 with dissolve
    ec "You'd better!"
    ec "I simply cannot bear to live my life without witnessing such a thing. *Giggles*"
    scene ch6sc07_296 with dissolve
    ec "I’m glad we got everything squared away, though."
    ec "We’ll keep this ‘Edward’ locked up until you return."
    ec "Once you’re back, we can decide how to deal with him."
    scene ch6sc07_297 with dissolve
    mc "Sounds good. I’m counting on you to take care of things here until I’m back."
    scene ch6sc07_298 with dissolve
    ec "Oh, are you now? As if I haven’t done just that my entire life? *Giggles softly*"
    ec "Already acting like you’re the A’khan?"
    scene ch6sc07_299 with dissolve
    mc "*Chuckles* Based on your people’s previous A’khans, I’ve far surpassed any of them in feats."
    mc "So, all that’s left are the formalities. Yeah, I am your A’khan."
    scene ch6sc07_298 with dissolve
    ec "*Softly* Yes... yes, you are."
    ec "Good luck, [mc]... I, too, will ask the goddesses to watch over you."
    scene ch6sc07_299 with dissolve
    mc "I appreciate that. I’ll be back before you know it... then we can finally make this official."
    scene ch6sc07_298 with dissolve
    ec "I long for that to happen... Go on, A’nai will eagerly await your return."
    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene ch6sc07_300 with Dissolve(1.5)
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause(0.5)
    "On your way towards the main gate, you pass by Miyo’s hut and hear her talking with Vex inside."
    mct "{i}Let’s check on the girls before we head out. They might know something more about the Arugoh tribe.{/i}"
    scene ch6sc07_301 with dissolve
    mct "{i}They’re both too young to have much history with the other tribe, but they could have heard things.{/i}"
    "As you enter Miyo’s hut, the girls turn their attention to their visitor."
    scene ch6sc07_302 with dissolve
    mc "Good morning, girls."
    mc "Looks like the two of you are up early. We’re barely past dawn."
    scene ch6sc07_303 with dissolve
    vx "[mc]! H-Hi! Good morning!"
    vx "We wanted to be up early to see you off."
    scene ch6sc07_304 with dissolve
    mi "Forgive us... we didn't expect such a handsome visitor this early, otherwise we’d have been naked to greet you. *Snickers*"
    scene ch6sc07_305 with dissolve
    with vpunch
    vx "Miyo!!"
    mi "*Snickers* What? I bet he’d love to see us naked first thing in the morning."
    scene ch6sc07_306 with dissolve
    vx "Please, forgive her. She gets a little horny in the morning."
    mc "*Chuckles* Don’t we all?"
    scene ch6sc07_307 with dissolve
    vx "I... I..."
    vx "I suppose it is natural to feel that way when waking up..."
    scene ch6sc07_304 with dissolve
    mi "Of course it is! When you’ve had dreams filled with desire all night, how could you not be horny in the morning?"
    mi "Now that we’ve established that all three of us are horny in the mornings..."
    mi "To what do we owe the pleasure of your visit, [mc]?"
    scene ch6sc07_308 with dissolve
    mc "Guess."
    mi "Hmmh... *Giggles*"
    scene ch6sc07_304 with dissolve
    mi "Hmmm... then I'd guess you’re here because you know a young herbalist needs the touch of a handsome champion?"
    scene ch6sc07_309 with dissolve
    vx "He’s not here to play with you."
    vx "He must be here about the imprisoned outsider."
    scene ch6sc07_310 with dissolve
    mc "Not quite, he’s of no interest to me at the moment."
    mc "I’m here because I was wondering if you knew anything about the Arugoh tribe?"
    scene ch6sc07_307 with dissolve
    vx "The Arugoh tribe? ..."
    vx "They're not a friendly bunch, even with us."
    vx "Sometimes we cross paths with them in the jungle, and it is never a pleasant exchange."
    scene ch6sc07_304 with dissolve
    mi "I only know what they like to do to outsiders..."
    mi "They capture shipwrecked sailors and keep them chained, only providing them with water, no food."
    scene ch6sc07_311 with dissolve
    mi "At first they test their strength. If they're weak... they kill them immediately."
    mi "But if they find them satisfyingly strong, they will use them for breeding."
    scene ch6sc07_312 with dissolve
    mi "They will continue this breeding process relentlessly, taking turns for days, sometimes weeks."
    mi "Until eventually the man expires from exhaustion and starvation."
    scene ch6sc07_313 with dissolve
    vx "W-What ... Miyo, you’re jesting... right?"
    scene ch6sc07_310 with dissolve
    mc "I’m afraid she isn’t kidding, Vex... Echo told me something similar."
    scene ch6sc07_311 with dissolve
    mi "We have been awaiting our future A’khan to provide us what we need to rebuild our tribe."
    scene ch6sc07_312 with dissolve
    mi "But they... have taken it upon themselves to rebuild their ranks in this way."
    scene ch6sc07_313 with dissolve
    vx "B-But... that is disgusting! How could they do such a thing?! Isn't that the same as what was done to our people?!"
    scene ch6sc07_304 with dissolve
    mi "That is why they're doing it... they are angry and view all outsiders as the same."
    mi "You need to be careful, [mc]... I know you are capable of great things."
    scene ch6sc07_312 with dissolve
    mi "But... a man of your caliber? They will undoubtedly attempt to subject you to imprisonment and breeding."
    scene ch6sc07_314 with dissolve
    vx "No. I can not accept this... we will go with him and protect him!"
    vx "On my life as a huntress, they will {b}NOT{/b} breed him like that!"
    scene ch6sc07_315 with dissolve
    vx "They only respect strength, so I shall show them mine!"
    scene ch6sc07_316 with dissolve
    mc "I appreciate the concern, Vex, but I have to do this on my own. Echo made it clear the A’nai tribe can’t get involved."
    mc "It could worsen your tribe's relationship with them, which is the opposite of what we’re trying to accomplish."
    mc "Besides, if I’m escorted by huntresses, they will know it’s a trick. I need to let them capture me."
    "Vex nods reluctantly in agreement."
    scene ch6sc07_303 with dissolve
    mc "Thank you, girls, I appreciate you telling me what you know."
    vx "Of course!"
    scene ch6sc07_304 with dissolve
    mi "Is there... anything else you'd like from us? Anything at all?"
    scene ch6sc07_317 with dissolve
    mi "Anything you desire? Handsome champion."
    vx "Miyo..."
    scene ch6sc07_318 with dissolve
    mi "What, Vex? I’m just saying what you’re thinking."
    mi "Couldn't he have come to see us for another reason as well?"
    scene ch6sc07_319 with dissolve
    mi "A far more... pleasurable reason."
    vx "How can you say such things out loud! I-In front of him!"
    scene ch6sc07_320 with dissolve
    mi "Isn't it true, hero?"
    mi "Didn't you come to give us a... proper goodbye?"
    scene ch6sc07_308 with dissolve
    mc "I mean..."
    #####Choice####
    menu:
        "I came to see you, Miyo. ({color=#ff8cdd}Miyo Scene{/color})":
            mc "Miyo is correct, I did come here wanting more than just information."
            scene ch6sc07_304 with dissolve
            mi "Then, what do you want? What do you desire?"
            scene ch6sc07_308 with dissolve
            mc "You."
            mc "I came to see you."
            $ mi_trust += 5
            "Miyo is pleased by your reveal, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch6sc07_322 with dissolve
            mi "*Sensual* I know."
            mi "*Sensual* You crave me as much as I crave you."
            scene ch6sc07_323 with dissolve
            vx "And that is my cue... it was nice to see you, [mc]."
            mc "Likewise, Vex, always a pleasure."
            scene ch6sc07_324 with dissolve
            #play music lewd_1 fadein 1.0
            stop music fadeout 1.0
            mi "Finally..."
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            mi "Now that we’re alone... what do you want to do to me?"
            scene ch6sc07_325 with dissolve
            mi "How does my handsome champion desire me?"
            scene ch6sc07_326 with dissolve
            mi "Share it with me, and I will make it come true."
            scene ch6sc07_327 with dissolve
            mc "I want those naughty lips of yours, wrapped tightly around my cock."
            mi "*Sensual* Then put it in my mouth and fuck it."
            scene ch6sc07_328 with dissolve
            with vpunch
            mi "*Muffled* Mmffhh! Mmfghh!"
            mc "Fuck, Miyo... there’s that little warm mouth of yours."
            scene mi_lewd7 with dissolve
            $ renpy.pause()
            mi "*Muffled sucking* Mmfghh... ssllrrhh... mmgh! I love your cock!"
            mc "Oh, yeah? Then let’s give you what you’re craving."
            scene mi_lewd8 with dissolve
            $ renpy.pause()
            "Miyo’s wet lips keeps a tight seal around your cock as you begin fucking her mouth."
            mi "*Muffled* Mmfgh! Mmh-mghh!"
            mc "Aahh... that’s a good girl- Mmmgh... keep sucking while I thrust."
            with vpunch
            mc "Suck harder, I’m getting close... mmmgh! Show me what your slutty mouth is capable of."
            with vpunch
            mi "*Muffled sucking and gagging* {b}Mmghh! Mmfgh!! MHH!!{/b}"
            scene ch6sc07_329 with dissolve
            with vpunch
            mi "Mmmfgh-Mmgh!"
            mc "Good girl, swallow all of it. It’s yours."
            scene ch6sc07_328 with dissolve
            mi "Mmmgh... soh... goohd- Mmmh..."
            scene ch6sc07_327 with dissolve
            mi "Thank you for this gift... I’ve desired your seed for breakfast for a while now."
            mc "Can’t let my naughty little herbalist starve, can I?"
            mi "*Giggles* No, that would be ill advised! Thank you... for using my mouth."
            scene ch6sc07_326 with dissolve
            mc "Pleasure was all mine, believe me. But I’ve got to get going now."
            mi "Don’t worry, as much as I’d love to cuddle with you right now, I know you’re busy."
            scene ch6sc07_325 with dissolve
            mi "[mc], thank you for this... I love feeling desired by you."
            mi "Please be careful out there. Return to me unharmed."
            mc "I’ll do my best. Take care, Miyo."

        "I came to see Vex. ({color=#ff8cdd}Vex Scene{/color})":
            mc "Miyo is correct, I did come here wanting more than just information."
            scene ch6sc07_304 with dissolve
            mi "Then, what do you want? What do you desire?"
            scene ch6sc07_308 with dissolve
            mc "I came here to see Vex."
            scene ch6sc07_313 with dissolve
            vx "{b}OH!{/b}"
            vx "Y-You came to see me?"
            $ vx_trust += 5
            "Vex is pleasantly surprised by your reveal, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch6sc07_330 with dissolve
            mi "I see..."
            mi "I just remembered, I have a bunch of herbs that needs mixing before they grow stale."
            scene ch6sc07_331 with dissolve
            mi "*Quietly* {size=-10}{b}Hunt her well, hero.{/b}{/size}"
            mi "*Quietly* {size=-10}{b}I’ll see you when you return, handsome champion.{/b}{/size}"
            scene ch6sc07_332 with dissolve
            vx "So... you came just to see me?"
            vx "How come?"
            scene ch6sc07_333 with dissolve
            mc "Well, I like being around you."
            vx "[mc]... I... the feeling is mutual."
            scene ch6sc07_334 with dissolve
            vx "Thank you... for your kind words towards me."
            vx "My entire life... everyone has been on edge at the mention of outsiders."
            scene ch6sc07_335 with dissolve
            mc "That explains why you gave me such a hard time when we first met."
            scene ch6sc07_334 with dissolve
            vx "Wouldn't you act the same if you had a history with outsiders like ours?"
            scene ch6sc07_335 with dissolve
            mc "I would. That is why I don’t hold any of your people's behavior against you."
            mc "Even Marah, as much as I dislike her and her actions, it’s easy to tell she’s just too set in her ways."
            mc "But she’s trying to protect the tribe in such an extreme way that she is pushing aside potential allies."
            scene ch6sc07_334 with dissolve
            vx "Yeah... she does care deeply for the tribe. I just hope she won’t keep hating you."
            scene ch6sc07_336 with dissolve
            vx "But even if she does... just know that I... I will never hate you."
            vx "I... I like you very much."
            #play music summon_3 fadein 1.0
            stop music fadeout 1.0
            scene ch6sc07_337 with dissolve
            play music lewd_1 fadein 1.0
            #stop music fadeout 1.0
            mc "Who knew my little huntress could be so cute?"
            vx "*Whimpers softly* Mmmh..."
            mc "From pointing her sharpened spear towards me in distrust, to letting me caress her cheek."
            vx "*Giggles* ..."
            scene ch6sc07_338 with dissolve
            vx "You’ve showed me... showed all of us, a different path."
            vx "That you are different."
            scene ch6sc07_339 with dissolve
            vx "You’re truthful, kind, warm... you respect our people and our way of life."
            vx "You genuinely care about all of us. We aren’t just a means to an end with you."
            scene ch6sc07_340 with dissolve
            mc "Vex... thank you, I’m glad you see me in such a way."
            scene ch6sc07_339 with dissolve
            vx "How could I not? You’ve proven it time and time again by protecting us, putting your life on the line for us."
            vx "After everything I’ve experienced with you, I truly believe you to be the savior of our people."
            vx "The one true A’khan, chosen by the goddesses to rise far above all of the A’khans of our past."
            scene ch6sc07_340 with dissolve
            mc "*Chuckles* Okay, now you’re just making my head grow."
            mc "But thank you, I appreciate the compliment."
            scene ch6sc07_339 with dissolve
            vx "I’m really glad you found A’nai, [mc]..."
            vx "Maybe... maybe you would let me grow something else of yours?"
            scene ch6sc07_340 with dissolve
            mc "What does my little huntress have in mind?"
            scene ch6sc07_341 with dissolve
            vx "I’d like to grow him..."
            mc "Oh... you’re hungry for my cock?"
            scene ch6sc07_342 with dissolve
            vx "You speak so lewdly..."
            scene ch6sc07_343 with dissolve
            vx "Mmh... yes, I am hungry for your big cock."
            vx "You want me to satisfy you... I know you do."
            scene vx_lewd13 with dissolve
            $ renpy.pause()
            mc "Mmmh... that’s a naughty little grip you’ve got."
            vx "You like this? You like having your huntress touch you?"
            mc "Aahh... yeah, your touch is incredible..."
            vx "You’re so warm... and so hard... mmmh, but my hand is not enough for a man like you."
            scene ch6sc07_343 with dissolve
            vx "I have something better for you... come."
            scene ch6sc07_344 with dissolve
            mc "I think I’m going to like what you have in mind."
            vx "I’d hope so... you’re the only man who will ever have me like this."
            scene ch6sc07_345 with dissolve
            "Vex climbs onto the table, presenting herself to you, eager to be mated."
            vx "Please... your spear... I need to feel it, I need you inside me, [mc]."
            scene ch6sc07_346 with dissolve
            vx "*Gasps* Aannghh! Ohh..."
            "You feel the warmth of Vex’s tight little pussy surround you, her slick juices welcoming you inside, and then you begin to move."
            scene vx_lewd14 with dissolve
            $ renpy.pause()
            vx "*Moans* F-Finally! Mmmh... Oh! OH!! By the jungle your cock is so big inside my flower!"
            mc "Fuck, Vex... your pussy is so tight - Mmh!"
            vx "I was... Aahh! I was thinking about you last night and touching myself, and I discovered-"
            vx "- that I could- Ahhh... squeeze my fingers. Mmh! So, I kept practicing until the sun came up- Ahh!"
            with vpunch
            mc "Fuck that’s amazing- Mmgh... you’re a proper huntress now."
            vx "Fuck me harder! Aiiyh!!"
            with vpunch
            scene vx_lewd15 with dissolve
            $ renpy.pause()
            with vpunch
            vx "*Squeals in pleasure* {b}Aiiiyh-Ahhh! You’re so deeeeeep! AHhh!{/b}"
            with vpunch
            vx "{b}Fill me up! Aiiyh! Cum with me [mc]!{/b}"
            mc "Fuck! Mmgh! If you keep squeezing like that - Ahhh!"
            vx "Yes! Mmh! I want it! Fill me with your seed and satisfy me! AHhh!"
            with vpunch
            vx "I love this feeling! I feel like I’m the only woman in the world when we’re mating- Ahh! I’m cumming!! AHHH!"
            with vpunch
            scene ch6sc07_347 with dissolve
            with vpunch
            mc "Aahh! Vex! Mmmgh!"
            vx "*Gasps* Oh! Ohhh! Mmmh! Thank you... this is a wonderful gift, mmmh."
            mc "My little huntress deserves the best."
            vx "You certainly delivered. *Giggles lightly* You know exactly how to satisfy me."
            scene ch6sc07_348 with dissolve
            vx "You made me work up quite a sweat."
            scene ch6sc07_349 with dissolve
            mc "I love seeing you covered in sweat, and filled with my cum... just like nature intended it."
            scene ch6sc07_348 with dissolve
            vx "Mmh, indeed. When you return, you'd better be ready to mate with me again."
            vx "Until then, I will keep practicing more with my fingers."
            scene ch6sc07_349 with dissolve
            mc "Good girl. I’ll see you soon."
            scene ch6sc07_348 with dissolve
            vx "Don’t let anything or anyone stop you from returning to A’nai."
            scene ch6sc07_349 with dissolve
            mc "To A’nai... or to you?"
            scene ch6sc07_348 with dissolve
            vx "One doesn’t exclude the other... but mostly to me- mmmh... be careful out there."
            scene ch6sc07_349 with dissolve
            mc "Keep your little flower well prepared for when I return. I will be craving it."
            "Vex doesn’t say anything, she just giggles and wiggles her ass."

        "I’m not in the mood. (No Scene)":
            mc "I have too much on my mind currently. I just stopped by to see what you knew about the Arugoh tribe."
            mc "But I’m glad I got to see both of you before I leave. Make sure you keep A’nai safe until I return."
            scene ch6sc07_321 with dissolve
            mi "Oh... that’s... a shame."
            mi "I'd hoped for a different answer."
            scene ch6sc07_309 with dissolve
            vx "Come on, Miyo."
            vx "Just because your mind always thinks about lewd fantasies, doesn’t mean his does as well."
            vx "He has bigger things to worry about, like how to deal with the challenge ahead."
            scene ch6sc07_310 with dissolve
            mc "Vex is right. Having a good time is not my priority, right now, even though we all know it would feel... incredible."
            scene ch6sc07_311 with dissolve
            mi "Yes... it certainly would."
            mi "Can’t blame a girl for trying... right?"
            scene ch6sc07_310 with dissolve
            mc "No, and I never will. I can never fault you for going after what you want."
            scene ch6sc07_306 with dissolve
            vx "Thanks for stopping by, [mc]."
            vx "It was lovely to see you. I’m glad we managed to help you a bit."
            scene ch6sc07_303 with dissolve
            mc "Of course, even if you had no information, I’d still have been glad I came to see you."
            mc "I always enjoy seeing the two of you, my hunting partner and my favorite herbalist."
            bth "*Giggles*"
            scene ch6sc07_304 with dissolve
            mi "Come see us any time... you know we like your company just as much."
            scene ch6sc07_305 with dissolve
            mi "Especially Vex, over here... all she does is talk about you."
            scene ch6sc07_306 with dissolve
            vx "Uh! D-Don’t listen to her, okay? She is making things up!"
            scene ch6sc07_303 with dissolve
            mc "*Chuckles* Take care, you two."

    scene black with Dissolve(1.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch6sc05_124 with Dissolve(1.5)
    $ renpy.pause(0.5)
    mct "Okay... five hours north, let’s go find this ambassador."
    mct "By my count, Eliza should have roughly a week’s worth of blood left."
    mct "A week to conquer a hostile tribe, complete the last trial, unite the tribes, restore their connection to the goddesses-"
    mct "- claim the title of A’khan, return to Diana with the ambassador, and free Kira... *Sighs* How hard could it be?"
    scene black with Dissolve(1.5)
    $ renpy.pause(0.5)
    "As you approach the main gate, you see Pearl and Tazzy awaiting you."
    scene ch6sc07_350 with Dissolve(1.5)
    $ renpy.pause(0.5)
    pl "Here he comes... I look pretty, right?"
    scene ch6sc07_351 with dissolve
    tz "You look gorgeous babes, you know that."
    tz "Absolutely smashing."
    scene ch6sc07_350 with dissolve
    pl "*Giggles* Thanks!"
    scene ch6sc07_352 with dissolve
    mc "Fancy meeting the two of you here..."
    scene ch6sc07_353 with dissolve
    pl "H-Hi... you look handsome today."
    mc "And you’re beautiful as usual-"
    scene ch6sc07_354 with dissolve
    mc "Taz... that’s a new look? What’s the occasion?"
    tz "Like it?"
    mc "Mhm, I do... the tribal look suits you, you fit in well out here."
    tz "Why, thank you! I decided I'd best dress up for the adventure ahead."
    mc "Adventure?"
    scene ch6sc07_353 with dissolve
    pl "We’re coming with you."
    scene ch6sc07_355 with dissolve
    tz "Damn straight we are!"
    tz "We’re not about to let you walk alone into a savage tribe filled with women who want to violently breed you."
    scene ch6sc07_356 with dissolve
    mc "*Exhales* And I suppose if I tell you to stay here?"
    scene ch6sc07_355 with dissolve
    tz "We’ll follow you!"
    scene ch6sc07_353 with dissolve
    pl "*Nods* Mh, you know we will."
    scene ch6sc07_356 with dissolve
    mc "*Sighs* Yeah, I had a feeling ... Fine. You’re not members of A’nai, so it shouldn’t cause an issue on that front."
    mc "But my priority is to get the ambassador and complete the trial in the last temple."
    mc "So, don’t get yourself into trouble and force me to have to rescue you."
    scene ch6sc07_353 with dissolve
    pl "We can handle ourselves."
    scene ch6sc07_355 with dissolve
    tz "Correction, Pearl can handle herself, and she will kill anyone who messes with any of us."
    scene ch6sc07_353 with dissolve
    pl "*Nods* That is true."
    scene ch6sc07_356 with dissolve
    mc "C’mon, we'd better get going... we have a five hour trek through the jungle ahead of us."
    scene ch6sc07_357 with dissolve
    with vpunch
    tz "*Gasps* Five hours?! Surely not!"
    tz "You’re not serious! Right?"
    pl "*Snickers*"
    scene ch6sc07_358 with dissolve
    tz "Oh that’s funny is it? You enjoy my suffering?!"
    pl "*Laughs* S-Stop- Hahah! You know I’m ticklish! Hahah!"
    tz "Laugh all you want. I’m the one who’s going to get a massage from [mc] at the end of such a long walk."
    scene ch6sc07_359 with dissolve
    tz "*Whispers* {size=-10}{b}A... deep massage, like no other.{/b}{/size}"
    scene ch6sc07_360 with dissolve
    pl "N-No me!"
    pl "I want a deep massage from [mc]!"
    mc "Nobody is getting a massage if you two don’t hurry up..."
    scene ch6sc07_361 with dissolve
    "And so... you set out from A’nai, with a woman on each arm..."
    "And with a new adventure on the horizon."
    scene black with Dissolve(2.5)
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause(1)
    jump ch6sc8

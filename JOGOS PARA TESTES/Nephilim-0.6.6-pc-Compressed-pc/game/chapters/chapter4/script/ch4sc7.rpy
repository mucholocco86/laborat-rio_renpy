label ch4sc7:

    window hide dissolve
    play music forest_1 fadein 1.0
    scene black with Dissolve (1.0)
    scene ch4sc7 with dissolve
    $ renpy.pause()
    scene ch4sc07_001 with Dissolve(2.0)
    $ renpy.pause(1)
    el "*Stretching* HnnnnghhHhhh!"
    scene ch4sc07_002 with dissolve
    elt "Urrgh! What the hell happened last night?"
    elt "I feel like I’ve been out for a week."
    scene ch4sc07_003 with dissolve
    el "*Immense yawn* {b}Ahhaaaaaaaaooohh!!{/b}"
    scene ch4sc07_004 with dissolve
    el "*Stretching* Nnnggh!"
    el "Heavens! I haven't been this sore since ... well, ever!"
    scene ch4sc07_005 with dissolve
    elt "I just want to spend all day in bed!"
    scene ch4sc07_006 with dissolve
    $ renpy.pause(1)
    scene ch4sc07_005 with dissolve
    $ renpy.pause(1)
    scene ch4sc07_006 with dissolve
    $ renpy.pause(1)
    scene ch4sc07_005 with dissolve
    $ renpy.pause(1)
    scene ch4sc07_007 with dissolve
    elt "Huh?"
    elt "W-Why can’t I feel my legs?!"
    scene ch4sc07_008 with dissolve
    elt "What’s going on??"
    elt "I was... I was in that cold dungeon cellar."
    scene ch4sc07_007 with dissolve
    elt "There was a strange old man in my cell, w-... wibble something?"
    elt "And... [mc]! He found me! And- And..."
    scene ch4sc07_008 with dissolve
    elt "Damnit! I can’t remember what happened after that. Everything's a blur!"
    elt "W-Where’s [mc]?"
    scene ch4sc07_007 with dissolve
    elt "I want [mc]..."
    mc "Hey you..."
    scene ch4sc07_009 with dissolve
    $ renpy.pause()
    scene ch4sc07_010 with dissolve
    with vpunch
    el "{b}[mc]!!{/b}"
    "The frown on Eliza’s face instantly turns to joy as she sees you."
    el "{b}*Eagerly* Up!{/b}"
    scene ch4sc07_012 with dissolve
    mc "Up?"
    scene ch4sc07_010 with dissolve
    el "My legs won’t work... so... I want up!"
    scene ch4sc07_012 with dissolve
    mc "*Chuckles* If you want up. You’re getting up!"
    scene ch4sc07_013 with dissolve
    mc "You ready, your majesty?"
    scene ch4sc07_014 with dissolve
    el "Ready!"
    el "Don’t drop me!"
    scene ch4sc07_015 with dissolve
    mc "Up you go!"
    el "*Giggles* H-Hey! {b}That tickles!{/b}"
    mc "It can't be helped, a kitten needs her daily tickle after all."
    scene ch4sc07_016 with dissolve
    mc "Quit squirming, or we’ll end up on the floor."
    el "*Giggles* I feel so light in your arms! Are you saying you can't hold me up?"
    "You adjust your grip on each side of her ribs."
    scene ch4sc07_017 with dissolve
    el "{b}*Laughing* Hahah! S-Sorry! Haha-hhahah! M-mercy!{/b}"

    ###Choice###
    menu:
        "Show her no mercy! ({color=#ff8cdd}Romance{/color})":
            scene ch4sc07_017 with dissolve
            $ eliza_path = True
            mc "Ticklish, huh? Then I suppose you wouldn’t want me to do this!"
            scene ch4sc07_016 with dissolve
            $ renpy.pause(1)
            scene ch4sc07_017 with dissolve
            $ renpy.pause(1)
            scene ch4sc07_016 with dissolve
            $ renpy.pause(1)
            scene ch4sc07_017 with dissolve
            $ renpy.pause(1)
            scene ch4sc07_016 with dissolve
            with vpunch
            el "{b}*Giggles loudly* Nooo! D-Don’t!! HahaHa! Stoophh!{/b}"
            scene ch4sc07_016 with dissolve
            el "{b}YOU WIN! *Giggles* Hhhaaaahha! YOU WIN! MERCY! Hahahhh!{/b}"
            scene ch4sc07_017 with dissolve
            mc "Who’s the most handsome and charming guy you’ve ever met?"
            el "N-not you!! Hwhawhha!"
            scene ch4sc07_016 with dissolve
            "You poke her sides a little more firmly."
            scene ch4sc07_018 with dissolve
            with vpunch
            el "Okay- {b}OKAY!{/b} HahhHaa! {b}YOU! YOU ARE!{/b}"
            mc "I’m what?"
            el "The most handsome and charming guy I’ve ever met!"
            scene ch4sc07_019 with dissolve
            $ renpy.pause()
            el "..."
            scene ch4sc07_020 with dissolve
            el "Kiss me."
            scene ch4sc07_021 with dissolve
            $ renpy.pause()

            ####Animation####
            show mc_el_kiss8 with fade
            $ renpy.pause(2, hard=True)
            el "*Soft moan* Nnhhmm..."
            elt "I needed this."
            elt "He has a way of making me forget everything else."
            scene ch4sc07_021 with dissolve
            elt "Mnhh..."
            scene ch4sc07_020 with dissolve
            el "I desperately need a bath... I'm rubbing dirt all over you!"
            scene ch4sc07_019 with dissolve
            mc "You really do. I was holding my breath the entire time."
            scene ch4sc07_020 with dissolve
            el "Dummy!"
            el "For that comment alone, you'll have to wash me!"
            scene ch4sc07_022 with dissolve
            mct "Heh. It’s cute how she thinks that's a punishment."
            scene ch4sc07_023 with dissolve
            el "I know that smile."
            el "You’re thinking about washing my breasts, aren’t you?"
            scene ch4sc07_022 with dissolve
            mct "Her soft perky breasts are pressing into my back..."
            mct "She really seemed to enjoy the times I’ve touched them before."
            mct "They must be incredibly sensitive... I’ll be sure to wash them thoroughly."
            scene ch4sc07_023 with dissolve
            el "Earth to [mc]... You won’t get to wash any of me if we don’t make it to the baths!"
            scene ch4sc07_024 with dissolve
            mc "Huh? Oh, right! Hold on kitten."
            scene ch4sc07_023 with dissolve
            el "I have no intentions of letting go of my lion..."
            "Eliza loves that you were day-dreaming about giving her a bath, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ eliza_trust += 2
            scene black with Dissolve(2)

        "Ease up on the poor girl. ({color=#2bff8b}Friendly{/color})":
            scene ch4sc07_017 with dissolve
            mc "Alright, alright."
            mc "I think it’s time we get you cleaned up. You’re still covered in dirt from last night."
            scene ch4sc07_024 with dissolve
            mc "Hold on monkeygirl..."
            scene ch4sc07_023 with dissolve
            el "Oh, I’m not letting go!"
            el "Not until I see a warm bath!"
            scene black with Dissolve(2)

    scene black with dissolve
    $ renpy.pause(1)
    if eliza_path == True:
        scene ch4sc7a with Dissolve(2)
        $ renpy.pause()
        scene ch4sc07_025 with Dissolve(2)
        $ renpy.pause(1)
        mc "Hey... I was wondering..."
        mc "When you fainted in my arms in the cells."
        scene ch4sc07_027 with dissolve
        el "Yeah?"
        scene ch4sc07_025 with dissolve
        mc "You said Selena’s name?"
        scene ch4sc07_027 with dissolve
        el "Oh... I thought you must've already known by now."
        scene ch4sc07_025 with dissolve
        mc "Know what? I haven’t seen her since last night when she came bursting into the tavern..."
        mc "Shouting that you'd been taken."
        scene ch4sc07_027 with dissolve
        el "*Scoffs* That’s funny..."
        el "Given she’s the one who betrayed us."
        scene ch4sc07_025 with dissolve
        mc "{b}What!?{/b} Why would she-"
        scene ch4sc07_027 with dissolve
        el "I don’t know... but she said sorry when three masked men jumped us in the alley..."
        el "And she also visited me in my cell later on. She claimed that she 'had no choice'."
        el "I think it had something to do with her sister? Maybe Taron used her as leverage?"
        scene ch4sc07_026 with dissolve
        mc "Using someone's loved one against them, that does sound like Taron."
        mc "She will regret this, Eliza. I promise you."
        mc "She's not getting off scot-free, I'll make sure of that."
        scene ch4sc07_027 with dissolve
        el "I’m sorry... I should have been more aware, I let my guard down."
        el "I thought she was my friend..."
        scene ch4sc07_026 with dissolve
        mc "Don’t worry about it for now."
        mc "Let’s get you cleaned up, shall we?"
        scene ch4sc07_027 with dissolve
        el "How do you want me?"
        scene ch4sc07_025 with dissolve
        mc "Float on your back. I’ll support you."
        scene ch4sc07_027 with dissolve
        el "O-Okay. But if you let me drown... I’ll haunt you!"
        scene ch4sc07_025 with dissolve
        mc "I’ve seen you swim. I don’t think there's a chance of you drowning in a bathtub."
        scene ch4sc07_027 with dissolve
        el "That was when I could use my legs..."
        el "*Sigh* That’s not the case anymore."
        scene ch4sc07_025 with dissolve
        mc "Look at it this way... if your legs weren’t injured, I wouldn’t be giving you a bath right now."
        scene ch4sc07_027 with dissolve
        el "If I'd known all it would take for you to bathe me was a life threatening injury-"
        el "I would’ve thrown myself into way more dangerous situations!"
        scene ch4sc07_026 with dissolve
        mc "How about I promise to make sure you're bathed on a regular basis..."
        mc "{b}IF{/b} you promise to {b}NOT{/b} leap headfirst into danger?"
        scene ch4sc07_028 with dissolve
        el "Deal!"
        el "So, is this how you want me?"
        scene ch4sc07_029 with dissolve
        "Instead of answering her. You begin moving your hand, rubbing your palm against her wet naked body."
        scene ch4sc07_030 with dissolve
        "She immediately surrenders to your touch."
        el "*Moans* Mhhh... Nnhh..."
        scene ch4sc07_032 with dissolve
        "As your hand surrounds her smooth breast the warmth of your palm embraces her sensitive nipple."
        el "*Moans deeper* Mhhnnn! Mnngghhh, [mc]..."
        scene ch4sc07_031 with dissolve
        el "*Moans* [mc]... Nnhhh!"
        scene ch4sc07_033 with dissolve
        "As you reach to wash her cheek, the sensation of your arm rubbing against her nipple causes her to continue moaning softly."
        el "Nhhmm! [mc]... Mnhm!"
        scene ch4sc07_034 with dissolve
        "Feeling your thumb gently pushing against her lips she instinctively opens her mouth for you."
        stop music fadeout 1.0
        scene ch4sc07_035 with dissolve
        play music lewd_1 fadein 1.0
        "She closes her mouth around your thumb as it slips between her wet lips."
        "At first she licks the tip of your thumb, but then she follows up by gently sucking while she moans softly."

        ####Animation####
        show el_suck1 with fade
        $ renpy.pause(2, hard=True)
        "As she continues to suck and lick your thumb..."
        "- her nipple reacts sensitively to each slight movement of your arm that rests against her breast."
        "Her breathing increases with each new stimulation."
        scene ch4sc07_035 with dissolve
        "She releases your finger from her wet mouth."
        scene ch4sc07_034 with dissolve
        $ renpy.pause()
        el "I-I want it inside me."
        el "I need you."
        scene ch4sc07_036 with dissolve
        el "Be gentle, please..."
        el "She gazes intently into your eyes as she catches her breath."
        scene ch4sc07_037 with dissolve
        $ renpy.pause()
        el "Ouuh! That tickles!"
        scene ch4sc07_038 with dissolve
        "As you reach her perfect little pussy, you pause and look to her for permission..."
        "However what you see is not the lustful expression you were expecting."
        scene ch4sc07_039 with dissolve
        stop music fadeout 1.5
        el "I-I-I... I- *Heavy sigh*"
        play music chill_5 fadein 1.0
        scene ch4sc07_040 with dissolve
        el "[mc]. I can’t feel you..."
        el "I can’t feel your touch below my waist."
        scene ch4sc07_039 with dissolve
        el "*Sobbing* I’m sorry... I’m so sorry! I-I don’t know what to do!"
        scene ch4sc07_042 with dissolve
        mc "Hey..."
        scene ch4sc07_041 with dissolve
        el "I’ve let you down... I’ve ruined everything!"
        el "It was silly of me to ask you to touch me there... I'm such a tease! I'm sorry!"
        scene ch4sc07_042 with dissolve
        mc "Shhh. Everything’s fine... it’s okay."
        mc "You haven't done anything wrong. Nothing at all."
        scene ch4sc07_041 with dissolve
        el "No it's not! It’s not okay at all!"
        scene ch4sc07_043 with dissolve
        el "I-I can’t be with the man I {b}love!!{/b}"
        scene ch4sc07_044 with dissolve
        el "*Sobs* All because of him! He took this from us, [mc]."
        el "He's ruined everything! I hate him! I hate him so much!"
        scene ch4sc07_045 with dissolve
        mc "Eliza, did you just say you love me?"
        scene ch4sc07_046 with dissolve
        $ renpy.pause(0.5)
        "As if she just realised what she had admitted out loud, she freezes in place, just looking at you."
        elt "Oh, no! Did I really say that out loud??"
        elt "I've felt it for a while, but this... this isn't how I wanted to tell him for the first time!"
        scene ch4sc07_047 with dissolve
        el "W-What? N-No. You... I-I was just freaking out like a silly little girl."
        el "You heard wrong!"
        scene ch4sc07_045 with dissolve
        mc "Hey... Look at me."
        scene ch4sc07_046 with dissolve
        stop music fadeout 1.5
        $ renpy.pause(1.5)
        menu:
            "I love you. ({color=#ff8cdd}Romance{/color})":
                scene ch4sc07_045 with dissolve
                play music relax_2 fadein 1.0
                mc "I love you too."
                $ eliza_path = True
                scene ch4sc07_044 with dissolve
                el "I didn’t say it-"
                scene ch4sc07_048 with dissolve
                el "W-Wait... You do?"
                scene ch4sc07_045 with dissolve
                mc "Yes. I’ve felt it for a while now."
                scene ch4sc07_050 with dissolve
                $ eliza_relationship = True
                mc "Every time we touch, something ignites inside me."
                mc "With every kiss, I’ve felt my walls crumbling."
                mc "Every time I smell your hair, desire stirs inside me."
                scene ch4sc07_045 with dissolve
                $ eliza_kiss = True
                mc "Whenever you smile, it feels like time stands still and nothing else matters."
                mc "Eliza... I love you."
                scene ch4sc07_046 with dissolve
                $ renpy.pause(1)
                elt "T-That was so romantic!! He really means it!"
                scene ch4sc07_049 with dissolve
                el "I love you too!"
                scene ch4sc07_048 with dissolve
                el "Since we've both confessed now, there’s only one thing left to do..."
                mc "Oh yeah? And what is that?"
                scene ch4sc07_049 with dissolve
                el "*Giggling softly* We need to seal our confession with a kiss!"
                el "Our kisses will forever taste differently now!"
                scene ch4sc07_051 with dissolve
                "You lean down placing your hand at the back of her neck while your other hand slides up her belly and onto her breast."
                $ renpy.pause(1)
                "She instinctively let’s out a soft moan as you squeeze her sensitive breast."
                scene ch4sc07_052 with dissolve
                "As your lips passionately meet, she playfully licks your tongue, inviting you inside her mouth."
                ####Animation####
                show mc_el_kiss9 with fade
                $ renpy.pause(2, hard=True)
                el "*Moans* Mhhm! Nnhhh! Mhhnnnhh!"
                "She can’t hold back her quiet moans as you caress her breast. The kiss deepens, rich with passion and longing."
                "The kiss isn’t simple lust, it's an expression of something else entirely..."
                "Love."
                "Two hearts that have finally confessed their secret feelings, and no longer want to hold back."
                "She lovingly twines her tongue with yours, mingling your salivas together, and breathing her soft moans into your mouth."
                el "Mmnnh... Nhhghh..."
                mct "I love you, Eliza. There’s nothing I won’t do to make you happy."
                mct "The way she kisses me..."
                mct "I’ve never felt anything like it. It’s like she’s telling me how much she loves me."
                elt "I love him... Mnnhh... So-Nhhh much!"
                elt "I’m his. Mhmh... And he's mine."
                scene ch4sc07_052 with dissolve
                "Reluctantly, your lips eventually part as your jaws begin to ache."
                scene ch4sc07_051 with dissolve
                $ renpy.pause(1)
                el "*Panting softly* Woaah..."
                mc "*Panting* Woah indeed... you were right, that tasted different."
                el "I knew it would, having embraced the way we feel... every touch, kiss, taste, caress, it will all feel..."
                mc "Fated."
                el "*Moans softly* Mmhh... fated."
                scene ch4sc07_048 with dissolve
                el "I was so worried you wouldn’t feel the same way..."
                scene ch4sc07_047 with dissolve
                el "I didn’t think I’d be enough, you know?"
                scene ch4sc07_045 with dissolve
                mc "Enough? You definitely need some rest. It seems you’ve hit your head."
                mc "Seriously. Don’t ever think or feel like you aren’t enough. I’ve only loved one other woman before."
                mc "Rin... but it's not a comparison."
                scene ch4sc07_050 with dissolve
                mc "I spent five years with her to reach that point, romantically."
                mc "You’re the only person that has ever made me feel a love like this, like a fire that's been set ablaze, ever-growing."
                mc "That should tell you all you need to know."
                scene ch4sc07_045 with dissolve
                mc "Love isn't any one thing or any one feeling, it's always unique between the two people involved."
                mc "So don't compare yourself to anyone else... because the way you and I feel about each other?"
                scene ch4sc07_050 with dissolve
                mc "Our love? It's unique."
                mc "It's... ours."
                scene ch4sc07_048 with dissolve
                el "How do you do it?"
                scene ch4sc07_046 with dissolve
                mc "Do what?"
                scene ch4sc07_048 with dissolve
                el "You always know what to say to make me feel better."
                scene ch4sc07_049 with dissolve
                el "To make me happy."
                el "If it were any other guy telling me these things... I’d sucker punch them and run away! *Giggles*"
                el "But when it’s you, it just makes me feel all warm and fuzzy inside."
                scene ch4sc07_046 with dissolve
                mc "I suppose that’s what love is."
                mc "The emotions we share aren't something we’d want to experience with others."
                scene ch4sc07_047 with dissolve
                el "*Mumbles* {size=-10}{b}I don’t want to share you... ever!{/b}{/size}"
                el "*Mumbles* {size=-10}{b}I-... I want to keep you to myself.{/b}{/size}"
                mc "Hmm?"
                scene ch4sc07_049 with dissolve
                el "Nothing! Let’s get dry!"
                el "If we stay in here any longer, we’re going to be all shriveled up like old peaches!"

                scene black with Dissolve(2)

            "I'm not ready to commit. ({color=#f00}Romance end{/color})":
                $ eliza_path = False
                scene ch4sc07_045 with dissolve
                mc "Don’t worry about all this, Eliza. We’ll figure it out."
                $ eliza_relationship = False
                mc "Let’s get you dried off and back in bed. You need to rest and get well."
                scene ch4sc07_043 with dissolve
                stop music fadeout 1.5
                el "O-Okay fine..."
                "Eliza is disappointed that you don't feel the same as her, her trust has decreased by {size=+3}{b}{color=#f00}5{/color}{/b}{/size}."
                scene black with Dissolve(2)



    else:
        scene black with Dissolve(2)
        "You carry her to the baths and wait for her to finish. Then you take her back to bed."
        scene ch4sc07_053 with Dissolve(2)
        $ renpy.pause(1)


    scene ch4sc07_053 with Dissolve(2)
    el "Aaaahh! Nothing like the feeling of sheets on your skin after a rejuvenating bath!"
    el "So... what are we doing today?"
    scene ch4sc07_054 with dissolve
    mc "You and your cute butt are staying right here in this bed."
    scene ch4sc07_055 with dissolve
    el "It’s not like I can do much else in my condition, I suppose."
    el "What about you? Please say you’ll stay in bed with me!"
    el "We could... play games! I know the tavern has decks of cards downstairs we could bring up here?"
    scene ch4sc07_056 with dissolve
    mc "Eliza... there’s something I want you to have."
    mc "It’s an enchanted crystal, called an {b}Arc-stone.{/b}"
    mc "My friend, Rin, gifted it to me on my birthday, some years ago."
    scene ch4sc07_057 with dissolve
    el "O-Okay... What does it do? Why do you want me to have it?"
    "The Arc-stone begins to glow with an intense purple aura."
    scene ch4sc07_058 with dissolve
    mc "Each Arc-stone is individually tuned to its user. This one has been infused with some of my essence."
    mc "It allows me to communicate with you over large distances. It will light up like this when active."
    mc "It’s how mages and sorceresses stay in touch between continents."
    mc "If you'd had this when you got taken last night... I could’ve found you sooner. Prevented all this."
    scene ch4sc07_059 with dissolve
    el "[mc]. Why are you telling me this?"
    scene ch4sc07_058 with dissolve
    "An expression of worry emerges on her face."
    stop music fadeout 1.5
    scene ch4sc07_059 with dissolve
    play music forestnight_3 fadein 1.0
    el "You’re leaving, aren’t you?"
    el "This is why you're bringing up this stone-thingy!"
    scene ch4sc07_060 with dissolve
    mc "Eliza. I... Yes, I’m leaving."
    mc "Dalen has arranged a ship and crew to take Flynn and me to an island where there's an artifact capable of healing your injury."
    scene ch4sc07_061 with dissolve
    mc "Alice will stop by whenever she doesn’t have lessons at the academy."
    mc "Dalen and Sylph said they will have work for you at the guild, helping Sylph with management."
    mc "Borri will-"
    scene ch4sc07_062 with dissolve
    with vpunch
    el "{b}*Shouts* NO!!{/b}"
    scene ch4sc07_063 with dissolve
    el "I don’t want you to leave!"
    el "We stick together, just like you said!"
    scene ch4sc07_060 with dissolve
    mc "Eliza..."
    el "..."
    mct "I knew she wouldn't be okay with this. I wouldn't either, if our roles were reversed."
    scene ch4sc07_063 with dissolve
    el "You’re not going on some mad quest to an unknown island to 'fix' me!"
    el "If that’s the case... I-I would rather live like this!"
    scene ch4sc07_064 with dissolve
    el "*Sobs* ..."
    mc "Eliza... You know I have to do this."
    scene ch4sc07_063 with dissolve
    el "N-No you don’t! Please, just stay."
    el "Stay with me!"
    scene ch4sc07_064 with dissolve
    mc "I’ve already made my decision. Please try to understand why I’m doing this."
    mc "I hate seeing you like this... and it’s all my fault for getting you involved."
    scene ch4sc07_065 with dissolve
    el "*Sobbing* H-How long?"
    scene ch4sc07_066 with dissolve
    mc "Two moons. Maybe more... maybe less."
    mc "That’s why I want you to have the crystal. That way we can still talk while I’m away."
    scene ch4sc07_060 with dissolve
    mc "Trust me. Everything will be fine and I will be back before you know it."
    mc "You will walk again, Eliza. I promise."
    mc "I have to leave now. I’m meeting with Flynn at the docks."
    scene ch4sc07_067 with dissolve
    "You lean in and give her a parting kiss..."
    scene ch4sc07_068 with dissolve
    "As you kiss her forehead the tension in her body seems to fade away and her breathing returns to normal."

    if eliza_path == True:
        mct "Till I see you again... my kitten."
        elt "Please don't leave me! P-Please! Please! Please stay!"
    else:
        mct "Goodbye Eliza... I will find that chalice. You will walk again."

    scene black with Dissolve(1.5)
    stop music fadeout 1.0
    scene ch4sc07_069 with Dissolve(1.5)
    play music feels_1 fadein 1.0
    "Her composure crumbles as you leave the room... You hear Eliza sobbing uncontrollably... but you don’t turn back."
    elt "*Cries* {b}[mc]!!{/b} W-why? Why isn't he here!"
    elt "*Cries* {b}P-Please come back!{/b}"
    $ renpy.pause()
    scene black with Dissolve(1.5)
    stop music fadeout 1.0
    scene ch4sc07_070 with Dissolve(1.5)
    play music forestnight_3 fadein 1.0
    mct "Fuck... Hearing her cry like this..."
    mct "That sick fucker will get what's coming to him."
    mct "*Sigh* First things, first. Selena."
    mct "Eliza said Selena helped him capture her... She needs to answer for this."
    mct "I have a feeling I know where to find her."
    mct "Let’s go say hi..."
    scene black with Dissolve(1.5)
    stop music fadeout 1.0
    scene ch4sc7b with Dissolve(1.5)
    $ renpy.pause()
    scene ch4sc07_071 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    sl "Samarah, quickly!"
    sl "We don’t have much time!"
    scene ch4sc07_072 with dissolve
    sm "I don’t understand why you’re rushing me like this. Aren’t we free, finally?"
    scene ch4sc07_073 with dissolve
    sl "Samarah... I'll explain everything later on. Right now, I have to get you out of here."
    sl "I... I did something I'm not okay with... But I had to! To set you free."
    sl "I need to try to make amends, if it isn't already too late."
    sl "Please, just listen to me. Trust in your big sister, okay?"
    scene ch4sc07_074 with dissolve
    sm "*Sigh* I don’t like this. We only just reunited after countless moons apart..."
    sm "But I can tell this is important to you. Fine, where am I heading?"
    scene ch4sc07_075 with dissolve
    sl "You’ll take the horse. Ride north to Folkstead."
    sl "The stable keeper here has allowed us to use a cabin he has up there, you can lay low there for a while I come join you."
    sl "I know it’s not easy to understand. But once we have more time I will explain."
    scene ch4sc07_074 with dissolve
    sm "Folkstead. Got it."
    scene ch4sc07_075 with dissolve
    sl "Wait here, I’ll prepare the horse and get you some supplies for the journey."
    scene ch4sc07_076 with dissolve
    $ renpy.pause()
    scene ch4sc07_077 with dissolve
    $ renpy.pause(1)
    mct "This confirms it."
    mct "Eliza was right... she did betray her because Taron had her sister..."
    mct "Which means... your sister is... the reason Eliza got hurt."
    scene ch4sc07_078 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch4sc07_079 with dissolve
    sm "Selena!"
    scene ch4sc07_080 with dissolve
    stop music fadeout 1.0
    sl "Not now, Samarah. I’m almost done."
    scene ch4sc07_081 with dissolve
    play music dark_3 fadein 1.0
    sl "*Gasps* {b}[mc]!?{/b} W-What are you doing here?"
    scene ch4sc07_082 with dissolve
    mc "I thought I'd pay my friend a visit."
    mc "We are friends... right?"
    scene ch4sc07_084 with dissolve
    sl "Yes! We are friends, [mc]!"
    sl "Please let her go! She's my sister!"
    scene ch4sc07_082 with dissolve
    mc "Then you can probably imagine my surprise when I found out you betrayed us."
    mc "That my dear friend Selena is the reason Eliza was almost killed last night."
    mc "The reason she's now crippled from the waist down."
    scene ch4sc07_081 with dissolve
    sl "W-What!? I-I didn’t know!"
    sl "She was fine when I left! I swear!"
    scene ch4sc07_084 with dissolve
    sl "Taron, he had her! He had my sister! She's been a hostage for several moons!"
    sl "He said to lure Eliza away from you... that he'd just use her to trap you!"
    sl "He promised he wouldn’t harm her!"
    scene ch4sc07_082 with dissolve
    mc "*Scoffs* Surprise!"
    mc "The bad guy who kidnapped your sister lied to you!"
    scene ch4sc07_084 with dissolve
    sl "{b}Please! [mc]!{/b} Please let her go! She is innocent! I just wanted her to be free again."
    sl "I never meant for Eliza to get hurt in any way! You have to believe me..."
    scene ch4sc07_085 with dissolve
    sl "I know, given my actions it may not seem like it..."
    sl "But I do care about you and we are friends!"
    scene ch4sc07_084 with dissolve
    sl "Please... I’ll do anything."
    sl "Just... just let her go. She’s my only family, my sister!"
    scene ch4sc07_085 with dissolve
    sl "Surely you know how strong a family bond is."

    ###Choice###
    menu:
        "Kill Samarah. ({color=#f00}Dark Path{/color})":
            scene ch4sc07_082 with dissolve
            $ samarah_alive = False
            mc "I’m an only child."
            scene ch4sc07_083 with dissolve
            with vpunch
            sl "{b}*High-pitched scream* No! Samarah!{/b}"
            scene ch4sc07_086 with dissolve
            $ renpy.pause()
            scene ch4sc07_087 with dissolve
            $ renpy.pause()
            scene ch4sc07_088 with dissolve
            $ renpy.pause()
            scene ch4sc07_089 with dissolve
            sl "*Trembling voice* {b}Samarah! Wake up! W-Wake up right now!{/b}"
            scene ch4sc07_090 with dissolve
            with vpunch
            sl "What have you done! {b}You monster!{/b}"
            scene ch4sc07_089 with dissolve
            mc "These are the consequences of your own actions, Selena."
            scene ch4sc07_090 with dissolve
            sl "*Shaky voice* Y-You bastard..."
            scene ch4sc07_091 with dissolve
            mc "Remember that the next time you feel like betraying someone..."
            mc "Now you know what it feels like when someone hurts those you care about."
            mc "If I ever see you again. You will regret being born..."
            scene ch4sc07_090 with dissolve
            sl "*Shaky voice* Y-You will pay for this..."
            scene ch4sc19_622 with dissolve
            with vpunch
            mc "You see, Selena... I may still have a use for you, you did work for Taron after all."
            scene ch4sc07_090b with dissolve
            mc "However I can't have you going around wanting revenge... You will not harm anyone I care about."
            scene ch4sc07_090c with dissolve
            with vpunch
            mc "{b}AM I CLEAR?!{/b}"
            "Your will manifests itself and seems to put Selena into a trance."
            scene ch4sc07_090a with dissolve
            sl "*Mesmerized* I... will not... harm anyone... you care about..."
            scene ch4sc07_090a with dissolve
            mc "Now be a dear and go give your sister some attention."
            sl "*Mesmerized* I... will put my attention... to my sister..."
            $ dark += 5
            "{b}{color=#f00}Dark Morality{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            stop music fadeout 1.5
            scene black with Dissolve(1.5)

        "Let Samarah go. ({color=#87e1fa}Light Path{/color})":
            scene ch4sc07_082 with dissolve
            stop music fadeout 1.5
            mc "You're lucky Selena."
            mc "I'm not him... I'm not Taron. I won't harm your sister..."
            play music chill_5 fadein 1.0
            mc "But let this be a warning Selena. If you cross me again, or worse. Any further harm comes to Eliza..."
            mc "I won't be this forgiving."
            mc "She's free to go..."
            scene ch4sc07_092 with dissolve
            with vpunch
            sl "Samarah!"
            sl "It’s okay... everything is okay now."
            scene ch4sc07_092 with dissolve
            mct "I almost did to her what was done to me..."
            mct "Blazes... Was I really willing to go that far?"
            mct "She was only trying to save her sister from Taron."
            mct "I would have done the same or worse to protect Eliza."
            mct "Besides, it's not for me to judge her. It should be up to Eliza."
            scene ch4sc07_094 with dissolve
            mc "I have no family left. Taron took that away from me... I won’t do the same to you."
            mc "You’re both free to go."
            scene ch4sc07_092 with dissolve
            sl "It's okay Samarah. It's all going to be okay. He's a friend, he won't hurt you."
            sl "He only attacked you because of my actions, but I know him, you're safe."
            sm "O-Okay... I'm fine, he didn't harm me, he just held on to me."
            menu:
                "I never want to see you again. ({color=#fc584c}Intimidation{/color})":
                    scene ch4sc07_097 with dissolve
                    mc "Go on, get her out of here, far away from the capital."
                    mc "And I suggest you stay with her there. I do not wish to see you again, Selena."
                    scene ch4sc07_096 with dissolve
                    sl "[mc]... Thank you! I know I’ve hurt you, but if you let me... I will make it up to you!"
                    sl "No matter how long it takes..."
                    sl "I will do anything to regain your trust!"
                    scene ch4sc07_097 with dissolve
                    $ intimidation += 1
                    mc "I'm serious. Leave."
                    "Your intimidation was {b}Successful!{/b} Selena and her sister will leave Luxenford, your {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                    scene ch4sc07_095 with dissolve
                    sm "W-We're free? Let's go Selena! I want to get out of here!"
                    sl "It'll all be okay now... we'll find a safe place in Folkstead."

                "Redeem yourself with Eliza. ({color=#ffee54}Leadership{/color})":
                    mc "Get your sister somewhere safe... and then make amends with Eliza."
                    mc "She's the one who has been hurt the most. It will be up to her whether she forgives you or not."
                    mc "If she can't forgive you, there will be no place for you in our lives."
                    scene ch4sc07_095 with dissolve
                    $ renpy.pause()
                    scene ch4sc07_096 with dissolve
                    $ leadership += 1
                    sl "[mc]... Thank you! I know I’ve hurt you, but if you let me. I will make it up to you!"
                    sl "No matter how long it takes..."
                    sl "I will do anything to regain your trust! I will earn yours and Eliza's forgiveness!"
                    sl "I never wanted this... my hands were... forced, but I realise now, I should've come to you."
                    scene ch4sc07_097 with dissolve
                    mc "I'm glad you realise that, whether it's too late or not, we’ll see."
                    mc "The two of you were victims of Taron as well... he's the one I want to hurt."
                    mc "For now, take care of your sister."
                    mc "I'm leaving for a while. If you truly want to make amends... start with Eliza."
                    mc "If she forgives you, then I will... attempt to as well."
                    "You successfully took control of the situation, your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                    scene ch4sc07_096 with dissolve
                    sl "I'll do whatever it takes, for however long it takes, I will do as you say and earn my way back."
                    sl "T-Thank you, thank you so much for not taking it out on Samarah."

            $ light += 5
            "{b}{color=#87e1fa}Light Morality{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            stop music fadeout 1.5
            scene black with Dissolve(1.5)
            $ renpy.pause(1)

    jump ch4sc8

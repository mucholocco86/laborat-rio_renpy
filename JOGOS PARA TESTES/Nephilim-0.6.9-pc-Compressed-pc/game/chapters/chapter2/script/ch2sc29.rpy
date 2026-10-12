#Start Chaper
label ch2sc29:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music tavern_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc29_01 with Dissolve(2.0)
        mc "I’ll order us some drinks while you find us a spot."
        scene ch2sc29_02 with dissolve
        el "Sure! I’ll grab the best spots!"
        el "You can inform your butt that there's a seat waiting for him!"
        scene ch2sc29_03 with dissolve
        mc "I have the utmost faith in your spot-picking skills."
        scene ch2sc29_04 with dissolve
        el "You'd better! *Giggling*"
        el "They're amazing! Unmatched even!"
        scene ch2sc29_05 with dissolve
        ik "Welcome to the Rusty spoon!"
        ik "What can I get you?"
        scene ch2sc29_06 with dissolve
        mc "*Chuckles* Rusty spoon?"
        mc "There’s got to be a story behind a name like that."
        scene ch2sc29_07 with dissolve
        ik "Nothing eventful, I’m afraid."
        ik "When I was setting up the tavern, my wife accidentally forgot she left all the spoons in a crate at our house."
        scene ch2sc29_06 with dissolve
        mc "Outside?"
        scene ch2sc29_07 with dissolve
        ik "Yeah... We were getting ready to move it here, but it started pouring down."
        ik "The worst rainfall we’ve had in decades!"
        scene ch2sc29_08 with dissolve
        ik "It lasted a full week and we had to crash here for the duration of the storm."
        scene ch2sc29_06 with dissolve
        mc "So when you got back to the crate... the spoons were all rusted?"
        scene ch2sc29_09 with dissolve
        ik "Smart lad! Aye... We managed to scrape the rust off with a remedy my wife bought in Luxenford."
        ik "However, that’s what led us to the name."
        scene ch2sc29_10 with dissolve
        mc "I like it."
        mc "It has a certain charm to it."
        scene ch2sc29_11 with dissolve
        ik "*Chuckles* Thanks, lad. You’ll still have to pay for your ales, though."
        scene ch2sc29_12 with dissolve
        ik "Tell you what, why don’t you go sit with your girlfriend? I’ll bring the ales over in a moment."
        scene ch2sc29_13 with dissolve
        $ renpy.pause()
        menu:
            "Play along.":
                scene ch2sc29_14 with dissolve
                mc "She’s beautiful, isn’t she?"
                scene ch2sc29_15 with dissolve
                ik "She sure is, lad. What I wouldn’t give to be young again."
                ik "How did you land a girl like that?"
                scene ch2sc29_16 with dissolve
                mc "I couldn’t really tell you. I guess we’re alike in some ways."
                mc "Our lives have been intertwined since we were little, although we had no idea at the time."
                scene ch2sc29_17 with dissolve
                ik "You know what? First round of ales are on me."
                ik "In the spirit of young love!"
                scene ch2sc29_18 with dissolve
                mc "Thank you. I’ll be sure to let her know!"

            "Just friends.":
                scene ch2sc29_06 with dissolve
                mc "Oh she’s not my girlfriend, we’re just friends traveling together."
                scene ch2sc29_15 with dissolve
                ik "Apologies for assuming. You just seem to have some chemistry."
                scene ch2sc29_06 with dissolve
                mc "I guess we do. We’ve become close friends in a short amount of time."
                scene ch2sc29_10 with dissolve
                mc "We understand each other, and we've built up a solid amount of trust."
                scene ch2sc29_11 with dissolve
                ik "That’s a great foundation for many things: be it friendship, love, or marriage."
                scene ch2sc29_10 with dissolve
                mc "I’m starting to see that. How much for the ales?"
                scene ch2sc29_17 with dissolve
                ik "I’ve changed my mind. First round is on the house. Just make sure to let others know about the Rusty spoon!"
                scene ch2sc29_18 with dissolve
                mc "Thanks! I’ll be sure to mention it to others while we’re on the road."

        scene ch2sc29_19 with dissolve
        $ renpy.pause(1)
        el "*Hums to the ambiance* Hm-hn-hh-hm-hn-hh..."
        mc "Hey, you."
        scene ch2sc29_20 with dissolve
        el "Hi!"
        el "What took you so long?"
        scene ch2sc29_21 with dissolve
        mc "I got to talking with the innkeep."
        mc "He was telling me the story behind the name of the tavern, and then he thought you were my girlfriend."
        scene ch2sc29_27 with dissolve
        $ renpy.pause(1)
        el "!!"
        scene ch2sc29_22 with dissolve
        el "G-Girlfriend? What a silly idea."
        scene ch2sc29_22_b with dissolve
        el "Just out of curiosity... what did you tell him?"
        scene ch2sc29_23 with dissolve
        mc "Wouldn’t you like to know?"
        scene ch2sc29_24 with dissolve
        with vpunch
        el "{b}I WOULD!{/b}"
        scene ch2sc29_25 with dissolve
        el "I- mean, I would..."
        mc "*Chuckles* You're cute."
        el "It’s rude to keep a lady waiting, you know?"
        scene ch2sc29_26 with dissolve
        el "Soo?"
        ###CHOICE###
        menu:
            "That you are my girlfriend.({color=#ff8cdd}Romance{/color})":
                $ eliza_relationship = True
                "Eliza’s trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                $ eliza_trust += 3
                scene ch2sc29_27 with dissolve
                $ renpy.pause(1)
                "!!"
                scene ch2sc29_28 with dissolve
                el "Y-You did?"
                scene ch2sc29_29 with dissolve
                mc "Mmh, it felt right."
                mc "Why? Shouldn’t I have?"
                scene ch2sc29_30 with dissolve
                el "N-No, it’s okay."
                el "*Whispers quietly* {size=-10}{b}I’m really happy you did.{/b}{/size}"
                scene ch2sc29_31 with dissolve
                elt "Heavens... Girlfriend?"
                elt "Nyahh! I want to kiss him so badly!"
                elt "Just jump onto his lap and wrap my legs and arms tightly around him, while our lips intertwine passionately."
                scene ch2sc29_32 with dissolve
                $ eliza_path = True
                mc "Hmm?"
                scene ch2sc29_31 with dissolve
                $ renpy.pause(1)
                mc "You're day-dreaming about our future, aren't you? *Chuckles*"
                scene ch2sc29_33 with dissolve
                el "Hmm?! N-No! I-... that would be crazy... y-yeah... totally crazy..."
                el "A-Anyway! I’m ready for those ales!"
                scene ch2sc29_34 with dissolve
                mc "Me too, he should be here any moment now."

            "That we’re good friends.":
                $ eliza_trust += 1
                scene ch2sc29_35 with dissolve
                el "I wonder why he thought we were a couple?"
                scene ch2sc29_29 with dissolve
                mc "He said we had chemistry."
                scene ch2sc29_25 with dissolve
                el "I suppose we do. I just didn’t know it was obvious to others."
                scene ch2sc29_29 with dissolve
                mc "Maybe he's just perceptive."
                scene ch2sc29_30 with dissolve
                el "Yeah. That’s probably it..."
                el "Innkeepers talk to people all the time. They're probably used to picking up on such things."
                "Eliza’s trust increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

        scene ch2sc29_36 with dissolve
        ik "Here you are, do call me if you youngsters need anything else."
        scene ch2sc29_37 with dissolve
        el "Thank you sir! This is exactly what we need right now!"
        scene ch2sc29_38 with dissolve
        el "Oh! Oh! What should we toast to?"

        ###CHOICE###
        menu:
            "To us!":
                scene ch2sc29_39 with dissolve
                el "To us! Cheers!"
            "To starting our adventure!":
                scene ch2sc29_39 with dissolve
                el "I like it! Cheers!"
            "To getting our revenge!":
                scene ch2sc29_39 with dissolve
                el "The sweet taste of revenge! Cheers!"

        scene ch2sc29_47 with dissolve
        mc "You’ve earned it... being on the road for days isn't easy, yet you barely complaim."
        mc "Let’s enjoy ourselves, Cheers!"
        scene ch2sc29_41 with dissolve
        $ renpy.pause()
        scene ch2sc29_42 with dissolve
        $ renpy.pause()
        scene ch2sc29_43 with dissolve

        el "UUaaaAAaahh! This is so good!"
        scene ch2sc29_42 with dissolve
        $ renpy.pause(1)
        el "*Gulp, gulp* Hnngh..."
        scene ch2sc29_43 with dissolve
        el "You're right! We've earned a little bit of comfort!"
        stop music fadeout 2.0
        scene ch2sc29_44 with Dissolve(1.5)
        $ renpy.pause(1)
        play music home_1 fadein 1.0
        el "Is now a good time to ask you about the guy who attacked us at the lake?"
        scene ch2sc29_45 with dissolve
        el "He clearly wasn’t just a regular thug... the way he fought you, on top of the water..."
        el "At one point, I-I thought..."
        scene ch2sc29_46 with dissolve
        with vpunch
        el "He almost drowned you [mc]!"
        el "That’s not okay! I don’t accept that!"
        scene ch2sc29_47 with dissolve
        mc "Calm down, you little firecracker."
        mc "I’ll tell you... you're right, he wasn't a regular thug."
        scene ch2sc29_48 with dissolve
        mc "The guy who attacked us is... well, was a Shado-jin."
        mc "They're an elite group within the Mercenaries Guild."
        mc "They are technically free-lance, but from what I know, it's mostly that guild who makes use of them."
        scene ch2sc29_49 with dissolve
        mc "Only their best and most hardened members advance to become Shado-jins."
        scene ch2sc29_26 with dissolve
        el "I take it this wasn’t your first run-in with them?"
        el "Given you've been on the run and seemed familiar with them."
        scene ch2sc29_48 with dissolve
        mc "You’re right about that, apparently he had a brother who was also in that group."
        mc "And his brother tracked your father and me down, around two years ago."
        scene ch2sc29_49 with dissolve
        mc "I wasn’t a match for him, but Oren handled him."
        mc "The one who attacked us..."
        mc "He was after revenge for his brother, the bounty on me was just a bonus."
        scene ch2sc29_27 with dissolve
        $ renpy.pause(1)
        elt "Those bastards have been hunting [mc] ever since he was a kid..."
        scene ch2sc29_22_b with dissolve
        el "What happened after you defeated him at the lake?"
        el "You absorbed something from him? And then you collapsed, you were out cold for over an hour."

        if nz_alive == True:

            scene ch2sc29_48 with dissolve
            mc "I siphoned the mana cells in his body. He’ll live, but he won’t ever be able to use magic again."
            mc "He’ll be physically weaker as well."
            scene ch2sc29_49 with dissolve
            mc "I don’t gain as much strength from doing that compared to absorbing a soul, but it still makes me stronger."
        else:
            scene ch2sc29_49 with dissolve
            mc "I absorbed his soul after he died. It increases my strength and allows me to grow my abilities."
            mc "But it’s very painful and it can be overwhelming when it happens."


        scene ch2sc29_49
        mc "I don't have much experience doing... that."
        scene ch2sc29_22_b with dissolve
        el "I see... you really had me worried when you collapsed."
        el "Has that happened before?"
        scene ch2sc29_49 with dissolve
        mc "Not that I know of... All this is a learn-as-I-go process for me."
        mc "It’s not like I went around absorbing souls as a kid, you know?"
        scene ch2sc29_50 with dissolve
        mc "Your father always warned me to be careful with it."
        mc "Because power can be corrupting and addictive."
        scene ch2sc29_25 with dissolve
        el "I won’t allow you to end up like Balthazar."
        scene ch2sc29_51 with dissolve
        mc "I know you won't. I feel better knowing you have my back."
        scene ch2sc29_31 with dissolve
        elt "He really does appreciate me."
        scene ch2sc29_33 with dissolve
        el "I have your back, front, and sides!"
        scene ch2sc29_52 with dissolve
        $ renpy.pause()
        mct "If I have to go through all this with anyone, I'm glad it's her."
        scene ch2sc29_53 with dissolve
        mc "Anyway, I think we’ll reach Luxenford tomorrow."
        scene ch2sc29_35 with dissolve
        el "How do you know that?"
        el "*Giggling* Are you going to tell me that being a Nephilim gives you psychic powers?"
        scene ch2sc29_32 with dissolve
        $ renpy.pause()
        scene ch2sc29_29 with dissolve
        mc "*Chuckles* Not that I’m aware of."
        mc "I overheard someone talking about the capital when I was speaking to the innkeeper."
        scene ch2sc29_29 with dissolve
        mc "Sounded like they were on a day trip to deliver some goods."
        scene ch2sc29_22 with dissolve
        el "Then it should be close!"
        scene ch2sc29_29 with dissolve
        mc "Yeah, by the end of tomorrow we should arrive at the gates to the city."
        mc "I’m excited, honestly."
        scene ch2sc29_24 with dissolve
        el "Wait, how many ales did you have?"
        scene ch2sc29_23 with dissolve
        mc "One."
        mc "Why? Do I look drunk or something?"
        scene ch2sc29_28 with dissolve
        el "No, but-... You don't usually get excited about..."
        el "Well, anything!"
        scene ch2sc29_29 with dissolve
        mc "Reaching the capital is the first big step towards my goal."
        scene ch2sc29_26 with dissolve
        el "{b}Our{/b} goal."
        scene ch2sc29_32 with dissolve
        mc "Hmm?"
        scene ch2sc29_26 with dissolve
        el "It’s {b}our{/b} goal, [mc]."
        el "You’re forgetting, the person who killed your parents is also the reason why my father left Mother and me."
        scene ch2sc29_25 with dissolve
        el "And that led to Mother drinking and whoring her sorrows away, and eventually leaving me all alone."
        el "He ruined my childhood as much as he did yours."
        scene ch2sc29_53 with dissolve
        mc "You’re right."
        mc "I’m sorry, Eliza. {b}Our{/b} goal."
        scene ch2sc29_35 with dissolve
        el "I’ll drink to that! Cheers!"
        scene ch2sc29_41 with dissolve
        $ renpy.pause(1)
        scene ch2sc29_42 with dissolve
        $ renpy.pause(1)
        scene ch2sc29_41 with dissolve
        $ renpy.pause(2)
        scene ch2sc29_43 with dissolve
        el "UUaaaAAaahh! *Giggling*"
        scene ch2sc29_31 with dissolve
        "..."
        "......"
        "........."
        scene ch2sc29_33 with dissolve
        el "Hey, [mc]."
        scene ch2sc29_54 with dissolve
        mc "Yeah?"
        scene ch2sc29_33 with dissolve
        el "Why don’t we..."
        el "head upstairs?"
        scene ch2sc29_31 with dissolve
        mc "It's getting a little crowded down here..."
        elt "*Giggling softly* Yeah... way too crowded."
        scene ch2sc29_33 with dissolve
        el "Follow me."
        scene ch2sc29_55 with Dissolve(1.5)
        $ renpy.pause(1)
        mc "Right behind you."
        scene ch2sc29_56 with dissolve
        el "Good, enjoy the view."
        scene ch2sc29_57 with dissolve
        mc "We men are simple creatures..."
        mc "You know how much I appreciate a good view."
        scene ch2sc29_58 with dissolve
        el "*Giggling* I've noticed! And since you've been so sweet recently, I won't even pretend to be upset."
        stop music fadeout 1.0
        scene black with Dissolve(2)
        $ renpy.pause(1)
        scene ch2sc29_59 with Dissolve(2)
        play music summon_2 fadein 1.0
        $ renpy.pause(1)
        el "Woah! This room is so spacious!"
        el "I think we've been given the master-suit! Don't you?"
        scene ch2sc29_60 with dissolve
        $ renpy.pause(0.5)
        mc "*Chuckles* I wouldn't be surprised."
        scene ch2sc29_61 with dissolve
        $ renpy.pause(0.5)
        mc "The innkeep seemed like a fan of yours."
        scene ch2sc29_61_1 with dissolve
        el "What are you waiting for?"
        el "This bed literally has our names written on it!"

        ###CHOICE###
        menu:
            "Embrace Eliza. ({color=#ff8cdd}Romance{/color})":
                $ eliza_relationship = True
                scene ch2sc29_62 with dissolve
                $ renpy.pause(0.5)
                el "It's been a long day, I'm so happy we made it to a tavern."
                scene ch2sc29_63 with dissolve
                $ renpy.pause(0.5)
                el "*Whispers softly* {size=-10}{b}Finally... we're alone.{/b}{/size}"
                "She melts against you immediately as your arms wrap around her, as if she's been longing for you to be close."
                scene ch2sc29_64 with dissolve
                el "Mmhh... [mc]."
                "The sound of her soft moans as your bodies rub against each other is a melody you’ve been longing to hear."
                scene ch2sc29_65 with dissolve
                $ renpy.pause()
                "Her fingers slowly reach your hips, where she starts squeezing firmly while pressing herself against you."
                scene ch2sc29_66 with dissolve
                $ renpy.pause()
                el "Aaaiihh... Mmhmhh."
                "Leaning back into you, she whimpers as you grab her upper waist, holding onto her firmly."
                scene ch2sc29_67 with dissolve
                el "Hi you."
                scene ch2sc29_68 with dissolve
                mc "Hey Gorgeous."
                scene ch2sc29_69 with dissolve
                elt "Divines! I feel like I'm turning to pudding in his arms!"
                scene ch2sc29_70 with dissolve
                el "*Bites lip* Nnyah... This is just what I needed."
                scene ch2sc29_71 with dissolve
                mc "You didn’t get enough during training earlier?"
                scene ch2sc29_72 with dissolve
                el "Yes-No. It did something to me... You did something to me, [mc]."
                el "Our kisses earlier they... ignited something within me."
                el "I-I can’t stop thinking about your hands on me. How your touch sends pulses through my body..."
                scene ch2sc29_73 with dissolve
                mc "Like this?"
                scene ch2sc29_73 with dissolve
                elt "{b}MMhHhH!{/b} His touch is electrifying!"
                scene ch2sc29_74 with dissolve
                el "Yes! Every time you’ve spoken to me since then..."
                el "I've caught myself looking at your lips, just wanting to feel them on me."
                scene ch2sc29_75 with dissolve
                mc "Then I shouldn't keep you waiting."
                el "Aaah!! Y-Yes... that feels even better than I imagined."
                scene ch2sc29_76 with dissolve
                mc "*Whispers & Kisses* {size=-10}{b}You’ve been thinking about this?{/b}{/size}"
                mc "*Whispers & Kisses* {size=-10}{b}About my hands touching your smooth skin, while my lips taste your neck?{/b}{/size}"
                scene ch2sc29_77 with dissolve
                el "N-No."
                el "N-No. Aaah..."
                el "N-No... Aaah... Yes. Yes I have."
                el "Please don’t stop."
                scene ch2sc29_76 with dissolve
                elt "Every time his lips brush my skin, they send tingles inside me... It’s... Mmmhh!"
                scene ch2sc29_78 with dissolve
                $ renpy.pause()
                scene ch2sc29_79 with dissolve
                $ renpy.pause()
                elt "*Heavy breathing* AhhhhHhhMmMhh."
                elt "H-He's touching my breasts... Please like them!"
                with vpunch
                elt "Oh! He definitely likes them! If he keeps this up... Aaah!"
                mct "Her supple soft breast fits perfectly into my hand."
                scene ch2sc29_80 with dissolve
                el "[mc]... You’re the first to touch me like this."
                mct "Blazes, she’s sexy."
                mct "Adorable and innocent... untouched by another man."
                scene ch2sc29_81 with dissolve
                mc "I want to be the only one who touches you like this."
                scene ch2sc29_82 with dissolve
                el "Mmmhhh-Nyah... I would never let anyone else get close."
                el "It’s you and me, [mc]."
                el "{b}You... and... me.{/b}"
                scene ch2sc29_83 with dissolve
                el "*Moans softly* I'm yours."
                scene ch2sc29_84 with dissolve
                $ renpy.pause()
                "You feel the wetness of her tongue as she traces it along your lips."
                scene ch2sc29_85 with dissolve
                $ renpy.pause()
                scene ch2sc29_86 with dissolve
                $ renpy.pause()
                scene ch2sc29_85 with dissolve
                mct "Her kisses are different from before."
                mct "They’re filled with passion, playfulness, and desire."
                scene ch2sc29_84 with dissolve
                $ renpy.pause(1)
                el "*Licks* Nnnh..."
                scene ch2sc29_85 with dissolve
                $ renpy.pause(1)
                scene ch2sc29_84 with dissolve
                $ renpy.pause(1)
                el "*Licks* Only yours."
                scene ch2sc29_87 with dissolve
                mc "That was..."
                scene ch2sc29_88 with dissolve
                el "Magical."
                scene ch2sc29_89 with dissolve
                mc "Magical."
                mc "I feel like you've enchanted me."
                scene ch2sc29_88 with dissolve
                el "*Giggling* Does it?"
                el "Maybe I did..."
                el "Maybe... you're under my seduction spell?"
                scene ch2sc29_90 with dissolve
                mc "Now that would explain why I'm feeling the way I do..."
                mc "*Chuckles* Are you sure you aren’t a sorceress?"
                scene ch2sc29_91 with dissolve
                el "*Snickering* Not that I’m aware!"
                el "I'm afraid all I've got is my feminine charms!"
                scene ch2sc29_90 with dissolve
                mc "Those feminine charms are working as intended then."
                mc "It feels like I’m under your spell."
                scene ch2sc29_92 with dissolve
                el "Oh? I like the sound of that."
                el "If that’s the case, then..."
                scene ch2sc29_88 with dissolve
                el "*Sensual Whisper* {size=-5}{b}I have a certain spell in mind that I think you’re going to love.{/b}{/size}"
                menu:
                    "Accept her spell. ({color=#ff8cdd}Lewd Scene{/color})":
                        scene ch2sc29_90 with dissolve
                        mc "An incredibly sexy sorceress wants to enchant me? How can I refuse?"
                        scene ch2sc29_88 with dissolve
                        el "You can't!"
                        scene ch2sc29_92 with dissolve
                        el "Go ahead and sit on the bed... There’s something I need to do."
                        el "I won't be long."
                        scene black with Dissolve(1.5)
                        $ renpy.pause(0.5)
                        "You sit on the bed and a few moments later Eliza enters the room heading straight towards you."
                        scene ch2sc29_93_1 with Dissolve(1.5)
                        $ renpy.pause()
                        mct "Damn... she removed her pants, but kept her boots on?"
                        scene ch2sc29_93_2 with dissolve
                        $ renpy.pause()
                        mct "Now that's a look I can get behind..."
                        scene ch2sc29_93 with dissolve
                        $ renpy.pause()
                        el "{b}*Sensual voice*{/b} Are you ready to be enchanted?"
                        scene ch2sc29_94 with dissolve
                        mc "I-I think I already am."
                        el "I'll just... make myself comfortable riiiiiight down here..."
                        scene ch2sc29_95 with dissolve
                        "Eliza looks up to you as she kneels down between your legs."
                        el "You won’t be needing these."
                        scene ch2sc29_96 with dissolve
                        el "{b}*Gasps* OH!{/b} L-Looks like my spell is working as intended."
                        "Eliza’s eyes fills with excitement as she studies your manhood."
                        scene ch2sc29_97 with dissolve
                        $ renpy.pause()
                        el "Woaah."
                        scene ch2sc29_98 with dissolve
                        elt "No way! {b}That{/b} is supposed to fit inside me!? No way... Nuh-uh!"
                        elt "It’s been poking me every time we sleep against each other."
                        elt "I didn’t think it would look this... yummy."
                        scene ch2sc29_98 with dissolve
                        $ renpy.pause(1)
                        scene ch2sc29_99 with dissolve
                        $ renpy.pause(1)
                        scene ch2sc29_98 with dissolve
                        $ renpy.pause(1)
                        scene ch2sc29_99 with dissolve
                        $ renpy.pause(1)
                        scene ch2sc29_100 with dissolve
                        with vpunch
                        elt "Heavens! {b}It twitched!{/b}"
                        scene ch2sc29_101 with dissolve
                        mc "Aahhh.."
                        elt "Oh no!? Did I hurt him?!"
                        scene ch2sc29_102 with dissolve
                        el "D-Did I hurt you?"
                        scene ch2sc29_103 with dissolve
                        mc "No... it feels incredible when you touch me."
                        scene ch2sc29_104 with dissolve
                        elt "He likes it!"
                        scene ch2sc29_105 with dissolve
                        el "Touch you... like this?"
                        scene ch2sc29_106 with dissolve
                        with vpunch
                        "Eliza grabs hold of you firmly, but the softness of her palm makes it feel delicate."
                        mc "Aaahh..."
                        mc "Y-Yeah... Just like that."
                        scene ch2sc29_107 with dissolve
                        $ renpy.pause()
                        elt "It’s so warm... it’s radiating heat... this thing could almost light a campfire."
                        elt "He seems to really enjoy it when I stroke it up’n'down like this."
                        ###ANIMATION###
                        show el_hj_ani with fade
                        $ renpy.pause(3, hard=True)
                        "She strokes you slowly, carefully making sure you feel every squeeze of her fingers."
                        mc "Fffuu... you're a natural... keep going..."
                        elt "He likes my touch! Mmhh... and I like touching him..."
                        elt "Feeling him like this... pulsating with life right in my hand... it's incredible."
                        $ renpy.pause()
                        scene ch2sc29_107 with dissolve
                        mc "*Moans* Eliza ... Mhh."
                        scene ch2sc29_108 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_109 with dissolve
                        el "I want to taste you."
                        el "C-Can I... put you in my mouth?"
                        scene ch2sc29_110 with dissolve
                        mc "Go ahead, kitten. I’m in your hands, literally."
                        mct "By the divines... the feel of her squeezing my cock while looking at me like that ..."
                        scene ch2sc29_111 with dissolve
                        el "I wonder if you taste as delicious as you smell?"
                        "She doesn't wait for an answer. As the words leave her pretty little lips, her thumb gently rubs your tip."
                        scene ch2sc29_112 with dissolve
                        elt "Hi there, buddy. I have a feeling you and I will become great friends."
                        scene ch2sc29_113 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_114 with dissolve
                        $ renpy.pause()
                        "She carefully plants her soft wet lips on the tip of your cock."
                        "You can tell how badly she wants to please you, despite her inexperience."
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause()
                        "Another kiss lands, sending pulses of pleasure through your cock."
                        "She keeps a tight hold on your shaft with her slender fingers as her lips continue to make out with your tip."
                        scene ch2sc29_114 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_114 with dissolve
                        elt "Mhhmwaaah! Mmhh! I love it! I want to keep kissing him like this."
                        scene ch2sc29_115 with dissolve
                        elt "Maybe I should lick him, like when we kiss?"
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause()
                        elt "{b}Yum!!{/b}"
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_114 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_117 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_114 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_117 with dissolve
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_115 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_116 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_117 with dissolve
                        elt "*Soft moan* Mhaamh. I don’t think I can hold myself back any longer."
                        mc "*Moans* Fff... Eliza... you're amazing."
                        scene ch2sc29_118 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_119 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_120 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_121 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_122 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_118 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_119 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_120 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_121 with dissolve
                        $ renpy.pause(0.5)
                        scene ch2sc29_122 with dissolve
                        $ renpy.pause(0.5)
                        mct "This little vixen."
                        mct "Ahhh... she could literally have kings at her mercy."
                        scene ch2sc29_121 with dissolve
                        mct "Yet, she’s here with me."
                        mct "Kneeling between my legs and only caring about pleasuring me."
                        scene ch2sc29_123 with dissolve
                        $ renpy.pause()
                        "She pauses for a few moments, looking up at you with a mischievous smile while she rests your warm cock against her chin."
                        elt "If he isn't already enchanted, he's about to be!"
                        elt "I need him inside my mouth. {b}Now!{/b}"
                        scene ch2sc29_124 with dissolve
                        "She places her wet lips at your tip, preparing herself to fill her mouth with you."
                        ###ANIMATION###
                        show el_bj_ani with fade
                        $ renpy.pause(5, hard=True)
                        "She slowly opens her little mouth, allowing you within."
                        "Her wet lips surround your cock as she pushes you further inside."
                        "You can feel how she pushes her tongue against your cock, massaging it softly."
                        mc "Eliza... Ahhhh! You're going to make me cum if you keep sucking like that."
                        scene ch2sc29_124 with dissolve
                        elt "I can't wait to taste his cum!"
                        scene ch2sc29_125 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_126 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_127 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_128 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_129 with dissolve
                        $ renpy.pause()
                        "She listens intently to your moans as she continues to suck harder."
                        scene ch2sc29_128 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_129 with dissolve
                        $ renpy.pause()
                        "She presses her wet soft tongue firmly against your tip while sucking intensely, until you finally cum inside her."
                        scene ch2sc29_129 with dissolve
                        with vpunch
                        $ renpy.pause(0.5)
                        with vpunch
                        $ renpy.pause(0.5)
                        el "Mfffhh... {b}MmffhH!{/b}"
                        scene ch2sc29_130 with dissolve
                        $ renpy.pause()
                        "With her mouth filled with your seed, she looks up into your eyes."
                        mct "*Chuckles* She's awaiting my approval to swallow?"
                        mc "Go ahead, Kitten. You've earned it."
                        scene ch2sc29_131 with dissolve
                        $ renpy.pause()
                        el "{b}*Gulp*{/b}"
                        scene ch2sc29_132 with dissolve
                        $ renpy.pause(1)
                        el "Aaaaaaaaaaahhhhh."
                        mct "Five hells... she's letting me see that she swallowed every last drop."
                        scene ch2sc29_133 with dissolve
                        $ renpy.pause(1)
                        "She kisses you one last time, her gaze still locked onto you..."
                        "Proudly observing the pleasure you're feeling."
                        mct "This girl!"
                        mct "I'm a lucky man."
                        scene ch2sc29_134 with dissolve
                        $ renpy.pause()
                        elt "The look on his face. I’ve never seen him that happy before."
                        elt "I think he loved it as much as I did."
                        scene ch2sc29_109 with dissolve
                        el "D-Did I do alright?"
                        scene ch2sc29_103 with dissolve
                        mc "You're kidding, right? You’ve left me speechless."
                        mc "I've never felt this good, Eliza. You were incredible."
                        scene ch2sc29_109 with dissolve
                        el "Hold me? Please."
                        el "I'd like to... be close to you."
                        scene ch2sc29_89 with dissolve
                        mc "Anytime, anywhere, Eliza."
                        mc "You belong in my arms."
                        scene ch2sc29_88 with dissolve
                        el "That good, huh?"
                        el "I couldn't stop myself... you were delicious."
                        scene ch2sc29_89 with dissolve
                        mc "You were incredible, Eliza."
                        mc "That thing you did with your tongue... what was that?"
                        scene ch2sc29_92 with dissolve
                        el "I have no idea. You just tasted really good, so I wanted to keep licking."
                        el "Judging by how much you filled my mouth at the end, I think I can safely assume you enjoyed it?"
                        scene ch2sc29_89 with dissolve
                        mc "Enjoyed it?"
                        mc "I'm already thinking we should do it again."
                        scene ch2sc29_91 with dissolve
                        $ renpy.pause(0.5)
                        el "*Giggling* Mh-hm!"
                        el "Definitely!"
                        scene ch2sc29_88 with dissolve
                        el "I loved having you in my mouth... you tasted delicious! I was a little nervous..."
                        el "But that went away as soon as I tasted you, then my instincts to suck and lick took over..."
                        el "We just might have to make it a regular thing..."
                        scene ch2sc29_90 with dissolve
                        mc "No objection from me."
                        mc "I'm also looking forward to tasting you."
                        scene ch2sc29_88 with dissolve
                        el "Keeping talking like that, and you'll be having me for dessert soon."
                        el "I really want to kiss you... is that okay-"
                        scene ch2sc29_85 with dissolve
                        $ renpy.pause(0.2)
                        with vpunch
                        el "Mmffhh! Mmfhh... nnhh..."
                        "You swiftly grab her and pull her close to you, embracing her in an intimate kiss."
                        scene ch2sc29_86 with dissolve
                        $ renpy.pause(0.5)
                        el "*Kisses softly* Mmhh... you... don't mind?"
                        scene ch2sc29_85 with dissolve
                        $ renpy.pause(0.5)
                        mc "Mmmh... don't be ridiculous... I'm not a little boy."
                        scene ch2sc29_86 with dissolve
                        $ renpy.pause(0.5)
                        el "*Moans softly* Mmh... no... you're a man, a real man... *Mwaah*"
                        el "My... man."
                        scene ch2sc29_85 with dissolve
                        $ renpy.pause(0.5)
                        mc "Mmhh... my little kitten."
                        scene ch2sc29_89 with dissolve
                        mc "Ready for bed?"
                        "Eliza nods whilst caressing the back of your hair."
                        scene black with Dissolve(1.5)
                        $ renpy.pause(1)
                        scene ch2sc29_135 with Dissolve(1.5)
                        $ renpy.pause(0.5)
                        el "These scars... do they hurt?"
                        scene ch2sc29_136 with dissolve
                        mc "Not anymore."
                        scene ch2sc29_135 with dissolve
                        el "What happened? Who did this to you?"
                        el "They'd better be dead already. Otherwise, I'll make sure they are soon enough."
                        scene ch2sc29_136 with dissolve
                        mc "I... We were attacked by goblins."
                        mc "About two years ago, your father and I was discovered in the Sen'ju region, by the Shado-jin we spoke of earlier."
                        mc "We had been staying at the village {b}'Nakajima'{/b} for five years, we'd been lucky."
                        scene ch2sc29_137 with dissolve
                        mc "But since we had been found, we had to leave, back to life on the move... Eventually we found a village."
                        mc "The village we stayed at, {b}Lakeshire{/b}, was in a rural area."
                        mc "The village was fairly recently established at the time we arrived, perfect spot to lay low."
                        scene ch2sc29_136 with dissolve
                        mc "But they did have issues with a nearby goblin settlement."
                        mc "Apparently, the goblins in the area weren't happy with people settling there."
                        scene ch2sc29_136 with dissolve
                        mc "One night I woke up to some women screaming."
                        mc "I could barely see anything because there was thick dark smoke everywhere."
                        mc "Huts and buildings were ablaze, and there were goblins charging from all sides."
                        scene ch2sc29_138 with dissolve
                        mc "The screams of the innocent people being slaughtered by those beasts were deafening."
                        mc "Some women were dragged off into the forest, I can only imagine what happened to them..."
                        scene ch2sc29_136 with dissolve
                        mc "In the confusion, I'd left my sword back in the hut."
                        mc "And it wasn’t long till I was surrounded by the green-skinned, stinking creatures."
                        mc "I was able to fight off the first few. But soon I was overwhelmed by their sheer numbers."
                        scene ch2sc29_138 with dissolve
                        mc "Their claws tore deep, leaving me with these scars all over."
                        scene ch2sc29_139 with dissolve
                        elt "He's had to endure such horrors from such a young age."
                        elt "His parents... whole villages being destroyed, and innocents dying right in front of his eyes."
                        elt "I can't imagine such horror..."
                        scene ch2sc29_138 with dissolve
                        mc "Just as I was about to succumb to the pain, they all suddenly fell to the ground next to me."
                        scene ch2sc29_140 with dissolve
                        el "Huh? How so?"
                        scene ch2sc29_136 with dissolve
                        mc "Your father."
                        mc "Somehow, he slew them all in a whirlwind of slashes from his blade."
                        mc "I'd never seen him move like that before... as you know he was rather bulky and strong but..."
                        mc "Moving that swiftly for a man of his size, impressive to say the least."
                        scene ch2sc29_141 with dissolve
                        mc "Next thing I knew, I woke up in a new place."
                        mc "I'd been passed out for several days, with a heavy fever from my wounds."
                        mc "Oren told me that anyone else would've been dead, but due to my natural regeneration, I survived."
                        scene ch2sc29_142 with dissolve
                        $ renpy.pause()
                        scene ch2sc29_143 with dissolve
                        el "W-What happened to the village? All the civilians and kids?"
                        scene ch2sc29_141 with dissolve
                        mc "They were overrun. According to your father, there was little he could do."
                        mc "His primary concern was to get me to safety."
                        mc "If I hadn’t been so weak, we could have stayed and helped them."
                        mc "If I had just trained harder... listened to his instructions more attentively... I could've-"
                        scene ch2sc29_140 with dissolve
                        el "Don’t do that."
                        el "You're not to blame for the brutal actions of goblins."
                        el "The only ones at fault here are the goblins!"
                        el "I'm sure you and my father taking down a chunk of those filth means some of the villagers managed to escape."
                        scene ch2sc29_136 with dissolve
                        mc "That’s what I try to tell myself."
                        mc "That hopefully us being there might've saved a few of them... but I never got to confirm it."
                        scene ch2sc29_135 with dissolve
                        el "Is this why you’re always so hard on yourself?"
                        el "Why you don't think you deserve to be happy?"
                        scene ch2sc29_136 with dissolve
                        mc "One of my reasons."
                        mc "When you’re different... when you can do things that others can’t..."
                        scene ch2sc29_137 with dissolve
                        mc "You have a responsibility to help those in need."
                        mc "Something your father taught me, countless times."
                        scene ch2sc29_135 with dissolve
                        el "I agree with that line of thinking, in general."
                        el "But you also need to realize the world isn’t black and white."
                        scene ch2sc29_140 with dissolve
                        el "Each situation is unique and you have to act accordingly."
                        el "The best you can do is to use whatever information you have available at the time."
                        el "And make decisions that benefit those who need it."
                        scene ch2sc29_145 with dissolve
                        mc "*Chuckles* You sound a lot like him, you know?"
                        scene ch2sc29_140 with dissolve
                        el "He was my father for the first half of my life."
                        scene ch2sc29_136 with dissolve
                        mc "He never stopped."
                        scene ch2sc29_135 with dissolve
                        el "What-"
                        scene ch2sc29_136 with dissolve
                        mc "He always kept track of how you were doing."
                        mc "How do you think I knew where to look for you, even after he'd passed away?"
                        scene ch2sc29_139 with dissolve
                        elt "I never considered how [mc] actually found me."
                        elt "It's not like it's easy to find someone in the woods... and they wouldn't have been close to Whitehills or Riverside."
                        scene ch2sc29_136 with dissolve
                        mc "He just couldn’t contact you, for your own safety."
                        mc "With Shado-jins on our tail, seeking you out could have painted a target on you, to lure us out."
                        scene ch2sc29_142 with dissolve
                        $ renpy.pause(1)
                        elt "He's right... I've spent so much time being angry with father for abandoning us."
                        elt "But now that I know the story and reason... at least some of it, it makes sense."
                        scene ch2sc29_144 with dissolve
                        el "[mc], thank you for telling me..."
                        el "Somehow, it feels less of a burden going through this with you."
                        scene ch2sc29_145 with dissolve
                        mc "I'm glad you feel better after hearing some of it."
                        mc "But yeah, that is how I got most of my scars..."
                        mc "How about we try and get some sleep, before the sun graces us with it's presence."


                    "Decline. (Skip Lewd Scene, Still {color=#ff8cdd}Romance{/color})":
                        scene ch2sc29_61 with dissolve
                        mc "I’m sure you do. Ready for bed?"

                scene ch2sc29_144 with dissolve
                el "Yes! I have a feeling I’ll sleep like a baby!"
                scene ch2sc29_145 with dissolve
                mc "I wonder why."
                scene ch2sc29_144 with dissolve
                el "Keep wondering!"
                el "Now, come cuddle and protect me!"
                scene ch2sc29_145 with dissolve
                mc "It would be rude to refuse such a beautiful lady."
                scene ch2sc29_146 with dissolve
                $ renpy.pause(0.5)
                "You pull Eliza close and spoon her under the comfort of the blanket."
                el "*Giggling happily* Nnnh..."
                scene ch2sc29_147 with dissolve
                el "I see my lessons of etiquette have been paying off."
                mc "*Chuckles* You're just lucky..."
                scene ch2sc29_148 with dissolve
                mc "You caught me in a good mood."
                el "Uh-huh? *Giggles*"
                scene ch2sc29_149 with dissolve
                el "More like I put you in a good mood!"
                mc "*Chuckles* Mhm-hm..."
                scene ch2sc29_150 with dissolve
                mc "If you keep wiggling your ass like that, we won’t get any sleep."
                scene ch2sc29_149 with dissolve
                el "What do you mean? I’m innocent of that accusation!"
                "*Continues to wiggle her ass slowly against you.*"
                el "T-Toally- mmmh... Ino-... mmh... Innocent."
                scene ch2sc29_150 with dissolve
                mc "I’m not sure how you always manage to do that."
                scene ch2sc29_149 with dissolve
                el "Manage to do what?"
                scene ch2sc29_151 with dissolve
                mc "More often than not, you manage to take my mind off all the bad things that have happened."
                scene ch2sc29_152 with dissolve
                elt "You do the same for me, [mc]... More than you know."
                elt "Just being wrapped up in your arms like this... I couldn’t be happier."
                scene ch2sc29_153 with dissolve
                el "It’s because you care for me as much as I do you, [mc]."
                el "It’s not something you can explain."
                el "It’s a feeling... a bond we share with each other."
                scene ch2sc29_154 with dissolve
                mc "I don’t like it when you’re right."
                mc "But I can't help but agree..."
                scene ch2sc29_153 with dissolve
                el "You should be used to it by now."
                el "I'm glad you came into my life..."
                scene ch2sc29_154 with dissolve
                mc "Mmh... me too, goodnight, Kitten."
                scene ch2sc29_155 with dissolve
                el "Night, night, handsome."
                stop music fadeout 2.0
                "You squeeze her gently in your arms as you both fall asleep."
                scene black with Dissolve(2)
                jump ch2sc30

            "Go to bed. ({color=#f00}Ends Romance Path{/color})":
                $ eliza_relationship = False
                scene black with Dissolve(2)
                $ eliza_path = False
                "Both of you are exhausted from all that's happened recently and immediately pass out."
                jump ch2sc30

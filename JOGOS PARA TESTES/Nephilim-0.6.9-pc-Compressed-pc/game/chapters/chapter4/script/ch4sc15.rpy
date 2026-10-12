label ch4sc15:

    window hide dissolve
    play music explore_1 fadein 1.0
    #stop music fadeout 1.0
    scene black with Dissolve (1.0)
    scene ch4sc15_001 with Dissolve(2.0)
    $ renpy.pause(1)
    scene ch4sc15_002 with Dissolve(2.0)
    $ renpy.pause()
    scene ch4sc13_101 with Dissolve(2)
    al_t "Hmm. Shrinking potion... Life-root... Poison-breath elixir... Wiggleberry..."
    scene ch4sc13_102 with dissolve
    al_t "Arrgh! None of these will do..."
    scene ch4sc13_103 with dissolve
    al_t "..."
    scene ch4sc13_104 with dissolve
    al_t "Maybe ... Fairydust and Starflower?"
    scene ch4sc13_105 with dissolve
    with vpunch
    lu "Morning Alice!"
    al "Wuuaahh?! Luna!? How many times... ?"
    lu "Only 62 times this week."
    scene ch4sc13_106 with dissolve
    al "*Sigh* One of these days you’re going to make my heart give out."
    scene ch4sc13_107 with dissolve
    lu "..."
    scene ch4sc13_108 with dissolve
    lu "Studying this early?"
    scene ch4sc13_107 with dissolve
    al "Yeah... I think I’m getting the hang of some of these ingredients."
    al "How does it feel not having to study for this class?"
    scene ch4sc13_109 with dissolve
    lu "*Giggles* Amazity! Although, I already studied the material... when I was nine."
    scene ch4sc13_108 with dissolve
    lu "Mother always emphasized learning."
    lu "Make room!"
    scene ch4sc13_110 with dissolve
    al "What brings you to the Academy this early? More off-the-books lessons with the Professor?"
    scene ch4sc13_111 with dissolve
    lu "*Stretches* Hhhnnggh!"
    scene ch4sc13_113 with dissolve
    lu "Correct! I’ve got a special artifact that's been cursed. I need her help to break the curse."
    scene ch4sc15_003 with dissolve
    lu "Take a look! It’s quite beautiful!"
    "Proudly, Luna pulls out an onyx blade and presents it to Alice."
    lu "What do you think? Pretty neat, huh? You can even see reflections in it."
    scene ch4sc15_004 with dissolve
    al "You’re right, it’s beautiful. I’ve never seen a blade like that before. Not that I’ve seen many, to be honest."
    lu "I wonder what material it’s made of? To be this shiny and black all over..."
    al "If you don’t mind me asking, why do you have a cursed blade? And why do you need to lift the curse?"
    scene ch4sc13_123 with dissolve
    "Luna puts the blade away and looks at Alice."
    lu "It’s... complicated."
    al "Does it have anything to do with the ‘bad man’ you told me about?"
    scene ch4sc13_124 with dissolve
    lu "That obvious, huh?"
    lu "He gave me this blade and told me to break the curse. Otherwise... he'll hurt my mom."
    lu "I’m at a loss, to be honest. I’ve never dealt with curses before and this one... seems extra potent."
    scene ch4sc13_123 with dissolve
    lu "*Sigh* I'd better get going. The sooner I give him what he wants, the sooner I can get my mother back."
    scene ch4sc13_126 with dissolve
    lu "See you, Alice! And good luck with alchemy class today!"
    "Luna bolts off into the Academy."
    #play music explore_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc15_005 with Dissolve(2)
    play music summon_3 fadein 1.0
    #stop music fadeout 1.0
    $ renpy.pause()
    scene ch4sc15_006 with Dissolve(2)
    $ renpy.pause(2)
    scene ch4sc15_007 with dissolve
    uk "Most disappointing."
    uk "We expected more progress by now. Our Lord Eternal expects more."
    scene ch4sc15_008 with dissolve
    ta "Are you questioning my loyalties?"
    scene ch4sc15_007 with dissolve
    uk "Nobody here doubts your allegiance. Just... your usefulness."
    ta "*Clenches teeth*"
    scene ch4sc15_008 with dissolve
    ta "My usefulness?! I’ve been doing his bidding for the last ten years!"
    ta "Never once have I faltered. Never."
    scene ch4sc15_007 with dissolve
    uk "That may be so. But he grows tired of waiting..."
    uk "You were chosen to be the vessel that will return our Lord Eternal."
    uk "Has his faith in you been misplaced?"
    scene ch4sc15_008 with dissolve
    ta "*Clenches teeth* No..."
    ta "I have set things in motion. Several paths have been forged, all leading to his return."
    scene ch4sc15_007 with dissolve
    uk "For your sake... I hope so. He isn’t one to give second chances."
    scene ch4sc15_008 with dissolve
    ta "His will, my hands."
    scene ch4sc15_007 with dissolve
    uk "His will, our hands. Leave. And Taron... don’t return without progress again."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc13_162 with Dissolve(2)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    kl "Still no sign of Pearl?"
    scene ch4sc13_163 with dissolve
    fy "Afraid not. It’s like she just vanished when we got here..."
    fy "If you ask me, though, I think she went after Kira and [mc]."
    scene ch4sc13_162 with dissolve
    kl "Yeah... I don’t like it. The storm is still raging over the island."
    kl "What if something happened to them?"
    scene ch4sc13_163 with dissolve
    fy "I don’t know. But they are pretty capable. It'll take more than a storm to stop them."
    scene ch4sc13_162 with dissolve
    kl "*Sigh* I hope you’re right. I guess we'd better make sure the ship is in order for their return."
    #play music summon_3 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)

    $ renpy.pause(2)
    if kira_sex == True:
        scene ch4sc14_282 with Dissolve(2)
        $ renpy.pause(1)
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
        scene ch4sc14_281 with dissolve
        $ renpy.pause(1)
        scene ch4sc14_280 with dissolve
        ki "Hnnghh..."
        scene ch4sc14_008 with dissolve
        kit "He held on to me all night?"
        kit "I’ve never felt safer than right here... in his strong arms."
        scene ch4sc14_276 with dissolve
        "She shuffles a bit and accidently brushes against your thigh."
        kit "*Soft moan* Nnngh... Shoot! I accidently rubbed against him..."
        kit "His thigh is already wet? Have I? No way... I’ve rubbed against him during the night?"
        kit "I better wake him up..."
        scene ch4sc14_016 with dissolve
        ki "*Soft whisper* Good morning, handsome."
        ki "*Soft whisper* Your Captain requires your immediate attention..."
        scene ch4sc14_015 with dissolve
        ki "*Lick*"
        scene ch4sc14_014 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc14_015 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc14_014 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc14_279 with dissolve
        mc "*Chuckles* Urhh... Kira?"
        ki "Finally! I was starting to think I'd have to lick your entire face."
        scene ch4sc14_277 with dissolve
        mc "Is this the type of awakening I can expect from now on?"
        scene ch4sc14_278 with dissolve
        ki "Yes. It’s all part of the package. The one you signed for with your... cock."
        scene ch4sc14_277 with dissolve
        mc "I'd better make sure I signed properly then."
        ki "What are you- ?"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch4sc14_217 with dissolve
        "You roll her onto her back, leaning down to her delicious nipple."
        play music lewd_1 fadein 1.0
        #stop music fadeout 1.0
        #####ANIMATION#####
        show ki_nip1 with fade
        $ renpy.pause(1, hard=True)
        ki "*Moans* Ohhh... [mc]... Nnhhh!"
        ki "K-Keep sucking... Hnnghh! Yes..."
        ki "I love when you tease my nipples with your tongue..."
        "Her nipple tastes a little salty with sweat from your exertions in the night."
        "You feel her rubbing her already wet pussy against your thigh as you suck harder."
        ki "*Moans* Yess! Ahh! Please lick me! I want you to taste me again..."
        scene ch4sc14_230 with dissolve
        mct "It seems she wants to serve herself as breakfast. Don’t mind if I do."
        "You kiss along her smooth thigh til you reach her clitoris. As you kiss it, you can feel her thighs quiver."
        $ renpy.pause()
        scene ch4sc14_231 with dissolve
        ki "Please... Mnnhh... Taste me."
        scene black with Dissolve(2)
        #####ANIMATION#####
        show ki_lick1 with fade
        $ renpy.pause(1, hard=True)
        "You lick her glistening lips, her thighs squishing your face softly as her pleasure increases."
        ki "Oooohh... {b}Yes! [mc]!{/b} I love feeling you make out with me there..."
        mct "She’s so tasty... A little hint of saltiness just like her nipple, mixed with her own sweet warm juices."
        ki "*Begging* [mc]... {b}Ahhh!{/b} Please... Lick me inside. Nnhh! I want you inside..."
        "You push your tongue between her lips and reach her entrance. As you penetrate her, echoes of pleasure fill the cave."
        ki "{b}OHH! YES!{/b} Mnnh! This... AH! This is the best way to... Mnnhh! Wake up..."
        "You feel her quiver with each lick and realize she’s about to cum, but you stop before it happens."
        $ renpy.pause()
        scene ch4sc14_234 with dissolve
        ki "*Panting* Haah... Hhh... Why’d you stop?"
        scene ch4sc14_235 with dissolve
        "You rest your throbbing cock on top of her little pussy."
        ki "Ohh! Mmm... I see you have something for me."
        scene ch4sc14_236 with dissolve
        "She touches your cock and grabs a hold of it, stroking you slowly."
        ki "*Soft whisper* I could get used to waking up like this..."
        scene ch4sc14_237 with dissolve
        "She presses your tip against her clitoris, rubbing the two of you together gently."
        ki "Aaahhh..."
        scene ch4sc14_238 with dissolve
        ki "[mc]... I want you."
        ki "Do you want me?"
        mc "I do. There’s nothing I crave more than to be inside you again."
        scene ch4sc14_239 with dissolve
        "She shifts slightly and pushes you inside."
        scene ch4sc14_240 with dissolve
        with vpunch
        ki "{b}Aahhhh! Nnnhhh!{/b}"
        scene ch4sc14_244 with dissolve
        "You pull out until only the tip is inside."
        mc "Damn Kira... You’re just as tight as yesterday."
        ki "*Giggles* I hope you like it... I doubt that will change."
        #####ANIMATION#####
        show ki_fuck4 with fade
        $ renpy.pause(1, hard=True)
        "You answer her by pushing inside her. She’s already soaking wet and ready for you."
        ki "Ahh! Mmnhh! Yes! Ahhh... It feels much better today."
        "Encouraged by her moans you thrust deep inside her."
        "The sounds of her cries fill the cave, punctuated by the noise of your skin smacking repeatedly against her ass and lower thighs."
        "She holds on to you, bracing herself, and her nails dig into your back out of ecstacy."
        with vpunch
        ki "*Moans* Ahhh! {b}[mc]!!{/b} Ffuck... Mnnhh! You’re really {b}deeeeep!{/b}"
        with vpunch
        ki "I’m ... I’m!!{b} AHH! YESS!! FUCK ME! AHHH!{/b}"
        $ renpy.pause()
        scene ch4sc14_242 with dissolve
        "Her pussy tightens and her body shakes as she cums all over your cock."
        #####ANIMATION#####
        show ki_fuck2 with fade
        $ renpy.pause(1, hard=True)
        "While her orgasm is still ongoing, you keep fucking her, sending waves of pleasure through her body."
        ki "*Loud moan* {b}AHH! Ahh! [mc]!! YES!!{/b}"
        ki "*Loud moan* I-I!! Ahh! I’m yours! {b}ONLY YOURS!!{/b} Fuck me!!"
        "Her nails sink deeper into your back as the pleasure of being fucked through an orgasm overwhelms her."
        with vpunch
        ki "*Moans* Ahh! Yes!! I’m gonna!! OOhh!! {b}Cum with me!{/b}"
        ki "*Moans* {b}Cum inside me!!{/b} I want you to fill me up again!"
        with vpunch
        ki "{b}*Loud moan* AHH!! [mc]!!! YES!! CUM WITH ME!!{/b}"
        $ renpy.pause()
        scene ch4sc14_242 with dissolve
        with vpunch
        $ renpy.pause(1)
        scene ch4sc14_245 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch4sc14_210 with dissolve
        "With her pussy filled with your cock and cum, she leans up to you and embraces you lovingly."
        $ kira_trust += 5
        "Kira's feelings for you has grown, her trust has increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
        ki "*Soft moan* Nnnhh... *Kiss* Mmmm... *Kiss*"
        #play music summon_3 fadein 1.0
        stop music fadeout 1.0
        scene ch4sc14_201 with dissolve
        "As you get up she hugs you tightly."
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
        ki "That was incredible..."
        scene ch4sc14_202 with dissolve
        mc "It really was. You’re incredible, Kira."
        ki "So are you! I-I lov..."
        "She stops herself mid-sentence."
        scene ch4sc14_200 with dissolve
        ki "..."
        scene ch4sc14_199 with dissolve
        ki "I’ve gotta go wash up... Again."
        ki "I’ll meet you back here and we can explore the other tunnel?"
        scene ch4sc14_200 with dissolve
        mc "Sure, sounds good."
        scene ch4sc14_201 with dissolve
        "She hugs you again before leaving."
        scene black with Dissolve(1.5)

    else:
        scene black with Dissolve(1.5)
        play music forest_1 fadein 1.0
        #stop music fadeout 1.0
    scene black with dissolve

    "You wait for Kira at the fork in the tunnels."
    scene ch4sc15_009 with Dissolve(1.5)
    ki "Alright, I'm good to go! Ready to find some treasure?"
    mc "Sure, let’s see what we can find."
    scene ch4sc15_010 with dissolve
    ki "That's what I like to hear! Come on then!"
    scene ch4sc15_011 with dissolve
    ki "This tunnel has a totally different vibe to it. Full of lush vegetation, but no shiny crystals."
    ki "I didn't think plants could grow in caves. Only certain mushrooms and such?"
    mc "I don't think they grow naturally here. They might be magically seeded to grow here."
    mc "There's a strange type of magic coming from this tunnel. I'm not sure what it is."
    scene ch4sc15_012 with dissolve
    ki "Magic, huh? That’s your department Mr. Half-Angel."
    mc "Yeah... I’m curious about it. It feels potent, but so far there's only faint traces of it."
    scene ch4sc15_011 with dissolve
    "The two of you walk through the tunnel, following its twists and turns. The strange magic grows stronger the further you go."
    #play music forest_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    "You walk and chat for what seems to be an hour."
    play music intro_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc15_014 with dissolve
    "Finally, you reach a lair filled with red crystals, then you spot it. The source of the magic you’ve been feeling."
    scene ch4sc15_015 with dissolve
    $ renpy.pause()
    "A deep-red chalice with engraved symbols and a palpable sense of magic flowing out of it."
    "The closer you get, the more strongly the magic seems to ooze from it."
    mct "Could this be it? Dalen and Sylph mentioned the artifact would resemble a chalice or goblet of sorts."
    mct "It has to be! I've never felt any magic like this before."
    scene ch4sc15_016 with dissolve
    "You reach for the chalice and it’s like the magic reaches for you in return."
    ki "*Yells* [mc]! Wait! We don’t know -"
    scene ch4sc15_017 with dissolve
    with vpunch
    "As you touch the chalice, the magic coils around you, and sudden pain stabs every nerve in your body."
    scene ch4sc15_017b with dissolve
    ki "*Shouting* {b}[mc]!! No!!{/b}"
    ki "*Shouting* {b}Let go of it!{/b}"
    scene ch4sc15_018 with dissolve
    with vpunch
    mc "{size=+10}{b}ARRGH!!{/b}{/size}"
    "Once the blue mist has fully enveloped you, it turns red, and the pain is gone ..."
    scene ch4sc15_019 with dissolve
    "And so are you."
    scene ch4sc15_017b with dissolve
    ki "*Shouting* {size=+10}{b}[mc]!!{/b}{/size}"
    scene black with Dissolve(2)
    scene ch4sc15_019b with dissolve
    $ renpy.pause()
    scene ch4sc15_020 with dissolve
    uk "Tsk! I can’t believe him! He’s napping on this occasion?"
    scene black with Dissolve(2)
    scene ch4sc15_020 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_021 with dissolve
    uk "Doesn’t he know who I am?! Hrrrhpf!"
    uk "If he doesn’t wake up soon, I’ll... I’ll feed him to Jaz’ar!"
    scene black with Dissolve(2)
    scene ch4sc15_022 with Dissolve(2)
    uk "No... I can’t do that. He’s my neph-"
    mc "*Groan* Urrh... Where... am I?"
    scene ch4sc15_023 with dissolve
    uk "Finally! I’ve already been waiting minutes for you to wake up!"
    scene ch4sc15_024 with dissolve
    mc "Huh? ... Who are you?"
    uk "Hmhff!"
    scene ch4sc15_025 with dissolve
    uk "You don’t know who I am?"
    uk "You mortals really should pay more attention..."
    ###Choice####
    menu:
        "Compliment her.":
            scene ch4sc15_026 with dissolve
            mc "I might not know who you are, but I have a feeling I won’t forget meeting you."
            uk "..."
            scene ch4sc15_027 with dissolve
            uk "Huh... Interesting."
            uk "He flirts..."
            $ lucid_trust += 1
            "Lucid appreciates the compliment, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch4sc15_026 with dissolve
            mc "So... will you tell me who you are?"
            scene ch4sc15_027 with dissolve
            uk "Mmmh... Okay! But first... get up."
            uk "Can’t have my- uh... guest laying on the sacrificial altar."
            scene ch4sc15_026 with dissolve
            mc "Sacrificial... altar?"
            scene black with Dissolve(1.5)

        "Get to the point.":
            scene ch4sc15_024 with dissolve
            mc "Look I don’t know you, and you don’t know me. Why am I here?"
            scene ch4sc15_025 with dissolve
            uk "Ugh! Such a little busy-body... Fine! Fine... Tsk!"
            scene black with Dissolve(1.5)

    scene ch4sc15_028 with Dissolve(1.5)
    uk "I almost fed you to Jaz’ar, you know?"
    uk "Anyway... let’s sit!"
    "You sit down beside her on the stairs."
    scene ch4sc15_029 with dissolve
    uk "We don’t have much time before you return to Midomir ..."
    ld "I’m Lucid."
    ld "My followers often refer to me as ‘{b}Mother of the damned{/b}’."
    scene ch4sc15_030 with dissolve
    mc "Wait... Lucid? You’re one of the seven... A {b}Divine?{/b}"
    scene ch4sc15_031 with dissolve
    ld "Correct. As to where you are... you’re in my realm. The Inferno Isles."
    ld "When you touched my chalice, it transported you here."
    ld "A little enchantment I cast so that I could meet whoever wants to use it."
    scene ch4sc15_032 with dissolve
    mc "That confirms it. It is the artifact I’m looking for."
    scene ch4sc15_033 with dissolve
    ld "This is not how I’d thought we’d meet... I'd hoped we would have more time..."
    scene ch4sc15_032 with dissolve
    mc "You thought we would meet? Why?"
    scene ch4sc15_033 with dissolve
    ld "No questions, not now. Just listen. The enchantment will run out soon and you'll be transported back."
    ld "If you really intend to use the chalice. Then you must know its effects."
    ld "Firstly, my chalice can only be used once."
    scene ch4sc15_031 with dissolve
    ld "Once a mortal drinks from it, it will vanish, then reappear in some random hard-to-reach location elsewhere in Midomir."
    scene ch4sc15_033 with dissolve
    ld "‘Chalice of Vitality’ is what I call it. Before you attempt to use it... you have to understand."
    ld "It will change the person who drinks from it. Both physically and emotionally."
    scene ch4sc15_031 with dissolve
    ld "They will be granted eternal youth. Any injuries they've sustained, will regenerate. As will all future injuries."
    scene ch4sc15_033 with dissolve
    ld "Everything about them will be heightened. Their speed, their strength, their senses, hearing, vision, taste, touch, smell."
    scene ch4sc15_031 with dissolve
    ld "Their emotions will be magnified. Happiness becomes bliss, sadness becomes despair, anger turns to rage."
    ld "It can mentally cripple a person if they aren’t capable of adjusting to their new life."
    scene ch4sc15_033 with dissolve
    ld "Then there's the hunger. A thirst that can only be satiated but never quenched..."
    scene ch4sc15_032 with dissolve
    mc "Thirst for what?"
    scene ch4sc15_033 with dissolve
    ld "Blood. Only the blood of mortals will provide sustenance after they turn."
    scene ch4sc15_032 with dissolve
    mc "Sounds like you’re describing a vampire?"
    scene ch4sc15_031 with dissolve
    ld "Not just any vampire... A pure-blooded vampire. Made by my own blood."
    scene ch4sc15_032 with dissolve
    mc "A pureblood... what's that?"
    scene ch4sc15_033 with dissolve
    ld "Any vampire created directly by the source: me. Any vampire can turn mortals by feeding them their blood."
    scene ch4sc15_031 with dissolve
    ld "But vampires created that way are lesser, merely regular vampires."
    ld "Only those vampires made from my blood directly are pureblooded."
    scene ch4sc15_032 with dissolve
    mc "Hmh, I see. A pureblood must be stronger than regular vampires?"
    scene ch4sc15_031 with dissolve
    ld "There are three things that determine a vampire's strength."
    ld "Firstly, they grow stronger with time. A century-old vampire is no match for one that has lived for a millenia."
    scene ch4sc15_033 with dissolve
    ld "Secondly, through feeding. The more a vampire feeds, the stronger they get. For example-"
    ld "-A century-old old vampire who has fed a lot, may be stronger than a poorly fed vampire who has lived a few decades more."
    scene ch4sc15_031 with dissolve
    ld "And finally, the strength of their bloodline."
    ld "Each time a vampire turns a mortal, then the strength of their bloodline is diluted and loses potency."
    ld "The closer a vampire is to my bloodline, the stronger they are. For example-"
    scene ch4sc15_033 with dissolve
    ld "A relatively young pure-blooded vampire could easily be as strong as-"
    ld "-a regular vampire aged two or three centuries older than them."
    ld "And of course, a pureblood's abilities and strength will grow much faster than others."
    scene ch4sc15_031 with dissolve
    ld "So that is why I enchanted the chalice to relocate itself after being used: as a safeguard."
    scene ch4sc15_033 with dissolve
    ld "An artifact like that, in the wrong hands... At least this way it can only create one pureblood at a time."
    scene ch4sc15_032 with dissolve
    mc "It can heal any wounds or injury, you say?"
    scene ch4sc15_033 with dissolve
    ld "Any."
    ld "No matter the severity of the injury. Even if the person has been carved in half, it'll regenerate them to their prime."
    ld "Of course, the bigger the injury the longer it will take to heal. But feeding can speed up the process."
    ld "Do keep in mind, vampires are 'immortal', but they're not 'invincible'."
    scene ch4sc15_031 with dissolve
    ld "Stabbing a vampire in the heart won't do anything. They will heal, although slowly."
    ld "But removing their heart completely will kill them. And same goes for their head."
    ld "Decapitating them will result in their demise. Lastly, if they are fully scorched with fire, they will die as well."
    scene ch4sc15_032 with dissolve
    mc "What about sunlight? Garlic? Wooden stakes?"
    scene ch4sc15_031 with dissolve
    ld "None of that will have any major impact, wooden stakes would hurt but that's about it."
    ld "As for the sun, pureblood vampires feel no effect from the sun."
    ld "However, regular vampires are weakened when they are in sunlight, but it won't kill them."
    scene ch4sc15_032 with dissolve
    mc "I see..."
    mc "That's a lot to keep track of..."
    scene ch4sc15_033 with dissolve
    ld "Mh-hm! If it’s used on an old person, they'll turn young again. Eternally."
    ld "A vampire won't fall sick to illness either."
    scene ch4sc15_032 with dissolve
    mc "What about people who've died? Let’s say, a decade ago?"
    scene ch4sc15_031 with dissolve
    ld "No... afraid not. It won’t be able to bring back your parents, [mc]."
    mct "She knows my name... and there’s something familiar about her."
    mct "I feel completely at ease around her... As if I’m safe."
    mct "The only times I've felt like this is with Eliza and-"
    scene ch1sc2_2 with Dissolve(1.5)
    mct "Mom?"
    scene ch1sc2_4 with dissolve
    $ renpy.pause(1.5)
    scene ch1sc2_5 with dissolve
    mct "Mother! Don't go..."
    scene black with Dissolve(2)
    scene ch1sc2_28 with Dissolve(2)
    $ renpy.pause()
    scene black with Dissolve(2)
    scene ch4sc15_033 with dissolve
    ld "Are you listening?"
    scene ch4sc15_032 with dissolve
    mc "Huh? Oh... I was just thinking-"
    scene ch4sc15_033 with dissolve
    ld "Thinking about our connection? I’m afraid I can’t tell you today... We’re out of time."
    ld "We’ll see each other again. And when we do, I'll tell you everything."
    ld "Everything about who you are."
    scene ch4sc15_032 with dissolve
    mc "Lucid? Please... I-I need to know."
    scene ch4sc15_031 with dissolve
    ld "[mc], sorry. I promise we'll see each other again."
    "Her tone is heavy with emotion."
    scene ch4sc15_035 with dissolve
    "She leans toward you and gently ruffles your hair while planting her rosy lips on your forehead."
    "As her kiss lingers, you feel warm inside... your eyes start to close..."
    scene ch4sc15_036 with dissolve
    "One feeling inside of you stands out above the rest... family."
    scene black with Dissolve(2)
    scene ch4sc15_037 with Dissolve(2)
    ldt "Till we meet again... Neph-"
    uk "Rrhhghh..."
    scene ch4sc15_038 with dissolve
    ld "*Giggles* Can you believe Castiel's son could be that cute, Jaz’ar?"
    ld "Aahh! I just wanted to hug him! Hold him! Squeeze him! {b}Bite him!{/b}"
    scene ch4sc15_037 with dissolve
    ldt "Heeh-heeh! Definitely bite him!"
    uk "*Angry* Rrggahhh!"
    scene ch4sc15_039 with dissolve
    with vpunch
    ld "{b}Don’t make me fireball you!!{/b}"
    uk "*Whimpers* {b}Rrhghrh! Rhhuuhh!{/b}"
    scene ch4sc15_038 with dissolve
    ld "I wonder what he'd taste like? His scent was so... mmhm! Delicious!"
    ld "I just wanted to tell him everything! And keep him here! And- play with him! *Infatuated giggle*"
    scene ch4sc15_037 with dissolve
    ld "*Sighs* He's really grown up... has it really been twenty years already?"
    #play music intro_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc15_040 with Dissolve(1.5)
    play music home_2 fadein 1.0
    #stop music fadeout 1.0
    ki "[mc]... What the hell happened to him? Where is he?"
    scene ch4sc15_041 with dissolve
    with vpunch
    "Crackling noise from above."
    ki "Wha-"
    scene ch4sc15_042 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_043 with dissolve
    "You re-appear in a cloud of faint blue mist."
    scene ch4sc15_044 with dissolve
    with vpunch
    ki "*Groans* Urrrh..."
    scene black with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_045 with dissolve
    $ renpy.pause(1.5)
    scene black with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_045 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_046 with dissolve
    $ renpy.pause(1.5)
    if kira_sex == True:
        scene ch4sc15_046 with dissolve
        mct "Mnhh... This has a familiar smell."
        mct "Kira."
        mct "Either Lucid killed me and I’m in the high heavens, or..."
        mct "She sent me back and I somehow ended up between Kira’s legs."
        scene ch4sc15_049 with dissolve
        ki "*Groans* Ahhhh... Wake up... Your fat ass weighs more than a barrel of cannon powder!"
        ki "W-What are you doing back there?!"
        scene ch4sc15_046 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc15_047 with dissolve
        mct "I think a little taste is in order... I did just travel across dimensions, after all."
        ki "What are you doing... T-That’s not getting up..."
        scene ch4sc15_048 with dissolve
        "As you inch your way between her warm thighs, the scent of her flower grows increasingly alluring."
        "You finally reach your destination, and you don’t hesitate you plant your lips on hers."
        with vpunch
        ki "*Moans* AHH! S-Stop that!!"
        scene ch4sc15_049 with dissolve
        ki "*Moans* This isn’t... Ahh... the time for your... AH! sinful actions..."
        scene ch4sc15_050 with dissolve
        ki "*Bites lip* Mnnhh... Nnghh..."
        kit "Fuck... I... Mnnhh! I don’t even want him to stop anymore..."
        scene ch4sc15_048 with dissolve
        "After planting a few more kisses, you decide it's best not to push your luck."
        scene black with dissolve

    else:
        scene ch4sc15_044 with dissolve
        ki "*Groans* Arrgh... Get up already!"
        scene black with dissolve

    scene ch4sc15_051 with dissolve
    ki "J-Jerk!"
    ki "I... I didn’t know where you were! You just vanished!"
    scene ch4sc15_052 with dissolve
    ki "You’re a real selfish squid-brain, you know that?"
    scene ch4sc15_053 with dissolve
    mc "Kira... Don’t be like that. I didn’t vanish on purpose, you know?"
    ki "HHnnrrh..."
    scene ch4sc15_054 with dissolve
    ki "I... *Sigh* I know. It’s just that... I didn’t know what to think. You looked like you were in pain-"
    ki "And then, poof! You vanished..."
    scene ch4sc15_053 with dissolve
    mc "Yeah... How about we head back? I’m starving. So I know you are too."
    scene ch4sc15_054 with dissolve
    ki "Y-Yeah... some food would be nice. Grab the artifact and let’s go."
    scene ch4sc15_055 with dissolve
    $ renpy.pause(1.5)
    mc "It’s... it’s gone?"
    scene ch4sc15_054 with dissolve
    #play music home_2 fadein 1.0
    stop music fadeout 1.0
    ki "What do you mean, it’s gone? It was right there."
    scene ch4sc15_053 with dissolve
    play music darknight_1 fadein 1.0
    #stop music fadeout 1.0
    pl "Deepest apologies... But I’ll be taking this."
    scene ch4sc15_056 with dissolve
    $ renpy.pause(1.5)
    ki "Pearl! What are you-"
    pl "Sorry Sis, but it’s for your own good."
    pl "Father’s orders and all."
    scene ch4sc15_057 with dissolve
    ki "Pearl. I swear... Give that back to [mc]! Do you have any idea what we’ve been through to get it?"
    scene ch4sc15_056 with dissolve
    pl "No can do, Sis. You know how Father gets when he doesn’t get what he wants..."
    pl "I’m doing this for you. You’ll see."
    scene ch4sc15_058 with dissolve
    mc "Pearl."
    scene ch4sc15_059 with dissolve
    pl "Hi..."
    scene ch4sc15_058 with dissolve
    mc "We’re friends."
    mc "Don’t... Don’t force my hand. You know what this means to me."
    scene ch4sc15_059 with dissolve
    pl "We are friends... I’m not doing this to spite you. But I have to... there’s no other way."
    pl "I’m... sorry."
    scene ch4sc15_060 with dissolve
    pl "Please ... forgive me."
    "She reveals a glowing orb in her palm, you’ve seen this before... A transporter orb."
    "It will allow its user to instantly transport themselves a short distance, one time use."
    scene ch4sc15_060a with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_060b with dissolve
    $ renpy.pause(1.5)
    scene ch4sc15_061 with dissolve
    mc "{b}*Shouting* PEARL! NO!{/b}"
    scene ch4sc15_061b with dissolve
    $ renpy.pause()
    scene ch4sc15_060b with dissolve
    pl "Please don't hate me."
    scene ch4sc15_062 with dissolve
    with vpunch
    $ renpy.pause()
    "You sprint into the teal light of the orb, but you just barely miss grabbing hold of Pearl."
    scene ch4sc15_017b with dissolve
    ki "{b}[mc]!!{/b}"
    scene ch4sc15_063 with dissolve
    mct "{b}FUCK!!{/b} Fucking! Fuck!"
    scene ch4sc15_064 with dissolve
    #play music darknight_1 fadein 1.0
    stop music fadeout 1.0
    "Before you have a chance to let your thoughts and anger run wild, you feel her ... Kira."
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    ki "[mc]... Are you okay?"
    ###CHOICE###
    menu:
        "Be calm with her.":
            scene ch4sc15_065 with dissolve
            mc "No, I’m not... Why would Pearl do this?"
            scene ch4sc15_064 with dissolve
            ki "I-I don’t know... She didn’t tell me anything. Which is totally out of character for her."
            scene ch4sc15_065 with dissolve
            mc "I need to find her."
            scene ch4sc15_064 with dissolve
            ki "Please... Please promise me that you won’t hurt her."
            ki "You know she clearly didn’t want this! She mentioned Father... he must be behind this!"
            scene ch4sc15_065 with dissolve
            mc "Kira, you can relax. I won’t hurt her... She’s my friend."
            mc "Even after what she just pulled... it obviously has everything to do with your father."
            mc "We knew he would try to pull something... now we found out."
            mc "Come on, let’s get going. We have a lost blonde to find."
            "Kira appreciates that you're smart enough to see reason, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            $ kira_trust += 3
            scene black with Dissolve(2)

        "Be angry with her.":
            scene ch4sc15_065 with dissolve
            mc "Obviously I’m not okay!"
            mc "What the fuck was that? Did you know she would try something like that?"
            scene ch4sc15_064 with dissolve
            ki "Wha- No!"
            ki "I'm just as much in the dark as you are..."
            scene ch4sc15_065 with dissolve
            mc "Whatever."
            mc "Let’s get out of here... I need to find your sister."
            "Kira didn't like that you took out your frustration on her, her trust has decreased by {size=+3}{b}{color=#f00}3{/color}{/b}{/size}."
            $ kira_trust -= 3
            scene black with Dissolve(2)

    scene ch4sc15_066 with Dissolve(2)
    #play music darknight_1 fadein 1.0
    stop music fadeout 1.0
    $ renpy.pause()
    play music dark_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc15_067 with dissolve
    $ renpy.pause()
    scene ch4sc15_068 with dissolve
    $ renpy.pause()
    scene ch4sc15_069 with dissolve
    ta "Report."
    scene ch4sc15_070 with dissolve
    lu "I want to see her..."
    scene ch4sc15_069 with dissolve
    ta "Report."
    scene ch4sc15_070 with dissolve
    lu "*Sigh* No progress..."
    lu "It’s not a simple task you’ve given me. This curse is ancient, and it isn’t responding to my magic..."
    scene ch4sc15_069 with dissolve
    ta "You know the rules."
    scene ch4sc15_068 with dissolve
    lu "But I-"
    scene ch4sc15_069 with dissolve
    with vpunch
    ta "Shut up!"
    ta "You don’t make demands of me, girl. You do as I command, or you won’t get to see her again."
    scene ch4sc15_071 with dissolve
    ta "And my patience is running thin. You'd best remember that the next time you show up empty-handed."
    ta "Am I making myself clear?"
    ta "Or perhaps you need a demonstration of what will happen to your mother if you don’t break this curse?"
    scene ch4sc15_072 with dissolve
    lu "No! Don't hurt her!"
    lu "I-I... I’ll do better!"
    scene ch4sc15_071 with dissolve
    ta "Leave... And don’t return until you have something of value to show."
    lut "Mom... I have to do as he asks. I know you wouldn’t want me to..."
    lut "But I can’t let him hurt you!"
    lut "I have to break this curse... it's the only way to free you."
    #play music darknight_1 fadein 1.0
    stop music fadeout 1.0
    scene black with Dissolve(2)
    scene ch4sc15_005 with dissolve
    $ renpy.pause()
    play music forest_1 fadein 1.0
    #stop music fadeout 1.0
    scene ch4sc11_046 with dissolve
    el "Come on Borri!"
    el "Tell me! What was your quest yesterday?"
    scene ch4sc11_047 with dissolve
    br "Oh, ah..."
    br "Best we get te the guild and see if anything is available t'day, lass."
    scene ch4sc11_046 with dissolve
    el "Oh? It’s something embarrassing, isn’t it?!"
    el "Borri, you have to tell me! I promise I won’t laugh."
    jump ch4sc16

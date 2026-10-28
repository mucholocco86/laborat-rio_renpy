label scene42:
    $ in_scene42 = True
    $ in_scene35_2 = False
    $ free_roam_arrows = True
    scene 42_s1 with Fade(1.0,1.0,1.0)
    $ current_objective = "After getting attacked by a werewolf, we stumbled \ninto some village. The people here seem kind, they \neven took care of Alex. But I don't know... something \nfeels off about them. \nMaybe it's just me being paranoid. I'll look around \nand see for myself."
    $ second_objective = ""
    $ third_objective = ""
    perception "The village is brighter than yesterday. The sun is warm, the air smells faintly of soil and woodsmoke."
    $ in_free_roam = True

    if not mc_maia_left:
        $ mc_marital = "single"
    else:
        $ mc_marital = "divorced"

    $ mc_residency = "castle"
    $ mc_job = "royal_servant"

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene42_free_roam with dissolve

default scene42_afterwell_first = True
label scene42_afterwell:
    if scene42_afterwell_first:
        $ scene42_afterwell_first = False
        if not mc_met_well_villager:
            scene 42_s1 with Fade(1.0,1.0,1.0)
        else:
            scene 42_s2 with Fade(1.0,1.0,1.0)
    else:
        if not mc_met_well_villager:
            scene 42_s1 with dissolve
        else:
            scene 42_s2 with dissolve
    call screen scene42_free_roam with dissolve

default mc_met_well_villager = False
default mc_met_heiter = False
default mc_met_sigrun = False
default mc_met_werewolf_villager = False

label scene42_forward:
    if not mc_met_well_villager:
        $ mc_met_well_villager = True
        scene 42_s4 with dissolve
        mc "Hey. Having some trouble?"
        scene 42_s5 with Dissolve(0.8)
        villager "Oh, hello! As a matter of fact, I am... This stubborn thing won't budge."
        scene 42_s6 with dissolve
        mc "Want me to help?"
        scene 42_s5 with dissolve
        villager "If it's not too much trouble, young one."
        scene 42_s6 with dissolve
        scene 42_s7 with Dissolve(0.8)
        sensation "The bucket is heavier than expected. The water inside shimmers faintly."
        mc "What's in this, rocks?"
        villager "*laughs*"
        if persistent.skip_mini:
            $ result = "Perfect"
            jump scene42_well
        else:
            call screen qte_tutorial with dissolve
            jump scene42_well
    else:
        if scene42_poster1:
            scene 42_s11_2 with dissolve
        else:
            scene 42_s11 with dissolve
        call screen scene42_up with dissolve

label scene42_poster1:
    $ persistent.yuuhi_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene42_poster1 = False
    jump scene42_forward

label scene42_well:
        if persistent.skip_mini:
            "Mini-Game Skipped"
        else:
            $ result = renpy.call_screen("quick_event")
        if result == "Perfect":
            scene 42_s8 with dissolve
            villager "My, my... that was impressive."
        elif result == "Good":
            scene 42_s8 with dissolve
            villager "Nicely done. You've got some strength in you."
        elif result == "Bad":
            mc "Hngg!"
            villager "Almost. Try nudging it to the side."
            jump scene42_well
        else: 
            villager "Hmm... Not quite. Try pulling with more control next time."
            jump scene42_well
        scene 42_s10 with dissolve
        mc "Come on, it wasn't that heavy..."
        scene 42_s9 with dissolve
        villager "Still, I appreciate your help. Maybe I was wrong about you."
        scene 42_s10 with dissolve
        mc "Wrong about what?"
        scene 42_s9 with dissolve
        villager "Don't worry about it. It was a pleasure meeting you, traveler. May the Goddess keep you."
        scene 42_s10 with dissolve
        mc "Thanks..."
        jump scene42_afterwell

label scene42_heiter:
    $ mc_met_heiter = True
    scene 42_s40 with dissolve
    mc "Hello."
    scene 42_s12 with dissolve
    heiter_ "Traveler! The Goddess smiles on your arrival."
    scene 42_s13 with dissolve
    roza_ "He means 'hello'."
    scene 42_s12 with dissolve
    heiter_ "I'm Heiter, and these are Ada and Roza. They are my—"
    villager "Good morning, Heiter!"
    scene 42_s14 with dissolve
    heiter "Good morning!"
    scene 42_s12 with dissolve
    heiter "Anyway, like I was saying—these two are my—"
    villager "Heiter! Come help me with this!"
    scene 42_s14 with dissolve
    heiter "I will in a bit! Just give me a moment!"
    scene 42_s12 with dissolve
    heiter "...So... what was I talking about?"
    scene 42_s13 with dissolve
    roza "*sigh* Forget it."
    scene 42_s40 with dissolve
    mc "Good meeting you all."
    mc "The place seems livelier than yesterday. When we arrived, it was like a ghost town."
    scene 42_s12 with dissolve
    heiter "*chuckles* Sorry if we scared you. You must have arrived during the village meeting."
    scene 42_s40 with dissolve
    mc "A meeting? Must've been important if the entire village was there."
    scene 42_s15 with dissolve
    ada "Is that not what you came for? You missed it."
    scene 42_s40 with dissolve
    mc "What are you talking about?"
    scene 42_s12 with dissolve
    heiter "The Festival, of course. It usually draws men from all over—though no one showed up this time. Aside from you that is."
    scene 42_s40 with dissolve
    mc "Festival? Not really what I came here for, I just wanted to treat my friend and maybe trade."
    scene 42_s13 with dissolve
    roza "A shame... We could definitely use a fresh man this year. The ones we have are... lacking."
    scene 42_s12 with dissolve
    heiter "Hey! Come on. I'm standing right here."
    scene 42_s18 with dissolve
    ada "*laughs* She's right. You're sweet, Heiter, but you're not exactly a warrior. You almost passed out last time."
    scene 42_s16 with dissolve
    heiter "*groan*"
    mc "Can someone please tell me what's going on?"
    scene 42_s12 with dissolve
    heiter "The Goddess's Festival! It's a sacred tradition. Every ten years, the men of the village compete in a series of tests."
    heiter "The winner is chosen to bless the womb of all birth able women of the village."
    heiter "It's the highest calling a man can aspire to. The Goddess herself watches over the Trial and blesses the victor with her favor."
    scene 42_s40 with dissolve
    empathy "There's no hesitation in his voice. He's stating this as if it's the most natural thing in the world."
    scene 42_s15 with dissolve
    ada "Exciting, isn't it? It's our first time participating. We're both hoping to be blessed."
    scene 42_s40 with dissolve
    mc "I... don't know what to say. What happens to the losers?"
    scene 42_s12 with dissolve
    heiter "The winner takes all, friend."
    scene 42_s40 with dissolve
    mc "So nothing? The losers just... go home?"
    scene 42_s17 with dissolve
    ada "Who'd want to breed with a loser, anyway? The Goddess demands the best. Only the strongest seed is worthy."
    scene 42_s40 with dissolve
    mc "This all seems barbaric. Can't you just, you know... choose who to love?"
    scene 42_s12 with dissolve
    heiter "To outsiders, maybe. But we've followed this tradition for generations."
    heiter "The Goddess ordains this. Without strong blood, the blight would've consumed us decades ago. Our harvests thrive because {i}she{/i} thrives. The Trial ensures her favor."
    heiter "Unfortunately, not all have remained faithful. Some strayed... and the Goddess's wrath was merciless."
    heiter "That is why so few of us remain."
    scene 42_s13 with dissolve
    roza "Why not compete? You're clearly strong—I saw you lift that bucket. *giggles* {size=30}It was a test, by the way.{/size}"
    roza "I wouldn't mind being blessed by you, traveller."
    scene 42_s40 with dissolve
    mc "I still don't quite understand some things..."
    scene 42_s12 with dissolve
    heiter "Mother Ysella would be more than happy to explain further."
    scene 42_s40 with dissolve
    mc "Got it. Good seeing you all."
    scene 42_s11 with dissolve
    call screen scene42_up with dissolve

label scene42_up_down:
    scene 42_s2 with dissolve
    call screen scene42_free_roam with dissolve

label scene42_down:
    play music "2_opening_ride.mp3" fadein 1.0 volume 0.1 loop
    if scene42_coin:
        scene 42_s3_2 with dissolve
    else:
        scene 42_s3 with dissolve
    call screen scene42_down with dissolve

label scene42_free_roam_coin:
    $ mc_coin += 10
    $ renpy.notify("You found 1 silver coin!")
    play sound "sound_effects/coin_collect.mp3"
    $ scene42_coin = False
    mc "Is this yours Alex?"
    mc "I'm just gonna borrow it for a bit..."
    jump scene42_down

label scene42_left:
    scene 42_s19 with dissolve
    call screen scene42_left with dissolve

label scene42_left_up:
    scene 42_s20 with dissolve
    call screen scene42_left_up with dissolve

label scene42_left_up_up:
    scene 42_s25 with dissolve
    call screen scene42_left_up_up with dissolve

label scene42_left_up_up_left:
    if scene42_poster2:
        scene 42_s28_2 with dissolve
    else:
        scene 42_s28 with dissolve
    call screen scene42_left_up_up_left with dissolve

label scene42_poster2:
    $ persistent.queen_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene42_poster2 = False
    mc "What's this doing on you, pal?"
    jump scene42_left_up_up_left

label scene42_down_up:
    play music "2_opening_ride.mp3" fadein 1.0 loop
    if scene42_afterwell_first:
        $ scene42_afterwell_first = False
        if not mc_met_well_villager:
            scene 42_s1 with Fade(1.0,1.0,1.0)
        else:
            scene 42_s2 with Fade(1.0,1.0,1.0)
    else:
        if not mc_met_well_villager:
            scene 42_s1 with dissolve
        else:
            scene 42_s2 with dissolve
    call screen scene42_free_roam with dissolve

label scene42_sigrun:
    $ mc_met_sigrun = True
    scene 42_s22 with dissolve
    mc "Hey."
    scene 42_s21 with dissolve
    sigrun_ "Oh, traveler. A pleasure to meet you. How is your friend doing?"
    scene 42_s22 with dissolve
    mc "She's still sleeping, Ymir gave her something for the pain. I hope she gets better soon."
    scene 42_s21 with dissolve
    sigrun "I hope so too. Ymir's brews are effective—if a little strong. I'm Sigrun, and this is my husband, Aldwin."
    scene 42_s22 with dissolve
    aldwin "*sigh*"
    scene 42_s23 with dissolve
    sigrun "Won't you greet our guest, dear?"
    scene 42_s24 with dissolve
    aldwin "Welcome, traveler. Forgive me, I'm not... in the best health."
    mc "You alright?"
    aldwin "Just feeling my years catch up to me, that's all. I used to be strong once."
    scene 42_s23 with dissolve
    sigrun "And you still are, love."
    scene 42_s24 with dissolve
    aldwin "Not strong enough to fight this time... And now..."
    sigrun "..."
    aldwin "Twice I fought. Won. Proved myself. Kept you as mine. But now..."
    scene 42_s23 with dissolve
    sigrun "It's tradition, Aldwin. I don't like it any more than you do, but it's what keeps the village alive."
    scene 42_s24 with dissolve
    aldwin "Easy for you to say."
    mc "..."
    scene 42_s21 with dissolve
    sigrun "Forgive us, traveler. This has been hard for me... for both of us."
    sigrun "We love each other deeply, but love doesn't always matter when the Goddess calls."
    scene 42_s22 with dissolve
    mc "I can tell. Well, I'll leave you two in peace."
    scene 42_s21 with dissolve
    sigrun "Thank you. May the goddess watch over you."
    scene 42_s22 with dissolve
    jump scene42_left_up

label scene42_werewolf_villager:
    $ mc_met_werewolf_villager = True
    scene 42_s26 with dissolve
    mc "You... don't look like the others."
    scene 42_s27 with dissolve
    villager "Ah, you noticed? And here I thought I blended right in with all the pale, golden-haired folk."
    scene 42_s26 with dissolve
    mc "How'd you end up here?"
    scene 42_s27 with dissolve
    villager "Our caravan was attacked... a werewolf. I was lucky—ran as soon as I heard the first scream."
    villager "The others... I don't know. I try not to think about it."
    scene 42_s26 with dissolve
    mc "A werewolf... What happened after?"
    scene 42_s27 with dissolve
    villager "The villagers took me in. Kind folks, if a little strange—especially when they start talking about their {i}goddess.{/i}"
    villager "Still, their hearts are in the right place. I think."
    scene 42_s26 with dissolve
    mc "Thanks for sharing that."
    scene 42_s27 with dissolve
    villager "Not like I'm going anywhere."
    scene 42_s26 with dissolve
    jump scene42_left_up_up

label scene42_end_freeroam:
    call screen scene42_free_roam_end with dissolve
    scene 42_s2 with dissolve
    call screen scene42_free_roam with dissolve

label scene42_end_freeroam_forward:
    call screen scene42_free_roam_end with dissolve
    if scene42_poster1:
        scene 42_s11_2 with dissolve
    else:
        scene 42_s11 with dissolve
    call screen scene42_up with dissolve

label scene42_end_freeroam_down:
    call screen scene42_free_roam_end with dissolve
    if scene42_coin:
        scene 42_s3_2 with dissolve
    else:
        scene 42_s3 with dissolve
    call screen scene42_down with dissolve

label scene42_end_freeroam_left:
    call screen scene42_free_roam_end with dissolve
    scene 42_s19 with dissolve
    call screen scene42_left with dissolve

label scene42_end_freeroam_left_up:
    call screen scene42_free_roam_end with dissolve
    scene 42_s20 with dissolve
    call screen scene42_left_up with dissolve

label scene42_end_freeroam_left_up_up:
    call screen scene42_free_roam_end with dissolve
    scene 42_s25 with dissolve
    call screen scene42_left_up_up with dissolve

label scene42_end_freeroam_left_up_up_left:
    call screen scene42_free_roam_end with dissolve
    if scene42_poster2:
        scene 42_s28_2 with dissolve
    else:
        scene 42_s28 with dissolve
    call screen scene42_left_up_up_left with dissolve


label scene42_continue:
    $ in_free_roam = False
    mc "(I guess I'll ask Ysella about what's going on.)"
    stop music fadeout 3.0 
    scene 42_s29 with Fade(1.0,1.0,1.0)
    ""
    play music "fire.mp3" fadein 3.0 volume 0.3 loop
    scene 42_s30 with Dissolve(0.9)
    ""
    scene 42_s31 with dissolve
    ysella "Ah, [mc]. Come here, sit."
    scene 39_s20 with Fade(0.5,0.5,0.5)
    ysella "Good morning, [mc]. I hope you had a restful night. You'll likely need it for what's to come."
    scene 39_s17 with dissolve
    mc "So... Tell me. What's really going on here?"
    scene 39_s20 with dissolve
    ysella "I suppose we can't hide it any longer... We are preparing for our tradition that comes around every three years, where the men compete for the right to plant their seed in every willing womb."
    ysella "The winner earns the honor of blessing the families of the defeated. The ritual strengthens us. Unites us."
    scene 39_s17 with dissolve
    mc "And when does this festival begin?"
    scene 39_s20 with dissolve
    ysella "At moonrise. We can't afford to delay. I'm sure you've already heard bits of it from the villagers."
    scene 39_s26 with dissolve
    oswald "Our village was struck by a devastating blight last year. Most of our people fled the village and some even died."
    scene 39_s17 with dissolve
    mc "...Why keep this secret in the first place?"
    scene 39_s20 with dissolve
    ysella "We cannot trust just any traveler. Outsiders must first prove themselves—through their actions, their character."
    scene 39_s17 with dissolve
    mc "And I passed?"
    scene 39_s20 with dissolve
    ysella "Yes. Even the smallest acts reveal the soul."
    scene 39_s17 with dissolve
    mc "What happens if I refuse?"
    scene 39_s26 with dissolve
    oswald "Nothing will happen to you. You're free to walk away."
    oswald "But... we would very much like for you to join us."
    oswald "As you have seen, our numbers have dwindled. The last two festivals were won by the same man—Aldwin—and he's no longer strong enough to fight. We fear the effects of continued inbreeding."
    scene 39_s20 with dissolve
    ysella "It's not just a tradition—it's survival too."
    scene 39_s17 with dissolve
    call screen scene42_choice01 with dissolve

label scene42_choice01_op1:
    $ mc_paricipated_festival = True
    mc "Alright. I'll participate. I'm not sure I agree with all of it, but... I can see you're desperate."
    mc "If I can help, I will."
    scene 39_s20 with dissolve
    ysella "Wonderful! Oh, wonderful! The Goddess will be so pleased! A fresh champion."
    scene 39_s26 with dissolve
    oswald "Goddess bless you, [mc]. You have given us hope we haven't felt in years."
    scene 39_s17 with dissolve
    mc "How does this competition go? Do we fight?"
    scene 39_s20 with dissolve
    ysella "It isn't just about physical prowess, though that certainly matters. We hold three trials for the mind, body, and soul."
    scene 39_s26 with dissolve
    oswald "Why not prepare, [mc]? Take a rest, get yourself ready."
    scene 39_s17 with dissolve
    mc "Can I get some hints on what's to come?"
    scene 39_s26 with dissolve
    oswald "Heh, that wouldn't be fair to the others, would it?"
    scene 39_s17 with dissolve
    mc "Fine. I'll be at the cabin then."
    scene 39_s20 with dissolve
    ysella "Of course."
    scene 39_s17 with dissolve
    jump scene42_continue2

label scene42_choice01_op2:
    mc "I don't want to participate. I only came here to trade, that's all."
    scene 42_s33 with dissolve
    ysella "Are you certain, [mc]? We could really use someone like you. Think of our dying village..."
    scene 42_s41 with dissolve
    mc "Sorry, but I'm sure. I hope things get better for you."
    mc "And just a tip... don't rely on a ritual to repopulate. Let people choose who they love."
    mc "Sigrun and Aldwin clearly love each other, so let them be together. Let people marry who they want."
    scene 42_s32 with dissolve
    oswald "Heresy!"
    scene 42_s33 with dissolve
    ysella "Calm down, Oswald. He's an outsider. He doesn't understand yet."
    ysella "So be it. We thank you for coming to our village, [mc]. Safe travels. May the road rise to meet you."
    scene 42_s41 with dissolve
    jump scene42_continue2

label scene42_continue2:
    stop music fadeout 1.0 
    scene 42_s34 with Fade(1.0,1.0,1.0)
    if not mc_paricipated_festival:
        mc "Alex, get up. We're leaving."
        "*knock* *knock*"
        mc "Hmm?"
        scene 42_s42 with dissolve
        mc "Yes?"
        scene 42_s43 with dissolve
        annette "Um... [mc]. I saw you walking back here."
        scene 42_s42 with dissolve
        mc "What do you want?"
        scene 42_s43 with dissolve
        annette "I—sorry. I didn't mean to intrude. I just... I heard you said no to the festival."
        scene 42_s42 with dissolve
        mc "Yeah. I'm not interested in their goddess-blessed breeding contest."
        scene 42_s43 with dissolve
        annette "I understand. Really. I just thought..."
        annette "Maybe you could stay a little longer. Not for the ritual—just... for a day or two. There's still food. The weather's nice. The moon's been... really pretty at night."
        scene 42_s42 with dissolve
        mc "You asking me to stargaze with you?"
        scene 42_s43 with dissolve
        annette "N-No!"
        scene 42_s44 with dissolve
        annette "I mean—maybe...?"
        scene 42_s45 with dissolve
        mc "Annette... this village has some serious issues. I'm not sure I belong here."
        scene 42_s43 with dissolve
        annette "Maybe not. But that doesn't mean you have to vanish the moment you say no."
        annette "If nothing else... I'd like to talk again. Before you go."
        scene 42_s42 with dissolve
        call screen scene42_choice02 with dissolve

    else:
        if mc_lost_festival:
            scene 46_s1 with Fade(1.0,1.0,2.0)
            mc "*yawn*"
            scene 42_s34 with Fade(0.5,0.5,0.5)
            mc "Alex, get up. We're leaving."
            alex "Mhnmm..."
            mc "Come on. We got the supplies we needed."
            $ mc_coin += 50
            scene 42_s36 with vpunch
            alex "*groan* Fine! Stop screaming."
            scene 42_s35 with dissolve
            mc "I wasn't..."
            jump scene50_maia_event
        else:
            mc "Alex? Seriously? You're still asleep?"
            alex "Mmm..."
            mc "I might need some help with something."
            alex "*groan* Go away..."
            scene 42_s37 with dissolve
            mc "Alright... Might as well take a nap too."
            scene black with Fade(1.0,1.0,1.0)
            play music "night.mp3" fadein 2.0 volume 0.2 loop
            "*knock* *knock* *knock*"
            scene 42_s38 with dissolve
            ymir "[mc]? It's time."
            scene 42_s39 with dissolve
            mc "Huh? Oh right, coming..."
            scene 42_s38 with dissolve
            ymir "And... I just want to apologize for my behavior earlier."
            ymir "I... I also need you to wear this."
            scene black with fade
            mc "This? Uh... Sure."
            jump scene43

    label scene42_choice02_op1:
        $ mc_paricipated_festival = True
        mc "*sigh* ...I guess I can stay a little longer."
        scene 42_s44 with dissolve
        annette "Really?! I'll go tell Mother right now!"
        scene 42_s46 with dissolve
        mc "Wait!"
        mc "..."
        scene 42_s37 with dissolve
        mc "*sigh* Might as well take a nap before the shenanigans start."
        scene black with Fade(1.0,1.0,1.0)
        play music "night.mp3" fadein 2.0 volume 0.2 loop
        "*knock* *knock* *knock*"
        scene 42_s38 with dissolve
        ymir "[mc]? It's time."
        scene 42_s39 with dissolve
        mc "Huh? Oh right, coming..."
        scene 42_s38 with dissolve
        ymir "And... I just want to apologize for my behavior earlier."
        ymir "I... I also need you to wear this."
        scene black with fade
        mc "This? Uh... Sure."
        jump scene43

    label scene42_choice02_op2:
        mc "I've already made my decision, Annette."
        annette "..."
        scene 42_s43 with dissolve
        annette "I see..."
        annette "Then... please take care out there, [mc]."
        scene 42_s42 with dissolve
        mc "..."
        annette "..."
        scene 42_s46 with dissolve
        ""
        scene 42_s34 with dissolve
        mc "Alex."
        alex "Mmmm... Wha..."
        mc "Alex!"
        scene 42_s36 with vpunch
        alex "Huh?! What!?"
        scene 42_s35 with dissolve
        mc "Get up. We're leaving."
        scene 42_s36 with dissolve
        alex "W-Why? Did something happen?"
        scene 42_s35 with dissolve
        mc "I'll explain on the way. Come on."
        scene 42_s36 with dissolve
        alex "*yawn* Alright... did you at least get some supplies?"
        scene 42_s35 with dissolve
        mc "We won't find any supplies here."
        jump scene50_maia_event

label scene43:
    scene 43_s1 with Fade(1.0,1.0,1.0)
    ""
    play music "cult.mp3" fadein 2.0 loop
    scene 43_s2 with Fade(0.5,0.5,0.5)
    env "The villagers gather in a wide circle. Fire sway in the wind. At the center, three men sit before Ysella and Oswald."
    ysella "Sit, [mc]. We have been waiting for you."
    scene 43_s3 with dissolve
    ysella "My people, we gather once more for our sacred festival."
    ysella "Tonight, four men step forward, their spirits weighed against the will of the Goddess. Only the worthy may claim her favor."
    scene 43_s4 with dissolve
    ysella "Heiter, son of the Agnarr bloodline, who stands proud in his family's name."
    ysella "Agi, heir to the Brynjarr family, whose strength has long upheld our traditions."
    ysella "Aldwin, of the Faroald kin, whose name once stood unchallenged in this sacred trial."
    scene 43_s5 with dissolve
    ysella "And [mc]... a traveler. One who walks with no name, but carries the weight of will."
    mc "..."
    mc "(I really hope Alex doesn't mind this little situation I got myself in...)"
    scene 43_s3 with dissolve
    ysella "Heiter, [mc]. Agi and Aldwin. Step forward."
    scene 43_s6 with dissolve
    roza "Good luck."
    scene 43_s7 with Fade(0.5,0.5,0.5)
    ysella "This is the Trial of the soul. A battle not of fists, but of endurance. Conquer yourself."
    heiter "Ready?"
    mc "I think..."
    scene 43_s8 with dissolve
    ysella "Drink."
    scene 43_s9 with dissolve
    mc "Huh? What's in this...?"
    mc "(Shit... I'm feeling...)"
    stop music fadeout 2.0 
    scene 43_s10 with Fade(2.0,1.0,2.0)
    play music "soul.mp3" fadein 1.0 loop
    call screen scene43_forward with dissolve
    scene 43_s11 with dissolve
    call screen scene43_forward with dissolve
    scene 43_s12 with dissolve
    pause(0.5)
    call screen scene43_choice01 with dissolve

label scene43_choice01_op1:
    scene 43_s13 with dissolve
    ""
    scene 43_s14 with dissolve
    ""
    scene 43_s15 with dissolve
    ""
    scene 43_s16 with vpunch
    ""
    jump scene43_continue

label scene43_choice01_op2:
    $ mc_plunge = True
    scene 43_s17 with dissolve
    ""
    scene 43_s18 with Dissolve(1.0)
    ""
    jump scene43_continue

label scene43_continue:
    scene black with Fade(1.0,1.0,1.0)
    stop music 
    if mc_plunge:
        scene 43_s19 with vpunch
        mc "*gasp* What the!"
        play music "cult.mp3" fadein 3.0 loop
        sensation "Your limbs feel heavy, your mind sluggish. The air is thick, suffocating. A ringing hum lingers in your ears."
        ysella "[mc] has prevailed!"
        scene 43_s20 with dissolve
        mc "Is he gonna be fine?"
        scene 43_s21 with dissolve
        ysella "He will wake in time."
        roza "*tch* You still have a long way to go, Heiter."
        ysella "I'm sure you're eager, [mc] but you still have two others who want to take what could be yours."
    else:
        scene 43_s45 with Dissolve(1.0)
        ysella "Heiter prevails! [mc] couldn't handle the liquor and woke up later than him."
        heiter "Yes!"
        mc "Hnngg..."
        sensation "Your limbs feel heavy, your mind sluggish. The air is thick, suffocating. A ringing hum lingers in your ears."
    scene black with fade
    ysella "Step forward, Agi."
    scene 43_s22 with Fade(0.5,0.5,0.5)
    ysella "This is a trial of the mind. A contest of riddles—whoever proves the sharper will claim victory."
    scene 43_s24 with dissolve
    mc "Riddles? Oh no..."
    scene 43_s23 with dissolve
    agi "Focus, brother."
    scene 43_s24 with dissolve
    ysella "I hold dominion over kings and peasants alike. I can make men kneel or rise, yet I have no blood, no body, no voice. What am I?"
    logic "It affects everyone, regardless of their status. Not something physical... but something that lives in the mind? Whatever it is, it controls, but doesn't command."
    call screen scene43_choice02 with dissolve

default scene43_counter = 0
label scene43_choice02_correct:
    $ scene43_counter += 1
    mc "Fear!"
    ysella "Correct. [mc] wins this round."
    scene 43_s23 with dissolve
    agi "I knew it too but you were quicker. Good job."
    scene 43_s24 with dissolve
    mc "Thank you."
    jump scene43_continue2

label scene43_choice02_wrong:
    ysella "Wrong."
    scene 43_s23 with dissolve
    agi "Fear?"
    scene 43_s24 with dissolve
    ysella "Correct. Agi wins this round."
    mc "Damn..."
    jump scene43_continue2

label scene43_continue2:
    ysella "Next riddle."
    ysella "I offer freedom to all, yet I enslave those who follow me. I promise truth, yet speak only what you wish to hear. What am I?"
    logic "It tempts people... maybe even gives them hope. But the more you give in to it, the more it owns you. Something seductive. Dangerous."
    call screen scene43_choice03 with dissolve

label scene43_choice03_correct:
    $ scene43_counter += 1
    mc "Desire."
    ysella "You got it right, [mc]."
    scene 43_s23 with dissolve
    agi "Ah, desire. I assumed it was temptation."
    scene 43_s24 with dissolve
    jump scene43_continue3

label scene43_choice03_wrong:
    ysella "Wrong."
    if mc_answered_temp:
        scene 43_s23 with dissolve
        agi "Temptation?"
        scene 43_s24 with dissolve
        ysella "Agi..."
        scene 43_s23 with dissolve
        agi "What? Oh... Sorry I wasn't paying attention."
        scene 43_s24 with dissolve
        ysella "That's no good Agi. Focus."
        scene 43_s23 with dissolve
        agi "I apologize. It's just that [mc] has a nice body. I can't seem to stare away."
        scene 43_s24 with dissolve
        mc "..."
        ysella "*ahem* Let's continue."
    else:
        scene 43_s23 with dissolve
        agi "Temptation?"
        scene 43_s24 with dissolve
        ysella "Wrong. Neither of you got it right."
        scene 43_s23 with dissolve
        agi "*chuckles* This one's too hard, huh?"
        scene 43_s24 with dissolve
    jump scene43_continue3

label scene43_continue3:
    ysella "Last riddle!"
    ysella "I walk without feet, speak without breath, and die each time I am born. What am I?"
    logic "It's something fleeting. Repeating. A reflection, maybe? Every time it appears, it fades just as quickly..."
    call screen scene43_choice04 with dissolve

label scene43_choice04_correct:
    $ scene43_counter += 1
    mc "An echo?"
    ysella "Correct, [mc]."
    scene 43_s23 with dissolve
    agi "Ah, I thought I had it."
    scene 43_s24 with dissolve
    jump scene43_continue4

label scene43_choice04_wrong:
    ysella "Wrong."
    scene 43_s23 with dissolve
    agi "An echo?"
    scene 43_s24 with dissolve
    ysella "Yes, Agi. That is correct."
    mc "Shit."
    jump scene43_continue4

label scene43_continue4:
    scene 43_s26 with dissolve
    if scene43_counter >= 2:
        $ mc_riddles = True
        ysella "A brilliant display of quick thinking by [mc]! You won this trial."
        scene 43_s23 with dissolve
        agi "*sigh* You won, fair and square. Well played."
        scene 43_s24 with dissolve
        mc "Thank you."
    else:
        ysella "A brilliant display of quick thinking by Agi! You won this trial."
        scene 43_s24 with dissolve
        mc "Damn it! I was never good with riddles..."
        scene 43_s23 with dissolve
        agi "*chuckles* You did well. Don't let it weigh on you, brother."
        scene 43_s24 with dissolve
        mc "Thanks..."

    scene 43_s23 with dissolve
    agi "You're after my sister?"
    scene 43_s24 with dissolve
    mc "What are you talking about?"
    scene 43_s23 with dissolve
    agi "Annette. I'm sure you've met her by now."
    scene 43_s24 with dissolve
    mc "Oh... yeah, I have."
    scene 43_s23 with dissolve
    agi "If you do end up winning this thing... just take care of her, alright?"
    agi "She's... not like the others around here. Too soft. Too sensitive for the kind of life we live."
    scene 43_s24 with dissolve
    mc "I see. I'll keep that in mind."
    scene 43_s23 with dissolve
    agi "You'd better."
    scene 43_s24 with dissolve
    scene black with Fade(0.5,0.5,0.5)
    ysella "Aldwin has proven his strength against Heiter in a single punch."
    scene 43_s3 with Fade(0.5,0.5,0.5)
    oswald "And now, the final trial. Let us see how our champions have fared!"

    if mc_riddles:
        $ mc_festival_count += 1
    if mc_plunge:
        $ mc_festival_count += 1

    if mc_festival_count == 1:
        ysella "It's a tie between [mc] and Aldwin!"
        ysella "Aldwin, step forward. Your next and final trial is against [mc]."
        scene 43_s27 with Fade(0.5,0.5,0.5)
        ysella "The final trial is of the body. A test of strength and resolve."
        ysella "Whoever lands three clean strikes shall be declared the victor of this trial. Strike with honor—no blows to the crotch."
    elif mc_festival_count == 2:
        ysella "[mc] has the lead with two wins! However, Aldwin, you can still bring it back."
        ysella "Aldwin, step forward. Your next and final trial is against [mc]."
        scene 43_s27 with Fade(0.5,0.5,0.5)
        ysella "The final trial is of the body. A test of strength and resolve."
        ysella "Usually, whoever lands three clean strikes would be declared the victor of this trial."
        ysella "But since you're behind, Aldiwn. You must deliver five strikes to [mc] if you want to win. [mc] on the other hand must only deliver three."
    else:
        $ mc_lost_festival = True
        ysella "It's a tie between Agi and Aldwin!"
        ysella "Aldwin, step forward. Your next and final trial is against Agi."
        oswald "The rest of the contestant are now withdrawn. You may stand up and leave."
        mc "(Shit... I lost.)"
        jump scene43_mc_lose

    if mc_festival_count == 2:
        scene 43_s28 with dissolve
        aldwin "Please..."
        scene 43_s29 with dissolve
        mc "What is it?"
        scene 43_s30 with dissolve
        aldwin "..."
        scene 43_s31 with dissolve
        ""
        scene 43_s32 with dissolve
        ""
        scene 43_s28 with dissolve
        aldwin "*sigh* I can't do this anymore. My wife prepared me a vitality brew, but... it's wearing off."
        aldwin "I can't fight you, not like this."
        aldwin "Please, [mc]. Surrender my wife to me."
        scene 43_s29 with dissolve
        mc "What are you talking about? You can still win, you just have to hit me five times instead of three."
        scene 43_s28 with dissolve
        aldwin "I told you that I can barely move my body to hit you twice, let alone five times at this point so just hear me out..."
        aldwin "The winner can surrender any famlies they don't want. I only ask of you to not mate with my wife."
        aldwin "Please... I'll reward you with everything I have. You'd be doing me a kindness."
        scene 43_s29 with dissolve
        mc "..."
        call screen scene43_choice05 with dissolve

    elif mc_festival_count == 1:
        scene 43_s28 with dissolve
        aldwin "Please..."
        scene 43_s29 with dissolve
        mc "What is it?"
        scene 43_s30 with dissolve
        aldwin "..."
        scene 43_s31 with dissolve
        ""
        scene 43_s32 with dissolve
        ""
        scene 43_s28 with dissolve
        aldwin "*sigh* I can't do this anymore. My wife prepared me a vitality brew, but... it's wearing off."
        aldwin "I can't fight you, not like this. Please... let me have this win."
        scene 43_s29 with dissolve
        mc "I only won once... If you win, you'll claim the other families."
        scene 43_s28 with dissolve
        aldwin "I'll surrender them to you. I swear it. I don't care about any of that—I just want my wife."
        aldwin "Please... I'll reward you with everything I have. You'd be doing me a kindness."
        scene 43_s29 with dissolve
        mc "..."
        call screen scene43_choice05 with dissolve

label scene43_mc_lose:
    scene 43_s46 with Fade(1.0,1.0,1.0)
    roza "A shame you didn't win. I actually had my hopes up for you."
    scene 43_s47 with dissolve
    ada "Don't let it get to you, [mc]! You can always try later. Although, you'll miss out on us... Maybe with the next generation then?"
    scene 43_s46 with dissolve
    roza "*chuckles* Assuming he won't be shriveled up like a prune by then. You're already looking a little sluggish now."
    scene 43_s66 with dissolve
    mc "Yeah, yeah. Laugh all you want. I participated, and that's good enough for me."
    scene 43_s46 with dissolve
    roza "I'm not laughing... pfft... I swear I'm not."
    scene 43_s48 with Fade(0.5,0.5,0.5)
    ysella "Let [mc] breathe, girls. I'm sure he's worn out after that."
    scene 43_s49 with dissolve
    mc "So, I lost?"
    scene 43_s48 with dissolve
    ysella "Indeed. But you should be honored that you were chosen to participate in the first place."
    scene 43_s49 with dissolve
    mc "I don't feel honored."
    scene 43_s48 with dissolve
    ysella "Now, now, [mc]. It isn't a good look to be sore about it. Remember, there's always next time."
    scene 43_s49 with dissolve
    mc "I suppose so, {i}years{/i} later. Anyway, thank you, Ysella, but I guess it's our time to leave. Tomorrow morning, we're leaving."
    scene 43_s48 with dissolve
    ysella "I understand. Still, we're glad that you stayed till this point, [mc]. Please have a safe journey."
    ysella "We shall provide you two with some supplies as thanks for participating."
    scene 43_s49 with dissolve
    mc "Thank you."
    scene 43_s50 with Fade(1.0,1.0,2.0)
    mc "*sigh* You won't believe what I went through, Alex..."
    mc "I keep ending up in the weirdest situations since I got here."
    alex "*groan* Good for you..."
    mc "Yeah. Anyway, we're leaving tomorrow. We got the supplies we need."
    alex "Mfhmm."
    mc "Hmm..."
    impulse "She's right there. Soft. Warm. You could disappear into her and forget everything else."
    call screen scene43_choice06 with dissolve

label scene43_choice05_op1:
    $ mc_let_aldwin_win = True
    $ mc_won_festival = True
    $ mc_lost_festival = False
    mc "Fine, I'll let you have her."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 43_s28 with dissolve
    aldwin "Thank you, brother. You have a kind heart."
    scene 43_s29 with dissolve
    ysella "What are you two waiting for? Begin!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 43_s27 with dissolve
    ""
    play sound "sound_effects/punch.mp3"
    scene 43_s35 with vpunch
    mc "Agh!"
    play sound "sound_effects/bodydrop.mp3"
    scene 43_s37 with dissolve
    ysella "Aldwin proves his strength once again! A single punch is all it took to down [mc]."
    mc "(Shit! That hurt!)"
    aldwin "Hahhaa... *cough*... Thank you."
    scene 43_s38 with dissolve
    mc "You didn't have to punch so hard..."
    aldwin "*chuckles* Sorry, I had to make it look believable."
    scene 43_s43 with dissolve
    aldwin "Mother... I'd like to forsake my victory in favor of [mc]. I only ask for my wife."
    scene 43_s44 with dissolve
    oswald "What are you saying, Aldwin?"
    scene 43_s43 with dissolve
    aldwin "[mc] fought with honor. His skills are unmatched. My health isn't what it was... I have no strength to satisfy the village's expectations. Only my wife."
    aldwin "Let the second-best take my place."
    scene 43_s44 with dissolve
    ysella "Hmm... If you are unable to fulfill the Goddess's blessing, then so be it."
    ysella "[mc] shall assume your burden. He will bless the willing."
    scene 43_s41 with dissolve
    aldwin "Meet me before you leave our village, I'll have prepared something for you."
    scene 43_s42 with dissolve
    mc "Ouch... Got it."
    jump scene43_continue5

default scene43_punch_count = 0
default scene43_aldwin_punch_count = 0
label scene43_choice05_op2:
    mc "We fight as intended, Aldwin. No deal."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 43_s28 with dissolve
    aldwin "*groan* Damn..."
    scene 43_s29 with dissolve
    ysella "What are you two waiting for? Begin!"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 43_s27 with dissolve
    if persistent.skip_mini:
        "Mini-Game Skipped"
        
        jump scene43_continue5
    else:
        ""
    $ result = renpy.call_screen("quick_event")
    if result == "Perfect":
        play sound "sound_effects/punch.mp3"
        scene 43_s33 with vpunch
        aldwin "Nghnn!"
        $ scene43_punch_count += 1

    elif result == "Good":
        if random.randint(1, 100) <= aldwin_chance:
            play sound "sound_effects/punch.mp3"
            scene 43_s33 with vpunch
            aldwin "Nghnn!"
            $ scene43_punch_count += 1
        else:
            scene 43_s34 with vpunch
            ysella "[mc] strikes but Aldwin evades!"

    elif result == "Bad":
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            aldwin "Dammit!"
            ysella "Aldwin takes the advantage but misses!"

        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            ysella "[mc] stumbles! Aldwin takes the advantage and strikes back!"
            $ scene43_aldwin_punch_count += 1

    else: 
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            ysella "Aldwin punches but [mc] evades!"
        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            $ scene43_aldwin_punch_count += 1

    scene 43_s27 with dissolve
    ""

    $ result = renpy.call_screen("quick_event")
    if result == "Perfect":
        play sound "sound_effects/punch.mp3"
        scene 43_s33 with vpunch
        aldwin "Agghh!"
        $ scene43_punch_count += 1

    elif result == "Good":
        if random.randint(1, 100) <= aldwin_chance:
            play sound "sound_effects/punch.mp3"
            scene 43_s33 with vpunch
            aldwin "AGHH!"
            $ scene43_punch_count += 1
        else:
            scene 43_s34 with vpunch
            ysella "[mc] strikes but Aldwin evades!"

    elif result == "Bad":
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            aldwin "Dammit!"
            ysella "Aldwin takes the advantage but misses!"

        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            ysella "[mc] stumbles! Aldwin takes the advantage and strikes back!"
            $ scene43_aldwin_punch_count += 1

    else: 
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            ysella "Aldwin punches but [mc] evades!"
        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            $ scene43_aldwin_punch_count += 1

    if mc_festival_count == 2:
        if scene43_punch_count >= 3 or scene43_aldwin_punch_count >= 5:
            jump scene43_continue5
        else:
            jump scene43_punch_again
    else:
        if scene43_punch_count >= 3 or scene43_aldwin_punch_count >= 3:
            jump scene43_continue5
        else:
            jump scene43_punch_again

label scene43_punch_again:
    scene 43_s27 with dissolve
    ""
    $ result = renpy.call_screen("quick_event")
    if result == "Perfect":
        play sound "sound_effects/punch.mp3"
        scene 43_s33 with vpunch
        aldwin "Tchh!"
        $ scene43_punch_count += 1

    elif result == "Good":
        if random.randint(1, 100) <= aldwin_chance:
            play sound "sound_effects/punch.mp3"
            scene 43_s33 with vpunch
            aldwin "AGHH!"
            $ scene43_punch_count += 1
        else:
            scene 43_s34 with vpunch
            ysella "[mc] strikes but Aldwin evades!"

    elif result == "Bad":
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            aldwin "Dammit!"
        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            ysella "[mc] stumbles! Aldwin takes the advantage and strikes back!"
            $ scene43_aldwin_punch_count += 1
    else: 
        if random.randint(1, 100) <= aldwin_chance:
            scene 43_s36 with dissolve
            ysella "Aldwin punches but [mc] evades!"
        else:
            play sound "sound_effects/punch2.mp3"
            scene 43_s35 with vpunch
            mc "Ghnnm!"
            $ scene43_aldwin_punch_count += 1
    
    if mc_festival_count == 2:
        if scene43_punch_count >= 3 or scene43_aldwin_punch_count >= 5:
            if scene43_aldwin_punch_count >= 5:
                $ mc_aldwin_win_festival = True
            jump scene43_continue5
        else:
            jump scene43_punch_again
    else:
        if scene43_punch_count >= 3 or scene43_aldwin_punch_count >= 3:
            if scene43_aldwin_punch_count >= 3:
                $ mc_aldwin_win_festival = True
            jump scene43_continue5
        else:
            jump scene43_punch_again

label scene43_continue5:
    if mc_aldwin_win_festival:
        $ mc_lost_festival = True
        play sound "sound_effects/bodydrop.mp3"
        scene 43_s37 with dissolve
        ysella "Aldwin proves his strength once again!"
        mc "(Shit! That hurt!)"
        aldwin "Hahhaa... *cough*... Looks like I still got it."
        scene 43_s38 with dissolve
        aldwin "Here. Up you go, son."
        jump scene43_mc_lose
        
    if not mc_let_aldwin_win:
        $ mc_won_festival = True
        $ mc_lost_festival = False
        play sound "sound_effects/bodydrop.mp3"
        scene 43_s39 with vpunch
        ysella "And the winner is the outsider, [mc]!"
        scene 43_s40 with dissolve
        sigrun "Are you well, dear?"
        aldwin "*cough* *cough*... I'm fine..."
        sigrun "You're not. I'll get you some water—hold on."
    stop music fadeout 2.0 
    scene 43_s45 with Fade(1.0,1.0,1.0)
    play music "night.mp3" fadein 3.0 loop
    ysella "Our people, with that, our festival concludes! May the Goddess bless us with strong children to carry us forward!"

    if mc_let_aldwin_win:
        scene 43_s46 with Fade(2.0,1.0,1.0)
        roza "So Aldwin won—but he still handed you the honors, huh?"
        scene 43_s47 with dissolve
        ada "I still don't get why Mother and Father even chose him, knowing how sick he's been..."
        scene 43_s46 with dissolve
        roza "Regardless, you did well. Better than most."
        scene 43_s47 with dissolve
        ada "*giggles* And Heiter! One punch—he just crumpled like bread!"
        scene 43_s66 with dissolve
        ysella "Scurry along, ladies. I need to talk to [mc]."
        scene 43_s49 with dissolve
        ada "Yes, Mother."
        roza "Good night, [mc]~"
        scene 43_s48 with dissolve
        ysella "Even though you didn't win [mc], you showed us great performance today that even Aldwin was impressed by."
        scene 43_s49 with dissolve
        mc "I'm glad."

    else:
        scene 43_s46 with Fade(2.0,1.0,1.0)
        roza "Good job out there, champ."
        scene 43_s47 with dissolve
        ada "*giggles* I still can't believe Heiter went down with one punch!"
        scene 43_s66 with dissolve
        mc "Thanks. I guess that's it, then?"
        scene 43_s46 with dissolve
        roza "Not quite, big guy."
        scene 43_s66 with dissolve
        ysella "Scurry along, ladies. I need to talk to [mc]."
        scene 43_s49 with dissolve
        ada "Yes, Mother."
        roza "Good night, [mc]~"
        scene 43_s48 with dissolve
        ysella "Congratulations, [mc]. I knew you had it in you from the moment I saw you."
        scene 43_s49 with dissolve
        mc "...Really? Thanks."

    mc "So... what happens now?"
    scene 43_s48 with dissolve
    ysella "I imagine you're eager—as any man would be. But there is still one thing left to do."
    scene 43_s49 with dissolve
    mc "Really? I thought this was it."
    scene 43_s48 with dissolve
    ysella "Almost."
    ysella "The Goddess may grant her favor, but it is the women who grant themselves."
    ysella "You must win their hearts, [mc]. Only then will their bodies follow."
    scene 43_s49 with dissolve
    mc "That might be harder than the trials."
    scene 43_s48 with dissolve
    ysella "*chuckles* Don't give up just yet."
    ysella "Tomorrow, when you wake, go to them. Speak with each. Show them who you are."
    scene 43_s49 with dissolve
    mc "Got it. One more trial, huh?"
    scene 43_s48 with dissolve
    ysella "The most important one of all."
    scene 43_s49 with dissolve
    mc "Any tips?"
    scene 43_s48 with dissolve
    ysella "Mmm... listen more than you speak. Each of them wants something different—some want strength, some want kindness, and some... just want to be heard."
    scene 43_s49 with dissolve
    mc "Alright, thanks."
    scene 43_s48 with dissolve
    ysella "I'm counting on you, [mc]."
    scene 43_s49 with dissolve
    play music "night.mp3" fadein 3.0 volume 0.2 loop
    scene 43_s50 with Fade(1.0,1.0,2.0)
    mc "You won't believe what I went through, Alex..."
    mc "I keep ending up in the weirdest situations since I arrived to this world."
    alex "*groan* Good for you..."
    mc "I thought that was the end of it, but apparently... there's still more to do."
    mc "*sigh* And I'm not even tired. I already slept through most of the day."
    mc "Hmm..."
    impulse "She's right there. Soft. Warm. You could disappear into her and forget everything else."
    call screen scene43_choice06 with dissolve

label scene43_choice06_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene6_p4_replay:
        $ persistent.scene6_p4_replay = True
    $ mc_masturbated_to_alex = True
    scene 43_s50
    mc "Hey... Alex?"
    mc "Remember when I caught you going at it the other night?"
    mc "I never told you, but... I stayed awake after. Listened. Couldn't sleep."
    alex "Pervert."
    mc "You think I had a choice? You were being too loud. I want some payback."
    alex "*groan* You better be kidding..."
    mc "I'm not, so..."
    alex "*grumple* Just don't get your... seed on me."
    if persistent.alex_d:
        scene 43_s61 with dissolve
    elif persistent.alex_p:
        scene 43_s51 with dissolve
    perception "Alex shifts and removes the blanket, turning her body toward you—clearly annoyed, but too tired to care."
    call screen scene43_choice07 with dissolve

label scene43_choice07_ltits:
    $ scene43_ltits = True
    $ scene43_lpussy = False
    $ scene43_lfeet = False
    scene 43_s59 with dissolve
    call screen scene43_choice07 with dissolve
label scene43_choice07_ltits_inspect:
    scene 43_s59 with dissolve
    perception "Her chest rises and falls slowly with each breath, soft mounds resting naturally. The faintest movement draws your eyes—round, supple, and gently swaying with her breath."
    call screen scene43_choice07 with dissolve
label scene43_choice07_ltits_touch:
    scene 43_s60 with dissolve
    sensation "You reach out, brushing your fingertips against the gentle slope of her breast. Soft... warm... your touch barely enough to disturb her skin."
    call screen scene43_choice07 with dissolve

label scene43_choice07_lpussy:
    $ scene43_ltits = False
    $ scene43_lpussy = True
    $ scene43_lfeet = False
    if persistent.alex_p:
        scene 43_s62 with dissolve
    elif persistent.alex_d:
        scene 43_s57 with dissolve
    call screen scene43_choice07 with dissolve

label scene43_choice07_lpussy_inspect:
    if persistent.alex_p:
        scene 43_s62 with dissolve
        perception "Her folds are barely parted, glistening faintly from heat and sleep. You feel your cock twitch at the sight."
    elif persistent.alex_d:
        scene 43_s57 with dissolve
        perception "Her cock glistens beneath the soft glow of the lamp. A rush of thoughts pierce your mind—desires you haven't fully accepted, not yet."
    call screen scene43_choice07 with dissolve
label scene43_choice07_lpussy_touch:
    if persistent.alex_p:
        scene 43_s63 with dissolve
        sensation "Your fingers trace the outer edge of her folds—warm and slightly damp. The skin there is delicate, responsive, pulsing with quiet heat. She shifts slightly in her sleep, but doesn't wake."
    elif persistent.alex_d:
        scene 43_s58 with dissolve
        sensation "You brush your fingers over her tip. It's hot to the touch, pulsing slightly. A subtle shudder travels through it as you begin to tease her."
    call screen scene43_choice07 with dissolve
label scene43_choice07_lpussy_sniff:
    sensation "You inch closer, her scent growing clearer—sweet, raw, intimate. A natural perfume that hits the back of your throat and settles in your spine."
    call screen scene43_choice07 with dissolve

label scene43_choice07_lfeet:
    $ scene43_ltits = False
    $ scene43_lpussy = False
    $ scene43_lfeet = True
    if persistent.alex_p:
        scene 43_s52 with dissolve
    elif persistent.alex_d:
        scene 43_s55 with dissolve
    call screen scene43_choice07 with dissolve
label scene43_choice07_lfeet_inspect:
    if persistent.alex_p:
        scene 43_s52 with dissolve
    elif persistent.alex_d:
        scene 43_s55 with dissolve
    perception "Her legs are stretched out, toes curling slightly with each breath. They're slender, soft-looking, dotted with tiny imperfections that somehow make them perfect."
    call screen scene43_choice07 with dissolve
label scene43_choice07_lfeet_touch:
    if persistent.alex_p:
        scene 43_s53 with dissolve
    elif persistent.alex_d:
        scene 43_s56 with dissolve
    sensation "You graze a finger along the sole of her foot. It twitches faintly, but she doesn't move. Smooth... tender... impossibly delicate."
    scene 43_s54 with dissolve
    perception "Your lips meet her toes, and your tongue traces a slow, wet path across her skin. Her foot twitches in response."
    if persistent.alex_p:
        scene 43_s53 with dissolve
    elif persistent.alex_d:
        scene 43_s56 with dissolve
    call screen scene43_choice07 with dissolve
label scene43_choice07_lfeet_sniff:
    sensation "You lift one gently and bring it closer—an earthy warmth clings to her skin, subtle but strangely arousing."
    call screen scene43_choice07 with dissolve

label scene43_choice07_cum:
    sensation "Your fist glides up your shaft slowly, your breath catching with each stroke. The images in your mind blur with what's right in front of you—her shape, her warmth, her scent."
    play sound "se_sfx/blowjob/facial1.mp3" 
    show screen cum
    mc "Ahh!"
    if persistent.alex_p:
        scene 43_s64 with dissolve
    elif persistent.alex_d:
        scene 43_s65 with dissolve
    mc "Fuck..."
    scene black with Fade(2.0,1.0,1.0)
    perception "You wipe yourself with a cloth by the bedside, then lie back down, heart slowing, eyes heavy. The last thing you hear is her soft breathing beside you."
    hide screen cum
    $ renpy.end_replay()
    jump scene43_continue6

label scene43_choice06_op2:
    mc "(Yeah, better not get any weird ideas.)"
    jump scene43_continue6

label scene43_continue6:
    scene 43_s67 with fade
    mc "..."
    "*knock* *knock*"
    scene 43_s68 with dissolve
    mc "Someone there?"
    scene 43_s69 with dissolve
    if not mc_won_festival:
        annette "Hello, [mc]... I-I came to make you feel better."
        scene 43_s70 with dissolve
        mc "Feel better? About what?"
        scene 43_s69 with dissolve
        annette "Your loss at the festival."
        scene 43_s70 with dissolve
        mc "Ah, I already got over it. You don't have to worry, Annette."
        scene 43_s69 with dissolve
        annette "T-That's good... Umm... is it still alright if we play a game? I saw you lying there, unable to sleep, so I thought... maybe you'd want to pass the time."
        scene 43_s70 with dissolve
        mc "Play?"
        mc "Wait... you were watching me?"
        scene 43_s73 with dissolve
        annette "Mhm. From the window."
        scene 43_s70 with dissolve
        mc "...Right."
        annette "..."
        mc "What kind of game are we talking about?"
        scene 43_s69 with dissolve
        annette "Umm..."  
        annette "Oh! Let's play... touch and tell!"
        scene 43_s70 with dissolve
        mc "How does that work?"
        scene 43_s69 with dissolve
        annette "W-We take turns. One of us closes our eyes, and the other gives them something to feel... then you have to guess what it is."
        scene 43_s70 with dissolve
    else:
        annette "Hello, [mc]... I-I came to congratulate you."
        scene 43_s70 with dissolve
        mc "Thank you. Did you need something?"
        scene 43_s69 with dissolve
        annette "No... I just saw you lying there, unable to sleep, so I thought... maybe you'd want to play."
        scene 43_s70 with dissolve
        mc "Play?"
        mc "Wait... you were watching me?"
        scene 43_s73 with dissolve
        annette "Mhm. From the window."
        scene 43_s70 with dissolve
        mc "...Right."
        annette "..."
        mc "What kind of game are we talking about?"
        scene 43_s69 with dissolve
        annette "Umm..."  
        annette "Oh! Let's play... touch and tell!"
        scene 43_s70 with dissolve
        mc "How does that work?"
        scene 43_s69 with dissolve
        annette "W-We take turns. One of us closes our eyes, and the other gives them something to feel... then you have to guess what it is."
        scene 43_s70 with dissolve
    call screen scene43_choice08 with dissolve

label scene43_choice08_op1:
    mc "I'm not really in the mood for games tonight."
    scene 43_s71 with dissolve
    annette "Oh... I see."
    scene 43_s72 with dissolve
    mc "Thanks for checking in, though."
    scene 43_s71 with dissolve
    if not mc_won_festival:
        annette "O-Of course... Goodnight, [mc]. I hope you have a safe journey tomorrow."
    else:
        annette "O-Of course... Goodnight, [mc]."
    jump scene44
    
label scene43_choice08_op2:
    mc "Sounds fun. Sure."
    scene 43_s69 with dissolve
    annette "Alright!"
    play music "annette.mp3" fadein 3.0 volume 0.5 loop
    scene 43_s75 with Fade(0.5,0.5,0.5)
    annette "I'll go first. Close your eyes."
    scene 43_s74 with dissolve
    scene black with fade
    mc "Okay, I'm ready."
    sensation "Your finger brushes against soft, warm skin. It gives slightly under pressure—smooth, but a little hollow."
    scene 43_s75 with dissolve
    annette "Now guess!"
    scene 43_s74 with dissolve
    call screen scene43_choice09 with dissolve

label scene43_choice09_shoulder:
    mc "Is it... your shoulder?"
    scene 43_s76 with dissolve
    annette "*giggles* Wrong!"
    scene 43_s77 with dissolve
    mc "Damn. Elbow?"
    scene 43_s76 with dissolve
    annette "It was my cheek!"
    scene 43_s77 with dissolve
    mc "Damn it. Should've known."
    jump scene43_continue7
    
label scene43_choice09_hand:
    mc "Is it your hand?"
    scene 43_s75 with dissolve
    annette "Wrong~"
    scene 43_s74 with dissolve
    mc "Seriously?"
    scene 43_s75 with dissolve
    annette "Yep~ It was my cheek!"
    scene 43_s74 with dissolve
    mc "Ugh. Of course."
    jump scene43_continue7

label scene43_choice09_cheek:
    mc "Is it your cheek?"
    scene 43_s76 with dissolve
    annette "Yes! Good job."
    scene 43_s77 with dissolve
    mc "Come on, that was easy."
    scene 43_s76 with dissolve
    annette "Hahaha~ Then no complaints when I get the next one!"
    scene 43_s77 with dissolve
    jump scene43_continue7

label scene43_continue7:
    mc "Alright. Your turn—close your eyes."
    scene 43_s78 with dissolve
    impulse "Shove it up—"
    mc "No."
    annette "Hmm?"
    mc "Nothing. Just... deciding."
    call screen scene43_choice10 with dissolve

label scene43_choice10_mcm:
    $ scene43_mcmouth = True
    scene 43_s79 with dissolve
    annette "Ah! It feels... wet..."
    scene 43_s74 with dissolve
    mc "Okay. Go."
    scene 43_s75 with dissolve
    annette "Wait... was it... your mouth?"
    scene 43_s74 with dissolve
    mc "Correct."
    scene 43_s76 with dissolve
    annette "Ahaha! That was too easy."
    scene 43_s77 with dissolve
    mc "Yeah, yeah. Don't get cocky."
    mc "Your turn."
    scene black with fade
    if scene43_nose:
        jump scene43_lips
    else:
        jump scene43_nose

label scene43_nose:
    $ scene43_nose = True
    scene black with fade
    sensation "It's soft, tight, oddly humid. Squishy at the tip and slightly cool."
    scene 43_s74 with dissolve
    call screen scene43_choice11 with dissolve

label scene43_choice09_ear:
    mc "Is it... your ear?"
    scene 43_s76 with dissolve
    annette "*snorts* Wrong!"
    scene 43_s77 with dissolve
    mc "Damn."
    scene 43_s76 with dissolve
    annette "It was my nose!"
    scene 43_s77 with dissolve
    mc "Eww..."
    scene 43_s76 with dissolve
    annette "Hahahaha~"
    if scene43_mcmouth:
        scene 43_s82 with dissolve
        annette "Payback for sticking my finger in your mouth."
        scene 43_s77 with dissolve
        mc "Fair enough. My turn."
    else:
        mc "Laughing at my misery?"
        annette "Hehe~"
    mc "Close your eyes."
    scene 43_s78 with dissolve
    call screen scene43_choice10 with dissolve

label scene43_choice09_lips1:
    mc "Your lips?"
    scene 43_s75 with dissolve
    annette "Wrong!"
    scene 43_s74 with dissolve
    mc "Damn, okay. What was it?"
    scene 43_s75 with dissolve
    annette "My nose!"
    scene 43_s74 with dissolve
    mc "Eww..."
    scene 43_s76 with dissolve
    annette "Hahahaha~"
    if scene43_mcmouth:
        scene 43_s82 with dissolve
        annette "Payback for sticking my finger in your mouth."
        scene 43_s77 with dissolve
        mc "Fair enough. My turn."
    else:
        scene 43_s77 with dissolve
        mc "Laughing at my misery?"
        annette "Hehe~"
    mc "Close your eyes."
    scene 43_s78 with dissolve
    call screen scene43_choice10 with dissolve

label scene43_choice09_nose:
    mc "Is it... your nose?"
    scene 43_s76 with dissolve
    annette "Yes!"
    scene 43_s77 with dissolve
    mc "Eww..."
    scene 43_s76 with dissolve
    annette "Hahahaha~"
    if scene43_mcmouth:
        scene 43_s82 with dissolve
        annette "Payback for sticking my finger in your mouth."
        scene 43_s77 with dissolve
        mc "Fair enough. My turn."
    else:
        scene 43_s77 with dissolve
        mc "Laughing at my misery?"
        annette "Hehe~"
    mc "Close your eyes."
    scene 43_s78 with dissolve
    call screen scene43_choice10 with dissolve

label scene43_choice10_mcn:
    $ scene43_mcneck = True
    scene 43_s81 with dissolve
    annette "Hmm..."
    annette "This is... soft. Kind of bumpy... chin?"
    scene 43_s74 with dissolve
    mc "You're close. Try again."
    scene 43_s75 with dissolve
    annette "Neck?"
    scene 43_s74 with dissolve
    mc "Yep."
    scene 43_s75 with dissolve
    annette "Hah! Knew it."
    annette "My turn. Close your eyes!"
    if scene43_nose:
        jump scene43_lips
    else:
        jump scene43_nose

label scene43_choice10_mcc:
    $ scene43_mcchest = True
    scene 43_s80 with dissolve
    annette "Woah..."
    annette "It feels... muscly."
    scene 43_s75 with dissolve
    annette "Your chest?"
    scene 43_s74 with dissolve
    mc "Yup."
    scene 43_s75 with dissolve
    annette "It felt really hard. Are you used to lifting heavy things [mc]?"
    scene 43_s74 with dissolve
    mc "I used to. I'm not sure if this world has a gym."
    scene 43_s75 with dissolve
    annette "Gym? And what do you mean by this world?"
    scene 43_s74 with dissolve
    mc "Forget it."
    scene 43_s76 with dissolve
    annette "Wait! Did you come from space!? *giggle*"
    scene 43_s77 with dissolve
    mc "Uh... Yes. It was a long journey through the stars. I finally made it here after years and my plan to conquer your planet is going smoothly."
    scene 43_s76 with dissolve
    annette "*laughs* I'm not young to believe these stories anymore, you know?"
    scene 43_s77 with dissolve
    mc "You'll see one day~"
    scene 43_s76 with dissolve
    annette "My turn. Close your eyes!"
    if scene43_nose:
        jump scene43_lips
    else:
        jump scene43_nose

label scene43_lips:
    scene black with fade
    sensation "Something warm... and soft. Not like before. Delicate. It lingers longer than the others."
    scene 43_s74 with dissolve
    call screen scene43_choice12 with dissolve

label scene43_choice09_lips2:
    mc "Is it your lips?"
    scene 43_s75 with dissolve
    annette "Maybe."
    scene 43_s74 with dissolve
    mc "What do you mean, maybe?"
    scene 43_s76 with dissolve
    annette "It's a secret."
    scene 43_s77 with dissolve
    mc "Oh, come on..."
    jump scene43_continue8

label scene43_choice09_boobs1:
    $ scene43_boobs1 = False
    mc "Is it your boobs?"
    scene 43_s76 with dissolve
    annette "*laughs* Wrong!"
    scene 43_s77 with dissolve
    mc "You sure?"
    scene 43_s76 with dissolve
    annette "You really want another guess?"
    scene 43_s77 with dissolve
    call screen scene43_choice12 with dissolve

label scene43_choice09_boobs2:
    mc "Yep. It has to be your boobs."
    scene 43_s82 with dissolve
    annette "You already guessed that!"
    scene 43_s77 with dissolve
    mc "*sigh* Alright, I give up. What was it?"
    scene 43_s76 with dissolve
    annette "It's a secret."
    scene 43_s77 with dissolve
    mc "Oh, come on..."
    jump scene43_continue8

label scene43_choice09_hair:
    mc "Was it... your hair?"
    scene 43_s82 with dissolve
    annette "Really? That doesn't feel anything like hair."
    scene 43_s74 with dissolve
    mc "*groan* Alright, I lost. What was it?"
    scene 43_s76 with dissolve
    annette "It's a secret."
    scene 43_s77 with dissolve
    mc "Oh, come on..."
    jump scene43_continue8
    
label scene43_continue8:
    scene 43_s75 with Fade(1.0,1.0,1.0)
    annette "Well... That was fun."
    scene 43_s74 with dissolve
    mc "Yeah. Surprisingly."
    scene 43_s75 with dissolve
    if not mc_won_festival:
        annette "Goodnight, [mc]. I-I hope you come visit our village sometime soon."
        scene 43_s74 with dissolve
        mc "Maybe not soon, but who knows."
        scene 43_s75 with dissolve
        annette "Well, whenever you're in the way, please don't hesistate to come. Our people are very generous and would welcome you anytime."
        scene 43_s74 with dissolve
        mc "Thank you, Annette. Take care of yourself."
    else:
        annette "Goodnight, [mc]. I have to leave before my brother learns I'm not in bed."
        scene 43_s74 with dissolve
        mc "Are you sure that was your brother? You two don't look very similar. No offense."
        scene 43_s75 with dissolve
        annette "He... is?"
        scene 43_s74 with dissolve
        mc "You don't sound very sure about that."
        scene 43_s75 with dissolve
        annette "I don't know... I don't really... remember."
        annette "A-Anyway! I really have to go. Thank you for playing with me tonight, [mc]. It was... really fun."
        scene 43_s74 with dissolve
        mc "Of course. Sleep well, Annette."
        mc "(Something isn't right with her...)"

    stop music fadeout 2.0 
    if not mc_won_festival:
        jump scene42_continue2
    else:
        jump scene44
    
image maia_m1 = Movie(play="images/3_chapter2/scene44/maia44_m1.webm", loop=True)
image maia_m2 = Movie(play="images/3_chapter2/scene44/maia44_m2.webm", loop=True)

label scene44:
    if not mc_maia_left:
        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene7_p4_replay:
            $ persistent.scene7_p4_replay = True
        $ mc_saw_maia_event = True
        scene 43_s67 with Fade(0.5,0.5,0.5)
        ""
        stop music fadeout 2.0 
        scene black with Fade(2.0,1.0,1.0)
        play music "maia.mp3" fadein 2.0 loop
        scene 43_s83 with dissolve
        ""
        scene black with dissolve
        env "The morning light spills gently across the stone floor. In the quiet of the quarters, Maia sits with Crumps."
        scene 44_s1 with Fade(0.5,0.5,0.5)
        m "*sigh* Where did you go, [mx]...?"
        m "You left without a word. Again."

        if maia_pussy_sex > 0:
            $ maia_pussy_virgin = False
            $ maia_virgin = False
        if maia_anal_sex > 0:
            $ maia_anus_virgin = False
            $ maia_virgin = False
        if maia_pregnant:
            $ maia_pussy_virgin = False
            $ maia_virgin = False

        if maia_virgin:
            m "You never even touched me, yet my body won't stop aching..."
            scene 44_s2 with dissolve
            play sound "sound_effects/meow.mp3"
            crumps "Mao."
            m "Hmm?"
            crumps "Mmmph. Mrow."
            scene 44_s1 with dissolve
            m "It's not fair. He made me feel this way and just left."
            scene 44_s3 with dissolve
            m "I'll just have to make do..."
            m "If I don't... I'll go insane..."
            m "Please... look away, Crumps."
            play sound "sound_effects/meow2.mp3"
            crumps "Meow..."
            stop music fadeout 2.0 
            scene 44_s4 with Fade(1.0,0.5,0.5)
            m "Just... pretend he's here..."
            play sound "se_sfx/sex/touch2.mp3" 
            scene 44_s5 with dissolve
            m "S-Slowly..."
            show maia_m1 with dissolve
            m "Ahhh... Hahh~"
            m "Hnngh... [mx]... you don't even know what you do to me..."
            m "Why do you make me feel like this...?"
            m "It hurts... and yet... it feels so good..."
            m "Mmh~ [mx]... I wish it was your hands... not this stupid banana!"
            m "Hnn... I'm such an idiot...!"
            m "Hahh... [mx]... I'm gonna—! Nghhh~!"
            show maia_m2 with dissolve
            hide maia_m1 with dissolve
            m "Hnmm~ [mx]! [mx]!"
            m "Yes~ Yes! Just like that, [mc]~ It's sooooo huge~"
            m "I can't... Hnghh~ believe I'm doing this again... but it feels... so good!"
            m "[mx]... I'm going to... spill my juices all over your pillow!"
            stop sound
            scene 44_s6 with vpunch
            r "*yawn* Maia, would you accompany me to the market—"
            scene 44_s7 with dissolve
            r "..."
            scene 44_s8 with dissolve
            m "..."
            scene 44_s7 with dissolve
            ""
            play sound "sound_effects/door.mp3"
            scene 44_s9 with dissolve
            ""
            scene 44_s10 with dissolve
            m "Someone please kill me..."
            $ renpy.end_replay()
        else:
            m "My body hasn't stopped aching since..."
            scene 44_s2 with dissolve
            play sound "sound_effects/meow.mp3"
            crumps "Mao."
            m "Hmm?"
            play sound "sound_effects/meow.mp3"
            crumps "Mmmph. Mrow."
            scene 44_s1 with dissolve
            m "I hope so too..."
            scene 44_s3 with dissolve
            m "I'll just have to make do until he returns..."
            m "Please... look away, Crumps."
            play sound "sound_effects/meow2.mp3"
            crumps "Meow..."
            stop music fadeout 2.0 
            scene 44_s4 with Fade(1.0,0.5,0.5)
            m "I hope you don't mind me doing it above your pillow, [mx]..."
            m "Alright. just... pretend it's him..."
            play sound "se_sfx/sex/touch2.mp3" 
            scene 44_s5 with dissolve
            m "S-Slowly..."
            show maia_m1 with dissolve
            m "Ahhh! Hahh~"    
            m "Hnn... husband... just like that..."
            m "Don't leave me empty again..."
            m "It's okay, husband~ Hnng~ You can be rough with me!"
            show maia_m2 with dissolve
            hide maia_m1 with dissolve
            m "Hnmm~ [mx]! [mx]!"
            m "Yes~ Yes! Just like that, [mc]~ It's sooooo huge~"
            m "I can't... Hnghh~ believe I'm doing this again... but it feels... so good!"
            m "[mx]... I'm going to... spill my juices all over your pillow!"
            stop sound
            scene 44_s6 with vpunch
            r "*yawn* Maia, would you accompany me to the market—"
            scene 44_s7 with dissolve
            r "..."
            scene 44_s8 with dissolve
            m "..."
            scene 44_s7 with dissolve
            ""
            play sound "sound_effects/door.mp3"
            scene 44_s9 with dissolve
            ""
            scene 44_s10 with dissolve
            m "Someone please kill me..."
            $ renpy.end_replay()
        
        if not mc_won_festival:
            jump scene42_continue2
        else:
            jump scene45

    else:
        if not mc_won_festival:
            jump scene42_continue2
        else:
            jump scene45

        jump scene45

default scene45_first = True
default scene45_second = False

label scene45:
    play music "nature.mp3" fadein 2.0 volume 0.5 loop
    if mc_date_adaroza_final and mc_date_annette_final:
        if mc_let_aldwin_win:
            jump scene49
        else:
            if mc_date_sigrun_final:
                jump scene49
            else:
                if scene45_first:
                    $ scene45_first = False
                    $ scene45_second = True
                    scene 46_s1 with Fade(1.0, 1.0, 1.0)
                    mc "(Alright, let's do this. Just a little talk with the girls, it can't be hard, right?)"
                    call screen scene46_choice01 with dissolve

                elif scene45_second:
                    $ mc_saw_yuuhi_event = True
                    $ scene45_second = False
                    scene black with Fade(1.0, 1.0, 1.0)
                    scene 43_s83 with dissolve
                    stop music fadeout 2.0 
                    ""
                    play music "yuuhi.mp3" fadein 2.0 loop
                    scene 47_s43 with fade
                    yuuhi "(No, no, no... The seam needs to sit {i}above{/i} the hipbone, not below! Ugh, I'm such a fraud...)"
                    yuuhi "(You think Gavlan would ever had to worry about waistlines? I bet he just wore whatever the wind gave him...)"
                    dean "Yuuhi! The Queen's guards want that tabard before sundown!"
                    scene 47_s44 with dissolve
                    yuuhi "I'm working on it!"
                    scene 47_s43 with dissolve

                    if mc_harem_yuuhi:
                        yuuhi "(...I hope [mc] is alright.)"
                        yuuhi "(No more daydreaming...)"
                    play sound "sound_effects/metalhit.mp3"
                    scene 47_s45 with vpunch
                    yuuhi "Ah!"
                    dean "What happened? That damn club fall again?!"
                    scene 47_s46 with dissolve
                    yuuhi "...No."
                    scene 47_s47 with dissolve
                    dean "We ought to throw that thing out. No one's ever going to buy it."
                    scene 47_s46 with dissolve
                    yuuhi "No! There has to be someone... out there... maybe..."
                    scene 47_s47 with dissolve
                    stop music fadeout 2.0 
                    scene 46_s1 with Fade(1.0, 1.0, 1.0)
                    play music "nature.mp3" fadein 2.0 volume 0.5 loop
                    call screen scene46_choice01 with dissolve

                else:
                    scene 46_s1 with Fade(1.0, 1.0, 1.0)
                    play music "nature.mp3" fadein 2.0 volume 0.5 loop
                    call screen scene46_choice01 with dissolve
    else:
        if scene45_first:
            $ scene45_first = False
            $ scene45_second = True
            scene 46_s1 with Fade(1.0, 1.0, 1.0)
            mc "(Alright, let's do this. Just a little talk with the girls, it can't be hard, right?)"
            call screen scene46_choice01 with dissolve

        elif scene45_second:
            $ scene45_second = False
            scene black with Fade(1.0, 1.0, 1.0)
            scene 43_s83 with dissolve
            stop music fadeout 2.0 
            ""
            play music "yuuhi.mp3" fadein 2.0 loop
            scene 47_s43 with fade
            yuuhi "(No, no, no... The seam needs to sit {i}above{/i} the hipbone, not below! Ugh, I'm such a fraud...)"
            yuuhi "(You think Gavlan would ever had to worry about waistlines? I bet he just wore whatever the wind gave him...)"
            dean "Yuuhi! The Queen's guards want that tabard before sundown!"
            scene 47_s44 with dissolve
            yuuhi "I'm working on it!"
            scene 47_s43 with dissolve
            if mc_harem_yuuhi:
                yuuhi "(...I hope [mc] is alright.)"
                yuuhi "(No more daydreaming...)"
            play sound "sound_effects/metalhit.mp3"
            scene 47_s45 with vpunch
            yuuhi "Ah!"
            dean "What happened? That damn club fall again?!"
            scene 47_s46 with dissolve
            yuuhi "...No."
            scene 47_s47 with dissolve
            dean "We ought to throw that thing out. No one's ever going to buy it."
            scene 47_s46 with dissolve
            yuuhi "No! There has to be someone... out there... maybe..."
            scene 47_s47 with dissolve
            stop music fadeout 2.0 
            scene 46_s1 with Fade(1.0, 1.0, 1.0)
            play music "nature.mp3" fadein 2.0 volume 0.5 loop
            call screen scene46_choice01 with dissolve

        else:
            scene 46_s1 with Fade(1.0, 1.0, 1.0)
            play music "nature.mp3" fadein 2.0 volume 0.5 loop
            call screen scene46_choice01 with dissolve

label scene46_adaroza:
    stop music fadeout 2.0 
    $ mc_date_adaroza = True
    scene 46_s2 with Fade(1.0,0.5,0.5)
    play music "date1.mp3" fadein 3.0 volume 0.5  loop
    perception "You step outside and find Ada and Roza seated on a bench beneath the shade of a tree. Their postures are casual, but there's a spark of curiosity in their eyes."
    scene 46_s5 with fade
    mc "You two look comfortable. Feels like I'm doing an interview..."
    scene 46_s4 with dissolve
    ada "Don't be too tense. I'm sure Mother Ysella exaggerated it... we're just talking."
    scene 46_s5 with dissolve
    mc "Alright, what are we talking about?"
    scene 46_s3 with dissolve
    roza "You, of course."
    scene 46_s4 with dissolve
    ada "We want to know a bit more about the man we're supposed to... you know... accept."
    scene 46_s3 with dissolve
    roza "Think of it as a little warm-up before the real fun."
    scene 46_s5 with dissolve
    mc "Alright. Ask away."
    scene 46_s3 with dissolve
    roza "How big is it?"
    scene 46_s6 with dissolve
    ada "Roza!"
    scene 46_s7 with dissolve
    roza "Sorry, sorry! I meant emotionally."
    scene 46_s4 with dissolve
    ada "*ahem* What she meant to ask is... do you think we could feel safe around you, [mc]?"
    scene 46_s5 with dissolve
    call screen scene46_choice02 with dissolve

label scene46_choice02_op1:
    mc "Safe? Maybe. Satisfied? Definitely."
    scene 46_s7 with dissolve
    roza "Hah! Goddess, you're ridiculous."
    scene 46_s6 with dissolve
    ada "Roza, don't encourage him!"
    jump scene46_adaroza2

label scene46_choice02_op2:
    $ mc_date_adaroza_points += 1
    mc "I'd do my best. I'm not perfect, but I try."
    scene 46_s4 with dissolve
    ada "Honest. I like that more than pretending."
    scene 46_s3 with dissolve
    roza "Trying's better than running."
    jump scene46_adaroza2

label scene46_choice02_op3:
    $ mc_date_adaroza_points += 2
    mc "With me? Always. I'd never let harm come to either of you."
    scene 46_s4 with dissolve
    ada "That's... reassuring."
    scene 46_s3 with dissolve
    roza "Chivalrous and confident. Not bad. Let's hope it's not just talk."
    jump scene46_adaroza2

label scene46_adaroza2:
    scene 46_s3 with dissolve
    roza "Didn't you once get chased around the yard by a rooster, Ada?"
    scene 46_s6 with dissolve
    ada "That was ages ago!"
    scene 46_s7 with dissolve
    roza "*laughs* And I'll never forget it. You screamed like it was a dragon chasing you."
    scene 46_s47 with dissolve
    mc "Should I be worried next time we pass a coop?"
    scene 46_s6 with dissolve
    ada "You two are the worst..."
    scene 46_s7 with dissolve
    roza "Let's just hope [mc] is braver than you, or those chickens might win again."
    scene 46_s6 with dissolve
    ada "Can we please just move on?"
    scene 46_s7 with dissolve
    roza "Alright, next one—what do you value most in a woman?"
    scene 46_s5 with dissolve
    call screen scene46_choice03 with dissolve

label scene46_choice03_op1:
    $ mc_date_adaroza_points += 1
    mc "Her loyalty. I'd rather be with someone who stands by me through everything."
    scene 46_s4 with dissolve
    ada "That's... sweet."
    scene 46_s3 with dissolve
    roza "Good answer. Could've been worse."
    jump scene46_adaroza3

label scene46_choice03_op2:
    mc "Her body. I mean, who doesn't appreciate a beautiful figure?"
    scene 46_s8 with dissolve    
    ada "Oh..."
    scene 46_s3 with dissolve
    roza "Predictable."
    roza "And speaking of bodies..."
    jump scene46_adaroza3

label scene46_choice03_op3:  
    $ mc_date_adaroza_points += 2
    mc "Her spirit. The way she thinks."
    mc "I care more about the person than the shape."
    scene 46_s4 with dissolve
    ada "That's really thoughtful..."
    scene 46_s3 with dissolve
    roza "Oh~ I wasn't expecting that from you, [mc]. Nicely said."
    jump scene46_adaroza3

label scene46_adaroza3:
    roza "Say, [mc]... which of us has the bigger breasts?"
    scene 46_s6 with dissolve
    ada "That's not a fair question..."
    scene 46_s7 with dissolve
    roza "Really? Why not?"
    scene 46_s6 with dissolve
    ada "Because..."
    scene 46_s7 with dissolve
    roza "Go on."
    scene 46_s8 with dissolve
    ada "*sigh* Because yours are bigger..."
    scene 46_s7 with dissolve
    roza "Correct. Glad we cleared that up."
    scene 46_s47 with dissolve
    call screen scene46_choice04 with dissolve

label scene46_choice04_op1:
    mc "Honestly? I prefer smaller breasts."
    scene 46_s4 with dissolve
    ada "R-Really?!"
    scene 46_s3 with dissolve
    roza "No way you're serious. He's just saying it to make you feel better, dear."
    scene 46_s5 with dissolve
    mc "No. I genuinely do."
    scene 46_s4 with dissolve
    ada "Hehe~ See? It's not always about how big it is."
    scene 46_s3 with dissolve
    roza "You're weird."
    roza "Alright weirdo, final question."
    roza "If you had to choose between me and Ada... who would you pick?"
    scene 46_s6 with dissolve
    ada "Ugh! For fuck's sake!"
    scene 46_s47 with dissolve
    call screen scene46_choice05 with dissolve

label scene46_choice04_op2:
    mc "Yeah. The bigger the better. No offense, Ada."
    scene 46_s6 with dissolve
    ada "Alright, alright, no need to shove it in my face. I get it."
    scene 46_s7 with dissolve
    roza "Don't pout, darling. I'm sure someone out there appreciates... subtlety."
    scene 46_s6 with dissolve
    ada "Shut up..."
    scene 46_s7 with dissolve
    roza "Let's move on. Final question."
    roza "If you had to choose between me and Ada... who would you pick?"
    scene 46_s6 with dissolve
    ada "Ugh! For fuck's sake!"
    scene 46_s47 with dissolve
    call screen scene46_choice05 with dissolve

label scene46_choice05_op1:
    $ mc_date_adaroza_points += 1
    mc "Roza. I like a woman who speaks her mind."
    scene 46_s3 with dissolve
    roza "Flattery will get you everywhere."
    scene 46_s8 with dissolve
    ada "Guess I need to be louder then..."
    jump scene46_adaroza4

label scene46_choice05_op2:
    $ mc_date_adaroza_points += 2
    mc "I couldn't choose. You're both incredible in your own way."
    scene 46_s4 with dissolve
    ada "That's... really sweet."
    scene 46_s3 with dissolve
    roza "You wriggled your way out of this one. But I'll allow it."
    jump scene46_adaroza4

label scene46_choice05_op3:
    $ mc_date_adaroza_points += 1
    mc "Ada. I like quiet, reserved women."
    scene 46_s4 with dissolve
    ada "T-Thank you... *ahem* And please forgive me for swearing, I usually don't say things like that."
    scene 46_s3 with dissolve
    roza "Well, that's a first."
    scene 46_s4 with dissolve
    ada "Don't be jealous~"
    jump scene46_adaroza4

label scene46_choice05_op4:
    mc "Whoever moans louder."
    scene 46_s7 with dissolve
    roza "Oh Goddess. That's horrible. *laughs*"
    scene 46_s6 with dissolve
    ada "Roza, stop laughing. You're only making it worse!"
    ada "[mc] please. You can't be saying things like that."
    scene 46_s7 with dissolve
    roza "Oh calm your tits. He's just having fun."
    scene 46_s6 with dissolve
    ada "{size=30}Bitch.{/size}"
    scene 46_s7 with dissolve
    roza "Huh? Did you say something?"
    scene 46_s6 with dissolve
    ada "No."
    jump scene46_adaroza4

label scene46_adaroza4:
    scene 46_s48 with dissolve
    ada "That was a terrible question, Roza..."
    roza "What? It was fun."
    ada "We're supposed to see if he'd make a good partner... not turn it into a competition."
    roza "It still tells us plenty. Especially how he handles pressure."
    scene 46_s47 with dissolve
    mc "Is that what this was? A trap?"
    scene 46_s7 with dissolve
    roza "Life's full of traps, darling. Get used to it."
    scene 46_s6 with dissolve
    ada "*sigh* Goddess help me."
    scene 46_s47 with dissolve
    mc "Are we done?"
    scene 46_s3 with dissolve
    roza "I think we got what we need."
    scene 46_s5 with dissolve
    mc "And how did I do?"
    if mc_date_adaroza_points == 6:
        $ mc_date_adaroza_win = True
        scene 46_s4 with dissolve
        ada "I think Mother Ysella was right. You're... more than just a visitor."
        scene 46_s3 with dissolve
        roza "Don't fall in love with us now. We might just make you stay."
    elif mc_date_adaroza_points >= 3:
        $ mc_date_adaroza_win = True
        scene 46_s4 with dissolve
        ada "Not bad. You're rough around the edges, but..."
        scene 46_s3 with dissolve
        roza "You just need a little polishing. We could help with that~"
    elif mc_date_adaroza_points < 3:
        $ mc_date_adaroza_fail = True
        $ mc_date_adaroza_final = True
        scene 46_s8 with dissolve
        ada "I'm sorry, [mc]... I don't think I'm comfortable with this."
        scene 46_s3 with dissolve
        roza "You're not a bad guy... just not the one for us."
        scene 46_s5 with dissolve
        mc "I see..."
        scene 46_s3 with dissolve
        roza "Don't take it personally. Or maybe do—I don't know, depends on your ego."
        scene 46_s4 with dissolve
        ada "I hope you find someone who fits you, [mc]. I saw Annette sneaking into your cabin a few times so maybe her?"
        scene 46_s5 with dissolve
        stop music fadeout 2.0 
        scene black with Fade(1.0,1.0,1.0)
        empathy "Ada and Roza stand and walk away. Their footsteps are light... but final."
        jump scene45

    if mc_date_adaroza_win:
        if mc_knows_cabin:
            scene 46_s5 with dissolve
            mc "Should I wait for you in the cabin then?"
            scene 46_s4 with dissolve
            ada "Yes. Just... give me a few minutes. I need to freshen up first."
            scene 46_s3 with dissolve
            roza "Are you sure? I might just steal him for myself while you're gone."
            scene 46_s4 with dissolve
            ada "Not worried. I'm sure [mc] will turn and run the moment he smells your unwashed vagina."
            scene 46_s3 with dissolve
            roza "You little..."
            scene 46_s5 with dissolve
            mc "Easy, you two. I can wait."
            scene 46_s3 with dissolve
            roza "Alright then. Just don't keep us waiting too long."
            stop music fadeout 2.0 
            scene 46_s5 with dissolve
            jump scene45
        else:
            $ mc_knows_cabin = True
            scene 46_s5 with dissolve
            mc "What now?"
            scene 46_s4 with dissolve
            ada "Head to the cabin outside the village fence."
            scene 46_s5 with dissolve
            mc "That one? I always wondered why it was so far from everything."
            scene 46_s3 with dissolve
            roza "Now you know. It's... for special occasions."
            scene 46_s4 with dissolve
            ada "But don't go right away. I need to clean up first."
            scene 46_s3 with dissolve
            roza "Are you sure? I might just steal him for myself while you're gone."
            scene 46_s4 with dissolve
            ada "Not worried. I'm sure [mc] will turn and run the moment he smells your unwashed vagina."
            scene 46_s3 with dissolve
            roza "You little..."
            scene 46_s5 with dissolve
            mc "Easy, you two. I can wait."
            scene 46_s3 with dissolve
            roza "Alright then. Just don't keep us waiting too long."
            stop music fadeout 2.0 
            scene 46_s5 with dissolve
            jump scene45

image adaroza_bj1 = Movie(play="images/3_chapter2/scene46/adaroza/ada_roza_bj1.webm", loop=True)
image adaroza_bj1_faster = Movie(play="images/3_chapter2/scene46/adaroza/ada_roza_bj1_faster.webm", loop=True)
image adaroza_bj2 = Movie(play="images/3_chapter2/scene46/adaroza/ada_roza_bj2.webm", loop=True)
image adaroza_bj2_faster = Movie(play="images/3_chapter2/scene46/adaroza/ada_roza_bj2_faster.webm", loop=True)

image ada_bj = Movie(play="images/3_chapter2/scene46/adaroza/ada_bj.webm", loop=True)
image ada_bj_faster = Movie(play="images/3_chapter2/scene46/adaroza/ada_bj_faster.webm", loop=True)
image roza_bj = Movie(play="images/3_chapter2/scene46/adaroza/roza_bj.webm", loop=True)
image roza_bj_faster = Movie(play="images/3_chapter2/scene46/adaroza/roza_bj_faster.webm", loop=True)

image ada_sex = Movie(play="images/3_chapter2/scene46/adaroza/ada_sex.webm", loop=True)
image ada_sex_faster = Movie(play="images/3_chapter2/scene46/adaroza/ada_sex_faster.webm", loop=True)
image roza_sex = Movie(play="images/3_chapter2/scene46/adaroza/roza_sex.webm", loop=True)
image roza_sex_faster = Movie(play="images/3_chapter2/scene46/adaroza/roza_sex_faster.webm", loop=True)

label scene46_adaroza_sex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene8_p4_replay:
        $ persistent.scene8_p4_replay = True
    $ mc_date_adaroza_final = True
    stop music fadeout 2.0 
    scene 46_s46 with Fade(1.0,0.5,1.0)
    perception "You step inside. The room is dimly lit, warm with the scent of sweat and something faintly floral. Roza and Ada are already waiting—naked, side by side, their bare skin illuminated by the flickering firelight."
    scene 46_s11 with fade
    roza "Ready?"
    scene 46_s10 with dissolve
    ada "This is... a little embarrassing..."
    scene 46_s12 with dissolve
    mc "Let's make you girls pregnant."
    scene 46_s11 with dissolve
    roza "Woah. Hold on, big man. Why don't you prepare us first?"
    roza "Make sure our wombs are wet and steamy to properly accept your seed."
    scene 46_s12 with dissolve
    scene 46_s49 with Dissolve(1.5)
    roza "Go on. Don't be shy~"
    call screen scene46_choice0 with dissolve

label scene46_sex_roza_eatp:
    roza "Well? Don't keep a lady waiting... lick."  
    scene 46_s53 with Dissolve(1.5)
    play sound "se_sfx/sex/touch2.mp3" 
    sensation "Your tongue brushes her pussy lightly at first, teasing her."  
    roza "Tch. Don't tease me—ahhh, yes... more like that."  
    roza "Mmmhnnn~ Goddess, yes. You learn fast. Keep that rhythm, right there."  
    sensation "The taste floods your mouth, rich and intoxicating. Every flick of your tongue draws another gasp, another moan."  
    roza "You're making me sing already... what a wicked tongue you have."  
    scene 46_s52 with Dissolve(1.5)
    play sound "se_sfx/lick/lick1.mp3" 
    perception "Her thighs squeeze your head, pulling you tighter as her hips grind against your mouth."  
    roza "Don't stop. Don't you dare stop until I'm shaking."  
    sensation "Your tongue works tirelessly, exploring every curve and fold, chasing her reactions, drawing sharper moans from her throat."  
    roza "Yessss... ahhhhnnn...! Show me, [mc]. Show me how much you crave me."
    scene 46_s49 with Dissolve(1.5)  
    call screen scene46_choice0 with dissolve

label scene46_sex_roza_eata: 
    roza "Mmm... I see where your eyes are drifting. Bold of you, to want {i}that{/i} hole." 
    mc "You want bold? You'll get bold."   
    scene 46_s52 with Dissolve(1.5)
    play sound "se_sfx/lick/lick1.mp3"
    perception "You press your face between her cheeks, tongue darting out."  
    roza "Ahhh~! Gods, yes... That tongue of yours... naughty boy."  
    sensation "Your tongue circles deliberately, tracing the puckered ring, savoring every twitch." 
    scene 46_s53 with Dissolve(1.5)
    play sound "se_sfx/masturbate_female/3_masturbate3.mp3" 
    roza "*giggles* Mmm, yes... take your time. Push your tongue deeper."  
    roza "Deeper! Don't be shy. I want to feel you claiming me there."  
    sensation "You push your tongue inside, the taste sharp, forbidden, but addictive. Her moans grow richer, huskier."  
    roza "Yes... yes... That's it. Goddess, you're too good at this~" 
    scene 46_s49 with Dissolve(1.5)
    call screen scene46_choice0 with dissolve

label scene46_sex_ada_eatp:
    scene 46_s50 with Dissolve(1.5)
    perception "You lower yourself, tongue hovering right at her glistening entrance."  
    play sound "se_sfx/masturbate_female/3_masturbate3.mp3" 
    sensation "The first lick sends hot juice flooding across your lips."  
    ada "M-Mfhmmm~!"  
    roza "I love hearing you moan like that, sweet Ada~"  
    perception "Ada's thighs press against your head, her hips jerking at every flick of your tongue."  
    sensation "The taste is intoxicating, her body opening more with every push of your tongue."  
    ada "Oh Goddess... ahhhnn~! Don't stop...!"  
    roza "He won't. Not until you're shaking apart for us."
    scene 46_s49 with Dissolve(1.5)
    call screen scene46_choice0 with dissolve

label scene46_sex_ada_eata:
    scene 46_s50 with Dissolve(1.5)
    play sound "se_sfx/lick/lick1.mp3"
    perception "You spread Ada's cheeks and bury your face between them."  
    ada "Ahh! H-He's licking... m-my asshole!"  
    roza "*chuckles* Relax, dear. Just breathe... let yourself feel it."  
    scene 46_s51 with Dissolve(1.5)
    play sound "se_sfx/blowjob/facial2.mp3" 
    sensation "Your tongue circles the tight ring before pressing deeper, tasting her heat."  
    ada "Oh Goddess—! That feels so strange, but...! Mhhhnn~"  
    roza "See? He knows what he's doing. Don't be shy, let it out."  
    mc "Mmhhnn..."  
    ada "Ahhhnn~! Goddess, I-I can't believe this...!"  
    ada "[mc] is licking my asshole..."
    roza "Would you lick mine once you're done, [mc]?"
    ada "H-Hold on... I want him to continue doing it for a bit..."
    scene 46_s49 with Dissolve(1.5)
    call screen scene46_choice0 with dissolve

label scene46_adaroza_sex_0:
    roza "Come on, Ada. Let's give him the same treatment."
    scene black with Fade(0.5,0.5,0.5)
    perception "Both girls drop to their knees in front of you, their bare skin brushing against each other."
    show adaroza_bj1 with fade
    sensation "A sudden jolt runs through you as Roza plants the first kiss on your shaft. Her lips are soft, slow, deliberate. Ada follows suit, placing gentle kisses along the underside of your cock, as if worshipping it."
    perception "Their heads move in rhythm. Roza strokes you lazily at the base while Ada flicks her tongue across your tip, tasting you with a shy hum."
    roza "How does it feel?"
    mc "You two are... something else."
    show adaroza_bj2 with dissolve
    hide adaroza_bj1
    sensation "The warmth of their mouths, the teasing pressure of their lips brushing your skin, makes your hips twitch. Their saliva coats your cock gradually, leaving it glistening in the dim light."
    $ scene46_bj1_1 = False
    $ scene46_bj1_2 = True
    call screen scene46_choice06 with dissolve


label scene46_bj1_1:
    $ scene46_bj1_speed = False
    $ scene46_bj1_1 = True
    $ scene46_bj1_2 = False
    scene black with Dissolve(0.3)
    show adaroza_bj1 with dissolve
    call screen scene46_choice06 with dissolve

label scene46_bj1_2:
    $ scene46_bj1_speed = False
    $ scene46_bj1_1 = False
    $ scene46_bj1_2 = True
    scene black with Dissolve(0.3)
    show adaroza_bj2 with dissolve
    call screen scene46_choice06 with dissolve

label scene46_bj1_faster:
    $ scene46_bj1_speed = True
    if scene46_bj1_1:
        show adaroza_bj1_faster with dissolve
        hide adaroza_bj1
        ada "Faster? Sure~ *slurp* *lick*"
        roza "*slurp* Hnnnn~"
    elif scene46_bj1_2:
        show adaroza_bj2_faster with dissolve
        hide adaroza_bj2
        roza "Mnnnn..."
        ada "It's getting bigger~"
    call screen scene46_choice06 with dissolve

label scene46_bj1_slower:
    $ scene46_bj1_speed = False
    if scene46_bj1_1:
        show adaroza_bj1 with dissolve
        hide adaroza_bj1_faster
        ada "Mnnn~"
        roza "You like that~?"
    elif scene46_bj1_2:
        show adaroza_bj2 with dissolve
        hide adaroza_bj2_faster
        roza "Fuck... The smell is making my head spin!"
        ada "Ahhnn~"
    call screen scene46_choice06 with dissolve

label scene46_adaroza_bj2:
    mc "I want you two to suck me dry."
    roza "With pleasure~"
    ada "S-Suck?"
    stop sound fadeout 0.5
    scene 46_s13 with Fade(1.0,1.0,1.0)
    roza "Go ahead, Ada. Don't be shy."
    scene 46_s14 with dissolve
    ada "*gulp* D-Do you... want me to pleasure you with my mouth?"
    scene 46_s15 with dissolve
    mc "Yeah. I want to feel that little mouth around me."
    scene 46_s14 with dissolve
    ada "Alright~"
    play sound "se_sfx/blowjob/blowjob1.mp3"
    scene 46_s16 with dissolve
    ada "Mhmm..."
    roza "I said don't be shy."
    play sound "se_sfx/blowjob/gag1.mp3"
    scene 46_s17 with dissolve
    ada "Mffhghmmm!!"
    show ada_bj with dissolve
    sensation "Her lips wrap around your cock slowly, cautiously. The warmth of her mouth envelops you as her tongue licks underneath, following every vein."
    ada "Mmm... it's so... thick."
    perception "She bobs her head, awkward at first but clearly trying. Spit begins to drip down her chin. Her hand works what her mouth can't reach."
    roza "Don't hog him all to yourself now."
    mc "Take your turn, Roza."
    show roza_bj with Fade(0.5,0.5,0.5)
    hide ada_bj
    perception "Roza slides in with practiced ease. Her mouth is hotter, wetter—her throat more welcoming. You feel her swallow around the tip as she sinks deeper."
    mc "Aghh..."
    sensation "The tight suction of her throat makes your knees tremble. Her pace is confident. She spits on the shaft, strokes it between sucks, then takes you back down without flinching."
    mc "Fuck..."
    roza "Mmmm~ You can ejaculate in my mouth whenever you like."
    $ scene46_bj2_roza = True
    call screen scene46_choice07 with dissolve

default scene46_ada_bj2_first = True
label scene46_bj2_ada:
    $ scene46_bj2_speed = False
    $ scene46_bj2_roza = False
    if scene46_ada_bj2_first:
        $ scene46_ada_bj2_first = False
        ada "Hey! What about me?"
        scene black with Dissolve(0.3)
        show ada_bj with dissolve
        sensation "Roza's pace quickens, tongue dancing as her fingers stroke the base. Your body tenses, your breath hitches."
        ada "He's getting so big..."
        roza "You like that, don't you? Making him twitch like this?"
        ada "Mhmm... I want him to feel good... really good."
        call screen scene46_choice07 with dissolve
    scene black with Dissolve(0.3)
    show ada_bj with dissolve
    ada "Mmmmmm~ *lick* *gag*"
    roza "You like seeing her gag on your cock, don't you?"
    call screen scene46_choice07 with dissolve

label scene46_bj2_roza:
    $ scene46_bj2_speed = False
    $ scene46_bj2_roza = True
    scene black with Dissolve(0.3)
    show roza_bj with dissolve
    roza "Fuck~ I can feel it twitch in my thorat."
    ada "I can't believe you can take it there, how did you learn to do that?"
    call screen scene46_choice07 with dissolve

label scene46_bj2_faster:
    $ scene46_bj2_speed = True
    if scene46_bj2_roza:
        show roza_bj_faster with dissolve
        hide roza_bj
        roza "Mfhmmm~ I can't wait for you fill my throat with that white liquid~"
    else:
        show ada_bj_faster with dissolve
        hide ada_bj
        ada "*gag* *cough* Aghhnnn!"
    call screen scene46_choice07 with dissolve

label scene46_bj2_slower:
    $ scene46_bj2_speed = False
    if scene46_bj2_roza:
        show roza_bj with dissolve
        hide roza_bj_faster
        roza "Mmmmm~ I will keep teasing it even if you ejaculate~"
    else:
        show ada_bj with dissolve
        hide ada_bj_faster
        ada "Slower is better~ I can lick every inch of it like this~"
    call screen scene46_choice07 with dissolve

label scene46_bj2_cum:
    mc "I'm getting close..."
    call screen scene46_choice08 with dissolve

label scene46_choice06_ci_ada:
    scene black with Dissolve(0.3)
    show ada_bj with dissolve
    mc "Ada! Keep going. I want to cum in your mouth."
    ada "I-I'll try..."
    perception "She leans forward, mouth stretching around your shaft. Her inexperience makes it messier, sloppier—but her effort drives you wild."
    mc "*groan* I'm... ahh—"
    play sound "se_sfx/blowjob/gag1.mp3" 
    show screen cum
    scene 46_s18 with vpunch
    perception "You release deep inside her mouth. Ada jerks slightly but doesn't pull away, doing her best to swallow—though some leaks past her lips and drips down her chin."
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 46_s19 with vpunch
    ada "Mgghhmmmm!"
    scene 46_s26 with dissolve
    ada "Ptoo!"
    hide screen cum
    scene 46_s27 with dissolve
    roza "Aww... I'm sure [mc] would have wanted you to swallow that."
    scene 46_s26 with dissolve
    ada "Ah can't!"
    scene 46_s28 with dissolve
    ada "*cough* Hahh... I-I hope that was okay..."
    scene 46_s29 with dissolve
    roza "You did better than I expected, sweetie."
    scene 46_s30 with dissolve
    roza "My womb is quivering... I'm ready~"
    scene black with Fade(0.5,0.5,1.0)
    sensation "Their scent fills the room—ripe, eager, overwhelming. You feel your cock twitch back to life."
    scene 46_s36 with Fade(0.5,0.5,0.5)
    roza "Who do you want to start with~?"
    scene 46_s37 with dissolve
    call screen scene46_choice09 with dissolve

label scene46_choice06_ci_roza:
    scene black with Dissolve(0.3)
    show roza_bj with dissolve
    mc "Roza... I'm going to cum. Keep going."
    roza "Mmm, don't hold back."
    sensation "Her lips seal tight around your shaft. She deepens her rhythm, burying your cock in her throat with every motion."
    mc "F-Fuck!"
    play sound "se_sfx/blowjob/gag2.mp3" 
    show screen cum
    scene 46_s20 with vpunch
    sensation "You erupt into her mouth. Roza doesn't flinch—she swallows each pulse eagerly, her throat twitching around your length."
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 46_s21 with vpunch
    ada "Mmmm~"
    hide screen cum
    scene 46_s22 with dissolve
    perception "When you finish, she slowly pulls back with a wet pop, licking the tip clean."
    roza "Aaahhhhh~"
    play sound "se_sfx/blowjob/swallow1.mp3" 
    scene 46_s23 with dissolve
    roza "*gulp*"
    scene 46_s24 with dissolve
    roza "Mmm~ I love the taste."
    ada "Eww... How can you do that?"
    roza "Hehe~"
    scene 46_s25 with dissolve
    roza "My womb is quivering... I'm ready~"
    scene black with Fade(0.5,0.5,1.0)
    sensation "Their scent fills the room—ripe, eager, overwhelming. You feel your cock twitch back to life."
    scene 46_s36 with Fade(0.5,0.5,0.5)
    roza "Who do you want to start with~?"
    scene 46_s37 with dissolve
    call screen scene46_choice09 with dissolve

label scene46_choice06_co:
    mc "Both of you... get ready."
    roza "As you wish~"
    ada "O-Okay..."
    scene 46_s31 with dissolve
    roza "Aghhhh~"
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 46_s32 with vpunch
    perception "Your cum hits Roza first. A thick streaks across her cheek and lips. Then another spurt on Ada, she winces as one rope hits her eye."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 46_s33 with vpunch
    mc "Agghh!"
    ada "Ah~!"
    hide screen cum
    scene 46_s34 with dissolve
    roza "A shared blessing~"
    scene 46_s35 with dissolve
    ada "Hngg..."
    mc "You two... really know how to worship a man."
    scene 46_s34 with dissolve
    roza "My womb is quivering... I'm ready~"
    scene 46_s35 with dissolve
    scene black with Fade(0.5,0.5,1.0)
    sensation "Their overwhelming scent fills the room. You feel your cock twitch back to life."
    scene 46_s36 with Fade(0.5,0.5,0.5)
    roza "Who do you want to start with~?"
    scene 46_s37 with dissolve
    call screen scene46_choice09 with dissolve

default scene46_sex_ada_first = True
default scene46_sex_ada_first2 = False
default scene46_sex_roza_first = True
default scene46_sex_roza_first2 = False

label scene46_sex_ada:
    $ scene46_sex_speed = False
    $ scene46_sex_roza = True
    scene black with Dissolve(0.3)
    if scene46_sex_ada_first:
        $ scene46_sex_ada_first = False
        $ scene46_sex_ada_first2 = True
        mc "Come here, Ada..."
        ada "*gasp* Y-Yes..."
        play sound "se_sfx/sex/touch1.mp3" 
        scene 46_s39 with dissolve
        sensation "You guide yourself to her entrance—she's wet, almost soaking, but still tight. Her walls wrap around your shaft—squeezing you hard."
        show ada_sex with dissolve
        ada "A-Ah... it's inside..."
        roza "Don't break her, now..."
        mc "No promises."
        sensation "Every thrust draws soft whimpers from her. Her walls pulse and clench around you with every movement."
    elif scene46_sex_ada_first2:
        $ scene46_sex_ada_first2 = False
        show ada_sex with dissolve
        perception "You press into her pussy again, this time rougher, deeper."
        perception "She gasps sharply as your cock fills her. Already wet from watching Roza take you."
        ada "H-Harder... please..."
        mc "Good girl."
        roza "Breed her deep. She needs it."
    else:
        show ada_sex with dissolve
        ada "Hnnnn!! I feel something weird!"
        roza "Just let it happen, dear~"
    call screen scene46_choice010 with dissolve

label scene46_sex_roza:
    $ scene46_sex_speed = False
    $ scene46_sex_roza = False
    scene black with Dissolve(0.3)
    if scene46_sex_roza_first:
        $ scene46_sex_roza_first = False
        $ scene46_sex_roza_first2 = True
        mc "Roza. Come here."
        scene 46_s38 with Fade(0.5,0.5,0.5)
        play sound "se_sfx/sex/touch2.mp3" 
        roza "I've been waiting for this."
        show roza_sex with dissolve
        sensation "Her walls grip you immediately. She rocks her hips against yours, greedy for rhythm."
        roza "Mmm~ Yes. Just like that."
        perception "Your hips slap against her bare flesh, each impact sharper, wetter, louder."
        ada "H-How does that not hurt?"
        roza "Because I want it to."
    elif scene46_sex_roza_first2:
        $ scene46_sex_roza_first2 = False
        show roza_sex with Fade(0.5,0.5,0.5)
        perception "Roza pulls you onto her, guiding your cock back inside without hesitation."
        roza "Give it to me rough. I want to feel it in my stomach."
        sensation "You slam into her, deeper, harder. Her moans grow louder with each thrust, unashamed."
        roza "O-oh Goddess..."
    else:
        show roza_sex with dissolve
        roza "Why is it so fucking big!? Ahh~ I can feel it in my stomach~"
    call screen scene46_choice010 with dissolve

label scene46_sex_faster:
    $ scene46_sex_speed = True
    if not scene46_sex_roza:
        show roza_sex_faster with dissolve
        hide roza_sex
    else:
        show ada_sex_faster with dissolve
        hide ada_sex
    call screen scene46_choice010 with dissolve

label scene46_sex_slower:
    $ scene46_sex_speed = False
    if not scene46_sex_roza:
        show roza_sex with dissolve
        hide roza_sex_faster
    else:
        show ada_sex with dissolve
        hide ada_sex_faster
    call screen scene46_choice010 with dissolve

label scene46_sex_cum:
    $ mc_date_adaroza_win_fin = True
    scene black with Dissolve(0.3)
    show ada_sex with dissolve
    mc "I'm close!"
    roza "Try to ejacualate inside us both!"
    ada "P-Please... I want it inside...!"
    play sound "se_sfx/sex/sex_cum1.mp3" 
    if persistent.xray_mode:
        scene 46_s41_xray1 with vpunch
        sensation "You explode inside Ada first—her legs start trembling, her back arching. Her walls squeeze your cock tight while you try to pull out."
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene 46_s40_xray2 with vpunch
        roza "YES! Give it to me!"
        sensation "Another burst of thick, hot seed floods Roza's womb as she milks you with her slick, desperate walls."
        scene 46_s42_xray3 with Fade(0.5,0.5,0.5)
        perception "Both girls lie sprawled across the bed, legs trembling, filled and leaking."
    else:
        scene 46_s41 with vpunch
        sensation "You explode inside Ada first—her legs start trembling, her back arching. Her walls squeeze your cock tight while you try to pull out."
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene 46_s40 with vpunch
        roza "YES! Give it to me!"
        sensation "Another burst of thick, hot seed floods Roza's womb as she milks you with her slick, desperate walls."
        scene 46_s42 with Fade(0.5,0.5,0.5)
        perception "Both girls lie sprawled across the bed, legs trembling, filled and leaking."
    ada "I feel so full..."
    roza "Hahh... It's leaking all over the bed~"
    scene black with Fade(0.5,0.5,1.0)
    perception "The two of them slowly rise from the bed—bodies trembling, thighs glistening. They stagger slightly as they reach for their clothes."
    scene 46_s43 with fade
    ada "I hope I can get pregnant... I've always wanted to be a mother~"
    scene 46_s44 with dissolve
    roza "Hahh... Yes... Bless this seed, Goddess."
    roza "Thank you, [mc]. That may have been the most enjoyable night of my life."
    scene 46_s43 with dissolve
    ada "I can say the same~"
    scene 46_s45 with dissolve
    mc "Will you two be alright? Want me to carry you?"
    scene 46_s44 with dissolve
    roza "We'll manage..."
    scene 46_s43 with dissolve
    ada "I-I don't mind being carried..."
    scene 46_s45 with dissolve
    scene 46_s46 with dissolve
    perception "They dress slowly, sharing soft glances and lingering touches. As they reach the door, Roza turns back and blows you a kiss."
    roza "Until next time~"
    perception "The door closes behind them, and the cabin falls quiet again. Only the scent of sex and warmth lingers in the air."
    $ renpy.end_replay()
    jump scene45

label scene47_annette:
    $ mc_date_annette = True
    stop music fadeout 2.0 
    scene 47_s1 with Fade(1.0,1.0,1.0)
    play music "annette.mp3" fadein 2.0 loop
    perception "You find Annette standing in the middle of a small flower field, bathed in sunlight."
    annette "[mc]... There you are."
    mc "Hey. Looking for me?"
    scene 47_s3 with dissolve
    annette "Yes. Mother Ysella said we should talk... before... you know."
    scene 47_s2 with dissolve
    mc "I get it. Just a chat, right?"
    scene 47_s3 with dissolve
    annette "Mhmm... Just a chat."
    scene 47_s2 with dissolve
    mc "It's beautiful out here."
    scene 47_s3 with dissolve
    annette "Thank you... I grew all of these myself."
    scene 47_s2 with dissolve
    mc "Seriously? That's amazing."
    scene 47_s3 with dissolve
    annette "I'm glad you like it."
    annette "So... what do you... think of me, [mc]?"
    scene 47_s2 with dissolve
    mc "In what way?"
    scene 47_s3 with dissolve
    annette "Just... in general."
    scene 47_s2 with dissolve
    call screen scene47_choice01 with dissolve

label scene47_choice01_op1:
    $ mc_date_annette_points += 2
    mc "You're sweet. Gentle. I like that about you."
    scene 47_s5 with dissolve
    annette "Thank you... I try to be..."
    jump scene47_annette2

label scene47_choice01_op2:
    mc "You're shy, sure. But I bet you're wild once someone gets you alone."
    scene 47_s7 with dissolve
    annette "I—! T-That's...! I mean..."
    scene 47_s6 with dissolve
    mc "Are you not?"
    annette "..."
    jump scene47_annette2

label scene47_choice01_op3:
    $ mc_date_annette_points += 1
    mc "You're a little weird sometimes. But... kind of cute, too."
    scene 47_s5 with dissolve
    annette "*giggle* I'll take that as a compliment."
    jump scene47_annette2

label scene47_annette2:
    scene 47_s7 with dissolve
    annette "*sigh* The villagers... say I'm weird sometimes."
    scene 47_s6 with dissolve
    mc "Well..."
    scene 47_s7 with dissolve
    annette "Are they right?"
    scene 47_s6 with dissolve
    mc "I did wake up to you staring at me the other day... so..."
    scene 47_s7 with dissolve
    annette "I-I wasn't doing it on purpose! I just... you looked peaceful. I thought maybe... watching you would help me fall asleep too."
    scene 47_s6 with dissolve
    mc "That's not how that works, Annette."
    scene 47_s7 with dissolve
    annette "I know... I just didn't want to be alone in my head."
    scene 47_s6 with dissolve
    mc "You're not weird. Just... different. In a good way."
    scene 47_s3 with dissolve
    annette "You really think so?"
    scene 47_s2 with dissolve
    mc "Mhm."
    scene 47_s3 with dissolve
    annette "And if something bad happened... Would you protect me?"
    scene 47_s2 with dissolve
    mc "From who? The villagers?"
    scene 47_s3 with dissolve
    annette "No. They would never dare to... Just protecting me from anyone who tries to harm me."
    scene 47_s2 with dissolve
    call screen scene47_choice02 with dissolve

label scene47_choice02_op1:
    mc "Honestly? I'd turn around a hundred and eighty degrees and run."
    scene 47_s3 with dissolve
    annette "A hundred and eighty degrees? Doesn't that mean you'd run right back at the danger?"
    scene 47_s2 with dissolve
    mc "Oh... right."
    scene 47_s5 with dissolve
    annette "*laughs* You're funny... but that's not very reassuring..."
    jump scene47_annette3

label scene47_choice02_op2:
    $ mc_date_annette_points += 1
    mc "I mean... depends on what you did."
    scene 47_s3 with dissolve
    annette "*giggle* I guess that's fair..."
    jump scene47_annette3

label scene47_choice02_op3:
    $ mc_date_annette_points += 2
    mc "Of course. I wouldn't let anyone touch you."
    scene 47_s3 with dissolve
    annette "That makes me feel... really safe."
    jump scene47_annette3

label scene47_annette3:
    scene 47_s2 with dissolve
    mc "Do you have a {i}something bad{/i} in mind?"
    scene 47_s3 with dissolve
    annette "*nod* A while ago, a group of goblins settled near our village."
    scene 47_s41 with Dissolve(1.0)
    mc "Goblins?"
    annette "Yes. Sometimes they'd come and steal livestock... they took Erie from me."
    mc "Erie? Is that... your sister?"
    annette "No... my favorite chicken. I raised her from a tiny fluffball."
    mc "Ah... I'm sorry to hear that."
    mc "Did the goblins ever come back?"
    annette "No. Agi and Aldwin found their camp and burned it down. After that, they left."
    scene 47_s2 with dissolve
    mc "Good. Sounds like they did right by you."
    scene 47_s3 with dissolve
    annette "I just... don't want to feel helpless again. It's a horrible feeling."
    scene 47_s2 with dissolve
    mc "I know."
    scene 47_s3 with dissolve
    annette "Alright, I think we're almost done here."
    scene 47_s2 with dissolve
    mc "That's it?"
    scene 47_s3 with dissolve
    annette "Well... Maybe one last question."
    scene 47_s2 with dissolve
    mc "Alright, what is it?"
    scene 47_s7 with Dissolve(0.8)
    annette "After we... um... m-mate... What would you do?"
    scene 47_s6 with dissolve
    call screen scene47_choice03 with dissolve

label scene47_choice03_op1:
    mc "Go for a second round, obviously."
    scene 47_s7 with dissolve
    annette "Y-You're insatiable..."
    jump scene47_annette4

label scene47_choice03_op2:
    $ mc_date_annette_points += 2
    mc "I'd love to cuddle once we're done. Let you sleep on my chest while I hug you."
    scene 47_s7 with dissolve
    annette "That sounds... really nice."
    jump scene47_annette4

label scene47_choice03_op3:
    $ mc_date_annette_points += 1
    mc "Say thanks. Then probably knock out immediately."
    scene 47_s7 with dissolve
    annette "*laughs* I guess that's honest."
    annette "I assume it takes a great deal of stamina to do... {i}that.{/i}"
    scene 47_s6 with dissolve
    mc "Depends. Do you want me to go slow or fast?"
    scene 47_s7 with dissolve
    annette "I-I..."
    jump scene47_annette4

label scene47_annette4:
    annette "Actually, [mc]... there's something I should probably tell you."
    scene 47_s6 with dissolve
    mc "Yeah? What's up?"
    scene 47_s7 with dissolve
    annette "My womb... it's really small. Smaller than normal, they said. It can make things... um... difficult."
    scene 47_s6 with dissolve
    mc "Difficult how?"
    scene 47_s7 with dissolve
    annette "It might hurt. Or... not work right. I mean, I want to do this, I do—but I thought you should know."
    scene 47_s6 with dissolve
    mc "..."
    call screen scene47_choice04 with dissolve 

default mc_hugged_annette = False
label scene47_choice04_op1:
    $ mc_hugged_annette = True
    mc "Come here..."
    scene black with fade
    annette "*gasp* [mc]...?!"
    scene 47_s9 with fade
    mc "Thank you for telling me. We'll take it slow. I want this to feel good for you too."
    scene 47_s8 with dissolve
    annette "O-Okay... That means a lot to me."
    scene 47_s4 with fade
    empathy "Her heartbeat thuds through her ribs—nervous, but trusting."
    jump scene47_annette5

default mc_suggest_anal_annette = False
label scene47_choice04_op2:
    $ mc_date_annette_points -= 1
    $ mc_suggest_anal_annette = True
    mc "Then maybe we try... somewhere else instead."
    scene 47_s7 with dissolve
    annette "Somewhere else?"
    scene 47_s6 with dissolve
    mc "Yeah. You've got a second hole, don't you?"
    scene 47_s7 with dissolve
    annette "I—! T-That's... y-you—"
    annette "If that's what you want... I'll try. Just... be gentle."
    scene 47_s6 with dissolve
    mc "We'll see."
    jump scene47_annette5

label scene47_annette5:
    mc "By the way... what's that smell?"
    scene 47_s3 with dissolve
    annette "Smell? Which flower are you talking about?"
    scene 47_s2 with dissolve
    mc "It's... It's coming from you actually."
    scene 47_s3 with dissolve
    annette "Oh! That's me—um, my vagina."
    scene 47_s2 with dissolve
    mc "...What?"
    scene 47_s3 with dissolve
    annette "I didn't wash it. Mother Ysella said the natural scent—my pheromones—might attract you more."
    scene 47_s2 with dissolve
    call screen scene47_choice05 with dissolve 

default mc_told_annette_shower = False
label scene47_choice05_op1:
    $ mc_told_annette_shower = True
    mc "I think you should... take a shower first."
    scene 47_s3 with dissolve
    annette "Huh? Do I not smell nice, [mc]?"
    scene 47_s2 with dissolve
    mc "You really don't."
    scene 47_s7 with dissolve
    annette "I-I see... I'll go clean myself right away. Please wait for me!"
    jump scene47_annette6

default mc_likes_annette_smell = False
label scene47_choice05_op2:
    $ mc_likes_annette_smell = True
    mc "I like it. Don't wash."
    scene 47_s5 with dissolve
    annette "Hehe~ As you wish."
    jump scene47_annette6

label scene47_annette6:   
    $ mc_date_annette_win = True
    scene 47_s3 with Fade(0.5,0.5,0.5)
    annette "I guess we're done here."
    scene 47_s2 with dissolve
    mc "How did I do?"
    if mc_date_annette_points == 6:
        scene 47_s3 with dissolve
        annette "You're... really sweet, [mc]."
        annette "You listened... you didn't laugh at my condition... You even made me feel a little brave."
        annette "I'm really happy it's you. I mean that."
        scene 47_s2 with dissolve
        mc "I'm glad."
    elif mc_date_annette_points >= 3:
        scene 47_s3 with dissolve
        annette "I was a little nervous... but I feel okay now."
        annette "You didn't say all the right things, but... you didn't scare me off either."
        annette "That's already more than I hoped for."
        scene 47_s2 with dissolve
        mc "Glad I passed... sorta."
    elif mc_date_annette_points < 3:
        scene 47_s3 with dissolve
        annette "Even if you teased me a little..."
        annette "I still want it to be you."
        annette "Maybe I'm silly... but I trust you."
        scene 47_s2 with dissolve
        mc "You're not silly. Not at all."

    if mc_knows_cabin:
        mc "Wait for you at the cabin then?"
        scene 47_s3 with dissolve
        annette "*nod* Yes..."
        scene 47_s2 with dissolve
        stop music fadeout 2.0 
        mc "Alright."
    else:
        $ mc_knows_cabin = True
        mc "What now?"
        scene 47_s3 with dissolve
        annette "See that cabin over there?"
        scene 47_s2 with dissolve
        mc "That one? I always wondered why it's tucked away like that."
        scene 47_s3 with dissolve
        annette "It's for after the festival... you know, when people choose to..."
        scene 47_s2 with dissolve
        stop music fadeout 2.0 
        mc "Got it. I'll wait for you."
    jump scene45

label scene47_annette_sex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p5_replay:
        $ persistent.scene1_p5_replay = True
    $ mc_date_annette_final = True
    stop music fadeout 2.0 
    scene 47_s10 with Fade(1.0,1.0,1.0)
    annette "H-Hello, [mc]..."
    annette "Sorry if I'm acting weird, it's just... this is the first time someone's seen me like this."
    if mc_likes_annette_smell:
        annette "I kept my musk as you asked. I hope you like it."
        scene 47_s11 with dissolve
        mc "*sniff* I can tell. I love it."
        jump scene47_choice06_op1
    else:
        annette "I went ahead and washed myself for you."
        scene 47_s11 with dissolve
        call screen scene47_choice06 with dissolve

label scene47_choice06_op1:
    mc "You look beatiful."
    scene 47_s10 with dissolve
    annette "Hahaha~ T-Thank you..."
    annette "Mother Ysella told me to make sure your penis is erect before you enter me."
    scene 47_s11 with dissolve
    mc "And how are you going to do that?"
    scene 47_s10 with dissolve
    annette "She said... to use my mouth first. So I... practiced with a cucumber."
    scene 47_s11 with dissolve
    mc "I appreciate you doing that for me. But first, why don't you lay down on the bed?"
    scene 47_s10 with dissolve
    annette "Why? Wouldn't it be easier if—"
    scene 47_s11 with dissolve
    mc "Trust me. I have to do this first."
    scene 47_s10 with dissolve
    annette "Alright."
    scene 47_s11 with dissolve
    jump scene47_annette_sex2_0

label scene47_choice06_op2:
    mc "You could've at least cleaned up a bit more first."
    scene 47_s12 with dissolve
    annette "R-Right... Sorry. I didn't want to keep you waiting..."
    annette "Mother Ysella told me to make sure your penis is erect before you enter me."
    scene 47_s13 with dissolve
    mc "And how are you going to do that?"
    scene 47_s12 with dissolve
    annette "She said... to use my mouth first. So I... practiced with a cucumber."
    scene 47_s13 with dissolve
    mc "Good, I love you dedication. But first, why don't you lay down on the bed?"
    scene 47_s12 with dissolve
    annette "Why? Wouldn't it be easier if—"
    scene 47_s13 with dissolve
    mc "Trust me. I have to do this first."
    scene 47_s12 with dissolve
    annette "Alright."
    scene 47_s13 with dissolve
    jump scene47_annette_sex2_0

label scene47_annette_sex2_0:
    scene 47_s48 with Fade(1.0,1.0,1.0)
    annette "..."
    mc "What's wrong? Why are you covering yourself up?"
    scene 47_s49 with dissolve  
    annette "I-I'm sorry... I just got really nervous."  
    scene 47_s48 with dissolve
    mc "Are you uncomfortable? We can stop if you want."  
    scene 47_s49 with dissolve
    annette "No! Please don't stop... I'm fine... just a little scared."  
    scene 47_s48 with dissolve
    mc "It's your first time, it's natural to feel that way."  
    mc "Don't worry. I won't just... you know. I'll prepare you first. Is that alright?"  
    scene 47_s49 with dissolve
    annette "Y-Yes... that would be better. Thank you, [mc]."  
    scene 47_s48 with dissolve
    mc "Of course. We'll go slow." 
    annette "..."  
    mc "Will you...?"  
    scene 47_s49 with dissolve
    annette "Ah... r-right."  
    scene 47_s50 with Dissolve(1.0)
    annette "..."
    scene 47_s51 with Dissolve(1.5)
    annette "Ahh! [mc], y-you're licking me there..."  
    scene 47_s55 with dissolve
    mc "Mhm. It might hurt if I don't."  
    scene 47_s51 with dissolve
    annette "You're so gentle... thank you for doing this in such a... dirty place."  
    scene 47_s55 with dissolve
    mc "Dirty? Nonsense. I love your taste, your scent. You're beautiful down here."  
    scene 47_s51 with dissolve
    annette "*giggle* It makes me feel better when you say that."  
    scene 47_s55 with dissolve
    scene 47_s52 with Dissolve(1.2)
    perception "Your tongue teases her folds first, gentle licks easing her open."  
    annette "Mmmfhh~ Ahhnn~ it tickles... but feels so good..."  
    perception "Her hips shift without her realizing, chasing your tongue."  
    scene 47_s53 with Dissolve(1.0)
    play sound "se_sfx/blowjob/facial2.mp3" 
    mc "*lick* This is your clit. It's your most sensitive place."  
    perception "Her body jolts with each flick of your tongue against the little bud."  
    annette "Ahhhnnn~! Oh goddess... I-I can't hold still..."  
    scene 47_s54 with Dissolve(1.0)
    mc "Look at you. Your juices are already flowing for me."  
    annette "*gasps* Oh my... I didn't know it would be like this..."  
    scene 47_s56 with Dissolve(1.0)
    play sound "se_sfx/blowjob/facial3.mp3" 
    annette "Ahhh~ mmmhh~ Hhnnn~!"  
    annette "Y-You can stop now, [mc]... a-anymore and... I might... I might pee on you..."  
    mc "*laughs* That just means you're close. You're doing perfectly fine, Annette."
    annette "Thank you~ L-Let me return the favor now. Ahnn~!"
    jump scene47_annette_sex2

image ann_bj1 = Movie(play="images/3_chapter2/scene47/ann_bj1.webm", loop=True)
image ann_bj1_faster = Movie(play="images/3_chapter2/scene47/ann_bj1_faster.webm", loop=True)
image ann_bj2 = Movie(play="images/3_chapter2/scene47/ann_bj2.webm", loop=True)
image ann_bj2_faster = Movie(play="images/3_chapter2/scene47/ann_bj2_faster.webm", loop=True)

image ann_sex = Movie(play="images/3_chapter2/scene47/ann_sex.webm", loop=True)
image ann_sex_faster = Movie(play="images/3_chapter2/scene47/ann_sex_faster.webm", loop=True)
image ann_sex2 = Movie(play="images/3_chapter2/scene47/ann_sex2.webm", loop=True)
image ann_sex2_faster = Movie(play="images/3_chapter2/scene47/ann_sex2_faster.webm", loop=True)
image ann_sex3 = Movie(play="images/3_chapter2/scene47/ann_sex3.webm", loop=True)
image ann_sex3_faster = Movie(play="images/3_chapter2/scene47/ann_sex3_faster.webm", loop=True)

image ann_fj = Movie(play="images/3_chapter2/scene47/ann_fj.webm", loop=True)
image ann_fj_faster = Movie(play="images/3_chapter2/scene47/ann_fj_faster.webm", loop=True)

label scene47_annette_sex2:
    scene 47_s14 with Fade(1.5,1.0,1.0)
    annette "Can you see... the inside of my mouth?"
    mc "Yeah. I can see it."
    annette "Then... please place it inside."
    scene 47_s15 with fade
    play sound "se_sfx/blowjob/blowjob1.mp3" 
    sensation "Her lips wrap around you, tight and careful. Her tongue swirls nervously across the tip, awkward at first—but undeniably eager."
    annette "Mhmm..."
    show ann_bj1 with dissolve
    perception "She takes more of you slowly, inch by inch. Her cheeks hollow as she sucks, her eyes flicking up to watch your reaction."
    annette "*gag* Nhngg..."
    sensation "The heat of her mouth pulls you in. Her jaw trembles as she goes deeper... and deeper..."
    mc "Are you sure you can do this?"
    annette "Yesh... *gag*"
    perception "Tears gather at the corners of her eyes, but she doesn't stop. Saliva drips from her chin, pooling between her bare knees."
    sensation "Her throat flutters around the tip as she tries to breathe through her nose. The messy, wet rhythm makes your knees tighten."
    annette "Mmmph... Hnn..."
    $ scene47_bj1 = True
    call screen scene47_sex2 with dissolve

label scene47_bj1:
    $ scene47_bj1 = True
    $ scene47_bj2 = False
    $ scene47_bj_speed = False
    scene black with Dissolve(0.3)
    show ann_bj1 with dissolve
    annette "*slurp* *lick* Ah love licking it..."
    call screen scene47_sex2 with dissolve

label scene47_bj2:
    $ scene47_bj1 = False
    $ scene47_bj2 = True
    $ scene47_bj_speed = False
    scene black with Dissolve(0.3)
    show ann_bj2 with dissolve
    annette "Mhnnmm..."
    call screen scene47_sex2 with dissolve

label scene47_bj_faster:
    $ scene47_bj_speed = True
    if scene47_bj1:
        show ann_bj1_faster with dissolve
        hide ann_bj1
        annette "*gag* Nghhh!"
    else:
        show ann_bj2_faster with dissolve
        hide ann_bj2
        annette "Oghhnnnn! *suck* *gag*"
    call screen scene47_sex2 with dissolve

label scene47_bj_slower:
    $ scene47_bj_speed = False
    if scene47_bj1:
        show ann_bj1 with dissolve
        hide ann_bj1_faster
        annette "Mnnnn~ Cah you fee mah tongue?"
    else:
        show ann_bj2 with dissolve
        hide ann_bj2_faster
        annette "*slurp* Nhnnnn..."
    call screen scene47_sex2 with dissolve

label scene47_bj_cum:
    mc "I'm cumming!"
    call screen scene47_bj_cum with dissolve

default scene47_cum_loca = 0
label scene47_bj_cum_inside:
    annette "Mmmmm!!"
    play sound "se_sfx/blowjob/gag1.mp3" 
    show screen cum
    scene 47_s16 with vpunch
    sensation "You release into her mouth. Her eyes flutter closed as she holds still, swallowing instinctively. Some of it spills from the corner of her lips—hot and white across her chin."
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 47_s17 with vpunch
    mc "Take it all!"
    hide screen cum
    scene 47_s18 with Dissolve(1.0)
    mc "Swallow it."
    scene 47_s19 with dissolve
    play sound "se_sfx/blowjob/swallow2.mp3" 
    annette "*gag* *gulp* *gulp*"
    mc "Show me."
    scene 47_s20 with dissolve
    annette "Ahhhh..."
    scene 47_s21 with dissolve
    annette "D-Did I do well...?"
    scene 47_s22 with dissolve
    mc "More than well."
    scene 47_s21 with dissolve
    annette "Is your penis... erect now?"
    scene 47_s22 with dissolve
    mc "It was the moment I tasted you."
    scene 47_s21 with dissolve
    annette "O-Oh... Haha~"
    annette "Then... would you like to start breeding me?"
    scene 47_s22 with dissolve
    call screen scene47_choice07 with dissolve

label scene47_bj_cum_outside:
    $ scene47_cum_loca += 1
    annette "W-Where?"
    mc "On your face. Hold still."
    play sound "se_sfx/blowjob/facial3.mp3" 
    show screen cum
    scene 47_s23 with vpunch
    sensation "You erupt with a grunt, warm spurts landing across her cheeks, her lips, and her eye. She flinches and closes her eyes as the heat splashes against her skin."
    scene 47_s24 with dissolve
    annette "It's... warmer than I thought."
    hide screen cum
    annette "Is your penis... erect now?"
    scene 47_s25 with dissolve
    mc "It was the moment I tasted you."
    scene 47_s24 with dissolve
    annette "O-Oh... Haha~"
    annette "Then... would you like to start breeding me?"
    scene 47_s25 with dissolve
    call screen scene47_choice07 with dissolve
    
label scene47_choice07_op1:
    mc "Actually... I'd like a footjob first."
    if scene47_cum_loca == 1:
        scene 47_s26 with dissolve
        annette "A footjob?"
        scene 47_s25 with dissolve
        mc "It's when you use your feet to pleasure me."
        scene 47_s26 with dissolve
        annette "Is... is that really a thing?"
        scene 47_s25 with dissolve
        mc "Mhm. And I'd love for you to try it."
        scene 47_s24 with dissolve
        annette "O-Okay... I'd love to learn from you."
        scene 47_s25 with dissolve
    else:
        scene 47_s27 with dissolve
        annette "A footjob?"
        scene 47_s22 with dissolve
        mc "It's when you use your feet to pleasure me."
        scene 47_s27 with dissolve
        annette "Is... is that really a thing?"
        scene 47_s22 with dissolve
        mc "Mhm. And I'd love for you to try it."
        scene 47_s27 with dissolve
        annette "O-Okay... I'd love to learn from you."
        scene 47_s22 with dissolve
    scene 47_s30 with Fade(0.5,0.5,1.0)         
    perception "Annette sits on the edge of the bed, her bare legs pressed together, watching you with curiosity as you step closer."
    mc "Just squeeze gently... and move."
    show ann_fj with dissolve
    annette "Like this...?"
    mc "Just like that. You're doing great."
    perception "Her feet glide up and down your shaft with an awkward rhythm, but the innocence in her movements only makes it harder to hold back. Her toes curl around the head, smearing precum along the top."
    annette "You're so hard... It's twitching against me."
    show ann_fj_faster with dissolve
    sensation "As she builds confidence, her feet move faster, squeezing a little tighter. The contrast between the soft skin and her timid breathing only drives you closer."
    annette "You look so intense... Is it okay if I keep going?"
    call screen scene47_fj with dissolve
    mc "Annette... I'm gonna—"
    annette "*gasp* W-Wait—do you want to finish like this, or... inside me?"
    call screen scene47_choice08 with dissolve

label scene47_choice08_op1:
    play sound "se_sfx/blowjob/facial3.mp3" 
    show screen cum
    scene 47_s28 with vpunch
    sensation "With one final glide between her arches, your cock pulses violently. Thick spurts of cum splash across her ankles and toes."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 47_s29 with vpunch
    annette "Oh!"
    hide screen cum
    scene 47_s31 with dissolve
    annette "O-Oh my... that was so much..."
    annette "I-Is this part of the custom too?"
    scene 47_s32 with dissolve
    mc "It is now."
    mc "Get on the bed. Now I want to fuck you."
    scene 47_s31 with dissolve
    annette "Yes~!"
    scene 47_s32 with dissolve
    jump scene47_annette_sex3

label scene47_choice07_op2:
    mc "Get on the bed."
    if scene47_cum_loca == 1:
        scene 47_s24 with dissolve
        annette "Yes~!"
    else:
        scene 47_s27 with dissolve
        annette "Yes~!"
    jump scene47_annette_sex3

label scene47_choice08_op2:
    mc "Get on the bed! I'll finish inside you!"
    annette "Yes~!"
    jump scene47_annette_sex3

label scene47_annette_sex3:
    scene black with Fade(0.5,0.5,0.5)
    perception "Annette turns around shyly, lowering herself onto the bed with her knees apart, her back arched, her pale skin glowing in the candlelight."
    scene 47_s33 with fade
    annette "Just a reminder... please don't go too far in, alright?"
    mc "I understand. I'll be gentle."
    show ann_sex with dissolve
    annette "Ahh~ H-Hahh..."
    perception "Her fingers clutch the sheets, face turned to the side, hair falling over her eyes as you push in deeper."
    annette "I-It feels strange... but good..."
    sensation "Her walls squeeze around you, pulsing like they're trying to keep you inside. The rhythm is slow at first—gentle—each thrust making her moan louder."
    $ is_annette_anim_vsex1 = True
    call screen is_annette_sex_sex1 with dissolve

label is_annette_sex1:
    $ is_annette_anim_vsex1 = True
    $ is_annette_anim_vsex2 = False
    $ is_annette_anim_asex = False
    scene black with Dissolve(0.3)
    show ann_sex with dissolve
    annette "Hahhh! Ahh~ Hnnn~!"
    call screen is_annette_sex_sex1 with dissolve

label is_annette_sex2:
    $ is_annette_anim_vsex1 = False
    $ is_annette_anim_vsex2 = True
    $ is_annette_anim_asex = False
    scene black with Dissolve(0.3)
    show ann_sex2 with dissolve
    annette "Hnn~ Mmmm~ It feels so good!"
    call screen is_annette_sex_sex1 with dissolve

default is_annette_asex_first = True
label is_annette_asex:
    $ annette_sex_pos_toggle = True
    $ is_annette_anim_vsex1 = False
    $ is_annette_anim_vsex2 = False
    $ is_annette_anim_asex = True
    if is_annette_asex_first:
        $ is_annette_asex_first = False
        if mc_hugged_annette:
            mc "Hahh... You ever heard of anal sex, Annette?"
            annette "Ahh~ Hah~ W-What's that?"
            mc "I want to fuck you in the ass."
            annette "I-I... But that's where I..."
            mc "Yeah, I know. I just want to try it with you."
            annette "W-Will it hurt?"
            mc "Not if I lube you up first."
            annette "Alright... I'll let you take me in the butt..."
            scene black with Fade(0.5,0.5,0.5)
            perception "You guide your hand down between her legs, gathering her nectar with your fingers. Her body trembles as you press some of it against her puckered entrance."
            scene 47_s42 with fade
            sensation "She flinches as your tip presses against her ass—tight, resistant, trembling."
            show ann_sex3 with dissolve
            annette "H-Hnnn!! It's so strange!"
            sensation "Her back arches sharply as you push into her inch by inch. Her ass clenches around you like a vice, the pressure dizzying."
            annette "I-I'm really sorry if you didn't feel pleasure before... when you used my womb..."
            mc "It's fine. Really. I just wanted to feel your ass."
            annette "Mmmm~ I-I'll try to make it feel good for you..."
            perception "Her face is flushed red, tears welling slightly as she takes you deeper, her body adjusting with every slow thrust."
            sensation "You pick up the pace. The heat of her ass tightens with every inch, gripping you like she was made for it."
        else:
            mc "I want to fuck you in the ass, Annette!"
            annette "Ahh~ Hah~ Fine... Just please be gentle. I tried my best to stretch it out when you told me..."
            mc "I'll lube you up with your pussy juice."
            scene black with Fade(0.5,0.5,0.5)
            perception "You guide your hand down between her legs, gathering her nectar with your fingers. Her body trembles as you press some of it against her puckered entrance."
            scene 47_s42 with fade
            sensation "She flinches as your tip presses against her ass—tight, resistant, trembling."
            show ann_sex3 with dissolve
            annette "H-Hnnn!! It's so strange!"
            sensation "Her back arches sharply as you push into her inch by inch. Her ass clenches around you like a vice, the pressure dizzying."
            annette "I-I'm really sorry if you didn't feel pleasure before... when you used my womb..."
            mc "It's fine. Really. I just wanted to feel your ass."
            annette "Mmmm~ I-I'll try to make it feel good for you..."
            perception "Her face is flushed red, tears welling slightly as she takes you deeper, her body adjusting with every slow thrust."
            sensation "You pick up the pace. The heat of her ass tightens with every inch, gripping you like she was made for it."
    else:
        scene black with Dissolve(0.3)
        show ann_sex3 with dissolve
        annette "Ah! Goddess... I can feel it all the way inside me!"
        annette "Ahh! Hah~"
    call screen is_annette_sex_sex1 with dissolve

label is_annette_sex_faster:
    if is_annette_anim_vsex1:
        show ann_sex_faster with dissolve
        hide ann_sex
        annette "Ah! [mc]! Please be careful..."
    elif is_annette_anim_vsex2:
        show ann_sex2_faster with dissolve
        hide ann_sex2
        annette "Nghnn~ My vagina won't stop dripping~"
    elif is_annette_anim_asex:
        show ann_sex3_faster with dissolve
        hide ann_sex3
        annette "[mc] please!! You told me you will be gentle!"
    call screen is_annette_sex_sex1 with dissolve

label is_annette_sex_cum:
    mc "Fuck! I'm gonna cum—"
    if is_annette_anim_asex:
        annette "Ahh~ I-Inside my butt...?"
        show screen cum
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene 47_s36 with vpunch
        sensation "You thrust deep and release inside her ass, heat flooding her insides. She gasps as her body twitches beneath you."
        play sound "se_sfx/sex/sex_cum2.mp3"
        scene 47_s37 with vpunch
        annette "Hnnngghh!!"
        scene 47_s38 with Dissolve(1.0)
        annette "Oww.. [mc]... You weren't gentle with me..."
        mc "Oh... Sorry, Annette. I thought I lubed you good enough."
        annette "N-No, it's fine. *giggles* I can't feel my butt anymore. It's so sore from your big penis."
        mc "*chuckles* You did good on taking me."
        perception "She tries her best to clench her gaping anus but to no avail."
        annette "Nghn! Ouch... and also..."
        annette "You didn't finish in my womb."
        mc "One more... I'll finish in your womb now."
        annette "Y-Yes... Please fill me..."
        show ann_sex with fade
        perception "You slide back into her soaked folds, now dripping even more from arousal and your earlier release."
        sensation "Her pussy welcomes you back with eager pulses, tighter now from all the stimulation."
        annette "I-It's too much... I-I'm gonna—"
        mc "Me too!"
        play sound "se_sfx/sex/sex_cum2.mp3"
        show screen cum
        if persistent.xray_mode:
            scene 47_s33_xray1 with vpunch
            sensation "You bury yourself as deep as her tiny passage allows and explode inside her, hips jerking as you fill her womb with heat."
            play sound "se_sfx/sex/sex_cum1.mp3"
            annette "[mc]! [mc]! [mc]!"
            scene 47_s34_xray2 with vpunch
            perception "Annette's body shakes uncontrollably. Her face buries into the sheets, mouth open, moaning your name as her orgasm hits."
            scene 47_s35_xray3 with Dissolve(1.0)
        else:
            scene 47_s33 with vpunch
            sensation "You bury yourself as deep as her tiny passage allows and explode inside her, hips jerking as you fill her womb with heat."
            play sound "se_sfx/sex/sex_cum1.mp3"
            annette "[mc]! [mc]! [mc]!"
            scene 47_s34 with vpunch
            perception "Annette's body shakes uncontrollably. Her face buries into the sheets, mouth open, moaning your name as her orgasm hits."
            scene 47_s35 with Dissolve(1.0)
    else:
        annette "Please fill me!"
        perception "You slide back and forth into her soaked folds, now dripping and spasming around your cock with anticipation."
        annette "I-It's too much... I-I'm gonna—"
        mc "Me too!"
        play sound "se_sfx/sex/sex_cum1.mp3"
        if persistent.xray_mode:
            scene 47_s33_xray1 with vpunch
            sensation "You bury yourself as deep as her tiny passage allows and explode inside her, hips jerking as you fill her womb with heat."
            annette "[mc]! [mc]! [mc]!"
            play sound "se_sfx/sex/sex_cum2.mp3"
            scene 47_s34_xray2 with vpunch
            perception "Annette's body shakes uncontrollably. Her face buries into the sheets, mouth open, moaning your name as her orgasm hits."
            scene 47_s35_xray3 with Dissolve(1.0)
        else:
            scene 47_s33 with vpunch
            sensation "You bury yourself as deep as her tiny passage allows and explode inside her, hips jerking as you fill her womb with heat."
            annette "[mc]! [mc]! [mc]!"
            play sound "se_sfx/sex/sex_cum2.mp3"
            scene 47_s34 with vpunch
            perception "Annette's body shakes uncontrollably. Her face buries into the sheets, mouth open, moaning your name as her orgasm hits."
            scene 47_s35 with Dissolve(1.0)
    annette "*gasp* D-Do you think... I'll really get pregnant?"
    mc "Hahh... hah... I hope so. You were so tight."
    perception "The room is dim and quiet now—only your breathing and hers remain. The sweat on her back glistens faintly in the soft candlelight."
    scene 47_s39 with Fade(1.0,1.0,1.0)
    annette "That was... a lot..."
    hide screen cum
    annette "I'm glad it was you..."
    scene 47_s40 with dissolve
    mc "You mean that?"
    scene 47_s39 with dissolve
    annette "Mhm... It didn't feel scary. Just... full."
    scene 47_s40 with dissolve
    mc "..."
    annette "..."
    scene 47_s39 with dissolve
    annette "Please don't leave me..."
    scene 47_s40 with dissolve
    mc "I'm here."
    $ mc_date_annette_win_fin = True
    scene black with Fade(2.0,1.0,1.0)
    empathy "Annette sleeps peacefully at your side, a soft smile on her lips... her body filled, her purpose fulfilled. If only for tonight."
    $ renpy.end_replay()
    jump scene45


label scene48_sigrun:
    if mc_let_aldwin_win:
        mc "(Wait, didn't I let him win? I should hold my end of the deal.)"
        call screen scene46_choice01 with dissolve
    else:
        $ mc_date_sigrun = True
        stop music fadeout 2.0 
        scene 48_s1 with Fade(1.0,1.0,1.0)
        play music "date1.mp3" fadein 3.0 volume 0.5 loop
        ""
        scene 48_s2 with fade
        mc "Hey."
        scene 48_s3 with dissolve
        sigrun "[mc]... I was wondering if you'd show up."
        scene 48_s2 with dissolve
        mc "Were you waiting for me?"
        scene 48_s3 with dissolve
        sigrun "Yes. Mother Ysella asked us to speak... to see if we understand each other before anything happens."
        scene 48_s2 with dissolve
        mc "Alright."
        scene 48_s3 with dissolve
        sigrun "I've had my share of years... I won't give myself to someone who doesn't take this seriously."
        scene 48_s2 with dissolve
        mc "Understood."
        scene 48_s3 with dissolve
        sigrun "Let me ask you something... Why did you even agree to join this festival?"
        scene 48_s2 with dissolve
        call screen scene48_choice01 with dissolve

label scene48_choice01_op1:
    mc "Well, it sounded like a good chance to get lucky. You know?"
    scene 48_s6 with dissolve
    sigrun "If that's all you're here for, we can stop now."
    scene 48_s7 with dissolve
    mc "..."
    scene 48_s6 with dissolve
    sigrun "So? Should we finish this now?"
    scene 48_s7 with dissolve
    mc "No. Let's keep going."
    scene 48_s2 with dissolve
    sigrun "..."
    jump scene48_sigrun2

label scene48_choice01_op2:
    $ mc_date_sigrun_points += 2
    mc "Because I wanted to help this village. I may be an outsider, but I felt like I could do some good by participating in the festival."
    scene 48_s5 with dissolve
    sigrun "A selfless reason. You don't hear that often anymore. I hope you truly mean it."
    jump scene48_sigrun2

label scene48_choice01_op3:
    $ mc_date_sigrun_points += 1
    mc "Honestly? I just went with the flow. I didn't expect things to get this serious."
    scene 48_s3 with dissolve
    sigrun "At least you're honest. Intentions can change with time."
    jump scene48_sigrun2

label scene48_sigrun2:
    scene 48_s3 with dissolve
    sigrun "*sigh* When I was younger, the festival was treated like a sacred rite. It wasn't just about repopulating... it was about honoring the bond between two people. Something deeper."
    scene 48_s2 with dissolve
    mc "Do you still feel that way?"
    scene 48_s3 with dissolve
    sigrun "Some days, yes. Other days... it feels more like a ritual we're all expected to perform, even if our hearts aren't in it."
    scene 48_s2 with dissolve
    mc "You sound... tired of it."
    scene 48_s3 with dissolve
    sigrun "Not tired. Just older. I've seen the festival change faces more than once. But I guess I still hope for something real in it—something meaningful."
    scene 48_s2 with dissolve
    mc "Even now?"
    scene 48_s3 with dissolve
    sigrun "Maybe especially now."
    sigrun "Second question... What does a woman's past mean to you?"
    sigrun "Be honest."
    scene 48_s2 with dissolve
    call screen scene48_choice02 with dissolve

label scene48_choice02_op1:
    $ mc_date_sigrun_points += 2
    mc "It's part of who she is. I'd never ask her to forget it, or hide it."
    scene 48_s5 with dissolve
    sigrun "That's a rare kind of answer. Thank you."
    jump scene48_sigrun3

label scene48_choice02_op2:
    mc "As long as she wasn't out whoring around, I don't care."
    scene 48_s6 with dissolve
    sigrun "I understand what you're tying to say, but that's a terrible way to see things."
    sigrun "The past should stay in the past."
    scene 48_s7 with dissolve
    mc "*shrug*"
    jump scene48_sigrun3

label scene48_choice02_op3:
    $ mc_date_sigrun_points += 1
    mc "I guess it depends on the past. Some things are easier to accept than others."
    scene 48_s3 with dissolve
    sigrun "That's reasonable I suppose."
    jump scene48_sigrun3

label scene48_sigrun3:
    scene 48_s8 with dissolve
    sigrun "I've lived longer than most of the women still left here. Time does that—it gifts you stories... and mistakes."
    mc "You've made choices you regret?"
    sigrun "Of course. Some nights I lie awake, wondering if I could have been someone better. But I've also loved deeply. Held someone who looked at me like I was the only light in a dark world."
    mc "Aldwin?"
    scene 48_s5 with dissolve
    sigrun "Always. He was never perfect. But he was mine. And I was his."
    scene 48_s4 with dissolve
    mc "You miss those days."
    scene 48_s5 with dissolve
    sigrun "Every day."
    scene 48_s3 with dissolve
    sigrun "Final question."
    sigrun "What do you expect... from a woman you lie with?"
    scene 48_s2 with dissolve
    call screen scene48_choice03 with dissolve

label scene48_choice03_op1:
    $ mc_date_sigrun_points += 1
    mc "Warmth. Connection. Even if it's brief. That's enough."
    scene 48_s5 with dissolve
    sigrun "Not many are brave enough to say that."
    jump scene48_sigrun4

label scene48_choice03_op2:
    $ mc_date_sigrun_points += 2
    mc "Honesty. If we share something that intimate, I want it to be real."
    scene 48_s5 with dissolve
    sigrun "A rare thing... but a powerful one."
    jump scene48_sigrun4

label scene48_choice03_op3:
    mc "A good time. That's all I really expect."
    scene 48_s6 with dissolve
    sigrun "Then I think you'll find that's all you'll get."
    jump scene48_sigrun4

label scene48_sigrun4:
    scene 48_s3 with dissolve
    sigrun "You can tell a lot about someone by how they answer that question."
    scene 48_s2 with dissolve
    mc "Yeah?"
    scene 48_s3 with dissolve
    sigrun "Yes. Some want control. Others want escape. But once in a while, someone just wants to be seen... even if it's only for a night."
    scene 48_s2 with dissolve
    mc "And what about you? What do you want?"
    scene 48_s3 with dissolve
    sigrun "To feel... desired. Not because of duty. Not because it's expected. Just because someone chose me. Me—without the years, the titles, the scars."
    scene 48_s2 with dissolve
    mc "You're easy to choose, Sigrun."
    scene 48_s3 with dissolve
    sigrun "That's kind of you to say. But I think I needed to hear it more than I thought."
    scene 48_s2 with dissolve
    mc "So... how did I do?"
    if mc_date_sigrun_points == 6:
        $ mc_date_sigrun_win = True
        scene 48_s5 with dissolve
        sigrun "You're a rare one, [mc]."
        sigrun "I thought I was past the age where this kind of connection mattered... but you proved me wrong."
        sigrun "If I give myself to you... I know it will be with no regrets."
        scene 48_s4 with dissolve
        mc "I'll make sure of it."
        scene 48_s5 with dissolve
        sigrun "Then I'll wait for you in the cabin outside the village fence."
        stop music fadeout 2.0 
        scene 48_s4 with dissolve
    elif mc_date_sigrun_points >= 3:
        $ mc_date_sigrun_win = True
        scene 48_s5 with dissolve
        sigrun "I don't know if we're a perfect match, but... you listened."
        sigrun "You gave me honesty. That counts for something."
        sigrun "If you're still willing... I'd accept your company tonight."
        scene 48_s4 with dissolve
        mc "I am."
        scene 48_s5 with dissolve
        sigrun "Then I'll wait for you in the cabin outside the village fence."
        stop music fadeout 2.0 
        scene 48_s4 with dissolve
    elif mc_date_sigrun_points < 3:
        $ mc_date_sigrun_final = True
        scene 48_s3 with dissolve
        sigrun "*sigh* You speak as expected from someone your age, but... there's something missing."
        sigrun "This isn't just about seed or ritual for me, [mc]. I need something... deeper."
        scene 48_s2 with dissolve
        mc "We can still work something out."
        scene 48_s3 with dissolve
        sigrun "No, I don't think we can. I hope you find someone who fits what you're looking for."
        scene 48_s2 with dissolve
        scene black with Fade(0.5,0.5,0.5)
        stop music fadeout 2.0 
        empathy "She doesn't turn away harshly—just quietly, gracefully. Like she's already let go."
    jump scene45

label scene48_sigrun_sex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p5_replay:
        $ persistent.scene2_p5_replay = True
    stop music fadeout 2.0 
    scene 48_s9 with Fade(1.0,1.0,1.0)
    perception "You step inside and catch the soft sound of shifting cloth. Sigrun stands near the bed, halfway through undressing—her dress sliding off her shoulders, revealing bare skin beneath."
    scene 48_s10 with dissolve
    sigrun "Oh, [mc]. I apologize... looks like you caught me early."
    mc "No worries. Take your time."
    sigrun "Could you... turn away for a moment?"
    mc "Huh?"
    sigrun "Ah... I forgot why I'm even here. Silly me."
    scene 48_s11 with Fade(0.5,0.5,0.5)
    mc "Are you ready?"
    scene 48_s12 with dissolve
    sigrun "Yes. I even went through the trouble of shaving down there, so you'd better make it worth it."
    scene 48_s11 with dissolve
    mc "You shaved your pubes?"
    sigrun "Mhm."
    call screen scene48_choice04 with dissolve

label scene48_choice04_op1:
    scene 48_s11 with vpunch
    mc "You really shouldn't have!"
    scene 48_s12 with dissolve
    sigrun "Oh my... such a strong reaction. Why does it bother you so much?"
    scene 48_s13 with dissolve
    mc "I just think it's natural. You didn't need to change anything for me."
    sigrun "Well... I... Sorry? I thought you'd prefer it that way."
    mc "*sigh* You should've asked me before you did it."
    jump scene48_sigrun_sex2

label scene48_choice04_op2:
    mc "Good. I like it better this way."
    scene 48_s13 with dissolve
    sigrun "That's what Aldwin always used to say. He'd refuse to touch me if I had even a hint of a bush."
    mc "Alright, I'm not that extreme..."
    jump scene48_sigrun_sex2

label scene48_sigrun_sex2:
    sigrun "What do you want to do?"
    call screen scene48_choice05 with dissolve

label scene48_choice05_op1:
    mc "Let's get straight to it."
    sigrun "Alright, it will be a bit dry at first but don't worry. Just keep going."
    jump scene48_sigrun_sex3_0

image sig_tj = Movie(play="images/3_chapter2/scene48/sigrun_tj.webm", loop=True)
image sig_tj_faster = Movie(play="images/3_chapter2/scene48/sigrun_tj_faster.webm", loop=True)

image sig_sex1 = Movie(play="images/3_chapter2/scene48/sigrun_sex1.webm", loop=True)
image sig_sex1_faster = Movie(play="images/3_chapter2/scene48/sigrun_sex1_faster.webm", loop=True)

image sig_sex2 = Movie(play="images/3_chapter2/scene48/sigrun_sex2.webm", loop=True)
image sig_sex2_faster = Movie(play="images/3_chapter2/scene48/sigrun_sex2_faster.webm", loop=True)

label scene48_choice05_op2:
    mc "Actually... I'd love to feel your breasts first. They're.. really beautiful."
    scene 48_s12 with dissolve
    sigrun "I... I understand."
    scene 48_s11 with dissolve
    scene 48_s14 with Fade(0.5,0.5,0.5)
    sigrun "You know... ever since I came of age, the men in the village couldn't help staring at my chest."
    scene 48_s15 with dissolve
    mc "All of them?"
    scene 48_s14 with dissolve
    sigrun "*chuckles* Yes. Even my dear husband, back when we were just courting."
    sigrun "He used to say he couldn't help it. Always had an excuse to walk past the smithy twice when I was washing clothes."
    scene 48_s15 with dissolve
    mc "Can't blame him, honestly."
    scene 48_s14 with dissolve
    sigrun "Oh, hush. Just relax and enjoy." 
    show sig_tj with dissolve
    sensation "She pushes your shaft between her breasts—warm, soft, pillowy. Her skin slides against you with slow, controlled motions."
    sigrun "It's been... a long time since I did something like this."
    mc "You still know how."
    perception "Her nipples brush the sides of your shaft occasionally—hard, pebbled from the air or maybe... the moment."
    sigrun "Hmm... You're not planning to ejaculate on my breasts are you?"
    mc "Maybe I am."
    sigrun "Oh, dear... Will you be making a big mess?"
    mc "Mhmm..."
    sigrun "Will you cover them with your seed~? Maybe on my face too?"
    sigrun "You want to see me drenched and dripping with it?"
    mc "Fuck..."
    sigrun "Don't hold back, big boy~"
    call screen scene48_tj with dissolve

label scene48_tj_cum:
    mc "I'm close..."
    sigrun "Then give it to me... right here."
    play sound "se_sfx/blowjob/facial1.mp3" 
    show screen cum
    scene 48_s16 with vpunch
    sensation "With one final squeeze, your cock pulses. Thick white ropes shoot across her chest, painting her breasts and collar in warmth."
    sigrun "I know you still have more in there~!"
    play sound "se_sfx/blowjob/facial3.mp3" 
    scene 48_s17 with vpunch
    sigrun "Ahhh!"
    hide screen cum
    scene 48_s18 with Dissolve(1.0)
    sigrun "Just like that... Are you sure you can still go after this?"
    scene 48_s19 with dissolve
    mc "Oh, you bet."

label scene48_sigrun_sex3:
    scene 48_s18 with dissolve
    sigrun "So..."
    scene 48_s19 with dissolve
    mc "So?"
    sigrun "..."
    mc "I want to hear you say it."
    scene 48_s18 with dissolve
    sigrun "*sigh* Always the proud ones..."
    scene 48_s19 with dissolve
    mc "Seriously? That won't do. Come on."
    scene 48_s18 with dissolve
    sigrun "Please, [mc]... use me. Breed me. Make this old body feel wanted again."
    scene 48_s19 with dissolve
    mc "That's more like it."

label scene48_sigrun_sex3_0:
    scene black with Fade(0.5,0.5,0.5)
    perception "She lies back on the bed, legs spreading slowly, invitingly. Her hands glide down her sides and rest on her thighs. Her body is toned and curved—experienced, but no less beautiful."
    scene 48_s24 with dissolve
    sensation "You guide yourself between her thighs, pressing the head of your cock to her entrance. She's wet—more than you expected—and warm, almost feverish."
    sigrun "H-Hahh..."
    scene 48_s25 with dissolve
    play sound "se_sfx/sex/touch2.mp3" 
    mc "You're already soaked..."
    sigrun "Don't tease. Just go! I want you to be rough with me."
    show sig_sex1 with dissolve
    perception "You push inside her with one thrust. Her body stretches around you—tight and familiar with the act, yet still trembling slightly from anticipation."
    sigrun "Mmmn~ Y-You feel... so full..."
    sensation "Each push sinks you deeper into her warmth—slick, slow, deliberate. Her inner muscles tighten as if trying to hold you there forever."
    sigrun "Goddess... it's been too long..."
    sensation "Your pace builds—her moans growing louder, her thighs tightening around you. The sound of skin meeting skin echoes in the cabin."
    sigrun "D-Don't stop... Don't you dare stop—"
    sigrun "Mhnnn~ You're stretching me so wide!"
    $ scene48_sex1 = True
    call screen scene48_sex with dissolve

label scene48_sex1:
    $ scene48_sex_speed = False
    $ scene48_sex1 = True
    $ scene48_sex2 = False
    scene black with Dissolve(0.3)
    show sig_sex1 with dissolve
    sigrun "Hnnn~ I love it when you go deeper~ You're hitting my special spot~"
    call screen scene48_sex with dissolve

default scene48_sex2_first = True
label scene48_sex2:
    $ scene48_sex_speed = False
    $ scene48_sex1 = False
    $ scene48_sex2 = True
    if scene48_sex2_first:
        mc "(Should I ask her to show me her feet?)"
        call screen scene48_choice06 with dissolve
        $ scene48_sex2_first = False
        mc "Show me your feet."
        sigrun "Ahh~ H-Huh? My feet? W-Why?"
        mc "Just do it."
        scene black with Dissolve(0.3)
        show sig_sex2 with dissolve
        perception "She hesitates for a moment, then lifts one leg slowly, presenting her soles with a soft flush on her cheeks."
        sigrun "Here... Is this what you wanted?"
        mc "Yeah."
        sigrun "Does... looking at them really turn you on that much?"
        mc "More than you know."
        sigrun "I've heard of this... I think it's the pheromones, or... maybe the warmth... I-I don't know—"
        sensation "Her toes curl slightly as your arousal presses harder against her, throbbing with urgency."
        sigrun "*gasp* I-I can feel you getting bigger... Just from looking at my feet?!"
        mc "Guess I'm a little weirder than you thought."
        sigrun "No... I like it."
        sigrun "Come closer, let me shove them on your face~"
    else:
        scene black with Dissolve(0.3)
        show sig_sex2 with dissolve
        sigrun "Keep staring at my feet~"
        sigrun "I can feel your cock getting bigger."
        sigrun "Ahh~ Hnn~ Mphhmm~ Yes, baby! Keep fucking me~"
    call screen scene48_sex with dissolve

label scene48_sex_cum:
    $ mc_date_sigrun_final = True
    mc "I'm close..."
    sigrun "Inside! Fill me~! Don't waste a drop~"
    play sound "se_sfx/sex/sex_cum1.mp3" 
    show screen cum
    if persistent.xray_mode:
        scene 48_s20_xray1 with vpunch
        sensation "You thrust deep one last time. Your cock twitches violently inside her, spurting thick warmth into her womb. Her back arches, crying out softly as you flood her."
        sigrun "I can feel it inside me... So hot..."
    else:
        scene 48_s20 with vpunch
        sensation "You thrust deep one last time. Your cock twitches violently inside her, spurting thick warmth into her womb. Her back arches, crying out softly as you flood her."
        sigrun "I can feel it inside me... So hot..."
    scene 48_s21 with Fade(0.5,0.5,0.5)
    mc "You took it all..."
    hide screen cum
    scene 48_s22 with dissolve
    sigrun "Of course I did. You think I'd let any of it go to waste?"
    scene 48_s21 with dissolve
    perception "The room is quiet now. Only the sound of your shared breath fills the air. Sigrun lies beneath you, her chest rising and falling in steady waves."
    perception "Your seed slowly begins to trickle from between her legs. She makes no move to wipe it away."
    scene 48_s22 with dissolve
    sigrun "It's strange... how different I feel now."
    scene 48_s21 with dissolve
    mc "Regret?"
    scene 48_s22 with dissolve
    sigrun "Not quite. Just... reminded."
    scene 48_s21 with dissolve
    mc "Of what?"
    scene 48_s22 with dissolve
    sigrun "That I'm still a woman. Not just someone's wife. Or someone's memory."
    sigrun "Goddess, if Aldwin could see me now..."
    if persistent.xray_mode:
        scene 48_s23_xray2 with dissolve
    else:
        scene 48_s23 with dissolve
    mc "Would he be angry?"
    sigrun "No. He'd be furious. Then he'd sigh... and say he understood."
    mc "You think?"
    sigrun "He always knew I was the stronger one. He was just better at pretending otherwise."
    sigrun "Don't you dare think this makes you special though."
    mc "Oh?"
    sigrun "But seriously... Thank you. For making me feel wanted. For making me feel like me again."
    mc "You're welcome."
    sigrun "Goodbye, [mc]. I hope your seed proves potent. It's not easy for someone my age to conceive."
    mc "We'll just have to wait and see."
    sigrun "Mhmm..."
    scene 46_s46 with fade
    perception "She gathers her things and slips out quietly, leaving the door half-closed behind her. The room falls silent."
    $ renpy.end_replay()
    jump scene45

label scene49:
    scene black with fade
    mc "Finally done with all the girls..."
    scene 49_s1 with Fade(1.0,1.0,1.0)
    mc "Ugh! The sun..."
    scene 49_s2 with Fade(0.5,0.5,0.5)
    ada "It looks like you're done with all the women. Good job, [mc]."
    scene 49_s20 with dissolve
    mc "Wasn't too hard."
    scene 49_s2 with dissolve
    ada "*chuckles* Look at mister horse stamina over here."
    ada "Anyway, I hope your seed bears fruit."
    scene 49_s20 with dissolve
    mc "Where's Ysella?"
    scene 49_s2 with dissolve
    ada "She's with Oswald—appointing the next bride to lead us. The cycle must continue, even after the festival."
    scene 49_s20 with dissolve
    mc "A new couple has to be chosen?"
    scene 49_s2 with dissolve
    ada "Yes. That's how it goes."
    scene 49_s20 with dissolve
    mc "I see. Wait, shouldn't I be chosen? I was the one who won."
    scene 49_s2 with dissolve
    ada "*chuckles* It doesn't work like that. The couple is chosen after years of commitment. Besides, it's the goddess who decides."
    scene 49_s3 with dissolve
    annette "Would you like to come watch?"
    scene 49_s20 with dissolve
    mc "I'm not sure. I need to go find Alex first."
    scene 49_s2 with dissolve
    ada "I understand."
    scene 49_s3 with dissolve
    annette "You must really love her..."
    scene 49_s20 with dissolve
    mc "Love her? Well... that's not really it. She saved my life. Twice."
    scene 49_s3 with dissolve
    annette "Hmm... So... You're leaving now, right?"
    scene 49_s20 with dissolve
    mc "Leaving? Right... I was so caught up in all of this that I almost forgot why I came here in the first place..."
    scene 49_s2 with dissolve
    ada "Be careful not to lose your way, [mc]... but, um... we'd be happy if you stayed a bit longer."
    scene 49_s20 with dissolve
    mc "I'm not sure I can, even if I wanted to."
    scene 49_s4 with dissolve
    ada "Oh? Looks like your friend finally woke up."
    scene 49_s5 with dissolve
    mc "Huh?"
    scene 49_s6 with Dissolve(0.8)
    mc "...Alex?"
    if mc_masturbated_to_alex:
        scene 49_s9 with dissolve
        alex "..."
        play sound "sound_effects/punch2.mp3"
        scene 49_s10 with vpunch
        mc "Aww!"
        mc "What the hell?!"
        scene 49_s8 with dissolve
        alex "You know exactly why."
        scene 49_s11 with dissolve
        mc "But... *gasp* But you agreed to it... Agh..."
        alex "..."
        ada "Is... everything fine?"
    scene 49_s7 with dissolve
    alex "Who are they?"
    scene 49_s6 with dissolve
    mc "That's Ada."
    ada "Pleasure to meet you."
    mc "And that's Annette."
    annette "Hello."
    scene 49_s7 with dissolve
    alex "Thank you for taking care of me."
    scene 49_s9 with dissolve
    mc "Good to see you again. How are you feeling?"
    scene 49_s8 with dissolve
    alex "Better. Still sore, but it should fade in a couple of days."
    scene 49_s9 with dissolve
    mc "Glad to hear it. You... missed a lot."
    alex "Hmm?"
    mc "I'll fill you in later. What do you want to do now?"
    scene 49_s8 with dissolve
    alex "Did you get the supplies?"
    scene 49_s9 with dissolve
    mc "Supplies? Oh... no, I didn't..."
    scene 49_s8 with dissolve
    alex "What the hell were you doing all this time? I've been out cold for days."
    scene 49_s6 with dissolve
    ada "[mc] was handling sacred duties. Please don't be too hard on him. We'll make sure you have what you need when you leave."
    scene 49_s8 with dissolve
    alex "*sigh* Thank you. But we really need to get a move on, [mc]. I can't waste any more time."
    scene 49_s9 with dissolve
    mc "Let's go. We've already stayed too long."
    scene 49_s8 with dissolve
    alex "Good."
    scene 49_s9 with dissolve
    annette "I..."
    scene 49_s12 with dissolve
    mc "You don't know, I might come back one day. For now goodbye, Annette. Ada."
    scene black with Fade(0.5,0.5,0.5)
    ada "Goodbye, [mc]."
    stop music fadeout 2.0 
    annette "..."
    play music "2_opening_ride.mp3" fadein 3.0 loop
    scene 49_s13 with fade
    mc "Oh... Agi?"
    mc "And is that Roza?"
    ada "Yes, she was the one chosen."
    mc "Good for her."
    mc "What will happen to Ysella and Oswald?"
    ada "They will retire their positions and live as regular villagers from now on."
    alex "What is going on..."
    mc "It's... complicated."
    if mc_let_aldwin_win:
        mc "Before we head out... I want to visit someone first."
        alex "Alright. I'll wait."
        scene 49_s15 with Fade(1.0,1.0,1.0)
        aldwin "Ah... [mc]. Welcome."
        scene 49_s14 with dissolve
        mc "Why aren't you out celebrating with the new bride?"
        scene 49_s15 with dissolve
        aldwin "Ah... these things aren't really for me anymore."
        scene 49_s16 with dissolve
        aldwin "Here. As promised."
        scene 49_s17 with dissolve
        perception "He hands you a small golden braclet. Its weight tells you it's worth at least a fortune."
        call screen scene49_choice01
    jump scene49_2

label scene49_choice01_op1:
    $ mc_took_aldwin_gift = True
    mc "Thanks, Aldwin."
    scene 49_s15 with dissolve
    aldwin "Not at all. I should be the one thanking you."
    scene 49_s14 with dissolve
    mc "I'm leaving the village soon."
    scene 49_s15 with dissolve
    aldwin "I heard. Then I won't keep you. Be safe out there, [mc]."
    scene 49_s14 with dissolve
    mc "You too."
    jump scene49_2

label scene49_choice01_op2:
    mc "That won't be necessary."
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    play sound "sound_effects/karma_more.mp3" volume 0.2
    show screen stat_change with easeinright
    scene 49_s16 with dissolve
    aldwin "Hm? Are you sure?"
    scene 49_s17 with dissolve
    mc "I am."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 49_s18 with dissolve
    aldwin "...Then maybe I'll buy something nice for Sigrun."
    scene 49_s19 with dissolve
    mc "That sounds like a better use for it."
    scene 49_s18 with dissolve
    aldwin "I heard you're heading out. May the goddess watch over your path."
    scene 49_s19 with dissolve
    mc "Take care of yourself, Aldwin."
    scene 49_s18 with dissolve
    aldwin "You have a heart of gold, don't let them take it from you."
    scene 49_s19 with dissolve
    jump scene49_2

label scene49_2:
    scene 49_s21 with Fade(1.0,1.0,1.0)
    ysella "Wait, [mc]. Take this. it will help you on your journey."
    scene 49_s22 with dissolve
    perception "She hands you two bags. One is filled with water and the other with various fruits."
    mc "Thank you, Ysella. And thanks for patching up my friend too."
    scene 49_s21 with dissolve
    ysella "You are most welcome. Please, visit us whenever you can."
    ysella "We'd be delighted to hear from you again. Your children might love to see their father one day."
    scene 49_s22 with vpunch
    alex "C-C-CHILDREN?"
    mc "Ahahaha... Yeah... Sure..."
    scene 49_s21 with dissolve
    ysella "Oh dear... I hope I haven't said anything I shouldn't have..."
    scene 49_s22 with dissolve
    mc "*ahem* It's fine... Goodbye, Ysella. Give my congratulations to Agi and his Roza."
    scene 49_s21 with dissolve
    ysella "I will. Farewell, [mc]."
    scene 49_s22 with dissolve
    scene 49_s23 with Fade(1.0,1.0,1.0)
    alex "What the fuck was she talking about? Whose children?!"
    mc "Look, it'll make sense... just let me explain."
    mc "So I basically—"
    scene black 
    jump scene50

label scene50_maia_event:
    $ mc_saw_maia_event = True
    if not mc_maia_left:
        $ mcname = persistent.name
        if persistent.name == "None" or mcname == "None":
            while mcname == "None" or mcname == "":
                $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
            $ persistent.name = mcname
        if not persistent.scene7_p4_replay:
            $ persistent.scene7_p4_replay = True
        $ mc_saw_maia_event = True
        stop music fadeout 2.0 
        scene black with Fade(2.0,1.0,1.0)
        play music "maia.mp3" fadein 2.0 loop
        scene 43_s83 with dissolve
        ""
        scene black with dissolve
        env "The morning light spills gently across the stone floor. In the quiet of the quarters, Maia sits with Crumps."
        scene 44_s1 with Fade(0.5,0.5,0.5)
        m "*sigh* Where did you go, [mx]...?"
        m "You left without a word. Again."
        if not persistent.scene3_p2_replay and not persistent.scene4_p2_replay and not persistent.scene5_p2_replay and not persistent.scene6_p2_replay and not persistent.scene7_p2_replay and not persistent.scene7_replay and not persistent.scene5_replay and not persistent.scene3_replay:
            m "You never even touched me, yet my body won't stop aching..."
            scene 44_s2 with dissolve
            play sound "sound_effects/meow.mp3"
            crumps "Mao."
            m "Hmm?"
            crumps "Mmmph. Mrow."
            scene 44_s1 with dissolve
            m "It's not fair. He made me feel this way and just left."
            scene 44_s3 with dissolve
            m "I'll just have to make do..."
            m "If I don't... I'll go insane..."
            m "Please... look away, Crumps."
            play sound "sound_effects/meow2.mp3"
            crumps "Meow..."
            stop music fadeout 2.0 
            scene 44_s4 with Fade(1.0,0.5,0.5)
            m "Just... pretend he's here..."
            play sound "se_sfx/sex/touch2.mp3" 
            scene 44_s5 with dissolve
            m "S-Slowly..."
            show maia_m1 with dissolve
            m "Ahhh... Hahh~"
            m "Hnngh... [mx]... you don't even know what you do to me..."
            m "Why do you make me feel like this...?"
            m "It hurts... and yet... it feels so good..."
            m "Mmh~ [mx]... I wish it was your hands... not this stupid banana!"
            m "Hnn... I'm such an idiot...!"
            m "Hahh... [mx]... I'm gonna—! Nghhh~!"
            show maia_m2 with dissolve
            hide maia_m1 with dissolve
            m "Hnmm~ [mx]! [mx]!"
            m "Yes~ Yes! Just like that, [mc]~ It's sooooo huge~"
            m "I can't... Hnghh~ believe I'm doing this again... but it feels... so good!"
            m "[mx]... I'm going to... spill my juices all over your pillow!"
            stop sound
            scene 44_s6 with vpunch
            r "*yawn* Maia, would you accompany me to the market—"
            scene 44_s7 with dissolve
            r "..."
            scene 44_s8 with dissolve
            m "..."
            scene 44_s7 with dissolve
            ""
            play sound "sound_effects/door.mp3"
            scene 44_s9 with dissolve
            ""
            scene 44_s10 with dissolve
            m "Someone please kill me..."
            $ renpy.end_replay()
        else:
            m "My body hasn't stopped aching since..."
            scene 44_s2 with dissolve
            play sound "sound_effects/meow.mp3"
            crumps "Mao."
            m "Hmm?"
            play sound "sound_effects/meow.mp3"
            crumps "Mmmph. Mrow."
            scene 44_s1 with dissolve
            m "I hope so too..."
            scene 44_s3 with dissolve
            m "I'll just have to make do until he returns..."
            m "Please... look away, Crumps."
            play sound "sound_effects/meow2.mp3"
            crumps "Meow..."
            stop music fadeout 2.0 
            scene 44_s4 with Fade(1.0,0.5,0.5)
            m "I hope you don't mind me doing it above your pillow, [mx]..."
            m "Alright. just... pretend it's him..."
            play sound "se_sfx/sex/touch2.mp3" 
            scene 44_s5 with dissolve
            m "S-Slowly..."
            show maia_m1 with dissolve
            m "Ahhh! Hahh~"    
            m "Hnn... husband... just like that..."
            m "Don't leave me empty again..."
            m "It's okay, husband~ Hnng~ You can be rough with me!"
            show maia_m2 with dissolve
            hide maia_m1 with dissolve
            m "Hnmm~ [mx]! [mx]!"
            m "Yes~ Yes! Just like that, [mc]~ It's sooooo huge~"
            m "I can't... Hnghh~ believe I'm doing this again... but it feels... so good!"
            m "[mx]... I'm going to... spill my juices all over your pillow!"
            stop sound
            scene 44_s6 with vpunch
            r "*yawn* Maia, would you accompany me to the market—"
            scene 44_s7 with dissolve
            r "..."
            scene 44_s8 with dissolve
            m "..."
            scene 44_s7 with dissolve
            ""
            play sound "sound_effects/door.mp3"
            scene 44_s9 with dissolve
            ""
            scene 44_s10 with dissolve
            m "Someone please kill me..."
            $ renpy.end_replay()
    if not mc_saw_yuuhi_event:
        jump scene50_yuuhi_event
    else:
        jump scene50

label scene50_yuuhi_event:
    $ mc_saw_yuuhi_event = True
    stop music fadeout 2.0 
    scene black with Fade(1.0, 1.0, 1.0)
    play music "yuuhi.mp3" fadein 2.0 loop
    scene 47_s43 with fade
    yuuhi "(No, no, no... The seam needs to sit {i}above{/i} the hipbone, not below! Ugh, I'm such a fraud...)"
    yuuhi "(You think Gavlan would ever had to worry about waistlines? I bet he just wore whatever the wind gave him...)"
    dean "Yuuhi! The Queen's guards want that tabard before sundown!"
    scene 47_s44 with dissolve
    yuuhi "I'm working on it!"
    scene 47_s43 with dissolve
    if mc_harem_yuuhi:
        yuuhi "(...I hope [mc] is alright.)"
        yuuhi "(No more daydreaming...)"
    play sound "sound_effects/metalhit.mp3"
    scene 47_s45 with vpunch
    yuuhi "Ah!"
    dean "What happened? That damn club fall again?!"
    scene 47_s46 with dissolve
    yuuhi "...No."
    scene 47_s47 with dissolve
    dean "We ought to throw that thing out. No one's ever going to buy it."
    scene 47_s46 with dissolve
    yuuhi "No! There has to be someone... out there... maybe..."
    stop music fadeout 2.0 
    scene 47_s47 with dissolve
    if not mc_saw_maia_event:
        jump scene50_maia_event
    else:
        jump scene50

label scene50:
    scene 50_s1 with Fade(1.0,1.0,2.0)
    if mc_paricipated_festival:
        alex "I can't believe this..."
        mc "Crazy, right?"
        alex "Crazy?! You participated in it!"
        if not mc_won_festival:
            mc "I didn't win, so who cares?"
        else:
            mc "..."
        alex "*sigh* Whatever. At least we got some supplies out of it."
        alex "...Did they tell you anything? About me?"
        mc "What do you mean?"
        alex "...Forget it. Let's just keep moving."
    else:
        alex "I can't believe this..."
        mc "Insane. I'm just glad we're out of there."
        alex "...Did they tell you anything? About me?"
        mc "Not really. Why?"
        alex "Never mind. Let's just go."
        alex "We need to make some stops before we head out."
        mc "For what?"
        alex "Supplies. Food. Bandages. Anything we can scrape together."
        mc "Is it that bad?"
        alex "We won't even last the night if we leave now. And I'm not marching off half-dead again."
        mc "So how long are we talking?"
        alex "Hopefully not too long."
    stop music fadeout 2.0 
    scene 50_s2 with Fade(0.5,0.5,0.5)
    env "The air grows heavier. The scent of charcoal and scorched wood thickens with each step."
    mc "Do you smell that?"
    alex "*gasp* No... no, no, no—"
    scene 50_s3 with dissolve
    mc "Alex?!"
    play music "despair.mp3" fadein 3.0 loop
    scene 50_s4 with Fade(0.5,0.5,0.5)
    perception "The remains of the queen of pleasure's mansion lie in blackened ruin. Ash drifts in the wind. Bodies litter the ground."
    mc "...Holy shit."
    alex "No... No!"
    play sound "sound_effects/bodydrop.mp3"
    scene 50_s6 with dissolve
    alex "She was the only one... The only one who could undo the curse."
    scene 50_s5 with dissolve
    mc "We don't know that. Maybe someone else—"
    scene 50_s6 with dissolve
    alex "What do I do now? What do I—"
    alex "I need to look around. Maybe someone's still—"
    scene 50_s7 with dissolve
    mc "Wait... is that...?"
    scene 50_s8 with dissolve
    mc "Gaius?"
    alex "Is he the one who did this?!"
    mc "Hold on. Calm down—"
    play sound "sound_effects/unsheathe2.mp3"
    kat "State your intentions!"
    scene 50_s9 with dissolve
    kat "Wait... if it isn't [mc]!"
    scene 50_s10 with dissolve
    mc "Kat?!"
    scene 50_s9 with dissolve
    kat "Hah! Thought you were probably dead in a ditch. Guess I lost a bet."
    scene 50_s10 with dissolve
    mc "What the hell happened here?"
    scene 50_s9 with dissolve
    kat "Reiner's patience snapped. He ordered the Queen to send Gaius in."
    kat "And since I was still under contract, he sent me to tag along."
    kat "He seems to be doing just fine without me..."
    scene 50_s11 with dissolve
    kat "...Huh? That's not— Is that you Alex?"
    scene 50_s12 with dissolve
    alex "He sent Gaius?"
    alex "Of course he did."
    kat "He... He was really worried for you, Alex. He assumed you were being held here... by force."
    kat "Besides, you told me you'll be gone for only a few days. You almost got me into big trouble!"
    scene 50_s19 with Dissolve(1.0)
    alex "Well, he didn't come for me. He came for his heir. His legacy. He doesn't care if I'm dead, so long as someone sits on that throne."
    alex "I was never his daughter. Just an heir in a dress."
    scene 50_s13 with vpunch
    mc "Alex—wait!"
    alex "If he wants me this bad then I'll go to him myself!"
    kat "Gaius!"
    scene 50_s14 with dissolve
    alex "Out of my way Gaius!"
    scene 50_s15 with vpunch
    alex "*gasp* Let go...!"
    scene 50_s16 with dissolve
    kat "Don't do anything stupid, [mc]. You know better than to go against {i}him{/i}."
    alex "*wheeze* Aghhh!"
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene50_choice01 with dissolve

label scene50_choice01_op1:
    mc "I can't just stand here!"
    scene 50_s27 with dissolve
    mc "Get your hands off of her!"
    kat "[mc], stop! Don't—!"
    play sound "sound_effects/metalhit2.mp3"
    scene 50_s28 with vpunch
    sensation "You put your entire weight behind the punch. Your knuckles smash into the cold metal of his helmet with a loud CLANG. A jolt of intense pain shoots up your arm. It definitely hurt you more than it hurt him."
    scene 50_s29 with dissolve
    perception "Caught off guard by the attack, Gauis releases Alex and staggers back a single step. He immediately regains his balance, his featureless helmet turning to focus on you. Alex crumples to the ground, gasping and coughing for air."
    kat "Gaius, stand down! Don't attack him!"
    mc "What's the matter? You want some more?!"
    scene 50_s30 with dissolve
    mc "*chuckles* Fine. Let's do this."
    scene 50_s31 with dissolve
    mc "AHHHHH!"
    play sound "sound_effects/punch3.mp3"
    scene 50_s32 with hpunch
    sensation "Your head snaps to the side. The world dissolves into a burst of white light and a high pitched ring."
    scene 50_s33 with dissolve
    perception "You're on your knees before you even realize you've fallen, the taste of copper flooding your mouth."
    mc "Fuck... Hah... Is that..."
    scene 50_s34 with Dissolve(1.0)
    mc "...Is that the best you got?! You hit like a bitch!"
    alex "ENOUGH!"
    scene 50_s35 with dissolve
    alex "Just... just fucking take me, alright!? I'll come! Stop it!"
    mc "Alex...?"
    alex "It's fine, [mc]. Really... it's over."
    mc "..."
    call screen scene50_choice01_new with dissolve
    stop music fadeout 2.0 
    scene 50_s36 with dissolve
    mc "Gimme your hand."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    $ mc_tried_help_alex = True
    play music "night.mp3" fadein 1.0 loop
    scene 50_s38 with Dissolve(1.5)
    alex "*cough* ...Thank you."
    alex "You're insane. I've never seen anyone even try to stand up to him, let alone get back up after taking a shot like that."
    hide screen stat_change with easeoutright
    $ karma_more = False
    alex "*chuckles* I can't tell if you're the bravest person I've ever met or just the stupidest."
    scene 50_s37 with dissolve
    mc "A little bit of both."
    scene 50_s38 with dissolve
    alex "*laughs* Come on. Let's just... leave."
    scene 50_s37 with dissolve
    kat "Alex... I have to tie you up. I'm sorry."
    scene 50_s39 with dissolve
    alex "Ugh. Seriously?"
    kat "I just can't take any chances on the road back."
    alex "*grumples*"
    jump scene50_2

default mc_kept_attack_gaius = False
label scene50_choice01_op2_new:
    $ mc_kept_attack_gaius = True
    scene 50_s40 with Dissolve(1.0)
    mc "Sorry, Alex. But I'm not doing this for you."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    alex "W-What?"
    mc "I just wanted to beat this guy up for a while now."
    hide screen stat_change with easeoutright
    $ karma_less = False
    alex "..."
    mc "You think you can do whatever the hell you want, huh? Well, I'm about to show you otherwise—"
    play sound "sound_effects/punch5.mp3"
    scene black with vpunch
    sensation "Pain explodes at the base of your skull. Your knees buckle and the world tilts."
    kat "...That's enough, [mc]. I can't let you hurt yourself any further."
    jump scene50_2

label scene50_choice01_op2:
    scene 50_s18 with dissolve
    mc "Dammit..."
    perception "You watch, helpless, as Gaius's grip strengthened. Alex's face turned a darker shade of purple, her body going limp. She was out cold."
    kat "Come on, [mc]. We're leaving."
    mc "..."
    jump scene50_2

label scene50_choice01_op1_2:
    $ renpy.notify("Check failed!")
    mc "(Fuck... I'm shaking really bad... I can barely move my arms!)"
    perception "You watch, helpless, as Gaius's grip strengthened. Alex's face turned a darker shade of purple, her body going limp. She was out cold."
    kat "Come on, [mc]. We're leaving."
    mc "..."
    jump scene50_2

label scene50_2:
    scene 50_s20 with Fade(0.5,0.5,0.5)
    ""
    stop music fadeout 2.0 
    scene 50_s21 with Fade(1.0,1.0,1.0)
    play music "desert.mp3" fadein 2.0 volume 0.2 loop
    ""
    scene 50_s22 with Fade(0.5,0.5,0.5)
    ""
    scene 50_s23 with dissolve
    ""
    scene 50_s24 with dissolve
    ""
    scene 50_s25 with Dissolve(1.0)
    ""
    scene 50_s26 with Dissolve(1.0)
    ""
    stop music fadeout 2.0 
    scene black with Fade(0.5,0.5,0.5)
    play music "images/custom_gui/global/mainmenu/mainmenu_song.mp3" fadein 2.0 loop
    show expression "chapter1_journey_main" at center with dissolve

    window hide
    pause 0.5
    window show
    ""
    show chapter2_recap1 with dissolve
    if mc_maia_left:
        "Maia left you. Broken trust leaves no room for love."
    else:
        "Maia stayed by your side. Not out of fear but out of love. For now."
    show chapter2_recap2 with dissolve
    hide chapter2_recap1
    if maia_know_wed_reb:
        "Maia knows you intend to marry the princess. Jealousy brews in quiet places."
    show chapter2_recap3 with dissolve
    hide chapter2_recap2
    if mc_friend_reb:
        "You've earned the princess's favor. Whether it's love or leverage, time will tell."
    else:
        "The princess remains distant. Or maybe she's just playing a longer game."

    show chapter2_recap4 with dissolve
    hide chapter2_recap3
    if mc_allowed_ymir:
        if mc_forgive_ymir:
            "You forgave Ymir. Mercy is a rare luxury in this world."
        elif mc_agree_punish_ymir:
            "You let Ysella punish Ymir in your place. Delegation is a kind of justice."
        else:
            "You punished Ymir yourself. A message, loud and clear."
    else:
        "You didn't allow Ymir to {i}help{/i} you with bathing. Your instincts are sharp."
    
    show chapter2_recap5 with dissolve
    hide chapter2_recap4
    if mc_paricipated_festival:
        "You stepped into the circle and played the cult's game. Strange rites for stranger rewards."
        show chapter2_recap6 with dissolve
        hide chapter2_recap5
        if mc_let_aldwin_win:
            "You let Aldwin win. One final gift to a dying man's pride."
        else:
            "You fought and won. Strength claims what sentiment cannot."
        show chapter2_recap7 with dissolve
        hide chapter2_recap6
        if mc_masturbated_to_alex:
            "You asked Alex to let you use her body. Not quite love. Not quite hate."
        else:
            "You kept your urges in check. Barely."
        show chapter2_recap8 with dissolve
        hide chapter2_recap7
        if mc_date_adaroza_win:
            "You won Roza and Ada over. Charm and timing go a long way."
        else:
            "You fumbled your way through their hearts. Two doors closed—just like that."
        
        if not mc_let_aldwin_win:
            show chapter2_recap9 with dissolve
            hide chapter2_recap8
            if mc_date_sigrun_win:
                "You earned Sigrun's trust. A rare thing from a woman who's lost so much."
            else:
                "You didn't make the cut. Some walls weren't meant for you to climb."

        if mc_let_aldwin_win and mc_took_aldwin_gift:
            show chapter2_recap10 with dissolve
            hide chapter2_recap9
            "You accepted Aldwin's reward. A simple exchange between men who understood each other."
        elif mc_let_aldwin_win and not mc_took_aldwin_gift:
            show chapter2_recap10 with dissolve
            hide chapter2_recap9
            "You turned down Aldwin's reward. He offered to buy his wife something with it instead."
    else:
        "You walked away from the cult's tradition. Not every ritual deserves your seed."

    show chapter2_recap11 with dissolve
    hide chapter2_recap10
    if mc_tried_help_alex:
        "You tried to help Alex when Gaius had her by the throat. Some instincts still matter."
    else:
        "You hesitated. Maybe that moment will haunt you more than her."

    show chapter1_recap12 with dissolve
    hide chapter2_recap11
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1

    if mc_karma < 1:
        $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    "You have [mc_coin] coins to your name, and your honor stands at [mc_karma] out of 10. Whatever that means."
    scene chapter3 with Fade(1.5,0.5,1.5)
    ""
    stop music fadeout 1.5
    scene 51_s1 with Fade(1.0,1.0,1.0)
    play music "2_opening_ride.mp3" fadein 0.5 loop
    env "The carriage rocks gently over the cobbled road. In the distance, the grey stone towers of Irda rise against the cloudy sky. The city's banners flap in the wind, black and gold."
    window hide
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if mc_kept_attack_gaius:
        scene 51_s11 with dissolve
        mc "Ughh... my head..."
        kat "Morning, [mc]. Sorry about that. Don't get too upset about it, it was for your own good."
        mc "Fuck... whatever."
        scene 51_s2 with dissolve
        mc "Agh... So... you're royalty?"
    else:
        scene 51_s2 with dissolve
        mc "So... you're royalty?"
    scene 51_s3 with dissolve
    alex "Apparently."
    scene 51_s2 with dissolve
    mc "Why didn't you tell me? I remember telling you when we first met that I was looking for a girl going to meet the queen of pleasure."
    scene 51_s3 with dissolve
    alex "Shouldn't it have been obvious? I was the only soul walking that forest."
    scene 51_s2 with dissolve
    mc "I... You didn't exactly {i}look{/i} the part, you know?"
    scene 51_s3 with dissolve
    alex "What's {i}that{/i} supposed to mean?"
    scene 51_s2 with dissolve
    mc "Forget it."
    mc "Does she really need to be tied up? It feels a bit excessive now."
    scene 51_s4 with dissolve
    alex "Yes. Is this really necessary?"
    kat  "Please, Alex. It's for your own good."
    alex  "My own good? You think tying me up like a criminal is for my own good?"
    kat "*sigh* I'm sorry."
    kat "...Just hang in there. We're almost there."
    scene 51_s5 with dissolve
    alex  "And you. Don't think for a second you'll get away with what you did."
    scene 51_s6 with dissolve
    "..."
    scene 51_s7 with dissolve
    mc "Does the Queen know about any of this?"
    kat "Hmm? ...Of course."
    mc "That didn't sound convincing."
    kat "Look. Lord Reiner ordered it. She... must have approved it."
    mc "Burning down an entire mansion? Killing everyone inside?"
    mc "I barely know anything about the queen but that doesn't sound like her."
    kat "Shit. You're right."
    scene 51_s8 with dissolve
    kat "Gaius? You have anything to say?"
    scene 51_s9 with dissolve
    "..."
    scene 51_s8 with dissolve
    kat "Great, thanks for that."
    kat "[mc]... listen carefully. You need to say they attacked us first."
    scene 51_s9 with dissolve
    mc "You want me to lie? That bloodbath looked more like a slaughter."
    scene 51_s8 with dissolve
    kat "Just... don't mention it at all. I'll handle the rest."
    scene 51_s9 with dissolve
    alex "*chuckles* You two have tangled yourselves into quite the mess."
    scene 51_s7 with dissolve
    kat "Please, Alex..."
    alex "I'm not saying anything. But this will bite you eventually."
    kat "..."
    scene 51_s10 with Fade(0.5,0.5,0.5)
    perception "The city of Irda grows larger ahead, its towering gates looming ever closer."
    stop music fadeout 2.0
    alex "My nose itches."
    scene 52_s1 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 0.5 loop
    kat "Remember what I said, [mc]. Stick to the story."
    scene 52_s2 with dissolve
    mc "I'll say what I feel like."
    scene 52_s1 with dissolve
    kat "Oh? Maybe you need an intensive first?"
    scene 52_s2 with dissolve
    mc "What kind?"
    scene 52_s3 with dissolve
    kat "Would a fist to the face do?"
    scene 52_s4 with dissolve
    d "[mc]! Welcome back."
    scene 52_s6 with dissolve
    mc "Hey, Darius."
    scene 52_s5 with dissolve
    d "*chuckles* I'll admit—I was a little worried. Things can get messy for you new adventures."
    scene 52_s6 with dissolve
    mc "Job's done. No need to worry."
    scene 52_s7 with dissolve
    d "I can see that."
    d "Though I don't recall Kathrine and Gaius being part of your escort."
    scene 52_s8 with dissolve
    kat "..."
    scene 52_s7 with dissolve
    d "Kathrine?"
    scene 52_s8 with dissolve
    kat "Oh, that. While walking near the city, I noticed some activity not far from the road—looked suspicious."
    scene 52_s9 with dissolve
    kat "So Gaius and I went to investigate. Turned out it was just a traveling circus caravan."
    kat "*laughs* Can you believe that?"
    scene 52_s7 with dissolve
    d "Hah... And is there a particular reason why the next in line to Eurina's throne is bound like a criminal?"
    scene 52_s9 with dissolve
    kat "[mc]?"
    scene 52_s10 with dissolve
    mc "Huh?"
    mc "(Shit... Damn it, Kat...)"
    scene 52_s11 with dissolve
    alex "I ran off. He had to restrain me to bring me back safely."
    scene 52_s7 with dissolve
    d "I see..."
    d "Regardless—welcome, Lady Alex. Your father is eagerly awaiting your return. A carriage will come pick you up shortly."
    d "*ahem*. Untie her."
    scene 52_s12 with dissolve
    guard "Yes, sir."
    scene 52_s13 with Fade(1.0,1.0,0.5)
    d "And you, [mc], you'll come with me. We'll be heading to the throne room as well."
    scene 52_s14 with dissolve
    mc "No carriage for us?"
    scene 52_s13 with dissolve
    d "Afraid not."
    scene 52_s14 with dissolve
    mc "Before we go, what you said earlier about Alex. Is she really next in line for the throne?"
    scene 52_s13 with dissolve
    d "It was more of a compliment, honestly. She's the daughter of the king's brother."
    d "The king has no heirs of his own. So if he dies, succession falls to either Lord Reiner... or his daughter."
    scene 52_s14 with dissolve
    mc "I see. Thanks for clearing that up."
    scene 52_s13 with dissolve
    d "Of course. Now come on. We shouldn't keep royalty waiting."
    stop music fadeout 2.0
    scene 52_s14 with dissolve
    scene 8_s5 with Fade(1.0,1.0,1.0)
    ""
    scene 52_s15 with Fade(0.5,0.5,0.5)
    play music "queen.mp3" fadein 0.5 loop
    q "[mc]? I wasn't expecting your return so soon. Darius—what news do you bring?"
    scene 52_s16 with dissolve
    d "Your Majesty, [mc] has fulfilled his task. Lord Reiner's daughter has been retrieved and returned safely and soundly."
    scene 52_s15 with dissolve
    q "Is that so? I had prepared myself to hear only a report. To see her returned as well... that is commendable."
    scene 52_s16 with dissolve
    mc "Thank you, Your Majesty."
    scene 52_s15 with dissolve
    q "You've gone above and beyond, [mc]. Your service will not go unrewarded."
    scene 52_s16 with dissolve
    mc "Of course."
    scene 52_s15 with dissolve
    q "Darius. Where is she?"
    scene 52_s16 with dissolve
    d "I apologzie, Your Majesty. I... assumed she would arrive ahead of us. I ordered her a carriage, surrounded by guards."
    scene 52_s15 with dissolve
    q "That was careless. You should have accompanied her yourself."
    scene 52_s17 with dissolve
    d "My apologies, Your Majesty. I'll depart to retrieve her immediately."
    scene 52_s18 with dissolve
    reiner "No need. I am here."
    scene 52_s19 with Dissolve(1.0)
    d "Lord Reiner. Welcome."
    scene 52_s20 with Dissolve(0.8)
    q "Reiner. How is your daughter?"
    scene 52_s21 with dissolve
    reiner "Not as well as I'd like. Scratches, bruises, broken rib. I had her examined on the way here."
    scene 52_s20 with dissolve
    q "That wasn't the report you gave me, Darius."
    d "Your Majesty—I only saw what was visible. I hadn't the chance to perform a full examination."
    scene 52_s22 with dissolve
    alex "I'm fine. Let's not make a scene out of this."
    scene 52_s23 with dissolve
    reiner "Enough, girl. You're fortunate I'm not sending you straight to reconditioning."
    scene 52_s21 with dissolve
    reiner "Those {i}bandits{/i} will pay for this. I'll see every one of them hunted down."
    scene 52_s20 with dissolve
    q "We'll address that in due time, Reiner."
    scene 52_s21 with dissolve
    reiner "*sigh* Regardless, she is returned. And for that, I am thankful."
    reiner "As agreed, I will press the king to open the trade routes and provide the troops we discussed."
    scene 52_s20 with dissolve
    q "Good. The sooner, the better. Our window grows narrow."
    scene 52_s24 with dissolve
    reiner "Then, if you'll excuse me. My daughter needs proper instruction before she's seen publicly again."
    scene 52_s25 with dissolve
    q "Farewell. And be safe out there."
    scene 52_s24 with dissolve
    reiner "I brought my own men this time. From {i}our{/i} lands. We'll be fine."
    scene 52_s25 with dissolve
    q "..."
    scene 52_s26 with Dissolve(0.8)
    q "Reiner. Aren't you forgetting something?"
    scene 52_s27 with dissolve
    reiner "Ah... Of course."
    reiner "A reward is due."
    scene 52_s28 with Dissolve(1.0)
    reiner "Here, young man."
    reiner "*cough* Spend it wisely."
    scene 52_s29 with dissolve
    impulse "Look at that bag... it's practically bursting with gold. With that much, you could finally hire that maid from the market."
    empathy "Alex is watching you. Quietly. Carefully. It's better to let go."
    window hide
    call screen scene52_choice01 with dissolve

default mc_took_reiner_money_first = False
label scene52_choice01_op1:
    $ mc_took_reiner_money = True
    $ mc_coin += 1000
    if not mc_took_reiner_money_first:
        $ mc_took_reiner_money_first = True
        $ alex_love -= 30
    if mc_karma > 1:
        $ mc_karma -= 2
    if mc_karma <= 0:
        $ mc_karma = 1 

    scene 52_s30 with dissolve
    mc "Thank you."
    $ renpy.notify("You received 1000 coins!")
    play sound "sound_effects/coin_collect.mp3"
    mc "(Holy shit! This is way too much.)"
    scene 52_s31 with dissolve
    reiner "Of course."
    scene 52_s30 with dissolve
    scene 52_s32 with Fade(0.5,0.5,0.5)
    ""
    jump scene52_2

label scene52_choice01_op2:
    mc "I'll have to decline."
    scene 52_s28 with dissolve
    reiner "Take it."
    scene 52_s29 with dissolve
    mc "No. Keep it. I didn't do it for coin."
    scene 52_s31 with dissolve
    reiner "I see... An honorable man. Or perhaps a proud one."
    reiner "Very well then."
    scene 52_s30 with dissolve
    scene 52_s32 with Fade(1.0,0.5,0.5)
    ""
    jump scene52_2

label scene52_2:
    scene 52_s15 with Fade(0.5,0.5,0.5)
    q "Quite the man, isn't he?"
    scene 52_s16 with dissolve
    mc "Yeah... he seems it."
    scene 52_s15 with dissolve
    q "*sigh*"
    q "I feel like a great weight has been lifted from my chest."
    scene 52_s16 with dissolve
    mc "What do you mean?"
    scene 52_s26 with dissolve
    q "Have you forgotten already, [mc]? Our kingdom has been sliding toward ruin for years. Resources depleted, alliances strained... disaster looming."
    q "Reiner's daughter going missing was... an opportunity I never dared hope for. *ahem* Not that I wished for such misfortune, of course."
    q "With this marriage alliance, his lands will provide the resources we need to rebuild. His daughter's return secured far more than just her life. It secured our survival."
    scene 52_s27 with dissolve
    mc "Marriage alliance?"
    scene 52_s26 with dissolve
    q "Yes. His daughter will marry my son, once the arrangements are finalized."
    scene 52_s27 with dissolve
    mc "You have a son? I've never seen him before."
    scene 52_s26 with dissolve
    q "He governs our second city, Aria. A vital duty, but one that keeps him... distant. He rarely visits the capital."
    scene 52_s27 with dissolve
    mc "Well... that's good. For the kingdom, I mean."
    scene 52_s15 with dissolve
    q "Good for us, [mc]. You have proven yourself remarkably dependable. Far more than I ever anticipated from an... outsider."
    scene 52_s15 with dissolve
    q "Rebecca, you may leave us."
    scene 52_s35 with Dissolve(1.0)
    r "Huh? Why? You summoned me here yourself!"
    scene 52_s36 with dissolve
    q "I know. And you have listened. Now you must learn that a ruler's work often continues in private. Leave us."
    scene 52_s35 with dissolve
    r "I just wish you would be more honest next time, Mother. I prefer not to sit through these mindless political speeches."
    scene 52_s36 with dissolve
    scene 52_s26 with Dissolve(1.0)
    q "*sigh* Approach, [mc]."
    scene 52_s40 with Dissolve(1.5)
    mc "...Yes?"
    scene 52_s39 with dissolve
    q "Tell me. What is your honest opinion of my daughter?"
    scene 52_s40 with dissolve
    mc "I... I'm not sure what you mean. She's the Princess."
    scene 52_s39 with dissolve
    q "Do not play coy. It does not suit you. I am thinking of offering her hand to you, [mc]."
    scene 52_s40 with dissolve
    mc "..."
    scene 52_s41 with dissolve
    q "It is a painful thing for a mother to admit, but... I fear I have done a poor job raising her. I was grieving a husband and ruling a crumbling kingdom. She was spoiled, left to her own devices."
    q "She never had a strong, manly figure to guide her."
    scene 52_s39 with dissolve
    q "I believe you could be that for her. I have seen the way she looks at you, even if she would rather die than admit it. She is willful, but not blind."
    scene 52_s40 with dissolve
    mc "Are you suggesting...?"
    scene 52_s39 with dissolve
    q "I am. Hundreds of noble sons have proposed. She has rejected every single one. This cannot continue. She is in her prime; a choice must be made, and soon."
    q "I would rather it be a man of proven character than a politically convenient stranger."
    scene 52_s40 with dissolve
    mc "I don't know what to say... Wouldn't that mean I would be... the future king?"
    scene 52_s39 with dissolve
    q "King? [mc], no. Rebecca is not the heir to the throne. My son is. Do not be confused."
    q "You would be her husband, a prince consort. Your duty would be to guide her, not to rule us."
    scene 52_s40 with dissolve
    mc "I see."
    scene 52_s39 with dissolve
    q "Giving her the crown after I am gone would be... disastrous, to say the least."
    scene 52_s37 with dissolve
    q "We will talk about this later. For now, I wish to reward you personally for returning Reiner's daughter."
    scene 52_s38 with dissolve
    mc "Of course, Your Majesty. What do you have in mind?"
    scene 52_s37 with dissolve
    q "I find myself at a rare impasse. I have already granted you quarters within the castle and my most beautiful maid. Material wants seem... beneath you. Yet, coin is the language of gratitude for most."
    q "So I ask you directly. What is on {i}your{/i} mind?"
    scene 52_s38 with dissolve
    call screen scene52_choice02 with dissolve


label scene52_choice02_op1:
    $ mc_queen_choice_coin = True
    $ mc_coin += 500
    mc "Can't say no to more coin, Your Majesty."
    scene 52_s37 with dissolve
    q "Very well. Direct and pragmatic. A most sensible reward."
    q "Speak with the treasurer tomorrow. He will provide a sum I believe you will find more than satisfactory for your efforts."
    scene 52_s38 with dissolve
    mc "Thank you, Your Majesty."
    scene 52_s37 with dissolve
    q "You are most welcome. You may leave, [mc]. I expect this will not be the last great service."
    scene 52_s38 with dissolve
    jump scene53

label scene52_choice02_op2:
    $ mc_queen_choice_sex = True
    mc "Your Majesty, I must ask that you don't get angry at this..."
    scene 52_s39 with dissolve
    q "Hmm? You need not be shy. If it is a truly vast sum of coin, you have earned the right to ask."
    scene 52_s40 with dissolve
    mc "No, not that."
    scene 52_s39 with dissolve
    q "Speak up then."
    scene 52_s40 with dissolve
    mc "Since the moment I first saw you, I have been... entranced. Not by the crown, but by the woman wearing it. By the sharp intellect in your eyes, the strength of your will... your undeniable beauty."
    mc "I find myself wanting what no one here should ever dare to ask for."
    q "..."
    mc "I don't want a reward, or a favor. I ask for a moment. Not with my Queen, but with Hannah, the woman. To know her."
    q "..."
    scene 52_s39 with dissolve
    q "You are certainly the most interesting man to have walked these halls in some time. Now I understand why you told me not to get angry."
    scene 52_s40 with dissolve
    mc "..."
    scene 52_s39 with dissolve
    q "You must know, were you any other man, my guards would already be dragging you to the dungeons. But... it is you."
    scene 52_s40 with dissolve
    mc "Thank you for not calling them..."
    scene 52_s41 with dissolve
    q "*sigh* It has been... a very long time since I have been looked upon as a woman. The last man to see me thus was my late husband."
    scene 52_s42 with dissolve
    mc "I didn't mean to bring back any painful memories, Your Majesty."
    scene 52_s41 with dissolve
    q "Do not apologize. They are fond memories. It is merely a fact."
    scene 52_s37 with dissolve
    if not maia_virgin:
        q "I have been woken before by the sounds of Maia... screaming in pleasure. It has made me wonder about the man capable of eliciting such passion."
    q "Go. Bathe. Present yourself at my private quarters afterwards. Do not be late. I still have matters to attend to today."
    scene 52_s38 with dissolve
    mc "I'll be there!"
    jump scene13

label scene52_choice02_op3:
    $ mc_queen_choice_nothing = True
    mc "Thank you, Your Majesty, but I don't need anything. You already gave me more than enough."
    scene 52_s39 with dissolve
    q "Hmm? There is no need for such modesty, [mc]. Ask anything. It is yours."
    scene 52_s40 with dissolve
    mc "No, I'm serious. You have done enough for me."
    scene 52_s39 with dissolve
    q "Is that your final answer? I will not offer again."
    scene 52_s40 with dissolve
    mc "Yes."
    scene 52_s37 with dissolve
    q "Very well. *chuckles* You had better not change your mind and come begging later."
    q "And thank you again, [mc]. Your service, and now your character, have been exceptional. I am in your debt."
    scene 52_s38 with dissolve
    mc "I'm honored."
    scene 52_s37 with dissolve
    q "You may leave, [mc]. I have a feeling this will not be the last time we have such a conversation."
    scene 52_s38 with dissolve
    jump scene53

label scene53:
    stop music fadeout 2.0
    scene 53_s1 with Fade(1.0,1.0,1.0)
    ""
    if not mc_maia_left:
        mc "Hmm?"
        scene 53_s2 with dissolve
        mc "Oh, Maia!"
        play sound "sound_effects/clothing_rustle.mp3"
        scene 53_s3 with vpunch
        mc "Ah!"
        scene 53_s4 with dissolve
        play music "maia.mp3" fadein 0.5 loop
        m "[mx]! I missed you so much!"
        scene 53_s5 with dissolve
        sensation "Her arms cling to you like vines, her soft breasts pressing firmly against your chest, her warmth instantly familiar."
        mc "Hey... it's been a while."
        scene 53_s4 with dissolve
        m "Oh, [mx]... I can't believe you were gone for so long..."
        scene 53_s5 with dissolve
        mc "Sorry. I didn't really have much control over that."
        scene 53_s4 with dissolve
        m "I know... I know. But still..."
        m "So... um, how are you? Are you hurt?"
        scene 53_s5 with dissolve
        mc "All good. What about you?"
        scene 53_s6 with dissolve
        m "M-Me? I... I'm fine now that you're back."
        if maia_pregnant:
            m "Maybe I gained some weight."
            scene 53_s7 with dissolve
            mc "(I can tell...)"
            mc "You've been eating good?"
            scene 53_s6 with dissolve
            m "No, [mx]... It's because of my pregnancy."
            scene 53_s7 with dissolve
            mc "Preg— Right..."
        scene 53_s4 with dissolve
        m "Come! Sit down. You must be exhausted."
        scene 53_s5 with dissolve
        scene 53_s9 with Fade(1.0,1.0,1.0)
        mc "So? What did I miss while I was away?"
        scene 53_s10 with dissolve
        m "Umm..."
        scene 53_s9 with dissolve
        mc "...?"
        scene 53_s10 with dissolve
        m "*giggle* N-Nothing?"
        scene 53_s9 with dissolve
        mc "Nothing?"
        scene 53_s10 with dissolve
        m "I—I'm sorry, [mx]! I didn't leave our room much once you left..."
        m "But! I'm sure everything's fine out there!"
        scene 53_s9 with dissolve
        mc "That's good to hear."
        scene 53_s11 with Dissolve(1.0)
        m "[mx]... I... missed your warmth. It's been so cold without you at night."
        m "Sometimes, I hugged your pillow. Pretending it was you."
        scene 53_s12 with dissolve
        mc "You're too adorable for your own good, you know that?"
        scene 53_s11 with dissolve
        m "I-I'm serious... W-When you're not here, it's as if my whole world shrinks."
        scene 53_s12 with dissolve
        mc "I didn't think you'd get so attached."
        scene 53_s11 with dissolve
        m "I don't want anyone else... just you."
        scene 53_s12 with dissolve
        m "..."
        empathy "Her breathing quickens. The mood grows heavier."
        if not persistent.scene3_p2_replay and not persistent.scene4_p2_replay and not persistent.scene5_p2_replay and not persistent.scene6_p2_replay and not persistent.scene7_p2_replay and not persistent.scene7_replay and not persistent.scene5_replay and not persistent.scene3_replay:
            $ mc_maia_no_sex = True
            $ mc_maia_no_sex_real = True
            mc "Something on your mind?"
            m "..."
            scene 53_s13 with Dissolve(1.0)
            m "It's just... things feel different when you're gone. Quiet. Empty."
            scene 53_s14 with dissolve
            mc "Yeah... I missed you too, Maia."
            scene 53_s13 with dissolve
            m "You did?"
            scene 53_s14 with dissolve
            mc "Of course. Things don't feel the same without you."
            scene 53_s13 with dissolve
            m "Then maybe... don't leave for so long next time."
            scene 53_s14 with dissolve
            mc "*chuckles* I'll try not to."
            scene 53_s11 with Dissolve(1.0)
            m "*giggle* Good."
            m "And um... [mx]?"
            scene 53_s12 with dissolve
            mc "Yeah?"
            scene 53_s11 with dissolve
            m "There's something I need to tell you."
            scene 53_s12 with dissolve
            mc "What is it?"
            scene 53_s11 with dissolve
            m "You... you've never touched me before. Not even once. I don't know if you're... waiting for something."
            scene 53_s12 with dissolve
            mc "Well... I just prefer having you as my roommate, I guess."
            scene 53_s11 with dissolve
            m "Roommate?"
            scene 53_s12 with dissolve
            mc "Yeah, friends."
            scene 53_s15 with Dissolve(1.0)
            m "But... [mx], I'm your wife."
            scene 53_s14 with dissolve
            mc "I know, I know. I guess I'm just not... sexually interested."
            mc "Not in you—don't get me wrong—just in general."
            scene 53_s13 with dissolve
            m "I-I see..."
            scene 53_s14 with dissolve
            mc "Is it okay if we keep things the way they are?"
            scene 53_s13 with dissolve
            m "O-Of course, [mx]!"
            m "Being with you has been the best thing that's happened to me in a long time. You treat me so kindly."
            scene 53_s14 with dissolve
            mc "*chuckles* That's good to hear. Anyway, I'm gonna get some rest now."
            scene 53_s11 with Dissolve(1.0)
            m "Of course. I'll be right here."
            scene 53_s12 with dissolve
            scene black with Fade(1.0,1.0,1.0)
            sensation "The world fades into a quiet haze as you lean your head back, sleep pulling you under."
            scene black with Fade(1.5,1.0,1.0)
            jump scene54

        else:
            mc "Something on your mind?"
            m "..."
            scene 53_s11 with dissolve
            m "Uhh... I... The princess..."
            scene 53_s12 with dissolve
            mc "Rebecca? What about her? Did she mistreat you?"
            scene 53_s11 with dissolve
            m "No, no! She... she walked in on me... doing... it."
            scene 53_s12 with dissolve
            mc "It?"
            scene 53_s11 with dissolve
            m "Y-You know..."
            scene 53_s12 with dissolve
            mc "Oh."
            m "..."
            mc "Did she say something?"
            scene 53_s11 with dissolve
            m "She just... left. She didn't say anything. But ever since then... I—I can't even look her in the eyes!"
            scene 53_s12 with dissolve
            mc "That's... unfortunate."
            mc "Why were you doing it anyway?"
            scene 53_s13 with dissolve
            m "Because! B-Because you were away for so long, [mx]..."
            scene 53_s14 with dissolve
            mc "I see..."
            mc "Were you thinking of me?"
            scene 53_s13 with dissolve
            m "Y-Yes..."
            scene 53_s14 with dissolve
            mc "What did you do?"
            scene 53_s15 with dissolve
            m "It's embarrassing!"
            scene 53_s14 with dissolve
            mc "Come on... Tell me."
            scene 53_s13 with dissolve
            m "Umm... I grabbed a banana..."
            scene 53_s14 with dissolve
            mc "*laughs* A banana?!"
            scene 53_s15 with dissolve
            m "S-Stop laughing!"
            scene 53_s14 with dissolve
            mc "Alright, alright. Go on."
            scene 53_s13 with dissolve
            m "I put it... inside me..."
            scene 53_s14 with dissolve
            mc "In your pussy?"
            scene 53_s13 with dissolve
            m "Mmm... It reminded me of you."
            if maia_pussy_sex > maia_anal_sex:
                m "The way you... s-stretch me... reach so deep inside..."
            elif maia_anal_sex > maia_pussy_sex:
                m "The way you... a-always stretch my butthole..."
            scene 53_s14 with dissolve
            mc "You really missed me, huh?"
            scene 53_s13 with dissolve
            m "I couldn't help it..."
            scene 53_s14 with dissolve
            mc "I assume you didn't get to finish when Rebecca walked in?"
            scene 53_s13 with dissolve
            m "No..."
            m "S-So...?"
            scene 53_s14 with dissolve
            call screen scene53_choice01 with dissolve
    else:
        scene 53_s39 with Fade(1.0,0.5,0.5)
        perception "The room lies exactly as you left it—quiet, still, untouched. The emptiness presses in around you."
        mc "I'm so tired..."
        mc "How long was I even gone? I can't even remember anymore..."
        mc "Whatever... Guess I'll take a nap."
        scene black with Fade(1.0,1.0,1.0)
        perception "The soft rhythm of your breath fills the empty space as you drift into a restless sleep."
        jump scene54

label scene53_choice01_op1:
    $ maia_virgin = False
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p5_replay:
        $ persistent.scene3_p5_replay = True
    mc "Let's do it properly, then."
    scene 53_s13 with dissolve
    m "[mx]... Really?"
    scene 53_s14 with dissolve
    mc "Mhm. No interruptions this time. Come here."
    scene 53_s16 with dissolve
    play sound "se_sfx/blowjob/kiss1.mp3" 
    m "Mmmm~"
    sensation "Her lips press softly against yours at first—warm, delicate. But soon, her mouth opens, her breath quickening as she melts into you."
    scene 53_s17 with dissolve
    play sound "se_sfx/lick/lick1.mp3" 
    m "[mx]..."
    sensation "Her tongue slips into your mouth, shy at first, then bolder, exploring and curling around your own."
    scene 53_s18 with dissolve
    m "[mx]... I feel really hot..."
    scene 53_s19 with dissolve
    call screen scene53_choice02 with dissolve

label scene53_choice02_op1:
    mc "Come here."
    scene 53_s16 with dissolve
    play sound "se_sfx/blowjob/kiss2.mp3" 
    sensation "You pull her closer, your lips crashing together once more. This time, her kiss is sloppy, hungry—her saliva coats your lips and chin as she moans into your mouth."
    m "Mhnnn~ [mx]..."
    scene 53_s17 with dissolve
    play sound "se_sfx/lick/lick1.mp3" 
    sensation "She kisses you passionetly. A sloppy kiss. Her saliva coats your lips."
    scene 53_s18 with dissolve
    m "I-I can feel it dripping down there already~"
    scene 53_s19 with dissolve
    call screen scene53_choice02 with dissolve

image 53_bj1 = Movie(play="images/4_chapter3/scene53/53_bj1.webm", loop=True)
image 53_bj1_faster = Movie(play="images/4_chapter3/scene53/53_bj1_faster.webm", loop=True)
image 53_bj2 = Movie(play="images/4_chapter3/scene53/53_bj2.webm", loop=True)
image 53_bj2_faster = Movie(play="images/4_chapter3/scene53/53_bj2_faster.webm", loop=True)

label scene53_maia:
    $ maia_mouth_virgin = False
    stop music fadeout 2.0
    scene 53_s18 with dissolve
    m "Let me pleasure you with my mouth, [mx]~"
    scene 53_s19 with dissolve
    scene 53_s20 with Dissolve(1.0)
    sensation "Her eyes widen slightly as your shaft springs free. She lowers herself eagerly, wrapping her lips around your tip with a soft moan."
    m "Mmmhnnn..."
    show 53_bj1 with Dissolve(1.0)
    $ scene53_bj1 = True
    sensation "She slowly takes you deeper, inch by inch, her throat tight and quivering around your cock. You can feel her breathing through her nose, steady but excited."
    m "Nnnf... m-mhmm..."
    perception "Her rhythm builds as she slides back and forth, her drool now coating you completely. The wet sounds of her eager mouth fill the room, blending with her soft, needy moans."
    call screen scene53_maia1 with dissolve
    
label scene53_bj1:
    $ scene53_bj1 = True
    $ scene53_bj2 = False
    $ scene53_bj_speed = False
    scene black with Dissolve(0.3)
    show 53_bj1 with dissolve
    m "*slurp* Hgnnn~ *suck*"
    call screen scene53_maia1 with dissolve

label scene53_bj2:
    $ scene53_bj1 = False
    $ scene53_bj2 = True
    $ scene53_bj_speed = False
    scene black with Dissolve(0.3)
    show 53_bj2 with dissolve
    m "Mmmmm~ *slurp*"
    call screen scene53_maia1 with dissolve

label scene53_bj_faster:
    scene black with Dissolve(0.3)
    $ scene53_bj_speed = True
    if scene53_bj1:
        show 53_bj1_faster with dissolve
        hide 53_bj1
    else:
        show 53_bj2_faster with dissolve
        hide 53_bj2
    sensation "Her movements quicken, her head bobbing with enthusiasm. Each wet slurp echoes louder as her tongue presses firmly against the underside of your cock with every stroke. Her cheeks hollow as she sucks you harder."
    m "Mfhmmm~"
    call screen scene53_maia1 with dissolve

label scene53_bj_slower:
    mc "Slow down. Take your time."
    scene black with Dissolve(0.3)
    $ scene53_bj_speed = False
    if scene53_bj1:
        show 53_bj1 with dissolve
        hide 53_bj1_faster
    else:
        show 53_bj2 with dissolve
        hide 53_bj2_faster
    m "Mhmm~"
    sensation "She eases her pace, letting your cock glide slowly between her lips. Her tongue traces every inch with care, swirling in slow, deliberate circles."
    call screen scene53_maia1 with dissolve

label scene53_bj_cum:
    sensation "The pressure builds quickly. Her sloppy sounds grow louder, and her throat suddenly tightens up as she anticipates your climax."
    mc "Maia... I'm close!"
    m "Mmmnn!~"
    show screen cum
    scene 53_s21 with vpunch
    play sound "se_sfx/blowjob/gag1.mp3"
    sensation "With a final sharp thrust into her eager mouth, you erupt deep inside her throat. Thick, hot pulses of your seed coat her insides as her throat contracts, swallowing instinctively around you."
    mc "Ahh! Keep doing that with your tongue!"
    scene 53_s21 with vpunch
    play sound "se_sfx/blowjob/blowjob_cum1.mp3"
    m "Hgnn~!"
    scene 53_s22 with Dissolve(0.7)
    mc "Swallow all of it."
    hide screen cum
    play sound "se_sfx/blowjob/swallow2.mp3"
    m "*gulp*... *gulp*... *gulp*..."
    scene 53_s23 with Dissolve(1.0)
    m "Ahhn~"
    m "All gone~"
    scene 53_s24 with dissolve
    m "D-Did I do well... [mx]?"
    scene 53_s25 with dissolve
    mc "Hah... hahh... Yes. You're getting really good at this."
    scene 53_s24 with dissolve
    m "Hehe~ I'm glad I can make you feel good."
    m "My... pussy is dripping a lot, [mx]~"
    scene 53_s25 with dissolve
    mc "Show me."
    scene black with Fade(0.5,0.5,0.5)
    perception "Maia leans back slightly, her fingers reaching for the waistband of her panties. With trembling hands, she slides them down her thighs, exposing herself fully to you."
    scene 53_s27 with Fade(0.5,0.5,0.5)
    m "..."
    perception "Her glistening folds pulse softly, the clear sheen of her arousal coating her inner lips. A faint stream trickles down the curve of her thigh, proof of just how worked up she's become."
    call screen scene53_choice03 with dissolve

label scene53_choice03_op1:
    scene 53_s30 with Dissolve(1.0)
    play sound "se_sfx/rubbing4.mp3"
    perception "Your thumb brushes lightly over her sensitive clitoris, drawing a soft moan from her lips. Her hips twitch in response, desperate for more contact."
    m "Hhng! [mx]... P-Please... I want you inside..."
    scene 53_s27 with Dissolve(1.0)
    call screen scene53_choice03 with dissolve

label scene53_choice03_op2:
    scene 53_s29 with Dissolve(1.0)
    play sound "se_sfx/masturbate_female/1_masturbate.mp3"
    perception "You reach out, spreading her folds apart with your fingers. The delicate pink flesh parts eagerly, her heat radiating against your hand. The wetness clings to your fingertips in long, sticky strands as her body shudders under your touch."
    m "Ahh~ It feels so warm when you touch me there..."
    scene 53_s27 with Dissolve(1.0)
    call screen scene53_choice03 with dissolve

label scene53_choice03_op3:
    mc "Spread your legs."
    scene 53_s28 with Dissolve(1.0)
    perception "She spreads her legs wider, presenting her hole to you, trembling with anticipation. Her flushed face, heavy breaths, and glistening wet folds practically beg for you to claim her."
    m "Mmm..."
    call screen scene53_choice03 with dissolve

image 53_sex1 = Movie(play="images/4_chapter3/scene53/53_sex1.webm", loop=True)
image 53_sex1_faster = Movie(play="images/4_chapter3/scene53/53_sex1_faster.webm", loop=True)
image 53_sex2 = Movie(play="images/4_chapter3/scene53/53_sex2.webm", loop=True)
image 53_sex2_faster = Movie(play="images/4_chapter3/scene53/53_sex2_faster.webm", loop=True)

image 53_sex1_a = Movie(play="images/4_chapter3/scene53/53_sex1_a.webm", loop=True)
image 53_sex1_a_faster = Movie(play="images/4_chapter3/scene53/53_sex1_a_faster.webm", loop=True)
image 53_sex2_a = Movie(play="images/4_chapter3/scene53/53_sex2_a.webm", loop=True)
image 53_sex2_a_faster = Movie(play="images/4_chapter3/scene53/53_sex2_a_faster.webm", loop=True)

label scene53_maia2:
    scene 53_s27 with Dissolve(1.0)
    if maia_pussy_sex > maia_anal_sex:
        mc "Come here. I'll make sure to stretch your pussy really well."
        scene 53_s26 with dissolve
        m "Y-Yes!"
        scene 53_s42 with Fade(0.5,0.5,0.5)
        perception "Maia straddles you carefully, her knees pressing into the couch as she aligns herself above your erect cock. Her breath grows heavier, her chest rising and falling rapidly."
        scene 53_s43 with Dissolve(1.0)
        sensation "The heat radiating from her dripping folds sends a pulse through your shaft as she hovers just above the tip. You feel the faint, slippery tease of her entrance brushing against you."
        m "You're... so big, [mx]..."
        show 53_sex1 with dissolve
        sensation "The soft, yielding flesh parts as she begins to sink down, inch by inch. Warmth engulfs you, her inner walls hugging your cock tightly as she gasps softly."
        m "A-ahh~ [mx]!"
        m "Am I squeezing you well, [mx]?"
        mc "You're really tight!"
        perception "She starts to move, lifting herself slightly before easing back down. Her breasts bounce gently with every motion, her moans growing louder with each descent."
        m "Ahh... nghh... y-you're stretching me so good~"
        perception  "Her soaked walls cling and slide against your cock with every motion. The slick sounds of her juices mixing with your thrusts fill the room, as her rhythm grows faster and needier."
        call screen s53_sex with dissolve

    elif maia_anal_sex > maia_pussy_sex:
        $ s53_asex1 = True
        $ s53_asex2 = False
        $ s53_vsex1 = False
        $ s53_vsex2 = False
        mc "Come here. I'll make sure to stretch your ass really well."
        scene 53_s26 with dissolve
        m "Y-Yes!"
        scene 53_s42 with Fade(0.5,0.5,0.5)
        perception "Maia carefully positions her soft round ass on top of your cock, her face flushed crimson."
        m "A-Alright... I'm ready..."
        scene 53_s44 with Dissolve(1.0)
        sensation "Her tight ring resists at first, but with gentle persistence, you feel her slowly begin to yield. The tight warmth wraps around your cock, each inch sinking deeper as her breath catches."
        show 53_sex2_a with dissolve
        m "A-Ahh! Nghh~ I can feel... e-every bit of you..."
        sensation "The pressure inside her is unbelievable—warm, tight, like a velvet vise squeezing your shaft. She pauses for a moment, adjusting to the intense sensation."
        mc "God..."
        show 53_sex1_a with dissolve
        hide 53_sex2_a 
        perception "Once fully seated, Maia begins to rock her hips. With each rise and fall, her tight hole stretches and slides around you, her breathy moans filling the room."
        m "Nghh~! I-It always makes me feel so... full..."
        perception "Her ass jiggles slightly with every motion, and the snug pressure keeps your shaft firmly embraced at every angle. Wet, sticky sounds of her dripping folds below join the chorus of pleasure."
        $ s53_asex_first = False
        call screen s53_sex with dissolve

    else:
        if maia_pussy_virgin:
            mc "This will be your first time, right? Come here, let me finally stretch your pussy."
            $ maia_pussy_virgin = False
            scene 53_s26 with dissolve
            m "Y-Yes! I've been waiting for this for so long!"
        else:
            mc "Come here. I'll make sure to stretch your pussy really well."
            scene 53_s26 with dissolve
            m "Y-Yes!"
        scene 53_s42 with Fade(0.5,0.5,0.5)
        perception "Maia straddles you carefully, her knees pressing into the couch as she aligns herself above your erect cock. Her breath grows heavier, her chest rising and falling rapidly."
        scene 53_s43 with Dissolve(1.0)
        sensation "The heat radiating from her dripping folds sends a pulse through your shaft as she hovers just above the tip. You feel the faint, slippery tease of her entrance brushing against you."
        m "You're... so big, [mx]..."
        show 53_sex1 with dissolve
        sensation "The soft, yielding flesh parts as she begins to sink down, inch by inch. Warmth engulfs you, her inner walls hugging your cock tightly as she gasps softly."
        m "A-ahh~ [mx]!"
        m "Am I squeezing you well, [mx]?"
        mc "You're really tight!"
        perception "She starts to move, lifting herself slightly before easing back down. Her breasts bounce gently with every motion, her moans growing louder with each descent."
        m "Ahh... nghh... y-you're stretching me so good~"
        perception  "Her soaked walls cling and slide against your cock with every motion. The slick sounds of her juices mixing with your thrusts fill the room, as her rhythm grows faster and needier."
        call screen s53_sex with dissolve

label s53_sex1:
    $ s53_speed = False
    if s53_vsex1 or s53_vsex2:
        $ s53_vsex1 = True
        $ s53_vsex2 = False
        scene black with Dissolve(0.3)
        show 53_sex1 with dissolve
        m "Hah~ [mx]... Ahhhnn~"
        call screen s53_sex with dissolve
    elif s53_asex1 or s53_asex2:
        $ s53_asex1 = True
        $ s53_asex2 = False
        if s53_asex_first:
            if maia_anus_virgin:
                $ maia_anus_virgin = False
                mc "I've been waiting to finally take your ass virginity."
                m "M-My ass?"
                mc "You don't want to?"
                m "N-No, it's fine! Any of my holes are yours to use as you please, [mx]~"
                mc "Good girl."
            else:
                mc "I want to feel your ass."
                m "...You really like doing it in my butt, [mx]."
                mc "You don't want to?"
                m "I do! I'm starting to... really like it too~"
                mc "Good girl."
            scene 53_s44 with Dissolve(1.0)
            perception "Maia carefully positions her soft round ass on top of your cock, her face flushed crimson."
            m "A-Alright... I'm ready..."
            show 53_sex2_a with dissolve
            perception "She bites her lower lip, breathing deeply as she slowly begins to lower herself onto you."
            sensation "Her tight ring resists at first, but with gentle persistence, you feel her slowly begin to yield. The tight warmth wraps around your cock, each inch sinking deeper as her breath catches."
            m "A-Ahh! Nghh~ I can feel... e-every bit of you..."
            sensation "The pressure inside her is unbelievable—warm, tight, like a velvet vise squeezing your shaft. She pauses for a moment, adjusting to the intense sensation."
            mc "God..."
            show 53_sex1_a with dissolve
            hide 53_sex2_a 
            perception "Once fully seated, Maia begins to rock her hips. With each rise and fall, her tight hole stretches and slides around you, her breathy moans filling the room."
            m "Nghh~! I-It always makes me feel so... full..."
            perception "Her ass jiggles slightly with every motion, and the snug pressure keeps your shaft firmly embraced at every angle. Wet, sticky sounds of her dripping folds below join the chorus of pleasure."
            $ s53_asex_first = False
            call screen s53_sex with dissolve
        else:
            scene black with Dissolve(0.3)
            show 53_sex1_a with dissolve
            m "Gah! Agh! Mhhnn..."
            m "You're poking my insides, [mx]~"
            call screen s53_sex with dissolve

label s53_sex2:
    $ s53_speed = False
    if s53_vsex1 or s53_vsex2:
        scene black with Dissolve(0.3)
        show 53_sex2 with dissolve
        $ s53_vsex1 = False
        $ s53_vsex2 = True
        m "Ahhhh~ Yes! I-I want you deeper, [mx]~!"
        call screen s53_sex2 with dissolve
    elif s53_asex1 or s53_asex2:
        $ s53_asex1 = False
        $ s53_asex2 = True
        if s53_asex_first:
            if maia_anus_virgin:
                $ maia_anus_virgin = False
                mc "I've been waiting to finally take your ass virginity."
                m "M-My ass?"
                mc "You don't want to?"
                m "N-No, it's fine! Any of my holes are yours to use as you please, [mx]~"
                mc "Good girl."
            else:
                mc "I want to feel your ass."
                m "...You really like doing it in my butt, [mx]."
                mc "You don't want to?"
                m "I do! I'm starting to... really like it too~"
                mc "Good girl."
            scene 53_s44 with Dissolve(1.0)
            perception "Maia carefully positions her soft round ass on top of your cock, her face flushed crimson."
            m "A-Alright... I'm ready..."
            show 53_sex2_a with dissolve
            perception "She bites her lower lip, breathing deeply as she slowly begins to lower herself onto you."
            sensation "Her tight ring resists at first, but with gentle persistence, you feel her slowly begin to yield. The tight warmth wraps around your cock, each inch sinking deeper as her breath catches."
            m "A-Ahh! Nghh~ I can feel... e-every bit of you..."
            sensation "The pressure inside her is unbelievable—warm, tight, like a velvet vise squeezing your shaft. She pauses for a moment, adjusting to the intense sensation."
            mc "God..."
            show 53_sex1_a with dissolve
            hide 53_sex2_a 
            perception "Once fully seated, Maia begins to rock her hips. With each rise and fall, her tight hole stretches and slides around you, her breathy moans filling the room."
            m "Nghh~! I-It always makes me feel so... full..."
            perception "Her ass jiggles slightly with every motion, and the snug pressure keeps your shaft firmly embraced at every angle. Wet, sticky sounds of her dripping folds below join the chorus of pleasure."
            show 53_sex2_a with dissolve
            hide 53_sex1_a 
            $ s53_asex_first = False
            call screen s53_sex with dissolve
        else:
            $ s53_asex1 = False
            $ s53_asex2 = True
            scene black with Dissolve(0.3)
            show 53_sex2_a with dissolve
            #m "Ahhhh~"
            #sensation "She slowly lowers herself, letting her tight anus stretch around your cock. Soft whimpers escape her lips as she struggles to take you in."
            mc "Fuck, you're so tight!."
            m "Mhmm~ [mx]! Please... Don't hold back~"
            call screen s53_sex2 with dissolve

label s53_faster:
    scene black with Dissolve(0.3)
    $ s53_speed = True
    if s53_vsex1:
        show 53_sex1_faster with dissolve
        hide 53_sex1 with dissolve
        m "Haahhh! Hah! Nghnnnn~"
        m "[mx]! [mx]!"
        call screen s53_sex with dissolve
    elif s53_vsex2:
        show 53_sex2_faster with dissolve
        hide 53_sex2
        m "Hah~! Mfhnnn~ D-Do you like that?"
        sensation "She desperately tries to tighten her walls as your cock sinks deeper and deeper into her."
        call screen s53_sex2 with dissolve
    elif s53_asex1:
        show 53_sex1_a_faster with dissolve
        hide 53_sex1_a
        m "Aghnn! Be rough with me, [mx]! I-I don't mind it~"
        perception "You can feel her tight hole clench around your cock. She moans louder whenever your cock reaches her colon."
        call screen s53_sex with dissolve
    elif s53_asex2:
        show 53_sex2_a_faster with dissolve
        hide 53_sex2_a
        m "It's s-so deep! [mx]!"
        call screen s53_sex2 with dissolve

label s53_slower:
    scene black with Dissolve(0.3)
    $ s53_speed = False
    if s53_vsex1:
        show 53_sex1 with dissolve
        hide 53_sex1_faster with dissolve
        m "Don't stop, [mx]~ I-I'm almost there~!"
        sensation "Juices drip from her warm pussy and land on your balls and thighs."
        call screen s53_sex with dissolve
    elif s53_vsex2:
        show 53_sex2 with dissolve
        hide 53_sex2_faster
        m "Keep staring into my eyes, [mx]~ I-It feels better w-when you do..."
        call screen s53_sex2 with dissolve
    elif s53_asex1:
        show 53_sex1_a with dissolve
        hide 53_sex1_a_faster
        m "I can feel it in my tummy, [mx]~ It feels really... g-good!"
        call screen s53_sex with dissolve
    elif s53_asex2:
        show 53_sex2_a with dissolve
        hide 53_sex2_a_faster
        m "Hahh~ Nghnn! [mx]~!"
        call screen s53_sex2 with dissolve

label s53_sex_cum:
    if s53_vsex1 or s53_vsex2:
        m "[mx]... I... I don't think I can hold it much longer!"
        mc "Me neither... Keep going, Maia."
        perception "Her hips slap down against your pelvis in frantic rhythm, her wet walls tightening even more with every bounce. The lewd, sticky sounds grow louder, filling the room."
        m "A-Ahhn! Y-You're hitting my womb... a-again and again~"
        sensation "Your cock throbs inside her, the heat building to an unbearable peak. Her soaked insides clutch you desperately, as if begging to be filled."
        mc "I'm... I'm going to cum, Maia!"
        m "Inside! Inside me, [mx]! Fill my womb!"
        show screen cum
        play sound "se_sfx/sex/sex_cum3.mp3"
        if persistent.xray_mode:
            scene 53_s33_xray1 with vpunch
            sensation "With one final desperate thrust, you slam into her fully. A wave of intense release surges through you as you erupt deep inside her. Warm, thick seed floods her welcoming depths, coating every inch of her spasming walls."
            scene 53_s33_xray2 with vpunch
            play sound "se_sfx/sex/sex_cum2.mp3"
            m "M-Mhnn~ S-So warm... I can feel it filling me~!"
            scene 53_s34_xray3 with Dissolve(1.0)
        else:
            scene 53_s33 with vpunch
            sensation "With one final desperate thrust, you slam into her fully. A wave of intense release surges through you as you erupt deep inside her. Warm, thick seed floods her welcoming depths, coating every inch of her spasming walls."
            scene 53_s33 with vpunch
            play sound "se_sfx/sex/sex_cum2.mp3"
            m "M-Mhnn~ S-So warm... I can feel it filling me~!"
            scene 53_s34 with Dissolve(1.0)
        if not maia_pregnant:
            call pregnancy_check_maia from __call_pregnancy_check_maia
        play sound "se_sfx/sex/touch4.mp3" 
        hide screen cum
        m "S-So much... You filled me up, [mx]~ Did it feel that good?"
    elif s53_asex1 or s53_asex2:
        sensation "Her hips rock faster now, her tight ring stretching around you with every deep stroke. The slippery wetness from her folds below drips freely onto your thighs, mixing with your sweat."
        m "A-Ahhhn! I-It feels s-so... strange but... g-good~!"
        mc "I'm getting close, Maia..."
        m "Nnhh~! I-I'm... ready... ejaculate in me, [mx]!"
        show screen cum
        play sound "se_sfx/sex/sex_cum1.mp3"
        scene 53_s31 with vpunch
        sensation "Your release builds to an explosive peak. With a final sharp thrust upward, you bury yourself completely. Your cock pulses inside her tight, stretched hole, pumping thick, hot streams of semen deep into her bowels."
        scene 53_s31 with vpunch
        play sound "se_sfx/sex/sex_cum4.mp3"
        m "S-So much... I can feel it all inside me~..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 53_s32 with Dissolve(1.0)
        hide screen cum
        m "Hahh... hah... [mx]... I can feel your seed in my stomach~ I hope you enjoyed having sex with my butt~"
    $ renpy.end_replay()

label scene53_after:
    scene 53_s35 with Fade(1.5,1.0,1.0)
    mc "Hahh..."
    m "Ahh~ Hah~ T-That was... wonderful, [mx]."
    m "I really missed this feeling... being this close to you~"
    scene 53_s36 with dissolve
    mc "Me too, Maia."
    scene 53_s35 with dissolve
    m "I'm so tired... but so happy..."
    scene 53_s37 with dissolve
    m "Mmm..."
    mc "Maia?"
    mc "Guess I'll take a nap too."
    sensation "The world fades into a quiet haze as you lean your head back, sleep pulling you under."
    scene black with Fade(1.5,1.0,1.0)
    jump scene54

label scene53_choice01_op2:
    mc "I can't right now, Maia. I'm too tired, remember?"
    scene 53_s13 with dissolve
    m "O-Of course! I wasn't thinking... it's fine."
    scene 53_s11 with dissolve
    m "Just rest. I'll be right here."
    scene 53_s12 with dissolve
    sensation "The world fades into a quiet haze as you lean your head back, sleep pulling you under."
    scene black with Fade(1.5,1.0,1.0)
    jump scene54

label scene54:
    "*knock* *knock* *knock*"
    if not mc_maia_left:
        scene 53_s40 with Fade(0.5,0.5,0.5)
        mc "Hmm?"
        m "*yawn* Did you invite someone [mx]?"
        mc "No..."
        scene 53_s41 with Fade(0.5,0.5,0.5)
        mc "Who's there?"
        guard "I apologize for the intrusion, sir. The Queen requests your presence immediately."
        mc "The Queen? Alright... I'm coming."
        m "Is something wrong, [mx]?"
        mc "Hopefully not. Stay here. I'll be back soon."
        m "As you wish..."
    else:
        mc "*yawn* Hmm?"
        scene 53_s41 with Fade(0.5,0.5,0.5)
        mc "Someone there?"
        guard "I apologize for the intrusion, sir. The Queen requests your presence immediately."
        mc "The Queen? Alright... I'm coming."
    scene 54_s2 with Fade(1.0,1.0,1.0)
    play music "queen2.mp3" fadein 3.0 volume 0.5 loop
    perception "You step into the grand courtroom. Tension crackles in the air. The Queen sits tall upon her throne, her eyes locked on a man standing below—cloaked in foreign colors. A handful of guards watch silently."
    scene 54_s3 with Dissolve(1.0)
    amb "Someone must answer for this— now!"
    scene 54_s4 with dissolve
    q "I understand your frustration, Ambassador, but you will mind your tone in {i}my{/i} throne room."
    q "[mc]. Approach."
    mc "..."
    scene 54_s6 with Dissolve(1.0)
    mc "Yes, Your Majesty?"
    scene 54_s5 with dissolve
    q "A terrible incident has taken place, [mc]. The manor of the Queen of pleasure has been burned to the ground. Many lives were lost."
    scene 54_s6 with dissolve
    mc "That's... tragic. But forgive me, I don't see how this involves your kingdom directly?"
    scene 54_s5 with dissolve
    q "It seems she was under the protection of our neighbors in Nahraya."
    scene 54_s7 with dissolve
    amb "Am I invisible here, Your Majesty?! Must I stand idly while you whisper amongst yourselves?"
    scene 54_s9 with Dissolve(0.7)
    amb "I shall reiterate—King Hod is enraged beyond words!"
    scene 54_s10 with dissolve
    q "I will address this, Ambassador. I have already taken action against those involved."
    scene 54_s9 with dissolve
    amb "That will not suffice! The King demands their heads delivered to him on horseback!"
    scene 54_s8 with dissolve
    q "Silence! You do not command me. I have stated my position. Inform your king that I am handling it. Let him keep his patience—for both our sakes."
    scene 54_s7 with dissolve
    amb "Your Majesty, neither I nor my king wish for any conflict. But you know his temper well."
    scene 54_s8 with dissolve
    q "Grant me time. I will resolve this, personally."
    scene 54_s3 with Dissolve(0.8)
    amb "Why do you protect the identities of these criminals? Reveal them and we end this {i}now.{/i}"
    scene 54_s4 with dissolve
    q "It is not so simple. And I will not repeat myself. You may take your leave, Ambassador. I appreciate your visit."
    scene 54_s7 with Dissolve(0.8)
    amb "We are watching, Your Majesty."
    scene 54_s8 with dissolve
    q "*sigh* Just when I thought fortune had finally favored us... it all threatens to unravel."
    q "[mc]."
    scene 54_s7 with dissolve
    mc "Yes, Your Majesty?"
    scene 54_s8 with dissolve
    q "We have interrogated a mercenary—Kathrine. Darius informed me she returned with you."
    scene 54_s7 with dissolve
    mc "That's-"
    scene 54_s5 with dissolve
    q "Do {i}not{/i} interrupt me."
    scene 54_s6 with dissolve
    mc "..."
    scene 54_s5 with dissolve
    q "She confessed everything. How Lord Reiner coerced her and Gaius into carrying out that massacre."
    q "You have no idea how relieved I was when she spoke nothing of your involvement, [mc]."
    scene 54_s6 with dissolve
    mc "Thank you. And if I may ask... what about Gaius?"
    scene 54_s5 with dissolve
    q "*sigh* As much as I hate to admit it... he's too important right now, [mc]."
    scene 54_s6 with dissolve
    mc "...Isn't that unfair?"
    scene 54_s5 with dissolve
    q "Yes. Deeply unfair. But I need his protection more than ever. So for now, he'll get off lightly."
    q "But only for now. I promise, I'll deal with him when the time is right."
    scene 54_s6 with dissolve
    mc "That's good to hear."
    scene 54_s5 with dissolve
    q "Regardless, you've continued to prove yourself—far beyond what I ever expected."
    q "As you witnessed—this kingdom teeters on the edge... again. And now, I must depart to confront Reiner directly."
    q "We need their resources, yes. But I will not allow this alliance to drag us into war. That price is too high."
    scene 54_s5 with dissolve
    q "Tell me, [mc]. If you were in my place... what would you do?"
    scene 54_s6 with dissolve
    mc "Me? Well..."
    call screen scene54_choice01 with dissolve

label scene54_choice01_op2:
    $ mc_suggest_war = True
    mc "Reiner directly mocked you, Your Majesty. This should not go unanswered."
    mc "If I were in your position, I'd march to war."
    scene 54_s11 with dissolve
    q "*chuckles* You truly have no grasp of the full weight of this, do you, [mc]?"
    q "Even if we scraped together every able-bodied man, armed peasants with pitchforks and hope... we wouldn't make it to their gates."
    scene 54_s12 with dissolve
    mc "I see..."
    jump scene54_2
    
label scene54_choice01_op1:
    $ mc_suggest_peace = True
    mc "Like you said yourself—things are fragile enough as they are. A war would break what little remains of this kingdom."
    scene 54_s5 with dissolve
    q "Indeed. But sadly, it's never as simple as shaking hands and parting ways."
    q "Reiner's pride. Nahraya's demands. Every path forward is lined with thorns."
    scene 54_s6 with dissolve
    mc "I trust your judgment, Your Majesty. If anyone can do this, it's you."
    scene 54_s11 with dissolve
    q "Oh my... careful with such flattery, [mc]. You're raising my expectations of you."
    jump scene54_2

label scene54_choice01_op3:
    $ mc_suggest_leverage = True
    mc "Use Reiner's guilt to your advantage. Control him. Let him serve us even more while he desperately tries to avoid exposure."
    mc "Placate Nahraya, preserve the alliance, and strengthen your grip."
    scene 54_s5 with dissolve
    q "Oh? I didn't expect such cunning from you, [mc]. Coerce the coerced, is that it?"
    q "You would make quite the ruler someday..."
    scene 54_s12 with dissolve
    mc "We resolve tensions with Nahraya, and extract even more from Eurina at the same time."
    scene 54_s11 with dissolve
    q "Now that... is real power. Sometimes, those who owe you serve far better than those you punish."
    jump scene54_2
    
label scene54_2:
    $ free_roam_reb_first = False
    scene 54_s5 with Dissolve(1.0)
    q "*sigh* I suppose time will tell how this all unfolds."
    q "But for now, my course is set. Regarding your position, [mc], I need you here in Irda."
    q "I can think of no one better to serve as temporary steward in my absence."
    scene 54_s6 with dissolve
    mc "Steward? Your Majesty, that's a big responsibility..."
    scene 54_s5 with dissolve
    q "It is. And one you will bear. But that is not all." 
    q "Our discussion yesterday was not mere contemplation. I will be wedding you to my daughter, Rebecca."
    scene 54_s6 with dissolve
    mc "You... you were actually serious?"
    scene 54_s5 with dissolve
    q "Yes."
    scene 54_s6 with dissolve
    mc "...Are you sure, Your Majesty? This is... sudden"
    scene 54_s5 with dissolve
    q "I am certain. Trust is a rarer currency than gold, and there are few in this court I trust as I have come to trust you."
    q "Beyond that... she is isolated here. Her personality makes it difficult for her to form connections, and others are often too intimidated or irritated to try."
    q "Other than Maia, she barely has anyone else to speak to."
    scene 54_s11 with dissolve
    q "I am not just giving you her hand. I am asking you to be her shield."
    q "With Nahrayan spies likely to become more bold in my absence, I need to know she has a man she can rely on. A man who will protect her with his life."
    scene 54_s12 with dissolve
    call screen scene54_choice00 with dissolve
    mc "Thank you, Your Majesty. I... will."
    scene 54_s11 with dissolve
    q "Think nothing of it. Preparations will be made. I will part at dawn."
    scene 54_s12 with dissolve
    mc "Who will oversee Irda while you're gone?"
    scene 54_s11 with dissolve
    q "My younger sister, Avery. You have yet to meet her, I believe."
    scene 54_s12 with dissolve
    mc "You have a sister?"
    scene 54_s11 with dissolve
    q "The most capable in Irda. Behind me of course."
    q "You'll work with her closely."
    scene 54_s12 with dissolve
    mc "I understand."
    scene 54_s11 with dissolve
    q "I will handle the marriage contracts. In the meantime, visit Rebecca in her quarters. I already talked to her about you but speak with her. Reassure her."
    scene 54_s5 with dissolve
    q "But, [mc]... do not lie with her yet."
    scene 54_s6 with dissolve
    mc "May I ask why, Your Majesty?"
    scene 54_s5 with dissolve
    q "What would the people say if they saw their future princess with child before the wedding? No, [mc], we must make this union public first, properly."
    q "Once it is done, you'll have my blessing in full."
    scene 54_s6 with dissolve
    mc "As you wish, Your Majesty."
    stop music fadeout 2.0 
    scene 54_s14 with Fade(1.0,1.0,1.5)
    "*knock* *knock*"
    scene 54_s15 with dissolve
    r "What? Who is it?"
    mc "Rebecca, it's me. [mc]."
    r "What do you want?"
    mc "Could you open the door? It's hard to talk through solid wood."
    r "Why should I? State your business."
    mc "Please..."
    scene 54_s16 with Dissolve(1.0)
    r "Well?"
    scene 54_s17 with dissolve
    mc "Hey. Your mo... *ahem* Her Majesty, she—"
    scene 54_s16 with dissolve
    r "I know. She told me."
    scene 54_s17 with dissolve
    mc "Great! So..."
    r "..."
    mc "May I come in?"
    if not mc_reb_works_for_me and not mc_kissed_reb_foot and not mc_friend_reb:
        scene 54_s16 with dissolve
        r "Can you?"
        scene 54_s17 with dissolve
        mc "..."
        scene 54_s16 with dissolve
        r "*sigh* ...Fine. Just... come in."
        scene 54_s17 with dissolve
        jump scene54_3

    elif mc_reb_works_for_me:
        scene 54_s16 with dissolve
        r "Can you?"
        scene 54_s17 with dissolve
        mc "..."
        scene 54_s16 with dissolve
        r "*sigh* ...Fine. Just... come in."
        scene 54_s17 with dissolve
        jump scene54_3

    elif mc_friend_reb and mc_kissed_reb_foot:
        scene 54_s16 with dissolve
        r "Come on, you weirdo."
        scene 54_s17 with dissolve
        mc "Weirdo?"
        scene 54_s16 with dissolve
        r "You kissed my foot, remember?"
        scene 54_s17 with dissolve
        mc "Ah, right..."
        jump scene54_3

    else:
        scene 54_s16 with dissolve
        r "You refused my request last time. Why should I let you in now?"
        scene 54_s17 with dissolve
        mc "Are you still holding onto that?"
        scene 54_s16 with dissolve
        r "I am."
        scene 54_s17 with dissolve
        mc "But you said we were friends... *sigh* Is there anything I can do that... doesn't involve me kissing your foot?"
        scene 54_s16 with dissolve
        r "*sigh* Times have changed, so... here."
        scene 54_s18 with dissolve
        mc "Alright! This is much more reasonable."
        call screen scene54_choice02 with dissolve

label scene54_choice00_op2:
    $ mc_rejected_wedding_reb = True
    mc "I'll protect her. I'll be her ally or friend. But... I don't want to marry her."
    scene 54_s11 with dissolve
    q "You don't? The princess of Irda. The second heir to the throne. And you refuse her hand?"
    scene 54_s12 with dissolve
    mc "I don't refuse {i}her{/i}. I refuse the marriage."
    mc "I can protect her without a ring on her finger. I can love her without some contract binding us together. At least... I think I can."
    scene 54_s11 with dissolve
    q "Hmm... It's true that the weight of a crown has a way of turning love into obligation."
    q "I wanted something different for her, but if you can't give her that, then I won't force it."
    scene 54_s5 with dissolve
    q "But your loyalty and protection are still expected, [mc]. Can you promise me that, at least?"
    scene 54_s6 with dissolve
    mc "I can. I'll keep her safe."
    scene 54_s5 with dissolve
    q "Then that will have to be enough. For now."
    q "You may return to your room."
    scene 54_s6 with dissolve
    jump scene54_000

label scene54_choice00_op3:
    $ mc_rejected_wedding_reb = True
    $ mc_angered_queen = True
    mc "Can I just have a coin reward instead?"
    scene 54_s11 with dissolve
    q "Hm? What's wrong, [mc]? I'm wedding you to my daughter—the princess of Irda, the second heir to my throne, and you're asking for coin?"
    scene 54_s12 with dissolve
    mc "I am. Don't get me wrong, I appreciate the... offer. But I don't want anything to do with that girl."
    scene 54_s5 with dissolve
    q "{i}'That girl'{/i}. You speak of my daughter as if she were a burden... I see."
    q "Return to your room, [mc]. This conversation is over."
    scene 54_s6 with dissolve
    mc "Huh? What about my reward?"
    scene 54_s5 with dissolve
    q "You won't be receiving any reward. Neither coin nor my daughter's hand. Perhaps someone out there is more deserving of this gratitude."
    q "You will remain steward for now. I won't strip you of your duties, but we will talk more about your disobedience once I return."
    q "You may leave. I have nothing more to say to you."
    scene 54_s6 with dissolve
    mc "..."
    jump scene54_000
    
label scene54_choice02_op1:
    $ free_roam_reb_first = False
    $ mc_friend_reb = True
    scene 54_s19 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    ""
    scene 54_s17 with Dissolve(0.7)
    mc "Are we good?"
    scene 54_s16 with dissolve
    r "For now."
    scene 54_s17 with dissolve
    mc "May I come in?"
    scene 54_s16 with dissolve
    r "Yes, fine."
    scene 54_s17 with dissolve
    jump scene54_3

label scene54_choice02_op2:
    $ free_roam_reb_first = False
    $ mc_friend_reb = True
    $ mc_kneel_reb = True
    $ reb_love += 10 
    scene 54_s20 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    mc "Princess."
    r "*gasp*"
    scene 54_s22 with Dissolve(0.7)
    r "Oh... Well... That was unexpected."
    scene 54_s21 with dissolve
    mc "May I come in?"
    scene 54_s22 with dissolve
    r "Yes, come in."
    scene 54_s21 with dissolve

label scene54_3:
    scene black with Fade(0.5,0.5,0.5)
    play music "reb.mp3" fadein 3.0 loop
    perception "The room is littered with books. A faint smell of floarl perfume hangs in the air."
    scene 54_s23 with Dissolve(0.8)
    mc "So... How've you been? It's been a while."
    scene 54_s24 with dissolve
    r "Fine. Nothing's changed since you left."
    scene 54_s23 with dissolve
    mc "I expected you to be happier to see me."
    scene 54_s24 with dissolve
    r "Why the hell would I? It's not like we're best friends."
    scene 54_s23 with dissolve
    mc "We aren't? After everything we've been through, I thought we'd moved a little closer."
    scene 54_s24 with dissolve
    r "...You did kind of save the kingdom. And you saved that idiot's daughter."
    scene 54_s23 with dissolve
    mc "Was that a compliment?"
    scene 54_s24 with dissolve
    r "Don't push your luck."
    scene 54_s23 with dissolve
    mc "Rebecca... how do you feel about all of this? The marriage talk. The Queen making decisions for you."
    scene 54_s24 with dissolve
    r "...I don't know. I knew I'd eventually be married off to someone... but I thought I'd have more time. More say."
    scene 54_s23 with dissolve
    mc "You should have a say."
    scene 54_s24 with dissolve
    r "Maybe. But this is how it works here. Duty first."
    r "...I didn't expect it would be {i}you{/i}, though."
    scene 54_s23 with dissolve
    mc "Is that a good or bad thing?"
    scene 54_s24 with dissolve
    r "Hmm... I haven't decided."
    scene 54_s23 with dissolve
    mc "Well, I'll try not to make your life too miserable."
    scene 54_s24 with dissolve
    r "Oh, you'd better."
    scene 54_s23 with dissolve
    mc "You know, I think we might actually make a good couple."
    scene 54_s26 with dissolve
    r "That depends... Are you good at listening?"
    scene 54_s25 with dissolve
    mc "I'm learning."
    scene 54_s26 with dissolve
    r "If that's the case then here are my demands."
    scene 54_s25 with dissolve
    mc "Demands?"
    scene 54_s24 with dissolve
    r "*ahem*. First—you can't be away from me for more than three days."
    scene 54_s23 with dissolve
    mc "Uh... I mean, sometimes it isn't my choi—"
    scene 54_s24 with dissolve
    r "Second—When we dine, you sit beside me. Not across. Beside."
    scene 54_s23 with dissolve
    mc "Okay, a little odd but... sure."
    scene 54_s24 with dissolve
    r "Third—I get to pick the name of our first child."
    scene 54_s23 with dissolve
    mc "Shouldn't we at least wait until after we—"
    scene 54_s24 with dissolve
    r "Fourth—if you want to have other mistresses or wives then you must tell me beforehand. If you cheat on me, I will gut you and leave your corpse on the castle's walls."
    scene 54_s23 with dissolve
    mc "Alright..."
    scene 54_s24 with dissolve
    r "Fifth—when I wake up grumpy, you bring me honey pastries. No questions asked."
    scene 54_s23 with dissolve
    mc "..."
    scene 54_s24 with dissolve
    r "Sixth—no sending me to the countryside whenever politics get messy. I stay here."
    scene 54_s23 with dissolve
    mc "Of course..."
    scene 54_s24 with dissolve
    r "Seventh—if we argue, you always apologize first."
    scene 54_s23 with dissolve
    mc "Alright, alright. Anything else, your highness?"
    scene 54_s26 with dissolve
    r "...For now, that'll do."
    scene 54_s25 with dissolve
    mc "(God...)"
    scene 54_s26 with dissolve
    r "You'll thank me later."
    r "You know... I'm kind of hungry right now."
    scene 54_s25 with dissolve
    mc "(Must be from all that talking.)"
    scene 54_s26 with dissolve
    r "You know what to do."
    scene 54_s25 with dissolve
    mc "Yes, Your Highness. Your personal slave— *ahem* husband will retrieve your royal meal."
    scene 54_s26 with dissolve
    r "Chop chop! Hehe~"
    scene 54_s25 with dissolve
    stop music fadeout 2.0 
    mc "(I don't know about this anymore...)"
    scene 54_s27 with Fade(1.5,1.0,1.0)
    play music "fire.mp3" fadein 3.0 loop
    mc "Hello."
    scene 54_s29 with Dissolve(0.8)
    ren "Oh! Sir, it's a pleasure to see you again."
    scene 54_s28 with dissolve
    mc "Been a while. How are things? I didn't wake you up, did I?"
    scene 54_s29 with dissolve
    ren "All good, sir. I'm usually most active at these hours. How may I help?"
    scene 54_s28 with dissolve
    mc "Uh... damn, I forgot to ask what she wants."
    scene 54_s29 with dissolve
    ren "Who are we talking about?"
    scene 54_s28 with dissolve
    mc "Rebecca. She's hungry."
    scene 54_s29 with dissolve
    ren "Ah! Don't worry. I know what she usually eats around this time."
    scene 54_s28 with dissolve
    mc "Alright. I'll count on you."
    scene 54_s30 with Fade(1.0,1.5,1.0)
    ren "Here you go, sir."
    scene 54_s31 with dissolve
    mc "All this?"
    scene 54_s30 with dissolve
    ren "*chuckles* That's the princess's usual evening portion."
    scene 54_s31 with dissolve
    mc "I see... Thank you."
    scene 54_s30 with dissolve
    ren "Of course!"
    scene 54_s31 with dissolve
    perception "Her ears perk up at your words, twitching lightly. They look soft—tempting to touch."
    call screen scene54_choice03 with dissolve

label scene54_choice03_op2:
    $ mc_pet_ren = True
    scene 54_s32 with Dissolve(0.8)
    mc "Good job, Ren."
    ren "S-Sir?! What are you...?"
    scene 54_s33 with dissolve
    empathy "She stiffens for a moment—but doesn't pull away. Her ears twitch slightly. She doesn't know how to feel about being pet."
    mc "Sorry, is this weird?"
    scene 54_s34 with dissolve
    ren "...No. I-I mean, not really."
    scene 54_s33 with dissolve
    mc "Alright. I'll be going now."
    scene 54_s34 with dissolve
    ren "...Thank you."
    scene 54_s33 with dissolve

label scene54_4:
    stop music fadeout 2.0 
    mc "(Back to her.)"
    scene 54_s35 with Fade(1.0,1.0,1.0)
    mc "I've returned, Your Highness."
    scene 54_s36 with Dissolve(0.9)
    r "Mmm? Oh, just leave it on the table. I'm almost finished here."
    mc "Sure thing."
    call screen scene54_choice04 with dissolve

label scene54_choice04_op1:
    scene 54_s37 with Dissolve(1.0)
    perception "Her panties cling tightly to her curves, the fabric drawn taut by the lazy sprawl of her legs. She either doesn't notice or doesn't care. Probably both."

label scene54_5:
    scene 54_s38 with Fade(0.5,0.5,0.5)
    play music "reb.mp3" fadein 3.0 loop
    mc "Should you be eating this much close to bed?"
    r "I don't care. Life's too short to be worrying about your weight."
    mc "Alright..."
    r "Mmm... Want some?"
    mc "It's all yours."
    r "Here. Try this."
    scene 54_s39 with dissolve
    call screen scene54_choice05 with dissolve

label scene54_choice05_op2:
    $ mc_deepthroated_glizzy = True
    mc "Thanks."
    scene 54_s40 with Dissolve(1.0)
    ""
    scene 54_s41 with vpunch
    mc "*gag* Gah! Agh—!"
    scene 54_s42 with dissolve
    mc "*cough* *cough*"
    r "HAHAHAHAHA!!"
    scene 54_s38 with Dissolve(0.8)
    mc "Oh, you...!"
    r "You should've seen your face! Priceless!"
    mc "Yeah, yeah... I'll remember this."
    r "Heh~"
    jump scene54_6

label scene54_choice05_op1:
    mc "Thanks, but I'm not hungry."
    scene 54_s38 with dissolve
    r "Suit yourself."

default in_scene54 = False
label scene54_6:
    $ in_scene54 = True
    scene 54_s43 with Fade(0.5,1.0,0.5)
    r "Hahh~ That was nice. Ren always gets it right."
    scene 54_s44 with dissolve
    mc "Good for you."
    scene 54_s43 with dissolve
    r "Oh? You're still here? Don't you have anything better to do?"
    scene 54_s44 with dissolve
    mc "...Maybe I should leave then."
    scene 54_s43 with dissolve
    r "Relax, relax. I'm joking."
    r "*yawn* Mmm... nothing's better than a full belly and a soft bed."
    scene 54_s44 with dissolve
    mc "Planning to sleep already?"
    scene 54_s43 with dissolve
    r "Mhm. You can take the couch."
    scene 54_s44 with dissolve
    mc "I thought we were supposed to sleep together? We're practically engaged now, remember?"
    scene 54_s43 with dissolve
    r "Dream on. I don't even know you that well yet."
    scene 54_s44 with dissolve
    mc "Fine. I'll sleep in my own room then—"
    scene 54_s45 with dissolve
    r "W-Wait!"
    scene 54_s46 with dissolve
    mc "What?"
    scene 54_s45 with dissolve
    r "...Y-You must sleep here!"
    r "I need to know... if you snore or not."
    scene 54_s46 with dissolve
    mc "I don't understand you..."
    r "..."
    mc "Fine."
    scene 54_s47 with Fade(1.0,0.5,0.5)
    ""
    stop music fadeout 2.0 
    scene black with Fade(1.0,1.0,1.5)
    scene 54_s48 with dissolve
    jump scene54_000

label scene54_000:
    stop music fadeout 2.0
    if not mc_rejected_wedding_reb:
        mc "*yawn* (That was painful... My neck hurts.)"
        mc "(The Queen must have left by now. I should go see who this Avery person is.)"
    else:
        if not mc_maia_left:
            scene 29_1_s51 with Fade(1.3,1.0,1.3)
            mc "*yawn* (I better get some sleep. Tomorrow I'll have to meet the Queen's sister. I wonder what kind of person she is... Hopefully less strict.)"
        else:
            scene 26_s21 with Fade(1.0,1.0,1.0)
            mc "*yawn* (I better get some sleep. Tomorrow I'll have to meet the Queen's sister. I wonder what kind of person she is... Hopefully less strict.)"
        scene 29_s1 with Fade(1.3,1.0,1.3)
        mc "(The Queen must have left by now. I should go see who this Avery lady is.)"   
    scene 55_s1 with Fade(1.0,1.5,1.0)
    play music "avery.mp3" fadein 3.0 loop
    avery "Ensure the patrols double-check the borders. No oversights. Those desert rats sure love their spies."
    guard "As you wish, Lady Avery."
    scene 55_s2 with Dissolve(1.0)
    avery "Ah. You must be [mc]. My sister spoke of you. You certainly do look like an outsider."
    scene 55_s3 with dissolve
    mc "I hope she spoke kindly."
    scene 55_s2 with dissolve
    avery "I prefer forming my own opinions."
    scene 55_s3 with dissolve
    mc "...I understand."
    scene 55_s2 with dissolve
    avery "No need to look nervous. You're not in trouble. The perpetrator has denied your involvement."
    scene 55_s3 with dissolve
    empathy "Her commanding presence is tempered by an almost curious warmth—like steel wrapped in silk. Beautiful, but dangerous."
    mc "That's reassuring. I think."
    scene 55_s2 with dissolve
    avery "I know your role, [mc]. My sister entrusted you with certain... responsibilities. For now, we'll keep it simple."
    scene 55_s4 with Dissolve(0.8)
    avery "Outside the throne room, there's a task board. The citizens often post requests and issues that don't require urgent intervention on a board outside the castle."
    avery "The steward will randomly pick a few of them and bring them there for further investigation."
    avery "I already had a guard pick some of them for you. Handle them. Prove to me you can manage the simple things before I trust you with the difficult ones. Clear?"
    scene 55_s5 with dissolve
    mc "Clear, ma'am."
    scene 55_s4 with dissolve
    avery "Oh—and [mc]?"
    scene 55_s5 with dissolve
    mc "Yes?"
    scene 55_s4 with dissolve
    avery "Try not to ruin my morning reports with complaints from citizens."
    scene 55_s3 with dissolve
    mc "I'll do my best."
    scene 55_s2 with dissolve
    avery "Do better than {i}your best.{/i} Just succeed."
    scene 55_s3 with dissolve
    mc "Understood."
    scene 55_s2 with dissolve
    avery "Good. Dismissed."
    scene 55_s3 with dissolve
    stop music fadeout 2.0 
    scene 55_s7 with Fade(1.0,1.0,1.0 )
    mc "Alright, the board..."
    scene 55_s8 with dissolve
    mc "Oh, there."
    mc "Let's see."
    play music "fire.mp3" fadein 3.0 loop
    scene 55_s9 with Dissolve(1.0)
    mc "Alright, I guess I can pick one and go from there."
    call screen update0_3_1_tasks with dissolve

label scene55_taskboard:
    play music "fire.mp3" fadein 2.0 loop
    if not in_scene54:
        $ in_scene54 = True
    $ update0_3_1_tasks_armor = False
    $ update0_3_1_tasks_massage = False
    $ update0_3_1_tasks_tax = False
    $ update0_3_1_tasks_trial = False
    $ update0_3_1_tasks_dispute = False
    $ update0_3_1_tasks = True
    if update0_3_1_tasks_counter == 5:
        scene 55_s9 with Fade(1.0,1.5,1.0)
        jump scene62
    elif update0_3_1_tasks_counter == 3 and not mc_went_date1_reb and not mc_rejected_reb_friend_date:
        scene 55_s9 with Fade(1.0,1.5,1.0)
        ""
        jump scene61
    else:
        scene 55_s9 with Fade(1.0,1.5,1.0)
        call screen update0_3_1_tasks with dissolve

label free_roam_reb_main_before:
    mc "(I guess I can take a little break...)"
    jump free_roam_reb_main

label scene56:
    $ update0_3_1_tasks_counter += 1
    mc "Yuuhi wants to test some armor? Wait... am I the one being tested on?"
    mc "Great... let's get this over with."
    stop music fadeout 2.0 
    scene 56_s1 with Fade(1.5,1.0,1.3)
    mc "Yuuhi?"
    scene 56_s2 with vpunch
    yuuhi "Eep!"
    play music "yuuhi.mp3" fadein 2.0 loop
    if not mc_harem_yuuhi:
        scene 31_s1 with Dissolve(0.8)
        yuuhi "Oh! Sir! *ahem* Execuse me, can I help you?"
        scene 31_s2 with dissolve
        mc "Sorry for scaring you. Are you alright?"
        scene 31_s1 with dissolve
        yuuhi "It's fine. I just peed a little."
        scene 31_s15 with dissolve
        yuuhi "Uhh! I-I mean..."
        scene 31_s16 with dissolve
        mc "..." 
        mc "Anyway... I'm here because of your request."
        scene 31_s1 with dissolve
        yuuhi "Oh, haha, I see!"
    else:
        yuuhi "Oh! [mc]!?"
        scene 56_s3 with Fade(0.5,0.5,0.5)
        perception "She quickly leaps over the counter almost tripping and falling on her head."
        yuuhi "I missed you!"
        scene 56_s5 with Dissolve(0.8)
        mc "I missed you too, Yuuhi. Sorry for scaring you."
        scene 56_s4 with dissolve
        yuuhi "It's fine. I just peed a little."
        scene 56_s5 with dissolve
        mc "..."
        scene 56_s6 with dissolve
        yuuhi "Hmph! You always take so long to visit!"
        scene 56_s7 with dissolve
        mc "I'd love to visit more but you know my situation."
        scene 56_s6 with dissolve
        yuuhi "*sigh* I suppose it can't be helped..."
        scene 56_s4 with dissolve
        yuuhi "Anyway, I'm glad you're safe!"
        scene 56_s5 with dissolve
        mc "Thanks."
        mc "You requested assistance?"
    scene 31_s1 with Dissolve(1.0)
    yuuhi "You see, our store was closed to the public if you noticed because my Pops was working for a special request from Mr. Darius."
    scene 31_s2 with dissolve
    mc "Special request?"
    scene 31_s1 with dissolve
    yuuhi "He finished forging new armor for him. Only the chestplate for now."
    scene 31_s2 with dissolve
    mc "Alright, and you want me to... test it?"
    scene 31_s1 with dissolve
    yuuhi "Exactly!"
    scene 31_s2 with dissolve
    mc "Alright... where is it?"
    scene 31_s1 with dissolve
    yuuhi "Hold on, I'll bring it here."
    scene 56_s9 with Dissolve(1.0)
    perception "She holds up a polished chainmail chestplate, the metal glinting in the light."
    perception "You strip off your shirt while Yuuhi eagerly watches, practically bouncing with excitement."
    yuuhi "Oh my... Your physique hasn't changed since last time."
    mc "Focus, Yuuhi."
    scene 56_s8 with Dissolve(1.0)
    sensation "You slide the armor over your chest. Snug, but surprisingly comfortable. The weight settles evenly across your shoulders."
    mc "Fits well enough. How's it look?"
    yuuhi "You look very intimidating, [mc]!"
    mc "This looks like the same one the guards wear."
    scene 31_s6 with Dissolve(0.7)
    yuuhi "Yes! But this one's much more improved. Smaller gaps, stronger weave! And look at the finish!"
    scene 31_s2 with dissolve
    mc "Well, let's hope it works."
    scene 31_s17 with dissolve
    yuuhi "It will!"
    scene 31_s18 with dissolve
    mc "Fine. But if I end up dead, bury me under a cherry tree."
    scene 31_s1 with dissolve
    yuuhi "That's... oddly specific but sure. I mean... not like you will!"
    yuuhi "Alright! Time for the test!"
    scene 31_s2 with dissolve
    mc "With wha-"
    play sound "sound_effects/metal_ting.mp3"
    scene 56_s10 with vpunch
    perception "Without warning, she whips a dagger."
    scene 56_s11 with dissolve
    mc "Ahh!"
    perception "The blade bounces harmlessly off with a clink."
    scene 31_s2 with dissolve
    mc "At least let me brace myself first!"
    mc "And why did you aim it at my heart of all places?"
    scene 31_s1 with dissolve
    yuuhi "Sorry, sorry! But see? It works!"
    scene 31_s2 with dissolve
    mc "You nearly gave me a heart attack."
    scene 31_s1 with dissolve
    yuuhi "Now for the real test!"
    scene 31_s2 with dissolve
    mc "Real test?!"
    scene 56_s12 with dissolve
    mc "What are you looking at?"
    scene 56_s13 with Dissolve(0.9)
    mc "You can't be serious."
    yuuhi "Oh, but I am~!"
    mc "Can you even lift that?"
    yuuhi "Not me. Pops!"
    scene 56_s15 with Dissolve(1.0)
    dean "What is it, Yuuhi?"
    scene 56_s14 with dissolve
    yuuhi "The dagger worked great! Now we need the blunt force test!"
    scene 56_s15 with dissolve
    dean "Yuuhi, that's unnecessary. A sword would suffice."
    scene 56_s14 with dissolve
    yuuhi "Come on! When else do we get to use this club?!"
    scene 56_s15 with dissolve
    dean "Yuuhi..."
    scene 56_s14 with dissolve
    yuuhi "Pleeeaaaasse~!"
    scene 56_s15 with dissolve
    dean "*sigh* Fine."
    scene 56_s16 with dissolve
    dean "Son, brace yourself."
    scene 56_s17 with dissolve
    mc "*gulp* Nice to meet you too..."
    scene 56_s18 with Fade(0.5,0.5,0.5)
    mc "It's soo much bigger up close..."
    yuuhi "That's what she said! Hahahaha!"
    mc "..."
    dean "..."
    yuuhi "Haha..."
    stop music fadeout 0.1
    play sound "sound_effects/metalhit2.mp3"
    scene 56_s19 with vpunch
    sensation "The club slams into your chest with a deafening THUD. Your whole body lifts off the ground, you feel like vomiting."
    scene 56_s20 with Dissolve(0.6)
    ""
    play music "breakup.mp3" fadein 3.0 loop
    scene 56_s21 with Dissolve(3.0)
    yuuhi "*gasp* [mc]!?"
    yuuhi "Pops, that was way too hard!!"
    dean "It's a durability test, not a love tap."
    mc "It's fine..."
    mc "Take me. I'm useless anyway..."
    mc "I don't belong here."
    yuuhi "[mc]? What are you saying?"
    yuuhi "Are you breathing?!"
    stop music fadeout 2.0 
    scene 56_s23 with dissolve
    mc "...Huh?"
    scene 56_s22 with dissolve
    yuuhi "Can you breath?"
    scene 56_s23 with dissolve
    mc "Ngh... barely."
    mc "Just... let me... lie here a minute..."
    dean "The impact will settle. Give it time."
    scene 56_s22 with dissolve
    yuuhi "Oh no... I didn't mean for this to happen!"
    scene 56_s23 with dissolve
    mc "Argh..."
    mc "I hope this was worth it, Yuuhi."
    scene 56_s22 with dissolve
    yuuhi "*sniff* I'm sorry, [mc]! I didn't think it'd be so rough..."
    scene 56_s23 with dissolve
    mc "It's fine. The armor held, I'll give you that."
    scene 56_s22 with dissolve
    yuuhi "I'm so sorry, [mc]! I-I didn't know..."
    scene 56_s23 with dissolve
    mc "*cough* It's fine... I don't feel any pain. Actually, I don't feel anything at all..."
    scene 56_s22 with dissolve
    yuuhi "So... does that mean my design passed?"
    scene 56_s23 with dissolve
    mc "I guess so. Next time... No, fuck that. There won't be a next time."
    scene 56_s22 with dissolve
    yuuhi "I fully understand!"
    yuuhi "Is there anything I can do to make up for it?"
    scene 56_s23 with dissolve
    mc "...Anything?"
    scene 56_s22 with dissolve
    yuuhi "Yes! Just say the first thing that comes to your mind!"
    scene 56_s23 with dissolve
    call screen scene56_choice01 with dissolve

label scene56_choice01_op1:
    $ mc_ask_yuuhi_pussy = True
    mc "Pussy."
    scene 56_s22 with dissolve
    yuuhi "W-What?"
    scene 56_s23 with dissolve
    mc "Let me see your pussy..."
    scene 56_s22 with dissolve
    if mc_harem_yuuhi:
        yuuhi "[mc]!? This isn't the time for jokes!"
    else:
        yuuhi "[mc]! This isn't the time for jokes!"
    scene 56_s23 with dissolve
    mc "*cough* *cough*"
    scene 56_s24 with dissolve
    yuuhi "Fine! Fine! Please don't die on me!"
    yuuhi "He's gone, so..."
    scene 56_s25 with Dissolve(1.0)
    yuuhi "Here!"
    perception "Smooth... pussy... so pink and yummy..."
    mc "I can barely think straight..."
    yuuhi "Is this enough?"
    call screen scene56_choice02 with dissolve

label scene56_choice02_op1:
    mc "That's enough. Thank you."
    mc "Help me up."
    jump scene56_2

label scene56_choice02_op2:
    $ mc_ask_yuuhi_pee = True
    mc "Now pee."
    yuuhi "W-W-What?!"
    mc "I want you to pee on me, Yuuhi."
    yuuhi "I-I cant!"
    mc "Please... I think I might recover if your pee hits me square in the face."
    yuuhi "Now you're pushing it!"
    mc "Please..."
    yuuhi "Dammit! Fine. B-But you {i}will{/i} help me clean it!"
    mc "Alright..."
    play sound "sound_effects/pee.mp3"
    scene 56_s26 with Dissolve(1.0)
    yuuhi "Hnnnn!"
    sensation "It's warm... so warm..."
    scene 56_s27 with Dissolve(1.0)
    yuuhi "T-This is so embarrassing...!"
    scene 56_s25 with Dissolve(1.0)
    stop sound fadeout 1.5
    yuuhi "There isn't any left."
    mc "It's enough. You did good."
    yuuhi "Can you get up now?"
    mc "Yeah. Grab my hand."
    yuuhi "Eww, no! You're covered in pee..."
    jump scene56_2

label scene56_choice01_op2:
    mc "..."
    mc "I can't think of anything."
    mc "Just help me up."
    jump scene56_2

label scene56_2:
    $ update0_3_1_tasks_armor_fin = True
    scene 31_s19 with Fade(1.0,1.0,1.0)
    yuuhi "Are you sure you're fine to walk, [mc]?"
    scene 31_s20 with dissolve
    mc "I'm good. We're done here?"
    scene 31_s19 with dissolve
    yuuhi "Yes, yes! Thank you again!"
    scene 31_s20 with dissolve
    mc "Ouch..."
    if mc_ask_yuuhi_pussy:
        scene 31_s19 with dissolve
        yuuhi "A-And please don't tell Pops about... that."
        scene 31_s20 with dissolve
        mc "Sure. Later, Yuuhi."
    jump scene55_taskboard

label scene57:
    $ update0_3_1_tasks_counter += 1
    mc "Serena or Selene? Man, that handwriting is terrible!"
    mc "Anyway, I remember buying [horse] from her. But helping with a massage? I don't think this should belong here..."
    mc "I guess I better check it anyway."
    stop music fadeout 2.0 
    scene 33_s1 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 1.0 loop
    mc "Hahh... hahh... I really need to work on my cardio..."
    scene 57_s1 with Fade(0.5,0.5,0.5)
    stop music fadeout 2.0 
    mc "Hello?"
    play music "selene_temp.mp3" fadein 3.0 loop
    scene 33_s8 with Dissolve(1.0)
    selene "Oh! Sir! You here for another horse?"
    scene 33_s7 with dissolve
    mc "No, I'm here because of your letter."
    scene 33_s9 with dissolve
    selene "Even better!"
    scene 33_s10 with dissolve
    mc "What's the problem?"
    scene 33_s9 with dissolve
    selene "See, my body aint like it used to be. Not after all the animals started breeding outta control."
    scene 33_s10 with dissolve
    mc "You make it sound like the barn's turned into a brothel."
    scene 33_s9 with dissolve
    selene "*giggles* Ain't that far off sometimes, honestly."
    scene 57_s2 with Dissolve(0.7)
    mc "I see... wait— is that [horse]?!"
    selene "Huh? Oh! That's the one you bought, right?"
    mc "Yeah... What's she doing here?"
    selene "She came back a few days ago, looking all spooked. Must've ran from somethin' nasty."
    mc "Well, at least she found her way home."
    selene "Yup! You can take her back if you want. Less work for me."
    scene 33_s7 with dissolve
    mc "I'll keep her here for now. Anyway, let's get back to your letter..."
    scene 33_s8 with dissolve
    selene "Right, like I said. The work's been brutal, master used to help but he's real sick these days."
    scene 33_s7 with dissolve
    mc "Mhm."
    scene 33_s8 with dissolve
    selene "You humans are so fragile with your illnesses."
    scene 33_s7 with dissolve
    mc "Serena... can you get to the point? What exactly do you want?"
    scene 33_s8 with dissolve
    selene "A massage, of course!"
    scene 33_s7 with dissolve
    mc "...A massage."
    scene 33_s8 with dissolve
    selene "Yep! Master used to do it for me when my muscles got sore, but now he just coughs a lot."
    scene 33_s7 with dissolve
    mc "Serena... you do realize this isn't exactly what the task board is for, right?"
    scene 57_s3 with dissolve
    selene "Why not? I'm a citizen, too! Citizens have needs!"
    scene 57_s4 with dissolve
    mc "*sigh*"
    call screen scene57_choice01 with dissolve

label scene57_choice01_op1:
    $ update0_3_1_tasks_massage_fin = True
    $ update0_3_1_tasks_massage_fin_uncomplete = True
    $ serena_love -= 10
    mc "Serena, you can't post silly personal requests on an official board. I have real work to do."
    scene 57_s3 with dissolve
    selene "But my feet really do hurt..."
    scene 57_s4 with dissolve
    mc "Then tell your cheapskate master to hire someone to help you. Or maybe stop chasing goats barefoot."
    scene 57_s3 with dissolve
    selene "Excuse me! These goats are very persuasive!"
    scene 57_s4 with dissolve
    mc "Just... don't post nonsense like this again."
    scene 57_s3 with dissolve
    selene "Hmph. Fine. No fun allowed, I see."
    scene 57_s4 with dissolve
    jump scene55_taskboard

label scene57_choice01_op2:
    $ serena_love += 10
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene7_p5_replay:
        $ persistent.scene7_p5_replay = True
    scene 57_s4
    mc "Fine. I'll give you a massage."
    scene 33_s9 with dissolve
    selene "Yay! Thank you, sir!"
    scene 33_s10 with dissolve
    mc "Where do you want me to start?"
    scene 33_s9 with dissolve
    selene "My feet are screaming for it... but... you could also massage my breasts too."
    scene 33_s10 with dissolve
    mc "Your breasts?!"
    scene 33_s9 with dissolve
    selene "Uh-huh. Master always said it relaxed me better."
    scene 33_s10 with dissolve
    mc "I bet he did..."
    call screen scene57_choice02 with dissolve

label scene57_choice02_f:
    $ scene57_choice02_f = True
    $ scene57_choice02_b = False
    if scene57_choice02_f_first:
        $ scene57_choice02_f_first = False
        mc "Feet it is."
        scene 33_s9 with dissolve
        selene "My hero!"
        scene 33_s10 with dissolve
        scene 57_s6 with Fade(0.5,0.5,0.5)
        selene "Here ya go, sir!"
        scene 57_s5 with dissolve
        mc "(I can see her pussy...)"
        call screen scene57_choice02 with dissolve
    scene 57_s5 with Fade(0.5,0.5,0.5)
    call screen scene57_choice02 with dissolve

label scene57_choice02_f_soles:
    if not scene57_finish:
        $ scene57_finish = True
    if scene57_choice02_f_soles_first:
        $ scene57_choice02_f_soles_first = False
        scene 57_s7 with Dissolve(1.0)
        sensation "She wiggles her toes playfully as she extends her bare feet toward you. Despite her work in the barn, her feet are surprisingly well-kept, soft."
        mc "You weren't kidding... your soles are really tense."
        selene "Told ya! All that running around, chasing chickens and pulling stuck goats out of fences."
        scene 57_s8 with Dissolve(1.0)
        sensation "Your fingers press into her arches, kneading the tight muscles. A small shiver runs through her with each firm motion."
        selene "Ooooh~ That feels soooo good!"
        selene "You're really good at this! You ever consider massaging as a job, sir?"
        scene 57_s7 with Dissolve(1.0)
        mc "I don't think that's my calling."
        selene "Pity. Your hands are strong but gentle."
    else:
        scene 57_s7 with Dissolve(1.0)
        sensation "She wiggles her toes playfully as she extends her bare feet toward you. Despite her work in the barn, her feet are surprisingly well-kept, soft."
        scene 57_s8 with Dissolve(1.0)
        selene "Ahhh~ Hnnn~"
        mc "Stop moaning..."
        scene 57_s7 with Dissolve(1.0)
        selene "Mmmmm~ I can't help it!"
    scene 57_s5 with Dissolve(1.0)
    call screen scene57_choice02 with dissolve

label scene57_choice02_f_toes:
    if not scene57_finish:
        $ scene57_finish = True
    if scene57_choice02_f_toes_first:
        $ scene57_choice02_f_toes_first = False
        scene 57_s9 with Dissolve(1.0)
        perception "Her toes occasionally twitch as you work, her soft moans of relief making the barn feel oddly intimate."
        selene "Ahh~ Right there! That's the spot!"
        mc "You're acting like you're in heaven."
        scene 57_s10 with Dissolve(1.0)
        selene "Well, you ain't wrong!"
        selene "Ahnnn~"
        mc "It can't be that good?"
        scene 57_s9 with Dissolve(1.0)
        selene "It is if you're tired!"
    else:
        scene 57_s9 with Dissolve(1.0)
        perception "Her toes occasionally twitch as you work, her soft moans of relief making the barn feel oddly intimate."
        selene "Push your fingers in between~"
        scene 57_s10 with Dissolve(1.0)
        selene "Mfhhmmm~!"
    scene 57_s5 with Dissolve(1.0)
    call screen scene57_choice02 with dissolve
        
label scene57_choice02_b:
    $ scene57_choice02_f = False
    $ scene57_choice02_b = True
    if scene57_choice02_b_first:
        $ scene57_choice02_b_first = False
        mc "Breasts it is..."
        scene 57_s12 with Fade(0.5,0.5,0.5)
        perception "Serena lifts her arms behind her head, her large breasts swaying freely in front of you. Her expression is completely innocent."
        scene 57_s11 with dissolve
        selene "*giggles* Don't be shy, sir. They're quite soft!"
        scene 57_s12 with dissolve
        call screen scene57_choice02 with dissolve
    else:
        scene 57_s12 with Fade(0.5,0.5,0.5)
        call screen scene57_choice02 with dissolve

label scene57_choice02_b_breast:
    if not scene57_finish:
        $ scene57_finish = True
    if scene57_choice02_b_breast_first:
        $ scene57_choice02_b_breast_first = False
        scene 57_s13 with Dissolve(1.0)
        sensation "You gently cup them with both hands. Soft... pillowy... her warm flesh molds beneath your palms as you apply slow, circular pressure."
        selene "Oooh~ That's the spot! You got good hands, sir."
        mc "That so?"
        scene 57_s14 with Dissolve(1.0)
        selene "Master always said massaging the breasts helps with posture! Something about... blood flow? I forgot~"
        selene "Ahh~ My back hurts less when you lift them up!"
        scene 57_s13 with Dissolve(1.0)
        selene "Mhnnn~"
    else:
        sensation "You gently cup them with both hands. Soft... pillowy... her warm flesh molds beneath your palms as you apply slow, circular pressure."
        scene 57_s13 with Dissolve(1.0)
        selene "You seem to be fond of my breasts, sir."
        scene 57_s14 with Dissolve(1.0)
        mc "I am."
        selene "Hehe~ I hope you aren't thinking of anything else. This is just a massage."
        scene 57_s13 with Dissolve(1.0)
        mc "Right."
    scene 57_s12 with Dissolve(1.0)
    call screen scene57_choice02 with dissolve

label scene57_choice02_b_nipple:
    if not scene57_finish:
        $ scene57_finish = True
    if scene57_choice02_b_nipple_first:
        $ scene57_choice02_b_nipple_first = False
        scene 57_s15 with Dissolve(1.0)
        perception "You squeeze her nipples but she seems entirely unfazed, her breathing steady as she simply enjoys the massage."
        selene "Ahh! It's like you're milking a cow. Haha~"
        selene "You're really thorough, sir! Do all men massage this good?"
        scene 57_s16 with Dissolve(1.0)
        mc "I don't think most men even get the chance..."
        sensation "Her soft nipples squishes with every squeeze, warmth radiating through your fingers as you work."
        selene "Hm-hm-hmm~ You're loosening up the knots real nice!"
    else:
        scene 57_s15 with Dissolve(1.0)
        selene "Are ya trying to see if I can give milk?"
        mc "Can you?"
        selene "Not if I wasn't pregnant, sir."
        scene 57_s16 with Dissolve(1.0)
        selene "Ahh~ I thought you already knew that, being a big man and all."
        selene "You humans act really stupid sometimes."
        scene 57_s15 with Dissolve(1.0)
        mc "..."
    scene 57_s12 with Dissolve(1.0)
    call screen scene57_choice02 with dissolve


label scene57_choice02_b_tummy:
    if scene57_choice02_b_tummy_first:
        $ scene57_choice02_b_tummy_first = False
        scene 57_s17 with Dissolve(1.0)
        selene "Sir? Why are you touching my belly?"
        mc "It looked so soft."
        selene "Well it ain't hurtin so... you don't have to."
        mc "Have you been eating enough?"
        selene "Hmm? Of course, sir!"
        selene "Well, maybe not lately... you know..."
        mc "You have a beautiful body. You gotta take care of it."
        selene "O-Oh... Thank you, sir! I'll try."
    else:
        scene 57_s17 with Dissolve(1.0)
        selene "Ahh~ Sir... it feels funny and weird when you touch me there..."
        mc "Is this your weak spot?"
        selene "Weak spot? I don't got no... Ahnnh~! weak spots...!"
        mc "Sure you do."
    scene 57_s12 with Fade(0.5,0.5,0.5)
    call screen scene57_choice02 with dissolve

label scene57_2:
    $ update0_3_1_tasks_massage_fin = True
    scene 33_s9 with Fade(1.0,1.0,1.0)
    selene "Aaaah~ That was amazing! My body feels so light now!"
    scene 33_s10 with dissolve
    mc "I bet."
    $ renpy.end_replay()
    if not mc_maia_left:
        mc "Hmm. Maybe I'll give Maia a massage too."
        scene 33_s9 with dissolve
        selene "Maia?"
        scene 33_s10 with dissolve
        mc "My wife."
        scene 33_s9 with dissolve
        selene "Oh! I see."
        selene "She must be lucky to be married to you, sir."
        scene 33_s10 with dissolve
        mc "What do you mean?"
        scene 33_s9 with dissolve
        selene "If she's married to you then she doesn't have to work a lot, right?"
        scene 33_s10 with dissolve
        mc "I guess so."
        scene 33_s9 with dissolve
        selene "Any chance you could also take little ol' me?"
        scene 33_s10 with dissolve
        mc "Huh? You want me to marry you?"
        scene 33_s9 with dissolve
        selene "Haha forget it. Just messin' around..."
    selene "Anyways... Thanks again, sir! I'll let the Queen know you took care of my request!"
    scene 33_s10 with dissolve
    mc "...Maybe don't mention the details."
    scene 33_s9 with dissolve
    selene "Why not? You did great!"
    scene 33_s10 with dissolve
    stop music fadeout 2.0 
    mc "*sigh* Never mind."
    jump scene55_taskboard

label scene58:
    $ update0_3_1_tasks_counter += 1
    mc "A corrupt tax collector? Alright then, let's see what he has to say."
    scene 58_s1 with Dissolve(1.0)
    guard "If you wish, sir. I can have him brought in. I know this man. He attempted to extort my elderly mother. He does this sort of thing all the time."
    scene 58_s2 with dissolve
    mc "Sorry to hear that. And yes, bring him here."
    scene 58_s1 with dissolve
    guard "Sir."
    stop music fadeout 2.0 
    scene 58_s2 with dissolve
    scene 58_s3 with Fade(1.0,1.0,1.5)
    play music "side_event1.mp3" fadein 3.0 loop
    perception "Avery sits tall on the throne, one leg crossed over the other, watching as the guards drag the tax collector inside. The man glances nervously between the two guards."
    scene 58_s5 with Fade(0.5,0.5,0.5)
    avery "Ah. Our diligent collector. I trust you're comfortable?"
    scene 58_s4 with dissolve
    collector "Y-Your grace... I-I don't know what this is about—"
    scene 58_s5 with dissolve
    avery "You don't. Yet."
    avery "Well then, [mc]. He's all yours. Let me see how you handle this."
    mc "(Time to show my skills from playing all those detective games.)"
    mc "Your name?"
    scene 58_s6 with dissolve
    collector "B-Bernat, sir."
    scene 58_s7 with dissolve
    mc "Bernat. You've been accused of extorting citizens. Using your position to take coin beyond what's owed. Beatings, threats... sound familiar?"
    scene 58_s6 with dissolve
    collector "Lies, sir! Nothing but the usual peasant gossip! You know how they get... always complaining, never satisfied."
    scene 58_s7 with dissolve
    avery "Careful how you speak about my people, Bernat."
    scene 58_s6 with dissolve
    collector "O-Of course, my lady. I meant no disrespect."
    scene 58_s7 with dissolve
    mc "Witnesses speak of you striking an old man. Beating him for {i}fees.{/i}"
    scene 58_s6 with dissolve
    collector "M-misunderstandings, sir! Sometimes folk need... encouragement to pay timely!"
    scene 58_s7 with dissolve
    mc "Encouragement? With your fist?"
    collector "..."
    scene 58_s5 with dissolve
    avery "And the coin you collected on top of official taxes? Encouragement too?"
    collector "..."
    mc "(Let's see how to handle him...)"
    call screen scene58_choice01 with dissolve

label scene58_choice01_op1:
    scene 58_s8 with Dissolve(1.0)
    mc "*sigh* Bernat, I'm not here to ruin lives. But if you don't cooperate, things will get much worse. Tell me everything... {i}now.{/i}"
    scene 58_s9 with dissolve
    collector "..."
    scene 58_s8 with dissolve
    mc "It's for your own benefit, I assure you."
    scene 58_s9 with dissolve
    collector "...I might've asked for some extra coin here and there. But only from those who could afford it!"
    jump scene58_2

label scene58_choice01_op2:
    scene 58_s10 with vpunch
    mc "Do you want bruises, Bernat? Because you've been handing them out freely. Maybe you should taste your own medicine."
    scene 58_s11 with dissolve
    empathy "He visibly recoils, sweat dripping down."
    collector "N-No, sir! I swear, I lost control only once or twice! Please!"

label scene58_2:
    scene 58_s7 with Dissolve(1.0)
    mc "We can do this the easy way or keep playing games, Bernat."
    scene 58_s4 with dissolve
    collector "I... I might've... misunderstood the exact amounts owed, your grace. Simple accounting mistakes."
    scene 58_s5 with dissolve
    avery "Mistakes? Very well, I will take that as a confession."
    avery "I will let you handle his fate, [mc]."
    scene 58_s6 with Dissolve(0.8)
    collector "*whisper* S-sir... perhaps we can find a... private understanding? Spare your time, spare your effort... spare me?"
    scene 58_s7 with dissolve
    call screen scene58_choice02 with dissolve

label scene58_choice02_op1:
    $ karma_more = False
    $ mc_accept_collector_bribe = True
    mc "Consider this your first and only warning."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 58_s6 with dissolve
    collector "Thank you, Milord! I swear, you won't regret this!"
    collector "May I go now?"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 58_s7 with dissolve
    mc "You can."
    scene 58_s12 with dissolve
    avery "Hmm... I don't quite see why you let him walk free, [mc]. He was clearly guilty."
    scene 58_s13 with dissolve
    mc "I know his type. He just needed a reminder. I doubt he'll be foolish enough to try this again."
    scene 58_s12 with dissolve
    avery "Very well. I'll trust your instincts... for now."
    scene 58_s13 with dissolve
    jump scene58_3

label scene58_choice02_op2:
    $ mc_sent_collector_jail = True
    $ update0_3_1_tasks_tax_fin = True
    mc "Guards. Seize him."
    scene 58_s4 with Dissolve(0.8)
    collector "No! Please! Mercy!"
    scene 58_s5 with dissolve
    avery "Mercy? You had none for my people. You'll find little here."
    scene 58_s13 with Dissolve(1.0)
    mc "He's yours, ma'am."
    scene 58_s12 with dissolve
    avery "Efficient. I like that. On to your next task, [mc]."
    scene 58_s13 with dissolve
    jump scene55_taskboard

label scene58_choice02_op3:
    $ mc_told_collector = True
    $ update0_3_1_tasks_tax_fin = True
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    mc "You'll return every extra coin you've taken. And you will swear, before lady Avery, to never repeat this."
    scene 58_s6 with dissolve
    collector "O-Of course! Sir, lady Avery! You have my word!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 58_s7 with dissolve
    avery "Go. I will have my gaurds watch you closely for the next month."
    scene 58_s6 with dissolve
    collector "Y-Yes, lady Avery..."
    scene 58_s7 with dissolve
    scene 58_s12 with Dissolve(1.0)
    avery "Very merciful, [mc]. I just hope his word is worth more than his numbers."
    scene 58_s13 with dissolve
    jump scene55_taskboard

label scene58_3:
    stop music fadeout 2.0 
    scene 58_s14 with Fade(1.0,1.5,1.0)
    collector "Thank you very much, sir! Please accept this."
    scene 58_s15 with dissolve
    call screen scene58_choice03 with dissolve

label scene58_choice03_op2:
    $ update0_3_1_tasks_tax_fin = True
    scene 58_s18 with Dissolve(1.0)
    $ renpy.notify("You received 50 coins!")
    play sound "sound_effects/coin_collect.mp3"
    $ mc_coin += 50
    mc "Alright, now get out of here."
    collector "Yes, sir!"
    jump scene55_taskboard

label scene58_choice03_op1:
    $ karma_more = False
    $ update0_3_1_tasks_tax_fin = True
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    mc "That's it? That's all your life's worth?"
    scene 58_s16 with dissolve
    collector "O-Of course not! Please forgive me."
    scene 58_s18 with Dissolve(1.0)
    hide screen stat_change with easeoutright
    collector "Here!"
    $ renpy.notify("You received 100 coins!")
    play sound "sound_effects/coin_collect.mp3"
    $ mc_coin += 100
    mc "Alright, now get out of here."
    collector "Yes, sir!"
    jump scene55_taskboard

label scene59:
    $ update0_3_1_tasks_counter += 1
    mc "Medicine testing? Oh man... I've heard many stories of these going bad."
    stop music fadeout 2.0 
    scene 59_s1 with Fade(1.5,1.0,1.0)
    play music "city_ambience.mp3" fadein 1.0 loop
    "*knock* *knock*"
    mc "Hello?"
    elise_ "Who is it?"
    mc "I'm here because of your request."
    elise_ "Please come in."
    stop music fadeout 2.0 
    scene 59_s2 with Fade(1.0,1.0,0.5)
    play music "side_event2.mp3" fadein 3.0 loop
    mc "So... you need to test your new medicine, is that it?"
    scene 59_s3 with dissolve
    elise_ "Correct. I am doctor Elise. Pleasure to make your acquaintance."
    scene 59_s2 with dissolve
    mc "[mc]. Likewise."
    scene 59_s3 with dissolve
    elise "Please, sit. The first formula is a mild stimulant designed to improve focus and blood circulation."
    scene 59_s2 with dissolve
    mc "Sounds harmless enough."
    scene 59_s3 with dissolve
    elise "It is. Or rather, it should be. That's why you're here."
    scene 59_s2 with dissolve
    scene 59_s4 with Fade(0.5,0.5,0.5)
    perception "Her laboratory is meticulously clean. Shelves stacked with neatly labeled vials. The faint scent of herbs and something metallic hangs in the air."
    scene 59_s5 with Dissolve(0.8)
    elise "Here."
    perception "She hands you a small glass vial. The liquid inside shimmers faintly, a pale, almost glowing green."
    scene 59_s6 with Dissolve(1.0)
    mc "Cheers..."
    sensation "The liquid is slightly bitter, but smooth. A faint tingling spreads down your throat as it goes down."
    scene 59_s9 with Dissolve(0.8)
    mc "Not bad. A bit tangy."
    scene 59_s8 with dissolve
    elise "Good. Now we wait."
    scene 59_s9 with dissolve
    scene 59_s7 with Dissolve(1.0)
    sensation "After a minute or so, you feel your heartbeat quicken slightly. Your skin feels warmer, like a gentle flush spreading over your chest and face."
    mc "Hmm..."
    elise "Describe how you're feeling. Tell me everthing."
    mc "Feels... warm. Kinda like after a short run. A bit of a head rush, but nothing scary."
    elise "Excellent. No dizziness? Blurred vision?"
    mc "No. Just... a weird tingle in my fingertips."
    elise "Stimulated peripheral circulation. As expected."
    scene 59_s8 with Dissolve(0.9)
    elise "Is that all?"
    scene 59_s9 with dissolve
    mc "I think so."
    scene 59_s8 with dissolve
    elise "Good. You're tolerating it well. Shall we proceed to the second drug?"
    scene 59_s9 with dissolve
    mc "Already?"
    scene 59_s8 with dissolve
    elise "The sooner we're done, the better your odds of not developing side effects overnight."
    scene 59_s9 with dissolve
    mc "(That's reassuring...)"
    mc "Alright, let's get this over with."
    scene 59_s4 with Dissolve(0.7)
    elise "This next one is an experimental antipyretic, for fever treatment."
    elise "It's quite fast acting, but the method of administration may be new to some people."
    mc "New...?"
    elise "There are two options. Oral or rectal insertion."
    mc "Rectal?!"
    elise "Yes. Absorption is faster that way."
    mc "Uhh..."
    scene 59_s8 with Dissolve(0.8)
    elise "I won't pressure you. The choice is entirely yours."
    scene 59_s9 with dissolve
    call screen scene59_choice01 with dissolve

label scene59_choice01_op2:
    $ mc_took_pill_ass = True
    mc "Let's try rectal insertion."
    scene 59_s8 with dissolve
    elise "Very well. Please remove your clothes and lay on the table."
    scene 59_s9 with dissolve
    mc "Got it..."
    scene black with Fade(1.0,1.0,1.0)
    sensation "The cold air brushes against your bare skin as you settle onto the examination table. The surface beneath you feels cool."
    scene 59_s10 with Dissolve(1.0)
    elise "If you'll excuse me."
    sensation "You feel the softness of her hands spreading your cheeks gently, her touch clinical but careful."
    elise "I'll apply some lubricant now. Try to relax."
    elise "And by the way, you didn't have to remove all your clothes. Just the pants would have been fine."
    mc "..."
    sensation "A cool, slick sensation spreads around your entrance as her fingers begin to massage the area, working in slow, practiced circles."
    mc "Hahh..."
    elise "Does it hurt?"
    mc "No... just strange."
    elise "That's normal."
    perception "You feel her gloved fingertip press in slightly deeper, parting you with calm precision."
    sensation "Your body tenses for a moment, but her movements are deliberate, gentle—her finger slides smoothly inside, spreading warmth as she reaches deeper."
    elise "Excellent. I'm inserting the pill now."
    mc "It's not in yet?"
    elise "Just relax."
    play sound "se_sfx/blowjob/facial4.mp3" 
    sensation "You feel the soft pressure of the small capsule sliding past your rim, followed by a faint, satisfying fullness."
    scene 59_s11 with Dissolve(1.0)
    mc "Oh..."
    mc "Ah... sorry."
    scene 59_s12 with dissolve
    elise "No need to apologize. This is a normal reflex. In fact, it indicates healthy prostate response."
    mc "That's... good to know."
    scene 59_s13 with dissolve
    elise "And that's it. We're done."
    scene 59_s14 with dissolve
    mc "(Fuck... that felt way better than it should have...)"
    elise "..."
    mc "..."
    scene 59_s13 with dissolve
    elise "We're finished. You can dress up."
    scene 59_s14 with dissolve
    mc "Ah, right..."
    scene 59_s8 with Fade(1.0,1.0,1.0)
    elise "Anything unusual?"
    jump scene59_2

label scene59_choice01_op1:
    mc "Orally. Definitely orally."
    scene 59_s8 with dissolve
    elise "Very well."
    elise "Here."
    scene 59_s9 with dissolve
    scene 59_s6 with Dissolve(1.0)
    perception "She hands you a small glass of water and a white pill, slightly larger than you expected."
    mc "Hngh... that's... a big one."
    sensation "The pill slides down easily, but within seconds a curious warmth starts to pool in your stomach. Your muscles relax, almost like a gentle wave of comfort washing over you."
    scene 59_s8 with dissolve
    elise "Anything unusual?"
    jump scene59_2

label scene59_2:
    $ update0_3_1_tasks_trial_fin = True
    scene 59_s9 with dissolve
    mc "I feel... cozy. Like I could take a nap right here."
    scene 59_s8 with dissolve
    elise "Excellent. Drowsiness was one of the expected mild side effects. The formula works."
    scene 59_s9 with dissolve
    mc "Glad to hear it."
    perception "Her eyes briefly scan your body, calmly studying your reactions with professional detachment."
    scene 59_s8 with dissolve
    elise "No nausea? No tingling?"
    scene 59_s9 with dissolve
    mc "No. Just... kinda floaty."
    scene 59_s8 with dissolve
    elise "Perfect. That concludes our session."
    scene 59_s9 with dissolve
    mc "That was quick."
    scene 59_s3 with Fade(1.0,1.0,1.0)
    elise "You were an excellent test subject, [mc]. Thank you for your cooperation."
    scene 59_s2 with dissolve
    mc "No problem. You don't pay testers, do you?"
    scene 59_s15 with dissolve
    elise "I provide my gratitude."
    scene 59_s2 with dissolve
    mc "..."
    scene 59_s3 with dissolve
    elise "If you experience any side effects overnight, please return immediately."
    scene 59_s2 with dissolve
    mc "Let's hope I don't."
    scene 59_s3 with dissolve
    elise "Then we are done here. Goodbye, [mc]. I hope to see you again if I need more help."
    scene 59_s2 with dissolve
    mc "Goodbye, Elise."
    jump scene55_taskboard

label scene60:
    $ update0_3_1_tasks_counter += 1
    mc "Marriage problems, huh? I guess some things never change, no matter where you go."
    scene 58_s1 with Dissolve(1.0)
    guard "Shall I bring them here, sir?"
    scene 58_s2 with dissolve
    mc "That would be good."
    stop music fadeout 2.0 
    scene 58_s12 with Fade(1.0,1.0,1.0)
    avery "Is something the matter, [mc]?"
    scene 58_s13 with dissolve
    mc "I told the guard to bring over a married couple who need help."
    scene 58_s12 with dissolve
    avery "A marriage dispute? Ugh, I hate these..."
    scene 58_s13 with dissolve
    mc "Tell me about it."
    scene 60_s1 with Fade(1.0,1.0,1.0)
    osric "What are we even doing here?!"
    greta "Because of you, you bastard! I asked for help, and here we are."
    scene 60_s2 with Fade(0.5,0.5,0.5)
    greta "*ahem* Lady Avery, it's an honor, though I wish we met under better circumstances."
    scene 60_s3 with dissolve
    avery "Speak. What is your issue?"
    play music "sillytime.mp3" fadein 3.0 loop
    scene 60_s8 with dissolve
    osric "The issue is that this woman here is a BITCH!"
    scene 60_s5 with dissolve
    greta "Language! We aren't at your family's shack anymore!"
    scene 60_s4 with dissolve
    osric "You're lucky I only said that. The real word's much worse!"
    scene 60_s5 with dissolve
    greta "Oh really? At least I don't spend every coin we have at the tavern!"
    scene 60_s4 with dissolve
    osric "Because I need to drown my sorrows, living with you!"
    scene 60_s5 with dissolve
    greta "You wouldn't have any sorrows if you actually did something useful with your life!"
    scene 60_s4 with dissolve
    osric "I did plenty! Before you nagged me into quitting everything!"
    scene 60_s5 with dissolve
    greta "You call carving wooden toys plenty?!"
    scene 60_s4 with dissolve
    osric "They were artistic!"
    scene 60_s5 with dissolve
    greta "You have the artistic sense of a potato!"
    scene 60_s4 with dissolve
    osric "At least I still had some spirit—unlike you!"
    scene 60_s5 with dissolve
    greta "Spirit? You haven't touched me in months!"
    scene 60_s4 with dissolve
    osric "Maybe if you stopped wearing that awful nightgown, I'd feel like it!"
    scene 60_s5 with dissolve
    greta "That was your mother's wedding gift, you insensitive donkey!"
    scene 60_s4 with dissolve
    osric "Oh, we're bringing my mother into this now?!"
    scene 60_s5 with dissolve
    greta "She hated me from day one!"
    scene 60_s4 with dissolve
    osric "Because you never even tried to get along!"
    scene 60_s5 with dissolve
    greta "You didn't seem to mind when I was giving you nightly blowjobs every evening!"
    scene 60_s4 with dissolve
    osric "Well, you stopped doing that too!"
    scene 60_s5 with dissolve
    greta "Because {i}you{/i} stopped washing your disgusting balls!"
    scene 60_s4 with dissolve
    osric "Because YOU broke the washing bucket!"
    scene 60_s5 with dissolve
    greta "YOU used it to carve a toy in one of your drunken fits!"
    scene 60_s4 with dissolve
    osric "I... Wait... Did I really?"
    scene 60_s6 with Dissolve(1.0)
    perception "The shouting echoes through the grand hall, slowly giving way to an awkward silence. You and Avery exchange a glance, both unsure whether to laugh or cry."
    scene 60_s7 with dissolve
    avery "...Are you two quite finished?"
    scene 60_s6 with dissolve
    greta "..."
    osric "..."
    scene 60_s7 with dissolve
    avery "*sigh* I'll have a headache from all that shouting. I'll let you handle it, [mc]."
    scene 60_s6 with dissolve
    scene 60_s3 with Dissolve(1.0)
    call screen scene60_choice01 with dissolve

label scene60_choice01_op1: 
    $ update0_3_1_tasks_dispute_fin = True
    mc "Look, you both clearly have issues, but you're still here together, aren't you?"
    mc "Why not start small? Talk to each other. Compromise. Maybe cut back on the drinking, Osric, and maybe, Greta, appreciate his efforts, however... odd they may be."
    scene 60_s2 with dissolve
    greta "I tried talking. He just snores!"
    scene 60_s4 with dissolve
    osric "I snore because your voice puts me to sleep!"
    scene 60_s2 with dissolve
    greta "See?! He's impossible!"
    scene 60_s3 with dissolve
    mc "Uhh... You know what? Most couples would kill for the kind of passion you two just showed."
    mc "The arguing, the yelling... that's raw emotion! You still care."
    scene 60_s8 with dissolve
    osric "...Care?!"
    scene 60_s2 with dissolve
    greta "Is that what you think this is?"
    scene 60_s3 with dissolve
    mc "Absolutely! You're like two lovers in a dramatic play."
    scene 60_s8 with dissolve
    osric "If this is love, then my nuts are a pair of golden coins."
    scene 60_s5 with dissolve
    greta "And I'd rather marry those coins than you!"
    scene 60_s3 with dissolve
    mc "..."
    avery "I get what you're trying to say, [mc] but it's clearly not working."
    scene 60_s2 with dissolve
    greta "I doubt there is a solution for us, lady Avery..."
    scene 60_s8 with dissolve
    osric "The solution looks pretty clear to me!"
    scene 60_s5 with dissolve
    greta "Shut up!"
    scene 60_s2 with dissolve
    greta "*sigh* I apologize for wasting your time."
    scene 60_s3 with dissolve
    mc "Shit..."
    scene 58_s12 with Dissolve(1.0)
    avery "Don't worry, [mc]. I'm sure you did your best there. These... things can be quite complicated."
    avery "I will send for a counselor to visit them tomorrow. Hopefully they don't kill each other by then."
    scene 58_s13 with dissolve
    jump scene55_taskboard

label scene60_choice01_op2:
    $ update0_3_1_tasks_dispute_fin_success = True
    $ update0_3_1_tasks_dispute_fin = True
    mc "Maybe you two should just separate. Divorce."
    scene 60_s2 with vpunch
    greta "Divorce?!"
    scene 60_s8 with dissolve
    osric "Y-You mean... split up for good?"
    scene 60_s3 with dissolve
    mc "It might be the best for both of you."
    scene 60_s2 with dissolve
    greta "But then... who would feed him after he comes home drunk and battered?!"
    scene 60_s8 with dissolve
    osric "And who'd remind me to wear clean pants before I leave the house?!"
    scene 60_s2 with dissolve
    greta "He would be hopeless without me!"
    scene 60_s8 with dissolve
    osric "I-I wouldn't know what to do without her!"
    scene 60_s2 with dissolve
    greta "...Maybe we just need counseling!"
    scene 60_s8 with dissolve
    osric "Y-Yes, counseling! Not divorce!"
    scene 60_s3 with dissolve
    mc "..."
    avery "Fascinating."
    avery "Threaten to split them and suddenly they remember how much they depend on each other."
    mc "Uhh... I guess I'll take that as a win?"
    scene 60_s2 with dissolve
    greta "Thank you, lady Avery. And that man."
    scene 60_s3 with dissolve
    mc "It's [mc]..."
    scene 60_s8 with dissolve
    osric "We'll seek counseling! I promise."
    scene 60_s3 with dissolve
    avery "Good. I will send a guard to check on you in a few weeks. Until then, stay safe."
    scene 60_s2 with dissolve
    greta "Thank you."
    scene 58_s12 with Dissolve(1.0)
    stop music fadeout 2.0 
    avery "Good job, [mc]. Now onto your next task."
    scene 58_s13 with dissolve
    jump scene55_taskboard

image 61_hj = Movie(play="images/4_chapter3/scene61/61_hj.webm", loop=True)
image 61_hj_faster = Movie(play="images/4_chapter3/scene61/61_hj_faster.webm", loop=True)

label scene61_choice03_op1:
    $ mc_rejected_reb_friend_date = True
    mc "I'm too busy right now, Rebecca. I can't just wander off to drink wine in the middle of the day."
    scene 61_s25 with dissolve
    r "Ugh. Come on, it'll only be for a little bit."
    scene 61_s26 with dissolve
    mc "Even so. Also, how do you expect me to keep working after getting drunk with you?"
    scene 61_s25 with dissolve
    r "*sigh* Fine. Whatever. It's not like I was eager or anything."
    r "Get back to work. I'll find someone else to drink with."
    scene 61_s26 with dissolve
    jump scene55_taskboard

label scene61_choice03_op2:
    $ mc_went_date1_reb = True
    mc "Alright, sure. Where are we going?"
    scene 61_s25 with dissolve
    r "Just follow."
    scene 61_s26 with dissolve
    jump scene61_0

label scene61:
    $ cycle = 0
    scene 61_s25 with vpunch
    r "Boo!"
    scene 61_s26 with dissolve
    mc "Gah! Rebecca?! Don't sneak up on people like that."
    scene 61_s25 with dissolve
    r "You looked like you were about to sprout roots from standing here all day."
    scene 61_s26 with dissolve
    mc "I'm working."
    scene 61_s25 with dissolve
    if mc_rejected_wedding_reb:
        r "So am I—working on our new friendship. And I've decided to invite you for some wine."
        r "Consider it a peace offering. A chance for you to prove you're not completely unbearable."
        scene 61_s26 with dissolve
        mc "Wine? Now?"
        scene 61_s25 with dissolve
        r "Yes. Let's go."
        r "You're supposed to be my protector. My mother told me she trusted me to you, for some reason I still can't fathom."
        r "I still see you as a parasite, so I need to know if you're actually a decent man, or if you can at least handle your drink."
        scene 61_s26 with dissolve
        call screen scene61_choice03 with dissolve
    else:
        r "So am I—working on our marriage. And I've decided we're going on a date."
        scene 61_s26 with dissolve
        mc "A date? Now?"
        scene 61_s25 with dissolve
        r "Yes. You married me, remember? So that makes you mine. Let's go."
        scene 61_s26 with dissolve
        mc "Where are we going?"
        scene 61_s25 with dissolve
        r "Just follow."
        scene 61_s26 with dissolve
        jump scene61_0

label scene61_0:
    $ mc_went_date1_reb = True
    stop music fadeout 2.0 
    scene 61_s26 with dissolve
    scene 61_s1 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 3.0 loop
    mc "You're taking me somewhere inside? I thought you'd want to go outside."
    r "I would, but I'm not allowed beyond the gates without my mother's approval."
    mc "Seriously? That's strict."
    stop music fadeout 2.0 
    r "*scoff* Tell me about it."
    scene 61_s2 with Fade(1.0,1.0,1.0)
    mc "The cellar? You didn't lead me here to assassinate me, did you?"
    r "Don't be dramatic."
    mc "I just thought... we'd be going somewhere more {i}romantic.{/i}"
    r "This {i}is{/i} romantic. Dusty barrels, damp walls, the smell of alcohol, what's not to love?"
    mc "*chuckles* If you say so."
    scene 61_s3 with Fade(0.5,0.5,0.5)
    play music "reb.mp3" fadein 3.0 loop
    mc "You used to come here often?"
    r "Mhm. Whenever I wanted to disappear for a bit. No tutors, no sword drills, no court politics. Just me, the quiet... and occasionally, a stolen bottle of wine."
    mc "Ah, so this is your secret rebellion hideout."
    if mc_rejected_wedding_reb:
        r "Exactly."
    else:
        r "Exactly. And now it's date night."
    scene 61_s4 with dissolve
    perception "The room is lit by a few flickering torches. Old barrels line the walls, and there's a thick layer of dust on everything—except a worn table and a chair, recently used."
    r "Sit down. I'll pick our poison."
    scene black with Fade(0.5,0.5,0.5)
    perception "She fills an empty bottle and pours you both a generous amount."
    scene 61_s5 with dissolve
    mc "Is this the part where you seduce me with terrible wine?"
    scene 61_s6 with dissolve
    r "If the wine doesn't do it, my charm will."
    scene 61_s5 with dissolve
    mc "To what are we drinking?"
    scene 61_s6 with dissolve
    r "To freedom. The little we still have."
    scene 61_s5 with dissolve
    mc "...I'll drink to that."
    scene 61_s7 with Dissolve(1.0)
    perception "The wine is sharp, smoky, and unexpectedly smooth. It leaves a gentle burn that settles in your chest."
    scene 61_s9 with Dissolve(1.0)
    r "Ooph! That's the good stuff."
    scene 61_s8 with dissolve
    mc "It's pretty good."
    mc "You're not wearing you crown."
    scene 61_s9 with dissolve
    r "Fuck that thing. It's too heavy and it messes up my hair. For now... I'm just a regular girl."
    scene 61_s8 with dissolve
    mc "A regular girl with access to a private cellar full of royal wine."
    scene 61_s9 with dissolve
    r "Perks of being a princess."
    scene 61_s8 with dissolve
    mc "So, what does a {i}regular girl{/i} like you do on her days off?"
    scene 61_s9 with dissolve
    r "Drink. Sneak out. Threaten potential suitors. You know, normal things."
    scene 61_s8 with dissolve
    mc "Sounds intense."
    scene 61_s9 with dissolve
    r "Better than embroidery and pretending to like men who sweat perfume."
    r "You know... you're easier to be around like this."
    scene 61_s8 with dissolve
    mc "Like what?"
    scene 61_s9 with dissolve
    r "Relaxed. Not trying to impress anyone. Not acting all knightly and noble. Just... you."
    scene 61_s8 with dissolve
    mc "Acting noble? *chuckles* When have I ever done that?"
    scene 61_s9 with dissolve
    r "You're always so painfully earnest with my mother."
    scene 61_s8 with dissolve
    mc "Is that what it looks like to you? I'm just trying to survive in... an unfamiliar world."
    scene 61_s9 with dissolve
    r "Hmm. Maybe I don't really know you yet."
    scene 61_s8 with dissolve
    mc "We've got all day."
    scene 61_s12 with Dissolve(1.0)
    perception "She swirls her drink lazily, the candlelight catching in her eyes. Her cheeks are faintly flushed."
    mc "How many drinks until you start telling me embarrassing stories about your childhood?"
    scene 61_s11 with dissolve
    r "How many until you stop pretending you're not staring at my breasts every time I walk past you?"
    scene 61_s12 with dissolve
    mc "..."
    scene 61_s11 with dissolve
    r "*chuckles* I'm just joking. Relax. Your face is priceless."
    scene 61_s12 with dissolve
    mc "You're scary when you joke like that."
    scene 61_s11 with dissolve
    r "Scary's what keeps idiots away."
    scene 61_s12 with dissolve
    mc "You really used to come here alone?"
    scene 61_s11 with dissolve
    r "Yes. It was the only place I could just... be. No expectations. No eyes on me. I could just breathe."
    scene 61_s12 with dissolve
    mc "So why bring {i}me{/i} here?"
    r "..."
    scene 61_s11 with dissolve
    r "...I don't know. I thought... maybe it'd feel less lonely this time."
    scene 61_s12 with dissolve
    empathy "There's a softness in her voice, a rare crack in the armor. The kind you don't interrupt."
    mc "..."
    play sound "sound_effects/slam_wood.mp3"
    scene 61_s10 with vpunch
    r "Ugh! Enough of that. More drinks! This one's empty."
    mc "Coming!"
    scene 61_s13 with Dissolve(1.5)
    if not mc_rejected_wedding_reb:
        perception "You pour another round. The cellar is dim, quiet except for the flick of candlelight and the faint creak of wood. A world away from the throne room above."
        r "You know, I always imagined love would be complicated. Not like in stories."
        mc "You think this is love?"
        r "*laughs* I think this is drunk talk... but maybe drunk talk's more honest than sober silence."
        mc "Regardless. I love seeing you like this."
        r "...What are you talking about?"
        mc "I think this is the real you. No crown. No cold glares. Just... Rebecca."
        r "You're making it sound like I'm some repressed noble lady."
        mc "Aren't you?"
        r "Maybe a little..."
        scene 61_s9 with dissolve
        r "But don't get used to it. Once we're out of this cellar, I'm going back to being your terrifying princess."
        scene 61_s8 with dissolve
        mc "Deal. But I'll always know this version exists. The one who drinks cheap wine and swears a lot."
        scene 61_s44 with dissolve
        r "Cheap?! This is royal reserve—aged at least a month."
        scene 61_s43 with dissolve
        mc "You've been holding out on me."
        scene 61_s9 with dissolve
        r "Maybe I just needed someone to share it with."
        scene 61_s8 with dissolve
        mc "..."
        scene 61_s9 with dissolve
        r "What's on your mind?"
        scene 61_s8 with dissolve
        mc "Those demands of yours. They were... intresting. Like, always apologize first when we fight? That sounds... unreasonable."
        scene 61_s44 with dissolve
        r "*chuckles* I was just playing with you. Don't take them seriously. Well... some of them at least. "
        scene 61_s8 with dissolve
        mc "Phew..."
    mc "...Say, Rebecca."
    mc "What do you think will happen in the future?"
    scene 61_s44 with dissolve
    r "The future? It's a blur."
    scene 61_s43 with dissolve
    mc "Your mother told me you weren't the heir. That your brother is."
    scene 61_s44 with dissolve
    r "Of course. And even if they tried to force the crown on me, I'd refuse. Can you imagine? Me, sitting through council meetings about grain tariffs and border disputes?"
    r "I'd rather open a dusty little bookstore in some quiet village no one's ever heard of."
    scene 61_s43 with dissolve
    mc "Really? You'd give all this up?"
    scene 61_s9 with dissolve
    r "In a heartbeat."
    scene 61_s8 with dissolve
    if not mc_rejected_wedding_reb:
        mc "Hmm... but do you really think this marriage will... stick? Become real?"
        scene 61_s44 with dissolve
        r "What are you talking about? The contracts are signed. We're already married, you dweeb. It's done."
        scene 61_s43 with dissolve
        mc "Come on. Be serious. I'm an outsider. A stranger who fell into this world headfirst. And now I'm somehow married to the princess?"
        mc "It feels like a story that's going to have a very tragic ending."
        scene 61_s11 with dissolve
        r "Oh... I see what you mean."
        r "If you didn't know, it doesn't matter here if you're a commoner. Anyone can propose to the royal family. We're not like those other kingdoms, obsessed with pure bloodlines and inbreeding."
        r "I'm {i}not{/i} marrying my cousin or worse... I'd set the castle on fire first."
        scene 61_s12 with dissolve
        mc "Is that so?"
        scene 61_s11 with dissolve
        r "Mhm. My father was a farmer when he won my mother's heart. *laughs* He showed up at the gates with dirt on his boots and a basket of apples."
        r "Granted, my grandmother hated it. She wanted a proper noble. But in the end? Their love won out."
        scene 61_s12 with dissolve
        mc "That's sweet. So you're saying I've got farmer royalty potential?"
        scene 61_s11 with dissolve
        r "You're not even that. You're just some stray my mother picked up. No apples, no land, just a confused look on your face."
        scene 61_s12 with dissolve
        mc "Ouch."
        scene 61_s11 with dissolve
        r "But... maybe I like strays."
        scene 61_s12 with dissolve
        mc "That was dangerously close to being nice. Are you feeling alright?"
        scene 61_s45 with dissolve
        r "I'm... not great at this. I don't know how to be soft with people. I never had to be."
        r "It was always easier to just be sharp. To push people away before they could get close."
        scene 61_s46 with dissolve
        mc "You're doing just fine."
        scene 61_s45 with dissolve
        r "You really think so?"
        scene 61_s46 with dissolve
        mc "Yeah. I do. In fact, I think this might be the first real conversation we've ever had."
        scene 61_s45 with dissolve
        r "It's the wine. Don't get used to it."
        scene 61_s46 with dissolve
        mc "Too late."
    else:
        mc "Hmm... well, I really have to get back to work, Becky. I don't think your aunt will like me slacking off this much."
        scene 61_s45 with Dissolve(1.3)
        r "*sigh* Yeah, yeah. I know. Duty calls. The kingdom needs its steward..."
        scene 61_s46 with dissolve
        mc "You'll just stay here?"
        scene 61_s45 with dissolve
        r "Mhm. Just for a little while. I'll drink it alone, less fun, but... I'm used to it."
        scene 61_s46 with dissolve
        mc "Just don't drink too much, alright? I know I'm supposed to protect you, but it's not a good look to carry you through the halls like a sack of potatoes."
        stop music fadeout 1.5
        r "..."
        jump scene55_taskboard

    stop music fadeout 2.0 
    scene 61_s14 with Fade(1.5,1.0,1.0)
    play music "night.mp3" fadein 3.0 volume 0.5 loop
    perception "The hours slip by in a blur, the wine growing warmer and the room softer."
    scene 61_s16 with Dissolve(1.0)
    r "Hahh~ I like it when it gets to this point. It's like all my worries just vanish away."
    scene 61_s15 with dissolve
    mc "Yeah... I could stay like this forever."
    scene 61_s16 with dissolve
    r "I always end up talking about myself... What about you, [mc]? I've always wondered. Where did you actually come from?"
    r "The story is you lost your memory, but... is that really it? Or did you... run away from something? Someone?"
    scene 61_s15 with dissolve
    mc "I... It's not a story worth telling. Trust me."
    scene 61_s16 with dissolve
    r "Come on! I poured my heart out *hic* you have to at least give me something. It's only fair."
    scene 61_s15 with dissolve
    mc "Well..."
    scene 61_s17 with dissolve
    r "Wha..."
    scene 61_s18 with Dissolve(1.0)
    avery "Rebecca!"
    scene 61_s19 with dissolve
    r "Huh...?"
    scene 61_s18 with dissolve
    avery "Where the hell were you? I've searched the entire damn castle!"
    scene 61_s19 with dissolve
    r "Why do you care? Just leave me alone!"
    scene 61_s18 with dissolve
    avery "You're drunk!"
    scene 61_s21 with dissolve
    mc "We were just talking. That's all."
    scene 61_s20 with dissolve
    avery "And you, [mc]? Didn't I assign you work? What the hell are you doing down here?"
    scene 61_s21 with dissolve
    mc "Can't I take a moment to breathe?"
    scene 61_s18 with dissolve
    avery "*sigh* Get up. Both of you—back to your quarters. Now."
    scene 61_s19 with dissolve
    r "Booo!"
    scene 61_s18 with dissolve
    avery "Rebecca... I'd rather not tell your mother about this."
    scene 61_s19 with dissolve
    r "Fine, fine... You're no fun."
    scene 61_s22 with dissolve
    r "My room?"
    scene 61_s23 with dissolve
    mc "Huh?"
    scene 61_s22 with dissolve
    r "Come back to my room..."
    scene 61_s23 with dissolve
    mc "Yeah... I'd love to."
    scene 61_s18 with dissolve
    avery "I can't believe this... You two aren't children anymore."
    scene 61_s19 with dissolve
    stop music fadeout 2.0 
    $ mc_friend_reb = True
    scene 61_s24 with Fade(1.5,1.0,1.0)
    r "Ugh! That stupid bitch! She thinks she can tell {i}me{/i} what to do. Acting all high and mighty while mom's away..."
    r "She's barely any older than me... Can you believe it? Who decides to have a child in their fifties?!"
    call screen scene61_choice02 with dissolve
    mc "Calm down, Rebecca. Let's get you to bed. It's late."
    scene 61_s42 with Fade(1.0,1.0,1.0)
    r "What are you standing there for?"
    r "Get in..."
    call screen scene61_choice01 with dissolve
    mc "Sorry, Rebecca. But I gotta go."
    r "H-Huh?! Where are you going?"
    $ mc_rejected_reb_first = True
    mc "We're drunk and I don't want us to do anything careless."
    r "But... I..."
    mc "Sleep well, Rebecca. I'll talk to you later."
    r "Wait..."
    if not mc_maia_left:
        scene 29_1_s52 with Fade(1.5,1.0,1.0)
        mc "(All I need is you, Maia...)"
    else:
        scene 26_s21 with Fade(1.5,1.0,1.0)
        ""
    jump scene55_taskboard

label scene61_choice02_op1:
    $ mc_kiss_reb1 = True
    scene 61_s47 with Dissolve(1.0)
    perception "Your hand moves almost of its own accord. It doesn't grab, but finds her shoulder, your touch firm yet gentle as you turn her to face you. Her eyes, wide with confustion."
    r "[mc]? W-What's wrong? What are you—"
    scene 61_s48 with Dissolve(1.0)
    perception "You don't answer with words. You lean in and close the distance, your lips meeting hers. Her initial shock is tiny, sharp intake of breath against your mouth, her body stiffening for a heartbeat."
    scene 61_s49 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss4.mp3" 
    empathy "And then... she melts. Her lips soften, moving against yours with a sudden, desperate passion, as if she'd been waiting for this very moment without ever admitting it. The taste of wine on her lips."
    r "Mhmmnnn~"
    scene 61_s50 with Dissolve(1.5)
    r "That... was... unexpected..."
    scene 61_s51 with dissolve
    mc "Consider this my first piece of evidence for my love to you."
    scene 61_s50 with dissolve
    r "You... I..."
    r "You can't just... do that..."
    scene 61_s51 with dissolve
    mc "*chuckles* I'm sorry for startling you. But I thought action might speak louder than words right now. Did it... help?"
    scene 61_s50 with dissolve
    r "It... it did. Quite a lot, actually."
    scene 61_s51 with dissolve
    mc "Good. Now, let's get you to bed. It's been a long day..."
    r "Mhm."
    scene 61_s42 with Fade(1.0,1.0,1.0)
    r "What are you standing there for?"
    r "Get in..."
    call screen scene61_choice01 with dissolve
    mc "Sorry, Rebecca. But I gotta go."
    r "H-Huh?! Where are you going?"
    $ mc_rejected_reb_first = True
    mc "We're drunk and I don't want us to do anything careless."
    r "But... I..."
    mc "Sleep well, Rebecca. I'll talk to you later."
    r "Wait..."
    if not mc_maia_left:
        scene 29_1_s52 with Fade(1.5,1.0,1.0)
        mc "(All I need is you, Maia...)"
    else:
        scene 26_s21 with Fade(1.5,1.0,1.0)
        ""
    jump scene55_taskboard
    
label scene61_2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p5_replay:
        $ persistent.scene4_p5_replay = True
    scene 61_s28 with Fade(1.0,1.0,1.0)
    perception "The warmth of her body radiates despite the distance. You can hear her faint breathing, slightly faster than usual."
    scene 61_s27 with dissolve
    r "...You're staring."
    scene 61_s28 with dissolve
    mc "Huh?"
    scene 61_s27 with dissolve
    r "You're staring at my chest."
    scene 61_s28 with dissolve
    mc "I'm not..."
    scene 61_s27 with dissolve
    r "Are you saying that I don't look pretty?"
    scene 61_s28 with dissolve
    mc "That's not what I said."
    scene 61_s27 with dissolve
    r "...Are you... uh... excited?"
    scene 61_s28 with dissolve
    mc "No... I mean, yes?"
    scene 61_s27 with dissolve
    r "...Because of me?"
    scene 61_s28 with dissolve
    mc "Who else?"
    scene 61_s29 with dissolve
    r "Your pants! They're... getting bigger!"
    scene 61_s30 with dissolve
    mc "It's because of you."
    scene 61_s29 with dissolve
    r "H-Huh?!"
    scene 61_s30 with dissolve
    mc "You look beautiful, Rebecca."
    scene 61_s29 with dissolve
    r "S-Shut up! And stop staring..."
    scene 61_s30 with dissolve
    mc "You're staring too..."
    scene 61_s29 with dissolve
    r "D-Does it hurt?"
    scene 61_s30 with dissolve
    mc "What are you talking about?"
    scene 61_s29 with dissolve
    r "When your... thingy gets big. Does it hurt?"
    scene 61_s30 with dissolve
    mc "If it's not taken care of, then yeah."
    scene 61_s29 with dissolve
    r "T-Taken care of? You mean..."
    scene 61_s30 with dissolve
    mc "Ahuh."
    scene 61_s29 with dissolve
    r "Can you... use your hand?"
    scene 61_s30 with dissolve
    mc "I guess I could..."
    mc "If only I had a beautiful wife to help with it..."
    r "..."
    scene 61_s27 with dissolve
    r "I-I can help... But just with my hand, okay? Don't get any other ideas."
    scene 61_s28 with dissolve
    mc "I wasn't going to ask, but if you insist."
    scene 61_s27 with dissolve
    r "J-Just close your eyes..."
    scene 61_s28 with dissolve
    scene 61_s32 with Dissolve(1.5)
    sensation "She pulls down your pants with trembling fingers, exposing your shaft. A soft gasp escapes her lips."
    scene 61_s31 with dissolve
    r "...It's... bigger than I expected."
    scene 61_s32 with dissolve
    mc "Thank you for the compliment."
    scene 61_s31 with dissolve
    r "D-Don't talk while I'm... ugh, you're impossible."
    scene 61_s41 with Dissolve(1.0)
    sensation "Her fingertips barely graze your shaft at first, feather-light, almost as if testing the temperature. Then she slowly wraps her hand around it. Her grip is clumsy, unsure, but warm."
    show 61_hj with Dissolve(1.0)
    r "...Is this too hard? Or too soft? I don't really know what I'm doing..."
    mc "It's fine. You're doing great."
    r "I feel like I'm petting a wild animal."
    mc "Start moving your hand up and down."
    r "Like... this?"
    sensation "Her hand starts to glide up and down, slow at first, with cautious curiosity. The strokes are uneven, but her soft palm and fingers feel heavenly."
    r "I can feel it throbbing... A-Am I supposed to squeeze more?"
    mc "You're already making it hard to hold back."
    r "You're breathing pretty heavily... Does that mean I'm doing well?"
    sensation "Every stroke sends a new wave of pressure building inside you. Her skin is soft and warm, the friction perfect despite her nervous pacing."
    r "Hahh... hah... This is... more difficult than I thought."
    call screen scene61_hj with dissolve

default scene61_hj_speed_first = True
label scene61_hj_faster:
    $ scene61_hj_speed = True
    if scene61_hj_speed_first:
        $ scene61_hj_speed_first = False
        mc "Try going a little faster."
        r "F-Faster? ...I'll try."
        scene black with Dissolve(0.3)
        show 61_hj_faster with Dissolve(0.3)
        hide 61_hj
        r "You're really squirming... Is it that good?"
        mc "Yeah... Keep going just like that..."
        sensation "Her pace increases, fingers tightening ever so slightly, her hand sliding easily now as your pre-cum coats her palm."
    else:
        scene black with Dissolve(0.3)
        show 61_hj_faster with Dissolve(0.3)
        hide 61_hj
        perception "Her strokes pick up speed, still uneven but more confident. Her soft palm glides slick over your shaft, the friction sending sharp pulses through your groin."
        r "Are you... finishing soon?"
    call screen scene61_hj with dissolve
    
label scene61_hj_slower:
    $ scene61_hj_speed = False
    mc "Slow down... nice and steady."
    r "A-Alright."
    scene black with Dissolve(0.3)
    show 61_hj with Dissolve(0.3)
    hide 61_hj_faster
    sensation "Her hand gently glids up and down your slick shaft. Her thumb brushes the sensitive ridge just below your tip on every pass."
    r "I can feel you twitching... it's kind of... cute."
    mc "You're driving me crazy..."
    call screen scene61_hj with dissolve

label scene61_hj_cum:
    mc "Rebecca... I'm close..."
    r "A-Ah! W-What do I do?!"
    mc "Don't stop—keep going!"
    show 61_hj_faster with Dissolve(0.3)
    hide 61_hj
    sensation "Her hand pumps faster now, slipping slightly from the slick wetness. You feel your whole body tense as your climax surges forward uncontrollably."
    mc "Here it comes...!"
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 61_s33 with vpunch
    sensation "Your cock pulses hard in her grasp as thick ropes of hot seed spurt upward, landing across her hand and arm. Rebecca freezes, her eyes wide as the warmth splatters over her fingers."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 61_s34 with vpunch
    r "O-Oh... Gods... that's... a lot..."
    scene 61_s36 with Dissolve(1.5)
    mc "Hahh..."
    scene 61_s35 with dissolve
    hide screen cum
    r "I-It's... sticky and warm..."
    scene 61_s36 with dissolve
    mc "Yeah..."
    scene 61_s35 with dissolve
    r "I didn't think... this would be so... intense."
    scene 61_s36 with dissolve
    mc "First time for everything."
    scene 61_s35 with dissolve
    r "S-Shut up..."
    r "It's... really warm. I didn't expect it to get everywhere like that."
    scene 61_s36 with dissolve
    mc "Sorry. You kind of caught me off guard with your amazing technique."
    scene 61_s35 with dissolve
    r "Amazing? I was just fumbling the whole time..."
    scene 61_s36 with dissolve
    mc "That's what made it hot."
    scene 61_s35 with dissolve
    r "H-Hot?!"
    r "*sigh* Go bring me a towel. Quickly."
    scene 61_s36 with dissolve
    mc "Aye, aye."
    $ renpy.end_replay()
    scene 61_s37 with Fade(1.0,1.0,1.0)
    r "I can't believe I just did that... with you..."
    r "Just... don't tell anyone, alright?"
    scene 61_s38 with dissolve
    mc "Of course. No one needs to know."
    scene 61_s37 with dissolve
    r "Good..."
    r "Tired now... more than before."
    scene 61_s38 with dissolve
    mc "Now {i}that's{/i} taken care of, thanks to you. I suppose we can sleep soundly."
    scene 61_s37 with dissolve
    r "Alright... J-Just don't get used to it..."
    scene 61_s38 with dissolve
    mc "Me? Never. Well... maybe tomorrow morning I might need you again."
    scene 61_s37 with dissolve
    r "What are you talking about?"
    scene 61_s38 with dissolve
    mc "It's called morning wood. My 'thingy,' as you call it, tends to get hard before I wake up."
    scene 61_s37 with dissolve
    r "You can take care of that yourself... I'm not... uh..."
    scene 61_s38 with dissolve
    mc "Jerking?"
    scene 61_s37 with dissolve
    r "I'm not jerking you every morning."
    scene 61_s38 with dissolve
    mc "What if I bring you tasty breakfast first?"
    r "..."
    scene 61_s37 with dissolve
    r "...Maybe."
    scene 61_s38 with dissolve
    mc "*chuckles* Goodnight, Rebecca."
    scene 61_s37 with dissolve
    r "...Goodnight."
    scene 61_s39 with Dissolve(2.0)
    perception "The soft rhythm of her breath fills the quiet room as you both drift into sleep."
    scene 61_s40 with Fade(2.0,1.0,1.0)
    mc "*yawn* Back to work."
    jump scene55_taskboard

label scene62:
    mc "That's the last of them. I should report back to Avery."
    stop music fadeout 2.0 
    scene 62_s1 with Fade(1.0,1.0,1.0)
    mc "Lady Avery."
    scene 62_s2 with dissolve
    avery "It's late, [mc]. Talk to me tomorrow."
    mc "I just wanted to say that all tasks are done."
    avery "Oh... Already?"
    mc "Yes."
    scene 62_s3 with dissolve
    avery "You're efficient. I like that."
    scene 62_s4 with dissolve
    mc "What now?"
    scene 62_s3 with dissolve
    avery "There's still one final task for you."
    scene 62_s4 with dissolve
    mc "Of course there is. What is it?"
    scene 62_s3 with dissolve
    avery "You know of the Queen of pleasure massacre, yes? My sister briefed you about it."
    scene 62_s4 with dissolve
    mc "I have."
    scene 62_s3 with dissolve
    avery "Then you know that one of the culprits—Katherine—was captured."
    avery "I need you to decide her fate."
    scene 62_s4 with dissolve
    mc "Kat's fate...?"
    scene 62_s3 with dissolve
    avery "Correct. The Queen has granted {i}you{/i} authority in this matter."
    avery "You may order her execution... or condemn her to a lifetime in the dungeon."
    avery "Personally, I consider the dungeon far worse."
    scene 62_s4 with dissolve
    mc "...Why me?"
    scene 62_s3 with dissolve
    avery "Perhaps because you share... history with her. Or because she's testing you. I'm not sure, really."
    avery "But do not misunderstand, [mc]. This is no favor. This is responsibility."
    scene 62_s4 with dissolve
    mc "I see..."
    scene 62_s3 with dissolve
    avery "What will it be?"
    scene 62_s4 with dissolve
    mc "I need to decide {i}now{/i}?"
    scene 62_s3 with dissolve
    avery "Why delay?"
    scene 62_s4 with dissolve
    mc "Can I go talk to her at least?"
    scene 62_s3 with dissolve
    avery "There's no need. The guards already questioned her."
    scene 62_s4 with dissolve
    mc "...You don't know. I might be able to get something."
    scene 62_s3 with dissolve
    avery "Do as you wish. You will only waste your time."
    scene 62_s4 with dissolve
    mc "Thank you."
    scene 62_s3 with dissolve
    avery "But you will not leave the dungeon until you've made your decision. The faster we're done with this, the better."
    scene 62_s4 with dissolve
    mc "Understood."
    scene 62_s5 with Fade(1.5,1.0,1.0)
    play music "dungeon.mp3" fadein 3.0 loop
    perception "The heavy iron door groans as you push it open. The familiar stench of mildew and damp stone curls into your nostrils."
    mc "Still smells just as weird..."
    scene 62_s6 with Fade(0.5,0.5,0.5)
    mc "Kat? Wake up."
    scene 62_s7 with dissolve
    kat "Huh!? Wha—!?"
    scene 62_s8 with Dissolve(1.0)
    kat "Oh, [mc]... Thank gods! Please—you have to help me! You can explain what really happened!"
    kat "You saw it! I barely even drew my sword—it was Gaius! He led the whole damn slaughter!"
    scene 62_s9 with dissolve
    mc "Gaius is too important to end up here. That's... the Queen's words, not mine."
    scene 62_s8 with dissolve
    kat "That's not fair! It's not fair!"
    kat "I did what I was told..."
    scene 62_s9 with dissolve
    mc "I know. But right now... I'm here to judge you."
    scene 62_s10 with dissolve
    kat "Oh—oh thank you, gods! You're my judge? Then I'm safe!"
    scene 62_s11 with dissolve
    mc "Why so optimistic?"
    scene 62_s10 with dissolve
    kat "Because it's you! You know me, you know I don't deserve this!"
    scene 62_s11 with dissolve
    mc "Actually... I was only given two options."
    mc "Either you're executed... or you stay in here."
    scene 62_s8 with dissolve
    kat "W-What...?! No! That... that can't be it!"
    scene 62_s9 with dissolve
    mc "I'm sorry. That's what Lady Avery told me."
    scene 62_s8 with dissolve
    kat "No... no, no, no..."
    kat "Please... I'm sure you can do something!"
    scene 62_s9 with dissolve
    ruby "{i}Tch.{/i} There is another way."
    mc "Hmm?"
    scene 4_s4_3 with dissolve
    mc "Ruby? ...I didn't even notice you back there."
    scene 62_s12 with dissolve
    ruby "Means I still got it."
    ruby "But like I said—there's a way out. Maybe."
    scene 4_s4_3 with dissolve
    kat "What? How?"
    mc "I'm listening."
    scene 62_s12 with dissolve
    ruby "You marry her."
    scene 4_s4_3 with dissolve
    mc "What?"
    scene 62_s12 with dissolve
    ruby "You're climbing up the hierarchy, right? You muse be pretty high up there if they're letting you play judge and jury."
    ruby "Siblings, partners, spouses... when you're tied to someone with power, the law tends to... look away."
    scene 4_s4_3 with dissolve
    kat "Wait—is that really how it works?"
    scene 62_s12 with dissolve
    ruby "Oh, you bet. This game's rigged from the start."
    ruby "*chuckles* A beautiful web of noble corruption."
    scene 4_s4_3 with dissolve
    kat "B-But how? We need papers, witnesses, right?"
    scene 62_s12 with dissolve
    ruby "Strictly speaking? No. A simple ring is enough to start. Paperwork can come later."
    scene 4_s4_3 with dissolve
    kat "A ring? Where are we supposed to find a ring here?!"
    scene 62_s8 with dissolve
    kat "[mc]—please! You can go out and get one, right?"
    kat "I'll pay you back every copper, I swear it! Just get me out of here!"
    scene 62_s9 with dissolve
    mc "Kat... I can't. Avery's orders. A guard escorted me all the way down here and is probably waiting outside the door right now."
    scene 62_s8 with dissolve
    kat "Then what are we supposed to DO?! Just let me die?!"
    scene 62_s9 with dissolve
    ruby "Relax, honey~"
    scene 4_s4_3 with dissolve
    kat "What?"
    scene 62_s13 with dissolve
    ruby "I've got one."
    scene 62_s14 with dissolve
    perception "A simple, slightly tarnished silver ring glints between her fingers."
    scene 62_s13 with dissolve
    ruby "Lifted it off a guard who got a little too handsy during a search. Consider it... a souvenir."
    scene 62_s14 with dissolve
    kat "W-What do you want for it? Please, I'll do anything!"
    if mc_helped_ruby:
        play music "kat.mp3" fadein 3.0 loop
        scene 62_s13 with dissolve
        ruby "My freedom would be nice."
        scene 62_s14 with dissolve
        kat "Uh... [mc]?"
        scene 62_s13 with dissolve
        ruby "I'm joking. You helped me before, [mc], so this is the least I can do."
        scene 62_s20 with vpunch
        ruby "Take it. Just don't forget me when you're wearing a damn crown someday, [mc]."
        scene 62_s21 with Dissolve(1.0)
        ""
        scene 62_s10 with Dissolve(1.0)
        kat "[mc]?"
        scene 62_s11 with dissolve
        mc "(Oh God... Am I really about to do this? Marry someone in a prison just to cheat execution? This is insane.)"
        mc "(But I guess I can explain it to her later. I can tell her it was just to save her life. She'll understand...)"
    else:
        scene 62_s13 with dissolve
        ruby "Who said anything about giving it away?"
        ruby "Do you think he cares for you as much as I think?"
        ruby "Regardless, I want him to suffer."
        scene 62_s15 with dissolve
        perception "With a wicked grin, she suddenly swallows the ring whole."
        scene 62_s16 with dissolve
        ruby "*gulp*"
        scene 62_s16 with vpunch
        kat "Y-YOU WHAT?!"
        scene 4_s4_3 with dissolve
        mc "Damn..."
        scene 62_s12 with dissolve
        ruby "Good luck, fucker. This is for not helping me with my sister."
        scene 62_s17 with dissolve
        kat "Oh gods... It's over..."
        scene 62_s18 with dissolve
    call screen scene62_choice01 with dissolve

label scene62_choice01_op1:
    $ mc_harem_kat = True
    mc "I've made my decision."
    scene 62_s10 with dissolve
    kat "P-Please...?"
    scene 62_s11 with dissolve
    mc "I'll marry you, Kat."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 62_s10 with dissolve
    kat "Oh thank you... Thank you!"
    scene 62_s22 with vpunch
    perception "She practically lunges toward the bars, shoving her trembling hands through the cold iron."
    hide screen stat_change with easeoutright
    $ karma_more = False
    kat "Please, take my hand..."
    scene 62_s23 with Dissolve(1.5)
    empathy "The dirty silver ring slides onto her finger. Her breath catches as her shoulders tremble with relief."
    mc "For better or worse..."
    scene 62_s25 with Dissolve(1.0)
    kat "*sniff* Thank you, [mc]... thank you..."
    scene 62_s24 with dissolve
    ruby "*chuckles* Well... this might be the most romantic thing I've seen down here."
    ruby "Almost makes me shed a tear. Almost."
    mc "That's it then?"
    ruby "*laughs* Sure. Now go explain it to your queen. Let's see how much she loves surprises."
    mc "Fuck... I didn't think about that."
    scene 62_s25 with dissolve
    kat "I'll be waiting for you, [mc]..."
    scene 62_s24 with dissolve
    jump scene62_2

label scene62_choice01_op2:
    $ karma_more = False
    stop music fadeout 1.0 
    $ mc_life_kat = True
    mc "I've made my decision."
    play music "dungeon.mp3" fadein 3.0 loop
    scene 62_s8 with dissolve
    kat "A-And what is it?"
    scene 62_s9 with dissolve
    mc "You'll rot in here, Kathrine. For the rest of your life."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 62_s17 with dissolve
    kat "No... No... NO!"
    kat "You coward!! How could you?!"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 62_s18 with dissolve
    mc "Goodbye, Kat."
    scene 62_s17 with vpunch
    kat "Please! Don't leave me here! I'll go mad! I can't— I CAN'T!"
    scene 62_s19 with Dissolve(1.4)
    kat "PLEASE, [mc]! PLEASE!"
    if mc_got_ring_ruby:
        kat "W-What about the ring?! We had a way out! WHY WON'T YOU HELP ME?!"
    if not mc_helped_ruby:
        ruby "Sorry, honey. Guess you'll be staying with me."
    elif mc_helped_ruby:
        ruby "He's choosing the easy path. That's how they all end up, once they taste power."
        ruby "You'll get yours, [mc]. Sooner or later."
    jump scene62_2

label scene62_choice01_op3:
    $ karma_more = False
    stop music fadeout 1.0 
    $ mc_execute_kat = True
    mc "I've made my decision."
    play music "dungeon.mp3" fadein 3.0 loop
    scene 62_s8 with dissolve
    kat "A-And what is it...?"
    scene 62_s9 with dissolve
    mc "You'll be executed, Kathrine."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 62_s18 with dissolve
    kat "..."
    perception "The words seem to suck the air out of her lungs. She freezes, eyes wide, lips parting—but no sound comes out."
    scene 62_s17 with dissolve
    kat "No... no, please... I-I don't want to die..."
    hide screen stat_change with easeoutright
    $ karma_less = False
    if mc_got_ring_ruby:
        kat "W-w-what about t-the ring?"
    scene 62_s18 with dissolve
    mc "Goodbye."
    scene 62_s17 with dissolve
    kat "Please... Mother... someone... help me!"
    scene 62_s19 with Dissolve(1.4)
    kat "*sob* I don't want to die! Not like this! PLEASE!"
    if not mc_helped_ruby:
        ruby "Sheesh... I'm really sorry, darling. Didn't know he was that heartless."
        ruby "You'll get what's coming to you one day, [mc]."
        ruby "I swear it."
    elif mc_helped_ruby:
        ruby "Figures. You're almost a noble now. You're all the same."
        ruby "You'll get what's coming to you one day, [mc]."
        ruby "I swear it."
    jump scene62_2

label scene62_2:
    $ mc_friend_reb = True
    if mc_maia_left:
        $ mc_marital = "divorced"
    elif not mc_maia_left:
        $ mc_marital = "married"
    $ mc_residency = "castle"
    $ mc_job = "royal_servant"
    stop music fadeout 2.0 
    scene 62_s26 with Fade(1.0,1.0,1.0)
    mc "It's dawn already."
    scene 62_s27 with Fade(1.0,1.0,1.0)
    if mc_harem_kat:
        mc "(Oh god... please let this go smoothly...)"
    mc "(Wait, where is she? She's supposed to be up by now.)"
    "*snore*"
    scene 62_s28 with dissolve
    mc "Hmm?"
    mc "(Is she... sleeping?)"
    scene 62_s29 with Dissolve(1.0)
    mc "*ahem* Lady Avery?"
    avery "Mmm... I can't help it, sis... *snore*... It keeps me going... Please don't tell father..."
    mc "..."
    scene 62_s29 with vpunch
    mc "Lady Avery?!"
    scene 62_s30 with dissolve
    avery "Wha-?!" 
    avery "Ah, [mc]... Give me a minute."
    scene 62_s32 with Fade(0.5,0.5,0.5)
    avery "*yawn* Excuse me. I appear to have underestimated the amount of work my sister has to do on the daily." 
    avery "So, how was it?"
    avery "I hope you didn't get too attached to her, considering her ultimate fate."
    scene 62_s31 with dissolve
    if mc_harem_kat:
        mc "I... married her."
        avery "..."
        scene 62_s34 with dissolve
        avery "Pardon me? I must have misheard. Could you repeat that?"
        scene 62_s33 with dissolve
        mc "I married her."
        scene 62_s34 with dissolve
        avery "I see."
        avery "[mc]... Tell me, why... out of all people in this entire kingdom... did you choose to marry the one person you absolutely weren't supposed to?"
        scene 62_s33 with dissolve
        mc "(Alright, here we go.)"
        mc "Lady Avery, the Queen herself once told me to marry and provide strong children for Irda's future. I had the kingdom's interests in mind."
        mc "Kat is a highly capable mercenary. Pair her skills with mine, and we could produce children well-suited for service to Irda."
        mc "Strong bloodlines. Future warriors. That was the Queen's vision, wasn't it?"
        avery "..."
        scene 62_s34 with dissolve
        avery "Gods above..."
        avery "Get out of my sight before I lose my composure. You {i}marriage{/i} is unfounded. Consider it canceled."
        scene 62_s33 with dissolve
        mc "Lady Avery, I do understand your anger... but killing a woman like Kat would waste valuable talent."
        mc "Besides, she never had a fair trial. This entire situation is politically... fragile."
        mc "How would the public react if they learned how justice has become?"
        scene 62_s34 with dissolve
        avery "You dare lecture me on justice?"
        scene 62_s34 with vpunch
        avery "Do you forget what she's done, [mc]? People DIED!"
        scene 62_s33 with dissolve
        mc "Gaius led that massacre, not her. She was just a simple pawn."
        mc "This kingdom's strength lies not only in its armies, but in its image. Executing her would set a very dangerous precedent."
        avery "..."
        scene 62_s34 with dissolve
        avery "Hnnngh... Fine. I get your point."
        avery "But understand this. You've overstepped your boundaries today, [mc]. And rest assured, I will report every word of this to my sister."
        scene 62_s33 with dissolve
        mc "I'm sure the Queen will understand. That's why she sits on the throne, and... you don't."
        play sound "sound_effects/slap03.mp3"
        scene 62_s35 with vpunch
        perception "a sharp slap cracks across your cheek. A vision of younger days appear for a brief moment before disappearing."
        mc "(Ow... can't believe this is my second royal slap. Slightly softer than last time, at least.)"
        scene 62_s33 with dissolve
        impulse "Strangle the life out of her—"
        mc "(No! Calm down...)"
        scene 62_s34 with dissolve
        avery "Get OUT of my face."
        scene 62_s33 with dissolve
        mc "As you wish."
        $ mc_friend_reb = True
    else:
        if mc_execute_kat:
            mc "I ordered her execution."
        elif mc_life_kat:
            mc "I ordered life in prison for here."
        scene 62_s32 with dissolve
        avery "I see."
        avery "A necessary decision. The weight of authority is not always pleasant, is it?"
        scene 62_s31 with dissolve
        mc "No... it's not."
        scene 62_s32 with dissolve
        avery "But you followed through. That's what matters."
        avery "You've shown me you're capable of making the hard choices, [mc]. That quality is... rare."
        scene 62_s31 with dissolve
        mc "Thank you."
        scene 62_s32 with dissolve
        avery "*yawn* Take the rest for now. My sister will want to speak to you when she returns."
        avery "And, [mc]... don't lose sleep over it."
        avery "Mercy is often... *yawn* a luxury we cannot afford. Got it?"
        scene 62_s31 with dissolve
        mc "Understood."
        scene 62_s32 with dissolve
        avery "Good."
        scene 62_s31 with dissolve
        mc "..."
        scene 62_s32 with dissolve
        avery "What? You can leave now."
        scene 62_s31 with dissolve
        mc "As you wish."
        mc "(Alright... now this time I'm taking my damn rest.)"
        scene 29_1_s52 with Fade(1.0,1.0,1.0)
        $ mc_reb_first_talk_ = True
        $ speech_cycle += 1
        $ reb_speech_cycle += 1
        $ in_scene54 = False
        $ in_scene64 = True
        $ cycle = 0
        $ mc_roam_reb_break = False
        ""
        $ mc_friend_reb = True
        
        if not mc_maia_left:
            $ mc_marital = "married"
        else:
            $ mc_marital = "divorced"
        $ mc_card_reg = True
        $ mc_job = "royal_servant"
        $ mc_residency = "castle"

        jump free_roam_main_label

label scene62_3:
    play music "kat.mp3" fadein 3.0 loop
    scene 62_s5 with Fade(1.5,1.0,1.0)
    ""
    scene 62_s25 with Fade(0.5,0.5,0.5)
    kat "[mc]! What happened?!"
    scene 62_s24 with dissolve
    mc "You're still crying?"
    scene 62_s25 with dissolve
    kat "*laughs* Sorry, I can't help it..."
    scene 62_s24 with dissolve
    mc "Well, all is good. Though... I may have just earned a permanent spot on Lady Avery's shit list."
    scene 62_s25 with dissolve
    kat "I... see. Well... thank you. Really."
    scene 62_s24 with dissolve
    mc "Don't mention it. Come on, let's get you out of here."
    scene black with Fade(0.5,0.5,0.5)
    perception "You signal the guard outside to unlock the cell. The door creaks open, and Kat steps out, breathing in as if the air outside the bars is somehow fresher."
    scene 62_s36 with Fade(0.5,0.5,0.5)
    kat "Ahhh~ Gods, it feels good to finally be out of that metal coffin."
    scene 62_s38 with Dissolve(1.5)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    kat "Mwah! My hero."
    scene 62_s37 with dissolve
    ruby "Hey lovebirds. Just a reminder—I'm still here, you know? Don't get too excited."
    scene 62_s39 with dissolve
    kat "Thank you too. I swear, I'll find a way to get you out of here one day."
    scene 62_s40 with dissolve
    ruby "It's Ruby. And sure, I'll hold you to that. Don't make me rot in here forever, sweetheart."
    scene 4_s4_3 with dissolve
    mc "Thank you, Ruby. I won't forget this."
    scene 62_s12 with dissolve
    ruby "*chuckles* Damn right you won't."
    scene 4_s4_3 with dissolve
    scene 62_s37 with Dissolve(1.5)
    mc "Come on, let's go before someone changes their mind."
    scene 62_s43 with Fade(1.0,1.5,1.0)
    mc "Can you take care of yourself from here? I doubt they'll let you near the castle. Especially not while Lady Avery's in charge."
    kat "Don't worry. I'll manage. I'll stay with Ava for now."
    mc "Would she let you stay with her?"
    scene 62_s41 with Dissolve(1.5)
    kat "Mhm. She owes me a few favors anyway. Besides, she's good at keeping secrets."
    kat "But you better come visit sometime, you know... since we're married and all."
    scene 62_s42 with dissolve
    call screen scene62_choice02 with dissolve
    scene 62_s41 with dissolve
    kat "I'll show you exactly what that means~"
    scene 62_s44 with vpunch
    mc "H-Hey! Careful where you grab..."
    scene 62_s41 with Dissolve(1.5)
    kat "I'll be waiting for my husband to come visit~ Don't keep me waiting too long."
    scene 62_s42 with dissolve
    mc "Take care of yourself, Kat. *chuckles* Try not to get arrested again before I get there."
    scene 62_s41 with dissolve
    kat "You too. Try not to miss me too much."
    scene 62_s42 with dissolve
    scene 62_s43 with Dissolve(1.5)
    mc "(Alright... now this time I'm taking my damn rest.)"
    $ speech_cycle += 1
    $ reb_speech_cycle += 1
    $ in_scene54 = False
    $ in_scene64 = True
    $ cycle = 0
    $ mc_roam_reb_break = False

    if not mc_maia_left:
        $ mc_marital = "married"
    else:
        $ mc_marital = "divorced"
    $ mc_card_reg = True
    $ mc_job = "royal_servant"
    $ mc_residency = "castle"

    if not mc_maia_left:
        scene 29_1_s52 with Fade(1.0,1.0,1.0)
    else:
        scene 26_s21 with Fade(1.0,1.0,1.0)
    $ mc_reb_first_talk_ = True
    jump free_roam_main_label

label scene62_choice02_op1:
    $ mc_harem_kat = False
    scene 62_s43 with Dissolve(1.5)
    mc "Kat. Look... about that. I need you to understand something. What I did in there... I only did it to save your life."
    kat "...Oh."
    kat "*chuckles* Right. Yeah. Sorry, I guess... I guess I should've known that already. Pretty stupid of me."
    mc "Don't take it personally. It wasn't about you. It was about not letting you die for nothing."
    scene 62_s41 with dissolve
    kat "Of course. I get it. And I'm still... I owe you my life. That's a bigger debt than a marriage."
    kat "But... that doesn't mean we can't still hang out and have some fun sometime, right?"
    scene 62_s42 with dissolve
    mc "*chuckles* I guess not."
    mc "Take care of yourself, Kat."
    scene 62_s41 with dissolve
    kat "You too, [mc]. And... thanks. For everything. Really."
    scene 62_s42 with dissolve
    $ mc_reb_first_talk_ = True
    $ speech_cycle += 1
    $ reb_speech_cycle += 1
    $ in_scene54 = False
    $ in_scene64 = True
    $ cycle = 0
    $ mc_roam_reb_break = False

    if not mc_maia_left:
        $ mc_marital = "married"
    else:
        $ mc_marital = "divorced"
        
    $ mc_card_reg = True
    $ mc_job = "royal_servant"
    $ mc_residency = "castle"

    if not mc_maia_left:
        scene 29_1_s52 with Fade(1.0,1.0,1.0)
    else:
        scene 26_s21 with Fade(1.0,1.0,1.0)
    ""
    jump free_roam_main_label

label scene64:
    scene 64_s1 with Fade(1.0,1.0,1.0)
    play music "soul.mp3" fadein 2.0 loop
    call screen scene64_free_roam1 with dissolve
    scene 64_s2 with Dissolve(1.5)
    call screen scene64_free_roam2 with dissolve
    scene 64_s3 with Dissolve(1.5)
    call screen scene64_free_roam3 with dissolve
    play sound "sound_effects/door.mp3"
    scene 64_s4 with Dissolve(1.5)
    ""
    scene 64_s5 with Dissolve(1.0)
    son "Papa?"
    if not mc_maia_left:
        stop music 
        scene 64_s6 with vpunch
        mc "AH! What the-?"
        mc "Hah... Fucking nightmares!"
        scene 64_s7 with Fade(1.0,1.0,1.0)
        play music "nature.mp3" fadein 2.0  volume 0.3 loop
        m "*yawn*"
        scene 64_s8 with Dissolve(1.0)
        m "...Oh? [mx]? You woke up early today."
        scene 64_s9 with Dissolve(1.0)
        mc "Morning, Maia. Sorry, I just couldn't sleep."
        scene 64_s10 with Dissolve(1.0)
        m "Why? Are you ill?"
        scene 64_s11 with dissolve
        mc "No. Don't worry about me. It happened all the time back when..."
        scene 64_s10 with dissolve
        m "Back when?"
        scene 64_s11 with dissolve
        mc "*chuckles* Forget it."
        scene 64_s13 with dissolve
        m "[mx]! I want to know more about you..."
        scene 64_s12 with dissolve
        mc "Do you now?"
        mc "Why'd you never ask before?"
        m "..."
        scene 64_s13 with dissolve
        m "B-Because I didn't want to talk about my past too. And... I assumed you would do the same."
        scene 64_s12 with dissolve
        mc "I would talk about mine if you did. How's that for a deal?"
        m "..."
        mc "Figured so. Don't worry, I won't push you to talk."
        scene 64_s13 with dissolve
        m "Thank you. But I promise I will one day when I..."
        scene 64_s12 with dissolve
        mc "When you gather up that courage. I know."
        scene 64_s13 with dissolve
        m "I also heard you managed to find the daughter of a really important person, [mx]."
        scene 64_s12 with dissolve
        mc "Hmm? Right, I guess I did. She was never lost though."
        scene 64_s13 with dissolve
        m "What do you mean?"
        scene 64_s12 with dissolve
        mc "She ran off on her own. I don't think she was too happy with being caught."
        scene 64_s13 with dissolve
        m "I see... I hope she's doing better now."
        play music "side_event4.mp3" fadein 2.0 loop
        scene 64_s15 with Dissolve(1.0)
        m "...Are you doing something today?"
        scene 64_s14 with dissolve
        mc "I'm not sure, I finished some tasks for Avery and she hasn't asked for me yet so I assume I'm good for today."
        scene 64_s15 with dissolve
        m "S-So... you're free then?"
        scene 64_s14 with dissolve
        mc "Maybe. If she has nothing for me then I might check out the guild. It's been a while since I've been there."
        mc "Why do you ask?"
        scene 64_s19 with dissolve
        m "I just thought maybe you wanted to you stay here... with me."
        scene 64_s18 with dissolve
        call screen scene64_choice01 with dissolve
    else:
        stop music 
        scene 64_s46 with vpunch
        mc "AH! What the-?"
        mc "Hah... Fucking nightmares!"
        scene 64_s47 with Fade(1.0,1.0,1.0)
        mc "*sigh* (Avery didn't call for me. I guess I'm free today.)"
        mc "(Maybe I'll visit the guild, it's been a while.)"
        jump scene65

label scene64_choice01_op1:
    $ maia_love -= 10
    mc "I'm afraid I can't Maia. I have to go now."
    scene 64_s17 with dissolve
    m "N-Not even a little bit?"
    scene 64_s16 with dissolve
    mc "Sorry, not even."
    scene 64_s17 with dissolve
    m "...I understand. Please take care, [mx]."
    scene 64_s16 with dissolve
    mc "I will. See you soon, Maia."
    stop music fadeout 2.0 
    m "..."
    jump scene65

label scene64_choice01_op2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene8_p5_replay:
        $ persistent.scene8_p5_replay = True
    scene 64_s18
    mc "I guess I can hang with my lovely wife for a bit."  
    scene 64_s19 with dissolve
    m "*giggles* Then... please relax."  
    scene 64_s18 with dissolve
    scene 64_s20 with Fade(0.5,0.5,0.5)
    mc "*sniff* *sniff* You smell really good..."
    m "S-Stop... that's embarrassing."
    if mc_maia_no_sex:
        scene 64_s23 with dissolve
        m "What do you want to do, [mx]?"
        scene 64_s22 with dissolve
        jump scene64_choice02_op3
    else:
        scene 64_s21 with Dissolve(1.0)
        m "Oh... [mx]. You just can't keep your hands to yourself~"  
        mc "Not with you this close to me."  
        scene 64_s23 with Dissolve(1.0)
        m "Hmm... sometimes I wonder if you're only with me because of my body..."  
        scene 64_s22 with dissolve
        mc "What!? Who told you that?"
        scene 64_s23 with dissolve
        m "*laughs* I'm just teasing~"  
        scene 64_s22 with dissolve
        mc "Oh? Getting bold, are we?"  
        scene 64_s23 with dissolve
        m "Do... do you like it, [mx]?"  
        scene 64_s22 with dissolve
        mc "I do. I love you even more when you speak your mind."  
        m "..."  
        scene 64_s23 with dissolve
        m "Y-You can move your hands further down, [mx]..."
        scene 64_s22 with dissolve
        call screen scene64_choice02 with dissolve

default s64_fp = False
default s64_fa = False

label scene64_choice02_op1:
    $ mc_virgin = False
    stop music fadeout 2.0 
    $ s64_fa = True
    scene 64_s24 with Dissolve(1.0)
    sensation "Your finger drifts down, circling the soft curve of her ass before finding its way to her tight ring."  
    m "[mx]! That's... that's my butt..."  
    mc "I know."  
    m "S-So you meant to do that... I thought you just—"
    play sound "se_sfx/sex/touch1.mp3" 
    scene 64_s25 with Dissolve(1.0)
    m "Ahhn~!"  
    sensation "Your finger pushes in slowly, stretching her delicate rim as her body clenches around you."  
    scene 64_s28 with Dissolve(1.0)
    m "Haaahh~! [mx]...!"  
    scene 64_s27 with dissolve
    mc "Relax, Maia. Just feel it."  
    scene 64_s26 with dissolve
    m "Mmhh~... y-you're so mean..."
    scene 64_s27 with dissolve
    mc "*chuckles* I love seeing your reactions when I play with your butt." 
    scene 64_s26 with dissolve 
    m "I... I can't help it..."  
    scene 64_s27 with dissolve
    sensation "She clenches tighter around your finger with every motion, her body trembling from the pleasure."  
    scene 64_s24 with Dissolve(1.0)
    m "Ahhn~"
    play sound "se_sfx/sex/touch4.mp3" 
    scene 64_s25 with Dissolve(1.0)
    m "[mx]! Hnnm~ Nghn~!"
    mc "Is it starting to feel good?"
    m "Y-Yes~!"
    jump scene64_2

label scene64_choice02_op2:
    $ mc_virgin = False
    stop music fadeout 2.0 
    $ s64_fp = True
    scene 64_s29 with Dissolve(1.0)
    sensation "Your fingers slide lower, brushing past her folds until you find her entrance, already wet."  
    m "Ahh... [mx]... you're touching me there..."  
    mc "You're soaked. Were you waiting for me to do this?"   
    scene 64_s30 with Dissolve(1.0)
    play sound "se_sfx/sex/touch2.mp3" 
    sensation "You press inside, two fingers slipping past her warm walls. She gasps, clutching your chest."  
    scene 64_s31 with Dissolve(1.0)
    m "Hhhhn~! It feels... too good..."  
    scene 64_s32 with dissolve
    mc "That's it. Let me hear more of your voice, Maia."  
    scene 64_s31 with dissolve
    m "Nnhhh~ [mx]... I-I can't hide it when you touch me like that..."
    scene 64_s32 with dissolve
    mc "Keep moaning."
    scene 64_s31 with dissolve
    m "Ahhhhn~ Hahhh~! [mx], go deeper... please!" 
    scene 64_s29 with Dissolve(1.0)
    sensation "Your fingers slide further, curling against her sweet spot as her hips buck against your hand." 
    play sound "se_sfx/sex/touch3.mp3" 
    scene 64_s30 with Dissolve(1.0)
    m "Nghnn! Y-Yes! Mhnn~! I'm gonna lose it...!" 
    play sound "se_sfx/sex/touch2.mp3" 
    scene 64_s29 with Dissolve(1.0)
    mc "God... you're making me rock hard."  
    jump scene64_2

label scene64_choice02_op3:
    mc "Why don't we just... relax for a bit?"
    if mc_maia_no_sex:
        scene 64_s23 with dissolve
        m "I... I'd like that."
    if not mc_maia_no_sex:
        scene 64_s26 with dissolve
        m "Hmm? [mc], it's fine, really. I'm your wife. It's my duty to—"
        scene 64_s27 with dissolve
        mc "I get it. But right now, we can just... be. Just you and me."
        scene 64_s23 with Dissolve(1.0)
        m "Oh. Of course. I... I'd like that."
    scene 64_s22 with dissolve
    mc "So... what's on your mind? When you're not taking care of a guy like me, what does Maia think about?"
    scene 64_s23 with dissolve
    m "Umm... It's silly."
    scene 64_s22 with dissolve
    mc "I'm an expert in silly thoughts."
    scene 64_s23 with dissolve
    m "Well... I've been training to cook with Ren for some time now."
    scene 64_s22 with dissolve
    mc "That's great to hear. How's your progress so far?"
    scene 64_s26 with dissolve
    m "N-Not good... I tried baking bread yesterday and I... I completely burnt it. It was a black, smoking brick."
    m "I almost set Ren's hair on fire trying to get it out of the oven. She was really angry."
    scene 64_s27 with dissolve
    mc "*chuckles* Wish I've been there to see it."
    scene 64_s23 with dissolve
    m "*giggles* Me too. You would have laughed."
    m "...What else do you want to know?"
    scene 64_s22 with dissolve
    mc "Hmm. What else indeed..."
    scene 64_s26 with Dissolve(1.0)
    m "[mc]... how is your relationship with Princess Rebecca?"
    scene 64_s27 with dissolve
    mc "Hmm? Do you really want to know about that? Now?"
    scene 64_s26 with dissolve
    m "I-It's fine if you don't want to say..."
    scene 64_s27 with dissolve
    mc "It's... doing fine. Better than fine, actually. I understand now what you were trying to tell me before."
    mc "She's... complicated. But she's good on the inside. Once you get past all the thorns."
    scene 64_s26 with dissolve
    m "Please take good care of her, [mc]. She puts on a brave face, but she's very sensitive."
    scene 64_s27 with dissolve
    mc "Even more than you?"
    scene 64_s26 with dissolve
    m "Yes... She's just much, much better at hiding it."
    scene 64_s27 with dissolve
    mc "I'll keep that in mind. Thank you, Maia."
    scene 64_s22 with dissolve
    if not mc_told_maia_nadia_sex:
        mc "You'll always be my favorite woman, Maia. No one's ever replacing you."
        empathy "She gives you a small, genuine smile."
    env "A cold draft slipped through the window, making you shiver."
    mc "...It's so cold."
    scene 64_s23 with dissolve
    m "Winter is right around the corner. You should really stop sleeping without a shirt, [mc]. You'll catch a cold."
    scene 64_s22 with dissolve
    mc "Maybe."
    scene 64_s23 with dissolve
    m "Well, for now, I'll keep you warm."
    scene 64_s20 with dissolve
    mc "I should probably go now, Maia."
    m "Aww... already? Can we cuddle for a little bit longer? Please?"  
    mc "*chuckles* Fine. Just a little."  
    m "Mmm... I love being like this with you..."  
    mc "Me too."  
    scene black with Fade(1.0,1.0,1.0)
    stop music fadeout 2.0 
    perception "Her breathing slows, eyelids fluttering shut as she drifts. You hold her close, letting the silence linger."  
    $ renpy.end_replay()
    jump scene65


image 64_hj1 = Movie(play="images/4_chapter3/scene64/64_hj1.webm", loop=True)
image 64_hj2 = Movie(play="images/4_chapter3/scene64/64_hj2.webm", loop=True)

image 64_hj1_2 = Movie(play="images/4_chapter3/scene64/64_hj1_2.webm", loop=True)

image 64_fa = Movie(play="images/4_chapter3/scene64/64_fa.webm", loop=True)
image 64_fp = Movie(play="images/4_chapter3/scene64/64_fp.webm", loop=True)

label scene64_2:
    scene 64_s31 with Dissolve(1.0)
    m "Hahh~! [mx]! I-It's not fair that only I feel good..." 
    scene 64_s33 with Dissolve(1.0)
    perception "Her trembling hands move down, fumbling at your pants."
    mc "Woah... You really are getting bolder, huh?"  
    m "I want to make you feel good too."  
    scene 64_s34 with Dissolve(1.0)
    perception "She pulls your cock free, her fingers wrapping around you with an eager grip."  
    scene 64_s35 with dissolve
    m "It's... so hot... and heavy..."  
    scene 64_s34 with dissolve
    mc "Mhhhn... Maia... your hands are just too soft."  
    show 64_hj1 with Dissolve(1.0)
    perception "Her pace quickens, strokes gliding smoother as precum slicks her palm. She watches your face, lips parted in awe."  
    m "I-I can feel it... pulsing... every time I move my hand."  
    mc "That's because you're making me hard as hell."  
    m "*giggles* So it really is because of me..."  
    m "It's leaking... ahh... there's so much..."
    mc "Rub it all over. It'll make it easier for you." 
    perception "She obeys, spreading your precum along your shaft, strokes now smoother, faster. Her lips part in awe as she stares at your cock in her hand."  
    m "You're throbbing so much... nghhh~"  
    mc "If you keep this up, I won't last long." 
    m "*whispers* Then let it all out for me, [mx]..."  
    scene black with Dissolve(0.3)
    if s64_fp:
        show 64_fp with Dissolve(1.0)
        hide 64_hj1
    elif s64_fa:
        show 64_fa with Dissolve(1.0)
        hide 64_hj1
    mc "I want you to lick it all when you're done."  
    m "I will. B-But... it has to be a big load."  
    mc "I'll give you the biggest one you've seen... Just keep... Ahh!"  
    perception "Her body twitches at your words, thighs pressing together as if your lustful promise arouses her just as much as her touch arouses you." 
    m "[mx]...? Are you about to...?"
    mc "Yeah. Take off your top, I wanna see your breasts."
    scene black with Dissolve(0.3)
    show 64_hj2 with Dissolve(1.0)
    hide 64_fp
    hide 64_fa
    m "You love my breasts don't you? You're always staring at them, [mx]~"
    mc "Fuck, Maia... I'm close."  
    m "Hahh~ Then... then cum for me. I want it... I want to see it all over my hand."  
    sensation "Your hips buck into her strokes as she milks you desperately, her grip tightening at the base while her thumb teases your sensitive tip."  
    m "It's going to come out, isn't it?"
    call screen scene64_choice04 with dissolve

label scene64_choice04_op1:
    scene black with Dissolve(0.3)
    show 64_hj1_2 with Dissolve(1.0)
    hide 64_fp
    hide 64_fa
    hide 64_hj2
    m "L-Look into my eyes when you ejaculate, [mx]."
    m "Pretend you're shooting it into my womb~"
    call screen scene64_choice04 with dissolve

label scene64_choice04_op2:
    scene black with Dissolve(0.3)
    show 64_hj2 with Dissolve(1.0)
    hide 64_fp
    hide 64_fa
    hide 64_hj1
    mc "I can't stop smelling your breasts. It's making me dizzy."
    m "*giggles* Go ahead and keep sniffing me, [mx]~"
    call screen scene64_choice04 with dissolve

label scene64_choice04_op3:
    scene black with Dissolve(0.3)
    if s64_fa:
        show 64_fa with Dissolve(1.0)
        hide 64_hj1
        hide 64_hj2
        hide 64_fp
        m "Nghn~! If you keep fingering my butt, I won't be able to hold still, [mx]~"
        call screen scene64_choice04 with dissolve
    elif s64_fp:
        show 64_fp with Dissolve(1.0)
        hide 64_hj1
        hide 64_hj2
        hide 64_fa
        m "Ahhnn~ All my juices will drip on the bed, [mx]~"
        mc "I don't mind."
        call screen scene64_choice04 with dissolve

label scene64_choice04_op4:
    mc "Don't stop!"
    show screen cum
    play sound "se_sfx/sex/sex_cum7.mp3" 
    scene 64_s36 with vpunch
    sensation "Heat surges up your shaft as your climax hits, thick ropes of cum shooting from your tip. The first spurt paints across her hand and wrist, splattering onto your belly."  
    m "Ahhh~! It's so hot... it just keeps coming!"  
    hide screen cum
    play sound "se_sfx/sex/sex_cum1.mp3" 
    scene 64_s37 with vpunch
    perception "She gasps in delight as more spurts cover her palm, dripping between her fingers, each one making her squirm with excitement. Your cock twitches violently in her grip as she milks out the last drops."
    scene 64_s38 with Dissolve(1.0)  
    m "I-I caught so much... it's so thick... nghhh..."  
    scene 64_s39 with dissolve
    perception "She looks at your cum-coated shaft, then back at her dripping hand, as if struggling between shock and fascination."  
    mc "Go on... scoop it all up and drink it." 
    scene 64_s41 with dissolve
    m "Umm... [mx]..."  
    scene 64_s40 with dissolve
    mc "You promised, didn't you?"  
    scene 64_s41 with dissolve
    m "I-I know. It's just that... there's so much!"  
    scene 64_s40 with dissolve
    mc "*chuckles* Fruits of your labor."  
    scene 64_s41 with dissolve
    m "I don't know if I can... My mouth will smell like your seed for the rest of the day."
    scene 64_s40 with dissolve
    call screen scene64_choice03 with dissolve

label scene64_choice03_op1:
    mc "No excuses, Maia. You worked me this hard—now you'll taste every drop." 
    scene 64_s41 with dissolve
    m "As you wish, [mx]..."
    scene 64_s40 with dissolve
    scene 64_s42 with Fade(0.5,0.5,0.5)
    perception "Her trembling fingers gather the thick mess pooling in her palm. She stares at it, blushing furiously, before bringing it to her lips."  
    scene 64_s43 with Dissolve(1.0)
    play sound "se_sfx/lick/1_lick1.mp3" 
    m "*slurps*... it's warm... ahhnnn..."  
    play sound "se_sfx/blowjob/swallow4.mp3" 
    m "*slurps* Mmm..."
    perception "Her tongue flicks out, tentative at first, then bolder as she licks her hand clean. Sticky strands stretch between her fingers and mouth as she forces herself to swallow."  
    mc "That's it... good girl."  
    mc "Show me your mouth."
    scene 64_s44 with Dissolve(1.0)
    m "I-I did it... I drank all of it..."  
    mc "Mhhhn... you look so damn sexy right now. My perfect little wife."  
    scene 64_s45 with dissolve
    perception "She collapses against your chest, still trembling, but smiling faintly with pride." 
    jump scene64_3

label scene64_choice03_op2:
    mc "Relax. You don't need to force yourself. You've already made me feel amazing."  
    scene 64_s38 with dissolve
    m "R-Really...? Thank you..."  
    scene 64_s39 with dissolve
    mc "You're too precious."  
    scene 64_s45 with Dissolve(1.0)
    perception "She cuddles close, resting her head on your chest as her messy hand clings to you. The scent of semen lingers in the air."  
    m "I'm glad... I made you feel good, [mx]..."  
    mc "And I'll return the favor soon."  
    m "Mhm~"
    jump scene64_3
    
label scene64_3:
    m "I'm... feeling sleepy."  
    mc "But you just woke up."
    m "It takes a lot of energy to move your arm up and down so much, [mx]!"  
    m "You should try it yourself." 
    mc "*chuckles* Don't worry, I believe you."  
    mc "I should probably go now, Maia."  
    m "Aww... already? Can we cuddle for a little bit at least?"  
    mc "*chuckles* Fine. Just a little."  
    m "Mmm... I love being like this with you..."  
    mc "Me too."  
    scene black with Fade(1.0,1.0,1.0)
    perception "Her breathing slows, eyelids fluttering shut as she drifts. You hold her close, letting the silence linger." 
    $ renpy.end_replay() 
    jump scene65

label scene65:
    scene 65_s1 with Fade(1.0,1.0,1.0)
    if mc_rejected_wedding_reb:
        ""
        jump scene66
    else:
        r "[mc]! Over here!"  
        play music "reb.mp3" fadein 2.0 loop
        scene 65_s3 with Dissolve(1.5)
        mc "Hey, Rebecca." 
        scene 65_s2 with dissolve
        r "What do you think?"
        scene 65_s4 with Dissolve(1.2)
        ""
        scene 65_s5 with Dissolve(1.2)
        r "Hehe~"
        scene 65_s3 with Dissolve(1.2)
        mc "Woah, Is that real gold?"
        scene 65_s2 with dissolve
        r "You bet it is. Custom made in Eurnia. Took a month for the artisans to weave it and another for the ship to brave the seas. So? Your final verdict?"
        scene 65_s3 with dissolve
        call screen scene64_choice05 with dissolve


label scene64_choice05_op1:
    $ mc_liked_reb_dress = True
    mc "You look absolutely beautiful, Becky."
    scene 65_s6 with dissolve
    r "*giggles* I already knew that, of course... but it sounds so much nicer coming from you. Thank you."
    jump scene65_2

label scene64_choice05_op2:
    mc "If I'm being honest? I liked your older, simpler outfit more."
    scene 65_s8 with dissolve
    r "What?! Seriously? You're joking. You have to be joking. You prefer common linen over Eurnian silk and gold?!"
    scene 65_s9 with dissolve
    mc "Mhm. It suited you better. It felt more... Rebecca. This feels like you're playing dress up as a queen."
    scene 65_s8 with dissolve
    r "Ugh! So much for my excitement to show you..."
    scene 65_s9 with dissolve
    mc "Don't get me wrong, you're still beautiful. I'm just talking about the outfit."
    scene 65_s8 with dissolve
    r "Whatever..."
    jump scene65_2

label scene65_2:
    scene 65_s2 with dissolve
    r "So, where are you off to in a hurry anyway?"
    scene 65_s3 with dissolve
    mc "The guild. Just... felt like making myself useful."
    scene 65_s8 with dissolve
    r "Why? Is Avery sending you off on another dreary quest again?"
    scene 65_s9 with dissolve
    mc "No. Just... felt like going myself."  
    scene 65_s8 with dissolve
    r "You're always out there. Can you not sit on your ass for a single day? The city won't crumble because you took the day off, you know?"
    scene 65_s9 with dissolve  
    mc "Funny. I keep wishing for a day of rest, but when it comes, I never know what to do with myself." 
    scene 65_s8 with dissolve
    r "Well, I suppose I won't stop you. If you're helping the guild, you're helping the city too."  
    scene 65_s2 with dissolve
    r "But when you're done... come back quick. I'm tired of playing it safe. And I'm bored." 
    scene 65_s3 with dissolve
    mc "What do you mean?"  
    scene 65_s2 with dissolve
    r "I want to... spice things up. Between us. You may be forbidden from entering me, but that doesn't mean there isn't an entire book to explore~"
    scene 65_s3 with dissolve
    mc "Oh? Didn't take you for that type."  
    scene 65_s2 with dissolve
    r "There's a lot you don't know about me. I'm not some delicate flower who just kisses her champion and then falls asleep. I have... appetites."
    scene 65_s3 with dissolve
    mc "...Let me guess. You got these ideas from a book. One of those smutty romances hidden under your bed. They're popular in... well, any time period."
    scene 65_s8 with dissolve
    r "I—! That's—! No, I most certainly did not!"
    scene 65_s9 with dissolve
    mc "You definitely did."  
    scene 65_s8 with dissolve
    r "Ugh! Whatever the source, just... come back quickly."
    scene 65_s6 with dissolve
    r "...And don't get yourself hurt doing something stupid."
    scene 65_s7 with dissolve
    mc "*chuckles* Got it, princess. I'll return soon."  
    scene 65_s9 with dissolve
    r "*ahem*"
    mc "...Was there something else?"
    scene 65_s8 with dissolve
    r "You're seriously going to leave without even trying to touch me? What kind of husband are you?"
    scene 65_s9 with dissolve
    mc "*chuckles* I don't know, Becky... I thought that touching the princess without permission in a public hallway might get me thrown {i}under{/i} the dungeon."
    scene 65_s2 with dissolve
    r "Maybe if there {i}were{/i} people around. But it's empty here. Which means..."
    r "...you'd better be quick before a guard walks by~"
    scene 65_s3 with dissolve
    call screen scene64_choice06 with dissolve

label scene64_choice06_op2:
    $ mc_grope_reb = True
    scene 65_s10 with Dissolve(1.2)
    sensation "Acting on her invitation, you reach out and cup her breast through the fine silk of her dress. The shape fits perfectly in your palm, firm yet soft."
    r "Ahh~ Mmm... H-Hey... easy there..."
    scene 65_s11 with Dissolve(1.0)
    mc "Fuck... you're so hot."
    scene 65_s12 with dissolve
    r "Enough, y-you idiot. Don't go getting your thingy all hard on me. You've got your guild to run to... and I've unfortunately got a courtly dinner to pretend to enjoy."
    r "Now, be a good boy and take your hand back."
    scene 65_s11 with dissolve
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene64_choice07 with dissolve

label scene64_choice07_op1:
    $ mc_grope_reb_ass = True
    scene 65_s13 with Dissolve(1.0)
    stop music fadeout 2.0 
    sensation "Your hand slides down from her breast, over the curve of her hip, and gives her ass a firm squeeze."
    r "Ah! Hey!"
    r "Dammit, [mc]! I said enough!"
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    mc "What? I couldn't resist."
    r "..."
    mc "What's wrong? I thought—"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 65_s14 with dissolve
    r "You thought you could just do whatever you want?"
    r "I'm not your toy, you know? I give an inch, and you take a mile."
    r "When I tell you to stop, you stop."
    scene 65_s9 with dissolve
    mc "I'm sorry, I just—"
    scene 65_s8 with dissolve
    r "I'm not mad. I'm... frustrated. Just... go. Go to your guild."
    scene 65_s9 with dissolve
    mc "..."
    scene black with Fade(1.0,1.0,1.0)
    empathy "Her tone makes it clear the conversation is over. She turns away, not giving you another glance."
    jump scene66

label scene64_choice07_op2:
    mc "Fine... I'll calm him down. For now."
    scene 65_s2 with dissolve
    r "*giggles* I suppose you won't be gone too long now, huh?"
    scene 65_s3 with dissolve
    mc "Not with something this pretty waiting for me."
    scene 65_s2 with dissolve
    r "Heh. See you~"
    stop music fadeout 2.0 
    scene 65_s3 with dissolve
    jump scene66

label scene64_choice06_op1:
    mc "I'm not gonna risk it, Becky. Someone could still walk in."
    scene 65_s8 with dissolve
    r "Tch. Always so careful. It's annoying."
    scene 65_s9 with dissolve
    mc "Hey, you'd never forgive me if a guard saw me squeezing the princess in the hallway."
    scene 65_s8 with dissolve
    r "...True."
    scene 65_s9 with dissolve
    mc "I'll make it up to you later."
    scene 65_s2 with dissolve
    r "You'd better. Or I'll drag you to my room myself."
    scene 65_s3 with dissolve
    mc "Looking forward to it."
    scene 65_s2 with dissolve
    r "Heh. Now get going~"
    stop music fadeout 2.0 
    scene 65_s3 with dissolve
    jump scene66

label scene64_choice07_op1_fail:
    $ renpy.notify("Check failed!")
    mc "(I... I can't. She told me to get my hands off.)"
    empathy "There's a flicker of respect in her eyes at your restraint."
    call screen scene64_choice07 with dissolve

label scene66:
    scene 66_s1 with Fade(1.0,1.0,1.0)
    ""
    play music "side_event2.mp3" fadein 2.0  volume 0.3 loop
    scene 66_s2 with Dissolve(1.5)
    alice "Ah, [mc]. Perfect timing. I was looking for you."
    scene 66_s3 with dissolve
    mc "Alice? What's up?"
    scene 66_s4 with vpunch
    alice "Recruit!"
    scene 66_s5 with dissolve
    joan_ "Y-Yes, ma'am!"
    scene 66_s4 with dissolve
    alice "Introduce yourself."
    scene 66_s6 with dissolve
    joan "I-I'm Joan, ma'am! Guard recruit assigned to Irda's northern post! Rank: Trooper, ma'am!"
    scene 66_s7 with dissolve
    perception "She snaps to attention, but her voice cracks halfway through the sentence. A guard standing nearby chuckles under his breath."
    mc "...What's happening here?"
    scene 66_s4 with Dissolve(1.0)
    alice "This is Trooper Joan. The newest addition to our post. Joan, this is [mc]. He serves Her Majesty directly."
    scene 66_s3 with dissolve
    mc "I see. Hey, Joan."
    scene 66_s9 with dissolve
    joan "S-Sir!"
    scene 66_s8 with dissolve
    mc "At ease soldier!"
    scene 66_s9 with dissolve
    joan "Y-Yes— I mean, no— I mean... understood!"
    scene 66_s8 with dissolve
    mc "*laughs* Sorry, couldn't resist. I've always wanted to say that."
    scene 66_s2 with dissolve
    alice "*sigh* Case in point."
    alice "Basically, I want you to train her, [mc]."
    scene 66_s3 with dissolve
    mc "Train her? What about Adam? He's the one who's been drilling me."
    scene 66_s2 with dissolve
    alice "Sargent Adam doesn't train women. Says he doesn't like to hit them."
    scene 66_s3 with dissolve
    mc "Huh. That's one way to dodge work."
    scene 66_s2 with dissolve
    alice "Normally, the job falls on Captain Roana, but she's away on an important mission."
    scene 66_s3 with dissolve
    mc "Still... why me?"
    scene 66_s2 with dissolve
    alice "Why not you? You've accomplished more for her majesty than half the men here combined. Word is you even fought off a werewolf."
    alice "You have real world experience. That's more valuable than any training manual. You're more than capable, as far as I can see."
    scene 66_s3 with dissolve
    mc "Hmm..."
    call screen scene66_choice01 with dissolve

label scene66_choice01_op2:
    scene 66_s11 with Dissolve(1.0)
    mc "I appreciate the offer, Alice, but I can't. You'll need to find someone else. Adam will have to get over himself."
    scene 66_s10 with dissolve
    alice "...Hmph. Very well. I'm in no position to force you."
    scene 66_s11 with dissolve
    perception "Alice's eyes narrow slightly. She doesn't argue, but you can feel her judgment weighing on you."
    joan "..."
    empathy "Joan lowers her gaze, clearly disappointed. She shuffles her feet, as if your refusal is a personal indictment of her potential."
    scene black with Fade(1.0,1.0,1.0)
    alice "Come along, recruit. It seems we'll have to find another... arrangement."
    jump scene67

label scene66_choice01_op1:
    $ mc_accept_joan = True
    mc "Alright. I'll do it."
    scene 66_s2 with dissolve
    alice "Good. Then she's your responsibility now."
    scene 66_s4 with dissolve
    alice "Trooper Joan! [mc] is your acting instructor effective immediately. You will obey his orders as you would my own. Is that clear?"
    scene 66_s5 with dissolve
    joan "Y-Yes, ma'am! I-I'm honored to be under your service, sir!"
    scene 66_s2 with dissolve
    alice "I'll leave you with her then. And [mc], I will be visiting you weekly for reports on her progress."
    scene 66_s3 with dissolve
    mc "Understood."
    scene 66_s12 with Dissolve(1.5)
    perception "Alice strides away, leaving you alone with Joan. The recruit looks like she's about to explode from nervous energy."
    empathy "She looks at you with a mixture of awe and panic."
    joan "..."
    mc "Well... I have things to attend to today, Joan. Consider this a day off."
    scene 66_s13 with dissolve
    joan "A-As you wish, sir!"
    scene 66_s12 with dissolve
    mc "(Actually... she just accepted that without question. If she's going to follow my orders blindly... maybe I can test this a little.)"
    mc "Hold on. On second thought, I might have a small task for you first."
    scene 66_s13 with dissolve
    joan "What are your orders, sir?"
    scene 66_s12 with dissolve
    call screen scene66_choice02 with dissolve

label scene66_choice02_op1:
    mc "Give me your best... cute pose."
    scene 66_s13 with dissolve
    joan "C-Cute... p-pose, sir...?"
    scene 66_s12 with dissolve
    mc "Mhm."
    scene 66_s14 with Dissolve(1.5)
    perception "Her entire face flushes red. After a few seconds of fidgeting, she awkwardly lifts her hands into what might be bunny ears and forces the stiffest smile you've ever seen."
    mc "*chuckles* ...Not bad."
    mc "That's all, Joan. You can leave now."
    scene 66_s16 with Dissolve(1.0)
    stop music fadeout 2.0 
    joan "Yes, sir..."
    jump scene67

label scene66_choice02_op2:
    mc "Hmm. My boots are looking a little dull from all that walking. A good soldier maintains her kit... and her instructor's. Polish them."
    scene 66_s13 with dissolve
    joan "S-Sir? Polish your...?"
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 66_s12 with dissolve
    mc "You heard me, recruit. Hop to it."
    scene 66_s15 with Dissolve(1.5)
    hide screen stat_change with easeoutright
    $ karma_less = False
    perception "She kneels quickly, nearly fumbling as she digs a cloth from her belt. The earnest way she scrubs makes it hard not to laugh."
    mc "That's enough. Stand up."
    scene 66_s12 with dissolve
    mc "That's all. Dismissed."
    scene 66_s16 with Dissolve(1.0)
    stop music fadeout 2.0 
    joan "Yes, sir..."
    jump scene67

label scene66_choice02_op3:
    mc "(No. Abusing my power isn't right. I need to build trust, not break her spirit.)"
    mc "On second thought... nevermind. You have the day off. Dismissed."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 66_s13 with dissolve
    joan "...Yes, sir."
    scene 66_s12 with dissolve
    scene 66_s16 with Dissolve(1.0)
    perception "She bows awkwardly and nearly trips over her own feet as she hurries off."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene black with Fade(0.5,0.5,0.5)
    stop music fadeout 2.0 
    mc "*sigh* (Poor girl's going to break before the training even begins.)"
    jump scene67

label scene67:
    play music "guild.mp3" fadein 2.0  volume 0.3 loop
    scene 67_s1 with Fade(1.0,1.0,1.0)
    ""
    scene 67_s3 with Fade(0.5,0.5,0.5)
    eireen "*sigh* I told you, Negumi. There's... nothing for you."
    scene 67_s2 with dissolve
    negumi "Impossible! Search thoroughly, there has to be something!"
    scene 67_s3 with dissolve
    eireen "Gods..."
    scene 67_s5 with Dissolve(1.5)
    mc "Hey, Eireen."
    scene 67_s4 with dissolve
    eireen "Hello, [mc]. Glad to have you back."
    scene 67_s5 with dissolve
    mc "Thanks. I wanted to see if there's anything I can help with... but judging by what I just heard, maybe not."
    scene 67_s4 with dissolve
    eireen "Not exactly. There is work, well, one of Able's men specifically asked for you."
    scene 67_s5 with dissolve
    if mc_accept_helped_nadia:
        mc "Able? I knew this day would come eventually. I met one of his men."
        scene 67_s7 with dissolve
        eireen "[mc], why in the world did you get close to him?"
        eireen "Did no one warn you about his reputation? Now that you have ties with Her Majesty, it's better not to deal with him at all."
        scene 67_s6 with dissolve
        mc "I didn't make a deal or anything. Just took care of something for a woman. That's it."
    else:
        mc "Able? The guy who supposedly owns the market?"
        scene 67_s7 with dissolve
        eireen "[mc], why would you even deal with that man?"
        scene 67_s6 with dissolve
        mc "I didn't. Never talked to him before."

    scene 67_s7 with dissolve
    eireen "If you have no ties with him, don't go."
    scene 67_s6 with dissolve
    mc "I don't have anything else to do today so might as well see what he has to say, right?"
    scene 67_s7 with dissolve
    eireen "I'd advise against it... but the choice is yours. Her Majesty won't be happy about it though."
    scene 67_s6 with dissolve
    scene 67_s9 with Dissolve(1.0)
    negumi "Hey! Stop ignoring me!"
    scene 67_s8 with dissolve
    eireen "Negumi, I've told you many times—there's nothing suitable for your experience. Come back tomorrow."
    scene 67_s9 with dissolve
    negumi "Then give me something {i}above{/i} my experience! I can do it!"
    scene 67_s8 with dissolve
    eireen "No. And I won't argue with you."
    scene 67_s9 with dissolve
    negumi "W-Where do you expect me to sleep today without coin!?"
    scene 67_s8 with dissolve
    eireen "You earned plenty from your last task. Am I to believe that you blew it all already?"
    negumi "..."
    scene 67_s10 with Dissolve(1.0)
    negumi "Hey you. I'm coming with."
    scene 67_s11 with dissolve
    mc "Excuse me?"
    scene 67_s14 with Dissolve(1.0)
    negumi "Heh~ Let me introduce myself."
    scene 67_s15 with Dissolve(1.0)
    negumi "I am called Negumi, the most powerful of all fire magicians! And she who is the harbinger of DOOM!"
    play sound "sound_effects/woosh1.mp3"
    scene 67_s12 with vpunch
    negumi "Behold, mortal!"
    scene 67_s13 with dissolve
    mc "..."
    eireen "..."
    perception "A nearby adventurer coughs awkwardly."
    eireen "No fire magic inside the guild quarters, Negumi. Put down your staff."
    scene 67_s10 with Dissolve(1.0)
    negumi "Now that you know who I am, I will be accompanying you."
    negumi "You see, I'm not exactly... thriving coin wise. As a reward for helping you, you will compensate me."
    scene 67_s11 with dissolve
    mc "...You'll help me?"
    scene 67_s10 with dissolve
    negumi "Yes! Be grateful. And don't worry, I shan't ask for much."
    scene 67_s11 with dissolve
    mc "Right... And if I refuse?"
    scene 67_s16 with dissolve
    negumi "R-Refuse!? Why would you even consider that?"
    negumi "The most powerful fire magician is at your service and you'd brush me off? Tch, tch. Foolish mortal."
    scene 67_s4 with dissolve
    eireen "*whispers* {size=30}[mc], please take her with you.{/size}"
    eireen "{size=30}As you can see, she's been spouting the same nonsense for an hour. You'll be doing me a favor.{/size}"
    scene 67_s17 with dissolve
    mc "*sigh* Fine. Negumi, I guess you can come along."
    scene 67_s10 with dissolve
    negumi "You won't be disappointed!"
    scene 67_s11 with dissolve
    eireen "*ahem* [mc], once you're done with Able, come back. I need to talk to you about something else."
    scene 67_s4 with Dissolve(1.0)
    eireen "One more thing. You don't have to agree to whatever he asks you of right away, alright?" 
    scene 67_s5 with dissolve
    mc "Yeah. I'll just see what he wants first."
    scene 67_s11 with dissolve
    stop music fadeout 2.0 
    mc "Let's go, Negumi."
    
    scene 67_s18 with Fade(1.0,1.0,1.0)
    play music "side_event1Talking.mp3" fadein 1.0 loop
    env "The tavern is filled with sound of chatter and clinking glasses. Patrons are from a dozen different races. The air is thick with smoke and the smell of ale."
    scene 67_s19 with Fade(0.5,0.5,0.5)
    tom "You. Upstairs."
    tom "The woman stays here."
    scene 67_s20 with dissolve
    negumi "What!? No! I'm coming too!"
    scene 67_s21 with dissolve
    tom "And who the hell are you supposed to be?"
    scene 67_s22 with dissolve
    negumi "E-Excuse me!? Don't you know who—"
    scene 67_s21 with dissolve
    mc "Stay here, Negumi. I won't be long."
    scene 67_s22 with dissolve
    negumi "Ngh... fine..."
    negumi "...Baldy."
    scene 67_s21 with dissolve
    tom "What did you say?!"
    scene 67_s22 with dissolve
    negumi "N-Nothing!"
    stop music fadeout 2.0 
    scene 67_s21 with dissolve
    scene 67_s23 with Fade(1.0,1.0,1.0)
    play music "side_event5Talking.mp3" fadein 2.0 loop
    denovan_ "Forgive me, brother. But I must ask you to surrender any weapons you have with me."
    scene 67_s24 with dissolve
    able "Let him through, son! Can't you see? Our guest {i}is{/i} the weapon."
    scene 67_s25 with Fade(0.5,0.5,0.5)
    able "[mc]! Welcome, welcome."
    able "I would shake your hand, but you caught me at a bad time. Please, sit."
    scene 67_s27 with Dissolve(1.0)
    perception "You try your best to ignore the bizarre sight but your eyes betray you. A woman is laying on her stomach, perfectly still, serving as a living table."
    empathy "Her eyes are vacant and unblinking. She doesn't seem to register your presence at all."
    mc "Eireen said you wanted to meet."
    scene 67_s26 with dissolve
    able "That I did, that I did! You've caught our attention, [mc]."
    able "Some men stumble into gold, the rest of us just watch it happen. Me? I'd rather walk alongside the lucky ones... maybe leech a little sparkle while I'm at it~."
    scene 67_s27 with dissolve
    mc "...That's honestly kind of creepy."
    scene 67_s26 with dissolve
    able "*chuckles* Creepy? No, no, no. Think of it more like... professional curiosity."
    able "When a man has potential, it's only natural that someone who needs it takes notice. Don't you agree?"
    scene 67_s27 with dissolve
    mc "And what exactly does a man like you need from me? You already have your posse."
    scene 67_s26 with dissolve
    able "Oh, [mc]! You think too small, darling. And that's why I like you."
    scene 67_s27 with dissolve
    mc "Huh?"
    scene 67_s26 with dissolve
    able "Your heart's in the right place... it just needs a little nudge. Nothing major. A touch of guidance. A kind hand."
    scene 67_s27 with dissolve
    mc "Just get to the point, man."
    scene 67_s28 with dissolve
    able "Straightforward! I {i}love{/i} that! It's a man's way. Straight to it. No pointless details, no emotional riffraff."
    scene 67_s26 with dissolve
    able "Very well. A servant of mine... ran away, not long ago. A dreadful business."
    scene 67_s27 with dissolve
    if mc_accept_helped_nadia:
        vic "For the love of tits, Able, just let it go. She's probably dead by now."
    else:
        vic_ "For the love of tits, Able, just let it go. She's probably dead by now."
    scene 67_s31 with dissolve
    able "Not that one, Vic! A different girl. A lovely little thing. Though, I'll always keep an eye out for her too, of course."
    scene 67_s30 with dissolve
    mc "Why did she run away?"
    scene 67_s29 with dissolve
    able "Your guess is as good as mine. My girls are kept in excellent condition. A roof over their heads, three meals a day, and most importantly..."
    able "...discipline. Without that, they'd have no sense of purpose."
    scene 67_s30 with dissolve
    mc "Discipline, huh. How's that work with you?"
    scene 67_s29 with dissolve
    able "You let them slack, they wander. You keep them in line, they stay loyal. Simple as that."
    scene 67_s30 with dissolve
    mc "Do you even know where she might be?"
    scene 67_s29 with dissolve
    able "That's where you come in. My best guess? The old king's forest north of the city."
    able "Not far enough to escape the city's reach, not close enough to be found easily. A desperate girl's halfway limbo."
    scene 67_s30 with dissolve
    mc "Are you sure?"
    scene 67_s29 with dissolve
    able "Certainty is a luxury, my boy. But that's the most logical place. They can't stay in the city, yet if they go too far... well, starvation or the local nasty creatures tends to take care of the rest."
    able "I'd start looking there."
    scene 67_s27 with dissolve
    mc "Hold on... I still haven't accepted yet."
    scene 67_s26 with dissolve
    able "Of course. No pressure."
    able "Still, I'd be very grateful if you decided sooner. Poor thing must be freezing her pretty little ass off out there."
    scene 67_s27 with dissolve
    mc "Right. I'll have think about it. I'll take my leave."
    scene 67_s26 with dissolve
    able "The pleasure was all mine, [mc]."
    able "And remember. I'll be watching your career with great interest~"
    stop music fadeout 2.0 
    scene 67_s27 with dissolve
    scene 67_s32 with Fade(1.0,1.0,1.0)
    play music "side_event1Talking.mp3" fadein 1.0 loop
    mc "You didn't order anything?"  
    negumi "The heart is willing but the purse is empty."  
    scene 67_s33 with Dissolve(1.5)
    mc "Wait! Your eyepatch? I thought you were..."  
    scene 67_s34 with dissolve
    negumi "Blind? No... I just wear it to look intimidating."  
    negumi "Besides, it looks cool... right? right!?"
    scene 67_s37 with dissolve
    mc "..."
    scene 67_s35 with dissolve
    mc "Yeah."
    scene 67_s36 with dissolve
    negumi "Heh."
    scene 67_s35 with dissolve
    mc "Eireen said you had coin to spare. Did you really spend it all?"  
    scene 67_s36 with dissolve
    negumi "I don't want to talk about it."  
    scene 67_s35 with dissolve
    mc "That bad, huh?"  
    scene 67_s36 with dissolve
    negumi "Let's just say gold doesn't like staying in my pockets for long..."  
    scene 67_s35 with dissolve
    mc "Fair enough."  
    scene 67_s38 with dissolve
    negumi "Speaking of coin, what happened up there? Did you get a job?"  
    scene 67_s39 with dissolve
    mc "I did, but I chose not to take it."  
    scene 67_s38 with dissolve
    negumi "W-What? Why?!"  
    scene 67_s39 with dissolve
    mc "It's too dangerous, Negumi. You heard what Eireen said about Able."  
    mc "Doesn't feel right rushing into it without thinking." 
    scene 67_s38 with dissolve
    negumi "Nghhh... That makes... sense. I hate it when things make sense."  
    scene 67_s32 with Dissolve(1.5)
    mc "*chuckles* Anyway, I've got to go."
    mc "You gonna be alright?"  
    negumi "Of course! The great Negumi always finds a way..."  
    mc "You don't sound too sure."  
    negumi "..."  
    call screen scene67_choice01 with dissolve

label scene67_choice01_op1:
    if mc_coin >= 10:
        $ mc_gave_coin_negumi = True
        $ mc_coin -= 10
        mc "Here. Take this. Should be enough for a room tonight."  
        play sound "sound_effects/karma_more.mp3" volume 0.2
        if mc_karma < 10:
            $ mc_karma += 1
        $ karma_more = True
        show screen stat_change with easeinright
        scene 67_s40 with dissolve
        negumi "S-Seriously?"  
        scene 67_s41 with dissolve
        mc "Yeah. No point acting tough if you freeze on the street."  
        hide screen stat_change with easeoutright
        $ karma_more = False
        scene 67_s40 with dissolve
        negumi "Thank you... [mc], right?"  
        scene 67_s41 with dissolve
        mc "Yup."  
        scene 67_s40 with dissolve
        negumi "I promise I'll pay you back tenfold!"  
        scene 67_s41 with dissolve
        mc "*laughs* Don't worry about it. Just take care of yourself."  
    else:
        mc "(Shit... I don't have enough coin.)"
        call screen scene67_choice01 with dissolve
    jump scene68

label scene67_choice01_op2:
    mc "Well, I hope you really do find a way."  
    mc "Goodbye, Negumi."  
    negumi "Farewell..." 
    jump scene68

label scene68:
    mc "(I should report back to Eireen. See what she has to say.)"
    stop music fadeout 2.0 
    scene 68_s1 with Fade(1.5,1.0,1.0)
    play music "guild.mp3" fadein 2.0 loop
    eireen "There were more candidates than usual this time around."
    mc "Ava?"
    scene 68_s2 with Dissolve(1.0)
    ava "Oh, hello, [mc]."
    scene 68_s3 with dissolve
    eireen "You're back sooner than I expected. What happened?"
    scene 68_s10 with dissolve
    mc "He asked me to find a servant. I played it cautious, told him I'd think about it first."
    scene 68_s3 with dissolve
    eireen "A servant... Hmm. Not the offer I anticipated, but perhaps more revealing than a simple job."
    scene 68_s10 with dissolve
    mc "What do you mean?" 
    scene 68_s4 with dissolve
    eireen "Ava, could you give a moment?"
    scene 68_s5 with dissolve
    ava "Of course."
    scene 68_s6 with dissolve
    eireen "Before you decide, [mc]. Give me some time. I need to speak with Lady Avery or Her Majesty when she returns. This... this changes things significantly."
    scene 68_s7 with dissolve
    mc "Why? It just seems like a weird request."
    scene 68_s6 with dissolve
    eireen "Because it's not a request. It's a test. And it might be our best chance in years. [mc], how would you feel about becoming a double agent?"
    scene 68_s7 with dissolve
    mc "A double agent? For Able? You can't be serious."
    scene 68_s6 with dissolve
    eireen "Deadly serious. The group he runs is a fortress. He doesn't invite people in; he vets them, tests them, and breaks them if they fail."
    eireen "This {i}servant{/i} role is a foot in the door. If you pass his test, he may invite you deeper into his circle."
    eireen "If that happens, you'd have a chance to see what no guard or guild spy has ever uncovered."
    scene 68_s7 with dissolve
    mc "Why would I ever want that? Getting closer to that man sounds like a nightmare."
    scene 68_s6 with dissolve
    eireen "Because for years, we have suspected or... known that Able is the mastermind behind the underground slave ring that plagues this city."
    eireen "But he is cunning, protected, and leaves no evidence. Her Majesty's hands are tied without proof."
    eireen "If you were on the inside... if you could find just one piece of irrefutable evidence... you wouldn't just be helping the city. You would be freeing countless lives from a fate worse than death."
    eireen "Your name would be remembered by every soul you saved."
    scene 68_s7 with dissolve
    mc "...I hear what you're saying. But you're talking about spying on the most powerful criminal in the city. He'll kill me if he finds out. You know that, right?"
    mc "...You're basically asking me to crawl into the wolf's den."
    scene 68_s6 with dissolve
    eireen "I won't sugarcoat the danger. It would be the most difficult thing you have ever done. That is why I will not order you to do it."
    eireen "And why I must consult with Lady Avery or Her Majesty. This is not a decision we can make lightly."
    scene 68_s7 with dissolve
    mc "Right. Okay. Let's... see what they say."
    mc "That aside, you mentioned you wanted to tell me something before I left?"
    scene 68_s8 with dissolve
    eireen "Ah, yes. Right. We are holding our monthly member evaluation. Judging new candidates. It serves as a good way to stengthen our guild. And filter out any incompetence."
    scene 68_s9 with dissolve
    mc "An evaluation? I never went through that."
    scene 68_s8 with dissolve
    eireen "*chuckles* Of course you didn't. You arrived with Her Majesty's personal recommendation. Did you think I'd refuse her?"
    scene 68_s9 with dissolve
    mc "Point taken. So, do you need help?"
    scene 68_s8 with dissolve
    eireen "Do you know someone who can judge a person's strength? Ava assesses their mana potential. I judge their character. And normally, Gaius judges their physical prowess, but he is... indisposed currently."
    scene 68_s9 with dissolve
    mc "Gaius? Wait, he talks?!"
    scene 68_s8 with dissolve
    eireen "You would think so. But no. He typically just gives a approving nod or a disappointed stare. It was surprisingly effective."
    scene 68_s9 with dissolve
    mc "Figures."
    mc "In that case... why not me?"
    scene 68_s8 with dissolve
    eireen "[mc], I appreciate the offer, but..."
    scene 68_s5 with Dissolve(1.0)
    ava "Why not, Miss Eireen? I believe [mc] is capable. Maybe not with magic, but strength? He seems a fine judge."
    scene 68_s4 with dissolve
    eireen "Ava, were you listening in on us?"
    scene 68_s5 with dissolve
    ava "I just heard that last part. Promise."
    ava "If the rumors are true, he even stood his ground against a werewolf."
    scene 68_s3 with dissolve
    eireen "A werewolf? Is that true, [mc]?"
    scene 68_s10 with dissolve
    mc "It is. Still not entirely sure how I managed it."
    scene 68_s3 with dissolve
    eireen "Incredible! Very well. It's settled. You will be our third judge this month."
    eireen "The candidates will begin arriving within the hour. Let's prepare."
    scene 68_s10 with dissolve
    scene 68_s11 with Fade(1.0,1.0,1.0)
    eireen "Alright, everything's set up. Before we begin, let me brief you on the procedure, [mc]."
    scene 68_s13 with Dissolve(1.0)
    mc "Go ahead."
    scene 68_s12 with dissolve
    eireen "Your role is to assess their physical prowess, their raw strength, combat potential, and overall durability."
    eireen "Some may choose to perform a feat of strength; lifting a heavy weight, striking a training dummy. Others may not, relying on their physique alone."
    scene 68_s13 with dissolve
    mc "How am I supposed to judge them if they don't do anything?"
    scene 68_s12 with dissolve
    eireen "Honestly, I'm not entirely sure how Gaius did it. He had a lifetime of experience. He could look at a person's posture, the set of their shoulders, the way they moved... and just know."
    eireen "For now, do your best. Gauge their confidence, their muscle definition, their presence. It's not a perfect science, and your gut instinct is part of it."
    scene 68_s13 with dissolve
    mc "...Right. Sure. I'll try my best."
    scene 68_s12 with dissolve
    eireen "The voting is simple. Each of the three of us gives a single verdict: in or out."
    eireen "A candidate requires a majority to be accepted. That means at least two in votes. A vote of two outs or three outs means they are rejected. No exceptions."
    scene 68_s13 with dissolve
    mc "Seems straightforward enough."
    scene 68_s14 with dissolve
    eireen "The most important rule, [mc]. Check your personal feelings at the door. This isn't about being nice. It's about integrity and safety."
    eireen "Letting in an inexperienced adventurer is a death sentence, for them and potentially for any party they join. We are responsible for the lives of everyone who wears our guild's insignia."
    eireen "Furthermore, our reputation is built on competence. A single incompetent member can tarnish the trust we've built for years, making it harder for every other member to find work."
    eireen "Your judgment today protects them, too. Understood?"
    scene 68_s15 with dissolve
    stop music fadeout 2.0 
    mc "Understood. I won't take it lightly."
    play music "guild2.mp3" fadein 2.0 loop
    scene 68_s30 with Dissolve(1.0)
    eireen "Good. Then let's begin. Whoever is first, please step up."
    scene 68_s16 with Dissolve(1.0)
    show screen guild_strength with dissolve
    eireen "Welcome. Please introduce yourself."
    scene 68_s17 with dissolve
    agnis "My name is Agnis. I'm thirty two years old. I specialize in offensive front line combat. I have five years of experience working caravan guard along the western trade route."
    scene 68_s16 with dissolve
    eireen "Thank you, Agnis. Do you wish to demonstrate your capability?"
    scene 68_s17 with dissolve
    agnis "Yes."
    scene 68_s16 with dissolve
    scene 68_s18 with Fade(0.5,0.5,0.5)
    ""
    play sound "sound_effects/slash03.mp3"
    scene 68_s19 with vpunch
    perception "He takes a solid stance, exhales, and delivers a single, perfectly clean strike with his sword. The dummy's head comes clean off."
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 68_s20 with dissolve
    eireen "Impressive control. Being able to swing a long sword that heavy with one arm is commendable."
    ava "Miss Eireen, did you remember to bring extra dummies this time?"
    eireen "Of course. I've learned my lesson since the last incident... wouldn't want a repeat of that mess."
    ava "Good. [mc], could you please replace the dummy?"
    mc "Sure."
    scene 68_s16 with Fade(0.5,0.5,0.5)
    eireen "With that out of the way. Ava?"
    scene 68_s31 with dissolve
    ava "His mana is negligible, but his life force is strong and steady. He relies on skill, not magic. I see no issue. In."
    scene 68_s30 with dissolve
    eireen "I agree. Practical, experienced, and understands the reality of the work. In."
    scene 68_s16 with dissolve
    eireen "[mc]?"
    call screen scene68_choice01_1 with dissolve

label scene68_choice01_1_op1:
    scene 68_s16 with dissolve
    perception "His arms and shoulders are corded with functional muscle, not for show but for use. He moves with the efficient grace of someone accustomed to conflict."
    call screen scene68_choice01_1 with dissolve
label scene68_choice01_1_op2:
    scene 68_s21 with dissolve
    perception "His longsword bears the wear of countless battles, but the edge is keen and the grip perfectly molded to his hand. This is a tool, not a decoration."
    call screen scene68_choice01_1 with dissolve
label scene68_choice01_1_op3:
    scene 68_s22 with dissolve
    perception "He meets your gaze directly. There's no arrogance, only confidence and professionalism."
    empathy "Yet behind that steadiness, his eyes are flat. Reliable, yes, but you question whether he has the fire to rise beyond competence when truly tested."
    call screen scene68_choice01_1 with dissolve

label scene68_choice01_1_op4:   
    call screen scene68_choice02_1_j with dissolve

default mc_agnis_in = False
label scene68_choice02_1_op1:
    $ mc_agnis_in = True
    mc "The guild needs solid, reliable fighters. In."
    scene 68_s16 with dissolve
    eireen "Accepted. Welcome to the guild, Agnis. Report to the quartermaster for your orientation."
    $ guild_strength_change = "+4"
    show screen guild_strength_change with dissolve
    $ guild_strength += 4
    scene 68_s17 with dissolve
    agnis "Thank you."
    hide screen guild_strength_change with dissolve
    scene 68_s16 with dissolve
    jump scene68_2

label scene68_choice02_1_op2:
    mc "Out."
    scene 68_s14 with dissolve
    eireen "Interesting. May I ask your reasoning? On the surface, he seemed an ideal candidate."
    scene 68_s15 with dissolve
    mc "He's skilled, no doubt. But he's a soldier, not an adventurer. He follows orders and handles predictable threats. This work? It demands improvisation. Fire. I didn't see that in him."
    scene 68_s14 with dissolve
    eireen "...Harsh. But fair. Still, with two approvals he passes regardless."
    $ guild_strength_change = "+4"
    show screen guild_strength_change with dissolve
    $ guild_strength += 4
    scene 68_s16 with dissolve
    eireen "Welcome to the guild, Agnis. Report to the quartermaster for your orientation."
    hide screen guild_strength_change with dissolve
    scene 68_s17 with dissolve
    agnis "...I'll prove your doubt misplaced."
    scene 68_s16 with dissolve
    jump scene68_2

label scene68_2:
    scene 68_s30 with Dissolve(1.5)
    eireen "A strong start. Who's next?"
    scene 68_s23 with Dissolve(1.0)
    perception "A young woman steps forward, hips swaying. She's wearing a skimpy outfit of silk and bronze that seems better suited for a brothel than combat. She carries a staff that looks more like a piece of art than a weapon."
    eireen "Tell us about yourself."
    scene 68_s24 with dissolve
    jenny "I'm Jenny, twenty one years young! I'm a healer of... considerable repute. I have lots of experience mending broken hearts and... other things."
    scene 68_s23 with dissolve
    eireen "Lots? Ava?"
    ava "No... sorry, Jenny. Your mana signature is faint. It flickers like a dying candle."
    scene 68_s24 with dissolve
    jenny "I'm purposely suppressing it, obviously! You think I'd just walk around radiating my full aura? It's so... undignified."
    scene 68_s23 with dissolve
    eireen "We'll see. [mc], your assessment?"
    call screen scene68_choice01_2 with dissolve

label scene68_choice01_2_op1:
    scene 68_s23 with dissolve
    perception "There doesn't seem to be any discernible muscle mass on her. Her body is soft, lacking the tone of someone who travels or endures hardship. Her hands are smooth, without a single callus."
    call screen scene68_choice01_2 with dissolve

label scene68_choice01_2_op2:
    scene 68_s25 with dissolve
    perception "The staff gleams, flawless. No nicks, no scratches. Its beauty suggests wealth, not battle. An ornament masquerading as a tool."
    call screen scene68_choice01_2 with dissolve

label scene68_choice01_2_op3:
    scene 68_s26 with Dissolve(1.0)
    perception "Her breasts sway freely, barely contained by her flimsy top."
    desire "This observation doesn't help with the evaluation of her combat or healing prowess... though a part of your brain suggests it might be a different kind of tactical advantage."
    scene 68_s27 with Dissolve(1.0)
    jenny "See something you like? Just wanted to say that I'm a huge fan of you, [mc]!"
    scene 68_s28 with dissolve
    mc "H-Huh?"
    scene 68_s27 with dissolve
    jenny "Oh, don't be modest! I know you were the one who rid us of that nasty ogre. Not many know it was you~ My hero!"
    scene 68_s28 with dissolve
    mc "Ahaha... thanks."
    eireen "Focus, [mc]. Your verdict?"
    call screen scene68_choice01_2 with dissolve

label scene68_choice01_2_op4:   
    call screen scene68_choice02_2_j with dissolve

default mc_jenny_in = False

label scene68_choice02_2_op1:
    $ mc_jenny_in = True
    mc "In."
    scene 68_s23 with dissolve
    eireen "...Are you serious?"
    ava "Absolutely not. She's unfit."
    eireen "This is not a guild for flatterers and pretenders. Out."
    scene 68_s24 with dissolve
    jenny "Ugh! You're all so dull. I'll join Able's guild instead. At least they appreciate a little charm."
    scene 68_s23 with dissolve
    jump scene68_3

label scene68_choice02_2_op2:
    scene 68_s23 with dissolve
    mc "She has no strength, her gear is for show, and she's trying to distract us. Out."
    ava "Agreed. Out."
    eireen "Your attempt at manipulation is noted and is precisely the behavior we filter out. This guild is built on merit, not flirtation. Out."
    scene 68_s24 with dissolve
    jenny "You're all so boring. Able's guild is much better anyway."
    scene 68_s23 with dissolve
    jump scene68_3

default mc_nevarth_in = False
label scene68_3:
    scene 68_s30 with Dissolve(1.0)
    eireen "Well, that was... tedious. Let's move on."
    scene 68_s29 with Dissolve(1.5)
    perception "An elderly elf shuffles in. He is leaning heavily on a wooden staff, his robes looking ancient but clean. Eireen immediately looks concerned."
    eireen "Excuse me, sir, I think you might be in the wrong building. The herbalist's guild is—"
    scene 68_s58 with vpunch
    ava "In!"
    scene 68_s59 with dissolve
    eireen "Huh? Really, Ava? On what grounds?"
    scene 68_s58 with dissolve
    ava "His mana potential... Miss Eireen, it's... it's not a pond. It's an ocean. I've never felt anything like it!"
    scene 68_s30 with Dissolve(1.0)
    eireen "Forgive my presumption. Please, introduce yourself."
    scene 68_s29 with Dissolve(0.8)
    nevarth "Nevarth. Two thousand and seventy three years of age. I am... a mage."
    eireen "...Understood. Thank you, Master Nevarth. [mc]?"
    call screen scene68_choice01_3 with dissolve

label scene68_choice01_3_op1:
    scene 68_s29 with dissolve
    perception "He looks frail, but there's an unnatural steadiness to his stance. His hands, though aged, are steady and covered in faint, silvery scars that look like old fire burns."
    call screen scene68_choice01_3 with dissolve

label scene68_choice01_3_op2:
    scene 68_s32 with dissolve
    perception "His staff is not just for leaning. It's humming with so much power that you can actually feel it. The wood is petrified and polished smooth from centuries of use."
    call screen scene68_choice01_3 with dissolve

label scene68_choice01_3_op3:
    scene 68_s33 with dissolve
    sensation "He exudes an aura of immense, patient power. It feels like standing next to a sleeping mountain."
    call screen scene68_choice01_3 with dissolve

label scene68_choice01_3_op4:   
    call screen scene68_choice02_3_j with dissolve

label scene68_choice02_3_op1:
    $ mc_nevarth_in = True
    mc "In. No question."
    $ guild_strength_change = "+12"
    show screen guild_strength_change with dissolve
    $ guild_strength += 12
    scene 68_s29 with dissolve
    eireen "The guild would be honored to have you, Master Nevarth. In. Welcome."
    hide screen guild_strength_change with dissolve
    nevarth "Mhm."
    scene 68_s30 with Dissolve(1.0)
    eireen "Who's next?"
    jump scene68_4

label scene68_choice02_3_op2:
    mc "Out."
    scene 68_s29 with dissolve
    eireen "Out? Truly? Even with such power?"
    ava "I can't agree with that, [mc]. His presence alone could shield this guild."
    eireen "Majority rules. Master Nevarth, you're welcome in our guild."
    $ guild_strength_change = "+12"
    show screen guild_strength_change with dissolve
    $ guild_strength += 12
    scene 68_s33 with Dissolve(1.0)
    nevarth "Mhm. Perhaps you should dispose of that man. He does not seem to know why he is here."
    hide screen guild_strength_change with dissolve
    eireen "Ahaha... Forgive us."
    eireen "[mc], get your head straight. Please."
    scene 68_s30 with Dissolve(1.0)
    eireen "Who's next?"
    jump scene68_4

label scene68_4:
    scene 68_s34 with Dissolve(1.5)
    perception "A tall, broad shouldered man steps in. His armor is a practical, foreign make of hardened leather and reinforced plates."
    eireen "Welcome. Please, introduce yourself."
    scene 68_s35 with dissolve
    desmond "I am Desmond. I hail from the sands of Nahraya. I came to this city seeking gold. Your guild seems the most efficient path to acquire it."
    desmond "I served for four years in the Nahrayan Falcon Corps. I was even granted the honor of personal guard to His Excellency, for a time."
    scene 68_s34 with dissolve
    eireen "An ex-soldier of the Falcon Corps? That is... notable. Your motivation is clear, if not altruistic."
    eireen "A question, if you will. Why did you leave such prestigious service?"
    scene 68_s35 with dissolve
    desmond "That is a matter between me and the desert winds. I would rather not speak of it."
    scene 68_s34 with dissolve
    eireen "Very well."
    mc "Since you're a physical combatant, actions speak louder than words. Show us something."
    scene 68_s35 with dissolve
    desmond "Of course."
    scene 68_s37 with dissolve
    desmond "You. Archer."
    scene 68_s36 with dissolve
    elara "M-Me? Y-Yes?"
    scene 68_s37 with dissolve
    desmond "Nock an arrow. Shoot it at me."
    scene 68_s36 with dissolve
    elara "Wh— I... Huh?!"
    scene 68_s37 with dissolve
    desmond "You heard me. Draw your bow and loose an arrow. At my chest."
    scene 68_s36 with dissolve
    elara "Are you sure?"
    scene 68_s37 with dissolve
    desmond "Do not be afraid. Or are you unsure of your own aim?"
    scene 68_s36 with dissolve
    elara "A-Alright..."
    scene 68_s37 with dissolve
    scene 68_s38 with Fade(0.5,0.5,0.5)
    eireen "This is highly unusual... Please be careful."
    desmond "Shoot!"
    play sound "sound_effects/arrow_hit1.mp3"
    scene 68_s39 with vpunch
    perception "In a blur of motion almost too fast to follow, Desmond's arm snaps up. Instead of blocking it with his blade, his open hand flashes across his body."
    perception "There's a sharp SMACK as his palm closes around the arrow's shaft, stopping the arrowhead a mere inch from his heart."
    eireen "*chuckles* Oh my... I expected a parry, but to snatch it from the air... that is exceptional reflexes."
    mc "No argument here."
    ava "Hmm..."
    scene 68_s34 with Fade(0.5,0.5,0.5)
    eireen "You seem troubled, Ava. Your assessment?"
    ava "His spirit is fierce, but closed. He has no magic, only a will that burns like a desert sun."
    ava "I sense a thirst within him, but not for water. For something darker. I do not trust it. My verdict is Out."
    eireen "He is undoubtedly strong and experienced. We need capable fighters, and his type can be useful, if managed carefully. In."
    eireen "[mc]? The deciding vote is yours."
    call screen scene68_choice02_4_j with dissolve

default mc_desmond_in = False
label scene68_choice02_4_op1:
    $ mc_desmond_in = True
    mc "The guild faces real monsters. We need real weapons to fight them. His skill is undeniable. In."
    $ guild_strength_change = "+6"
    show screen guild_strength_change with dissolve
    $ guild_strength += 6
    eireen "Very well. Accepted, Desmond. Understand that guild membership comes with rules and a chain of command. You will follow them, or you will be removed. Report to the quartermaster."
    hide screen guild_strength_change with dissolve
    jump scene68_5

label scene68_choice02_4_op2:
    mc "He's only out for himself. That's a risk in a team. Out."
    eireen "Rejected. You may try again if your motivations change, Desmond."
    desmond "..."
    jump scene68_5

label scene68_5:
    scene 68_s30 with Dissolve(1.0)
    eireen "Last candidate is up."
    scene 68_s53 with Dissolve(1.0)
    perception "A young woman steps in. She's wearing cheap leather armor. She holds a bow, her grip nervous and unfamiliar. She looks like she's trying very hard to be brave."
    eireen "Welcome. Tell us about yourself."
    scene 68_s52 with dissolve
    elara "I-I'm Elara. I'm a novice archer. I haven't had any real adventuring experience, b-but I learn very fast!"
    elara "I am also training to become a mage! My dream is to one day infuse my arrows with elemental magic. To be a true arcane archer."
    scene 68_s53 with dissolve
    ava "She's telling the truth. Her mana is unrefined, yes, and flickers with her nerves... but it's... vibrant. It has a pure, strong spark at its core. It's rare."
    mc "An arcane archer? Sounds awesome. Why don't you show us the archer part first? Take a shot at the target."
    scene 68_s52 with dissolve
    elara "Yes! Of course!"
    scene 68_s53 with dissolve
    scene 68_s40 with Fade(0.5,0.5,0.5)
    ""
    play sound "sound_effects/arrow1.mp3"
    scene 68_s41 with vpunch
    ""
    scene 68_s42 with dissolve
    elara "Ah! I'm so sorry! I—!"
    eireen "It's fine, Elara. Nerves are a natural enemy. Try again."
    scene 68_s43 with Dissolve(1.0)
    ""
    play sound "sound_effects/arrow2.mp3"
    scene 68_s44 with vpunch
    ""
    scene 68_s42 with dissolve
    ""
    scene 68_s50 with dissolve
    elara "I-Impossible! I don't usually miss from this range... I practice every day..."
    scene 68_s51 with dissolve
    ava "*whispers* This is embarrassing..."
    scene 68_s46 with dissolve
    eireen "The range isn't the problem. The pressure is. You must learn to master it before you can master the bow."
    scene 68_s60 with dissolve
    mc "Look at the target, not us. Just you and that straw man. Take one deep breath."
    scene 68_s60 with vpunch
    mc "You can do it!"
    scene 68_s47 with Dissolve(1.0)
    elara "*inhales*..."
    scene 68_s48 with dissolve
    elara "*exhales*..."
    play sound "sound_effects/arrow_hit2.mp3"
    scene 68_s49 with vpunch
    perception "The arrow flies straight and true, striking the dummy square in the chest."
    elara "Yes! I did it!"
    ava "Well done!"
    mc "A shaky start, but a strong finish."
    scene 68_s31 with Dissolve(1.0)
    ava "That spark of mana is tied directly to her will. When she focused, her aim was true. She's like an unpolished gemstone."
    ava "With proper training and mentorship... she could shine. My verdict is In."
    scene 68_s30 with dissolve
    eireen "Elara, that last shot was excellent, and your potential is undeniable. But this is not a school. It is a battlefield."
    eireen "Out there, your enemies won't let you take three shots. The goblins won't wait for you to find your breath. Throwing you into a den of wolves because you {i}learn fast{/i} is a recipe for tragedy."
    scene 68_s53 with Dissolve(1.0)
    eireen "You need experience in a safer environment first. For your own safety, my verdict must be Out."
    ava "The vote is split. [mc], the final decision is yours. Do we invest in her potential, or prioritize her safety?"
    call screen scene68_choice02_5_j with dissolve

default mc_elara_in = False
label scene68_choice02_5_op1:
    $ mc_elara_in = True
    mc "Safety is important, but so is opportunity. Everyone deserves a first chance."
    mc "She won't learn that shooting at dummies in a yard. She needs something real. I believe she can get that here. My verdict is In."
    $ guild_strength_change = "+1"
    show screen guild_strength_change with dissolve
    $ guild_strength += 1
    eireen "Very well. Elara, you are accepted on a provisional basis. You will be assigned to beginner level quests with senior party members only. Understood?"
    hide screen guild_strength_change with dissolve
    scene 68_s52 with dissolve
    elara "Y-Yes, Ma'am! Thank you! Thank you so much! I won't let you down!"
    scene 68_s53 with dissolve
    jump scene68_6

label scene68_choice02_5_op2:
    mc "That was three shots. In a real fight, she'd be dead twice over. Eireen is right."
    mc "You need to master your nerves on a practice range, not in a life or death situation where she gets people killed. My verdict is Out."
    eireen "Elara, I am sorry. The answer is no. This is not a rejection of you, but a protection of you."
    eireen "Train for a few months. Hone that focus until it's your first shot, not your third. Then come back and show us."
    scene 68_s52 with dissolve
    elara "...I understand. Thank you for your honesty. I... I will be back. I promise to train even harder!"
    scene 68_s53 with dissolve
    jump scene68_6

label scene68_6:
    stop music fadeout 2.0 
    hide screen guild_strength with dissolve
    scene 68_s4 with Fade(1.0,1.0,1.0)
    play music "guild.mp3" fadein 2.0 loop
    eireen "Good work, both of you. I think we managed to find some promising candidates this month."
    scene 68_s10 with dissolve
    mc "Happy to help."
    ava "Mhm."
    scene 68_s3 with dissolve
    eireen "*ahem* And remember what I told you earlier, [mc]. Regarding our other matter. Don't do anything rash. Wait for my word."
    scene 68_s10 with dissolve
    mc "I'll try to stay out of trouble."
    scene 68_s2 with dissolve
    ava "[mc]. Maybe you should speak with Master Nevarth. If anyone can unravel this strange enigma inside you, it's him."
    scene 68_s10 with dissolve
    mc "The old elf? Hmm. You're probably right, he might know something. I'll talk to him next time I see him."
    scene 68_s2 with dissolve
    ava "...There's also something else. Could we speak, just the two of us?"
    scene 68_s10 with dissolve
    mc "Sure. What's on your mind, Ava?"
    if not mc_execute_kat and not mc_life_kat:
        scene 68_s54 with Fade(1.0,1.0,1.0)
        ava "Kat... she found me. She told me what you did. Thank you. Truly, from the bottom of my heart, thank you."
        scene 68_s55 with dissolve
        mc "I just did what was right. It wasn't justice for her to pay for a crime she didn't commit."
        scene 68_s54 with dissolve
        ava "I know, but... still. She never should have gotten involved with that to begin with. She's clever, but too reckless for her own good."
        ava "I'm just so grateful it ended this way, and not... the other way."
        scene 68_s55 with dissolve
        mc "How is she holding up?"
        scene 68_s54 with dissolve
        ava "She's laying low, staying with me for now."
        ava "*chuckles* Though my pantry is paying the price. I swear she eats her weight in pastries when she's stressed. I hope she finds her footing and a proper job soon."
        scene 68_s55 with dissolve
        mc "Give her time. She's just decompressing. The fear will pass."
        scene 68_s54 with dissolve
        ava "I hope so. Anyway, that's all I wanted to say. Thanks again, [mc]. It means more than you know." 
        scene 68_s55 with dissolve
        mc "Anytime, Ava. Take care of her."

    elif mc_execute_kat:
        scene 68_s56 with Fade(1.0,1.0,1.0)
        ava "Did you... hear what happened to Kat?"
        scene 68_s57 with dissolve
        mc "...Yes. I heard."
        scene 68_s56 with dissolve
        ava "It's a nightmare... They executed her. For a crime everyone knew she didn't commit!"
        ava "It's made me lose all faith in the Queen's justice."
        scene 68_s57 with dissolve
        mc "She meant a great deal to you, didn't she?"
        scene 68_s56 with dissolve
        ava "She was my best friend."
        ava "Maybe even... more than that, sometimes."
        ava "I tried my best to force a smile today for Eireen's sake but... it hurts. I just can't keep doing it anymore."
        scene 68_s57 with dissolve
        mc "..."
        mc "(It's better she never knows I was the one who let it happen...)"
        scene 68_s56 with dissolve
        ava "Ah, listen to me..."
        ava "I'm sorry, [mc]. I just... needed to talk to someone. It feels so... suffocating."
        scene 68_s57 with dissolve
        mc "Don't apologize. Talking about it is all you can do right now."
        scene 68_s56 with dissolve
        ava "Thank you for listening. I'll... I'll see you around, [mc]."
        scene 68_s57 with dissolve
        mc "See you, Ava."

    elif mc_life_kat:
        scene 68_s56 with Fade(1.0,1.0,1.0)
        ava "Did you... hear what happened to Kat?"
        scene 68_s57 with dissolve
        mc "...Yes. I heard."
        scene 68_s56 with dissolve
        ava "It's a living nightmare... She's rotting in the dungeons, sentenced to life for crimes she didn't commit! How is that justice?"
        ava "It's made me lose all faith in the Queen's justice."
        scene 68_s57 with dissolve
        mc "She meant a great deal to you, didn't she?"
        scene 68_s56 with dissolve
        ava "She was my best friend."
        ava "Maybe even... more than that, sometimes."
        ava "I tried my best to force a smile today for Eireen's sake but... it hurts. I just can't keep doing it anymore."
        scene 68_s57 with dissolve
        mc "..."
        mc "Have you... been able to see her? To talk to her?"
        scene 68_s56 with dissolve
        ava "No. The guards won't allow any visitors. They say her crimes are too great."
        ava "She's completely alone in there..."
        scene 68_s57 with dissolve
        mc "..."
        mc "(She can't ever find out the order came from me...)"
        scene 68_s56 with dissolve
        ava "Ah, listen to me..."
        ava "I'm sorry, [mc]. I just... needed to talk to someone. It feels so... suffocating."
        scene 68_s57 with dissolve
        mc "Don't apologize. Talking about it is all you can do right now."
        scene 68_s56 with dissolve
        ava "Thank you for listening. I'll... I'll see you around, [mc]."
        scene 68_s57 with dissolve
        mc "See you, Ava."

label scene69:
    scene 69_s1 with Fade(1.0,1.0,1.0)
    ""
    scene 69_s3 with Dissolve(1.5)
    jenny2 "Well, hey there, handsome~! Fancy meeting you here."
    scene 69_s2 with dissolve
    mc "Jenna? What are you still doing here?"
    scene 69_s3 with dissolve
    jenny "Jenny. And I was waiting for you. I wanted to talk."
    scene 69_s2 with dissolve
    mc "Talk about what? The decision was made. You're out."
    scene 69_s3 with dissolve
    jenny "Decisions can be... reconsidered. People change their minds all the time, don't they?"
    scene 69_s2 with dissolve
    mc "...What are you getting at?"
    scene 69_s4 with Dissolve(1.0)
    perception "Her fingers, light as a feather, trail down your chest. She doesn't look at her hand, her eyes are locked on yours, watching for your reaction as her fingertips trace a line down your stomach, heading lower and lower."
    jenny "I think you do~"
    mc "..."
    scene 69_s5 with dissolve
    jenny "It's simple, my hero. All I need is a little favor. Just a good word from you in Eireen's ear. Tell her you saw... potential in me that {i}she{/i} didn't see."
    jenny "And I promise, I will be {i}so{/i} very grateful. I'll make it more than worth your while."
    scene 69_s6 with dissolve
    call screen scene69_choice01 with dissolve

label scene69_choice01_op2:
    play sound "sound_effects/slap04.mp3"
    scene 69_s7 with vpunch
    perception "Your own hand snaps up, slapping her hand away from your body. The seductive mask on her face shatters, replaced by shock and insult."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 69_s8 with dissolve
    jenny "W-What is your problem!? What was that for?!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 69_s9 with dissolve
    mc "The decision was final, Jenny. This isn't a negotiation. Your attempt to bribe a judge only confirms we made the right choice."
    mc "You should leave. Now. Don't make me report this to Eireen on top of everything else."
    scene 69_s8 with dissolve
    jenny "...Hmph! Fine! Your loss, you self righteous prick!"
    scene 69_s9 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    jump scene70

image 69_bj1 = Movie(play="images/4_chapter3/scene69/69_bj1.webm", loop=True)
image 69_bj2 = Movie(play="images/4_chapter3/scene69/69_bj2.webm", loop=True)
image 69_bj3 = Movie(play="images/4_chapter3/scene69/69_bj3.webm", loop=True)

label scene69_choice01_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p6_replay:
        $ persistent.scene1_p6_replay = True
    play sound "sound_effects/karma_less.mp3" volume 0.2
    $ mc_accept_jenny = True
    
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 69_s6
    mc "I'm... interested. But words are cheap. How exactly would you make it worth my while? Be specific."
    stop music fadeout 2.0 
    scene 69_s5 with dissolve
    jenny "Like this~"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 69_s11 with Fade(0.5,0.5,0.5)
    perception "She drops to her knees before you. Her hands are quick, unbuckling your belt before you can even process the speed of it. The cool air of the stairwell hits your skin."
    mc "Jenny... right here? Someone could come any sec—"
    play sound "se_sfx/blowjob/gag1.mp3" 
    scene 69_s12 with Dissolve(1.0)
    sensation "Her mouth devours your cock with a single gulp, and all coherent thought vanishes in a wave of sudden, overwhelming heat."
    desire "The risk of being discovered is suddenly a distant, irrelevant concern."
    play sound "se_sfx/blowjob/facial7.mp3" 
    scene 69_s13 with Dissolve(1.3)
    jenny "Mmmh... Relax. Trust me~ You won't last long enough for it to be a problem."
    show 69_bj1 with Dissolve(1.0)
    sensation "Her throat welcomes your cock. The world narrows to the feeling of her warm, sloppy mouth, the skillful movement of her tongue, and the soft, muffled sounds she makes."
    jenny "Mfmmnn~ I can feel you getting harder and harder in my mouth~"
    mc "(Fuck... She's too good at this! I'm losing my balance...)"
    show 69_bj2 with Dissolve(1.3)
    hide 69_bj1
    perception "As if she's reading your mind, Jenny's arms slide around your hips, her grip surprisingly strong, anchoring you firmly against the wall and against her. There's no escape."
    jenny "*slurp* Feels too good to stand? Mghmmm~"
    mc "Ah— Jenny..."
    jenny "Mmh... already twitching? Told you it wouldn't take long~"
    sensation "Her tongue circles and teases your tip, quicker now, the wet sounds echoing off the walls."
    mc "F–Fuck..."
    env "Somewhere beyond the door, boots thud past. Close... too close. But she doesn't stop. If anything, she sucks you harder."
    perception "Her pace becomes relentless, her cheeks hollowing with each thrust."
    mc "Jenny—!"
    mc "You're sucking too hard!"
    scene 69_s16 with vpunch
    perception "Your hands scramble against her head, trying to push her away, but her iron grip holds you fast."
    scene 69_s17 with Dissolve(1.3)
    jenny "Nuh-uh! You're doing it inside! Fill my throat with your cum, [mc]~! *slurp* *suck*"
    show 69_bj3 with Dissolve(1.0)
    hide 69_bj2
    call screen scene69_choice02 with dissolve

label scene69_choice02_op1:
    show 69_bj1 with Dissolve(1.0)
    hide 69_bj2
    hide 69_bj3
    jenny "Mfghmmmnn~ Fack... If I washn't sho bushy today *slurps* I would've ad you shticking thihs huge cock in my pushy."
    call screen scene69_choice02 with dissolve

label scene69_choice02_op2:
    show 69_bj2 with Dissolve(1.0)
    hide 69_bj1
    hide 69_bj3
    if mc_liked_feet:
        jenny "*sucks* *slurps* Are you sherioushly shtaring at my feet?"
        jenny "I'm giving you the besht blowjob in your life and you're shtaring at them..."
    elif mc_liked_ass:
        jenny "*sucks* *slurps* Are you shtaring at my ahss?"
        jenny "*slurps* Too bad~ My moush will have to do fah now~"
    elif mc_liked_tits:
        jenny "*sucks* *slurps* Are you shtaring at my tits?"
        jenny "Do you like how they sway and bob while I give you the besht throat in your life?"
    else:
        jenny "Mghmm~! *sucks* *slurps* Come on, big boy. Cum for me~"
    call screen scene69_choice02 with dissolve
    
label scene69_choice02_op3:
    show 69_bj3 with Dissolve(1.0)
    hide 69_bj2
    hide 69_bj1
    jenny "*gags* Can you feel my throat burshing your tip?"
    sensation "Your enitre cock is submerged in her steamy hot saliva. Your tip feels like melting each time she gags."
    call screen scene69_choice02 with dissolve

label scene69_choice02_op4:
    mc "Jenny!"
    show screen cum
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 69_s14 with vpunch
    sensation "Your cum comes crashing down into her throat, every muscle tightening as she milks you through it, swallowing without a flinch."
    hide screen cum
    play sound "se_sfx/blowjob/blowjob_cum3.mp3" 
    scene 69_s15 with vpunch
    sensation "Even as you cum, her tongue flicks and teases at your sensitive tip, coaxing out a few final spurts."
    scene 69_s18 with Fade(0.5,0.5,0.5)
    jenny "Ahh~ Sheesh... Ish thish your firsht time ejaculating thish year? Et got in mah nose."
    scene 69_s21 with Dissolve(1.5)
    play sound "se_sfx/blowjob/swallow1.mp3" 
    jenny "*gulps* Listen to it going down my throat. *gulps*"
    scene 69_s19 with Dissolve(1.3)
    jenny "Ahhhn~ Your stinky semen is swimming in my belly now."
    jenny "*laughs* It's probably so confused, trying to my find my eggs."
    scene 69_s20 with dissolve
    mc "Fuck... You never stopped sucking while I was cumming..."
    scene 69_s19 with dissolve
    jenny "Of course! You never stop once the semen stars flowing~ And judging by your face, I did a great job."
    jenny "Say... Why don't you keep doing these tiny little favors for me and I might reward you."
    scene 69_s20 with dissolve
    mc "More of the same thing?"
    scene 69_s19 with dissolve
    jenny "Hmm... Maybe we can do something different next time. *winks*"
    scene 69_s20 with dissolve
    mc "I'll think about it..."
    scene 69_s19 with dissolve
    jenny "Think long and hard about how warm and sloppy my mouth was while you're at it too."
    jenny "Now... Hurry along and get me my good word with Eireen."
    scene 69_s20 with dissolve
    mc "Yes... I'll do it..."
    scene 69_s19 with dissolve
    jenny  "Mhmm~ I knew I could count on my favorite hero~!"
    jenny "I'll be seeing you around~"
    scene 69_s20 with dissolve
    mc "Yeah... See you..."
    scene black with Fade(1.0,1.0,1.0)
    $ renpy.end_replay()
    
label scene70:
    scene 70_s20 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 2.0 loop
    ""
    scene 70_s1 with Fade(1.0,1.0,1.0)
    mc "(Rebecca wanted to see me after I'm done. I wonder... Wait, is that Avery?)"
    scene 70_s2 with Dissolve(1.0)
    mc "Lady Avery?"
    scene 70_s3 with Dissolve(1.0)
    avery "Hmm? What is it, [mc]?"
    scene 70_s4 with dissolve
    mc "It's rare seeing you outside the castle like this."
    scene 70_s3 with dissolve
    avery "Ah, well. There was a rather large event today. The opening of a new promenade by the riverfront. Endless speeches and ribbon cuttings."
    scene 70_s4 with dissolve
    mc "Sounds exhausting."
    scene 70_s3 with dissolve
    avery "It was. I've only just returned less than an hour ago. Before facing another mountain of documents, I thought I'd steal a moment of quiet."
    scene 70_s4 with dissolve
    mc "I see. For what it's worth, you look beautiful. Tired... but beautiful."
    scene 70_s19 with dissolve
    avery "*chuckles* You're not wrong. I am utterly drained. I've been standing and walking in these ridiculous heels since morning. My feet are threatening to secede from the rest of my body."
    scene 70_s5 with dissolve
    mc "Anything I can do to help?"
    scene 70_s19 with dissolve
    avery "Unless you've secretly trained as a master masseuse, then no, I'm afraid not. The damage is done. It's just me and my aching feet tonight."
    scene 70_s5 with dissolve
    mc "Your... feet?"
    call screen scene70_choice01 with dissolve
    
label scene70_choice01_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p6_replay:
        $ persistent.scene2_p6_replay = True
    $ mc_feet_massage_avery = True
    scene 70_s5
    mc "I'm no master, but I've been told I have a decent touch. If you'd allow me... I could try to help."
    scene 70_s19 with dissolve
    avery "[mc]... I appreciate the offer, but that's... highly improper."
    scene 70_s5 with dissolve
    mc "Trust me. It's fine. I'd love to actually."
    scene 70_s19 with dissolve
    avery "...You are a strange and bold man. Very well."
    scene 70_s5 with dissolve
    scene 70_s6 with Dissolve(1.5)
    perception "You kneel before her. Her foot is slender, pale in the sun."
    scene 70_s8 with Dissolve(1.5)
    avery "By the gods... where did you learn to do that?"
    scene 70_s7 with dissolve
    mc "You pick things up along the way."
    scene 70_s8 with dissolve
    avery "*laughs* Well, consider your service immensely appreciated. Hah... perhaps I'll promote you to my royal footman."
    scene 70_s7 with dissolve
    mc "I live to serve, my lady."
    scene 70_s9 with Dissolve(1.5)
    mc "(I can see her panties...)"
    avery "Hnnn~ Ahh~!"
    perception "Her breathing grows heavier as your fingers press into the arch of her foot. She squirms slightly, cheeks tinged with color."
    scene 70_s10 with Dissolve(1.0)
    avery "Oh, that's the one... Thank you. Now the other one, please. Don't let that one get jealous."
    scene 70_s11 with Dissolve(1.5)
    perception "She slips off her other heel and presents the second foot with a small, mischievous smile."
    avery "Both deserve equal treatment, don't you think?"
    mc "*chuckles* Of course."
    scene 70_s12 with Dissolve(1.0)
    sensation "You take her second foot in hand, kneading along her sole, then carefully along her toes. Her voice comes out in soft, involuntary gasps."
    avery "Ahhh~ Hnnn~ I really... needed this..."
    mc "How about this?"
    avery "Y-Yes! Perfect. Right there~!"
    scene 70_s13 with Dissolve(1.5)
    mc "*gulp* (...She's too close. The way she's trusting me...)"
    call screen scene70_choice02 with dissolve

label scene70_choice02_op1:
    scene 70_s5 with Dissolve(1.5)
    mc "There. That should feel a little better."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 70_s19 with dissolve
    avery "It does. More than a little, actually. Thank you."
    scene 70_s5 with dissolve
    hide screen stat_change with easeoutright
    $ karma_more = False
    mc "Then I'll take my leave. Rest well, Lady Avery. If you need something else, you know where to find me."
    scene 70_s19 with dissolve
    avery "I do. And I might just take you up on that~"
    scene 70_s5 with dissolve
    $ renpy.end_replay()
    jump scene71

label scene70_choice02_op2:
    $ mc_feet_massage_avery_toes = True
    scene 70_s14 with dissolve
    play sound "se_sfx/sex/touch3.mp3" 
    perception "Without much thinking, you lift her foot and press her toes to your mouth."
    scene 70_s15 with dissolve
    avery "..."
    scene 70_s14 with dissolve
    ""
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 70_s16 with dissolve
    mc "..."
    perception "Her body freezes. Her eyes widen, caught between disbelief and shock."
    mc "Sh-sorry... I just... wanted to... taste?"
    scene 70_s17 with Dissolve(1.5)
    perception "Slowly, she withdraws her foot, expression unreadable. She stands, smoothing her dress with silence."
    scene 70_s18 with Dissolve(1.0)
    perception "Without another word, she turns and leaves the garden, barefoot."
    mc "(Shit... this'll be awkward later...)"
    $ renpy.end_replay()
    jump scene71

label scene70_choice01_op2:
    mc "Right. Well, I'll leave you to it then. Good luck with that... I hope they feel better."
    scene 70_s19 with dissolve
    avery "Yes. Thank you for your concern. It's simply the price of duty."
    scene 70_s5 with dissolve
    mc "I'll be leaving. If you need something else... you know where to find me."
    scene 70_s19 with dissolve
    avery "I know. Goodbye, [mc]."
    scene 70_s5 with dissolve
    jump scene71

label scene71:
    stop music fadeout 2.0 
    scene 71_s1 with Fade(1.0,1.0,1.0)
    ""
    if mc_rejected_wedding_reb:
        scene 53_s39 with Fade(1.0,1.0,1.0)
        if not mc_maia_left:
            mc "(Just where did you go, Maia?)"
        else:
            mc "(I haven't seen Maia in a while. She doesn't live here anymore, but still... I used to see her in the halls sometimes.)"
        mc "(Maybe Avery knows something, I'll rest a bit then go ask her.)"

        jump scene74_3
    else:
        scene 71_s2 with Fade(1.0,1.0,1.0)
        mc "Becky? I'm back."
        jump scene71_2



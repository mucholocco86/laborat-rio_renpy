label ch3sc21:

    window hide dissolve
    play music explore_2 fadein 1.0
    scene ss27 with Dissolve (1.0)
    $ renpy.pause()
    scene ch3sc21_001 with Dissolve(2.0)
    $ renpy.pause(0.5)
    "You and Eliza follows the directions given by Sylph."
    scene ch3sc21_002 with dissolve
    $ renpy.pause(0.5)
    "You've been trekking through the woods for almost two hours at this point."
    scene ch3sc21_003 with dissolve
    el "Can you believe it?"
    el "After we complete this quest, we’ll actually become C-Rank Adventurers!"
    scene ch3sc21_004 with dissolve
    mc "It does seem sudden."
    mc "But our skills are better than D-Rank, and that’s probably obvious to Dalen."
    scene ch3sc21_005 with dissolve
    el "Yeah, I kinda got the feeling Dalen was sizing us up when we met him."
    scene ch3sc21_006 with dissolve
    el "I guess that’s to be expected."
    el "He's the Guildmaster, after all, and with the guild struggling recently..."
    scene ch3sc21_005 with dissolve
    el "He would have to be wary of new recruits."
    scene ch3sc21_006 with dissolve
    el "Tell me about these goblins? Sylph seemed really worried."
    scene ch3sc21_007 with dissolve
    mc "You’ve probably read about them in your mother's books, right?"
    scene ch3sc21_008 with dissolve
    el "Yeah... Not exactly friendly fellas."
    el "If the books were creditable."
    scene ch3sc21_009 with dissolve
    mc "Forget everything you've read about them."
    scene ch3sc21_010 with dissolve
    el "Huh, why?"
    scene ch3sc21_011 with dissolve
    mc "They are vicious creatures, Eliza. Don’t underestimate them."
    mc "A single goblin might not seem like much trouble..."
    mc "But they are group oriented creatures... if you ever see one by itself, always expect an ambush."
    scene ch3sc21_012 with dissolve
    mc "And unlike common bandits, don’t think they'll content themselves with taking your stuff and beating you up, either."
    mc "They maim. Kill. Ravage. Rape. Eat... all without a shred of remorse."
    scene ch3sc21_009 with dissolve
    mc "Don’t hesitate to strike a killing blow, given the opportunity."
    scene ch3sc21_010 with dissolve
    el "I see... Mother's books left out a few details."
    scene ch3sc21_011 with dissolve
    mc "It’s important you understand how serious the situation is."
    mc "All we know is there’s a group of goblins among some ruins."
    mc "Other than that, we’re pretty much going in blind."
    scene ch3sc21_013 with dissolve
    "Eliza places both her hands around your arm, with her soft, warm breast squished against your tricep."
    el "We’ll watch each other's backs, as always."
    scene ch3sc21_014 with dissolve
    "You can feel her heart beating rapidly, she’s afraid."
    mct "This won't do, if she goes into this fight mentally checked out..."
    mct "It could end badly, I need to get her head straight."
    scene ch3sc21_015 with dissolve
    mc "Remember our team training?"
    scene ch3sc21_016 with dissolve
    el "Whenever your partner creates an opening, don’t hesitate to strike."
    el "If your partner gets hurt, finish off any remaining threats before attending to them."
    scene ch3sc21_017 with dissolve
    mc "Good. I’m counting on you, Eliza."
    scene ch3sc21_018 with dissolve
    elt "It’s scary having to deal with this..."
    elt "But it feels really good that he trusts me enough to fight with him."
    elt "But... will I be strong enough to help him? Or... will I hold him back?"
    scene ch3sc21_014 with dissolve
    "You feel Eliza's grip tighten, she's clearly a little freaked out."
    ####Choice####
    menu:
        "Relate to her situation. ({color=#87e1fa}Charisma{/color})":
            scene ch3sc21_015 with dissolve
            mc "Hey... it's okay to feel a little on edge."
            mc "My first goblin encounter was an ambush while on the road with your father."
            mc "The suddenness of the situation didn't let me grasp how scared I really was... my body was in shock."
            scene ch3sc21_013 with dissolve
            el "Y-You were scared? Yeah right!"
            el "I've never seen you afraid of anything..."
            scene ch3sc21_015 with dissolve
            mc "You're forgetting I was just a kid..."
            mc "I had nightmares for about a week after that encounter."
            scene ch3sc21_016 with dissolve
            mc "You're going into the situation being aware of the goblins... I can see why that would make you nervous."
            mc "But I won't let anything happen to you, I've got your back like you have mine."
            scene ch3sc21_014 with dissolve
            $ charisma += 1
            "Eliza squishes your arm gently, she feels comforted by your words."
            "You successfully managed to calm Eliza's nerves, {color=#87e1fa}Charisma{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

        "Inspire her to remain strong. ({color=#ffee54}Leadership{/color})":
            scene ch3sc21_015 with dissolve
            mc "I know facing goblins might seem a little overwhelming."
            mc "But, you've got this, trust me."
            scene ch3sc21_013 with dissolve
            el "How can you be so sure? What if I freeze?"
            scene ch3sc21_016 with dissolve
            mc "You won't, you have more determination than any trained individual I've met."
            mc "Not to mention you care about others, eliminating these goblins will ensure the safety of nearby settlements."
            el "You're right, no matter how terrifying they might be, if I freeze, others might die."
            scene ch3sc21_015 with dissolve
            mc "That's right, now what does that tell you?"
            mc "What does that mean?"
            scene ch3sc21_013 with dissolve
            el "It means..."
            el "I can't freeze, I... cannot afford to fail."
            scene ch3sc21_015 with dissolve
            $ leadership += 1
            mc "Exactly, and we won't, not if we work together like we've trained for."
            "Eliza squeezes your arm gently and nods in agreement."
            "You successfully managed to inspire Eliza, {color=#ffee54}Leadership{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."


    scene ch3sc21_018 with dissolve
    elt "That was really sweet of him to give me a pep-talk like that."
    elt "He really knows how to rein in my emotions and make me feel at ease."
    scene ch3sc21_019 with dissolve
    elt "If these nasty goblins even scratch him... I’ll show them the definition of anguish."
    scene ch3sc21_020 with dissolve
    el "I won’t let you down, [mc]. I promised Sylph I'd protect you."
    scene ch3sc21_021 with dissolve
    mc "I’m sure I'll end up having to carry your butt home."
    scene ch3sc21_022 with dissolve
    el "Oh, please! As far as I recall, you enjoy carrying me!"
    scene ch3sc21_023 with dissolve
    mc "As if!"
    scene ch3sc21_024 with dissolve
    el "*Giggles* You don’t think I felt your hands on my butt last time?"
    scene ch3sc21_023 with dissolve
    mc "I-I... was just getting a better grip."
    scene ch3sc21_025 with dissolve
    elt "[mc] is so cute when I tease him!"
    scene ch3sc21_026 with dissolve
    el "Suuure!"
    el "That’s the reason... Mhm-hm..."
    scene ch3sc21_027 with dissolve
    mc "Next time, I’ll just let you slide down."
    scene ch3sc21_026 with dissolve
    el "Hey!"
    el "I never said I didn’t like it..."
    scene ch3sc21_028 with dissolve
    with vpunch
    "Eliza stiffens as she realises she just admitted to liking having her ass grabbed by you."
    el "Uh, never mind!!"
    scene ch3sc21_031 with dissolve
    menu:
        "Grab her ass.":
            scene ch3sc21_028 with dissolve
            elt "Eliza, calm yourself! You almost told him that you liked having his hands on your ass."
            elt "But would it be so bad to tell him? Maybe he'd do it again if he knew I liked it..."
            scene ch3sc21_030 with dissolve
            elt "Focus, Eliza!! We’re on a dangerous mission!"
            elt "He would think I'm weird if I asked him to do it now..."
            scene ch3sc21_031 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc21_032 with dissolve
            $ renpy.pause()
            scene ch3sc21_033 with dissolve
            with vpunch
            $ renpy.pause(0.3)
            elt "{b}!!!!!!!!!!!!{/b}"
            elt "His hands... Firmly squeezing my ass..."
            scene ch3sc21_035 with dissolve
            "Her firm little butt fits perfectly in your palm, her moans continue as you caress her tender butt cheek."
            el "Aahhm... Mhmh..."
            scene ch3sc21_034 with dissolve
            el "Someone's mhm... Feeling mhh... Handsy today..."
            mc "I simply couldn't resist... not with a perky little butt like yours."
            el "Do you like it? I know it’s not the biggest..."
            scene ch3sc21_032 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc21_035 with dissolve
            with vpunch
            el "*Moans* Ammhh! I’ll take that as you approving of my ass."
            "You give her ass a firm squeeze, really letting her know that you favor her ass, no matter the size."
            scene ch3sc21_027 with dissolve
            mc "Stating the obvious, are we?"
            scene ch3sc21_036 with dissolve
            el "You know I get insecure about my body... I'm not as big as some girls."
            scene ch3sc21_032 with dissolve
            with vpunch
            $ renpy.pause(0.5)
            el "*Moans* Nnyyah!"
            scene ch3sc21_028 with dissolve
            el "Heeey!!"
            scene ch3sc21_027 with dissolve
            mc "Eliza. You're one of the most beautiful girls I've ever laid eyes on."
            mc "Everywhere we go, I catch men turning their heads as we pass by... filled with jealous of the young man having you on his arm."
            mc "I wouldn't want you to be any different than you are."
            scene ch3sc21_023 with dissolve
            mc "C’mon. As much as I'd like to keep spanking your cute little butt, we have goblins to slay..."
            scene ch3sc21_019 with dissolve
            elt "F-Fucking goblins! Not only are they nasty, but now they've also ruined my spanking..."
            elt "Hrrrhh! Hrrrhhrrh! I wouldn't have minded a couple more firm grabs... maybe even a slap..."

        "Don't":
            scene ch3sc21_028 with dissolve
            elt "Eliza, calm yourself! You almost told him that you liked having his hands on your ass."

    scene ch3sc21_023 with dissolve
    mc "Are you listening?"
    scene ch3sc21_036 with dissolve
    with vpunch
    el "Huh?! Y-Yeah I’m listening!"
    scene ch3sc21_017 with dissolve
    mc "Okay, great. Then you won’t mind repeating what I just explained?"
    scene ch3sc21_039 with dissolve
    el "Uhhh... You said something about... Urh..."
    scene ch3sc21_040 with dissolve
    el "Trees..? I definitely heard the word tree!"
    scene ch3sc21_023 with dissolve
    mc "Good to know you have my back against all the scary trees."
    scene ch3sc21_036 with dissolve
    el "Okay... Can you please say it again? I spaced out."
    scene ch3sc21_038 with dissolve
    mc "When we reach the ruins, I’ll enter alone."
    mc "You wait in the nearby trees, and don't engage until I’ve created an opening for you."
    scene ch3sc21_026 with dissolve
    el "Okay, I can do that."
    scene ch3sc21_036 with dissolve
    el "After what you told me earlier... I assume we're engaging to kill? No captives?"
    scene ch3sc21_038 with dissolve
    mc "No captives. These creatures can’t be reasoned with. We have to eliminate every last one."
    scene ch3sc21_040 with dissolve
    el "Understood. I won’t show any mercy to these creatures."
    scene ch3sc21_037 with dissolve
    mct "It’s good that she's not hesitant. But it’s easier said than done."
    mct "I’ll have to observe her in actual combat."
    mct "She's learned a lot through our training together. But it’s only that... training."
    mct "This will be her first real combat experience."
    mct "And against goblins no less..."
    mct "But I have faith she'll be able to handle it. She’s your daughter... Oren."
    scene black with Dissolve(2)
    stop music fadeout 2.0
    $ renpy.pause(1.5)
    jump ch3sc22

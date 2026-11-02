
label ch3sc5:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (2.0)
    "You walk around the city for a bit until Eliza spots a shop."
    scene ch3sc05_001 with Dissolve(2.0)
    $ renpy.pause(1)
    el "Oh, look!"
    el "Let’s take a look in here, they might have something useful?"
    scene ch3sc05_002 with dissolve
    mc "*The Hag’s Cauldron* Charming name."
    scene ch3sc05_003 with dissolve
    el "Come on, you turtle."
    el "I'm positive they'll have something interesting in there!"
    scene ch3sc05_004 with dissolve
    mc "Sure... worth a look, I guess."
    mc "Sounds like it'll be an alchemy shop."
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch3sc05_005 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "I’m sure they'll have all sorts of cool potions we could use!"
    el "Maybe something that will allow me to walk on water like you?"
    scene ch3sc05_006 with dissolve
    $ renpy.pause(0.5)
    "The two of you begin browsing the shop."
    scene ch3sc05_007 with dissolve
    $ renpy.pause(1.5)
    scene ch3sc05_008 with dissolve
    mct "Looks like they got all sorts of weird stuff."
    mct "I honestly don’t know too much about alchemy."
    mct "Alice used to talk a great deal about becoming a herbalist, which is alchemy-adjacent."
    scene ch3sc05_009 with dissolve
    el "Woah! [mc], take a look at this bad boy!"
    el "I wonder what this potion is for?"
    scene ch3sc05_010 with dissolve
    mc "Your guess is as good as mine."
    scene ch3sc05_011 with dissolve
    elt "I bet it tastes super gross!"
    elt "Like... pea soup! Yuck!"
    scene ch3sc05_012 with dissolve
    $ renpy.pause(0.5)
    with vpunch
    wo "Careful with that! If you drop it, the whole shop will go up in flames."
    scene ch3sc05_013 with dissolve
    with vpunch
    el "{b}Aaah!{/b}"
    scene ch3sc05_014 with dissolve
    elt "{b}OH NO!{/b} No, no!"
    scene ch3sc05_015 with dissolve
    elt "We're all going to die! This is how it ends!"
    scene ch3sc05_016 with dissolve
    with vpunch
    $ renpy.pause()
    scene ch3sc05_017 with dissolve
    wo "Nice catch, young man! I thought we’d be burning up by now."
    wo "Your dexterity is impressive..."
    scene ch3sc05_018 with dissolve
    el "Phew! I’m so sorry!"
    el "You startled me... And I-"
    scene ch3sc05_019 with dissolve
    mc "Lady, you don’t seem very concerned that we almost incinerated your shop."
    mc "Or that the three of us were about to be burnt to a crisp."
    scene ch3sc05_020 with dissolve
    wo "*Laughs* Oh you, sweetling. That potion is just a shrinking elixir."
    wo "If you had dropped it though..."
    scene ch3sc05_021 with dissolve
    wo "Worst that would’ve happened is me, needing to deal with you two being ant-sized for a few hours."
    scene ch3sc05_022 with dissolve
    el "Heavens! You really had us scared for a second there!"
    el "I saw my life pass me by."
    scene ch3sc05_021 with dissolve
    wo "*Snickers* Sorry, I couldn't resist the chance to say hello! So, what can I do for you two?"
    wo "Maybe a love elixir? Or maybe... an enlargement potion?"
    scene ch3sc05_018 with dissolve
    el "E-Enlargement potion? Why would we need- {b}*Gasps* OH!{/b}"
    scene ch3sc05_023 with dissolve
    mc "Hard pass."
    mc "We’re about to start our first quest and we're looking for supplies."
    mc "Do you have any potions or elixirs that might help us?"
    scene ch3sc05_024 with dissolve
    wo "Oh, dearie. Hmm."
    wo "Yes, I certainly should have something laying around."
    scene ch3sc05_025 with dissolve
    wo "It’s hard to say without knowing the type of quest you'll be undertaking."
    wo "Hmm... let's see."
    scene ch3sc05_026 with dissolve
    wo "A few healing potions is always a sure bet!"
    wo "I should have some around here."
    scene ch3sc05_027 with dissolve
    wo "Mmmphf! If I could just reach. Hhrrr!"
    scene ch3sc05_028 with dissolve
    wo "I’ve almost got it! Just a little more."
    scene ch3sc05_029 with dissolve
    "."
    ".."
    "..."
    scene ch3sc05_030 with dissolve
    mc "No rush..."
    mc "No rush, at all."
    scene ch3sc05_031 with dissolve
    $ renpy.pause(1.5)
    scene ch3sc05_032 with dissolve
    $ renpy.pause(1.5)
    scene ch3sc05_033 with dissolve
    $ renpy.pause(1.5)
    scene ch3sc05_034 with dissolve
    with vpunch
    "Eliza gives you a hard nudge, signaling you to behave."
    scene ch3sc05_035 with dissolve
    mct "If looks could kill, I’d already have one foot in the grave."
    mct "Still cute, though."
    scene ch3sc05_036 with dissolve
    el "*Whispers* {size=-10}{b}Cut it out!{/b}{/size}"
    el "*Whispers* {size=-10}{b}We're here to buy supplies! You big oaf...{/b}{/size}"
    scene ch3sc05_035 with dissolve
    el "."
    el ".."
    scene ch3sc05_037 with dissolve
    with vpunch
    $ renpy.pause(0.5)
    "After trying to stare you down, Eliza can't help but giggle."
    scene ch3sc05_038 with dissolve
    $ renpy.pause(0.5)
    mct "*Chuckles* She's cute when she gets jealous."
    scene ch3sc05_039 with dissolve
    elt "Gaahh! I can’t stay mad at him... His heavenly blue puppy eyes always get me."
    elt "..."
    if eliza_relationship == True:
        elt "If it wasn't for this woman being here, I'd kiss him right now!"
        elt "Maybe I'd even climb that table like she's doing... allowing him to... see me."
        scene ch3sc05_040 with dissolve

    else:
        scene ch3sc05_040 with dissolve

    scene ch3sc05_040
    wo "Got it!"
    wo "Healing potions are quite valuable. They'll meet most needs that adventurers have."
    wo "They'll pretty much heal any immediate wounds you sustain."
    scene ch3sc05_041 with dissolve
    wo "I suppose a potion that lets you breathe underwater could come in handy as well."
    scene ch3sc05_042 with dissolve
    wo "Or maybe I could entice you with an elixir to enhance your night vision?"
    scene ch3sc05_043 with dissolve
    mct "Hmm, We’re a bit short on coin..."
    mct "I could try to convince her to give us a discount? Maybe by being persuasive?"

    menu:
        "Attempt to persuade her into giving a discount." if True:
            scene ch3sc05_044 with dissolve
            mc "Hmm, we’ll take two healing potions for now, since we don’t yet know what our quest will be."
            mc "And our coin is rather limited at the moment."
            scene ch3sc05_045 with dissolve
            mc "The other potions are more situational."
            mc "We'd best wait until we know if they will be needed."
            scene ch3sc05_046 with dissolve
            wo "Sure! Two healing potions coming right up!"
            wo "That’ll be four silver in total."

            if charisma >= 1:
                scene ch3sc05_047 with dissolve
                mc "After the little prank you played on us, I think a discount is in order."
                scene ch3sc05_048 with dissolve
                wo "I'm already one of the cheapest alchemists in Luxenford, sweetie."
                scene ch3sc05_047 with dissolve
                mc "Scaring your customers as if their lives were on the line? Might not be good for business if word gets out."
                scene ch3sc05_049 with dissolve
                elt "{b}[mc]!!{/b} What is he doing? Don’t push the crazy lady!"
                elt "If he upsets her she might turn us into mice!"
                scene ch3sc05_050 with dissolve
                wo "My, my... You’re a cunning one, aren’t you? *Snickers*"
                scene ch3sc05_051 with dissolve
                "You lock eyes with the woman."
                scene ch3sc05_050 with dissolve
                wo "Alright, fine! I'm not one to refuse a handsome face."
                wo "Three silvers for the potions."
                scene ch3sc05_052 with dissolve
                mc "And the shrinking potion for free."
                scene ch3sc05_053 with dissolve
                wo "Wha- *Sigh* Fine."
                wo "As an apology for my prank, you'll get your way... this time only!"
                scene ch3sc05_053_a with dissolve
                $ charisma += 1
                wo "Three silvers, and you also get the shrinking potion."
                "Your persuasion was {b}successful!{/b} Your Charisma & Persuasion increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch3sc05_054 with dissolve
                $ eliza_trust += 1
                elt "He’s so hot when he takes charge of situations like that."
                "Eliza is impressed by your improvement in social skills, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                $ persuasion += 1
                stop music fadeout 2.0
                scene black with Dissolve(1.5)
                jump ch3sc6

            else:
                scene ch3sc05_047 with dissolve
                mc "After the little prank you played on us, I think a discount is in order."
                scene ch3sc05_048 with dissolve
                wo "I'm already one of the cheapest alchemists in Luxenford, sweetie."
                wo "I won't be giving a discount, sorry."
                scene ch3sc05_047 with dissolve
                mc "Scaring your customers as if their lives were on the line? Might not be good for business if word gets out."
                scene ch3sc05_049 with dissolve
                elt "{b}[mc]!!{/b} What is he doing? Don’t push the crazy lady!"
                elt "If he upsets her she might turn us into mice!"
                scene ch3sc05_050 with dissolve
                wo "My, my... You’re a cunning one, aren’t you? *Snickers*"
                scene ch3sc05_048 with dissolve
                wo "No deal, Sugar."
                wo "The price is four silvers for the potions, take it or leave it."
                scene ch3sc05_052 with dissolve
                mc "*Sighs* It was worth a try..."
                mc "Four silvers it is then..."
                scene ch3sc05_050 with dissolve
                wo "Lovely! I'm glad you came to your senses."
                wo "*Snickers* It's a good thing you're pretty, but you'll have to work on your social skills."
                scene ch3sc05_051 with dissolve
                mct "This fucking hag..."
                elt "I had hoped he would've learned more by now, does he not care to listen to my teachings?"
                $ eliza_trust -= 2
                "Eliza is annoyed that you tried to haggle and failed, her trust has decreased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."
                stop music fadeout 2.0
                scene black with Dissolve(1.5)
                jump ch3sc6



        "Don’t risk it, might anger her." if True:
            scene ch3sc05_044 with dissolve
            mc "How much will it be?"
            scene ch3sc05_046 with dissolve
            wo "Four silvers for two healing potions."
            scene ch3sc05_049 with dissolve
            elt "Damn, four silvers. That’s enough for two nights at a tavern."
            elt "These potions better be effective!"
            scene ch3sc05_052 with dissolve
            mc "Four silvers for two potions? That’s pricey."
            scene ch3sc05_053 with dissolve
            wo "You’re welcome to try another shop."
            scene ch3sc05_044 with dissolve
            mc "No, it’s fine. Here."
            scene ch3sc05_050 with dissolve
            wo "Pleasure doing business with you!"
            scene ch3sc05_046 with dissolve
            wo "Please do stop by anytime should you need something!"
            scene ch3sc05_045 with dissolve
            mc "Sure."
            stop music fadeout 2.0
            scene black with Dissolve(1.5)
            jump ch3sc6

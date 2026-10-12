label ch3sc25:

    window hide dissolve
    stop music fadeout 2.0
    scene ch3sc24_101 with Dissolve(1.5)
    $ renpy.pause(1)
    da "Yes. Come on in, Sylph."
    scene ch3sc24_102 with dissolve
    play music dark_1 fadein 1.0
    uk "Sylph is a little preoccupied at the moment, I’m afraid."
    scene ch3sc24_103 with dissolve
    with vpunch
    da "You."
    scene ch3sc24_102 with dissolve
    uk "The one and only!"
    uk "How have you been, old friend?"
    scene ch3sc24_103 with dissolve
    da "You already know the answer to that."
    da "You’re the reason the Guild has been doing poorly of late."
    scene ch3sc24_102 with dissolve
    uk "I see you're still blaming others for your own shortcomings, eh?"
    scene ch3sc24_103 with dissolve
    da "You’re testing my patience, Taron."
    da "Get to the point and leave."
    scene ch3sc24_102 with dissolve
    ta "Relax, I’m simply here to extend an invitation."
    ta "Disband your little... guild of misfits... and come join the Mercenaries Guild."
    ta "I’ll even let you be second-in-command, for old times sake."
    scene ch3sc24_104 with dissolve
    da "*Sigh*"
    scene ch3sc24_103 with dissolve
    with vpunch
    da "{b}OUT!{/b}"
    scene ch3sc24_105 with dissolve
    ta "Holding on to your ideals as always, I see."
    ta "Admirably, really. But futile in the end."
    scene ch3sc24_106 with dissolve
    ta "You’ll take me up on my offer soon enough."
    ta "From under the rubble of your so-called Guild, if it has to be that way."
    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    scene ch3sc25 with Dissolve(1.5)
    $ renpy.pause()
    scene ch3sc25_001 with Dissolve(2.0)
    play music explore_1 fadein 1.0
    $ renpy.pause(1)
    el "*Giggling happily* Hurry up! I’m sore all over..."
    el "I need a pair of strong... warm... manly hands, rubbing me all over!"
    mct "*Chuckles* She has a way with words... I'll give her that."
    scene ch3sc25_002 with dissolve
    el "*Purrs* Nnyaah-Mmmh! I didn’t know how much I needed this!"
    el "K-Keep pressing like that... nhh..."
    scene ch3sc25_003 with dissolve
    elt "His hands... They’re so powerful, I’ve seen him snap the necks of bandits like a twig."
    elt "Yet on my body, they’re so tender and caring."
    scene ch3sc25_004 with dissolve
    elt "Mmhm... by the Divines! He makes me feel all giddy and warm."
    elt "He takes care of me... nnhh... he's so good to me... mmh..."
    scene ch3sc25_005 with dissolve
    el "Ahh... what a day... we slew a bunch of goblins."
    el "Probably saved a few settlements... found a couple of ancient trinkets... mmh..."
    scene ch3sc25_006 with dissolve
    el "We reached C-Rank status with the guild."
    scene ch3sc25_005 with dissolve
    el "We even had a warm, relaxing bath."
    scene ch3sc25_007 with dissolve
    mc "We made good progress today."
    scene ch3sc25_006 with dissolve
    el "And we had a bath!"
    scene ch3sc25_007 with dissolve
    mc "*Chuckles* And we had a bath."

    if eliza_lick == True:
        scene ch3sc25_006 with dissolve
        el "And you... you tasted me."
        scene ch3sc25_005 with dissolve
        el "D-Did I taste as you had hoped?"
        scene ch3sc25_007 with dissolve
        mc "Better."
        mc "My mouth is watering just thinking about it."
        scene ch3sc25_006 with dissolve
        el "*Excitedly* Nyaah! Hey... [mc]?"
        el "What do I taste like?"
        scene ch3sc25_007 with dissolve
        mc "You've never tasted yourself before?"
        mc "Not even once?"
        scene ch3sc25_005 with dissolve
        el "No... was I supposed to?"
        el "The thought never occured to me, although the scent lingering on my fingers after..."
        el "After taking care of myself, it does smell inviting... should I try it sometime?"
        scene ch3sc25_007 with dissolve
        mc "Maybe out of curiosity?"
        mc "You know what, we'll have to fix that sometime... if you want to?"
        scene ch3sc25_006 with dissolve
        el "I don't mind, you seemed to really enjoy it!"
        scene ch3sc25_005 with dissolve
        el "Maybe... next time you lick me..."
        el "You could share some of the taste with me through a kiss?"
        scene ch3sc25_006 with dissolve
        el "I think I would like it best directly from your mouth."
        scene ch3sc25_007 with dissolve
        mc "You bet, kitten."
        mc "I'll make sure you get a proper taste."
        scene ch3sc25_005 with dissolve
        el "*Giggles* We're so naughty!"
        el "Naughtiest kitten and her lion! Nnh-mhh!"
        scene ch3sc25_007 with dissolve
        mc "*Chuckles* I enjoy my kittens naughty side."
        mc "Especially knowing I'm the only one who gets that side of her... I'm a lucky man."
        scene ch3sc25_005 with dissolve
        el "You're the only one I want to show it to... to share it with..."
        el "The king himself could ask for my hand and I'd reject him for you... I-... I'm yours."
        scene ch3sc25_007 with dissolve
        mc "Yes, you're mine Eliza. All mine."

    else:
        scene ch3sc25_006 with dissolve
        el "I know you secretly loved it!"
        scene ch3sc25_005 with dissolve
        el "You’re allowed to enjoy things once in a while, you know?"
        scene ch3sc25_007 with dissolve
        mc "I suppose. The bath did feel refreshing."
        scene ch3sc25_005 with dissolve
        el "I knew you liked it!"

    scene black with Dissolve(1.5)

    scene ch3sc25_008 with Dissolve(1.5)
    if eye_beam == True:
        el "You know... the way you handled that Berzerker..."
        el "With those... eye beams you can do?"
        scene ch3sc25_007 with dissolve
        mc "Mmh?"
        mc "What about it?"
        scene ch3sc25_008 with dissolve
        el "It was... kind of hot?"
        el "Like... really hot!"
        scene ch3sc25_012 with dissolve
        el "*Snickers* I forbid you from showing that ability to other women!"
        scene ch3sc25_007 with dissolve
        mc "*Chuckles* Silly..."
        scene ch3sc25_006 with dissolve
        el "Call me silly all you want, I still forbid it! Mhm-hm!"
        scene ch3sc25_006 with dissolve
        el "Eye-beams is only to impress your kitten!"
        scene ch3sc25_003 with dissolve
        mc "Is that so?"
        el "*Purrs* Nnyyhh... mmhh..."

    else:
        pass

    scene ch3sc25_008 with Dissolve(1.5)
    el "Hey, [mc]?"
    scene ch3sc25_007 with dissolve
    mc "Mmh?"
    scene ch3sc25_008 with dissolve
    el "What do you think our next quest will be?"
    scene ch3sc25_009 with dissolve
    mc "I’ve got no clue, to be honest."
    mc "It could be anything, from 'Help an elderly lady with her daily chores' to..."
    mc "'There’s a monster on the loose in the city'"
    scene ch3sc25_008 with dissolve
    el "I like the helping elderly folk best!"
    el "I could do with a few days of no monsters, goblins or wolves..."
    scene ch3sc25_007 with dissolve
    mc "I know what you mean."
    scene ch3sc25_006 with dissolve
    el "I love when we have moments like these, just you and me."
    scene ch3sc25_004 with dissolve
    mc "Mhm... We’ve been quite busy since reaching the capital."
    scene ch3sc25_006 with dissolve
    el "It would be nice to have a day where it’s just the two of us."
    scene ch3sc25_005 with dissolve
    el "No monsters, no bandits, no old ladies."
    el "Just... us."
    ###Choice###
    menu:
        "Take Eliza on a date. ({color=#ff8cdd}Romance{/color})":

            $ eliza_trust += 3
            scene ch3sc25_007 with dissolve
            mc "You. Me. And a beautiful lake."
            mc "How does that sound?"
            scene ch3sc25_002 with dissolve
            with vpunch
            el "{b}YES!{/b} It’s a d-date!"
            scene ch3sc25_008 with dissolve
            el "Errh... I mean-"
            scene ch3sc25_007 with dissolve
            mc "It’s a date."
            "Upon hearing you confirm it, Eliza is overcome with joy, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch3sc25_009 with dissolve
            elt "Owh?! I didn’t expect him to agree!? D-Does he feel the same about me? No way, I’m just a peasant girl."
            elt "I know he cares about me. But a date? That would mean he sees me as a potential romantic partner... Right?"
            elt "That's literally everything I want! I want to tell him that I lov-"
            scene ch3sc25_010 with dissolve
            elt "Wake up Eliza! He’s literally a Nephilim... a half angel."
            elt "Why would he be interested in me? *Sigh*"
            elt "He can literally have anyone... Anyone!"
            elt "He's probably going to marry the princess! Urrgh!"
            scene ch3sc25_011 with dissolve
            el "You don’t have to... I just got excited."
            el "Never mind... I'm just a silly girl."
            scene ch3sc25_013 with dissolve
            mc "Eliza... would you like to go on a date with me?"
            scene ch3sc25_009 with dissolve
            elt "{b}!!!!!!{/b}"
            elt "He was being serious?!"
            scene ch3sc25_012 with dissolve
            el "[mc]... *Shyly* Yes."
            scene ch3sc25_013 with dissolve
            mc "What’s that? I couldn’t hear you."
            scene ch3sc25_012 with dissolve
            with vpunch
            el "{b}Yes!{/b} Yes, I want to go on a date with you!"
            scene ch3sc25_014 with dissolve
            el "I really want to go on a date! With you! {b}Only you!{/b}"
            scene ch3sc25_015 with dissolve
            $ renpy.pause()
            mct "..."
            ###Choice###
            menu:
                "Love.":
                    scene ch3sc25_015 with dissolve
                    mct "I love her."
                    mct "I've fallen for her... there's no denying it."
                "Lust.":
                    scene ch3sc25_015 with dissolve
                    mct "I'm crazy about her."
                    mct "I've never met a woman who gets me excited like her."

            scene ch3sc25_016 with dissolve
            el "Dummy..."
            scene ch3sc25_017 with dissolve
            mc "You’re cute when you get all shy."
            scene ch3sc25_016 with dissolve
            el "Shut up, you-you... *Sigh*"
            el "{b}Kiss me!{/b}"
            scene ch3sc25_018 with dissolve
            $ eliza_path = True
            $ renpy.pause()
            scene ch3sc25_019 with dissolve
            $ renpy.pause()
            "As her soft lips touch your upper lip, she sucks tenderly, like it has become a natural instinct for her."
            mct "Fuck... the way she likes to suck my lips... she drives me crazy."
            scene ch3sc25_020 with dissolve
            "She runs her fingers through your hair as she gives in to the passion of the kiss."
            "Small whimpers punctuate her soft moans as she presses herself into you."
            ####Animation####
            show mc_el_kiss7 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause()
            el "Mh... Hhhnn! *Sucks gently* Mhm."
            $ eliza_relationship = True
            mct "I love the way she kisses me... a simple kiss is never enough with her, she always begins sucking when our lips meet."
            mct "The way she pulls herself against me, her arms wrapped around my neck. She’s clearly wants to be as close as possible."
            elt "Mmhh! *Sucks* H-He asked me on a date! *Kisses* Hhhnn..."
            elt "Mhhaah... I... Mhhh... I love him!"
            elt "{b}I love him so much!{/b}"
            scene ch3sc25_020 with dissolve
            $ renpy.pause(0.3)
            "After a while, she stops. Just keeping her lips pressed against yours before gently pulling away."
            scene ch3sc25_019 with dissolve
            $ renpy.pause(0.3)
            mc "Mmmh... now that's what I call a kiss."
            mc "We didn't even use tongues... yet, it felt incredibly intimate."
            mc "Almost like you were telling me that-"
            scene ch3sc25_018 with dissolve
            $ renpy.pause(0.3)
            el "*Whispers softly* {size=-10}{b}That I love you.{/b}{/size}"
            mc "Hmm?"
            el "Nothing, I just agreed... that kiss had a lot of emotion behind it."
            scene black with Dissolve(2.5)
            stop music fadeout 2.0

        "Stay focused on your mission ({color=#2bff8b}Friendship{/color})":
            "Eliza’s trust increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ eliza_trust += 1
            scene ch3sc25_007 with dissolve
            mc "As nice as that sounds... we have to stay focused, Eliza."
            scene ch3sc25_005 with dissolve
            el "*Sigh* You’re right... I know. Don’t mind me and my silly ideas."
            $ eliza_path = False
            scene ch3sc25_007 with dissolve
            mc "Nothing wrong with the idea. Just the timing."
            scene ch3sc25_006 with dissolve
            el "Yeah, but we should remember to take a day off once in a while."
            el "It’s not healthy to stay hyper-focused on just one thing."
            $ eliza_relationship = False
            scene ch3sc25_007 with dissolve
            mc "Okay. We’ll see if we can make time for a day off, once in a while."
            scene ch3sc25_006 with dissolve
            el "At least we have relaxing moments like these."
            scene ch3sc25_005 with dissolve
            el "Now, get to work mister!"
            scene black with Dissolve(2.5)
            stop music fadeout 2.0


    jump ch3sc26

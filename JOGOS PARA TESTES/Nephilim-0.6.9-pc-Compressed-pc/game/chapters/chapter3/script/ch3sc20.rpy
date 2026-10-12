label ch3sc20:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (1.0)
    $ renpy.pause(0.2)
    scene ch3sc20_001 with Dissolve(2.0)
    $ renpy.pause(0.5)
    el "Last night was fun!"
    scene ch3sc20_002 with dissolve
    mc "Knowing you, you’ll want to do it again..."
    scene ch3sc20_003 with dissolve
    el "You bet! Don’t pretend you didn’t enjoy a relaxing night with friends and ales."
    scene ch3sc20_004 with dissolve
    mc "I admit it was kind of refreshing."
    mc "Borri and Selena. They..."
    ###Choice###
    menu:
        "They’re our friends. ({color=#87e1fa}Light Path{/color})":
            $ light += 1
            "{color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch3sc20_005 with dissolve
            $ renpy.pause(0.5)
            elt "I was hoping he'd feel that way, he's really come a long way."
            scene ch3sc20_006 with dissolve
            el "I knew you liked them!"
            el "I can tell that you and Borri get along like brothers!"
            scene ch3sc20_007 with dissolve
            mc "I’m an only child, but I suppose Borri is what I imagine having a brother would be like."
            scene ch3sc20_006 with dissolve
            el "I’m happy to see you like this."
            el "Remember we talked about what comes next after we accomplish our goal?"
            scene ch3sc20_008 with dissolve
            el "Making friends will be a big part of that."
            scene ch3sc20_007 with dissolve
            mc "I get it."
            mc "You won’t let me be a loner forever..."
            scene ch3sc20_009 with dissolve
            el "*Giggles* Finally, you're starting to understand!"
            scene ch3sc20_008 with dissolve
            el "Let's find Sylph and see what she has for us today."

        "They’re just a means to an end. ({color=#f00}Dark Path{/color})":
            $ dark += 1
            "{color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch3sc20_005 with dissolve
            $ renpy.pause(1)
            elt "I was hoping he'd have begun to consider them friends..."
            elt "I don't think keeping everyone at arms length will do him any good."
            scene ch3sc20_010 with dissolve
            el "*Sigh* You know you'll need friends down the line, right?"
            scene ch3sc20_007 with dissolve
            mc "I’m fine..."
            scene ch3sc20_011 with dissolve
            el "For now."
            el "But I worry about you..."
            el "If you close yourself off from everyone, nothing good comes from that."
            el "It'll lead to darkness... despair... loneliness."
            scene ch3sc20_012 with dissolve
            mc "Are you done? We have a quest to pick up."
            scene ch3sc20_013 with dissolve
            el "Yeah, yeah... Let’s go."
            el "We'll visit this topic again, though."
            el "You know I'm more stubborn than you."
            scene ch3sc20_004 with dissolve
            mc "*Sigh* I've noticed."

    scene ch3sc20_014 with dissolve
    el "Hmm... I don’t see Sylph anywhere."
    scene ch3sc20_015 with dissolve
    el "The Guild hall looks empty."
    el "I guess the Guild really has been having trouble getting contracts lately."
    scene ch3sc20_016 with dissolve
    mc "With the two of us, and now Borri as well, I’m sure things will turn around."
    mc "As the three of us begin completing more and more quests, word will spread."
    scene ch3sc20_015 with dissolve
    el "Totally! Completing today's quest will be another step towards a brighter future!"
    el "If anyone can return the Adventurer’s Guild to its former glory, it's us!"
    scene ch3sc20_016 with dissolve
    mc "Someone’s feeling confident. I like it."
    mc "Now, let’s see if Sylph is anywhere to be found."
    scene ch3sc20_015 with dissolve
    el "Uh-Uh! Allow me to summon her! *Snickers*"
    scene ch3sc20_017 with dissolve
    with vpunch
    el "{b}*Shouts*{/b} Sylph!"
    el "{b}*Shouts*{/b} Where are you hiding that cute little Pixie butt of yours?!"
    scene ch3sc20_018 with dissolve
    with vpunch
    sy "Who're you calling a Pixie?! I’m a Fae!"
    scene ch3sc20_019 with dissolve
    sy "Huge difference! Huge!"
    sy "Pixies are teeny-tiny! The size of your finger!"
    sy "I may be smaller than a human but I'm still big!"
    scene ch3sc20_020 with dissolve
    sy "Oh! Eliza, [mc]!"
    sy "Well, well, if it isn’t my two favorite recruits!"
    scene ch3sc20_021 with dissolve
    mc "We’re your only recruits."
    scene ch3sc20_022 with dissolve
    sy "For now! Hopefully our luck is about to change now that you two have begun completing quests!"
    scene ch3sc20_023 with dissolve
    sy "As you've probably noticed, our shelves are rather empty at the moment."
    scene ch3sc20_024 with dissolve
    sy "If you manage to find anything noteworthy while doing quests, be sure to bring it back and we can display it here!"
    scene ch3sc20_026 with dissolve
    sy "That will help with attracting new recruits!"
    sy "If people see our Guild Hall filling out with awesome artifacts and heirlooms, they will surely be impressed!"
    scene ch3sc20_025 with dissolve
    el "Makes sense, we'll keep our eyes peeled for anything that would be display worthy!"
    el "Speaking of quests, got anything for us today Sylph?"
    scene ch3sc20_027 with dissolve
    sy "You betcha!"
    sy "We actually happen to have two quests today!"
    scene ch3sc20_028 with dissolve
    with vpunch
    el "Great! We’ll take both!"
    scene ch3sc20_029 with dissolve
    sy "Love the enthusiasm girl! But you will have to settle for one today."
    sy "I have to keep one quest available for our newest recruit."
    scene ch3sc20_030 with dissolve
    mct "She’s talking about Borri."
    scene ch3sc20_029 with dissolve
    sy "So I’ve prepared one of the quests as his introductory task."
    scene ch3sc20_028 with dissolve
    el "Ah, you must be talking about Borri, he’s our friend and we suggested he should join us at the guild."
    scene ch3sc20_031 with dissolve
    sy "My, my! Completing quests and recruiting new members?"
    sy "Where have you two been all these years?"
    scene ch3sc20_032 with dissolve
    mc "You’re giving us too much credit, Sylph."
    mc "Borri needed a better way to earn coin, so we suggested the guild."
    scene ch3sc20_033 with dissolve
    sy "Everyone has their own reasons for joining."
    sy "Either way, the guild needs more members to stay competitive."
    scene ch3sc20_034 with dissolve
    mc "Hmm. Makes sense, we wouldn’t want to lose quests or contracts to other guilds."
    scene ch3sc20_035 with dissolve
    sy "Exactly!"
    sy "Let me just fetch your contract for today."
    scene ch3sc20_036 with dissolve
    sy "Here you go!"
    scene ch3sc20_037 with dissolve
    el "It says it’s a C-Rank quest?"
    el "But I thought we’re only approved for D-Rank?"
    scene ch3sc20_031 with dissolve
    sy "Yes, normally you’d have to rank up by completing several D-Rank contracts before receiving this."
    sy "But Dalen has a feeling you two will be able to complete it."
    sy "And if you do manage to complete it, you will officially be C-Rank Adventurers!"
    scene ch3sc20_034 with dissolve
    mc "We’ll take it."
    el "*Nods approvingly* Mh-hm!"
    scene ch3sc20_038 with dissolve
    elt "Hmm... This feels a little soon, it’s only our 2nd quest."
    elt "But I’ve got [mc] with me, it should be fine."
    scene ch3sc20_039 with dissolve
    el "So what is this quest about, Sylph?"
    el "If it's C-Rank, we need some info, going in blind would be dangerous."
    scene ch3sc20_040 with dissolve
    sy "Oh right!"
    sy "Silly me, I almost forgot to inform you! There’s some abandoned ruins to the east of Luxenford."
    scene ch3sc20_031 with dissolve
    sy "A scout reported that a group of goblins have set up camp within the ruins..."
    scene ch3sc20_032 with dissolve
    mc "Let me guess... they’re terrorizing the nearby villages and travelers?"
    scene ch3sc20_041 with dissolve
    sy "Yes!! And it's horrible. They're nasty creatures."
    sy "They attack anyone who comes across them."
    sy "I-I... It’s horrible what they’ve done, they eat people... and they... breed the women they capture-"
    scene ch3sc20_032 with dissolve
    mc "It’s alright, Sylph... you don’t need to tell us anymore."
    mc "I’ve dealt with goblins before... disgusting creatures."
    scene ch3sc20_042 with dissolve
    mc "Consider the contract completed by nightfall, Sylph."
    scene ch3sc20_043 with dissolve
    sy "So soon?!"
    sy "That would be amazing! Please be careful, guys."
    scene ch3sc20_044 with dissolve
    el "Don’t worry, Sylph!"
    el "I’ll protect [mc] from the nasty goblins."
    el "As long as I have his back, they don't stand a chance!"
    scene ch3sc20_047 with dissolve
    mc "We both know I’ll end up having to save you from mortal danger."
    scene ch3sc20_045 with dissolve
    sy "This is exciting! I can't wait to see the look on Dalen's face when you cruise through this quest!"
    sy "See you soon guys!"
    scene ch3sc20_046 with dissolve
    el "We won’t be long, Sylph."
    el "Keep our reward nearby! *Giggles*"
    mct "Goblins... this will be a good test for Eliza."
    mct "Sparring with me is one thing, battling goblins who will attempt to kill her is another."
    scene black with Dissolve(1.5)
    stop music fadeout 2.0
    $ renpy.pause(0.5)
    jump ch3sc20_b

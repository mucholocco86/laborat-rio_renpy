
label ch3sc6:

    window hide dissolve
    play music tavern_2 fadein 1.0
    scene black with Dissolve (2.0)
    "The two of you take your leave with your new supplies."
    scene ch3sc05_003 with Dissolve(2.0)
    $ renpy.pause(1)
    el "Sooo... have you given any more thought to what our first quest will be?"
    scene ch3sc05_002 with dissolve
    mc "I’m not sure what to expect."
    mc "But don’t get your hopes up for anything too exciting."
    scene ch3sc04_003 with dissolve
    el "You mean to tell me that they don’t just hand out high rank quests to complete rookies?"
    scene ch3sc04_002 with dissolve
    mc "Pretty much."
    mc "We’re currently D-Rank, as far I could tell from the look I got at the notice board we passed by."
    mc "So, most likely we'll have to progress up the ranks as follows D-Rank to C-Rank then B-Rank onto A-Rank and finally S-Rank."
    mc "It seems the difficulty and therefore reward from contracts & quests is tied to our Adventurers-Rank."
    scene ch3sc04_005 with dissolve
    el "Mmmh... You’ve got a point... as D-Class adventurers we probably won't get anything juicy."
    el "We should aim to reach a higher rank!"
    el "That way we could get quests that have better rewards and earn more coin!"
    scene ch3sc04_008e with dissolve
    el "We have to do our best, [mc]!"
    el "I'll accept nothing less."
    scene ch3sc04_008 with dissolve
    $ renpy.pause(2)
    scene ch3sc04_009 with dissolve
    mc "Why do I have the feeling that-"
    scene ch3sc04_010 with dissolve
    el "Nah-nah! Not telling."
    el "Just know I intend for us to reach the top ranks! S-Rank!"
    scene ch3sc04_008d with dissolve
    mc "Why do you care about our ranking?"
    mc "You know what our goal is."
    scene ch3sc04_008e with dissolve
    el "*Sighs* [mc]."
    el "Have you ever stopped to think about what life will be after we accomplish what we've set out to do?"
    el "Would we continue being adventurers? Would we separate and leave on different paths?"
    el "Would we buy a piece of land and become farmers?"
    scene ch3sc04_008d with dissolve
    mc "I... I don’t know."
    mc "Never really given any thought as what would come after."
    scene ch3sc04_008e with dissolve
    el "Exactly! I had a feeling you wouldn't be thinking longterm..."
    el "So I feel like at least one of us should be sensible and prepare for that."
    scene ch3sc04_008i with dissolve
    mc "Makes sense I suppose, I've always been so focused on... you know what."
    mc "But what does that have to do with us climbing the ranks of the guild?"
    scene ch3sc04_008e with dissolve
    el "As you said, higher rankings mean better quests and contracts that will bring in more coin."
    el "I want to be able to set aside a decent amount of coin from every quest."
    el "Not spend it all just as fast as we earn it."
    scene ch3sc04_008d with dissolve
    mc "Okay... makes sense."
    mc "I'm with you so far, go on."
    scene ch3sc02_007 with dissolve
    el "Once we’ve saved up a bunch, and we’ve gotten our... revenge."
    scene ch3sc02_005 with dissolve
    el "I suggest we purchase a house somewhere quiet? Still close to the capital, of course."
    el "But also far enough that we can have peace and relax!"
    el "Create a homestead, you know? Somewhere we can call home... it's something neither of us have had most of our lives."
    scene ch3sc02_009 with dissolve
    el "The divines know we'll need it after all this!"
    scene ch3sc02_010 with dissolve
    el "Now, c’mon! Let’s go pickup our first quest from Sylph!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1)
    "You catch up to her outside the guild."
    scene ch3sc02_011 with Dissolve(1.5)
    mct "Hmm... It’s actually not a bad idea... I've never really thought about what comes after."
    mct "She seems to have put quite a bit of thought into this... into... our future."
    mc "Eliza, wait up!"
    scene ch3sc06_001 with Dissolve(1.5)
    $ renpy.pause(0.5)
    el "Hmm?"
    ###Choice###
    menu:
        "Praise her idea." if True:
            scene ch3sc06_001 with dissolve
            $ eliza_trust += 2
            scene ch3sc06_002 with dissolve
            mc "You know what? That’s not a terrible idea."
            scene ch3sc06_003 with dissolve
            el "R-Really?! I was afraid you'd think it’s silly."
            "Eliza is pleasantly surprised that you praised her foresight, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            el "You don't think I'm getting ahead of myself?"
            scene ch3sc06_004 with dissolve
            mc "No, it makes sense. We don’t know how long it'll take us to get to that point."
            mc "Not to mention, I'm sure it won't be a straight path to vengeance, life don't tend to be that simple."
            mc "It feels great to have a plan, something we can work towards."
            scene ch3sc06_005 with dissolve
            el "*Giggles* You can call me Master-Planner from now on."
            el "You can add it to my ever-growing list of cool titles! *Snickers*"
            scene ch3sc06_006 with dissolve
            mc "Yeah... No."
            mc "Let's add it to the list of things to never call you."
            scene ch3sc06_007 with dissolve
            el "*Nudge* Don't be a meanie!"
            el "Just once? Please?"
            scene ch3sc06_006 with dissolve
            mc "Still a no."
            scene ch3sc06_008 with dissolve
            el "Whateverrr!"
            el "We both know I am! Mh-hm, Master-Planner Eliza."
            mct "*Chuckles* She's ridiculous..."
            scene ch3sc06_009 with dissolve
            el "Let’s go get that quest so we can begin climbing the ranks!"
            mc "Finally, a sensible suggestion."
            scene ch3sc06_007 with dissolve
            el "*Nudge* I'm gonna punch you!"
            el "Now c'mon before you say something you'll regret!"
            stop music fadeout 2.0
            scene black with Dissolve(1.5)
            jump ch3sc7

        "Refuse her idea." if True:
            scene ch3sc06_006 with dissolve
            mc "I don’t want to think that far ahead. We’ll just lose focus of our goal."
            scene ch3sc06_003 with dissolve
            el "I think we could manage fine. It won’t even require much effort."
            scene ch3sc06_006 with dissolve
            mc "Eliza, I’m not saying no. Just leave it for later, okay?"
            scene ch3sc06_003 with dissolve
            el "*Sigh* Fine, fine."
            $ eliza_trust -= 2
            "Eliza is disappointed that you won't consider the future, her trust has increased by {size=+3}{b}{color=#f00}2{/color}{/b}{/size}."
            scene ch3sc06_009 with dissolve
            el "But we still need to increase our ranking."
            el "Otherwise we'll be living in poverty and not be able to afford better equipment."
            el "Or food, or ales, or tavern rooms!"
            scene ch3sc06_006 with dissolve
            mc "You’re right."
            mc "We’ll need to earn a decent amount of coin if we want to accomplish anything."
            scene ch3sc06_004 with dissolve
            mc "Let’s go grab that quest and begin."
            stop music fadeout 2.0
            scene black with Dissolve(1.5)
            jump ch3sc7

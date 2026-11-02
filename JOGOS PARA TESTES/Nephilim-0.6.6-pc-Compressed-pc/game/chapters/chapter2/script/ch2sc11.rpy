#Start Chaper
label ch2sc11:

    #play music morning_1

    # start scene 2
        window hide dissolve
        #play music tavern_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ss91 with Dissolve (2.0)
        $ renpy.pause()
        scene ch2sc11_01 with Dissolve(2.0)
        $ renpy.pause()
        window show dissolve
        scene ch2sc11_01 with dissolve
        play music tavern_1 fadein 2.0
        mct "Hmm, it must be busy today. I can even hear the music out here."
        mct "Guess I’ll check if Eliza is anywhere to be found."
        scene ch2sc11_02 with dissolve
        mct "Hmm. Doesn’t seem like Eliza is here right now."
        mct "I guess I’ll have a drink while I wait."
        scene ch2sc11_03 with dissolve
        mct "Quite busy today compared to yesterday. I’m already looking forward to being on the road again."
        scene ch2sc11_04 with dissolve
        $ renpy.pause()
        scene ch2sc11_05 with dissolve
        mct "A dwarf? It’s been a while since I last saw one. I suppose it’s not that surprising."
        mct "They tend to travel around a lot, picking up any labor jobs they stumble upon."
        scene ch2sc11_06 with dissolve
        mct "Hmm. He's armed. I’ve never seen anyone in Riverside equipped with weapons before."
        mct "Maybe he's an escort for a merchant, or a traveling bounty hunter stopping here for a rest."
        scene ch2sc11_07 with dissolve
        mct "Clark is talking to some woman. Can’t say I’ve seen her before, either."
        mct "Not exactly surprising, considering I haven’t been back here for a decade now."
        scene ch2sc11_08 with dissolve
        mct "There’s bound to be new people that have settled down here over the years."
        scene ch2sc11_09 with dissolve
        cl "[mc]! What can I get you today?"
        scene ch2sc11_10 with dissolve
        mc "Hey, Clark. I’ll just have an ale, thanks."
        scene ch2sc11_11 with dissolve
        cl "One ale coming right up!"
        scene ch2sc11_12 with dissolve
        wo "Hey there handsome, you come here often?"
        ###Choice###
        menu:
            "Turn her down politely. ({color=#87e1fa}Light Path, Charisma{/color})":
                $ light += 1
                "{color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}"
                scene ch2sc11_13 with dissolve
                mc "Sorry, not interested."
                scene ch2sc11_14 with dissolve
                wo "You haven't even heard my offer."
                scene ch2sc11_15 with dissolve
                "..."
                scene ch2sc11_16 with dissolve
                wo "With looks like yours, I bet you get a lot of attention."
                scene ch2sc11_17 with dissolve
                mc "Sorry, lady. As I said, not interested."
                mc "You're beautiful, I can't imagine a woman like yourself has trouble finding a man."
                $ charisma += 1
                "The women appreciates your compliment, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc11_18 with dissolve
                wo "Are you sure I can't change your mind? I can be ... persuasive."

            "Be rude. ({color=#f00}Dark Path, Intimidation.{/color})":
                $ dark += 1
                "{color=#f00}Dark Morality{/color} Has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}"
                scene ch2sc11_13 with dissolve
                mc "No."
                scene ch2sc11_14 with dissolve
                wo "What’s the matter?"
                wo "Not used to an attractive woman giving you attention?"
                scene ch2sc11_15 with dissolve
                "..."
                scene ch2sc11_16 with dissolve
                wo "You might be hot, but that doesn't mean you'll get a chance like this again."
                scene ch2sc11_17 with dissolve
                mc "Look, I don't have time for you lady."
                mc "Yes, I could rock your world for one night. Who cares?"
                scene ch2sc11_18 with dissolve
                wo "You haven’t even heard what I have to offer."
                scene ch2sc11_19 with dissolve
                mc "I imagine it's tits and ass? You're nothing special, now back off or I'll put you down."
                "Your intimidation failed, but you've gained experience, your {b}{color=#fc584c}Intimidation{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc11_18 with dissolve
                wo "I don't believe you, you don't look like a man who'd hurt a woman."
                wo "Being with me could change your life kid."

        scene ch2sc11_19 with dissolve
        mc "Answer is still the same."
        scene ch2sc11_20 with dissolve
        wo "You’re a virgin, is that it? Hah, you wouldn’t be able to handle a real woman."
        scene ch2sc11_21 with dissolve
        mc "Go away... shoo!"
        mc "Make yourself disappear."
        scene ch2sc11_22 with dissolve
        wo "You have some nerve, kid! Most men would beg for my attention."
        scene ch2sc11_23 with dissolve
        el "Hi babe!"
        scene ch2sc11_24 with dissolve
        el "There you are! I’ve been looking all over for you."
        el "Typical, you're always sneaking away to the closest tavern!"
        el "Hope I didn’t make you wait long."
        mct "Ahh... I see what she's playing at, this might work."
        scene ch2sc11_25 with dissolve
        mc "No, it’s fine... honey."
        scene ch2sc11_26 with dissolve
        wo "I’m sorry miss, I didn’t know he was spoken for."
        scene ch2sc11_27 with dissolve
        with vpunch
        el "Not another word out of you!"
        el "Find your own man."
        scene ch2sc11_28 with dissolve
        el "Let’s go to our room, handsome!"
        scene ch2sc11_29 with dissolve
        mc "Sure, beautiful."
        scene ch2sc11_30 with dissolve
        "..."
        scene ch2sc11_31 with dissolve
        "......"
        scene ch2sc11_32 with dissolve
        wo "Pffft."
        wo "That girl doesn’t even hold a candle to a woman like me."
        scene ch2sc11_33 with dissolve
        with vpunch
        wo "Innkeep! Another ale!"
        stop music fadeout 2.0
        scene black with Dissolve(3)
        jump ch2sc12

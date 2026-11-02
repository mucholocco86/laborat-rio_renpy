#Start Chaper
label ch2sc12:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music home_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc12_01 with Dissolve(2.0)
        $ renpy.pause(0.2)
        window show dissolve
        scene ch2sc12_01
        mc "Not that I don't appreciate the backup, but..."
        scene ch2sc12_02 with dissolve
        mc "Babe? Handsome?"
        scene ch2sc12_03 with dissolve
        el "I was improvising!"
        el "I saw you struggling... thought I'd help you out."
        scene ch2sc12_04 with dissolve
        mc "And that’s what you thought of?"
        scene ch2sc12_05 with dissolve
        el "*Snickering* Worked, didn’t it?"
        el "She was completely dumbfounded!"
        scene ch2sc12_06 with dissolve
        mc "Yeah... Thanks for the save, by the way."
        mc "She didn't seem too thrilled being turned down."
        scene ch2sc12_07 with dissolve
        el "No problem!"
        el "I couldn’t exactly let some old woman get her claws into you."
        scene ch2sc12_05 with dissolve
        el "Although, it would have been funny to see how you'd get away from her."
        scene ch2sc12_06 with dissolve
        mc "I'm just happy we won't have to find out."
        scene ch2sc12_08 with dissolve
        mc "So, was that the only reason for your heroic moment?"
        scene ch2sc12_09 with dissolve
        el "Wh-what do you mean? Of course! Don-Don’t be silly!"
        el "What other reason could there be?"
        scene ch2sc12_08 with dissolve
        mc "So you weren’t jealous by seeing that woman all over me?"
        scene ch2sc12_09 with dissolve
        el "J-Jealous? Me?"
        scene ch2sc12_10 with dissolve
        el "Why would I be jealous?"
        el "It's not like we're together or anything..."
        scene ch2sc12_11 with dissolve
        el ".."
        el "....."
        el "........."
        mc "Eliza..."
        scene ch2sc12_12 with dissolve
        el "Okay, okay!"
        el "Maybe I just got a tiny winy, itsy-bit jealous."
        scene ch2sc12_13 with dissolve
        $ renpy.pause(0.5)
        mc "*Scoffs* ..."
        scene ch2sc12_10 with dissolve
        el "Don’t think anything of it, okay?"
        el "I just didn’t like her trying to seduce you."
        scene ch2sc12_14 with dissolve
        with vpunch
        el "Disgusting! Urrrh!"
        el "She can find a guy her own age to play with!"

        if eliza_relationship == True:
            scene ch2sc12_09 with dissolve
            el "You're my first kiss... we shared a bed..."
            scene ch2sc12_10 with dissolve
            el "I-I like you... when I saw her trying to get with you-... I..."
            el "She was totally drooling all over you! Uck!"
            scene ch2sc12_14 with dissolve
            with vpunch
            el "Ugh! Why does it make me feel this way! Hnngh!"
            mct "*Chuckles* It's cute that she gets jealous, she really does care."

        else:
            scene ch2sc12_13 with dissolve

        scene ch2sc12_13 with dissolve
        stop music fadeout 2.0
        mc "..."
        scene ch2sc12_15 with dissolve
        play music morning_1 fadein 2.0
        mc "Come here."
        scene ch2sc12_17 with dissolve
        el "Wha-"
        scene ch2sc12_16 with dissolve
        mc "Are you going to keep me waiting?"
        scene ch2sc12_17 with dissolve
        el "No, I- I..."
        scene ch2sc12_18 with dissolve
        with vpunch
        el "NyahH!"
        $ renpy.pause()
        scene ch2sc12_18 with dissolve
        "Eliza doesn't even finish her sentence before she rushes into your arms."
        scene ch2sc12_19 with dissolve
        el "Why? I thought you didn't like hugs."
        el "No-Not that I mind."
        ###Choice###
        scene ch2sc12_20 with dissolve
        menu:
            "I enjoy hugging you. ({color=#ff8cdd}Romance{/color})":
                $ eliza_trust += 3
                "Eliza feels a strong connection to you. Her trust increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
                scene ch2sc12_20 with dissolve
                mc "Hugging you makes me forget all the bad shit that I've been through."
                scene ch2sc12_21 with dissolve
                el "Then you should hug me more often..."
                el "I'd like more hugs... from you."

            "Don't get used to it. (Neutral)":
                $ eliza_trust += 1
                "Eliza appreciates your friendly banter. Her trust increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc12_20 with dissolve
                mc "I suppose I don't mind it, every now and then."

                scene ch2sc12_21 with dissolve
                el "You'll just have to endure them for my sake."

        scene ch2sc12_20 with dissolve
        mc "*Chuckles* I'll keep that in mind."
        scene ch2sc12_22 with dissolve
        mc "Thank you for the rescue, by the way."
        scene ch2sc12_23 with dissolve
        el "You’re welcome, I suppose."
        scene ch2sc12_24 with dissolve
        el "She was looking at you like she wanted to eat you!"
        scene ch2sc12_20 with dissolve
        mc "Thank god you came to my rescue, then."
        scene ch2sc12_23 with dissolve
        el "Count on me anytime you need help fending off old women!"
        scene ch2sc12_25 with dissolve
        el "..."
        el "Mhm. This is nice."
        scene ch2sc12_22 with dissolve
        mc "Don’t get used to it."
        scene ch2sc12_25 with dissolve
        el "Why not? I can feel you like it just as much as me."
        scene ch2sc12_26 with dissolve
        mc "I don’t."
        scene ch2sc12_25 with dissolve
        el "[mc]..."
        scene ch2sc12_27 with dissolve
        el "We don’t lie to each other. Remember?"
        scene ch2sc12_28 with dissolve
        mc "Fine, fine... I suppose I like it."
        mc "When it's you."
        scene ch2sc12_22 with dissolve
        mc "Happy?"
        scene ch2sc12_25 with dissolve
        el "Very much so!"
        scene ch2sc12_19 with dissolve
        el "You know? I just had a thought..."
        scene ch2sc12_21 with dissolve
        el "We should make this a daily thing."

        #Choice
        menu:
            "I can live with that. ({color=#2bff8b}Friendly{/color})":
                scene ch2sc12_20 with dissolve
                mc "Count me in."
                mc "Hugging you more often... I can live with that."
                scene ch2sc12_23 with dissolve
                el "*Giggling* I knew you would approve!"
                "You feel Eliza squeezing herself further into you."
                $ eliza_trust += 1
                "Eliza feels excited... Eliza's trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

            "Do we have to? (Neutral)":
                scene ch2sc12_22 with dissolve
                mc "Daily? That's a bit much don't you think?"
                scene ch2sc12_23 with dissolve
                el "I think that's the perfect amount!"

        scene ch2sc12_28 with dissolve
        mc "You think the coast is clear downstairs?"
        mc "I never got the ale I ordered."
        scene ch2sc12_29 with dissolve
        el "She's probably gone by now, but so is your ale."
        el "I saw her drinking it as we left."
        scene ch2sc12_30 with dissolve
        mc "That bitch!"
        scene ch2sc12_31 with dissolve
        el "Don't worry, I'm sure Clark will make you another."
        el "In exchange for some coins, of course."
        scene ch2sc12_32 with dissolve
        mc "You're enjoying this way too much."
        mc "Anyways let's head back down."

        if harem_path == True:
            scene ch2sc12_34 with dissolve
            el "*Snickers* You're eager to get back down and see if there's anymore women for you to add to your harem?"
            el "I'm not going to chase off anymore women tonight!"
            scene ch2sc12_33 with dissolve
            mc "Hmm... what if I wanted to add you to my harem?"
            el "*Snickers* Me!?"
            scene ch2sc12_34 with dissolve
            el "I'd wish you goodluck!"
            scene ch2sc12_33 with dissolve
            mc "Challenge accepted, you're going to beg to be part of my harem."
            "Eliza snickers at your remark in disbelief."
            mc "We better head back down and get some ales ordered."

        else:
            pass

        if eliza_relationship == True:
            scene ch2sc12_33 with dissolve
            el "Yeah, the others should be here soon... if they aren’t already."
            scene ch2sc12_34 with dissolve
            el "There’s just something I’ve gotta do real quick!"
            scene ch2sc12_35 with dissolve
            $ renpy.pause()
            scene ch2sc12_35_5 with dissolve
            "Eliza leans against you as she kisses you."
            scene ch2sc12_35 with dissolve
            $ renpy.pause(2)
            scene ch2sc12_35_5 with dissolve
            "You can tell how much she enjoys it by how enthusiastic she is."
            scene ch2sc12_35 with dissolve
            el "Mhmm..."
            scene ch2sc12_36 with dissolve
            el "There!"
            el "Now we can head downstairs."
            scene ch2sc12_37 with dissolve
            mc "Damn, kitten."
            scene ch2sc12_36 with dissolve
            el "Like it?"
            scene ch2sc12_37 with dissolve
            mc "Like it? I loved it."
            scene ch2sc12_36 with dissolve
            el "Good, good... in that case!"
            scene ch2sc12_35 with dissolve
            with vpunch
            $ renpy.pause(0.5)
            el "Mmmh! Nnhh..."
            scene ch2sc12_36 with dissolve
            el "Okaaay... Let's get going before I drag you to the bed over there."
            scene ch2sc12_44 with dissolve
            mc "You won't hear me complaining."
            scene ch2sc12_39 with dissolve
            el "C’mon... let’s order some ales while we wait for the others!"
            scene ch2sc12_40 with dissolve
            mc "I’m down for that. Tomorrow, our journey to Luxenford begins."
            mc "Luxenford should be anywhere from 4 to 7 days on foot from Riverside, depending on the conditions."
            scene ch2sc12_41 with dissolve
            mc "We won’t know how often we'll be able to stay in a village, or find a tavern along the road."
            scene ch2sc12_42 with dissolve
            el "Then it’s settled!"
            el "We’re going to enjoy our last night here to the fullest!"
            scene ch2sc12_43 with dissolve
            el "My butt is really not looking forward to sleeping outside again."
            el "The freezing ground doesn't do you any favors, right my poor bum?"
            scene ch2sc12_44 with dissolve
            mc "On this, my butt agrees with yours."
            scene ch2sc12_45 with dissolve
            el "Our butts are buddies!"
            scene ch2sc12_46 with dissolve
            mc "Has anyone ever told you, you’re a weirdo?"
            scene ch2sc12_47 with dissolve
            el "You, a few times."
            el "But... you like it!"
            scene ch2sc12_48 with dissolve
            mc "Let’s go."
            scene ch2sc12_49 with dissolve
            el "Hey, don’t leave without your butt-buddy!"
            scene ch2sc12_50 with dissolve
            mc "*Chuckles* Every butt for themselves!"
            scene ch2sc12_51 with dissolve
            stop music fadeout 2.0
            el "Wait up!"
            scene black with Dissolve(2)

        else:
            scene ch2sc12_38 with dissolve
            el "Yeah, I'm having a few drinks tonight!"
            scene ch2sc12_39 with dissolve
            el "C’mon let’s order some ales while we wait for the others!"
            scene ch2sc12_40 with dissolve
            mc "I’m down for that. Tomorrow, our journey to Luxenford begins."
            scene ch2sc12_41 with dissolve
            mc "We won’t know how often we'll be able to stay in a village, or find a tavern along the road."
            scene ch2sc12_42 with dissolve
            el "Then it’s settled. We’re going to enjoy our last night here to the fullest!"
            scene ch2sc12_43 with dissolve
            el "My butt is really not looking forward to sleeping outside again."
            scene ch2sc12_44 with dissolve
            mc "My butt agrees with yours."
            scene ch2sc12_45 with dissolve
            el "Our butts are buddies!"
            scene ch2sc12_46 with dissolve
            mc "Has anyone ever told you you’re a weirdo?"
            scene ch2sc12_47 with dissolve
            el "You like it!"
            scene ch2sc12_48 with dissolve
            mc "Let’s go."
            scene ch2sc12_49 with dissolve
            el "Hey, don’t leave without your butt-buddy!"
            scene ch2sc12_50 with dissolve
            mc "Every butt for themselves!"
            scene ch2sc12_51 with dissolve
            stop music fadeout 2.0
            el "Wait up!"
            scene black with Dissolve(2)

        jump ch2sc13

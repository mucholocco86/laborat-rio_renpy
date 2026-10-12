#Start Chaper
label ch2sc6:

    #play music home_1

    # start scene 2
        window hide dissolve
        play music home_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc6_01 with Dissolve(2.0)
        $ renpy.pause()
        window show dissolve
        scene ch2sc6_02 with dissolve
        $ renpy.pause()
        scene ch2sc6_03 with dissolve
        $ renpy.pause()
        scene ch2sc6_04 with dissolve
        mct "Heh. Sleeping like a log..."
        mct "I suppose we did have some pretty eventful days."
        mct "She's impressive, if we keep training, she will become a force to be reckoned with."

        if eliza_relationship == True:
            scene ch2sc6_05 with dissolve
            mct "She’s kinda cute when she sleeps."
            scene ch2sc6_06 with dissolve
            $ renpy.pause()
            scene ch2sc6_07 with dissolve
            $ renpy.pause()
            el "Nnhh..."
            scene ch2sc6_08 with dissolve
            $ renpy.pause()
            scene ch2sc6_09 with dissolve
            mct "Did last night really happen?"
            scene ch2sc6_10 with dissolve
            mct "We... we kissed."
            mct "It felt surreal, the more our lips merged, the more I wanted."
            scene ch2sc6_11 with dissolve
            mct "I’ve never felt anything like it before."
            mct "It was like..."
            scene ch2sc6_11 with dissolve
            mct "A surge of excitement mixed with raw emotion when our lips touched."
            scene ch2sc6_12 with dissolve
            mct "Neither of us pulled away, either. Until I lost control."
            mct "Did she like it as much as I did?"
            scene ch2sc6_13 with dissolve
            mct "She also seems to have an effect on me."
            mct "Somehow, she’s able to calm me when I lose control. But how?"
            scene ch2sc6_14 with dissolve
            mct "She doesn’t have any magic capabilities, as far as I can tell."
            scene ch2sc6_13 with dissolve
            mct "I guess I shouldn't complain..."
            mct "Just knowing she's able to calm me already makes me feel at ease."

        else:
            scene ch2sc6_15 with dissolve
            $ renpy.pause()

        scene ch2sc6_15 with dissolve
        "..."
        scene ch2sc6_16 with dissolve
        $ renpy.pause()
        el "Nnnh..."
        scene ch2sc6_17 with dissolve
        $ renpy.pause()
        scene ch2sc6_18 with dissolve
        elt "Huh? [mc]'s up already?"
        scene ch2sc6_19 with dissolve
        el "Were you watching me sleep?"
        mc "No-"
        scene ch2sc6_21 with dissolve
        el "Don't even try and deny it. I caught you!"
        scene ch2sc6_20 with dissolve
        mc "I wasn't."
        mc "I just woke up, then I noticed how nice and quiet you could be."
        scene ch2sc6_22 with dissolve
        el "Oh please! You enjoy my company."
        scene ch2sc6_23 with dissolve
        mc "You wish!"
        scene ch2sc6_24 with dissolve
        mc "Now, get up."
        mc "There won’t be any breakfast until you’re done with today's lesson."
        scene ch2sc6_25 with dissolve
        el "Huuuh! That's not fair!"
        el "How am I supposed to work hard on an empty belly!"
        scene ch2sc6_24 with dissolve
        mc "You wanted adventure?"
        mc "Well, first lesson is... you’ve got to earn your meals."
        scene ch2sc6_26 with dissolve
        el "*Sigh* Meanie..."
        scene ch2sc6_27 with dissolve
        "A few moments later you’re ready, while Eliza seems to be taking her time."
        ".."
        "....."
        "........."
        scene ch2sc6_28 with dissolve
        mc "I’ll wait for you outside."
        scene ch2sc6_29 with dissolve
        scene ch2sc6_30 with dissolve
        mct "I can't tell if she actually believes she has a chance or..."
        mct "... if she's just that stubborn."
        mct "Oh well. I guess that only time will tell."
        scene ch2sc6_31 with dissolve
        mc "Don’t be too long."
        scene ch2sc6_32 with dissolve
        elt "Now, where did I put my boots.?"
        elt "Ahh, there they are. Okay! Better get going!"
        scene ch2sc6_32_5 with dissolve
        elt "Aaaand... finally last strap in place!"
        elt "I'd like to have a word with whoever designed these boots."
        scene ch2sc6_33 with dissolve
        elt "I can’t believe [mc]..."
        elt "Earn my meals?!"
        scene ch2sc6_34 with dissolve
        elt "Why couldn’t we just have breakfast first?"
        elt "It would be so much better!"
        scene ch2sc6_35 with dissolve
        elt "I’m sure there’s a reason for his madness."
        elt "I’ll find out after I kick his ass."
        scene ch2sc6_36 with dissolve
        elt "It felt really comfortable having him next to me last night."
        scene ch2sc6_37 with dissolve
        elt "I wonder if he felt the same way about it too?"
        elt "I felt him put his arm around me... I hope he didn't notice how red my cheeks got!"

        if eliza_relationship == True:
            scene ch2sc6_38 with dissolve
            elt "And the kiss..."
            elt "I really want to do it again."
            elt "I can still feel it lingering on my lips..."
            scene ch2sc6_39 with dissolve
            elt "When his lips touched mine, it... it felt like everything bad just disappeared."
            elt "He was so tender, almost like he was afraid of harming me."
            elt "Divines! My belly feels funny just thinking about it."
            scene ch2sc6_40 with dissolve
            elt "It was just us... together."
            elt "I've never felt anything like it... it was so intimate..."
            scene ch2sc6_41 with dissolve
            elt "At one point, I thought he was going to throw me down and ravish me."
            elt "If he had done that... I'd have given myself to him, my body and soul wanted it."
            scene ch2sc6_42 with dissolve
            elt "Heavens... he was so hot!"
            elt "I'm getting flustered just thinking about if it could happen again tonight... mhh!"

        else:
            scene ch2sc6_43 with dissolve

        scene ch2sc6_43 with dissolve
        with vpunch
        elt "Arrhh! Stop it, Eliza!! {b}Focus!{/b}"
        scene ch2sc6_44 with dissolve
        elt "You have a goal to achieve..."
        elt "Make him regret skipping breakfast! I'll show him no mercy!"
        scene black with Dissolve(2)
        $ renpy.pause(1)
        jump ch2sc7

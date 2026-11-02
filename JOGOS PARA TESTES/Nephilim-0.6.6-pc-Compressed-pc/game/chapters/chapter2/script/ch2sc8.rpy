#Start Chaper
label ch2sc8:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music chill_4 fadein 2.0
        scene black with Dissolve (1.0)
        scene ch2sc8_01 with Dissolve(2.0)
        $ renpy.pause()
        window show dissolve
        scene ch2sc8_01 with dissolve
        el "Huh. Do you know that girl? She’s staring at us."
        scene ch2sc8_02 with dissolve
        mc "Hmm?"
        scene ch2sc8_03 with dissolve
        $ renpy.pause()
        scene ch2sc8_04 with dissolve
        mct "A-Alice?"
        stop music fadeout 2.0
        scene ch2sc8_05 with dissolve
        al_t "[mc]?"
        play music darknight_2 fadein 2.0
        scene ch2sc8_06 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_08 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_06 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_08 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_06 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_09 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_10 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_11 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_12 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_07 with dissolve
        $ renpy.pause()
        stop music fadeout 2.0
        scene ch2sc8_04 with dissolve
        mct "Uh, oh. I know that look."
        scene ch2sc8_07 with dissolve
        $ renpy.pause(2)
        play music darknight_3 fadein 2.0
        scene ch2sc8_13 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_14 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_15 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_16 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_17 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_18 with dissolve
        mc "Ali-"
        scene ch2sc8_19 with dissolve
        $ renpy.pause(2)
        scene ch2sc8_20 with dissolve
        with vpunch
        "{b}*SMACK*{/b}"
        scene ch2sc8_21 with dissolve
        al "You promised!"
        scene ch2sc8_22 with dissolve
        mc "Al-"
        scene ch2sc8_23 with dissolve
        al "Y-you left me."
        scene ch2sc8_24 with dissolve
        al "I thought you were- you were dead!"
        scene ch2sc8_23 with dissolve
        al "How could you, [mc]?"
        scene ch2sc8_22 with dissolve
        mc "Alice..."
        scene ch2sc8_25 with dissolve
        with vpunch
        al "{b}No!{/b} I don’t want to listen to you. Always and forever was a lie!"
        stop music fadeout 2.0
        scene ch2sc8_26 with dissolve
        $ renpy.pause()
        scene ch2sc8_27 with dissolve
        mc "Alice... I never forgot."
        scene ch2sc8_28 with dissolve
        $ renpy.pause()
        scene ch2sc8_29 with dissolve
        play music chill_4 fadein 2.0
        el "Alice? With that reaction I imagined an ex-girlfriend."
        scene ch2sc8_31 with dissolve
        mc "You do realize I was only ten summers old when I left this place?"
        scene ch2sc8_29 with dissolve
        el "Oh... right."
        scene ch2sc8_31 with dissolve
        mc "That was my best friend... the one I told you about."
        scene ch2sc8_32 with dissolve
        el "Ah, so that’s Alice?"
        scene ch2sc8_33 with dissolve
        mc "Yeah... the one and only."
        scene ch2sc8_34 with dissolve
        el "So... what was the promise about?"
        scene ch2sc8_35 with dissolve
        mc "I promised her that I would always protect her."
        scene ch2sc8_36 with dissolve
        mc "As you can imagine, I wasn’t able to keep my promise for a while."
        scene ch2sc8_37 with dissolve
        el "You clearly didn’t have a choice, otherwise you would have kept it."
        scene ch2sc8_38 with dissolve
        mc "What makes you say that?"
        scene ch2sc8_37 with dissolve
        el "You’re not the only one who can sense things. You’re not a liar."
        scene ch2sc8_39 with dissolve
        el "I know you'd have done anything to honor your promise, if it was possible."
        scene ch2sc8_41 with dissolve
        mc "Eliza... I appreciate your opinion, but I should've done more."
        mc "Now, let’s get that breakfast."
        scene ch2sc8_42 with dissolve
        with vpunch
        el "{b}Hold it!{/b}"
        el "You’re not having breakfast. You'll go make things right with Alice, while I have breakfast."
        scene ch2sc8_43 with dissolve
        el "We’ll meet up later."
        scene ch2sc8_44 with dissolve
        mct "Does Eliza have a point? Should I try to smooth things over with Alice?"
        mct "Eliza doesn’t know Alice like I do. It might be better to let her cool off before talking to her."
        stop music fadeout 2.0


        menu:
            #CHOICE 8a (Light)
            "Go look for Alice ({color=#87e1fa}Light Path{/color})":
                "{color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                $ light += 1
                $ eliza_trust += 1
                scene ch2sc8_45 with dissolve
                play music chill_4 fadein 2.0
                mc "Wha-"
                scene ch2sc8_46 with dissolve
                el "Earn it."
                scene ch2sc8_47 with dissolve
                mc "Hrrrh."
                scene ch2sc8_46 with dissolve
                el "Now, go!"
                mc "Fine, fine! I'll go talk to Alice..."
                "Eliza appreciates you taking her advice. Eliza's trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc8_48 with dissolve
                mct "Earn it? Using my own words against me! She’s really something else."
                mct "She's right, though. I have to make up with Alice."
                mct "At the very least, try to explain about what happened."
                scene black with Dissolve(3)
                stop music fadeout 2.0
                jump ch2sc9

            #CHOICE 8b (Dark)
            "Tell Eliza to stay out of it. ({color=#f00}Dark Path){/color}":
                $ dark += 1
                "{color=#f00}Dark Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc8_49 with dissolve
                play music explore_1 fadein 2.0
                mc "Back off, Eliza. It’s complicated."
                scene ch2sc8_50 with dissolve
                el "I-I was only trying to help."
                scene ch2sc8_51 with dissolve
                mc "Well, don’t."
                scene ch2sc8_52 with dissolve
                el "Okay, okay. I’ll stay out of it."
                scene ch2sc8_53 with dissolve
                el "I’ll see you later at the tavern. You'd better not bring that attitude back with you..."
                el "Otherwise you’ll be enjoying a nice cozy night on the floor."
                scene ch2sc8_54 with dissolve
                mc "Whatever."
                scene ch2sc8_55 with dissolve
                el "..."
                "Eliza feels like you don't value her opinion."
                "Eliza's trust has decreased by {size=+3}{b}{color=#f00}1{/color}{/b}{/size}."
                $ eliza_trust -= 1
                stop music fadeout 2.0
                scene black with Dissolve(3)
                jump ch2sc10

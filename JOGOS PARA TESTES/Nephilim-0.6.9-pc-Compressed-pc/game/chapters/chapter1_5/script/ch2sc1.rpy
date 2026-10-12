# Start Chaper
label ch2sc1:

    #play music home_1
    #stop music fadeout 2.0
    #window show dissolve
    #play music intro_1
    #show ch1sc0 with Dissolve (4.0)
    #show name_screen with fade

    # start scene 1
        scene chapter_screen with dissolve
        $ renpy.pause()
        scene chapter_screen1 with dissolve
        $ renpy.pause()
        window hide dissolve
        play music home_1
        scene black with Dissolve (2.0)
        "10 years later.."
        scene ch2sc01 with Dissolve(4)
        window show dissolve
        mct ".."
        scene ch2sc02 with dissolve
        mct "....."
        scene ch2sc03 with dissolve
        mct "........."
        scene ch2sc04 with dissolve
        mct "Should only be a few more days on the road now til I reach Riverside."
        scene ch2sc05 with dissolve
        mct "I wonder if I’ll run into them?"
        mct "Old man Gibs... Flynn... Sabrina... Alice."
        scene ch2sc06 with dissolve
        mct "No. I’ve got to avoid them, I can’t let them get involved."
        mct "But it sure would be nice to see them again. Fuck!"
        mct "Snap out of it, [mc]! You know it will only put them in danger."
        scene ch2sc07 with dissolve
        "You continue down the beaten path for a few miles."
        scene ch2sc03 with dissolve
        ".."
        scene ch2sc08 with dissolve
        "...."
        scene ch2sc04 with dissolve
        "......."
        scene ch2sc07 with dissolve
        with vpunch
        uk "{b}*Scream*{/b} Aaiiiee! Leave me alone!!"
        scene ch2sc08 with dissolve
        mct "Huh? The scream came from over there."
        scene ch2sc09 with dissolve
        uk "Get off me! You filthy swines!"
        scene ch2sc10 with dissolve
        uk "Come on sweetheart, let’s have some fun."
        scene ch2sc11 with dissolve
        uk "My friend and I like sweet things."
        uk "And you sure are a treat!"
        scene ch2sc12 with dissolve
        uk "Hrrrrah! I’ll cut off your tiny balls and stuff them down your throats!"
        uk "Woah, woah! Such a dirty mouth on such a pretty face."
        scene ch2sc13 with dissolve
        mct "*Sigh* So much for a peaceful journey home."
        scene ch2sc14 with dissolve
        uk "Get off me! I'll make sure to make you regret ever being born!"
        scene ch2sc13 with dissolve
        mct "Hmm... How should I handle this?"
        ###Choice###
        menu:
            #Light choice
            "Neutralize the outlaws. ({color=#87e1fa}Light Path{/color})":
                scene ch2sc13 with dissolve
                $ eliza_trust += 1
                $ light += 1
                "{color=#87e1fa}Light Morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                mct "Idiots like these guys really get my blood boiling. I'll help her."
                scene ch2sc15 with dissolve
                mc "Miss, are these men bothering you?"
                scene ch2sc16 with dissolve
                uk "Who the hell are you!?"
                scene ch2sc17 with dissolve
                mc "How about you fellas leave her alone? She clearly doesn’t want you harassing her."
                scene ch2sc18 with dissolve
                uk "Keep walking if you want to live, fool!"
                scene ch2sc19 with dissolve
                uk "No! Please..."
                scene ch2sc20 with dissolve
                with vpunch
                uk "Shut up! {b}BITCH!{/b}"
                scene ch2sc21 with dissolve
                mc "That’s not how you treat a lady."
                scene ch2sc18 with dissolve
                uk "Hah! What do you care? She’s not your girl. Mind your own business and get lost!"
                scene ch2sc19 with dissolve
                uk "Please..."
                scene ch2sc22 with dissolve
                with vpunch
                uk "I told you to shut it! {b}YOU BITCH!{/b}"
                scene ch2sc23 with dissolve
                uk "Arrgh! Wh-What are you doing?!"
                "You squeeze his wrist tightly as the guy starts to squirm in pain."
                uk "Let me go, you psycho!"
                scene ch2sc24 with dissolve
                with vpunch
                "You grant his wish, followed by a swift bone-cracking punch to his cheek."
                scene ch2sc25 with dissolve
                mc "All bark, no bite, eh?"
                scene ch2sc26 with dissolve
                with vpunch
                uk "Get off me you creep!!"
                scene black with Dissolve (2.0)
                jump ch2sc27

                #Dark Choice
            "Leave them alone. ({color=#f00}Dark Path{/color})":
                scene ch2sc13 with dissolve
                $ dark += 1
                "{color=#f00}Dark Morality{/color} increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                mct "Not worth the hassle... The faster I reach Riverside, the better."
                scene ch2sc03 with dissolve
                uk "Help! Please!"
                scene ch2sc22 with dissolve
                uk "Shut up! You filthy bitch!"
                uk "Once we’re done with you... no man will want you ever again!"
                scene ch2sc14 with dissolve
                uk "Let go of me! You disgusting pigs!"
                scene ch2sc13 with dissolve
                mct "*Sigh* Guess I can't help myself."
                scene ch2sc22 with dissolve
                uk "I'll show you how to obey a man!"
                scene ch2sc23 with dissolve
                uk "Who are you?!"
                scene ch2sc24 with dissolve
                with vpunch
                uk "Arrrgh!"
                "As your fist connects, you feel his cheekbone cracking under the force of your punch."
                scene ch2sc25 with dissolve
                mc "He won't be waking up anytime soon."
                scene ch2sc26 with dissolve
                with vpunch
                uk "Hirrya! Take this, you ugly pervert!"
                scene black with Dissolve (2.0)
                stop music fadeout 2.0
                jump ch2sc27

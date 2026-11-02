#Start Chaper
label ch2sc23:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music outdoors_2 fadein 2.0
        scene black with Dissolve (1.0)
        "You head over to investigate the noise."
        scene ch2sc23_01 with Dissolve(2.0)
        uk "Where did I put the bloody thing!"

        scene ch2sc23_02 with dissolve
        $ renpy.pause(1)
        scene ch2sc23_01 with dissolve
        $ renpy.pause(1)
        scene ch2sc23_02 with dissolve
        $ renpy.pause(1)
        scene ch2sc23_01 with dissolve
        $ renpy.pause(1)
        scene ch2sc23_03 with dissolve
        $ renpy.pause()
        scene ch2sc23_03 with dissolve
        uk "Blasted!"
        with vpunch
        uk "I just had it! A small bump on this rock and it's gone?! Arh!"
        scene ch2sc23_04 with dissolve
        el "*Whispers* {size=-10}{b}Should we say hi?{/b}{/size}"
        scene ch2sc23_05 with dissolve
        mc "Sure, go for it."
        scene ch2sc23_06 with dissolve
        with vpunch
        uk "{b}BLASTED!{/b} Tis not here! Me wife will skin me hide for this!"
        scene ch2sc23_07 with dissolve
        el "Uhm... Hi, sir."
        scene ch2sc23_08 with dissolve
        uk "Who are ye? What do ye want?"
        scene ch2sc23_09 with dissolve
        el "We-"
        scene ch2sc23_10 with dissolve
        with vpunch
        uk "Arrgh! Don’t bother me with yer squabbles!"
        scene ch2sc23_11 with dissolve
        mc "Looks like you lost something?"
        mc "Maybe we can help?"
        scene ch2sc23_12 with dissolve
        uk "Bloody arse, stick! Ha! Ye help me?"
        scene ch2sc23_13 with dissolve
        uk "I know yer kind, lad! Ye’d just as soon rob me as help me!"
        scene ch2sc23_14 with dissolve
        mc "*Sigh* Hey, Eliza... Let’s search the nearby area and see if we can find anything out of the ordinary."
        scene nz_fight_136 with dissolve
        el "Uh, okay! Anything out of the ordinary... anything."
        scene nz_fight_130 with dissolve
        $ renpy.pause()
        scene nz_fight_147 with dissolve
        el "This won’t be easy..."
        el "We don’t even know what to look for!"
        scene nz_fight_146 with dissolve
        el "I’m surprised you even want to help this guy?"
        el "He was very rude to us."
        scene nz_fight_130 with dissolve
        mc "I think he's just worked himself up in frustration, dwarves tend to get a little overzealous."
        el "Oh, I've never met a dwarf before... have you?"
        mc "Mmh, just a couple. C'mon, let's search this area."
        scene black with Dissolve(1.5)
        "You and Eliza search the area for anything that isn't 'natural'."
        scene ch2sc23_15 with Dissolve(1.5)
        $ renpy.pause()
        scene ch2sc23_16 with dissolve
        $ renpy.pause()
        scene ch2sc23_17 with dissolve
        $ renpy.pause()
        scene ch2sc23_18 with dissolve
        $ renpy.pause()
        "..."
        "........"
        scene ch2sc23_19 with dissolve
        $ renpy.pause()
        scene ch2sc23_20 with dissolve
        mc "Hey, check this out."
        scene ch2sc23_21 with dissolve
        $ renpy.pause(1)
        mc "You present Eliza with your find, a silver-crested ring."
        scene ch2sc23_22 with dissolve
        $ renpy.pause()
        mc "There’s something strange about it, though."
        mc "I can feel slight magical vibrations from it... it could be enchanted."
        mc "But... this would be expensive, way too expensive for a traveling merchant."
        el "Not to mention the size of it... that wouldn't fit his dwarven fingers."
        scene ch2sc23_23 with dissolve
        el "But that has to be what he’s looking for, right?"
        el "No other reason something shiny like this would be laying around, especially right in the area?"
        scene ch2sc23_24 with dissolve
        mc "Mhh. That’s what I’m thinking."
        mc "Now we have a decision to make... do we keep it or do we return it?"

        scene ch2sc23_22 with dissolve
        $ renpy.pause(1)
        el "Uhh... I'm leaning towards returning it to him, but you decide! I'll follow your lead."
        #CHOICE
        menu:
            "Let the dwarf know about your discovery. ({color=#87e1fa}Light Path{/color})":
                scene ch2sc23_22 with dissolve
                $ light += 1
                $ borri_ring = True
                "{color=#87e1fa}Light morality{/color} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc23_25 with dissolve
                mc "Hey, listen. We found something. It might be yours."
                scene ch2sc23_08 with dissolve
                uk "Hrrm. What? Yer still here?"
                scene ch2sc23_11 with dissolve
                mc "Just take a look."
                scene ch2sc23_10 with dissolve
                uk "This could be a trick! Aye... ye be trying to fool me and rob me!"
                scene ch2sc23_26 with dissolve
                with vpunch
                el "{size=+5}{b}*Angry*{/b}{/size} {b}Now you listen here, you stubborn stinky man!{/b}"
                el "We just spent an hour searching around for your stupid ring!"
                scene ch2sc23_27 with dissolve
                el "Even though you were rude to us, we decided to help you out."
                el "And now you have the nerve to doubt us still?!"
                scene ch2sc23_26 with dissolve
                el "Give me one good reason why I shouldn’t just knock some sense and common decency into your stubborn ass right now!"
                scene ch2sc23_28 with dissolve
                mct "Damn... remind me not to get on her bad side."
                scene ch2sc23_12 with dissolve
                uk "{b}*Surprised*{/b} Woah, woah, lass!"
                uk "I- arrgh, bloody hell! I’m sorry..."
                scene ch2sc23_09 with dissolve
                el "Apology accepted."
                el "Now, please take a look and see if this is the ring you’re looking for?"
                scene ch2sc23_29 with dissolve
                $ renpy.pause()
                scene ch2sc23_30 with dissolve
                uk "A-Aye! This is it! I-I can’t believe ye found it!"
                scene ch2sc23_11 with dissolve
                mc "Well, believe it."
                scene ch2sc23_12 with dissolve
                uk "Thank ye, lad! I thought I'd lost it fer good."
                scene ch2sc23_09 with dissolve
                el "If you don’t mind us asking, what is the meaning behind it?"
                el "It must be important, seeing how you reacted to losing it."
                scene ch2sc23_12 with dissolve
                uk "Aye, lass. It holds no value te anyone else."
                uk "But te me... it’s everything! Ye see, it belonged te me wife... before..."
                uk "Argh, it's no tale fer a time like this."
                scene ch2sc23_12 with dissolve
                mct "The ring definitely has magical properties."
                mct "Either he doesn’t know about it, or he’s not telling us everything."
                scene ch2sc23_09 with dissolve
                el "Oh... I’m sorry, sir."
                el "I didn’t mean to pry, the ring clearly holds personal value to you."
                scene ch2sc23_31 with dissolve
                uk "Naye! I shan't accept yer apology lass, I’m sorry fer my behavior."
                uk "Ye see, humans often don’t treat my kind well, te say the least."
                scene ch2sc23_32 with dissolve
                el "You mean dwarves?"
                scene ch2sc23_33 with dissolve
                uk "Aye, we’re often treated as second class citizens."
                scene ch2sc23_34 with dissolve
                uk "It don’t matter if we’re wealthy, or even if we're scholars from the royal academy!"
                scene ch2sc23_36 with dissolve
                el "I didn’t know dwarves had it that bad."
                el "I’ve never met a dwarf before, you're the first one."
                scene ch2sc23_37 with dissolve
                mc "I've only met a few, and to be honest..."
                mc "I barely had a conversation with them."
                scene ch2sc23_12 with dissolve
                uk "I suppose I should thank ye properly fer finding this."
                scene ch2sc23_38 with dissolve
                mc "There’s really no need."
                mc "Just remember, not all humans are against you..."
                mc "In fact, you can consider us your friends."
                scene ch2sc23_39 with dissolve
                uk "Arrgh, lad! Ye tryin' t’make me cry here?"
                scene ch2sc23_38 with dissolve
                mc "No, I-"
                scene ch2sc23_40 with dissolve
                with vpunch
                br "Names Borri! Happy te meet ye both!"
                scene ch2sc23_41 with dissolve
                el "Happy to meet you Borri! I’m Eliza! And my friend here-"
                scene ch2sc23_42 with dissolve
                mc "[mc]. Good to meet you, Borri."
                scene ch2sc23_31 with dissolve
                br "Say, where ye headed to?"
                scene ch2sc23_38 with dissolve
                mc "We’re going to the capital, traveling from Riverside."
                scene ch2sc23_43 with dissolve
                el "I can’t wait to see the capital! I hope it’s like my mothers books described it."
                scene ch2sc23_44 with dissolve
                el "I remember how the books described the busy streets, all the different shops, and the grand library!"
                scene ch2sc23_31 with dissolve
                br "Ah, the capital. I’ve been a few times me’self. Grand city."
                scene ch2sc23_33 with dissolve
                br "But be wary of the people... Not everyone is as kind hearted as ye, m’lady."
                scene ch2sc23_45 with dissolve
                el "Oh! *giggles* Aren’t you a charmer!"
                el "I’m not a lady, though."
                el "I'm lowborn, a commoner. So just call me Eliza."
                scene ch2sc23_40 with dissolve
                br "T’me yer a lady, Eliza."
                br "Tis not about yer birth, tis about yer actions."
                br "As a dwarf, I'll never understand humans desire te put value on people just from birth?"
                br "Dwarves, we have te earn our place in the world, and the respect that comes with it."
                br "That's why yer a lady te me lass, yer actions have made it so."
                scene ch2sc23_45 with dissolve
                el "Thank you, Borri."
                scene ch2sc23_38 with dissolve
                mc "Perhaps our paths will cross again someday."
                scene ch2sc23_39 with dissolve
                br "Aye lad! I'll be swinging by the capital every now and then."
                scene ch2sc23_40 with dissolve
                br "The people might be shite, but the ALE! Oooh... the ale!"
                scene ch2sc23_46 with dissolve
                mc "*Chuckles* I guess we’ll look for you whenever there’s ale being served then."
                scene ch2sc23_47 with dissolve
                br "*Chuckle* Ha! Yer a good lad! Take care of ye girl, [mc]."
                br "She’s a good one, I tell ye!"
                scene ch2sc23_48 with dissolve
                el "*Shy* Uh, We’re jus-"
                ###Choice###
                menu:
                    "Agree with Borri.":
                        scene ch2sc23_49 with dissolve
                        $ eliza_trust += 2
                        mc "She's a good one, indeed."
                        mc "I’ll make sure she’s taken good care of."
                        "Slightly surprised by your embrace, Eliza can't help but giggle."
                        "Borri seems to appreciate you being a man, Borri’s trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                        scene ch2sc23_50 with dissolve
                        elt "He's so sweet."
                        scene ch2sc23_51 with dissolve
                        $ renpy.pause(1)
                        el "*Blushes* ..."
                        $ borri_trust += 2
                        scene ch2sc23_52 with dissolve
                        elt "He didn’t correct Borri?! Does that mean-"
                        "Eliza is happy that you didn't correct Borri, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                        scene ch2sc23_53 with dissolve
                        $ renpy.pause(0.7)
                        scene ch2sc23_54 with dissolve
                        $ renpy.pause(0.7)
                        scene ch2sc23_53 with dissolve
                        $ renpy.pause(0.7)
                        scene ch2sc23_54 with dissolve
                        $ renpy.pause(0.7)
                        scene ch2sc23_55 with dissolve
                        elt "Stop it, Eliza! It probably didn’t mean anything."
                        "You release Eliza and you say your goodbyes."
                        scene ch2sc23_56 with dissolve
                        el "Bye-bye Borri! It was nice meeting you! I hope we run into you in Luxenford!"
                        br "Aye! Yer can search for ol'Borri at the taverns, typically 'The Drunken Rooster' is where I stay!"
                        el "The Drunken Rooster, noted!"
                        stop music fadeout 2.0
                        scene black with Dissolve(2)
                        jump ch2sc24

                    "Correct Borri.":
                        scene ch2sc23_57 with dissolve
                        mc "Actually, we’re just friends."
                        scene ch2sc23_56 with dissolve
                        $ borri_trust += 1
                        el "Bye-bye Borri! It was nice meeting you! I hope we run into you in Luxenford!"
                        br "Aye! Yer can search for ol'Borri at the taverns, typically 'The Drunken Rooster' is where I stay!"
                        el "The Drunken Rooster, noted!"
                        "Borri appreciates you returning his trinket, Borri’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                        stop music fadeout 2.0
                        scene black with Dissolve(2)
                        jump ch2sc24

            "Keep the ring and tell the dwarf you found nothing. ({color=#f00}Dark Path{/color})":
                scene ch2sc23_22 with dissolve
                $ dark += 1
                "{color=#f00}Dark morality{/color} has increased by{size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch2sc23_24 with dissolve
                mc "Eliza, I think this is valuable. We should keep it, and possibly sell it when we reach Luxenford."
                scene ch2sc23_36 with dissolve
                el "[mc]! That’s so shameful... But you have a point."
                el "We barely have any coin left, and we’ll need to pay for food and a room at a tavern."
                scene ch2sc23_37 with dissolve
                mc "So you agree?"
                scene ch2sc23_36 with dissolve
                el "Against my better judgment... yes."
                scene ch2sc23_25 with dissolve
                mc "Hey, we looked around the area. Didn’t find anything unusual."
                scene ch2sc23_08 with dissolve
                uk "Arrh ye still here? I told ye t’leave!"
                scene ch2sc23_26 with dissolve
                el "Hey! We’re just trying to help you, okay?"
                scene ch2sc23_46 with dissolve
                mc "Once again, sorry we couldn’t find it."
                scene ch2sc23_33 with dissolve
                uk "Oh, bloody hell. Sorry for yelling at ye, lad. Just in a foul mood t’day."
                scene ch2sc23_45 with dissolve
                el "That’s alright, sir. We understand the frustration of losing something."
                scene ch2sc23_40 with dissolve
                br "Sir? Phfff! Borri."
                scene ch2sc23_38 with dissolve
                mc "[mc]. This is Eliza."
                scene ch2sc23_41 with dissolve
                el "Nice to meet you, Borri!"
                scene ch2sc23_31 with dissolve
                br "Aye. I don’t often meet humans who be willing te help fer nothin' in return."
                scene ch2sc23_51 with dissolve
                elt "Oh heavens! I feel terrible for him. We’re even stealing his trinket."
                scene ch2sc23_32 with dissolve
                el "S-Sorry we couldn’t be of any help, in the end."
                scene ch2sc23_39 with dissolve
                br "Oh, lass. Don’t be blaming ye’self. Anyway, I need te be going."
                scene ch2sc23_42 with dissolve
                mc "Hope to see you under better circumstances, Borri."
                scene ch2sc23_47 with dissolve
                br "Aye, lad! If ye spend time enough at taverns, we'll be sure t’cross paths!"
                scene ch2sc23_45 with dissolve
                el "Bye, Borri! Don’t be a stranger!"
                scene ch2sc23_56 with dissolve
                $ renpy.pause()
                scene ch2sc23_36 with dissolve
                el "[mc], that was terrible! I feel so guilty."
                scene ch2sc23_37 with dissolve
                mc "Hey, it was my idea, so let me carry the guilt. We both know we need the coin."
                scene ch2sc23_09 with dissolve
                el "There have to be other ways we can get coin."
                scene ch2sc23_14 with dissolve
                mc "We’ll figure something out. Don’t worry."
                scene ch2sc23_36 with dissolve
                el "Urrhh. Okay, let’s just go."
                stop music fadeout 2.0
                scene black with Dissolve(2)
                jump ch2sc24

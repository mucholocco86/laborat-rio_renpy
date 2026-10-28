label party1:

    scene black
    with slowfade

    play music my_audio["night ambience2"] loop fadein 2.0
    pause 2.0

    my "Damn, girl, will you chill the fuck out!?"
    my "I said my boy got you! Relax! Got dayum!"
    gia "I keep asking because you keep giving me the same bullshit answer."
    gia "Did you actually talk to him, Myles? Did he personally agree to pay me five hundred dollars?"

    scene a299
    with slowfade

    my "Yes, you're getting paid. How many times I gotta tell you that?"
    my "My boy's good for it. I wouldn't have brought you all the way out here if he wasn't."
    gia "That wasn't my question. Did you speak to him and hear him agree to five hundred?"
    gia "Look me in the eye when you answer, because I can already tell you didn't."
    my "Man, trust me. Once he sees what you brought to the party, five hundred ain't gonna be a problem."

    scene a300
    with medium_dissolve

    my "You making this way bigger than it needs to be. You go inside, do your thing, everybody has a good time, and you get paid."
    my "I needed to bring some real entertainment. I wasn't about to show up here alone looking small-time in front of everybody."
    my "So stop worrying about whether I asked him the right way and let me handle my business."
    my "I know parties ain't really your thing, but I wouldn't have dragged you out here if I thought it was gonna be a waste of your time."
    my "You're acting like I'm about to let somebody play with your money. I said I got it handled."
    my "All this flipping out over nothing is starting to get on my damn nerves."

    scene a302
    with medium_dissolve

    gia "Hold on. Who the fuck do you think you're talking to?"
    gia "I came because you're my cousin and your mother asked me to look out for you. Not because I'm one of your little friends you can order around."
    my "Yo, chill! I'm just saying you doing too much right now."
    gia "No, you chill. You know what'll happen if I lose my temper and hit you, so choose your next words very carefully."

    scene a303
    with medium_dissolve

    my "Okay, damn! I ain't say you were weak, and I ain't trying to disrespect you."
    my "I just wanted the party to look serious, and I knew bringing you would get everybody's attention."
    my "Maybe I should've talked to him first, but we're already here. Just give me a chance to work it out."
    gia "......."
    gia "........."

    scene a304
    with medium_dissolve

    gia "You know what? Forget it. I'm here now, so I'll give you one chance to fix this."
    gia "But if your friend doesn't have my five hundred dollars, I'm walking out, and you can explain to your mother why you wasted my night."
    my "Aight, fuck it. Fine. Just get off my back and let me handle it, damn."

    scene black
    with slowfade
    stop music fadeout 2.0
    stop music2 fadeout 2.0
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    if superevil:
        jump ingroup
    else:
        pass

    pause 2.0
    play music my_audio["apartment4"] loop fadein 2.0

    scene a306
    with medium_dissolve

    voice my_audio["644"]
    nar "You finally leave your room, dressed and more or less ready for the party."
    voice my_audio["645"]
    nar "Strings of coloured lights glow along the hallway, while streamers and decorations cover nearly every free bit of the house."
    voice my_audio["646"]
    nar "The house looks ready. Strangely, it doesn't sound ready. No music, no crowds, and no sign that any guests have arrived."

    scene a307
    with medium_dissolve

    voice my_audio["647"]
    nar "You reach the top of the stairs and look down at the empty entrance hall."
    voice my_audio["648"]
    nar "For the moment, the entire house is quiet."
    voice my_audio["649"]
    nar "Then the doorbell rings."
    play sound my_audio["doorbell"] noloop
    pause 2.0

    scene a308
    with medium_dissolve

    voice my_audio["650"]
    nar "Someone has arrived early, or everyone else has lost track of time."
    voice my_audio["651"]
    nar "Nobody appears to be rushing towards the door, which means the job has apparently fallen to you."
    voice my_audio["652"]
    nar "You start down the stairs to welcome the first guests."

    scene a309
    with medium_dissolve

    voice my_audio["653"]
    nar "Halfway down, you catch sight of two figures waiting behind the glass."
    voice my_audio["654"]
    nar "One is a woman wearing an outfit that leaves little doubt she came prepared for a party."
    voice my_audio["655"]
    nar "Beside her stands a young man whose face seems strangely familiar."

    scene black
    with slowfade

    pause 2.0

label ingroup:

    scene a310
    with medium_dissolve
    play music my_audio["apartment4"]

    voice my_audio["656"]
    nar "By the time you reach the entrance, you are certain you've seen the young man before."
    voice my_audio["657"]
    nar "The memory refuses to come together, but something about him tells you this isn't your first meeting."
    voice my_audio["658"]
    nar "There is only one way to find out. You take hold of the knob and open the door."

    scene black
    with ffade
    play sound my_audio["dooropen"] noloop

    pause 1.5

    scene myleshug
    with ffast_dissolve
    if not persistent.seen_myleshug:


        $ config.allow_skipping = False
        $ renpy.pause(13.3, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_myleshug = True
        $ renpy.save_persistent()
    else:



        pause 13.3

    scene a311
    with medium_dissolve

    my "Yooooo, my boy! What's good!?"
    my "Ain't seen yo ass in a minute, playboy!"

    $ pee11 = "{image=superevil} .........."

    menu:
        "Still breathing, I guess.":




            my "Yeah I see that, nigga!"
            my "The fuck, I ain't know yo ass was gonna be here. How you know them?"
            my "Oooooh, wait. So this is the place you needed to come to?"
            my "Broooo, what the FUCK! That's craaaaazy!"
            my "Man, let's go in! We gotta talk!"
            jump insideparty

        "[pee11]" if superevil:

            my "Hah! Aye bro, you good? What's with the silent treatment?"
            my "You ain't do no xan's did you? I thought we were done with that shit, nigga."
            my "Last time I ever allow us to go for one of Sun's crazy ideas."
            my "Anyway, it's crazy seeing you here. I didn't know you knew Jennifer and the fam! This the place you were going to!?"
            my "Let's go in bitch, we gotta talk!"

            menu:
                "Watch your mouth....":




                    my "........"
                    my "..........."
                    my "Aye bro.....you good? I was just messing with you."
                    my "Ahhhh! I see, you tryna get me. Nice try bitch ass nigga!"
                    my "Anyway, let's go inside bro! We stallin!"
                    jump insideparty
                "Watch your mouth....":


                    my "........"
                    my "..........."
                    my "Aye bro.....you good? I was just messing with you."
                    my "Ahhhh! I see, you tryna get me. Nice try bitch ass nigga!"
                    my "Anyway, let's go inside bro! We stallin!"
                    jump insideparty
                "Watch your mouth....":


                    my "........"
                    my "..........."
                    my "Aye bro.....you good? I was just messing with you."
                    my "Ahhhh! I see, you tryna get me. Nice try bitch ass nigga!"
                    my "Anyway, let's go inside bro! We stallin!"
                    jump insideparty
                "Watch your mouth....":


                    my "........"
                    my "..........."
                    my "Aye bro.....you good? I was just messing with you."
                    my "Ahhhh! I see, you tryna get me. Nice try bitch ass nigga!"
                    my "Anyway, let's go inside bro! We stallin!"
                    jump insideparty
        "Myles? The fuck? What are you doing here?":


            my "Here for the party, nigga!"
            my "I ain't know yo ass was gonna be here though. So this is the place you needed to come to, huh?"
            my "That's craaaaaazy."
            my "Anyway, let's go in bitch. We gotta talk!"
            jump insideparty
        "Wait....Myles?":


            my "Yeah, nigga!"
            my "I ain't know yo ass was gonna be here. So this is the place you needed to come to, huh?"
            my "That's craaaaaazy."
            my "Anyway, let's go in bitch. We gotta talk!"
            jump insideparty


label insideparty:

    $ pee67 = "{image=superevil} *Enough! Show them!*"

    scene black
    with slowfade

    pause 2.0

    scene mylesexcited
    with ffast_dissolve
    if not persistent.seen_mylesexcited:


        $ config.allow_skipping = False
        $ renpy.pause(11, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mylesexcited = True
        $ renpy.save_persistent()
    else:



        pause 11

    if superevil:

        voice my_audio["666"]
        nar "Oh, you've got to be fucking kidding me. Myles has barely finished announcing his plans to drink the house dry when your attention shifts to the woman standing beside him."
        voice my_audio["667"]
        nar "That face. That sharp jaw. That absurdly sculpted body. Princess described the Amazons thoroughly enough for you to recognize one when she is practically standing beneath a spotlight."
        voice my_audio["668"]
        nar "The stranger could not look more obviously Amazon if she arrived barefoot, carrying a spear, and demanding an audience with her queen. The real question is why Myles brought her directly into Mommy's home."
        voice my_audio["669"]
        nar "Let us spare ourselves the pointless introductions and amateur detective work. Ask Myles how he knows this family. His answer should tell us precisely how much he knows... or how badly he intends to lie."

    jump jay2

label jay2:

    menu:

        "So, you mind telling me how you know this family?" if not thought3:

            scene myleswhy
            with ffast_dissolve
            if not persistent.seen_myleswhy:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_myleswhy = True
                $ renpy.save_persistent()
            else:



                pause 14

            $ thought3 = True

            if superevil:

                voice my_audio["670"]
                nar "Oh, come on! 'Why?' What the fuck does he mean, why? That innocent little performance might have been more convincing if he and the mysterious Amazon hadn't immediately exchanged that ridiculous little glance."
                voice my_audio["671"]
                nar "Myles knows precisely why you are asking. He simply believes that acting confused will make you abandon the question before he accidentally reveals something useful."
                voice my_audio["672"]
                nar "More importantly, I am rather curious about the woman. Princess explained how Amazons are taught to feel about Santa, and we now have a perfect opportunity to witness that devotion for ourselves."
                voice my_audio["673"]
                nar "Enough of these pointless questions. Show them your power. Let Myles discover what his old friend has become... and let us see exactly how this Amazon reacts when she realizes who is standing before her."

            menu:

                "You didn't think it was important to tell me that you recognized the address on my father's note?" if not superevil:
                    pass

                "That doesn't explain the look you and her just exchanged. What are you two hiding?" if not superevil:
                    pass

                "[pee67]" if superevil:

                    $ memory_santa_revealed_to_myles_gianna = True
                    $ show_tooltip(n=42)


                    scene mylessantareveal
                    with ffast_dissolve
                    if not persistent.seen_mylessantareveal:


                        $ config.allow_skipping = False
                        $ renpy.pause(26, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_mylessantareveal = True
                        $ renpy.save_persistent()
                    else:



                        pause 26
                    scene black

                    pause 3.0

                    jump outro

            voice my_audio["662"]
            nar "No. Leave it alone for now. Myles answered the question, even if he did so with all the confidence of a man hurriedly burying something beneath the floorboards."
            voice my_audio["663"]
            nar "That glance between him and this woman was brief, but it certainly wasn't meaningless. They both know something about this family that neither of them intends to explain here."
            voice my_audio["664"]
            nar "Push any harder, and all you'll accomplish is teaching them exactly how closely you're watching. People become considerably better liars once they realize they're being investigated."
            voice my_audio["665"]
            nar "Keep your suspicions to yourself, pay attention, and allow them to grow comfortable. Whatever they're hiding will eventually reveal itself... preferably before it becomes your problem."

            jump jay2

        "Who is this woman?" if not superevil:

            scene mylesthatsmycousin
            with ffast_dissolve
            if not persistent.seen_thatsmycousin:


                $ config.allow_skipping = False
                $ renpy.pause(13, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_thatsmycousin = True
                $ renpy.save_persistent()
            else:



                pause 13

            menu:
                "Excuse me? What money?":

                    scene mylesineedtogetpaid
                    with ffast_dissolve
                    if not persistent.seen_mylesineedtogetpaid:


                        $ config.allow_skipping = False
                        $ renpy.pause(12, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_mylesineedtogetpaid = True
                        $ renpy.save_persistent()
                    else:



                        pause 12
                        jump themoney
                "What? What are you talking about? What money?":


                    scene mylesineedtogetpaid
                    with ffast_dissolve
                    if not persistent.seen_mylesineedtogetpaid:


                        $ config.allow_skipping = False
                        $ renpy.pause(12, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_mylesineedtogetpaid = True
                        $ renpy.save_persistent()
                    else:



                        pause 12
                        jump themoney
label themoney:

    $ pe177 = "{image=good} I understand, I wouldn't want you to leave empty-handed after coming all the way here. Take this. *Pay her*."

    $ pe17 = "{image=good} Why would you put me in this position, Myles?"
    $ pe36 = "{image=evil} {image=sexaddict} Hang on, relax. I didn't say I wasn't going to pay you. But what exactly am I getting for my money?"

    menu:

        "I'm sorry but.....I wasn't told I had to pay anyone tonight." if not thought4:

            scene mylessheneedsthe
            with ffast_dissolve
            if not persistent.seen_mylessheneedsthe:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mylessheneedsthe = True
                $ renpy.save_persistent()
            else:



                pause 14
            $ thought4 = True
            jump themoney



        "Why would you put me in this position, Myles?" if not thought5:

            scene myleswhy2
            with ffast_dissolve
            if not persistent.seen_myleswhy2:


                $ config.allow_skipping = False
                $ renpy.pause(13, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_myleswhy2 = True
                $ renpy.save_persistent()
            else:
                pause 13
            $ thought5 = True

            jump themoney


        "[pe36]" if evil or sexaddict:

            scene myleswhatamigetting
            with ffast_dissolve
            if not persistent.seen_myleswhatamigetting:


                $ config.allow_skipping = False
                $ renpy.pause(12, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_myleswhatamigetting = True
                $ renpy.save_persistent()
            else:



                pause 12
            jump jumpset

        "[pe177]" if good:
            if not memory_gianna_paid:
                $ memory_gianna_paid = True
                $ show_tooltip(n=39)


            scene payingiannagood
            with ffast_dissolve
            if not persistent.seen_mylesfuckforfive:


                $ config.allow_skipping = False
                $ renpy.pause(9, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mylesfuckforfive = True
                $ renpy.save_persistent()
            else:



                pause 9

            jump outro



label jumpset:

    menu:

        "Let me be more....specific. Are you gonna fuck me if I pay you the five-hundred?" if not thought1:

            scene mylesfuckforfive
            with ffast_dissolve
            if not persistent.seen_mylesfuckforfive:


                $ config.allow_skipping = False
                $ renpy.pause(13, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mylesfuckforfive = True
                $ renpy.save_persistent()
            else:



                pause 13
            $ thought1 = True
            jump jumpset


        "Listen, honey, baby... If you want my money, you gotta show me a little something." if not thought2:

            scene mylesallurgetting
            with ffast_dissolve
            if not persistent.seen_mylesallurgetting:


                $ config.allow_skipping = False
                $ renpy.pause(23, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mylesallurgetting = True
                $ renpy.save_persistent()
                $ thought2 = True
            else:

                pause 23
            $ thought2 = True
            jump jumpset

        "*Ask your inner thoughts for guidance.*" if thought1 and thought2:

            voice my_audio["659"]
            nar "Hahaha! You ask your inner thoughts for guidance. Oh, we are absolutely paying her. Not merely because she has enormous tits, a magnificent ass, and the sort of body capable of bankrupting better men than you... though none of that hurts."
            voice my_audio["660"]
            nar "No, there is something else about this woman, something strange beneath all that attitude. You cannot explain it yet, but your instincts insist she may know far more than she is letting on."
            voice my_audio["661"]
            nar "Five hundred dollars is a small price to keep such a promising mystery nearby. Pay the woman, enjoy the scenery, and perhaps, if fortune is feeling particularly generous, we may leave tonight with more than one kind of answer."
            stop music

            scene payingiannabad
            with ffast_dissolve
            if not persistent.seen_payingianna1:


                $ config.allow_skipping = False
                $ renpy.pause(33.7, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_payingianna1 = True
                $ renpy.save_persistent()
            else:



                pause 33.7

            scene black
            pause 2.0

            jump theparty
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label jennifer1:


    $ metjennifer = True
    $ deniedjennifer = False
    $ memory_jennifer_followed = True
    $ show_tooltip(n=10)

    stop music fadeout 2.0

    scene black
    with slowfade
    stop narration
    play sound my_audio["dco"] noloop

    pause 3.0

    scene mommy1
    with ffade
    if not persistent.seen_mommy1:


        $ config.allow_skipping = False
        $ renpy.pause(13, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mommy1 = True
        $ renpy.save_persistent()
    else:



        pause 13

    menu:
        "I see...you must be Jennifer. Pleasure to meet you. I'm-":



            pass
        "I assume....Jennifer, right? I'm-":

            pass
        "You have to be Jennifer. A pleasure to meet you. I just met your parents, Marnie and Henry. My name is-":

            pass

    scene mommy2
    with fast_dissolve
    if not persistent.seen_mommy2:


        $ config.allow_skipping = False
        $ renpy.pause(13, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mommy2 = True
        $ renpy.save_persistent()
    else:



        pause 13

label questions3:

    menu:



        "Do Marnie and Henry know I'm a 'very important person'?" if not marniehen3:

            scene mommy3
            with fast_dissolve

            if not persistent.seen_mommy3:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mommy3 = True
                $ renpy.save_persistent()
            else:



                pause 15

            jump firstquest

        "I've noticed you've been smiling at me quite a bit...." if not marniehen4:

            scene mommy7
            with fast_dissolve

            if not persistent.seen_mommy7:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mommy7 = True
                $ renpy.save_persistent()
            else:



                pause 15

            jump secondquest

        "Have you known about me for awhile?" if not marniehen5:

            scene mommy11
            with fast_dissolve

            if not persistent.seen_mommy11:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mommy11 = True
                $ renpy.save_persistent()
            else:



                pause 14

            jump thirdquest
        "I'm sorry but, this is all a bit confusing....":


            scene mommy14
            with fast_dissolve

            if not persistent.seen_mommy14:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mommy14 = True
                $ renpy.save_persistent()
            else:



                pause 14

            jump lastquest

label lastquest:

    menu:
        "Mommy?":



            scene mommy15
            with fast_dissolve

            if not persistent.seen_mommy12:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy12 = True
                $ renpy.save_persistent()
            else:


                pause 15

    menu:
        "Why?":




            scene mommy16
            with ffast_dissolve
            if not persistent.seen_mommy16:

                $ config.allow_skipping = False
                $ renpy.pause(12, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy16 = True
                $ renpy.save_persistent()
            else:


                pause 12
        "I'm sorry, but I'd rather not do that. I'm also confused about why you want me to.":


            scene mommy16
            with ffast_dissolve
            if not persistent.seen_mommy16:

                $ config.allow_skipping = False
                $ renpy.pause(12, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy16 = True
                $ renpy.save_persistent()
            else:


                pause 12
        "You're.....you're serious? You want me to call you 'Mommy'? As in, a sexual thing?":


            scene mommy16
            with ffast_dissolve

            if not persistent.seen_mommy16:

                $ config.allow_skipping = False
                $ renpy.pause(13, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy16 = True
                $ renpy.save_persistent()
            else:


                pause 13

    scene mommy17snap copy

    voice my_audio["82"]
    nar "Well that was certainly informative. You asked a perfectly reasonable question, received a slap hard enough to rearrange your thoughts, and were instructed to call her Mommy."
    voice my_audio["86_1"]
    nar "And why does she keep repeating the word, 'understand'? Is that some sort of catchphrase or something that she uses?"
    voice my_audio["83"]
    nar "This strange little encounter has been fascinating, truly, but your survival instincts would like to suggest that it is now time to get the fuck out of here!"
    voice my_audio["250"]
    nar "This crazy woman is one hundred percent NOT your real mother, and she does NOT have any sort of spell controlling you or your thoughts. So, do us both a favor. Walk away from this crazy big-titted bitch right now."
    jump rrequests


label rrequests3:

    $ pee88 = "{image=superevil} Yes, Mommy."

    menu:
        "[pee88]":



            jump jennifer_mommy17_to_sex
        "[pee88]":

            jump jennifer_mommy17_to_sex
        "[pee88]":

            jump jennifer_mommy17_to_sex
        "[pee88]":

            jump jennifer_mommy17_to_sex




label jennifer_mommy17_to_sex:
    scene mommy17
    with ffast_dissolve
    pause 27.791667

    $ unlock_gallery_scene("mommy")

    scene black
    with slowfade
    pause 2.0
    jump jennifer_sex_scene


label rrequests2:

    menu:
        "Mom....my?":




            voice my_audio["94"]
            nar "No! STOP! You are making a bi-"
            nar "....."
            nar "........."
            voice my_audio["95"]
            nar "Yes.....Yes...! Mommy!"
            voice my_audio["96"]
            nar "We love Mommy. She is everything. She is our world. All that matters, is her."
            voice my_audio["97"]
            nar "This fucking hot BITCH with luscious, beautiful fucking tits is all that matters. Nothing else."
            voice my_audio["98"]
            nar "However, you get the feeling, that there is another. Yes, you can quickly understand that Mommy, does not, work alone."
            voice my_audio["99"]
            nar "We'll deal with that later. All that matters now, is our love for Mommy."
            $ resetallflags()
            $ superevil = True
            $ default_mouse = "superevil"
            $ deniedjennifer = False
            $ memory_jennifer_called_mommy = True
            $ show_tooltip(n=12)

            jump rrequests3
        "I'm not doing that. I won't.":


            scene mommy18
            with ffast_dissolve
            if not persistent.seen_mommy18:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy18 = True
                $ renpy.save_persistent()
            else:


                pause 14

            menu:
                "No, and on that note. I'm out of here. Stay away from me.":



                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer
                "You're fucking nuts, I'm out of here.":

                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer
                "Are you insane!? No way! I am OUT OF HERE! Don't try to follow me, and stay the HELL away from me!":


                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer

        "*Ask your inner thoughts for the best decision.*" if not rde:

            voice my_audio["85"]
            nar "You ask your inner thoughts for guidance. They are relieved to discover that, against all available evidence, you still remember they exist."
            voice my_audio["86"]
            nar "Let us review: this woman watched you from the shadows, knew about you before you introduced yourself, called you important, avoided nearly every direct question, and then demanded that you call her Mommy."
            voice my_audio["87"]
            nar "When you asked why, she answered by slapping you across the face. A remarkably efficient method of discouraging follow-up questions."
            voice my_audio["87_1"]
            nar "And then, to top it all off, the crazy bitch starts saying, 'Understand?'', 'Understand?'', 'Understand?'', 'Understa-....bitch, shut the fuck up!"
            voice my_audio["88"]
            nar "Our recommendation remains unchanged: turn around, use the perfectly functional door behind you, and get the fuck out before Mommy introduces you to the rest of her parenting techniques."

            $ rde = True
            jump rrequests

label rrequests:



    menu:
        "M....Mo....Momm......":




            voice my_audio["89"]
            nar "Whoa, whoa, whoa! NO! Stop that word exactly where it is."
            voice my_audio["90"]
            nar "We are not calling the mysterious woman who just slapped us 'Mommy.' That is not a road we are walking down."
            voice my_audio["91"]
            nar "Listen to me: if you surrender what remains of your judgment, there is a very real chance I will be affected too. I am your mind, remember?"
            voice my_audio["92"]
            nar "Do not do this. We have absolutely no idea where this will take us, and I can assure you, you DON'T want to find out."
            voice my_audio["251"]
            nar "And to be perfectly clear, this is not a spell, and she has no control over you. Calling her that will not give her any. If I change, it will be because your own feelings are changing the way you think. This decision is yours, entirely yours."
            voice my_audio["93"]
            nar "Let's just go back and re-do this, shall we? I warn you, don't be a fool here. An extremely beautiful woman with huge fucking tits is not worth losing yourself over."
            jump rrequests2
        "I'm not doing that. I won't.":


            scene mommy18
            with ffast_dissolve
            if not persistent.seen_mommy18:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy18 = True
                $ renpy.save_persistent()
            else:


                pause 14

            menu:
                "No, and on that note. I'm out of here. Stay away from me.":



                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer
                "You're fucking nuts, I'm out of here.":

                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer
                "Are you insane!? No way! I am OUT OF HERE! Don't try to follow me, and stay the HELL away from me!":


                    scene mommy19
                    with ffast_dissolve
                    if not persistent.seen_mommy19:

                        $ config.allow_skipping = False
                        $ renpy.pause(15, hard=True)
                        $ config.allow_skipping = True

                        $ persistent.seen_mommy19 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14
                    jump goodjennifer
        "*Ask your inner thoughts for the best decision.*" if not rde:

            voice my_audio["85"]
            nar "You ask your inner thoughts for guidance. They are relieved to discover that, against all available evidence, you still remember they exist."
            voice my_audio["86"]
            nar "Let us review: this woman watched you from the shadows, knew about you before you introduced yourself, called you important, avoided nearly every direct question, and then demanded that you call her Mommy."
            voice my_audio["87"]
            nar "When you asked why, she answered by slapping you across the face. A remarkably efficient method of discouraging follow-up questions."
            voice my_audio["87_1"]
            nar "And then, to top it all off, the crazy bitch starts saying, 'Understand?'', 'Understand?'', 'Understand?'', 'Understa-....bitch, shut the fuck up!"
            voice my_audio["88"]
            nar "Our recommendation remains unchanged: turn around, use the perfectly functional door behind you, and get the fuck out before Mommy introduces you to the rest of her parenting techniques."

            $ rde = True
            jump rrequests







label thirdquest:

    menu:
        "You sure do like to talk in riddles, instead of answering basic questions.":




            scene mommy12
            with fast_dissolve

            if not persistent.seen_mommy12:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy12 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "Do you ever answer anything straight? Seems like you do a lot of 'beating around the bush'.":


            scene mommy12
            with fast_dissolve

            if not persistent.seen_mommy12:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy12 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "Can you for once, just give me a straight answer?":


            scene mommy12
            with fast_dissolve

            if not persistent.seen_mommy12:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy12 = True
                $ renpy.save_persistent()
            else:


                pause 15



    menu:
        "Well that's not very fair. You apparently know a ton about me, but I know nothing about you.":




            scene mommy13
            with fast_dissolve

            if not persistent.seen_mommy13:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy13 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen5 = True
            jump questions3
        "That's not fair.":


            scene mommy13
            with fast_dissolve

            if not persistent.seen_mommy13:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy13 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen5 = True
            jump questions3
        "Does that seem fair to you?":


            scene mommy13
            with fast_dissolve

            if not persistent.seen_mommy13:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy13 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen5 = True
            jump questions3

label secondquest:

    menu:
        "What were you expecting?":




            scene mommy8
            with fast_dissolve

            if not persistent.seen_mommy8:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy8 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "Am I not good-looking enough? What exactly were you expecting?":


            scene mommy8
            with fast_dissolve

            if not persistent.seen_mommy8:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy8 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "All right... so how did you expect this to go? What were you expecting?":


            scene mommy8
            with fast_dissolve

            if not persistent.seen_mommy8:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy8 = True
                $ renpy.save_persistent()
            else:


                pause 15



    menu:
        "So... are you upset that I'm not the person you were expecting?":




            scene mommy9
            with fast_dissolve

            if not persistent.seen_mommy9:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy9 = True
                $ renpy.save_persistent()
            else:


                pause 14
        "Does it upset you that someone else showed up instead?":


            scene mommy9
            with fast_dissolve

            if not persistent.seen_mommy9:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy9 = True
                $ renpy.save_persistent()
            else:


                pause 14
        "Be honest....are you upset because you were expecting somebody else?":


            scene mommy9
            with fast_dissolve

            if not persistent.seen_mommy9:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy9 = True
                $ renpy.save_persistent()
            else:


                pause 14



    menu:
        "You know....you could have just said, 'No, I'm not upset,' and that would have been enough. Rather than....sucking my face.":




            scene mommy10
            with fast_dissolve

            if not persistent.seen_mommy10:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy10 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen4 = True
            jump questions3
        "I guess not.":


            $ marniehen4 = True
            jump questions3




label firstquest:

    menu:
        "Okay... but those are your parents. If you know something, shouldn't you tell them?":




            scene mommy4
            with fast_dissolve

            if not persistent.seen_mommy4:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy4 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "If you have important information, shouldn't your parents be the first people you tell?":


            scene mommy4
            with fast_dissolve

            if not persistent.seen_mommy4:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy4 = True
                $ renpy.save_persistent()
            else:


                pause 15
        "Why would you keep a secret from your parents? Tell them.":


            scene mommy4
            with fast_dissolve

            if not persistent.seen_mommy4:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy4 = True
                $ renpy.save_persistent()
            else:


                pause 15



    menu:
        "Wait... why do you call your parents Marnie and Henry instead of Mom and Dad?":




            scene mommy5
            with fast_dissolve

            if not persistent.seen_mommy5:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy5 = True
                $ renpy.save_persistent()
            else:


                pause 14
        "Aren't they your parents? Why do you refer to them by their first names?":


            scene mommy5
            with fast_dissolve

            if not persistent.seen_mommy5:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy5 = True
                $ renpy.save_persistent()
            else:


                pause 14
        "Why would you call your own mother and father Marnie and Henry?":


            scene mommy5
            with fast_dissolve

            if not persistent.seen_mommy5:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy5 = True
                $ renpy.save_persistent()
            else:


                pause 14



    menu:
        "So, you're after a title... and you don't care about anyone else?":




            scene mommy6
            with fast_dissolve

            if not persistent.seen_mommy6:

                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy6 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen3 = True
            jump questions3
        "You'd hurt anyone who gets in your way, as long as you get that title?":


            scene mommy6
            with fast_dissolve

            if not persistent.seen_mommy6:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy6 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen3 = True
            jump questions3
        "Is that title so important to you that everyone else is expendable? That doesn't seem right to me.":


            scene mommy6
            with fast_dissolve

            if not persistent.seen_mommy6:

                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_mommy6 = True
                $ renpy.save_persistent()
            else:


                pause 14
            $ marniehen3 = True
            jump questions3


label goodjennifer:

    $ superevil = False
    $ deniedjennifer = True
    $ memory_jennifer_resisted = True
    $ show_tooltip(n=11)


    scene black
    with slowfade

    pause 2.0

    scene a88
    with slowfade

    voice my_audio["100"]
    nar "Oh, thank God. The door closes behind you, and survival once again feels like a realistic possibility."
    voice my_audio["101"]
    nar "You escaped with your cheek stinging, your dignity limping, and one deeply unsettling invitation to reconsider the entire meaning of the word 'Mommy.' Frankly, it could have gone worse."
    voice my_audio["102"]
    nar "You could tell Marnie and Henry, of course. Then Jennifer denies everything, they ask why you followed her into her bedroom, and this quiet evening becomes a bloody family tribunal with you as the only defendant."
    voice my_audio["103"]
    nar "Your father sent you here for a reason, and starting a household scandal before discovering it would be spectacularly unhelpful. Keep this little nightmare to yourself, find the truth first, and try not to enter any more suspicious bedrooms."

    jump marnie2nd
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

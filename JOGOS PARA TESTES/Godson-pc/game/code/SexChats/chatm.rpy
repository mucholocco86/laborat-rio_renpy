default choicem1 = False
default choicem2 = False
default choicem3 = False
default choicem4 = False
default choicem5 = False
default choicem6 = False
default choicem7 = False
default choicem8 = False
default choicem9 = False
default choicem10 = False
default choicem11 = False
default choicem12 = False

label chatm1:


    menu:



        "How's that feel!?" if not choicem1:

            mon "Fuck! It feels soo good! Ugh!"
            mon "Keep....fucking...me....like....that! Ah~!"
            $ choicem1 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons1

        "This pussy is MINE now! Got it!? I'll make you my horny wife!" if not choicem2:

            mon "Y-Yes! I'm your....slutty big titted wife! Fuck my pussy whenever you want! Ugh~!"
            mon "I want...you....to fill me up! Cum in my pussy and get me pregnant!"
            $ choicem2 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons1

        "Yo Myles! How's this look on cam my guy!?" if not choicem3:

            my "God damn son! You goin' in on that ass!"
            my "This is some good shit bro, keep at it! Dick that bitch down!"
            my "I swear, older bitches really know some shit! She throwin' it BACK!"

            $ choicem3 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons1
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen idle_buttons1


label chatm2:

    menu:



        "You must like getting fucked, huh!?" if not choicem4:

            mon "Shit! Y-Yes! I do! Ugh~!"
            mon "I like your huge cock in my pussy! It feels so good!"
            mon "I want you cock everyday! I can't live without you fucking me!"

            $ choicem4 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons44

        "Shit! I'm gonna cum if this keeps up!" if not choicem5:

            mon "T-That's fine! Ugh~! Cum in my pussy!"
            mon "Fill me up with your thick hot cum! Impregnate me!"
            $ choicem5 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons44

        "Ay Myles! Make sure to get a close up of her tits!" if not choicem6:

            my "I got you bro, don't worry! Them big ass titties look great on cam!"
            my "Just keep giving her that good dick so I can see them bounce!"

            $ choicem6 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons44
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen idle_buttons44

label chatm56:

    menu:



        "Hell yeah! Good shit Kyle! Keep it up!" if not choicem7:

            kyl "........."
            kyl "............."
            kyl ".................."

            $ choicem7 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons56

        "Shit! I'm gonna cum if this keeps up! Film it Kyle!" if not choicem8:

            kyl "........."
            kyl "..............."
            kyl "................."

            $ choicem8 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons56

        "See? THIS is how you FUCK! You watching, Kyle!?" if not choicem9:

            kyl "Well obviously! I have to be watching to film!"
            kyl "..............."
            kyl "Jesus christ...."

            $ choicem9 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons56
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen idle_buttons56

label chatm57:

    menu:



        "How's it look on cam, Kyle!?" if not choicem10:

            kyl "........."
            kyl "............."
            kyl ".................."

            $ choicem10 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons57

        "What do you think, dude!?" if not choicem11:

            kyl "........."
            kyl "..............."
            kyl "................."

            $ choicem11 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons57

        "Kyle! You awake!?" if not choicem12:

            kyl "Yeah! I'm awake! I'm just trying to cold the camera steady!"
            kyl "..............."
            kyl "Holy shit...."

            $ choicem12 = True
            $ chat_hovered = False
            window hide
            call screen idle_buttons57
        "*Go Back.*":

            $ chat_hovered = False
            window hide
            call screen idle_buttons57
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

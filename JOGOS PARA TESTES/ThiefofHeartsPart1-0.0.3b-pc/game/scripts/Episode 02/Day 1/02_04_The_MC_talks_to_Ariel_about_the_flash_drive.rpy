init:
    $ ariel_heart_ep02_flash_drive_chat = False
    $ v_ep02_ariel_hearts_counter = 0

label lb_ep02_02_04_The_MC_talks_to_Ariel_about_the_flash_drive:
    #SCENE BEGINS
    #The scene begins with the MC in the hallway, standing outside Ariel's door
    play music "sound effects/02/Late Night Whispers.mp3" loop fadein 1.0
    scene sc mccheckpendi 001
    with dissolve
    mc"(Maybe I've left this too late.)"
    show sc mccheckpendi 002
    mc"([a_name] is probably fast asleep by now.)"

    show sc mccheckpendi 003
    mc"(Well, I can't wait until the morning.)"
    show sc mccheckpendi 004
    mc"(I could use her computer to check the drive, but I'll have to be very, very quiet.)"

    show sc mccheckpendi 005
    mc"(Or I could see if she's still awake.)"
    mc"(Then again, I wouldn't want to wake her if she's asleep.)"

    #[Let yourself in / Knock first]
    menu:
        "Let yourself in"(wt="Best option"):
            play sound "sound effects/02/door_creaking_open_reduced.mp3" noloop
            show sc mccheckpendi 006
            with dissolve
            pause 1.0
            #The MC carefully opens Ariel's bedroom door and lets himself in - creaking sound effect

            show sc mccheckpendi 007
            with dissolve
            pause 1.0
            #first image, opening the door
            #second image, the MC entering her room, which is dimly lit

            show sc mccheckpendi 008
            with dissolve
            mc"(Woah...)"
            #The MC sees Ariel in her bed, asleep, the covers over her lower half: her glasses sit on her nightstand

            show sc mccheckpendi 009
            mc"(Yep, she's asleep already.)"
            show sc mccheckpendi 010
            mc"(Hopefully I can boot up her computer without waking her.)"

            show sc mccheckpendi 011
            #OPTIONS - click on "Ariel's Computer" or "Ariel in the Bed", or
            #Show Ariel asleep in her bed and her computer, all in the same render - Mistress will code it so the player can click on one or the other


            #If the player clicks on Ariel's Computer
            #Go down to SCENE CONTINUES1

            #If the player clicks on Ariel in the Bed
            show sc mccheckpendi 012
            with dissolve
            pause 1.0
            #the MC stands over Ariel while she sleeps
            mc"(Oh [a_name]...)"
            show sc mccheckpendi 013
            mc"(In another life, you'd be working for the CIA or FBI instead of committing crimes.)"

            #[Go to the computer / Look closer]
            menu:
                "Go to the computer":
                    show sc mccheckpendi 013
                    mc"(I should get back to what I'm here for...)"

                    #Go down to SCENE CONTINUES1

                "Look closer"(wt="Best option"):
                    show sc mccheckpendi 014
                    mc"(She looks so peaceful when she sleeps.)"
                    show sc mccheckpendi 015
                    mc"(And pretty damn cute in what she's wearing.)"
                    $ rewards_unlock ("ariel",7)
                    #show Ariel's body, the bed sheet covers her lower half from her stomach downwards

                    show sc mccheckpendi 016
                    mc"(Hmm... Is she wearing anything down below?)"

                    menu:
                        "Go to the computer":
                            show sc mccheckpendi 013
                            mc"(I should get back to what I'm here for...)"

                            #Go down to SCENE CONTINUES1

                        "Pull the sheet down"(wt="Best option"):
                            show sc mccheckpendi 017
                            with vpunch
                            mc"(Oh shit!)"
                            #The MC pulls the sheet down to her knees

                            show sc mccheckpendi 018
                            mc"(I'd expect this from someone like [b_name] but not sweet, innocent [a_name].)"
                            $ rewards_unlock ("ariel",8)
                            show sc mccheckpendi 013
                            mc"(I should get back to what I'm here for.)"
                            mc"(But I'll pull her bedsheet back up first.)"

                            show sc mccheckpendi 015
                            with dissolve
                            mc"(There, no harm done.)"

                            #Go down to SCENE CONTINUES1


            #SCENE CONTINUES1

            with dissolve
            #The MC sits at Ariel's computer desk while she sleeps in the background

            show sc mccheckpendi 019
            with dissolve
            mc"(Okay... Time to find out what's so special about this thing.)"
            #The MC looks at the flash drive and boots up Ariel's computer
            show sc mccheckpendi 019a
            with dissolve
            pause 1.0
            show sc mccheckpendi 020a
            with dissolve
            pause 2.0
            play sound "sound effects/01/computer_boot.ogg" noloop
            pause 1.0
            show sc mccheckpendi 020
            #a sound effect on the computer is louder than the MC expects
            mc"(What the hell??)"
            show sc mccheckpendi 021
            a"Huh?"
            #Ariel's eyes flutter open

            show sc mccheckpendi 022
            with vpunch
            a"[y_name]??"

            show sc mccheckpendi 023
            a"What are you doing in here?"
            #she sits up on her bed

            show sc mccheckpendi 024
            mc"Oh, sorry, [a_name]."

            show sc mccheckpendi 025
            mc"I wanted to see what was on that flash drive and I didn't want to wake you."

            show sc mccheckpendi 026
            with dissolve
            mc"Sorry, I'll just be a few minutes."
            #the MC turns back to the screen

            show sc mccheckpendi 027a
            #Add these lines if the player selected - PULL THE SHEETS DOWN
            a"(Oh my God! He could have seen me in my underwear.)"
            a"(It's just as well my bedsheet was covering me.)"
            show sc mccheckpendi 028
            with dissolve
            a"(Still, it's pretty embarrassing.)"
            show sc mccheckpendi 029
            a"Just give me a second to put some more clothes on and I'll come and help you."

            show sc mccheckpendi 030
            with dissolve
            a"Besides, you won't be able to access the files on there as they're encrypted."

            show sc mccheckpendi 031
            mc"Oh, no problems. I can wait."

            #we see Ariel changing while the MC stares at the screen as it continues to boot up

            show sc mccheckpendi 032
            with dissolve
            pause 1.0
            #various images of Ariel putting her pants on - shots of her ass bent over, pulling her silk pyjamas shorts on

            show sc mccheckpendi 033
            with dissolve
            pause 1.0
            #these will be frame-by-frame images with no dialogue

            show sc mccheckpendi 033a
            with dissolve
            pause 1.0

            show sc mccheckpendi 034
            with dissolve
            pause 1.0
            #so we need a render of Ariel standing up to the side of her bed, one of her bending over to grab her silk pyjama pants on the floor

            show sc mccheckpendi 035
            with dissolve
            pause 1.0
            #one of her pulling her pants up, and finally one of her pants on - four images in total here

            show sc mccheckpendi 036
            with dissolve
            a"Okay, I'm ready now."
            #She stands by the MC who sits in her chair
            stop music fadeout 1.0
            show sc mccheckpendi 037
            mc"Uh... Maybe you should take this seat. You'll be quicker at this."
            #The MC stands up and offers the seat to her
            show sc mccheckpendi 038
            a"Thanks."

            #She smiles
            #Go down to SCENE CONTINUES2


        "Knock first":
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
            show sc mccheckpendi 039
            with dissolve
            pause 1.0
            #The MC knocks on the door
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3" noloop
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock.)"
            else:
                pause 2.0

            show sc mccheckpendi 040
            a"Who is it?"
            #we don't see Ariel, just the MC talking from outside her room
            show sc mccheckpendi 041
            mc"Hey [a_name]."
            #he talks from outside her door
            mc"It's [y_name]. Can I come in?"
            #reuse the same render as above

            show sc mccheckpendi 042
            a"Oh, sure..."
            #the MC's mouth is closed whenever Ariel speaks to him here

            a"Give me a few seconds to get changed."
            #reuse the same render as above

            show sc mccheckpendi 044
            mc"(Was she not wearing any clothes?)"
            #The MC stands at her door, thinking
            mc"(If I had let myself in, would I have seen her naked??)"
            #MC thinking
            with dissolve
            show sc mccheckpendi 045
            with dissolve
            pause 1.0
            #Ariel opens the door: closed mouth - sound effect
            #Ariel has on some pants/silk shorts, and her glasses on
            play sound "sound effects/01/Door_Opening.mp3" noloop
            show sc mccheckpendi 046
            a"Hi..."
            #Ariel stands at the door, mouth open to speak

            show sc mccheckpendi 047
            mc"(I have to admit, she looks pretty damn cute in what she's wearing.)"
            #The MC looks her up and down

            show sc mccheckpendi 048
            mc"Hey... Sorry to bother you, but I was wondering if I could use your computer?"
            #show Ariel with her mouth closed, listening to the MC

            show sc mccheckpendi 049
            mc"While [mc_vic_address] is out, I was hoping to see what was on this drive."
            #a slightly different expression here

            show sc mccheckpendi 050
            a"Sure, come on in."
            #Ariel opens up her door further and invites the MC in

            show sc mccheckpendi 051
            a"We just have to make sure we keep the noise down."
            #the MC follows Ariel in

            show sc mccheckpendi 052
            with dissolve
            a"I'll keep the lights dimmed so the others don't know what we're doing."
            stop music fadeout 1.0
            #the MC enters her room as she continues to speak. The room is dimly lit.
            #Go down to SCENE CONTINUES2

    #SCENE CONTINUES2
    play music "sound effects/01/Covert Affair.mp3" loop fadein 1.0
    show sc mccheckpendi 053
    with dissolve
    a"Let's see here."
    #The MC and Ariel look at her computer screen - Ariel sits in her computer chair and the MC stands behind her, looking over her. The drive has already been plugged in at the side of her laptop or in the tower (PC)

    #Like this - https://static.wikia.nocookie.net/aceventura/images/b/be/Woodstock.jpg/revision/latest?cb=20131114011838
    show sc mccheckpendi 054
    with dissolve
    pause 1.0
    #show around ten folders on the screen
    with dissolve

    show sc mccheckpendi 055
    with dissolve
    a"Hmm..."
    #Ariel's mouth closed, thinking face

    show sc mccheckpendi 056
    a"It has a few folders on here, [y_name]."
    show sc mccheckpendi 057
    a"What are we looking for anyway?"

    show sc mccheckpendi 058
    mc"I'm not sure yet."
    show sc mccheckpendi 059
    mc"Click on that one that says \"Art Gallery\"."
    pause 1.0
    #The MC points at the screen

    #reuse 054 - but with different image on PC screen
    #Ariel opens up the first folder that she clicks on
    #reuse 054 - but with different image on PC screen
    #It opens up a folder with images of a local art gallery
    show sc mccheckpendi 054a
    with dissolve
    pause 1.0
    show sc mccheckpendi 060
    with dissolve
    mc"Oh my God..."
    #surprised look on the MC's face
    show sc mccheckpendi 061
    a"What is it?"
    #open mouth for Ariel
    show sc mccheckpendi 054b
    with dissolve
    mc"These are images of the art gallery that I checked out with [mc_v_address!c] the other day."
    pause 1.0
    show sc mccheckpendi 054c
    with dissolve
    pause 1.5
    show sc mccheckpendi 063
    with dissolve
    a"Is this the same gallery that [mc_vic_address] is planning for us to hit?"
    #She turns to look top at the MC when she responds here

    show sc mccheckpendi 064
    mc"The very same."
    #the MC is straight-faced, mouth slightly open

    show sc mccheckpendi 065
    mc"And look at this one."
    #The MC points at the screen
    show sc mccheckpendi 054d
    with dissolve
    mc"It's the floor plans."
    mc"It shows all the air vents, exits and even underground passageways into the gallery."
    #reuse the same render as above

    show sc mccheckpendi 066
    with dissolve
    mc"(So that's why he wanted the drive back so badly.)"
    #the MC thinking, mouth closed
    show sc mccheckpendi 063
    a"I wonder what else is on here."
    #reuse the same render as above
    show sc mccheckpendi 067
    mc"Only one way to find out."
    #The MC looks at her, with a slight smile, raises one hand/palm
    play sound "sound effects/02/Door Slam Downstairs - sound effect.mp3" noloop
    stop music fadeout 1.0
    show sc mccheckpendi 068
    #sound effect - a door opening from downstairs alerts the MC and Ariel
    a"{i}(*Whispering*){/i}\nWhat was that?"
    #whispering

    show sc mccheckpendi 069
    with dissolve
    pause 1.0
    #they both turn to look at Ariel's bedroom door, which is slightly open

    show sc mccheckpendi 070
    with dissolve
    mc"{i}(*Whispering*){/i}\nI think it came from downstairs."
    #whispering - MC wary

    show sc mccheckpendi 071a
    mc"{i}(*Whispering*){/i}\nOh shit! It's probably [mc_vic_address]!"
    #whispering - the MC is surprised

    show sc mccheckpendi 072
    mc"{i}(*Whispering*){/i}\nQuick! Turn off your computer and give me the drive."
    #he turns back to Ariel

    show sc mccheckpendi 073
    a"(Oh God, oh God...)"
    #Ariel looks at her screen, panic-look on her face
    pause 1.0
    #the screen is shut down and she hands the drive to the MC

    show sc mccheckpendi 074
    with dissolve
    a"{i}(*Whispering*){/i}\nOkay, what now?"
    #she looks back at him, worried

    show sc mccheckpendi 075
    mc"{i}(*Whispering*){/i}\nWe wait to see if he goes to his room."
    #he responds to her calmly
    play music "sound effects/02/Deadly Roulette.mp3" loop fadein 1.0
    show sc mccheckpendi 076
    with dissolve
    vic"Hic!"
    #Show a drunken Victor at the top of the stairs, passing by Ariel's room
    #His top two buttons on his shirt are undone

    show sc mccheckpendi 077
    vic"(At least tonight wasn't a complete waste.)"
    #show Victor moving slowly past the bedroom doors - the background changes with each step that he makes

    show sc mccheckpendi 078
    vic"(And not just because of the free shots I did with that sexy waitress.)"
    #he doesn't notice Ariel and the MC peering through her door, watching him

    show sc mccheckpendi 079
    vic"(Great... Back to being a boring, unfulfilled husband again.)"
    #he smirks

    show sc mccheckpendi 080
    vic"(Until the next time I go out that is.)"
    #he looks happy

    show sc mccheckpendi 081
    mc"{i}(*Whispering*){/i}\nHe looks wasted."
    #whispering
    #Ariel looks through her slightly open door, the MC stands directly behind her

    show sc mccheckpendi 082
    mc"{i}(*Whispering*){/i}\nAnd his hair looks all messed up."
    #whispering -

    show sc mccheckpendi 083
    a"{i}(*Whispering*){/i}\nDid he get into a bar fight?"
    #whispering - she looks back at the MC who stands right behind her - show both characters in the same shot

    show sc mccheckpendi 084
    mc"{i}(*Whispering*){/i}\nHmm..."
    #whispering - mouth closed, thinking

    mc"{i}(*Whispering*){/i}\nThere's no bruises showing and his clothes aren't ripped or have any marks on them."
    #whispering - reuse the same render as above
    mc"(What did he get up to tonight?)"
    #reuse the same render as above

    show sc mccheckpendi 085
    a"{i}(*Whispering*){/i}\nLooks like he's going straight to bed."
    #whispering
    #Show Victor entering the main bedroom

    show sc mccheckpendi 086a
    mc"{i}(*Whispering*){/i}\nOkay, I better get back to my room."
    #whispering - they face each other now


    #These lines below if this player has LESS than ONE HEART with ARIEL
    if ariel_love_level == 0:
        show sc mccheckpendi 087
        mc"{i}(*Whispering*){/i}\nThanks again for your help."
        #whispering - the MC smiles

        show sc mccheckpendi 088
        a"{i}(*Whispering*){/i}\nAny time, {i}Comedy Crusader{/i}."
        #whispering - Ariel smiles back

        show sc mccheckpendi 086a
        mc"{i}(*Whispering*){/i}\nI'll see you in the morning."
        #whispering - reuse the same render as above

        show sc mccheckpendi 087
        mc"{i}(*Whispering*){/i}\nNight, [a_name]."
        #whispering - reuse the same render as above
        #NO ARIEL HEARTS AWARDED

        show sc mccheckpendi 089
        a"{i}(*Whispering*){/i}\nGoodnight..."
        stop music fadeout 1.0
        #She smiles
        #whispering
        #(screen goes blank)"
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_03_01_The_MC_has_sex_dreams
        #END SCENE

        ################################################################



    #These lines below if this player already has ONE HEART with ARIEL
    if ariel_love_level == 1:
        show sc mccheckpendi 089
        menu:
            "Leave":
                show sc mccheckpendi 087
                mc"Thanks again for your help."
                #whispering - the MC smiles

                show sc mccheckpendi 088
                a"{i}(*Whispering*){/i}\nAny time, {i}Comedy Crusader{/i}."
                #whispering - Ariel smiles back

                show sc mccheckpendi 086a
                mc"{i}(*Whispering*){/i}\nI'll see you in the morning."
                #whispering - reuse the same render as above

                show sc mccheckpendi 087
                mc"{i}(*Whispering*){/i}\nNight, [a_name]."
                #whispering - reuse the same render as above
                #NO ARIEL HEARTS AWARDED

                show sc mccheckpendi 089
                a"{i}(*Whispering*){/i}\nGoodnight..."
                #She smiles
                #whispering
                stop music fadeout 1.0
                #(screen goes blank)"
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep02_03_01_The_MC_has_sex_dreams
                #END SCENE


            "Wait"(wt="Best option"):
                stop music fadeout 1.0
                play music "sound effects/02/Whispered Secrets.mp3" loop fadein 1.0
                show sc mccheckpendi 090
                a"{i}(*Whispering*){/i}\nOr... We could switch my computer back on and see what else is on that drive?"
                #whispering - Ariel tries to persuade the MC to stay
                show sc mccheckpendi 091
                a"(I kind of want him to stay a little longer with me.)"
                #Ariel is concerned, mouth closed, thinking

                show sc mccheckpendi 092
                mc"{i}(*Whispering*){/i}\nNo, it's too risky."
                #whispering - The MC speaks, mouth open, Ariel's mouth is closed
                show sc mccheckpendi 086
                mc"{i}(*Whispering*){/i}\nIf he happens to come to my room, I need to have it with me."
                #whispering - reuse the same render as above
                show sc mccheckpendi 094
                a"{i}(*Whispering*){/i}\nYeah, you're probably right."
                #whispering - reuse the same render as above

                show sc mccheckpendi 093
                #The MC hugs Ariel
                a"(OH!)"
                a"Mmm..."

                show sc mccheckpendi 094
                #They break the hug
                a"{i}(*Whispering*){/i}\nWhat was that for?"

                show sc mccheckpendi 095
                mc"{i}(*Whispering*){/i}\nJust my way of saying thanks."
                #whispering - the MC smiles

                show sc mccheckpendi 088
                a"{i}(*Whispering*){/i}\nAny time, {i}Comedy Crusader{/i}."
                #whispering - Ariel smiles back

                show sc mccheckpendi 096
                mc"{i}(*Whispering*){/i}\nAnd I also wanted to tell you that I adore everything about you.."
                #whispering - the MC smiles

                show sc mccheckpendi 086a
                mc"{i}(*Whispering*){/i}\nYou really helped me out in a big way tonight, and I couldn't have got the drive back without you."
                #whispering - the MC smiles

                show sc mccheckpendi 098
                a"{i}(*Whispering*){/i}\nOh, I don't know what to say."

                show sc mccheckpendi 099
                a"(I know it seems crazy, but I kind of wish he would ki-)"

                show sc mccheckpendi 086a
                mc"{i}(*Whispering*){/i}\nAnyway, I'll see you in the morning."
                #whispering - reuse the same render as above

                show sc mccheckpendi 087
                mc"{i}(*Whispering*){/i}\nGoodnight, [a_name]."
                #whispering - the MC smiles at her
                $ ariel_love_level +=1
                $ v_ep02_ariel_hearts_counter += 1

                show sc mccheckpendi 089
                a"{i}(*Whispering*){/i}\nNight..."
                #She smiles back
                #whispering
                ###ONE ARIEL HEART AWARDED
                $ ariel_heart_ep02_flash_drive_chat = True

                show sc mccheckpendi 105a
                with dissolve
                pause 1.5

                #The MC leaves and closes her door

                show sc mccheckpendi 100
                with dissolve
                a"(Hmm... Perhaps what I was hoping for will happen next time...)"
                #Ariel seems optimistic about what just happened
                stop music fadeout 1.0
                #(screen goes blank)"
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep02_03_01_The_MC_has_sex_dreams
                #END SCENE

        ################################################################

    #These lines below if this player already has TWO HEARTS with ARIEL

    #[Leave / Wait]
    if ariel_love_level >= 2:
        show sc mccheckpendi 089
        menu:
            "Leave":
                show sc mccheckpendi 087
                mc"{i}(*Whispering*){/i}\nThanks again for your help."
                #whispering - the MC smiles

                show sc mccheckpendi 088
                a"{i}(*Whispering*){/i}\nAny time, {i}Comedy Crusader{/i}."
                #whispering - Ariel smiles back

                show sc mccheckpendi 086a
                mc"{i}(*Whispering*){/i}\nI'll see you in the morning."
                #whispering - reuse the same render as above

                show sc mccheckpendi 087
                mc"{i}(*Whispering*){/i}\nNight, [a_name]."
                #whispering - reuse the same render as above

                show sc mccheckpendi 089
                a"{i}(*Whispering*){/i}\nGoodnight..."
                #She smiles
                #whispering
                stop music fadeout 1.0
                #(screen goes blank)"
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep02_03_01_The_MC_has_sex_dreams
                #END SCENE


            "Wait"(wt="Best option"):
                stop music fadeout 1.0
                play music "sound effects/02/Whispered Secrets.mp3" loop fadein 1.0
                show sc mccheckpendi 090
                a"{i}(*Whispering*){/i}\nOr... We could switch my computer back on and see what else is on that drive?"
                #whispering - Ariel tries to persuade the MC to stay
                show sc mccheckpendi 091
                a"(I kind of want him to stay a little longer with me.)"
                #Ariel is concerned, mouth closed, thinking

                show sc mccheckpendi 092
                mc"{i}(*Whispering*){/i}\nNo, it's too risky."
                #whispering - The MC speaks, mouth open, Ariel's mouth is closed
                show sc mccheckpendi 086
                mc"{i}(*Whispering*){/i}\nIf he happens to come to my room, I need to have it with me."
                #whispering - reuse the same render as above
                show sc mccheckpendi 098
                a"Yeah, you're probably right."
                #whispering - reuse the same render as above

                show sc mccheckpendi 093
                a"(OH!)"
                #The MC hugs Ariel
                a"Mmm..."

                show sc mccheckpendi 094
                #They break the hug
                a"{i}(*Whispering*){/i}\nWhat was that for?"
                #they stare at each other while Ariel speaks

                show sc mccheckpendi 095
                mc"{i}(*Whispering*){/i}\nJust my way of saying thanks."
                #whispering - the MC smiles

                show sc mccheckpendi 088
                a"{i}(*Whispering*){/i}\nAny time, {i}Comedy Crusader{/i}."
                #whispering - Ariel smiles back

                show sc mccheckpendi 096
                mc"{i}(*Whispering*){/i}\nI also wanted to tell you that I adore everything about you."
                #whispering - the MC smiles

                show sc mccheckpendi 092
                mc"{i}(*Whispering*){/i}\nYou really helped me out in a big way tonight, and I couldn't have got the drive back without you."
                #whispering - the MC smiles

                show sc mccheckpendi 098
                a"{i}(*Whispering*){/i}\nOh, I don't know what to say."

                show sc mccheckpendi 101
                mc"{i}(*Whispering*){/i}\nI do..."
                #The MC moves in and gives her a closed-mouth kiss on the lips

                show sc mccheckpendi 102
                with dissolve
                pause 1.0
                a"Mmm..."
                #Ariel closes her eyes as they kiss
                show sc mccheckpendi 103
                with dissolve
                pause 1.0
                #Ariel closes her eyes as they kiss

                show sc mccheckpendi 104
                with dissolve
                pause 1.0
                #Their kiss ends and they stare at each other

                show sc mccheckpendi 086a
                with dissolve
                mc"{i}(*Whispering*){/i}\nI guess I'll see you in the morning."
                #whispering - reuse the same render as above
                mc"{i}(*Whispering*){/i}\nGoodnight, [a_name]."
                #whispering - the MC smiles at her

                show sc mccheckpendi 089
                a"{i}(*Whispering*){/i}\nNight, [y_name]."
                #She smiles back and also looks surprised
                #whispering

                show sc mccheckpendi 105a
                with dissolve
                pause 1.5

                #The MC leaves and closes her door

                show sc mccheckpendi 105
                with dissolve
                a"(Oh my God, oh my God!)"
                #Ariel happy with glee

                show sc mccheckpendi 106
                a"(I was hoping he would kiss me, I just can't believe that he actually did!)"

                show sc mccheckpendi 107
                a"(I know he probably shouldn't have, but I don't care about that right now.)"

                show sc mccheckpendi 108
                with dissolve
                a"(Oh wow... My first kiss.)"
                #Ariel lays back on her bed, staring at the ceiling smiling

                show sc mccheckpendi 109
                with dissolve
                a"(I've never felt anything like this before.)"
                #Ariel stares in wonder

                show sc mccheckpendi 110
                with dissolve
                a"(I'm definitely going to sleep well now...)"
                #(screen goes blank)"
                stop music fadeout 1.0
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep02_03_01_The_MC_has_sex_dreams
                #END SCENE


init:
    $ v_ep02_03_11_movie_date_with_ariel_counter = 0
    $ v_ep02_ariel_dates_counter = 0

    screen scr_ep02_03_10_The_MC_returns_home_note:
        zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc mcreturnshome k005"
        #add "black"
        hbox:
            xpos 0.54 ypos 0.431
            text "{alpha=0.8}[vic_name!c]{/alpha}":
                font "Inkfree.ttf"
                color "#000000"
                size 44
                bold False

        hbox:
            xpos 0.60 ypos 0.72
            text "{alpha=0.8}[mc_v_address!c]{/alpha}":
                font "Inkfree.ttf"
                color "#000000"
                size 44
                bold False

label lb_ep02_03_10_The_MC_returns_home_in_the_evening:
    #SCENE BEGINS
    #show the MC entering the front door
    #show that the living room and kitchen lights are dim and that no one is awake
    #show the MC going into the kitchen
    play music "sound effects/01/Whispers of Love1.mp3" loop fadein 1.0
    scene sc mcreturnshome k001
    with dissolve
    pause 1.0
    show sc mcreturnshome k002
    with dissolve
    pause 1.0
    show sc mcreturnshome k003
    with dissolve
    pause 1.0
    show sc mcreturnshome k004
    with dissolve
    mc"What's this?"
    #The MC sees a note on the kitchen counter from Vivian
    #show sc mcreturnshome k005
    show screen scr_ep02_03_10_The_MC_returns_home_note
    with dissolve
    #v"{i}Hi sweetheart.{/i}"
    #v"{i}I've been called into the restaurant to work so I won't be home until late.{/i}"

    #v"{i}There are some leftovers for you to have in the fridge, you just need to heat them up.{/i}"
    #v"{i}[mc_vic_address] is out working again tonight. I'm not sure what time he'll be home.{/i}"

    #v"{i}Talk to you in the morning, love you.{/i}"
    #v"{i}[mc_v_address!c].{/i}"
    $ renpy.pause(10.0, hard=True)
    "..."
    hide screen scr_ep02_03_10_The_MC_returns_home_note
    #show images of the MC opening the fridge and taking the leftovers out of there -
    #https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4wo8g2evTyW0iufuNlvbNXvjyet0Z9-WBbQ&s
    show sc mcreturnshome k006a
    with dissolve
    pause 0.6
    play sound "sound effects/02/Open_Fridge.mp3" noloop
    show sc mcreturnshome k006
    with dissolve
    pause 2.0
    stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #screen goes blank
    centered "A little later on...{w=2.0}{nw}" with dissolve
    show text "A little later on..."
    scene bg black with Dissolve(1)
    pause 1.0
    #This comes up on the screen with a black background

    show sc mcreturnshome k007
    with dissolve
    pause 1.0
    show sc mcreturnshome k008
    with dissolve
    pause 1.0
    #the MC heads upstairs into a darkened hallway. Use these images but darken them - https://pixhost.to/show/182/499224173_sc-girlsrooms-g22.jpg

    #show some light coming out of the bottom of Ariel's bedroom door

    #he sees Bella's lights are off, but sees a light from underneath Ariel's door - https://i.redd.it/sulkf4c70fha1.jpg

    #[Go to bed / Knock on [a_name]'s door]
    show sc mcreturnshome k009
    with dissolve
    pause 1.0
    menu:
        "Go to bed":

            #he MC stretches his arms out, closes his eyes and yawns
            show sc mcreturnshome k010
            with dissolve
            mc"(Time to hit the hay...)"
            #screen goes blank
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
            #the next scene after this would be Scene 04-01 - The MC gets a phone call from Megan

        "Knock on [a_name]'s door"(wt="Best option"):
            $ v_ep02_ariel_dates_counter +=1
            show screen scr_secret_icon("v_secrets_ep02_03_11_1") onlayer ontop
            with { "ontop": dissolve}
            show sc mcreturnshome k011
            with dissolve
            mc"([b_name]'s asleep but it looks like [a_name] could still be awake.)"
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3" noloop
            show sc mcreturnshome k012
            with dissolve
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock)"
            else:
                scene sc mcreturnshome k012
                pause 2.0
            show sc mcreturnshome k013
            with dissolve
            a"Who is it?"
            show sc mcreturnshome k014
            mc"It's [y_name]."
            show sc mcreturnshome k015
            a"Oh..."
            show sc mcreturnshome k016
            a"Okay, I'm coming!"
            pause 2.0
            #door opening sound effect

            #Ariel opens the door and she's wearing a cute little nightie - https://www.daz3d.com/dforce-comfy-homewear-outfit-for-genesis-8-and-81-females

            #https://pixhost.to/show/182/499233840_screenshot-2024-07-29-at-10-43-26-pm.jpg
            #ROLLING SCREEN FOR ARIEL
            play sound "sound effects/01/Door_Opening.mp3" noloop
            #if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            #    scene sc mcreturnshome k017 at tt_top
            #    pause
            #elif True:
            #    scene sc mcreturnshome k018
            show sc mcreturnshome k018
            with dissolve
            a"Hey, you're home!"
            show sc mcreturnshome k019
            mc"Yeah, I finished up a little later at the gym than expected."
            show sc mcreturnshome k020
            show screen scr_secret_hotspot ("sc mcreturnshome k020","1468,420,152,238","v_secrets_ep02_03_11_1")
            mc"I just had some dinner that [mc_v_address!c] left in the fridge for me."
            mc"I was about to go to bed but then I saw your light was still on."
            #[Cute / Hot / Sexy]
            menu:
                "Cute":
                    hide screen scr_secret_hotspot
                    show sc mcreturnshome k021
                    mc"Cute PJs, by the way."
                    show sc mcreturnshome k022
                    a"Oh, this?"
                    #Ariel looks down at what she's wearing
                    show sc mcreturnshome k023
                    a"Yeah, I like it a lot."
                    show sc mcreturnshome k024
                    mc"It suits you."
                    show sc mcreturnshome k025
                    a"Thanks."

                "Hot"(wt="Bonus image"):
                    hide screen scr_secret_hotspot
                    show sc mcreturnshome k026
                    mc"Pretty hot nightwear, by the way."
                    show sc mcreturnshome k022
                    a"Oh, this?"
                    #Ariel looks down at what she's wearing
                    show sc mcreturnshome k027
                    a"Maybe a bit warm, but it's comfortable."
                    show sc mcreturnshome k028
                    mc"No, that's not what I meant."
                    show sc mcreturnshome k029
                    mc"{b}You{/b} look hot wearing it, [a_name]."
                    $ rewards_unlock ("ariel",9)
                    show sc mcreturnshome k030
                    a"Oh!"
                    show sc mcreturnshome k031
                    a"Well... Thanks."
                    show sc mcreturnshome k032
                    a"I never looked at it like that when I bought it."

                "Sexy"(wt="Best option"):
                    hide screen scr_secret_hotspot
                    show sc mcreturnshome k033
                    mc"Pretty sexy nightwear, by the way."
                    show sc mcreturnshome k022
                    a"Really? This?"
                    #Ariel looks down at what she's wearing
                    show sc mcreturnshome k034
                    mc"Yeah... You don't agree?"
                    show sc mcreturnshome k035
                    a"Not really, no."
                    show sc mcreturnshome k036
                    a"The word \"sexy\" never came to mind when I decided to buy it."
                    show sc mcreturnshome k037
                    mc"Well, I think you do."
                    show sc mcreturnshome k025
                    a"Oh, thanks."
                    $ v_ep02_03_11_movie_date_with_ariel_counter += 1

            #scene continues
            show sc mcreturnshome k038
            mc"What are you still doing up?"
            show sc mcreturnshome k039
            a"I couldn't sleep, even after a ten-hour day working at the shop."
            show sc mcreturnshome k040
            a"So I thought I'd work on a few things on my computer and I thought that it would maybe tire me out."
            show sc mcreturnshome k041
            a"But that didn't work."
            show sc mcreturnshome k042
            mc"Well, I'm not overly tired either."
            show sc mcreturnshome k043
            mc"I was thinking of watching a movie or something downstairs, if you'd like to join me?"
            hide screen scr_secret_icon onlayer ontop
            with { "ontop": dissolve}
            show sc mcreturnshome k044
            a"Oh..."
            show sc mcreturnshome k045
            a"But what about everyone else?"
            show sc mcreturnshome k046
            mc"[b_name]'s asleep, [mc_v_address] took a late shift at the restaurant and [mc_vic_address] is out working again."
            show sc mcreturnshome k047
            mc"They both won't be home for another couple of hours."
            show sc mcreturnshome k048
            a"So it's pretty much just us two, then?"
            show sc mcreturnshome k049
            mc"That's right."
            show sc mcreturnshome k050
            a"All right, count me in."
            #+1 ARIEL POINT
            show sc mcreturnshome k051
            a"I'll meet you downstairs. I just have to freshen up."
            #Ariel turns to head back into her room and speaks to him when looking over her shoulder
            show sc mcreturnshome k052
            mc"I'll get the popcorn ready!"
            #Ariel smiles
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep02_03_11_The_MC_watches_a_movie_with_Ariel
            #END SCENE
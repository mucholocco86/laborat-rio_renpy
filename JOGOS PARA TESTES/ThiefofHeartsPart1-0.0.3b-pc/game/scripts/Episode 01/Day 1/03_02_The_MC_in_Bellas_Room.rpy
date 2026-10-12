init:
    default v_ep01_03_02_Turned_TV_Off = False

    image sc bella room television power:
        "sc bellasroom b010" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc bellasroom b011" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc bellasroom b011a" with Dissolve(0.2, alpha=True)

    image sc bella room secret vibrator1:
        "sc bellasroom b039" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc bellasroom b039a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc bella room secret vibrator2:
        "sc bellasroom b040" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc bellasroom b040a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc bella room secret vibrator3:
        "sc bellasroom b041" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc bellasroom b041a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc bella room secret vibrator4:
        "sc bellasroom b042" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc bellasroom b042a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc bella room secret vibrator5:
        "sc bellasroom b044" with Dissolve(0.2, alpha=True)
        pause 1.4
        "sc bellasroom b045" with Dissolve(0.2, alpha=True)

    transform tt_bella_scan:
        xpos 0    ## or anything else slightly outside your screen
        ypos 0
        easein 4 xpos -1600 ypos 0   ## or wherever you want it to end up

    screen scr_ep01_03_02_Bella_Room_Choices:
        default tt = Tooltip("What will you do now?")
        zorder 10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc bellasroom b009"

        imagebutton:
            focus_mask True
            xpos 586
            ypos 83
            hovered tt.Action("Leave")
            idle "images/Episode 01/Day 01/03-Girls Rooms/03-02 Bellas Room/sc bellasroom b009 door idle.png"
            hover "images/Episode 01/Day 01/03-Girls Rooms/03-02 Bellas Room/sc bellasroom b009 door hover.png"
            action [Hide("scr_ep01_03_02_Bella_Room_Choices"),Jump("lb_ep01_03_02_Bella_Room_3")]

        imagebutton:
            focus_mask True
            xpos 995
            ypos 801
            hovered tt.Action("Turn off the television first and then leave" + If(persistent.v_walkthrough_enabled == True,"{color=#33ff33} (Better option){/color}",""))
            idle "images/Episode 01/Day 01/03-Girls Rooms/03-02 Bellas Room/sc bellasroom b009 remote idle.png"
            hover "images/Episode 01/Day 01/03-Girls Rooms/03-02 Bellas Room/sc bellasroom b009 remote hover.png"
            action [Hide("scr_ep01_03_02_Bella_Room_Choices"),Jump("lb_ep01_03_02_Bella_Room_2")]

        frame:
            xfill True
            xalign 0.5
            yalign 0.0
            vbox:
                xalign 0.5
                yalign 0.5
                text tt.value

label lb_ep01_03_02_Bella_Room_1:
    #"If the player clicks on the older sister's door"
    #Bella's Room (Older Sister) needs to be dimly lit even after the TV is turned off, so the player can still see the paintings on the wall"
    scene sc bellasroom b002
    mc"(She's probably still pissed at me. But I hope she's calmed down now and we can have a civilised chat.)"
    #the MC lightly knocks on her door"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    scene sc bellasroom b001
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        scene sc bellasroom b001
        pause 1.0
    scene sc bellasroom b002
    pause 2.0
    stop sound fadeout 1.0
    mc"(Hmm... She's not answering.)"
    mc"(Maybe she's gone to sleep already.)"
    mc"(I'll try one more time.)"
    #the MC lightly knocks on her door again"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc bellasroom b003
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    show sc bellasroom b003
    pause 2.0
    stop sound fadeout 1.0
    mc"(It looks like I might be too late.)"
    #Bella's door cracks open slightly"
    show sc bellasroom b004
    with dissolve
    mc"Huh?"
    mc"(She didn't lock her door.)"
    play ambient "sound effects/01/tv_background.ogg" loop fadein 0.5
    #the MC enters Bella's room"
    play music "sound effects/01/Dreaming in Moonlight1.mp3" loop fadein 1.0
    show sc bellasroom b005
    mc"[b_name]? Are you still awake?"
    #the screen shakes when the MC sees Bella asleep in her sexy underwear lying on her back"
    show sc bellasroom b008
    mc"(Oh shit! She's asleep!)"
    show sc bellasroom b006
    mc"Oh man..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene wip_ep01_bellas_room_01 at tt_side
        pause
    elif True:
        show sc bellasroom b007
    mc"(I know she's my older [b_mc_rel] and we've had our issues lately, but I've always had a huge crush on her.)"
    scene sc bellasroom b009
    mc"(I mean, just look at her... She'd almost be the perfect girl if she didn't have that stick up her ass most of the time!)"
    #the MC sees that she left the TV on, and the player will have an option to \"Leave\" or \"Turn the TV off\"."
    #IMPORTANT: Make it possible to click on the TV remote at the end of the bed, or to exit the room"
    call screen scr_ep01_03_02_Bella_Room_Choices with Dissolve(0.2) onlayer master

label lb_ep01_03_02_Bella_Room_2:
    #"If the player chooses to Turn the TV off"
    #NOTE: The player grabs the remote and turns the TV off. Since the door was open, the house's cat has entered the room without the MC noticing"
    $ v_ep01_03_02_Turned_TV_Off = True
    show sc bellasroom b010
    mc"(I better turn this off.)"
    show sc bella room television power
    $ ui.timer(2.0, Stop("ambient"))
    $ ui.timer(2.0, Play("sound", "sound effects/01/television_off.ogg"))
    $ renpy.pause(3.0, hard=True)
    #the tv is turned off"
    #The MC sees a few of Bella's paintings hanging on the wall"
    show sc bellasroom b012
    mc"(It's hard for me to deny that [b_name] is an incredibly talented artist.)"
    mc"(If she could get out of thieving, I wonder if she would ever consider doing this professionally.)"
    #mc"(If she were ever to get out of thieving game, I wonder if she would consider doing this professionally.)"
    show screen scr_secret_icon("v_secrets_ep01_03_02_1") onlayer ontop
    with { "ontop": dissolve}
    show sc bellasroom b013
    mc"(Bah! I better get out of-)"
    #The MC puts the TV remote on her bedside table. When he's about to leave, he steps on the cat's tail and that makes the cat scream"
    #mc"(Now to carefully back out of-)"
    #show the MC stepping on the cat's tail - the cat screams"
    #screen shakes"
    stop music fadeout 1.0
    show sc bellasroom b014
    pause 0.2
    play sound "sound effects/01/cat_screaming.ogg"
    "EEEEEEAAAAAAAAAAAAAAARRRRRRRRRRRRRREIR!!!" with hpunch
    stop sound fadeout 1.0
    show sc bellasroom b015
    mc"(What the fuck??)"
    #Bella's eyes open"
    show sc bellasroom b016
    b"Huh??"
    show sc bellasroom b017
    #mc"(Shit! I better hide!!)"
    mc"(Shit!)"
    #the MC hides on the floor on the opposite side of the bed to where the cat is - https://us.images.westend61.de/0001755990f/father-and-son-playing-hide-and-seek-in-bedroom-little-boy-hiding-by-the-bed-with-father-searching-him-family-playing-games-inside-their-home-JLPSF26358.jpg"
    show sc bellasroom b018
    show screen scr_secret_hotspot ("sc bellasroom b018","400, 910, 230, 70","v_secrets_ep01_03_02_1")
    b"Oh, it was you. You woke me up!"
    #she turns her bedside table lamp on"
    #The cat jumps onto Bella's bed and she caresses it"
    hide screen scr_secret_hotspot
    show sc bellasroom b019
    b"How did you get in here?"
    show sc bellasroom b020
    b"You sure are a noisy little furball."
    b"Let me pet my little kitty."
    # or b"Little kitty needs some pets?"
    show sc bellasroom b028
    mc"(Ah geez...)"
    #Bella looks around the room and it's empty and silent. She doesn't realise the MC is on the floor below her, hiding"
    show sc bellasroom b021
    b"Hmm..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc bellasroom b022 at tt_bella_scan
        pause 4.0
    elif True:
        show sc bellasroom b022a
        pause 1.0
        show sc bellasroom b022b
        with dissolve
        pause 1.0
        show sc bellasroom b022c
        with dissolve
        pause 1.0
    b"(I guess it was just the cat.)"
    scene sc bellasroom b023
    b"Off you go. Maybe [a_name] is still awake. Go annoy her instead."
    #Bella drops the cat on the floor in front of the MC but she doesn't see him"
    #the cat eyeballs the MC and hisses"
    show sc bellasroom b024
    show screen scr_secret_hotspot ("sc bellasroom b024","1467, 716, 230, 70","v_secrets_ep01_03_02_1")
    pause 0.5
    play sound "sound effects/01/cat_hiss.ogg"
    if persistent.v_sounds_text_on == True:
        "Hisssssssss!"
    else:
        pause 1.4
    hide screen scr_secret_hotspot
    show sc bellasroom b025
    show screen scr_secret_hotspot ("sc bellasroom b025","1467, 716, 230, 70","v_secrets_ep01_03_02_1")
    stop sound fadeout 1.0
    mc"(Well fuck you too!)"
    hide screen scr_secret_hotspot
    #the cat scurries off and out of the room"
    scene sc bellasroom b026
    b"(Weirdo cat.)"
    #Bella turns off her lamp and goes back to sleep, this time lying on her side"
    show sc bellasroom b027
    mc"(I better wait a bit before trying to get out of here.)"
    #screen goes blank
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    scene black
    with dissolve
    pause 1.0
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #scene returns and the MC is still waiting on the floor on the side of Bella's bed"
    show sc bellasroom b028
    with dissolve
    mc"(The coast should be clear now.)"
    show sc bellasroom b029
    mc"(I'm pretty sure she's gone back to sleep.)"
    #the MC stands up and from his view, he can see Bella's ass as she's sleeping on her side away from him"
    show sc bellasroom b030
    mc"(Oh, fuck me...)"
    show sc bellasroom b031
    mc"(If she wasn't out cold, I'd say she was doing this to me on purpose.)"
    mc"(Or this is her way of saying,\"Kiss my ass, [y_name]'\".)"
    show sc bellasroom b032
    mc"(Hmm... Now there's a thought.)"
    if persistent.v_secrets_enabled and persistent.v_secrets_ep01_03_02_1:
        label lb_ep01_03_02_Bella_Room_1_fantasy_scene:
            if not _in_replay:
                scene img_secret_scene_overlay onlayer anim_layer
                with { "anim_layer": dissolve}
            else:
                show screen scr_end_replay
            stop music fadeout 2.0
            play music "sound effects/01/Dreaming in Moonlight2.mp3" loop fadein 1.0
            show sc bellasroom b032
            mc"(Actually... I think I spotted her little friend under the bed.)"
            show sc bellasroom b036
            mc"(This might be a good chance for me to get her back for always being such a bitch to me.)"
            show sc bellasroom b037
            mc"(All right little guy. I'll put you on the lowest setting. Less chance of waking her.)"
            play sex1 "sound effects/01/sex/Buzzing_noise_Sound_FX.ogg" loop fadein 0.5
            pause 1.0
            mc"(Perfect...)"
            show sc bellasroom b038
            play sex2 "sound effects/01/sex/bella_moan_slow.ogg" loop fadein 0.5
            b"{i}(*Whispering*){/i}\nMmm..."
            mc"(It sounds like she can definitely feel it, but not enough to wake her up.)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc bella room secret vibrator1
            else:
                show sc bellasroom b039
            b"{i}(*Whispering*){/i}\nMmm, yes right there..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc bella room secret vibrator2
            else:
                show sc bellasroom b040
            mc"(That's it [b_name], I want you to have to wash your sheets after this.)"
            b"{i}(*Whispering*){/i}\nOh god, I love it when you lick my pussy."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc bella room secret vibrator3
            else:
                show sc bellasroom b041
            mc"(She's no doubt dreaming of someone going down on her.)"
            stop sex2 fadeout 1.0
            play sex3 "sound effects/01/sex/bella_moan_fast.ogg" loop fadein 0.5
            b"{i}(*Whispering*){/i}\nMmm... don't stop."
            b"{i}(*Whispering*){/i}\nOh god yes, make me cum [y_name]..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc bella room secret vibrator4
                with vpunch
            else:
                show sc bellasroom b042
                with vpunch
            mc"(WAIT WHAT!?)"
            b"{i}(*Whispering*){/i}\nOh yes, fuck me with that big cock, [y_name]. I'm so close..."
            mc"(HOLY SHIT!)"
            mc"(Surely she must be talking about another [y_name] that she knows... Right?)"
            show sc bellasroom b043
            b"{i}(*Whispering*){/i}\nOhh..."
            stop sex3 fadeout 1.0
            play sex2 "sound effects/01/sex/female_orgasm.mp3"
            show sc bellasroom b043a
            b"{i}(*Whispering*){/i}\nOHHHHH [y_name!u]!!!!!!" with vpunch
            b"{i}(*Whispering*){/i}\nNGHH!" with vpunch
            stop sex1 fadeout 1.0
            b"{i}(*Whispering*){/i}\nOhhh yeah, you know just how to fuck me just right..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc bella room secret vibrator5
                mc"(Holy shit, look how wet she got. And she was dreaming about me fucking her!)"
            else:
                show sc bellasroom b044
                mc"(Holy shit, look how wet she got.)"
                show sc bellasroom b045
                mc"(And she was dreaming about me fucking her!)"
            mc"(I can't know for sure, but it was incredibly arousing to hear her call out my name before, during and after her climax!)"
            mc"(It looks like I'm not the only one with a dirty, perverse mind, [b_name].)"
            scene onlayer anim_layer
            with { "anim_layer": dissolve}
            show sc bellasroom b033
            mc"(Well, best not to hang around any longer. I've had my fun. Better go before she wakes up again.)"
            #the MC starts walking out of the room"
            show sc bellasroom b034
            $ v_ep01_bella_fantasy_counter += 1
            $ persistent.replay_bella_fantasy = False
            $ renpy.end_replay()
    else:
        show sc bellasroom b033
        mc"(I better go before someone sees me in here.)"
        #the MC starts walking out of the room"
        show sc bellasroom b034
    mc"(I'll try and talk with [b_name] in the morning before she goes to work...)"
    stop music fadeout 1.0
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)

    jump lb_ep01_girls_rooms_01

label lb_ep01_03_02_Bella_Room_3:
    mc"(I better go before someone sees me in here.)"
    show sc bellasroom b035
    #the MC starts walking out of the room"
    mc"(I'll try and talk with [b_name] in the morning before she goes to work...)"
    stop music fadeout 1.0
    #screen goes blank"
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_girls_rooms_01

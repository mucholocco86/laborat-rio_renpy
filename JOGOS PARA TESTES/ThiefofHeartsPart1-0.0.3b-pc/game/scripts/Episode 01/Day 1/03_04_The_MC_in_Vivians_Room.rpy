init:
    $ v_ep01_03_04_Vivians_Room_Entered = False
    $ v_ep01_03_04_Vivians_Room_Remained = False
    $ v_ep01_vivian_respect_counter = 0
    $ v_ep01_vivian_cocky_counter = 0
    $ v_ep01_vivian_arrogant_counter = 0

    image sc viviansroom shower1:
        "sc viviansroom v10[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower1x:
        "sc viviansroom v10x[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower2:
        "sc viviansroom v11[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower3:
        "sc viviansroom v29[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower4:
        "sc viviansroom v32[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower5:
        "sc viviansroom v33[renpy.random.choice(['a', 'b', 'c'])]x"
        pause 0.1
        repeat

    image sc viviansroom shower6:
        "sc viviansroom v41[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower7:
        "sc viviansroom v45[renpy.random.choice(['a', 'b', 'c'])]x"
        pause 0.1
        repeat

    image sc viviansroom shower8:
        "sc viviansroom v46[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom shower9:
        "sc viviansroom v50[renpy.random.choice(['a', 'b', 'c'])]"
        pause 0.1
        repeat

    image sc viviansroom breast fondle:
        "sc viviansroom v33" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc viviansroom v33a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc viviansroom v33b" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc viviansroom mc drop pants:
        "sc viviansroom v37" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v37a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v38" with Dissolve(0.2, alpha=True)

    image sc viviansroom mc stroke1:
        "sc viviansroom v38" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v38a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc viviansroom mc stroke2:
        "sc viviansroom v61" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc viviansroom v61a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc viviansroom mc stroke3:
        "sc viviansroom v38" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc viviansroom v38a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc viviansroom mc stroke3 and stop:
        "sc viviansroom v38" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc viviansroom v38a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc viviansroom v38" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc viviansroom v38a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v37a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v37" with Dissolve(0.2, alpha=True)

    image sc viviansroom breast glass:
        "sc viviansroom v39" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc viviansroom v40" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat

    image sc viviansroom sponge rub1:
        "sc viviansroom v43" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc viviansroom v43a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc viviansroom sponge rub2:
        "sc viviansroom v44" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc viviansroom v44a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc viviansroom sponge rub3:
        "sc viviansroom v45" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc viviansroom v45a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc viviansroom vivian turn:
        "sc viviansroom v52" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v53" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc viviansroom v54" with Dissolve(0.2, alpha=True)
        pause 1.0

label lb_ep01_vivians_room_3:
    #Vivian's Room
    show screen scr_secret_icon("v_secrets_ep01_03_04_1") onlayer ontop
    with { "ontop": dissolve}
    scene sc viviansroom v02
    mc"(While [mc_vic_address] is occupied downstairs, I can check on [mc_v_address] to see if she's okay.)"
    #the MC knocks on her door"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc viviansroom v01
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        show sc viviansroom v01
        pause 2.5
    show sc viviansroom v02
    pause 2.0
    stop sound fadeout 1.0
    mc"(She's not answering.)"
    mc"(I'm sure she won't mind if I let myself in.)"
    #The MC turns the handle and enters the room but finds no one inside. The TV is on"
    #door opening sound effect
    $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
    play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 0.3
    play sound "sound effects/01/Door_Opening.mp3"
    show sc viviansroom v03
    show screen scr_secret_hotspot ("sc viviansroom v03","1150, 740, 260, 80","v_secrets_ep01_03_04_1")
    mc"(Hmm... She's not here.)"
    mc"(But I didn't see her come out of the room.)"
    stop sound fadeout 1.0
    hide screen scr_secret_hotspot
    #the MC turns and can see the lights on in the bathroom"
    $ renpy.music.set_volume(0.3, 0.3, channel="ambient")
    show sc viviansroom v04
    mc"(Oh, she must be in there.)"
    # Note - the player can see both the exit out of the main bedroom or the door to the bathroom here"
    #IMPORTANT: Make it possible to click on either the ROOM EXIT or the BATHROOM DOOR"
    menu:
        "Leave":
            #If the player chooses the ROOM EXIT"
            show sc viviansroom v04
            mc"(Hmm... After what happened, perhaps it would be best if I don't disturb her.)"
            show sc viviansroom v09
            mc"(She might freak out, and I can imagine how she'd react if she knew I was here.)"
            $ v_ep01_vivian_respect_counter += 1
            mc"(I'll try and speak with her tomorrow...)"
            #screen goes blank
            stop ambient fadeout 1.0
            hide screen scr_secret_icon onlayer ontop
            with { "ontop": dissolve}
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_girls_rooms_01
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        "Stay"(wt="Best option"):
            #"If the player chooses the BATHROOM DOOR"
            hide screen scr_secret_icon onlayer ontop
            with { "ontop": dissolve}
            show sc viviansroom v04
            mc"(I could leave, but I might not be able to sleep without knowing for sure that she's okay.)"
            $ v_ep01_03_04_Vivians_Room_Entered = True
            $ rewards_unlock ("vivian",1)
            #the MC lightly knocks on her door"
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
            show sc viviansroom v05
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock)"
                pause 1.0
            else:
                show sc viviansroom v05
                pause 2.0
            stop sound fadeout 1.0
            show sc viviansroom v09
            #with fast_dissolve
            v"Only open that door if you're ready to treat me better and not make me feel horrible about myself."
            v"Otherwise, go back downstairs, [vic_name] and leave me alone."
            show sc viviansroom v04
            mc"(Ah geez... [mc_vic_address] really upset her this time.)"
            mc"(It sounds like all that [mc_v_address] needs is a friendly ear and someone to vent to.)"
            mc"(Fuck it! I'm going in...)"
            play sound "sound effects/01/Door_Opening.mp3"
            show sc viviansroom v09
            pause 0.3
            show sc viviansroom v07
            with dissolve
            pause 0.5
            #door opening sound effect
            #the MC opens the bathroom door, and he sees that Vivian is totally naked"
            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
            play music "sound effects/01/Whisper in the Dark1.mp3" loop fadein 2.0
            show sc viviansroom v06
            with dissolve
            mc"(Holy shit...)"
            #Vivian's back is facing the MC so she can't see him, and the player can only see her ass"
            #shower sound effect
            stop sound fadeout 1.0
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                #rolling screen of Vivian from the floor up to her head"
                show sc viviansroom shower1x onlayer anim_layer at tt_top
                scene wip_ep01_vivian_room_01 at tt_top
                pause
            elif True:
                if persistent.v_anim_enabled:
                    scene sc viviansroom shower1 onlayer anim_layer
                else:
                    scene sc viviansroom v10a onlayer anim_layer
                show sc viviansroom v10
            v"So are you just going to stand there? Or does my naked body repulse you to the point that you don't know what to say to me anymore, [vic_name]?"
            scene onlayer anim_layer
            scene sc viviansroom v07
            mc"(Oh [mc_v_address!c]... You have no idea just how gorgeous you are.)"
            if persistent.v_anim_enabled:
                scene sc viviansroom shower2 onlayer anim_layer
            else:
                scene sc viviansroom v11a onlayer anim_layer
            show sc viviansroom v13
            mc"(You'd give a dog a bone!)"
            show sc viviansroom v11
            v"(Sigh...)"
            show sc viviansroom v12
            v"I can't even bring myself to look at you. If you're not going to say anything then just leave."
            if persistent.v_secrets_enabled and persistent.v_secrets_ep01_03_04_1:
                label lb_ep01_vivians_room_fantasy_shower:
                    if not _in_replay:
                        scene img_secret_scene_overlay onlayer anim_layer_2
                        with { "anim_layer_2": dissolve}
                    else:
                        show screen scr_end_replay
                    show sc viviansroom v11
                    mc"(All the voices in my head are yelling at me to stay, and for once I think I'll listen.)"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v10a onlayer anim_layer
                    show sc viviansroom v23
                    mc"(I know this is wrong, but how could anyone resist such a beauty.)"
                    mc"(And [vic_name] never shows her just how wonderful she really is.)"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower2 onlayer anim_layer
                    else:
                        scene sc viviansroom v11a onlayer anim_layer
                    show sc viviansroom v24
                    v"(It feels like he's still there, but I'm not sure why he's not saying anything.)"
                    show sc viviansroom v25
                    v"(Although, it's pretty exciting to think [vic_name] is watching me right now and being quite coy about it.)"
                    show sc viviansroom v26
                    v"(Maybe I should give him a little show. Remind him of what he's been missing.)"
                    # We start to see Vivian get lathered up with soap.
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v10a onlayer anim_layer
                    show sc viviansroom v27
                    mc"(Oh wow [mc_v_address], you are really stunning.)"
                    # Vivian starts soaping up her ass
                    show sc viviansroom v28
                    mc"(Holy shit! Is she getting turned on by my presence, even though she thinks I'm [vic_name]?)"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v29a onlayer anim_layer
                    show sc viviansroom v29
                    v"(Let's see if I can tease him with my breasts without letting on that I know he's watching me.)"
                    # We start to see Vivian turn around, her hand covering her chest but her head still hidden.
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v10a onlayer anim_layer
                    show sc viviansroom v30
                    mc"(Oh shit, she's turning around!)"
                    # She completes the turn but her eyes are closed
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower2 onlayer anim_layer
                    else:
                        scene sc viviansroom v11a onlayer anim_layer
                    show sc viviansroom v31
                    mc"(I need to g-)"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v32a onlayer anim_layer
                    show sc viviansroom v32
                    mc"(Wait, she's keeping her eyes closed on purpose. But why?)"
                    # She is rubbing the soap all over her breasts
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v33ax onlayer anim_layer
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        show sc viviansroom breast fondle
                    else:
                        show sc viviansroom v33
                    v"(Lets get these big breasts all soapy and wet.)"
                    #cuts to of the MC putting a hand on his crotch, it clearly having a large bulge
                    scene onlayer anim_layer
                    show sc viviansroom v34
                    mc"(By the beard of Zeus, I'm about to burst!)"
                    # Cut's back to Vivian, holding her breasts from underneith, this time very close to the glass
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v33ax onlayer anim_layer
                    scene sc viviansroom v35
                    v"Oh my... My boobs are so heavy, but oh so firm..."
                    v"I want them silky smooth so they are perfect for sliding a {b}BIG{/b} hard cock between them."
                    #She presses her soaped up breasts against the glass
                    v"But I think I need to let them rest and recover for a bit from all this fondling."
                    show sc viviansroom v36
                    mc"(Fuck me!)"
                    scene onlayer anim_layer
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        show sc viviansroom mc drop pants
                    else:
                        show sc viviansroom v37a
                    mc"(That's it, I can't resist any longer.)"
                    # We see the MC pull out his cock and start to stroke it as he's watching her
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        show sc viviansroom mc stroke1
                    else:
                        show sc viviansroom v38a
                    mc"(Please forgive me [mc_v_address] for what you're making me do.)"
                    # She continues to rub her breasts all over the glass while keeping her eyes closed.
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v33ax onlayer anim_layer
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        show sc viviansroom breast glass
                    else:
                        show sc viviansroom v39
                    play sex1 "sound effects/01/sex/breast_glass.ogg" loop
                    v"Mmm... Having my big tits pressed against this glass feels so good."
                    v"(Oh my, all this dirty talk is causing my heart to beat like crazy!)"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v41a onlayer anim_layer
                    show sc viviansroom v41
                    stop sex1 fadeout 1.0
                    v"(Knowing that he's still watching me is also making me so wet, and not just from the hot shower.)"
                    # She reaches down between her legs and starts to rub up and down. (making sure the player cant see much)
                    v"Oh, but I can't forget about my tight, wet pussy now can I?"
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v45ax onlayer anim_layer
                    show sc viviansroom v42
                    v"I better rub it thoroughly to get it nice and clean."
                    play sex1 "sound effects/01/sex/woman_moaning_sound_effect.ogg" loop
                    if persistent.v_anim_enabled:
                        scene sc viviansroom shower1 onlayer anim_layer
                    else:
                        scene sc viviansroom v33ax onlayer anim_layer
                    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                        show sc viviansroom sponge rub1
                    else:
                        show sc viviansroom v43
                    mc"(NGHH! Fuck!)"
                    # cuts to a shot of Vivans crotch from the side as she rubs it up and down, all while you can see the MC cranking in the distance.
                    v"Oh yes, that feels soooo good."
                    v"Mmm... yes. Get my sensitive clit all nice and clean."
                    mc"(Geezus [mc_v_address], you're making me want to strip my clothes off and join you in there!)"
                    menu:
                        "Play it safe and leave":
                            scene onlayer anim_layer
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom mc stroke3 and stop
                                mc"(Dammit, I'm gonna explode. I better go before I do so, or before she realizes it's me who's been watching her.)"
                            else:
                                show sc viviansroom v37a
                                mc"(Dammit, I'm gonna explode.)"
                                show sc viviansroom v37
                                mc"(I better go before I do so, or before she realizes it's me who's been watching her.)"
                            # the MC Looks down at his cock, no longer doing it
                            show sc viviansroom v60
                            mc"(No doubt about it buddy... Tonight we're going to knock one out after what we've just witnessed.)"
                            $ v_ep01_vivian_arrogant_counter += 1
                            stop sex1 fadeout 1.0
                            # A shot of the MC leaving the bathroom, pants with a massive bulge
                            #screen goes blank"
                        "Keep risking it"(wt="Best option"):
                            $ v_ep01_03_04_Vivians_Room_Remained = True
                            mc"(Oh fuck yes [mc_v_address!c], you are simply incredible!)"
                            # Vivian turns back around, butt just resting against the glass.
                            stop music fadeout 2.0
                            play music2 "sound effects/01/Whisper in the Dark2.mp3" loop fadein 1.0
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom sponge rub2
                                with dissolve
                            else:
                                show sc viviansroom v44
                            v"Oh god, I wish I had someone's {b}big{/b} cock deep inside of me right now."
                            # the MC Looks down at his cock, pumping it even faster now
                            scene onlayer anim_layer
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom mc stroke2
                            else:
                                show sc viviansroom v61
                            mc"(Oh geez! No doubt about it buddy... Tonight we're going to knock one out after what we're witnessing.)"
                            $ v_ep01_vivian_cocky_counter += 1
                            mc"(That is, if I don't explode first!)"
                            if persistent.v_anim_enabled:
                                scene sc viviansroom shower1 onlayer anim_layer
                            else:
                                scene sc viviansroom v45ax onlayer anim_layer
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom sponge rub3
                            else:
                                show sc viviansroom v45
                            v"(Hmm, still nothing from [vic_name]. Let's see if this will loosen his tongue.)"
                            # Cuts to the MC still jacking it really fast.
                            scene onlayer anim_layer
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom mc stroke3
                            else:
                                show sc viviansroom v38
                            mc"(Dammit, I'm gonna explode. I better go before I do so, or before she-)"
                            stop sex1 fadeout 1.0
                            play sound "sound effects/01/sponge sounds.ogg"
                            # We hear the sound of something hitting the floor.
                            if persistent.v_sounds_text_on == True:
                                "(SPLOSH!)" with vpunch
                            else:
                                show sc viviansroom v38
                                with vpunch
                                pause 1.0
                            # Vivian pretends to drop the loufa
                            if persistent.v_anim_enabled:
                                scene sc viviansroom shower1 onlayer anim_layer
                            else:
                                scene sc viviansroom v46a onlayer anim_layer
                            stop sound fadeout 1.0
                            show sc viviansroom v46
                            v"Oopsie! I dropped my sponge. I better pick it up..."
                            # Vivian bends over to pick it up, in the process, pressing her butt against the glass, pussy in full view of the MC but not the player
                            if persistent.v_anim_enabled:
                                scene sc viviansroom shower1 onlayer anim_layer
                            else:
                                scene sc viviansroom v33ax onlayer anim_layer
                            show sc viviansroom v47
                            mc"(HOLY SH-){w=1.5}{nw}"
                            show sc viviansroom v47a
                            with hpunch
                            mc"(OH FUCK!){w=1.5}{nw}"
                            if persistent.v_anim_enabled:
                                scene sc viviansroom shower1 onlayer anim_layer
                            else:
                                scene sc viviansroom v45ax onlayer anim_layer
                            show sc viviansroom v48
                            with hpunch
                            mc"(NGH!){w=1.5}{nw}"
                            scene onlayer anim_layer
                            show sc viviansroom v49
                            with hpunch
                            mc"(UNGHH!)"
                            if persistent.v_anim_enabled:
                                scene sc viviansroom shower1 onlayer anim_layer
                            else:
                                scene sc viviansroom v50a onlayer anim_layer
                            show sc viviansroom v50
                            mc"(Shit, it's everywhere! How am I going to clean that up without her spotting me?)"
                            mc"(I better do it before I-)"
                            scene onlayer anim_layer
                            with dissolve
                            stop ambient fadeout 1.0
                            play sound "sound effects/01/turn_shower_off.ogg"
                            pause 1.0
                            # We hear the water being turned off.
                            show sc viviansroom v51
                            mc"(FUCK! There's no time!)"
                            show sc viviansroom v52
                            mc"(I better get out of here!)"
                            stop sound fadeout 1.0
                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                show sc viviansroom vivian turn
                                v"I hope you enjoyed the sh-"

                            else:
                                show sc viviansroom v53
                                v"I hope you enjoyed the sh-"
                                show sc viviansroom v54
                                v"I hope you enjoyed the sh-"
                            # We see Vivian look at the doorway to see nobody there and she gets a disapointed look on her face.
                            show sc viviansroom v55
                            v"Oh..."
                            # She then looks down at the glass and notices somethign white on it
                            show sc viviansroom v56
                            v"(Where did [vic_name] go?)"
                            v"(Wait... Is that...?)"
                            # She realized what it is and gets a really happy look on her face
                            show sc viviansroom v57
                            v"(Oh my, [vic_name]... You really enjoyed the show didn't you? I'm glad to see that I can still excite you this much.)"
                            v"(But why did he leave?)"
                            # We get a mischeivous look on her face
                            v"(You know, its been so long...)"
                            # She reaches a finger over and wipes some of it up on her finger
                            show sc viviansroom v58
                            v"(I've almost forgotten what he tastes like.)"
                            # and proceds to suck on her finger.
                            show sc viviansroom v59
                            v"Mmm..."
                            v"(He tastes even better than I remember...)"
                            #screen goes blank"
                            $ v_ep01_vivian_fantasy_counter += 1
                            $ persistent.replay_vivian_fantasy_bathroom = False
            else:
                if persistent.v_anim_enabled:
                    scene sc viviansroom shower1 onlayer anim_layer
                else:
                    scene sc viviansroom v50a onlayer anim_layer
                show sc viviansroom v23
                mc"(All the voices in my head are yelling at me to stay, but I can't.)"
                mc"(Why embarrass both of us? She's been through enough tonight as it is.)"
                scene onlayer anim_layer
                show sc viviansroom v08
                mc"(I'll try and speak with her tomorrow.)"
                #show a final shot of Vivian's ass before the MC leaves the room
                if persistent.v_anim_enabled:
                    scene sc viviansroom shower1 onlayer anim_layer
                else:
                    scene sc viviansroom v50a onlayer anim_layer
                show sc viviansroom v13
                mc"(To be continued...)"
            #screen goes blank"
            stop music fadeout 2.0
            stop music2 fadeout 1.0
            stop ambient fadeout 1.0
            scene onlayer anim_layer
            scene onlayer anim_layer_2
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ renpy.end_replay()
            centered "A few minutes later...{w=2.0}{nw}" with dissolve
            show text "A few minutes later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
            scene bg black with Dissolve(1)
            pause 1.0
            #Vivian exits the bedroom and finds Victor sitting on the bed, taking his socks off"
            if persistent.v_secrets_enabled and persistent.v_secrets_ep01_03_04_1:
                scene img_secret_scene_overlay onlayer anim_layer_2
                with { "anim_layer_2": dissolve}
                show sc viviansroom v17
                with dissolve
                v"Oh... There you are."
                show sc viviansroom v15
                vic"Yeah, where the hell else would I be?"
                show sc viviansroom v17
                if v_ep01_03_04_Vivians_Room_Remained == True:
                    v"And {i}now{/i} you want to talk after you already finished."
                    v"(Why is he giving me the cold shoulder after everything that just happened?)"
                else:
                    v"And {i}now{/i} you're talking to me. Great..."
                    v"(Why'd he up and leave and is suddenly giving me the cold shoulder? Was I that hideous to him?)"
                show sc viviansroom v20
                vic"What on earth are you talking about, woman?"
                show sc viviansroom v19
                v"Oh, come on, [vic_name]."
                if v_ep01_03_04_Vivians_Room_Remained == True:
                    v"I pretty much gave you an open invitation to join me in there, but you got what you wanted and left."
                else:
                    v"I pretty much gave you an open invitation to join me in there, but you just left."
                show sc viviansroom v17
                v"Why don't you want to be with me?"
                show sc viviansroom v20
                vic"Are you off your fucking meds??"
                vic"What the hell are you referring to?"
                show sc viviansroom v18
                vic"I literally just came back from being downstairs and sat on the bed."
                show sc viviansroom v19
                v"You... You did?"
                #victor looks at her like she's insane"
                show sc viviansroom v15
                vic"Unbelievable..."
                vic"You're losing it, [v_name]."
                show sc viviansroom v16
                vic"Christ... I'm going to get ready for bed as I need my sleep."
                vic"I'll leave you to sort out your paranoid delusions."
                #victor enters the bathroom and slams the door behind him"
                show sc viviansroom v18
                v"(Oh God...)"
                v"(I must be going out of mind.)"
                show sc viviansroom v22
                v"(I could have sworn that was [vic_name] watching me in there... wanting to salvage this night and our relationship.)"
                v"(But now he's acting like he knew nothing about it.)"
                show sc viviansroom v18
                if v_ep01_03_04_Vivians_Room_Remained == True:
                    v"(Someone was clearly in there because of the mess on the shower door.)"
                else:
                    v"(It felt like someone was watching me...)"
                v"(So if I wasn't doing all of that in front of him, then who?)"
                #final shot here of Vivian worried but also in deep thought"
                #screen goes blank"
                scene onlayer anim_layer_2
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_girls_rooms_01
            else:
                show sc viviansroom v17
                with dissolve
                v"So... You're still here."
                show sc viviansroom v15
                vic"Yeah, where the hell else would I be?"
                show sc viviansroom v17
                v"And {i}now{/i} you're talking to me. Great..."
                v"(Why is he suddenly giving me the cold shoulder?)"
                show sc viviansroom v20
                vic"What on earth are you talking about, woman?"
                show sc viviansroom v19
                v"Oh, come on, [vic_name]."
                v"I pretty much gave you an open invitation so we could salvage something from this night, and you completely ignored me."
                show sc viviansroom v17
                v"What more do I have to do?"
                show sc viviansroom v20
                vic"Are you off your fucking meds??"
                vic"What the hell are you referring to?"
                show sc viviansroom v18
                vic"I literally just came back from being downstairs and sat on the bed."
                show sc viviansroom v19
                v"You... You did?"
                #victor looks at her like she's insane"
                show sc viviansroom v15
                vic"Unbelievable..."
                vic"You're losing it, [v_name]."
                show sc viviansroom v16
                vic"Christ... I'm going to get ready for bed as I need my sleep."
                vic"I'll leave you to sort out your paranoid delusions."
                #victor enters the bathroom and slams the door behind him"
                show sc viviansroom v18
                v"(Oh God...)"
                v"(I must be going out of mind.)"
                show sc viviansroom v22
                v"(I could have sworn that I was talking to [vic_name] just a few minutes ago while I was having a shower.)"
                v"(But he acted like he knew nothing about it.)"
                show sc viviansroom v18
                v"(So if I wasn't talking to him, then who?)"
                #final shot here of Vivian worried but also in deep thought"
                #screen goes blank"
                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep01_girls_rooms_01

init:

    $ v_ep03_bella_fantasy_counter = 0
    $ v_ep3_bella_nc_scene_locked = False
    $ v_ep03_04_03_maze_minigame_giveup = False

    image anim_ep03_bella_bj1 = Movie(channel="anim_ep03_bella_bj1", play="images/extras/Episode 03/anim_ep03_bella_bj1.webm")
    image anim_ep03_bella_bj2 = Movie(channel="anim_ep03_bella_bj2", play="images/extras/Episode 03/anim_ep03_bella_bj2.webm")
    image anim_ep03_bella_bj_side1 = Movie(channel="anim_ep03_bella_bj_side1", play="images/extras/Episode 03/anim_ep03_bella_bj_side1.webm")
    image anim_ep03_bella_bj_side2 = Movie(channel="anim_ep03_bella_bj_side2", play="images/extras/Episode 03/anim_ep03_bella_bj_side2.webm")
    image anim_ep03_bella_boobj_close1 = Movie(channel="anim_ep03_bella_boobj_close1", play="images/extras/Episode 03/anim_ep03_bella_boobj_close1.webm")
    image anim_ep03_bella_boobj_close2 = Movie(channel="anim_ep03_bella_boobj_close2", play="images/extras/Episode 03/anim_ep03_bella_boobj_close2.webm")
    image anim_ep03_bella_boobj1 = Movie(channel="anim_ep03_bella_boobj1", play="images/extras/Episode 03/anim_ep03_bella_boobj1.webm")
    image anim_ep03_bella_boobj2 = Movie(channel="anim_ep03_bella_boobj2", play="images/extras/Episode 03/anim_ep03_bella_boobj2.webm")

init python:
    def image_sequence(base, image_list, pause_time):
        for img in image_list:
            renpy.show(base+" "+img)
            renpy.transition(dissolve)
            renpy.pause(pause_time)


label lb_ep03_04_03_Maze_Minigame:

#put these following lines in definition script or wherever you want them to be:
    python:
        #definitions of all rooms, containing their exits (next rooms), the render to show, and the best choice (for WT)
        way = [[6,0,0,0,2,0],[7,3,0,0,5,0],[0,0,0,2,1,3],[0,5,0,0,3,1],[10,0,0,4,4,0],
                [0,7,1,0,3,1],[12,8,2,6,7,0],[0,0,0,7,1,3],[14,10,0,0,5,0],[15,0,5,9,4,0],
                [16,0,0,0,2,0,0],[17,0,7,0,2,0],[18,14,0,0,5,0],[0,0,9,13,1,3],[20,0,10,0,2,0],
                [0,17,11,0,3,1],[22,18,12,16,7,1],[23,19,13,17,7,0],[0,20,0,18,6,3],[0,0,15,19,1,3],
                [0,22,0,0,3,1],[0,0,17,21,1,2],[0,24,18,0,3,1],[0,25,0,23,6,1],[0,0,0,24,1,1]]
        #starting room
        room = 1

    #wherever you want, start the maze with this jump
    jump maze
    #################################################

# ALL you need for the maze game (except the above definition), is the following label code:
label maze:
    # show the propper render, according to the room where you are at moment
    if way[room-1][4] == 1:
        scene sc_doors_left
    if way[room-1][4] == 2:
        scene sc_doors_middle
    if way[room-1][4] == 3:
        scene sc_doors_right
    if way[room-1][4] == 4:
        scene sc_doors_middle_left
    if way[room-1][4] == 5:
        scene sc_doors_middle_right
    if way[room-1][4] == 6:
        scene sc_doors_left_right
    if way[room-1][4] == 7:
        scene sc_doors_left_middle_right



    if room == 22:
        show screen scr_secret_icon("v_secrets_ep03_04_03_1") onlayer ontop
        with { "ontop": dissolve}
    else:
        hide screen scr_secret_icon onlayer ontop
    if room == 21:
        if persistent.v_secrets_ep03_04_03_1:
            $ renpy.notify("Secret Easter Egg was already unlocked!")
        else:
            $ renpy.notify("Secret Easter Egg Unlocked!")
            $ persistent.v_secrets_ep03_04_03_1 = True


    if persistent.v_secrets_enabled and persistent.v_secrets_ep03_04_03_1 and v_ep3_bella_nc_scene_locked == False and room == 21:
        label lb_04_03_bella_nc_scene:
            if not _in_replay:
                scene img_secret_scene_overlay onlayer anim_layer
                with { "anim_layer": dissolve}
            else:
                show screen scr_end_replay
            scene black
            with dissolve
            scene black
            with Pause (2)
            #THE NC SCENE BEGINS HERE
            #The “NON-CANON BONUS SCENE" writing will be at the top of the screen as soon as the player chooses “Go WEST"
            #
            #When they do, the screen will go blank, and then return with Bella and the MC in this room: https://pixhost.to/show/291/535783031_screenshot-2024-11-22-at-11-23-25-am.jpg
            #
            #The only difference is the options won’t be on the screen, just the door on the right
            show sc ep3bellanc b001
            with dissolve
            pause 1.0
            show sc ep3bellanc b002
            with dissolve
            mc"Looks like this is the wrong room."
            show sc ep3bellanc b003
            mc"Maybe we should go back the way we came."
            show sc ep3bellanc b004
            b"Sure, but can you give me a moment?"
            show sc ep3bellanc b001
            b"I just need to change."
            show sc ep3bellanc b005
            with dissolve
            pause 1.0
            #Bella removes her mask
            show sc ep3bellanc b006
            with dissolve
            pause 1.0
            #She then removes the top rubber part around her neck and her arms - https://pixhost.to/show/291/535783753_screenshot-2024-11-22-at-11-26-05-am.png
            show sc ep3bellanc b007
            mc"[b_name]? What are you doing?"
            #
            #she looks directly at the MC
            show sc ep3bellanc b008
            b"It’s a little hot in here, and I need some air."
            $ image_sequence("sc ep3bellanc", ["b009", "b010", "b011"], 1.5)
            # show sc ep3bellanc b009
            # with dissolve
            # pause 1.0
            # #Bella reaches behind her back to unzip her outfit
            # show sc ep3bellanc b010
            # with dissolve
            # pause 1.0
            # #Show her pulling the zip down on the back of her outfit, unveiling her back
            # show sc ep3bellanc b011
            # with dissolve
            # pause 1.0
            #Show Bella peeling off her rubbery outfit, so it slides down her body
            #
            #Her naked breasts are revealed - she’s not wearing a bra
            pause 0.5
            show sc ep3bellanc b012
            with vpunch
            mc"What the-"
            show sc ep3bellanc b013
            with dissolve
            pause 1.0
            #Show Bella sliding down her outfit to the ground. She’s wearing pink silk, almost see-through panties -
            #https://m.media-amazon.com/images/M/MV5BZmRkMWJhMzgtZTBmOC00YTYzLWJlZWEtMjkyZjQ4OGNjMmQwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg
            show sc ep3bellanc b014
            with dissolve
            pause 1.0
            #Then show her standing before the MC, in just her underwear
            show sc ep3bellanc b015
            with dissolve
            b"You can’t tell me that you haven’t fantasised about seeing me like this, [y_name]."
            show sc ep3bellanc b016
            b"You haven’t taken your eyes off my chest ever since we got out of the van."
            show sc ep3bellanc b016a
            with dissolve
            pause 1.5
            show sc ep3bellanc b017
            with dissolve
            mc"Yeah, but-"
            show sc ep3bellanc b018
            b"Shh..."
            show sc ep3bellanc b016
            b"It’s just you and me here, the rest of the [private_group] never have to know."
            show sc ep3bellanc b019
            mc"Never have to know what?"
            show sc ep3bellanc b020
            b"What I’m about to do for you."
            $ image_sequence("sc ep3bellanc", ["b022", "b023", "b021"], 1.5)
            # show sc ep3bellanc b022
            # with dissolve
            # pause 1.0
            # #Bella approaches the MC in slow motion - two or three frames
            # show sc ep3bellanc b023
            # with dissolve
            # pause 1.0
            # #She gets in close and kisses the MC
            # show sc ep3bellanc b021
            # with dissolve
            # pause 1.0

            play sound "sound effects/01/kiss_and_moan_sound_effect02.mp3" loop fadein 1.0
            show sc ep3bellanc b024
            with dissolve
            b"Mmm..."
            $ image_sequence("sc ep3bellanc", ["b025", "b026", "b027"], 1.5)
            # show sc ep3bellanc b025
            # with dissolve
            # pause 1.0
            # #Show the MC with a hand on her breast and the other on her asscheek while they makeout
            # show sc ep3bellanc b026
            # with dissolve
            # pause 1.0
            # show sc ep3bellanc b027
            # with dissolve
            # pause 1.0
            # show sc ep3bellanc b028
            # with dissolve
            # pause 1.0
            #They stop kissing
            stop sound fadeout 1.0
            show sc ep3bellanc b028
            with dissolve
            pause 1.5
            show sc ep3bellanc b029
            mc"Sorry, [b_name]. I had no idea that you felt this way."
            show sc ep3bellanc b030
            b"There’s a lot more that I’m feeling, [y_name]."
            show sc ep3bellanc b031
            b"Like for instance, your big, hard, cock..."
            #Show Bella’s hand on the erection in the MC’s pants
            mc"Uhh..."
            show sc ep3bellanc b032
            b"You’re incredibly tense, little [mc_b_rel]."
            #
            b"Want me to take care of that for you?"
            show sc ep3bellanc b033
            mc"Uh, how do you mean?"
            show sc ep3bellanc b030
            b"Let me explain it to you in Layman’s terms..."
            #
            #Bella puts her mouth up against the MC’s ear so she’s whispering
            show sc ep3bellanc b034
            b"I’m gonna suck your cock, and make you cum in my mouth."
            play sound "sound effects/01/kiss_and_moan_sound_effect02.mp3" loop fadein 1.0
            show sc ep3bellanc b035
            with dissolve
            b"Mmm..."
            #Bella licks the bottom part of his earlobe
            mc"NGHH..."
            #Bella and the MC kiss

            show sc ep3bellanc b036
            b"Mmm..."
            #
            #Show her sliding down the bottom half of his costume
            stop sound fadeout 1.0
            show sc ep3bellanc b037
            with vpunch
            mc"OH!"
            stop sound
            #Bella takes the MC’s cock in her hand
            show sc ep3bellanc b038
            b"Oooh..."
            show sc ep3bellanc b041
            b"Now this is a surprise."
            #
            #Bella slowly kneels down as the MC is backed up against one of the walls in the room
            show sc ep3bellanc b042
            mc"[b_name]..."
            show sc ep3bellanc b043
            b"Relax, [y_name]."
            b"We’ll get back to the heist shortly."
            show sc ep3bellanc b044
            b"But first, I need to make sure that your head is clear."
            show sc ep3bellanc b045
            b"Speaking of which."
            show sc ep3bellanc b046
            with dissolve
            pause 1.0
            #Bella looks at the tip of his cock
            show sc ep3bellanc b047
            with dissolve
            pause 1.0
            #Bella licks around the head of his cock
            show sc ep3bellanc b048
            with dissolve
            pause 1.0
            #Bella closes her moistened lips around the tip
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_bj1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b049
            mc"UHH!"
            #
            #ANIMATED SCENE OF BELLA SUCKING THE MC’S COCK
            play sound "sound effects/01/sex/sofa_blowjob.mp3" loop fadein 1.0
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_bj_side1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b050
            b"Mmm...."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_bj2:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b049
                with dissolve
            mc"Oh, [b_name]."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_bj_side2:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b050
            mc"Fuck..."
            stop sound
            #Show a shot from behind Bella where she’s kneeling before the MC, and is just in her underwear
            #
            #She takes him out of her mouth and looks up at the MC
            show sc ep3bellanc b051
            b"Well don’t just stand there, [y_name]."
            b"Play with my breasts, or ask me to take more of you in my mouth."
            show sc ep3bellanc b052
            b"Do something!"
            show sc ep3bellanc b053
            mc"You got it."
            #
            #[Fuck her mouth / Fondle her tits]
            menu:
                "Fuck her mouth":
                    #The MC puts a hand on the back of Bella’s head and fucks her mouth
                    play sound "sound effects/01/sex/sofa_blowjob.mp3" loop fadein 1.0
                    show sc ep3bellanc b054
                    mc"Aw yeah..."
                    show sc ep3bellanc b055
                    with dissolve
                    pause 1.0
                    mc"That’s it, take me deep, [b_name]."
                    show sc ep3bellanc b056
                    with dissolve
                    pause 1.0
                    b"Nnn..."
                    show sc ep3bellanc b057
                    with dissolve
                    pause 1.0
                    #ANIMATED SCENE OF BELLA SUCKING THE MC’S COCK while he has his hand on the back of her head

                "Fondle her tits":
                    #
                    #The MC reaches down to squeeze Bella’s breast while she sucks his cock
                    play sound "sound effects/01/sex/sofa_blowjob.mp3" loop fadein 1.0
                    show sc ep3bellanc b058
                    with dissolve
                    mc"Oh wow..."
                    show sc ep3bellanc b059
                    with dissolve
                    pause 1.0
                    mc"You’ve always had incredible tits, [b_name]."
                    show sc ep3bellanc b060
                    with dissolve
                    b"Nnn..."
                    #Bella smiles while she has the MC’s dick in her mouth
                    #ANIMATED SCENE OF BELLA SUCKING THE MC’S COCK while he squeezes one of her breasts
            #
            #scene continues
            show sc ep3bellanc b061
            with dissolve
            b"Mmm..."
            stop sound
            show sc ep3bellanc b062
            with dissolve
            pause 1.0
            #Bella resumes control, cupping the MC’s balls and sucking his dick
            show sc ep3bellanc b051
            with dissolve
            b"I want you to cum for me [y_name]."
            show sc ep3bellanc b052
            b"And to always remember it."
            show sc ep3bellanc b063
            b"And I know exactly the best way to make that happen."
            #
            #Show Bella letting go of his cock
            show sc ep3bellanc b064
            with dissolve
            pause 1.5
            #Show Bella kneeling up a bit higher, so her chest is the same height as the MC’s cock
            #
            #Show Bella grabbing her breasts
            #
            #And then pulling them apart
            show sc ep3bellanc b065
            with dissolve
            pause 1.5
            #Show Bella moving forward and pressing her tits around his dick
            show sc ep3bellanc b066
            with dissolve
            pause 1.5
            mc"Oh God..."
            #Bella looks up at the MC with her tits wrapped around his cock
            show sc ep3bellanc b067
            with dissolve
            b"Go for it. Fuck my huge, succulent titties..."
            #
            #ANIMATED SCENE OF THE MC titty-fucking BELLA
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_boobj_close1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b068
                with dissolve
            mc"NGHH!"
            mc"This feels amazing!"
            show sc ep3bellanc b069
            with dissolve
            b"Are you gonna cum for me, [y_name]?"
            show sc ep3bellanc b077
            b"Are you gonna cum for your older [b_mc_rel]?"
            show sc ep3bellanc b073
            mc"God yes!!"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_boobj_close2:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b066
            b"How hard?"
            show sc ep3bellanc b067
            mc"Huh?"
            play sound "sound effects/01/sex/sofa_blowjob.mp3" loop fadein 1.0
            show sc ep3bellanc b070
            b"Mmm..."
            #Bella bends her face down and licks the head of his cock while it’s between her breasts
            show sc ep3bellanc b068
            b"I said how hard are you gonna cum for me?"
            #
            #Bella bends her face down and places her lips on the head of his cock while it’s between her breasts
            show sc ep3bellanc b071
            b"Mmm..."
            show sc ep3bellanc b072
            mc"Oh shit!!"
            show sc ep3bellanc b073
            mc"Really fucking hard!!"
            stop sound
            show sc ep3bellanc b069
            b"Then do it!"
            show sc ep3bellanc b067
            b"I want you to cum all over me."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_boobj1:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b066
            b"Just like you’ve imagined doing whenever you’re all alone in your room and you’re jerking off thinking about me."
            #ANIMATED SCENE OF THE MC titty-fucking BELLA
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_boobj_close2:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b074
            b"I want you to cum on my big breasts."
            #Show his dick between her tits
            show sc ep3bellanc b075
            b"On my pretty face."
            #show her face
            show sc ep3bellanc b076
            b"Cream on my lips and inside my warm, wet mouth..."
            #show her lips as she says this line above
            #
            #Bella opens her mouth while she looks up at the MC
            show sc ep3bellanc b072
            mc"Here it comes, [b_name]..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene anim_ep03_bella_boobj2:
                    size (config.screen_width, config.screen_height)
            elif True:
                show sc ep3bellanc b077
            b"Give it to me, [y_name]!"
            show sc ep3bellanc b077
            with slow_dissolve
            b"[y_name]..."
            with slow_dissolve
            b"[y_name]..."
            scene black
            with Dissolve(1.0)


            #screen starts to fade before the MC climaxes
            show sc ep3bellanc b078
            with flash(0.25, 0, 0.75, "#fff")
            b"[y_name]?"
            #the screen fizzles
            #then the screen returns to Bella and the MC inside the same room, the MC is daydreaming
            show sc ep3bellanc b079
            b"[y_name]!"
            show sc ep3bellanc b080
            mc"Huh?"
            show sc ep3bellanc b081
            mc"Oh, what did you say, [b_name]?"
            show sc ep3bellanc b082
            b"Which way do we go next?"
            show sc ep3bellanc b081
            mc"Oh, right."
            show sc ep3bellanc b083
            with dissolve
            mc"Let me see here."
            scene onlayer anim_layer
            with { "anim_layer": dissolve}
            $ persistent.replay_ep03_bella_maze_fantasy = False
            $ renpy.end_replay()
            $ v_ep03_bella_fantasy_counter += 1
            $ v_ep3_bella_nc_scene_locked = True
            #THE NC SCENE ENDS HERE AND RETURNS TO THE MINI-GAME MAZE

#NOTE: all these choices are shown or hidden according to the WT settings and the current doors in the room
    menu:
        "Go NORTH"(wt="Correct choice") if (way[room-1][0] > 0) and (way[room-1][5] == 0) and (persistent.v_walkthrough_enabled):
            python:
                room = way[room-1][0]
        "Go NORTH" if (way[room-1][0] > 0) and (not (persistent.v_walkthrough_enabled) or (way[room-1][5] <> 0)):
            python:
                room = way[room-1][0]
        "Go EAST"(wt="Correct choice") if (way[room-1][1] > 0) and (way[room-1][5] == 1) and (persistent.v_walkthrough_enabled):
            python:
                room = way[room-1][1]
        "Go EAST" if (way[room-1][1] > 0) and (not (persistent.v_walkthrough_enabled) or (way[room-1][5] <> 1)):
            python:
                room = way[room-1][1]
        "Go SOUTH"(wt="Correct choice") if (way[room-1][2] > 0) and (way[room-1][5] == 2) and (persistent.v_walkthrough_enabled):
            python:
                room = way[room-1][2]
        "Go SOUTH" if (way[room-1][2] > 0) and (not (persistent.v_walkthrough_enabled) or (way[room-1][5] <> 2)):
            python:
                room = way[room-1][2]
        "Go WEST"(wt="Correct choice") if (way[room-1][3] > 0) and (way[room-1][5] == 3) and (persistent.v_walkthrough_enabled):
            python:
                room = way[room-1][3]
        "Go WEST" if (way[room-1][3] > 0) and (not (persistent.v_walkthrough_enabled) or (way[room-1][5] <> 3)):
            python:
                room = way[room-1][3]
        # Added choice to "Give up" and skip to the end of the maze
        "Give Up":
            $ v_ep03_04_03_maze_minigame_giveup = True
            python:
                room = 25
    # check for reaching last room, if not reached, continue maze in next room
    if room < 25:
        jump maze

    if v_ep03_04_03_maze_minigame_giveup == False:
        $ wallpaper_unlock(4)

    jump lb_ep03_04_03_The_Art_Gallery_Heist_Part_2_continues
#Continue the game like usual with next label
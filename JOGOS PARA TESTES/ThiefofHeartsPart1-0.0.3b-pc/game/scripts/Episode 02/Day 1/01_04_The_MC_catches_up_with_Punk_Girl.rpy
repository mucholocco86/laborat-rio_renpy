init python:
    import math
    def dial_events(event, x, y, st):
        global dial_rotate
        global old_mousepos
        global old_degrees
        global degrees
        global dial_start_rotate
        global dial_text
        global dial_number
        global previous_dial_text
        global dial_changed
        global combination_length
        global completed_combination_numbers
        global safe
        global dial_image
        global dial_image2
        global v_ep02_01_04_Cracking_Attempts

        if event.type == renpy.pygame_sdl2.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dial_start_rotate:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] + dial_x_offset and dial_sprite.y <= y <= dial_sprite.y + dial_size[1] + dial_y_offset:
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] - dial_y_offset / 2) - y, (dial_sprite.x + dial_size[0] - dial_x_offset / 2) - x)
                        old_degrees = math.degrees(angle_radians) % 360
                else:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] and dial_sprite.y <= y <= dial_sprite.y + dial_size[1]:
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] / 2) - y, (dial_sprite.x + dial_size[0] / 2) - x)
                        old_degrees = math.degrees(angle_radians) % 360
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                dial_rotate = False
                safe = "safe_{}".format(current_safe)
                if dial_changed:
                    if combination_length < 3:
                        dial_changed = False
                        if len(completed_combination_numbers) == 0:
                            completed_combination_numbers[safe] = []
                            completed_combination_numbers[safe].append(dial_text)
                        else:
                            completed_combination_numbers[safe].append(dial_text)
                        combination_length += 1
                    if combination_length == 3:
                        if completed_combination_numbers[safe] == combinations[safe]:
                            dial_changed = False
                            combination_length = 0
                            v_ep02_01_04_Cracking_Attempts += 1
                            renpy.jump("lb_ep02_01_04_Safe_Cracking_Success")
                        else:
                            dial_changed = False
                            combination_length = 0
                            v_ep02_01_04_Cracking_Attempts += 1
                            renpy.jump("lb_ep02_01_04_Safe_Cracking_Failed")
                renpy.restart_interaction()
        elif event.type == renpy.pygame_sdl2.MOUSEMOTION:
            safe = "safe_{}".format(current_safe)

            if dial_rotate:
                angle_radians = math.atan2((dial_sprite.y + dial_size[1] / 2) - y, (dial_sprite.x + dial_size[0] / 2) - x)
                degrees = math.degrees(angle_radians) % 360
                rotate_amount = math.hypot(x - old_mousepos[0], y - old_mousepos[1]) / 5 # Adjust the last number to change the rotate speed
                if degrees > old_degrees:
                    dial_sprite.rotate_amount += rotate_amount
                elif degrees < old_degrees:
                    dial_sprite.rotate_amount -= rotate_amount


                t = Transform(child = dial_image)
                t.rotate = 3.6 * round(dial_sprite.rotate_amount / 3.6) # Adjust the numerical values so it ticks in specific incriments
                if int(t.rotate /3.6) % 100 == 0 and int(t.rotate /2.6) != 0:
                    dial_number = 0
                    dial_sprite.rotate_amount = 0.0
                else:
                    dial_number = int(t.rotate / 3.6)

                if dial_number > 0 and dial_number < 100:
                    dial_text = 100 - dial_number
                elif dial_number < 0 and dial_number > -100:
                    dial_text = abs(dial_number)
                else:
                    dial_text = dial_number

                if dial_text != previous_dial_text:
                    dial_changed = True
                    renpy.music.play("sound effects/02/safe_tumbler_click_single.ogg", "sound2", relative_volume = 1.0)

                    for i in combinations[safe]:
                        if ((renpy.music.is_playing('sound3')) == False and (combination_length == 0 and dial_text == combinations[safe][0]) or (combination_length == 1 and dial_text == combinations[safe][1]) or (combination_length == 2 and dial_text == combinations[safe][2])):
                            renpy.music.play("sound effects/02/safe_tumbler_locking_into_place.ogg", "sound3", loop=False, relative_volume = 0.2)

                if(int(dial_text) >= 0 and int(dial_text) <= 99):
                    dial_image2 = "sc mcfindgirld 049 dial[dial_text]"
                    t2 = Transform(child = dial_image2)
                    dial_sprite2.set_child(t2)
                else:
                    dial_changed = False
                    combination_length = 0
                    renpy.jump("lb_ep02_01_04_Safe_Cracking_Fast")

                previous_dial_text = dial_text
                t.subpixel = True
                dial_start_rotate = True
                dial_sprite.set_child(t)
                dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2 - dial_x_offset
                dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2 - dial_y_offset
                dial_sprite2.x = config.screen_width / 2 - dial_size[0] / 2 - dial2_x_offset
                dial_sprite2.y = config.screen_height / 2 - dial_size[1] / 2 - dial2_y_offset
                old_degrees = math.degrees(angle_radians) % 360
                old_mousepos = (x, y)

                dial_sprite_manager.redraw(0)
                renpy.restart_interaction()

    def reset_safe():
        global dial_start_rotate
        global dial_text
        global dial_number
        global combination_length
        global completed_combination_numbers

        dial_number = 0
        dial_text = 0
        dial_sprite.rotate_amount = 0
        completed_combination_numbers = {}
        combination_length = 0
        dial_start_rotate = False

        t = Transform(child = dial_image)
        dial_sprite.set_child(t)
        dial_image2 = "sc mcfindgirld 049 dial0"
        t2 = Transform(child = dial_image2)
        dial_sprite2.set_child(t2)
        dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2 - 12
        dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2 - 5
        dial_sprite2.x = config.screen_width / 2 - dial_size[0] / 2 - 12
        dial_sprite2.y = config.screen_height / 2 - dial_size[1] / 2 - 5
        dial_sprite_manager.redraw(0)

init:
    $ v_ep02_01_04_Switch_The_Drives = False
    $ v_ep02_01_04_Leave_a_Note = False
    $ v_ep02_01_04_The_Shower = False
    $ v_ep02_01_04_Safe_Bypassed = False
    $ v_ep02_01_04_Cracking_Attempts = 0

    screen scr_ep02_01_04_Punk_Girl_Room_Choices:
        default tt = Tooltip("Where will you look?")
        zorder 10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc mcfindgirld 060"

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered tt.Action("The Shower" + If(persistent.v_walkthrough_enabled == True,"{color=#33ff33} (Better option){/color}",""))
            auto"images/Episode 02/Day 01/01-04 MC Mystery Girl/sc mcfindgirld 060 door %s.png"
            action [Hide("scr_ep02_01_04_Punk_Girl_Room_Choices"),Jump("lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door")]

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered tt.Action("The Shelves")
            auto "images/Episode 02/Day 01/01-04 MC Mystery Girl/sc mcfindgirld 060 shelves %s.png"
            action [Hide("scr_ep02_01_04_Punk_Girl_Room_Choices"),Jump("lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Shelves")]

        frame:
            xfill True
            xalign 0.5
            yalign 0.0
            vbox:
                xalign 0.5
                yalign 0.5
                text tt.value

    screen scr_ep02_01_04_Safe_Cracking:
        on "show" action Function(reset_safe)
        image "sc mcfindgirld 049 safe bg"
        image "sc mcfindgirld 049 safe arrow"

        add dial_sprite_manager
        text "{size=180}[dial_text]{/size}" color "#000000" align(0.494,-0.02) text_align 0.5
        text "{size=24}Spin the dial and release on the number you think it is. Repeat this 3 times to select the combination.\n(NOTE: Bypassing the lock will prevent any possible reward unlocks.)\nHINT: Listen for the sound of the tumbler clicking into place.{/size}" color "#ffffff" align(0.5,0.90)  outlines [ (3, "#000000", 0, 0) ] text_align 0.5

        textbutton "BYPASS":
            text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
            xalign 0.7
            yalign 0.5
            focus_mask True
            action [SetVariable("v_ep02_01_04_Safe_Bypassed",True),Jump("lb_ep02_01_04_Safe_Cracking_Success")]

    image sc mcfindgirld nc rub:
        "sc mcfindgirld nc 001" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 001a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 001b" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 001a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc mcfindgirld nc dildo1:
        "sc mcfindgirld nc 004" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 004a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 004b" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcfindgirld nc 004a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc mcfindgirld nc dildo2:
        "sc mcfindgirld nc 005" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc mcfindgirld nc 005a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc mcfindgirld nc 005b" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc mcfindgirld nc 005c" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc mcfindgirld nc dildo3:
        "sc mcfindgirld nc 006" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 006a" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 006b" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 006a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc mcfindgirld nc dildo4:
        "sc mcfindgirld nc 007" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 007a" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 007b" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 007a" with Dissolve(0.2, alpha=True)
        pause 0.3
        repeat

    image sc mcfindgirld nc dildo5:
        "sc mcfindgirld nc 008" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 008a" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 008b" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 008a" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat

    image sc mcfindgirld nc dildo6:
        "sc mcfindgirld nc 009" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 009a" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 009b" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 009a" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat

    image sc mcfindgirld nc dildo7:
        "sc mcfindgirld nc 010" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 010a" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 010b" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcfindgirld nc 010a" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat

    image sc mcfindgirld nc dildo fall:
        "sc mcfindgirld nc 011" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 011a" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc 011b" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mcfindgirld nc dildo twitch" with Dissolve(0.2, alpha=True)

    image sc mcfindgirld nc dildo twitch:
        "sc mcfindgirld nc 011c" with Dissolve(0.2, alpha=True)
        pause renpy.random.choice([0.3, 0.35, 0.4, 0.45, 0.5, 0.55])
        "sc mcfindgirld nc 011d" with Dissolve(0.2, alpha=True)
        pause renpy.random.choice([0.3, 0.35, 0.4, 0.45, 0.5, 0.55])
        repeat

    image sc mcfindgirld nc store dildo:
        "sc mcfindgirld nc 012" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcfindgirld nc 012a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcfindgirld nc 012b" with Dissolve(0.2, alpha=True)
        pause 1.5
        "sc mcfindgirld nc 012c" with Dissolve(0.2, alpha=True)
        pause 1.5
        "black" with Dissolve(1.0, alpha=True)
        pause 1.0
        "sc mcfindgirld nc 013" with Dissolve(1.0, alpha=True)

    image sc mcfindgirld zoom out:
        "sc mcfindgirld 147a" with Dissolve(0.6, alpha=True)
        pause 1.0
        "sc mcfindgirld 147b" with Dissolve(0.6, alpha=True)
        pause 1.0
        "sc mcfindgirld 147c" with Dissolve(0.6, alpha=True)

    image sc mcfindgirld flip card:
        "sc mcfindgirld 140a" with Dissolve(0.6, alpha=True)
        pause 0.4
        "sc mcfindgirld 140b" with Dissolve(0.6, alpha=True)

    image sc mcfindgirld eyes on you:
        "sc mcfindgirld 032" with Dissolve(0.6, alpha=True)
        pause 1.0
        "sc mcfindgirld 033" with Dissolve(0.6, alpha=True)

label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl:
    #SCENE BEGINS
    #The scene begins with the MC standing on a street corner, underneath a street light
    play ambient "sound effects/02/night_town_ambience.mp3" loop fadein 1.0
    scene sc mcfindgirld 001
    with dissolve
    mc"(This must be the place.)"
    #there's an abandoned apartment block across the road which is where Pretty Girl is hiding out
    #the building has 3-4 floors - IMPORTANT
    show sc mcfindgirld 002
    mc"(But where is this contact of Lucy's who I'm supposed to meet with?)"
    #the MC looks around
    #This contact stands behind the MC holding a gun to his back
    show sc mcfindgirld 003
    with dissolve
    un"Don't move, don't make a sound."
    show sc mcfindgirld 003a
    with faster_dissolve
    with hpunch
    mc"(Holy crap!)"
    un"Turn around, slowly."
    #Bruno has a hoodie on so we can't see his full face
    #He's an older guy - mid-30s, scruffy beard, a bigger guy and calm in his demeanour, rarely smiles
    show sc mcfindgirld 004
    with faster_dissolve

    mc"Are you... Bruno?"
    show sc mcfindgirld 005
    bruno"Yeah, that's me."
    #He pulls the gun away on mc
    show sc mcfindgirld 006
    bruno"And you're [y_name]."
    #bruno eyes up the MC
    show sc mcfindgirld 007
    bruno"Hmm... You're a lot younger than I was expecting."
    #his expression is slightly different to the line above
    show sc mcfindgirld 008
    mc"What I lack in experience I make up for in tactical nous, and being as rare as an Iberian lynx."
    #a cocky line from the MC
    show sc mcfindgirld 009
    bruno"I have no idea what nous means or what an Iberian lynx is."
    #Bruno angrily points at the MC
    show sc mcfindgirld 010
    with faster_dissolve
    bruno"What I do know is, that girl you're looking for just went into that building a short time ago and hasn't come out."
    show sc mcfindgirld 011
    with faster_dissolve
    #He points across the road to the building he's referring to
    mc"And it's definitely her? Are you sure?"
    show sc mcfindgirld 012
    with dissolve
    bruno"I make no bones about it."
    show sc mcfindgirld 013
    with faster_dissolve
    bruno"She's already eluded me more than enough times that I know her face like the back of my hand."
    #above render but slightly different expression
    show sc mcfindgirld 014
    with faster_dissolve
    bruno"But she won't get away from me this time."
    #bruno seems confident
    show sc mcfindgirld 015
    with faster_dissolve
    bruno"Or at the very least, I'll get back what she stole from Lucy."
    #a focused expression from Bruno
    show sc mcfindgirld 016
    mc"About that... What is it she wants me to steal for her?"
    #Bruno has his mouth closed while the MC speaks
    show sc mcfindgirld 017
    bruno"This..."
    #Bruno shows the MC a picture on his phone of the item Lucy wants him to steal
    show sc mcfindgirld 018
    with faster_dissolve
    pause
    show sc mcfindgirld 019
    mc"Are you shitting me? That's what she wants me to steal??"
    #the MC is somewhat angry
    show sc mcfindgirld 020
    with faster_dissolve
    mc"This has to be some kind of sick joke."
    show sc mcfindgirld 021
    bruno"It's no joke, kid."
    #Bruno has a serious look on his face
    show sc mcfindgirld 022
    with faster_dissolve
    mc"(Unbelievable...)"
    #Show the MC looking at the phone and it's a golden dildo like this - https://www.myfucsia.com/wp-content/uploads/2017/02/TheKing.jpg
    show sc mcfindgirld 023
    with faster_dissolve
    mc"(Of all the things I have to steal...)"
    show sc mcfindgirld 024
    mc"(This is so humiliating.)"
    #the MC looks dismayed
    show sc mcfindgirld 025
    bruno"It's very precious to Lucy, and if you can get it back, you'll definitely be in her good books."
    #sorry can't reuse it since Bruno is holding a gun or his phone 🥺
    show sc mcfindgirld 026
    with faster_dissolve
    bruno"And trust me, you don't want to be anywhere else with her."
    show sc mcfindgirld 027
    mc"Okay, fine. I'll do it."
    #the MC is reluctant
    show sc mcfindgirld 028
    with faster_dissolve
    mc"What else can you tell me about this place?"
    mc"Are there any back entrances in or out of there?"
    #reuse a render from above  #can reuse 019
    show sc mcfindgirld 029
    bruno"Just one way in, and one way out as far as I know."
    show sc mcfindgirld 013
    with faster_dissolve
    bruno"This apartment block has been abandoned for a few years and any exits have been boarded up."
    #reuse a render from above #you can reuse 025
    show sc mcfindgirld 030
    with faster_dissolve
    bruno"So even if she tries to escape or gets away from you, I'll be right here waiting for her."
    #a slightly different expression to the one above
    show sc mcfindgirld 025
    with faster_dissolve
    bruno"As for where exactly she is in there... You're going to have to figure that out for yourself."
    #reuse a render from above #can reuse 026
    show sc mcfindgirld 031
    mc"(Great... I'm going in blind.)"
    #the MC has a straight face, thinking
    show sc mcfindgirld 034
    mc"All right, let me get this over with."
    #reuse a render from above
    show sc mcfindgirld 029
    bruno"One more thing before you go..."
    #reuse a render from above
    show sc mcfindgirld eyes on you
    bruno"I've got my eyes on you too, kid..."
    #Bruno gives the MC the MEET THE PARENTS - De Niro look - https://y.yarn.co/9383f01f-053e-4ee3-a140-4d397df6d44c_text.gif
    show sc mcfindgirld 034
    mc"Yeah, I've been hearing that a lot lately."
    show sc mcfindgirld 035
    with dissolve
    pause 2.0
    stop ambient fadeout 1.0
    #Final shot of the MC walking across the street to the abandoned building
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #scene returns with the MC inside the abandoned building
    #Think empty hallways like in The Walking Dead - https://i.redd.it/780kciiwydab1.jpg
    play music "sound effects/01/Midnight Heist.mp3" loop fadein 1.0
    show sc mcfindgirld 036
    with dissolve
    pause 1.0
    show sc mcfindgirld 037
    #show the MC walking down this hallway, which is lit up
    #HE'S ON THE FIRST FLOOR - IMPORTANT FOR LATER
    with dissolve
    mc"(Hmm... I wonder if the owners of this building realise that the power is still on.)"
    show sc mcfindgirld 038
    with dissolve
    mc"(It's no wonder this girl is hiding out here.)"
    #make sure the hallway changes in the background to show he's walking forward
    show sc mcfindgirld 039
    with dissolve
    mc"(Free rent, free electricity and she's in a place most people would never look.)"
    mc"(Until now.)"
    #The MC notices a room at the end of the hall
    show sc mcfindgirld 040
    with dissolve
    mc"(That could be her room over there.)"
    #The MC gets to the door which is slightly open
    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
    show sc mcfindgirld 041
    with dissolve
    mc"(I can hear something coming from inside.)"
    #The MC pushes the door forward
    #creaking sound of the door effect
    stop music fadeout 1.0
    play music2 "sound effects/02/Mission Unseen.mp3" loop fadein 1.0
    $ renpy.music.set_volume(0.3, 1.0, channel="ambient")
    show sc mcfindgirld 042
    with dissolve
    mc"(Oh damn... This must be it.)"
    #The MC enters her room - https://i.redd.it/tjocvy06bw951.jpg (this but place a nice bed inside)
    show sc mcfindgirld 043
    with dissolve
    pause 0.6
    #It has a bed, dresser drawer for makeup, an open closet with numerous dresses - https://i.pinimg.com/236x/76/4b/e5/764be5b6ae4dc76419a2cd11815c3a13.jpg
    #IMPORTANT - have a table with 3-4 different wigs on it, but don't make it obvious -https://i.etsystatic.com/18719331/r/il/64e9c1/4221520184/il_fullxfull.4221520184_qb1r.jpg
    #Put it in the background
    #It's a clue about the girl's persona for a future update
    show sc mcfindgirld 044
    with faster_dissolve
    mc"(I wonder how much of this stuff is stolen.)"
    #Shower starts - sound effect
    show sc mcfindgirld 045
    with faster_dissolve
    mc"(Oh shit!)"
    #the MC cups his mouth
    show sc mcfindgirld 045a
    mc"(She's in the bathroom!!)"
    show sc mcfindgirld 046
    mc"(Now's my chance to get in and out of here without her even knowing.)"
    show sc mcfindgirld 047
    with dissolve
    mc"(I should look around for the flash drive first. But where would it be?)"
    #the MC looks around the room which has a small safe in the corner of the room -
    #https://www.daz3d.com/antique-safe

    show sc mcfindgirld 048
    with dissolve
    mc"(Hmm... There's a small safe over there.)"
    #the MC goes over to it

    #MINI-GAME - IMPORTANT
    #Dots or Mistress will create this mini-game - just make sure to have the renders in place for this scene
    #there will be a simple mini-game here where the player/MC will spin the dial in three directions - right (clockwise), left (anti-clockwise), and then right (clockwise) again.

    #When the player begins, the dial will begin at position "0", and click over in a clockwise direction. It will make a beep sound when it is at the correct point to stop.
    #they will then have the option to "turn the dial to the right" and then the same again - they need to stop when they hear a "beep" sound (then an option to "turn the dial left")

    #the dial will turn back to the left and when they hear the beeping sound a third time, they need to stop and an option will come up to "Open the safe".
    #IF the player goes past the "beep" position at any point, they will have to start over at position "0"

    #Like with the keypad safe in Episode 1, the player will get the BYPASS option if they don't want to do the mini-game, and will continue on with the game.
    #However, if they do the mini-game and beat it, they will get a SECRET IMAGE of Pretty Girl in the gallery
    #Combination - the dial needs to land on 80, then 22, then finish on 12.
    #the MC leans down and looks at the safe - https://www.daz3d.com/antique-safe
    #This is what the dial will look like - https://c8.alamy.com/comp/B5671A/safe-dial-B5671A.jpg

    show sc mcfindgirld 049
    with dissolve
    mc"(It looks quite old, so this should be a piece of cake.)"
    stop music2 fadeout 1.0
    play music "sound effects/02/Heist of the Night.mp3" loop fadein 1.0
    #The MC puts his ear to the safe

    #On-Screen Notification: "Listen out for the beep when you turn the dial. When you hear it, spin the dial in the opposite direction until you hear it again. After you hear the beep a third time, then you can open the safe."
    #scene sc mcfindgirld 049 safe bg

    # Dial Variables
    $ dial_image = "sc mcfindgirld 049 dial0"
    $ dial_image2 = "sc mcfindgirld 049 dial0"
    $ dial_size = (518, 518)
    $ t = Transform(child = dial_image)
    $ t2 = Transform(child = dial_image2)
    $ dial_sprite_manager = SpriteManager(event = dial_events)
    $ dial_sprite = dial_sprite_manager.create(t)
    $ dial_sprite2 = dial_sprite_manager.create(t2)
    $ dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2 - 12
    $ dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2 - 5
    $ dial_sprite2.x = config.screen_width / 2 - dial_size[0] / 2 - 12
    $ dial_sprite2.y = config.screen_height / 2 - dial_size[1] / 2 - 5
    $ dial_rotate = False
    $ dial_sprite.rotate_amount = 0
    $ dial_x_offset = 119.2
    $ dial_y_offset = 112.40
    $ dial2_x_offset = 12
    $ dial2_y_offset = 5
    $ dial_start_rotate = False
    $ dial_number = 0
    $ dial_text = 0
    $ previous_dial_text = 0
    $ dial_changed = False

    # Other Variables
    $ old_mousepos = (0.0, 0.0)
    $ degrees = 0
    $ old_degrees = 0
    $ combinations = {"safe_1" : [4,21,81]}
    $ completed_combination_numbers = {}
    $ current_safe = 1
    $ safe = "safe_{}".format(current_safe)
    $ completed_combination_numbers[safe] = []
    $ combination_length = 0

    call screen scr_ep02_01_04_Safe_Cracking onlayer master

label lb_ep02_01_04_Safe_Cracking_Failed:
    #AFTER THE SAFE FAILED TO BE OPENED
    show sc mcfindgirld 048
    mc"(Damn it! I guess it wasn't [completed_combination_numbers[safe][0]]-[completed_combination_numbers[safe][1]]-[completed_combination_numbers[safe][2]]. I must have screwed it up.)"
    show sc mcfindgirld 049
    mc"(Lets try that again.)"

    $ completed_combination_numbers = {}
    call screen scr_ep02_01_04_Safe_Cracking onlayer master

label lb_ep02_01_04_Safe_Cracking_Fast:
    #If the user spins it too fast, show this screen to prevent bugs.
    show sc mcfindgirld 048
    "" with hpunch
    mc"(Woh, maybe I shouldn't be spinning it that fast.)"
    show sc mcfindgirld 049
    mc"(Lets try that again.)"
    $ completed_combination_numbers = {}
    call screen scr_ep02_01_04_Safe_Cracking onlayer master

label lb_ep02_01_04_Safe_Cracking_Success:
    #AFTER THE SAFE HAS BEEN OPEN
    play sound "sound effects/02/opening_a_small_safe_effect.mp3" noloop
    if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
        show screen scr_secret_icon("v_secrets_ep02_01_04_1") onlayer ontop
        with { "ontop": dissolve}
    show sc mcfindgirld 050
    mc"(Got it!!)"
    if v_ep02_01_04_Safe_Bypassed == False:
        mc"(Looks like it was [completed_combination_numbers[safe][0]]-[completed_combination_numbers[safe][1]]-[completed_combination_numbers[safe][2]].)"
    #Sound effect for the lock opening
    #the MC sees the flash drive inside the safe
    if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
        # BONUS IMAGE UNLOCKED IF SAFE UNLOCKED IN SINGLE ATTEMPT
        $ wallpaper_unlock(3)

    show sc mcfindgirld 055
    mc"(Ah! There it is!)"
    if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
        show sc mcfindgirld 051a
        show screen scr_secret_hotspot ("sc mcfindgirld 051a","767, 508, 236, 160","v_secrets_ep02_01_04_1")
    else:
        show sc mcfindgirld 051
    mc"(And now for \"operation decoy\"...)"
    menu:
        "Switch the drives"(wt="Future scene with Lucy + Task Point"):
            if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
                hide screen scr_secret_hotspot
            show sc mcfindgirld 053
            mc"(Nobody steals from me and gets away it.)"
            #the MC replaces the flash drive with the one Ariel gave him
            show sc mcfindgirld 054
            mc"(Well, there are exceptions. Mikayla, Tasha... The asshole that stole my bike!)"
            #The MC thinks and looks bemused
            if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
                show sc mcfindgirld 051a
            else:
                show sc mcfindgirld 051
            with dissolve
            pause 1.0
            show sc mcfindgirld 055
            with dissolve
            mc"(Anyway, if you go after the prince then you better make sure you kill him, bitch!)"
            $ v_ep02_task09_find_the_flash_drive += 1
            stop ambient fadeout 1.0
            #the MC closes the safe
            #screen goes blank
            if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
                hide screen scr_secret_icon onlayer ontop
                with { "ontop": dissolve}
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ v_ep02_01_04_Switch_The_Drives = True
            #Go down to SCENE CONTINUES

        "Steal the drive and leave a note"(wt="Future scene with Pretty Girl + Task Point"):
            if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
                hide screen scr_secret_hotspot
            show sc mcfindgirld 055
            mc"(On second thought, I've got a better idea...)"
            #the MC thinks and has a slight grin on his face
            show sc mcfindgirld 058
            with dissolve
            pause 1.0
            show sc mcfindgirld 059
            with dissolve
            pause 1.0
            $ v_ep02_task09_find_the_flash_drive += 1
            #He reaches inside his pocket and starts to write something on a post-it note - https://media.istockphoto.com/id/640004460/vector/vector-sticky-notes.jpg?s=612x612&w=0&k=20&c=pGmnA092VQfbxfdix-bgnwVJAxdD2QFe-5g8ukcmrbo=
            #you can reuse the above renders for MC closing the safe.
            #screen goes blank
            if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
                hide screen scr_secret_icon onlayer ontop
                with { "ontop": dissolve}
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ v_ep02_01_04_Leave_a_Note = True
            #Go down to SCENE CONTINUES


    #SCENE CONTINUES
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
    play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
    show sc mcfindgirld 060
    with dissolve
    mc"(Now, to find this stupid dildo.)"
    #show the room but with the shower door as an option to click on and also the bed to click on
    #(similar to the Vivian bedroom scene where you could click on the closet or under the bed)
    call screen scr_ep02_01_04_Punk_Girl_Room_Choices with Dissolve(0.2) onlayer master

    label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door:
        $ v_ep02_01_04_The_Shower = True
        show sc mcfindgirld 061
        with dissolve
        mc"(Hmm... I'd be crazy not to take a quick peep first.)"
        $ v_ep02_task09_find_the_flash_drive += 1
        #the MC moves closer to the shower door
        show sc mcfindgirld 062
        with dissolve
        mc"(I'll just open it slightly.)"
        #stop ambient fadeout 1.0
        #the MC's hand hovers over the door handle
        #the MC kneels down and looks through the keyhole
        #play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
        show sc mcfindgirld 063
        with dissolve
        mc"(Hot damn!)"
        #the MC sees the pretty girl from the party in the shower, naked
        #IMPORTANT - DO NOT SHOW HER FACE, ONLY SHOW HER BODY
        show sc mcfindgirld 064
        with dissolve
        pause 1.0
        #Options - breasts, ass, vagina, legs and the tattoo on her back

        show sc mcfindgirld 065
        with dissolve
        pause 1.0
        mc"(She might be a thief, but she's a stunning looking thief!)"
        #show a different part of her body - choose from the Options above

        show sc mcfindgirld 066
        with dissolve
        mc"(Okay, that's enough. A nice little bonus on top of getting the drive back!)"
        #show another different part of her body - choose from the Options above

        show sc mcfindgirld 067
        with dissolve
        mc"(Now to the other task at hand.)"
        #the MC stands up and looks around the room
        stop ambient fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
        show sc mcfindgirld 068
        with dissolve
        mc"(Hmm... It's not in here.)"
        #the MC checks her underwear drawer

        show sc mcfindgirld 069
        with dissolve
        mc"(Or here either.)"
        #the MC checks inside the closet

        show sc mcfindgirld 070
        with dissolve
        mc"(Dammit!)"
        #the MC looks frustrated
        mc"(If I were a hot chick, where would I hide a dildo like that??)"

        show sc mcfindgirld 071
        with dissolve
        mc"(Unless...)"
        #show the bed

        show sc mcfindgirld 072a
        with dissolve
        mc"(I wonder what that is?)"
        #the MC looks under one of her pillows
        show sc mcfindgirld 072b
        with dissolve
        pause 1.0
        show sc mcfindgirld 075a
        with dissolve
        pause 0.6
        show sc mcfindgirld 077
        with vpunch
        mc"(Woah!!)"
        mc"(This is it!)"
        #The MC picks it up and struggles

        if persistent.v_secrets_enabled and persistent.v_secrets_ep02_01_04_1 and v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
            show sc mcfindgirld 074a
            mc"(This thing is heavy!)"
            mc"(But something looks strange about it.)"
            #a slightly different expression on his face to above
            jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_NC
        else:
            show sc mcfindgirld 074
            mc"(This thing is heavy!)"
            #a slightly different expression on his face to above
            show sc mcfindgirld 075
            jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door_Continue


    label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Shelves:
        show sc mcfindgirld 068
        with dissolve
        mc"(Hmm... It's not in here.)"
        #the MC checks her underwear drawer

        show sc mcfindgirld 069
        with dissolve
        mc"(Or here either.)"
        #the MC checks inside the closet

        show sc mcfindgirld 070
        with dissolve
        mc"(Dammit!)"
        #the MC looks frustrated
        mc"(If I were a hot chick, where would I hide a dildo like that??)"

        show sc mcfindgirld 071
        with dissolve
        mc"(Unless...)"
        #show the bed

        show sc mcfindgirld 072a
        with dissolve
        mc"(I wonder what that is?)"
        #the MC looks under one of her pillows
        show sc mcfindgirld 072b
        with dissolve
        pause 1.0
        show sc mcfindgirld 075a
        with dissolve
        pause 0.6
        show sc mcfindgirld 077
        with vpunch
        mc"(Woah!!)"
        mc"(This is it!)"
        #The MC picks it up and struggles

        if persistent.v_secrets_enabled and persistent.v_secrets_ep02_01_04_1 and v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
            show sc mcfindgirld 074a
            mc"(This thing is heavy!)"
            mc"(But something looks strange about it.)"
            #a slightly different expression on his face to above
            jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_NC
        else:
            show sc mcfindgirld 074
            mc"(This thing is heavy!)"
            #a slightly different expression on his face to above
            show sc mcfindgirld 075
            jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door_Continue

    label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_NC:
        #IF THE PLAYER CLICKS ON A SPOT ON THE DILDO TO TRIGGER THE NC SCENE
        ###NON-CANON SCENE BEGINS
        if not _in_replay:
            scene black
            with flash(0.25, 0, 0.75, "#fff")
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            centered "15 minutes earlier...{w=2.0}{nw}" with dissolve
            show text "15 minutes earlier..."
            scene bg black with Dissolve(1)
            pause 1.0
            scene img_secret_scene_overlay onlayer anim_layer
            with { "anim_layer": dissolve}
        else:
            scene black
            with dissolve
            show screen scr_end_replay
        #The pretty girl from the party lays on her back on her bed
        #legs apart with the tip of the dildo rubbing against her pussy lips
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc rub
        else:
            show sc mcfindgirld nc 001
        with dissolve
        pretty_g"Mmm..."
        show sc mcfindgirld nc 002
        with Dissolve(0.2, alpha=True)
        pause 0.6
        show sc mcfindgirld nc 002a
        with Dissolve(0.2, alpha=True)
        pause 0.6
        show sc mcfindgirld nc 002b
        with Dissolve(0.2, alpha=True)
        pause 0.6
        show sc mcfindgirld nc 002c
        with vpunch
        with Dissolve(0.2, alpha=True)
        pretty_g"Oh God yes..."
        #animation of the dildo sliding into her pussy
        show sc mcfindgirld nc 003
        pretty_g"Holy shit!"
        #show her mouth opened wide
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo1
        else:
            show sc mcfindgirld nc 004
        pretty_g"(This thing is a lot bigger than I first realised!)"
        #show the dildo in between her legs
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo2
        else:
            show sc mcfindgirld nc 005
        pretty_g"Oh shit!"
        #show her clutching one of her breasts
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo3
        else:
            show sc mcfindgirld nc 006
        pretty_g"Yes!"
        #show the dildo half inside of her pussy
        pretty_g"Get that huge fucker in there!"
        #show her mouth wide open
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo4
        else:
            show sc mcfindgirld nc 007
        pretty_g"NGHH!!"
        #then show her mouth tightly closed
        pretty_g"(I'm so happy I got my hands on this thing.... literally!)"
        #show her with two hands on the dildo, working it in and out of her pussy
        #show pretty girl on all fours, fucking herself with the dildo
        scene black
        with dissolve
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo5
        else:
            show sc mcfindgirld nc 008
        with dissolve
        pretty_g"Oh fuck!!"
        pretty_g"UNGHH!!" with hpunch
        #animation of the dildo fucking her pussy - close up
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo7
        else:
            show sc mcfindgirld nc 010
        with hpunch
        pretty_g"Uhhh!!"
        #show her breasts hanging down
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo6
        else:
            show sc mcfindgirld nc 009
        with hpunch
        pretty_g"Oh yeah..."
        #show a shot from above pretty girl, of her ass and the dildo going into her pussy
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            show sc mcfindgirld nc dildo fall
        else:
            show sc mcfindgirld nc 011
        with vpunch
        pretty_g"(Holy shit...)"
        pretty_g"(That was amazing.)"
        #show the dildo on the bed between her legs, and the gape of her pussy
        show sc mcfindgirld nc store dildo
        with faster_dissolve
        pretty_g"(Damn...)"
        #She sits on the bed and puts the dildo in the box - the one the MC finds
        pretty_g"(I'm going to need to take a shower after that...)"
        #Final shot of Pretty Girl heading to the bathroom - show her up to her shoulders walking away from the bed
        $ persistent.replay_ep02_mysterygirl_fantasy = False
        $ v_ep01_mystery_girl_fantasy_counter += 1
        $ renpy.end_replay()
        scene onlayer anim_layer
        with { "anim_layer": dissolve}
        scene black
        with dissolve
        centered "Back to the present...{w=2.0}{nw}" with dissolve
        show text "Back to the present..."
        scene bg black with Dissolve(1)
        pause 1.0
        ###NON-CANON SCENE ENDS
        play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
        show sc mcfindgirld 075
        with dissolve
        jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door_Continue

    label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Door_Continue:
        mc"(Hmm...)"
        #the MC thinking face

        show sc mcfindgirld 076
        mc"(It's not just a golden dildo...)"
        #a slightly different expression on his face to above

        show sc mcfindgirld 077
        mc"(It's a dildo made out of GOLD!!)"
        #a look of realisation on his face

        show sc mcfindgirld 078
        mc"(No wonder Lucy wants this back so badly. It must be worth a fortune!)"
        #a slightly different expression on his face to above

        show sc mcfindgirld 079
        mc"(I better get out of here before this chick finishes her shower.)"

        show sc mcfindgirld 145
        with dissolve
        mc"({b}Now{/b} we're even, mystery girl...)"
        stop music fadeout 1.0
        #show the MC's face as he's leaving, he has a cocky smirk as he exits her front door
        stop ambient fadeout 1.0
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Bruno

label lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_Bruno:
    play ambient "sound effects/02/night_town_ambience.mp3" loop fadein 1.0
    show sc mcfindgirld 115
    with dissolve
    bruno"What the hell happened in there?"
    #Bruno stretches his arms out when he asks this

    show sc mcfindgirld 116
    bruno"What took you so long?"
    #bruno looks pissed off

    show sc mcfindgirld 117
    mc"Okay, okay, calm down."
    #the MC responds calmly

    show sc mcfindgirld 118
    mc"I got what you asked for, see?"
    #Bruno surveys the dildo

    show sc mcfindgirld 119
    bruno"Ah, terrific!"
    show sc mcfindgirld 029
    bruno"So, can you tell me which apartment she's staying in?"
    show sc mcfindgirld 028
    mc"Why is that important?"
    show sc mcfindgirld 010
    bruno"Because I'm gonna go up there, take her by surprise, and pop a cap in her ass!"
    show sc mcfindgirld 011
    mc"(Fuck...)"
    mc"(If this nutcase kills her, then it might get traced back to me.)"
    show sc mcfindgirld 006
    mc"(Plus I don't want this on my conscience.)"

    show sc mcfindgirld 012
    mc"Sorry to burst your bubble, but she took off shortly after I confronted her."

    show sc mcfindgirld 121
    bruno"Really?"
    #Bruno looks unconvinced

    show sc mcfindgirld 122
    mc"Well, I did mention that you were down here and that seemed to spook her."
    #bruno has a straight face while the MC speaks

    show sc mcfindgirld 123
    bruno"Is that right?"
    #bruno raises an eyebrow

    show sc mcfindgirld 125
    bruno"Well, I guess I can see why she would take off in a hurry."
    mc"(It was a little white lie, but it looks like he bought it.)"
    #Bruno is happy and talks himself up
    show sc mcfindgirld 124
    mc"And there was another way out of there after all."
    #reuse a render from above
    show sc mcfindgirld 123
    bruno"Yeah, she's pretty crafty that one."
    #reuse a render from above
    show sc mcfindgirld 122
    mc"So, are we cool now?"
    #reuse a render from above
    show sc mcfindgirld 125
    bruno"Yeah, we're good."
    #reuse a render from above

    show sc mcfindgirld 123
    bruno"I'll tell Lucy the great news."
    #bruno seems happy

    show sc mcfindgirld 126
    bruno"However..."
    #then changes his expression
    show sc mcfindgirld 125
    bruno"She also told me to tell you that she will be in touch."
    #reuse a render from above
    show sc mcfindgirld 121
    bruno"Make sure to answer if she calls, kid."
    #reuse a render from above
    #Bruno pulls the hoodie over his head to cover his face and walks away from the MC
    show sc mcfindgirld 121a
    with dissolve
    pause 1.0
    show sc mcfindgirld 128
    with dissolve
    mc"(Sigh...)"
    #The MC puts a hand to his chest as he breathes a sigh of relief "

    show sc mcfindgirld 129
    with dissolve
    mc"(Damn... I don't know how I managed to pull this off but it's one hell of a relief.)"
    #the MC looks at the flash drive
    if v_ep02_task09_find_the_flash_drive == 4:
        $ task_completed(9,"aa")
        $ v_ep02_ariel_aa_tasks_counter +=1
    if v_ep02_task09_find_the_flash_drive == 3:
        $ task_completed(9,"a")
    if v_ep02_task09_find_the_flash_drive == 2:
        $ task_completed(9,"b")
    if v_ep02_task09_find_the_flash_drive <= 1:
        $ task_completed(9,"c")
    show sc mcfindgirld 130
    mc"(Time to get on home so I can tell the others...)"
    #(screen goes blank)"
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    #return with a blank screen
    centered "10 minutes later...{w=2.0}{nw}" with dissolve
    show text "10 minutes later..."
    scene bg black with Dissolve(1)
    pause 1.0
    #this appears on the screen with the blank background
    show sc mcfindgirld 146
    with dissolve
    pretty_g"(Hmm... I was certain that the door was closed before I took a shower.)"
    #she looks concerned

    show sc mcfindgirld 147
    with dissolve
    pretty_g"(Something feels... off.)"
    show sc mcfindgirld 132
    with faster_dissolve
    pretty_g"(It's like I'm missing something.)"

    #"These lines if the player selected to "SWITCH THE DRIVES"
    if v_ep02_01_04_Switch_The_Drives == True:
        show sc mcfindgirld 137
        with dissolve
        pretty_g"(I better check the safe.)"
        play sound "sound effects/02/opening_a_small_safe_effect.mp3" noloop
        show sc mcfindgirld 138
        with dissolve
        pause 1.5
        #she looks at her safe
        stop sound fadeout 1.0

        if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
            show sc mcfindgirld 051a
        else:
            show sc mcfindgirld 051
        with dissolve
        pretty_g"(Hmm... The drive is still in here.)"

        show sc mcfindgirld 133
        with dissolve
        pretty_g"(I'm sure everything is fine.)"
        #She looks at the flash drive in her hand

        show sc mcfindgirld 149
        pretty_g"(So why do I have this feeling in my stomach that something is still wrong?)"
        show sc mcfindgirld 148
        pretty_g"(There's only one way to know for sure...)"
        scene black
        with dissolve
        scene black
        with Pause (2)

        show sc mcfindgirld 134
        with dissolve
        pause 1.0
        #She sits in front of her laptop and looks at the screen in shock
        show sc mcfindgirld 135
        with dissolve
        pause 1.0
        show sc mcfindgirld 136
        pretty_g"(GODDAMMIT! I knew it! The drive is blank!)"
        #She looks angry

        show sc mcfindgirld 150
        pretty_g"(But how?)"

        show sc mcfindgirld 151
        pretty_g"(Wait a second...)"

        show sc mcfindgirld 151a
        pretty_g"(The open door, an empty flash drive...)"

        show sc mcfindgirld 151
        pretty_g"(There's only one person who could've done this.)"
        #reuse a render from above

        show sc mcfindgirld 152
        pretty_g"(Oh, he is going to {b}pay{/b} for this!!)"
        #she looks furious and set on revenge
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_01_The_MC_returns_home_Vivian_waits_for_him


    #"These lines if the player selected to "LEAVE THE NOTE"
    if v_ep02_01_04_Leave_a_Note == True:
        show sc mcfindgirld 137
        pretty_g"(I better check the safe.)"
        #she looks at her safe
        play sound "sound effects/02/opening_a_small_safe_effect.mp3" noloop
        show sc mcfindgirld 138
        with faster_dissolve
        pretty_g"(I'm sure everything is fine, but I won't be able to sleep until I know for sure.)"
        #She opens the safe
        if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
            show sc mcfindgirld 056b
        else:
            show sc mcfindgirld 056a
        with faster_dissolve
        pretty_g"(What the hell is this? And where's the drive gone??)"
        #She picks up the note and reads it
        show sc mcfindgirld 140
        with faster_dissolve
        pretty_g"{i}You've been had, by the thief extraordinaire. Better luck next time!{/i}"
        show sc mcfindgirld flip card
        pretty_g"..."

        show sc mcfindgirld 153a
        with vpunch
        pretty_g"GODDAMMIT!"
        #She looks angry

        show sc mcfindgirld 138
        pretty_g"(But how??)"
        show sc mcfindgirld 139
        pretty_g"(Wait a second...)"
        if v_ep02_01_04_Cracking_Attempts == 1 and v_ep02_01_04_Safe_Bypassed == False:
            show sc mcfindgirld 056c
        else:
            show sc mcfindgirld 056
        pretty_g"(That explains why my front door was open.)"
        pretty_g"({b}He{/b} was in my apartment while I was showering!)"

        show sc mcfindgirld 142
        pretty_g"(Well despite that, I have to admit, I'm pretty impressed.)"

        show sc mcfindgirld 143
        pretty_g"(It's admirable just how cunning and confident he was to get in and out of here without me knowing.)"

        show sc mcfindgirld zoom out
        with dissolve
        pretty_g"(However, this is far from over...)"
        #she has a slight smile on her face
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_01_The_MC_returns_home_Vivian_waits_for_him



    ### SCENE BELOW REMOVED - 07/09/2024



    #         play ambient "sound effects/01/Shower_Sound_Effect_Reduced_Audio.ogg" loop fadein 1.0
    #         play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
    #         show sc mcfindgirld 068
    #         with dissolve
    #         mc"(Hmm... It's not in here.)"
    #         #the MC checks her underwear drawer

    #         show sc mcfindgirld 069
    #         with dissolve
    #         mc"(Or here either.)"
    #         #the MC checks inside the closet

    #         show sc mcfindgirld 070
    #         with dissolve
    #         mc"(Dammit!)"
    #         #the MC looks frustrated
    #         mc"(If I were a hot chick, where would I hide a dildo like that??)"

    #         show sc mcfindgirld 071
    #         with dissolve
    #         mc"(Unless...)"
    #         #show the bed

    #         show sc mcfindgirld 072a
    #         with dissolve
    #         mc"(I wonder what that is?)"
    #         #the MC looks under one of her pillows
    #         show sc mcfindgirld 072b
    #         with dissolve
    #         pause 1.0

    #         show sc mcfindgirld 077
    #         with vpunch
    #         mc"(Woah!!)"
    #         #The MC picks it up and struggles
    #         show sc mcfindgirld 074
    #         mc"(This thing is heavy!)"
    #         #a slightly different expression on his face to above

    #         show sc mcfindgirld 075
    #         mc"(Hmm...)"
    #         #the MC thinking face
    #         stop ambient fadeout 1.0

    #         show sc mcfindgirld 076
    #         mc"(It's not just a golden dildo.)"
    #         #a slightly different expression on his face to above

    #         show sc mcfindgirld 077
    #         mc"(It's a dildo made out of GOLD!!)"
    #         #a look of realisation on his face

    #         show sc mcfindgirld 078
    #         mc"(No wonder Lucy wants this back so badly. It must be worth a fortune!)"
    #         #a slightly different expression on his face to above

    #         show sc mcfindgirld 079
    #         mc"(I should sneak back out of here before I get-)"

    #         show sc mcfindgirld 077
    #         pretty_g"Freeze!"
    #         stop music fadeout 1.0
    #         play sound "sound effects/01/record_scratch.ogg" noloop
    #         show sc mcfindgirld 080
    #         mc"(Caught...)"
    #         #the pretty girl points a gun at the MC. She has a towel around her waist, and also around her head (IMPORTANT) - https://pixhost.to/show/38/488507443_sc-vivshower-v60.jpg

    #         show sc mcfindgirld 081
    #         pretty_g"Turn around... Slowly."
    #         #The MC turns around with his hands up and the golden dildo in one hand
    #         show sc mcfindgirld 082
    #         with dissolve
    #         pause 1.0

    #         show sc mcfindgirld 083
    #         with dissolve
    #         mc"A gun, seriously?"
    #         #pretty girl with a closed mouth
    #         show sc mcfindgirld 084
    #         pretty_g"Hey, a girl's gotta protect herself, especially in this town."
    #         #reuse a render from above

    #         show sc mcfindgirld 085
    #         pretty_g"I see that your nose has shrunk since we last ran into each other."
    #         #she's calm because she recognises him

    #         show sc mcfindgirld 081
    #         pretty_g"I take it you've been telling fewer lies since then, huh?"

    #         show sc mcfindgirld 086
    #         mc"I'm not the only one who hasn't been telling the truth."

    #         show sc mcfindgirld 087
    #         pretty_g"Yeah, well... Some of us are simply better at hiding our true selves than others."
    #         #She gives a sexy smirk

    #         show sc mcfindgirld 088
    #         mc"(Damn, that's cold.)"
    #         #The MC looks bothered by that remark

    #         show sc mcfindgirld 089
    #         pretty_g"What do you want with that dildo?"
    #         #she has a quizzical look on her face

    #         show sc mcfindgirld 090
    #         mc"I was asked to steal it."
    #         mc"Does the name Lucy, ring any bells?"
    #         #reuse a render from above

    #         show sc mcfindgirld 081
    #         pretty_g"Shit..."
    #         #she seems agitated
    #         show sc mcfindgirld 089
    #         pretty_g"Why would you do that for her?"
    #         #reuse a render from above

    #         show sc mcfindgirld 092
    #         mc"Let's just say that I owed her one."
    #         #MC acts calm
    #         show sc mcfindgirld 080
    #         pretty_g"You know I could just shoot you, right?"
    #         #reuse a render from above
    #         show sc mcfindgirld 083
    #         mc"You could..."
    #         #reuse a render from above

    #         show sc mcfindgirld 093
    #         mc"But that won't solve anything."

    #         show sc mcfindgirld 094
    #         mc"Especially with one of her guys downstairs who is expecting me to return."
    #         #the MC looks towards the window

    #         show sc mcfindgirld 095
    #         mc"I take it you know Bruno."
    #         #he looks back at the girl

    #         show sc mcfindgirld 091
    #         pretty_g"Oh yeah. We know each other pretty well."
    #         #reuse a render from above
    #         show sc mcfindgirld 089
    #         mc"So it looks like we're at a stalemate."
    #         #reuse a render from above

    #         show sc mcfindgirld 096
    #         mc"Unless, of course..."
    #         #his expression is slightly different to the one above
    #         show sc mcfindgirld 084
    #         pretty_g"Unless what?"
    #         #reuse a render from above
    #         show sc mcfindgirld 089
    #         mc"You let me go, and I'll buy you some time to escape."
    #         #reuse a render from above
    #         mc"There's more than one way out of here, contrary to what I've been told, yes?"
    #         #reuse a render from above
    #         show sc mcfindgirld 085
    #         pretty_g"There is."
    #         #reuse a render from above
    #         show sc mcfindgirld 081
    #         pretty_g"But why would you help me?"
    #         #reuse a render from above
    #         show sc mcfindgirld 097
    #         mc"Because I'd also like to get out of here without any problems."
    #         #reuse a render from above
    #         show sc mcfindgirld 096
    #         mc"Is that a good enough reason?"
    #         #reuse a render from above
    #         show sc mcfindgirld 091
    #         pretty_g"I guess..."
    #         #reuse a render from above
    #         show sc mcfindgirld 085
    #         pretty_g"So Lucy wants her dildo back, huh?"
    #         #reuse a render from above
    #         show sc mcfindgirld 087
    #         pretty_g"Okay, fine... Take it to her."
    #         #reuse a render from above
    #         show sc mcfindgirld 092
    #         mc"Seriously? Just like that?"
    #         #reuse a render from above
    #         show sc mcfindgirld 093
    #         mc"Why?"
    #         #reuse a render from above
    #         show sc mcfindgirld 081
    #         pretty_g"I have my own reasons, which are none of your business."
    #         #reuse a render from above

    #         show sc mcfindgirld 097
    #         mc"Damn, grouchy much?"
    #         #the MC sounds annoyed

    #         show sc mcfindgirld 080
    #         pretty_g"Leave from here slowly, so I can get changed and still have enough time to get a head start on Bruno."
    #         #reuse a render from above

    #         show sc mcfindgirld 098
    #         mc"Sure, I can do that."
    #         #The MC makes it to her door as she continues to point the gun at him

    #         #they switch sides to where they are in the room so the pretty girl is standing near the safe
    #         show sc mcfindgirld 099
    #         with dissolve
    #         pretty_g"But before you go, I'll be taking that flash drive that you have on you."
    #         #girl has a serious face

    #         show sc mcfindgirld 100
    #         mc"What flash drive?"
    #         #the MC pretends to not know what she's talking about

    #         show sc mcfindgirld 101
    #         pretty_g"Don't play dumb with me."

    #         show sc mcfindgirld 102
    #         pretty_g"Do you seriously think I'm going to buy that you came all this way just to help Lucy?"

    #         show sc mcfindgirld 100
    #         pretty_g"I wasn't born yesterday."
    #         #reuse a render from above #reuse 101

    #         show sc mcfindgirld 103
    #         pretty_g"Now hand it over!"
    #         #she looks angry and demanding

    #         #"These lines if the player selected to "SWITCH THE DRIVES"
    #         if v_ep02_01_04_Switch_The_Drives == True:
    #             show sc mcfindgirld 106
    #             mc"I swear that I don't have it on me."
    #             #mc looks worried
    #             mc"You hid it so well that I had no time to find it."
    #             #reuse a render from above

    #             show sc mcfindgirld 106
    #             pretty_g"Hmm..."
    #             #girl looks suspicious
    #             show sc mcfindgirld 099
    #             pretty_g"Stay right where you are, and keep your hands where I can see them."
    #             #reuse a render from above #can reuse 099
    #             play sound "sound effects/02/opening_a_small_safe_effect.mp3" noloop
    #             show sc mcfindgirld 107
    #             with dissolve
    #             pause 1.0
    #             #pretty girl goes over to her safe, and she's still pointing the gun at him
    #             #she opens the safe and sees the flash drive still in there - SOUND EFFECT

    #             show sc mcfindgirld 108
    #             with dissolve
    #             pretty_g"(Hmm... So he was telling the truth.)"
    #             #she thinks, has her mouth closed

    #             show sc mcfindgirld 109
    #             mc"Ah, so that's where it was."
    #             #the MC looks over at where she is and responds

    #             show sc mcfindgirld 110
    #             pretty_g"Yeah, and you won't be getting this back."
    #             #She holds it in her other hand while she still points the gun at him

    #             mc"(Little does she know...)"
    #             #the MC has his mouth closed, smiling

    #             show sc mcfindgirld 112
    #             pretty_g"Now get the hell out of here!"

    #             show sc mcfindgirld 113
    #             mc"Aye, aye... Mystery girl!"
    #             #the MC mocks her by giving her a salute - https://dictionary.cambridge.org/images/thumb/salute_noun_002_32004.jpg?version=6.0.25

    #             show sc mcfindgirld 114a
    #             mc"({b}Now{/b}, we're even...)"
    #             #show the MC's face as he's leaving, he has a cocky smirk while the pretty girl is in the background, looking sceptical like something is wrong

    #             #screen goes blank
    #             scene black
    #             with dissolve
    #             scene black
    #             with Pause (2)
    #             jump lb_ep02_01_04_Final_Chat_With_Bruno



    #         #"These lines if the player selected to "LEAVE THE NOTE":
    #         if v_ep02_01_04_Leave_a_Note == True:
    #             show sc mcfindgirld 106
    #             mc"(Shit! I've already taken the flash drive out of the safe.)"
    #             #the MC looks worries
    #             show sc mcfindgirld 104
    #             mc"(However, I still have the decoy on me.)"
    #             #mc cheeky smile

    #             show sc mcfindgirld 100
    #             mc"Ugh... Fine."
    #             #the MC reaches inside his pocket for the dud flash drive

    #             show sc mcfindgirld 106
    #             mc"Here."
    #             #the MC throws the drive at her which she catches
    #             show sc mcfindgirld 110a
    #             with dissolve
    #             pretty_g"Hmm..."
    #             #she looks at it closely

    #             show sc mcfindgirld 110
    #             pretty_g"I bet you thought you'd got away with it, huh?"
    #             #reuse a render from above

    #             show sc mcfindgirld 104
    #             pretty_g"You see, some people are amateur thieves, and the rest of us are already in the big leagues like yours truly."
    #             #she's really cocky about her \"win\"

    #             show sc mcfindgirld 110
    #             pretty_g"You were so close, too..."
    #             show sc mcfindgirld 104
    #             mc"(If only I could be here when the penny drops and she realises how stupid she sounds right now.)"
    #             show sc mcfindgirld 112

    #             pretty_g"Now get the hell out of here!"
    #             show sc mcfindgirld 113

    #             mc"Aye, aye... Mystery girl!"
    #             #the MC mocks her by giving her a salute - https://dictionary.cambridge.org/images/thumb/salute_noun_002_32004.jpg?version=6.0.25
    #             show sc mcfindgirld 114a
    #             mc"({b}Now{/b} we're even...)"
    #             #show the MC's face as he's leaving, he has a cocky smirk while the pretty girl is in the background, looking sceptical like something is wrong

    #             #screen goes blank
    #             scene black
    #             with dissolve
    #             scene black
    #             with Pause (2)
    #             jump lb_ep02_01_04_Final_Chat_With_Bruno


    #         label lb_ep02_01_04_Final_Chat_With_Bruno:
    #             #Scene continues with the MC exiting the apartment block
    #             play ambient "sound effects/02/night_town_ambience.mp3" loop fadein 1.0
    #             show sc mcfindgirld 115
    #             bruno"What the hell happened in there?"
    #             #Bruno stretches his arms out when he asks this

    #             show sc mcfindgirld 116
    #             bruno"What took you so long?"
    #             #bruno looks pissed off

    #             show sc mcfindgirld 117
    #             mc"Okay, okay, calm down."
    #             #the MC responds calmly

    #             show sc mcfindgirld 118
    #             mc"I got what you asked for, see?"
    #             #Bruno surveys the dildo

    #             show sc mcfindgirld 119
    #             bruno"Ah, terrific!"
    #             show sc mcfindgirld 029
    #             bruno"And what about the girl? Did you see or speak to her?"

    #             show sc mcfindgirld 120
    #             mc"Um... She took off shortly after I confronted her."

    #             show sc mcfindgirld 121
    #             bruno"Really?"
    #             #Bruno looks unconvinced

    #             show sc mcfindgirld 122
    #             mc"Well, I did mention that you were down here and that seemed to spook her."
    #             #bruno has a straight face while the MC speaks

    #             show sc mcfindgirld 123
    #             bruno"Is that right?"
    #             #bruno raises an eyebrow

    #             show sc mcfindgirld 125
    #             bruno"Well, I guess I can see why she would take off in a hurry."
    #             #Bruno is happy and talks himself up
    #             show sc mcfindgirld 124
    #             mc"And there was another way out of there after all."
    #             #reuse a render from above
    #             show sc mcfindgirld 123
    #             bruno"Yeah, she's pretty crafty that one."
    #             #reuse a render from above
    #             show sc mcfindgirld 122
    #             mc"So, are we cool now?"
    #             #reuse a render from above
    #             show sc mcfindgirld 125
    #             bruno"Yeah, we're good."
    #             #reuse a render from above

    #             show sc mcfindgirld 123
    #             bruno"I'll tell Lucy the great news."
    #             #bruno seems happy
    #             show sc mcfindgirld 126
    #             bruno"However..."
    #             #then changes his expression
    #             show sc mcfindgirld 125
    #             bruno"She also told me to tell you that she will be in touch."
    #             #reuse a render from above
    #             show sc mcfindgirld 121
    #             bruno"Make sure to answer if she calls, kid."
    #             #reuse a render from above

    #             #Bruno pulls the hoodie over his head to cover his face and walks away from the MC

    #             show sc mcfindgirld 128
    #             mc"(Sigh...)"
    #             #The MC puts a hand to his chest as he breathes a sigh of relief "

    #             show sc mcfindgirld 129
    #             mc"(Damn... I don't know how I managed to pull this off but it's one hell of a relief.)"
    #             #the MC looks at the flash drive

    #             show sc mcfindgirld 130
    #             mc"(Time to get on home so I can tell the others...)"
    #             #(screen goes blank)"
    #             stop ambient fadeout 1.0
    #             scene black
    #             with dissolve
    #             scene black
    #             with Pause (2)

    #             #return with a blank screen

    #             "Meanwhile, at the apartment block..."
    #             #this appears on the screen with the blank background

    #             show sc mcfindgirld 131
    #             #pretty girl looks out from her apartment window
    #             pretty_g"(Looks like they're leaving.)"

    #             show sc mcfindgirld 132
    #             pretty_g"(Still, I shouldn't stay here any longer, in case they come back.)"
    #             #she turns her head slightly compared to the image above

    #             #"These lines if the player selected to "SWITCH THE DRIVES"
    #             if v_ep02_01_04_Switch_The_Drives == True:
    #                 show sc mcfindgirld 107
    #                 pretty_g"(Hmm... Something seems off about the way that guy just handed the drive back to me without a fight.)"
    #                 #she looks at her safe
    #                 show sc mcfindgirld 133
    #                 pretty_g"(I better check this out.)"
    #                 #She looks at the flash drive in her hand
    #                 with dissolve
    #                 show sc mcfindgirld 134
    #                 pretty_g"(Oh...!!)"
    #                 #She sits in front of her laptop and looks at the screen in shock
    #                 show sc mcfindgirld 135
    #                 pretty_g"(GOD DAMMIT! The drive is blank!)"
    #                 #She looks angry
    #                 pretty_g"(He must have switched it, as the drive I looked at last night, definitely had data and information on it.)"
    #                 show sc mcfindgirld 136
    #                 pretty_g"(Oh, he is going to {b}pay{/b} for this!!)"
    #                 #she looks furious and set on revenge
    #                 #screen goes blank
    #                 scene black
    #                 with dissolve
    #                 scene black
    #                 with Pause (2)
    #                 jump lb_ep02_02_01_The_MC_returns_home_Vivian_waits_for_him


    #             #"These lines if the player selected to "LEAVE THE NOTE"
    #             if v_ep02_01_04_Leave_a_Note == True:
    #                 show sc mcfindgirld 137
    #                 pretty_g"(Hmm... I better store this away. And change the code on the safe.)"
    #                 play sound "sound effects/02/opening_a_small_safe_effect.mp3" noloop
    #                 show sc mcfindgirld 056a
    #                 with dissolve
    #                 pretty_g"(Huh?)"
    #                 #she opens the safe and sees a Post-it note in there

    #                 show sc mcfindgirld 140
    #                 pretty_g"(What the hell is this?)"
    #                 #She picks up the note and reads it

    #                 show sc mcfindgirld 139
    #                 pretty_g"You've been had, by [y_name], thief extraordinaire. Better luck next time!"
    #                 pretty_g"Winking, smiley face."

    #                 show sc mcfindgirld 153a
    #                 pretty_g"GODDAMMIT!"

    #                 #She looks angry

    #                 show sc mcfindgirld 142
    #                 with dissolve
    #                 pretty_g"(I have to say though, I'm pretty impressed.)"

    #                 show sc mcfindgirld 143
    #                 pretty_g"(It's admirable how cunning and confident he was to get in and out of here without me knowing.)"

    #                 show sc mcfindgirld 142
    #                 pretty_g"(But this is far from over.... [y_name].)"
    #                 #she has a slight smile on her face
    #                 #screen goes blank
    #                 scene black
    #                 with dissolve
    #                 scene black
    #                 with Pause (2)
    #                 jump lb_ep02_02_01_The_MC_returns_home_Vivian_waits_for_him

    # #######################################################################


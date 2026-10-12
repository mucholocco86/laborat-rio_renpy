init:
    $ v_ep03_04_03_levers_minigame_giveup = False
#############################################################################
# Buttonscreen basically shows all buttons depending to their current state
#############################################################################
screen button_screen():
    python:
        #########################################################################################
        # in function toggle(pos) goes the magic. This defines which buttons toggle which others
        #########################################################################################
        def toggle(pos):
            if pos == 0:
                lamps[0] = abs(lamps[0]-1)
                lamps[1] = abs(lamps[1]-1)
                lamps[2] = abs(lamps[2]-1)
            if pos == 1:
                lamps[1] = abs(lamps[1]-1)
                lamps[5] = abs(lamps[5]-1)
            if pos == 2:
                lamps[2] = abs(lamps[2]-1)
                lamps[8] = abs(lamps[8]-1)
                lamps[6] = abs(lamps[6]-1)
            if pos == 3:
                lamps[3] = abs(lamps[3]-1)
                lamps[6] = abs(lamps[6]-1)
            if pos == 4:
                lamps[4] = abs(lamps[4]-1)
                lamps[2] = abs(lamps[2]-1)
                lamps[7] = abs(lamps[7]-1)
            if pos == 5:
                lamps[5] = abs(lamps[5]-1)
                lamps[3] = abs(lamps[3]-1)
            if pos == 6:
                lamps[6] = abs(lamps[6]-1)
                lamps[0] = abs(lamps[0]-1)
                lamps[3] = abs(lamps[3]-1)
            if pos == 7:
                lamps[7] = abs(lamps[7]-1)
                lamps[3] = abs(lamps[3]-1)
            if pos == 8:
                lamps[8] = abs(lamps[8]-1)
                lamps[4] = abs(lamps[4]-1)
                lamps[0] = abs(lamps[0]-1)

##############################################################################
# Following part are all buttons - either shown green or red
##############################################################################
#Row 1
    if lamps[0] == 0:
        button:
            action [Function(toggle,0), Return()]
            xpos 780
            ypos 365
            xsize 80
            ysize 80
    elif lamps[0] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,0), Return()]
            xpos 780
            ypos 365

    if lamps[1] == 0:
        button:
            action [Function(toggle,1), Return()]
            xpos 920
            ypos 365
            xsize 80
            ysize 80
    elif lamps[1] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,1), Return()]
            xpos 920
            ypos 365

    if lamps[2] == 0:
        button:
            action [Function(toggle,2), Return()]
            xpos 1060
            ypos 365
            xsize 80
            ysize 80
    elif lamps[2] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,2), Return()]
            xpos 1060
            ypos 365
# Row 2
    if lamps[3] == 0:
        button:
            action [Function(toggle,3), Return()]
            xpos 780
            ypos 530
            xsize 80
            ysize 80
    elif lamps[3] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,3), Return()]
            xpos 780
            ypos 530

    if lamps[4] == 0:
        button:
            action [Function(toggle,4), Return()]
            xpos 920
            ypos 530
            xsize 80
            ysize 80
    elif lamps[4] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,4), Return()]
            xpos 920
            ypos 530

    if lamps[5] == 0:
        button:
            action [Function(toggle,5), Return()]
            xpos 1060
            ypos 530
            xsize 80
            ysize 80
    elif lamps[5] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,5), Return()]
            xpos 1060
            ypos 530
# Row 3
    if lamps[6] == 0:
        button:
            action [Function(toggle,6), Return()]
            xpos 780
            ypos 690
            xsize 80
            ysize 80
    elif lamps[6] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,6), Return()]
            xpos 780
            ypos 690

    if lamps[7] == 0:
        button:
            action [Function(toggle,7), Return()]
            xpos 920
            ypos 690
            xsize 80
            ysize 80
    elif lamps[7] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,7), Return()]
            xpos 920
            ypos 690

    if lamps[8] == 0:
        button:
            action [Function(toggle,8), Return()]
            xpos 1060
            ypos 690
            xsize 80
            ysize 80
    elif lamps[8] == 1:
        imagebutton:
            idle "bg/levers/redbutton.jpg"
            hover "bg/levers/redbutton.jpg"
            action [Function(toggle,8), Return()]
            xpos 1060
            ypos 690

# NEED to adjust style of textbuttons
    vbox:
        textbutton " Skip the mini-game" action [SetVariable("quit", True), SetVariable("v_ep03_04_03_levers_minigame_giveup", True), Return()]
        textbutton " Reset the mini-game" action [SetVariable("reset",True), Return()]



############################################################################################################
# main label to start the Minigame - you'll need to rename it, or change it to a screen or whatever else
############################################################################################################
label lb_ep3_levers_minigame:

    $ quit = False
    $ lamps = [1,1,1,1,1,1,1,1,1]

    image bg background = "bg/levers/levers_background.jpg"  #stonewall from labyrinth minigame

#make it fullscreen, as i cur it out from another render
    transform stretch_fullscreen:
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height
    scene bg background  at stretch_fullscreen
##########################################################
    show buttonpanel_red  # base panel, all lights are red

    "Try to change all of the buttons to the color green and you will be to be able to turn the laser beams off."

    show buttonpanel  # all buttons are green, they will have layover in red if not active

    while quit == False:    # stay in minigame until either solved, or quit button
        $ reset = False     # reset is used to restart the game
        call screen button_screen   # go into button screen where you can toggle buttons
        if reset == True:
            $ lamps = [1,1,1,1,1,1,1,1,1]   # if reset wanted, the lights are reset zo default
        if lamps == [0,0,0,0,0,0,0,0,0]:  # if this condition is made, all lights are green and riddle is solved
            $ quit = True

    play sound "sound effects/03/laser_beam_success_jingle.mp3" noloop
    "Well done! The laser beams are now turned off."
    if v_ep03_04_03_levers_minigame_giveup == False:
        $ wallpaper_unlock(5)

    jump lb_ep03_04_03_The_Art_Gallery_Heist_Part_2_continues

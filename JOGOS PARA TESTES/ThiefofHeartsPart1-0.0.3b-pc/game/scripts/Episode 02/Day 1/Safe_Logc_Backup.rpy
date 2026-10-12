init:
    $ v_ep02_01_04_Switch_The_Drives = False
    $ v_ep02_01_04_Leave_a_Note = False
    default v_ep02_01_04_Attempts = 0
    default v_ep02_01_04_Pass = 0
    default v_ep02_01_04_Selected_Pin_Number = 0
    default v_ep02_01_04_Final_Pin_Number = ""
    default v_ep02_01_04_Selected_Random_Number = 0
    default count = 0

    image sc mcfindgirld dial blur right:
        "sc mcfindgirld 049 dial blur 01"
        pause 0.4
        "sc mcfindgirld 049 dial blur 02"
        pause 0.4
        "sc mcfindgirld 049 dial blur 03"
        pause 0.4
        "sc mcfindgirld 049 dial blur 04"
        pause 0.4
        "sc mcfindgirld 049 dial blur 05"
        pause 0.4
        "sc mcfindgirld 049 dial blur 06"
        pause 0.4
        "sc mcfindgirld 049 dial blur 07"
        pause 0.4
        "sc mcfindgirld 049 dial blur 08"
        pause 0.4
        repeat

    image sc mcfindgirld dial blur left:
        "sc mcfindgirld 049 dial blur 08"
        pause 0.4
        "sc mcfindgirld 049 dial blur 07"
        pause 0.4
        "sc mcfindgirld 049 dial blur 06"
        pause 0.4
        "sc mcfindgirld 049 dial blur 05"
        pause 0.4
        "sc mcfindgirld 049 dial blur 04"
        pause 0.4
        "sc mcfindgirld 049 dial blur 03"
        pause 0.4
        "sc mcfindgirld 049 dial blur 02"
        pause 0.4
        "sc mcfindgirld 049 dial blur 01"
        pause 0.4
        repeat

    screen scr_ep02_01_04_Safe_Cracking_Old:
        zorder -10
        add "sc mcfindgirld 049 safe bg"
        add "sc mcfindgirld 049 dial 01" xalign 0.494 yalign 0.498

        textbutton "START":
            text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
            xalign 0.5
            yalign 0.1
            focus_mask True
            action [SetVariable("v_ep02_01_04_Selected_Pin_Number",0),SetVariable("v_ep02_01_04_Pass",0),Play("sound2","sound effects/02/safe_tumbler_clicks_loop.ogg",loop=True),Hide("scr_ep02_01_04_Safe_Cracking"),Show("scr_ep02_01_04_Safe_Cracking_Start"),Jump("BeginCrackSafe")]

    screen scr_ep02_01_04_Safe_Cracking_Start_Old:
        zorder -10
        add "sc mcfindgirld 049 safe bg"
        if (v_ep02_01_04_Pass == 1):
            add "sc mcfindgirld dial blur left" xalign 0.494 yalign 0.498
        else:
            add "sc mcfindgirld dial blur right" xalign 0.494 yalign 0.498
        text "[Number]"
        text "Current Numbers: [v_ep02_01_04_Final_Pin_Number]" xalign 0.5 yalign 0.9
        textbutton "STOP":
            text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
            xalign 0.5
            yalign 0.7
            focus_mask True
            action [Stop("sound2"),Hide("scr_ep02_01_04_Safe_Cracking_Start_Old"),
                SetVariable("v_ep02_01_04_Selected_Pin_Number",Number),SetVariable("v_ep02_01_04_Pass",v_ep02_01_04_Pass+1),Jump("BeginCrackSafe")
                ]

label nextNumber:
    $ numberTest = False
    label get_number:
        $ Number = renpy.random.randint(1, 9)
        $ if Number not in numberList: numberTest = True
        if numberTest:
            $ numberList.append(Number)
            return
        else:
            jump get_number

label BeginCrackSafe:
    $ renpy.block_rollback()
    $ numberList = []
    $ count = 0

    label numberStart:
        $ count +=1
        if count == 10:
            stop sound2
            hide screen scr_ep02_01_04_Safe_Cracking_Start_Old
            jump lb_ep02_01_04_Safe_Timed_Out
        call nextNumber
        if v_ep02_01_04_Selected_Pin_Number == 0:
            if (Number == 4 and v_ep02_01_04_Pass == 0) or (Number == 2 and v_ep02_01_04_Pass == 1) or (Number == 1 and v_ep02_01_04_Pass == 2):
                play sound3 "sound effects/02/safe_tumbler_locking_into_place.ogg"
            pause 2.0
        else:
            $ v_ep02_01_04_Final_Pin_Number = str(v_ep02_01_04_Final_Pin_Number) + str(v_ep02_01_04_Selected_Pin_Number)

            if (v_ep02_01_04_Final_Pin_Number == "421"):
                hide screen scr_ep02_01_04_Safe_Cracking_Start_Old
                jump lb_ep02_01_04_Safe_Cracking_Success
            elif (len(v_ep02_01_04_Final_Pin_Number) < 3):
                $ v_ep02_01_04_Selected_Pin_Number = 0
                play sound2 "sound effects/02/safe_tumbler_clicks_loop.ogg" loop
                show screen scr_ep02_01_04_Safe_Cracking_Start_Old
                jump BeginCrackSafe
            elif (len(v_ep02_01_04_Final_Pin_Number) == 3):
                hide screen scr_ep02_01_04_Safe_Cracking_Start_Old
                jump lb_ep02_01_04_Safe_Cracking_Failed
        jump numberStart

label lb_ep02_01_04_Safe_Cracking_Failed_old:

    $ renpy.block_rollback()
    show sc mcfindgirld 048
    mc "(Damn it! I must have screwed it up.)"
    show sc mcfindgirld 049
    mc "(Lets try that again.)"
    $ v_ep02_01_04_Selected_Pin_Number = 0
    $ v_ep02_01_04_Pass = 0
    $ v_ep02_01_04_Final_Pin_Number = ""
    $ v_ep02_01_04_Attempts =+ 1
    scene sc mcfindgirld 049 safe bg
    call screen scr_ep02_01_04_Safe_Cracking

label lb_ep02_01_04_Safe_Timed_Out:

    $ renpy.block_rollback()
    show sc mcfindgirld 048
    mc "(Damnit, I didn't stop the dial in time.)"
    show sc mcfindgirld 049
    mc "(Lets try that again.)"
    $ v_ep02_01_04_Selected_Pin_Number = 0
    $ v_ep02_01_04_Pass = 0
    $ v_ep02_01_04_Final_Pin_Number = ""
    $ v_ep02_01_04_Attempts =+ 1
    scene sc mcfindgirld 049 safe bg
    call screen scr_ep02_01_04_Safe_Cracking
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

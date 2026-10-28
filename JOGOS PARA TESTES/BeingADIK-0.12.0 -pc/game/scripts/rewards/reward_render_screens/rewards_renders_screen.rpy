screen rewards_renders_screen:
    tag rewards_renders_screen
    modal True
    key "mouseup_2" action (SetVariable("tmpBool2", False),SetVariable("tmpBool", False),SetVariable("toggled_2d_mode", 1),Hide("rewards_renders_screen"))
    add "rewards_new_bg"
    if rewards_renders_list[tmpInt][tmpInt2][1]:
        $ rewards_mark_seen(tmpInt, tmpInt2,toggled_2d_mode)
        if tmpInt == 4:
            if tmpInt2 < len(new_art_girl_name_list):
                if toggled_2d_mode == 1:
                    add rewards_renders_list[tmpInt][tmpInt2][0][0]
                elif toggled_2d_mode == 2:
                    add rewards_renders_list[tmpInt][tmpInt2][0][1]
                else:
                    add rewards_renders_list[tmpInt][tmpInt2][0][2]
                if persistent.rewards_screen_on_hover:
                    imagebutton:
                        idle Transform ("rew_button_prox2")
                        hovered SetVariable("tmpBool2", True)
                        unhovered SetVariable("tmpBool2", False)
                        action NullAction()
                hbox:
                    xalign 0.02
                    yalign 0.02
                    if (persistent.rewards_screen_on_hover and tmpBool2) or not persistent.rewards_screen_on_hover:
                        if toggled_2d_mode == 1:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                idle "toggle_2d_clothed"
                                hover "toggle_2d_clothed"
                                action NullAction()
                        else:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                idle "toggle_2d_clothed_idle"
                                hover "toggle_2d_clothed_hover"
                                action SetVariable("toggled_2d_mode", 1)
                        if toggled_2d_mode == 2:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                idle "toggle_2d_partial"
                                hover "toggle_2d_partial"
                                action NullAction()
                        else:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                if persistent.art_unlocked_lvl2[tmpInt2]:
                                    idle "toggle_2d_partial_idle"
                                    hover "toggle_2d_partial_hover"
                                    action SetVariable("toggled_2d_mode", 2)
                                else:
                                    idle "toggle_2d_partial_disabled"
                                    hover "toggle_2d_partial_disabled"
                                    action NullAction()
                        if toggled_2d_mode == 3:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                idle "toggle_2d_nude"
                                hover "toggle_2d_nude"
                                action NullAction()
                        else:
                            imagebutton:
                                hovered SetVariable("tmpBool2", True)
                                if persistent.art_unlocked_lvl3[tmpInt2]:
                                    idle "toggle_2d_nude_idle"
                                    hover "toggle_2d_nude_hover"
                                    action SetVariable("toggled_2d_mode", 3)
                                else:
                                    idle "toggle_2d_nude_disabled"
                                    hover "toggle_2d_nude_disabled"
                                    action NullAction()
            else:
                if rewards_renders_list[tmpInt][tmpInt2][0][-1] != "a":
                    add rewards_renders_list[tmpInt][tmpInt2][0]
                else:
                    if toggled_2d_mode == 1:
                        add "%s" % rewards_renders_list[tmpInt][tmpInt2][0]
                    else:
                        add "%sb" % rewards_renders_list[tmpInt][tmpInt2][0][0:-1]
                    if persistent.rewards_screen_on_hover:
                        imagebutton:
                            idle Transform ("rew_button_prox2")
                            hovered SetVariable("tmpBool2", True)
                            unhovered SetVariable("tmpBool2", False)
                            action NullAction()
                    hbox:
                        xalign 0.02
                        yalign 0.02
                        if (persistent.rewards_screen_on_hover and tmpBool2) or not persistent.rewards_screen_on_hover:
                            if tmpInt2 != 34:
                                if toggled_2d_mode == 2:
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_clothed_idle"
                                        hover "toggle_2d_clothed_hover"
                                        action SetVariable("toggled_2d_mode", 1)
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_nude"
                                        hover "toggle_2d_nude"
                                        action SetVariable("toggled_2d_mode", 1)
                                else:
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_clothed"
                                        hover "toggle_2d_clothed"
                                        action SetVariable("toggled_2d_mode", 2)
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_nude_idle"
                                        hover "toggle_2d_nude_hover"
                                        action SetVariable("toggled_2d_mode", 2)
                            else:
                                if toggled_2d_mode == 2:
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_nocum_idle"
                                        hover "toggle_2d_nocum_hover"
                                        action SetVariable("toggled_2d_mode", 1)
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_cum"
                                        hover "toggle_2d_cum"
                                        action SetVariable("toggled_2d_mode", 1)
                                else:
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_nocum"
                                        hover "toggle_2d_nocum"
                                        action SetVariable("toggled_2d_mode", 2)
                                    imagebutton:
                                        hovered SetVariable("tmpBool2", True)
                                        idle "toggle_2d_cum_idle"
                                        hover "toggle_2d_cum_hover"
                                        action SetVariable("toggled_2d_mode", 2)
        elif tmpInt == 1 and tmpInt2 > 0 and tmpInt2 < 9:
            add rewards_renders_list[tmpInt][tmpInt2][0]
            if toggled_2d_mode != 2:
                add "%s_border" % rewards_renders_list[tmpInt][tmpInt2][0]
            if persistent.rewards_screen_on_hover:
                imagebutton:
                    idle Transform ("rew_button_prox2")
                    hovered SetVariable("tmpBool2", True)
                    unhovered SetVariable("tmpBool2", False)
                    action NullAction()
            hbox:
                xalign 0.02
                yalign 0.02
                if (persistent.rewards_screen_on_hover and tmpBool2) or not persistent.rewards_screen_on_hover:
                    if toggled_2d_mode == 2:
                        imagebutton:
                            hovered SetVariable("tmpBool2", True)
                            idle "toggle_2d_text_idle"
                            hover "toggle_2d_text_hover"
                            action SetVariable("toggled_2d_mode", 1)
                        imagebutton:
                            hovered SetVariable("tmpBool2", True)
                            idle "toggle_2d_notext"
                            hover "toggle_2d_notext"
                            action SetVariable("toggled_2d_mode", 1)
                    else:
                        imagebutton:
                            hovered SetVariable("tmpBool2", True)
                            idle "toggle_2d_text"
                            hover "toggle_2d_text"
                            action SetVariable("toggled_2d_mode", 2)
                        imagebutton:
                            hovered SetVariable("tmpBool2", True)
                            idle "toggle_2d_notext_idle"
                            hover "toggle_2d_notext_hover"
                            action SetVariable("toggled_2d_mode", 2)
        else:
            add rewards_renders_list[tmpInt][tmpInt2][0]
    else:
        add "locked_reward"

    if persistent.rewards_screen_on_hover:
        imagebutton:
            xalign 0.99
            yalign 0.00
            idle Transform ("rew_x_idle_prox")
            hover Transform ("rew_x_hover_prox")
            action NullAction()
        imagebutton:
            xalign 0.99
            yalign 0.00
            idle Transform ("rew_x_invis")
            hover Transform ("rew_x_hover")
            action (SetVariable("toggled_2d_mode",1),Hide("rewards_renders_screen"))
    else:
        imagebutton:
            xalign 0.99
            yalign 0.00
            idle Transform ("rew_x_idle")
            hover Transform ("rew_x_hover")
            action (SetVariable("toggled_2d_mode",1),Hide("rewards_renders_screen"))

    if persistent.rewards_screen_on_hover:
        hbox:
            xalign 0.99
            yalign 0.99
            spacing 0 * persistent.scale_factor
            imagebutton:
                idle Transform ("rew_button_prox")
                hovered SetVariable("tmpBool", True)
                unhovered SetVariable("tmpBool", False)
                action NullAction()
    hbox:
        xalign 0.99
        yalign 0.99
        spacing 0 * persistent.scale_factor
        if (persistent.rewards_screen_on_hover and tmpBool) or not persistent.rewards_screen_on_hover:
            imagebutton:
                if tmpInt2 == 0:
                    idle Transform ("rew_button_prev_disabled")
                    hover Transform ("rew_button_prev_disabled")
                else:
                    idle Transform ("rew_button_prev_idle")
                    hover Transform ("rew_button_prev_hover")
                hovered SetVariable("tmpBool", True)
                xoffset 5 * persistent.scale_factor
                action (SetVariable("toggled_2d_mode",1),SetVariable("tmpInt2",max(tmpInt2-1,0)))
            imagebutton:
                hovered SetVariable("tmpBool", True)
                if tmpInt2 == len(rewards_renders_list[tmpInt])-1:
                    idle Transform ("rew_button_next_disabled")
                    hover Transform ("rew_button_next_disabled")
                    action NullAction()
                else:
                    idle Transform ("rew_button_next_idle")
                    hover Transform ("rew_button_next_hover")
                    action (SetVariable("toggled_2d_mode",1),SetVariable("tmpInt2",tmpInt2+1))

init:
    if persistent.rewards_seen_list == None:
        $ persistent.rewards_seen_list = []
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
        $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
    else:

        if len(persistent.rewards_seen_list) > 10:
            $ persistent.rewards_seen_list = []
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])
            $ persistent.rewards_seen_list.append([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True])



        if len(persistent.rewards_seen_list[4]) < 51:
            python:
                persistent.rewards_seen_list[4].insert(10, [True,True,True])
                persistent.rewards_seen_list[4].insert(15, [True,True,True])
                for i in range(0,12):
                    persistent.rewards_seen_list[4].append(True)
        if len(persistent.rewards_seen_list[-1]) < 16:
            python:
                for i in range(0,8):
                    persistent.rewards_seen_list[-1].append(True)
        if len(persistent.rewards_seen_list[1]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[1].append(True)
        if len(persistent.rewards_seen_list[2]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[2].append(True)

        if len(persistent.rewards_seen_list[4]) < 59:
            python:
                for i in range(0,8):
                    persistent.rewards_seen_list[4].append(True)
        if len(persistent.rewards_seen_list[-1]) < 24:
            python:
                for i in range(0,8):
                    persistent.rewards_seen_list[-1].append(True)
        if len(persistent.rewards_seen_list[5]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[5].append(True)

        if len(persistent.rewards_seen_list[6]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[6].append(True)


        if len(persistent.rewards_seen_list[4]) < 63:
            python:
                for i in range(0,4):
                    persistent.rewards_seen_list[4].append(True)

        if len(persistent.rewards_seen_list[7]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[7].append(True)
        if len(persistent.rewards_seen_list[3]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[3].append(True)
        if len(persistent.rewards_seen_list[-1]) < 36:
            python:
                for i in range(0,12):
                    persistent.rewards_seen_list[-1].append(True)


        if len(persistent.rewards_seen_list[4]) < 68:
            python:
                for i in range(0,5):
                    persistent.rewards_seen_list[4].append(True)

        if len(persistent.rewards_seen_list[0]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[0].append(True)

        if len(persistent.rewards_seen_list[8]) < 20:
            python:
                for i in range(0,20):
                    persistent.rewards_seen_list[8].append(True)

        if len(persistent.rewards_seen_list[9]) < 50:
            python:
                for i in range(0,14):
                    persistent.rewards_seen_list[9].append(True)
        if len(persistent.rewards_seen_list[9]) > 50:
            $ persistent.rewards_seen_list[9] = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
init python:
    def updateRewardLists():
        global rewards_renders_list
        global tmpBool
        
        tmpBool = False
        rewards_renders_list = []
        
        tmpList = []
        tmpList.append(["ep12_reward_isabella1",persistent.ep12_cardisa1])
        tmpList.append(["ep12_reward_isabella2",persistent.ep12_cardisa2])
        tmpList.append(["ep12_reward_isabella3",persistent.ep12_cardisa3])
        tmpList.append(["ep12_reward_isabella4",persistent.ep12_cardisa4])
        tmpList.append(["ep12_reward_isabella5",persistent.ep12_cardisa5])
        tmpList.append(["ep12_reward_isabella6",persistent.ep12_cardisa6])
        tmpList.append(["ep12_reward_isabella7",persistent.ep12_cardisa7])
        tmpList.append(["ep12_reward_isabella8",persistent.ep12_cardisa8])
        tmpList.append(["ep12_reward_isabella9",persistent.ep12_cardisa9])
        tmpList.append(["ep12_reward_isabella10",persistent.ep12_cardisa10])
        tmpList.append(["ep12_reward_isabella11",persistent.ep12_cardisa11])
        tmpList.append(["ep12_reward_isabella12",persistent.ep12_cardisa12])
        tmpList.append(["ep12_reward_isabella13",persistent.ep12_cardisa13])
        tmpList.append(["ep12_reward_isabella14",persistent.ep12_cardisa14])
        tmpList.append(["ep12_reward_isabella15",persistent.ep12_cardisa15])
        tmpList.append(["ep12_reward_isabella16",persistent.ep12_cardisa16])
        tmpList.append(["ep12_reward_isabella17",persistent.ep12_cardisa17])
        tmpList.append(["ep12_reward_isabella18",persistent.ep12_cardisa18])
        tmpList.append(["ep12_reward_isabella19",persistent.ep12_cardisa19])
        tmpList.append(["ep12_reward_isabella20",persistent.ep12_cardisa20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep9_reward_jill1",persistent.ep9_cardji1])
        tmpList.append(["ep9_reward_jill2",persistent.ep9_cardji2])
        tmpList.append(["ep9_reward_jill3",persistent.ep9_cardji3])
        tmpList.append(["ep9_reward_jill4",persistent.ep9_cardji4])
        tmpList.append(["ep9_reward_jill5",persistent.ep9_cardji5])
        tmpList.append(["ep9_reward_jill6",persistent.ep9_cardji6])
        tmpList.append(["ep9_reward_jill7",persistent.ep9_cardji7])
        tmpList.append(["ep9_reward_jill8",persistent.ep9_cardji8])
        tmpList.append(["ep9_reward_jill9",persistent.ep9_cardji9])
        tmpList.append(["ep9_reward_jill10",persistent.ep9_cardji10])
        tmpList.append(["ep9_reward_jill11",persistent.ep9_cardji11])
        tmpList.append(["ep9_reward_jill12",persistent.ep9_cardji12])
        tmpList.append(["ep9_reward_jill13",persistent.ep9_cardji13])
        tmpList.append(["ep9_reward_jill14",persistent.ep9_cardji14])
        tmpList.append(["ep9_reward_jill15",persistent.ep9_cardji15])
        tmpList.append(["ep9_reward_jill16",persistent.ep9_cardji16])
        tmpList.append(["ep9_reward_jill17",persistent.ep9_cardji17])
        tmpList.append(["ep9_reward_jill18",persistent.ep9_cardji18])
        tmpList.append(["ep9_reward_jill19",persistent.ep9_cardji19])
        tmpList.append(["ep9_reward_jill20",persistent.ep9_cardji20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep9_reward_josy1",persistent.ep9_cardjo1])
        tmpList.append(["ep9_reward_josy2",persistent.ep9_cardjo2])
        tmpList.append(["ep9_reward_josy3",persistent.ep9_cardjo3])
        tmpList.append(["ep9_reward_josy4",persistent.ep9_cardjo4])
        tmpList.append(["ep9_reward_josy5",persistent.ep9_cardjo5])
        tmpList.append(["ep9_reward_josy6",persistent.ep9_cardjo6])
        tmpList.append(["ep9_reward_josy7",persistent.ep9_cardjo7])
        tmpList.append(["ep9_reward_josy8",persistent.ep9_cardjo8])
        tmpList.append(["ep9_reward_josy9",persistent.ep9_cardjo9])
        tmpList.append(["ep9_reward_josy10",persistent.ep9_cardjo10])
        tmpList.append(["ep9_reward_josy11",persistent.ep9_cardjo11])
        tmpList.append(["ep9_reward_josy12",persistent.ep9_cardjo12])
        tmpList.append(["ep9_reward_josy13",persistent.ep9_cardjo13])
        tmpList.append(["ep9_reward_josy14",persistent.ep9_cardjo14])
        tmpList.append(["ep9_reward_josy15",persistent.ep9_cardjo15])
        tmpList.append(["ep9_reward_josy16",persistent.ep9_cardjo16])
        tmpList.append(["ep9_reward_josy17",persistent.ep9_cardjo17])
        tmpList.append(["ep9_reward_josy18",persistent.ep9_cardjo18])
        tmpList.append(["ep9_reward_josy19",persistent.ep9_cardjo19])
        tmpList.append(["ep9_reward_josy20",persistent.ep9_cardjo20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep11_reward_maya1",persistent.ep11_cardmy1])
        tmpList.append(["ep11_reward_maya2",persistent.ep11_cardmy2])
        tmpList.append(["ep11_reward_maya3",persistent.ep11_cardmy3])
        tmpList.append(["ep11_reward_maya4",persistent.ep11_cardmy4])
        tmpList.append(["ep11_reward_maya5",persistent.ep11_cardmy5])
        tmpList.append(["ep11_reward_maya6",persistent.ep11_cardmy6])
        tmpList.append(["ep11_reward_maya7",persistent.ep11_cardmy7])
        tmpList.append(["ep11_reward_maya8",persistent.ep11_cardmy8])
        tmpList.append(["ep11_reward_maya9",persistent.ep11_cardmy9])
        tmpList.append(["ep11_reward_maya10",persistent.ep11_cardmy10])
        tmpList.append(["ep11_reward_maya11",persistent.ep11_cardmy11])
        tmpList.append(["ep11_reward_maya12",persistent.ep11_cardmy12])
        tmpList.append(["ep11_reward_maya13",persistent.ep11_cardmy13])
        tmpList.append(["ep11_reward_maya14",persistent.ep11_cardmy14])
        tmpList.append(["ep11_reward_maya15",persistent.ep11_cardmy15])
        tmpList.append(["ep11_reward_maya16",persistent.ep11_cardmy16])
        tmpList.append(["ep11_reward_maya17",persistent.ep11_cardmy17])
        tmpList.append(["ep11_reward_maya18",persistent.ep11_cardmy18])
        tmpList.append(["ep11_reward_maya19",persistent.ep11_cardmy19])
        tmpList.append(["ep11_reward_maya20",persistent.ep11_cardmy20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append([["ep7_reward_2d_camila","ep8_reward_2d_camila_2","ep12_reward_2d_camila_3"],persistent.art_unlocked_lvl1[0]])
        tmpList.append([["ep7_reward_2d_cathy","ep11_reward_2d_cathy_2",""],persistent.art_unlocked_lvl1[1]])
        tmpList.append([["ep7_reward_2d_envy","ep8_reward_2d_envy_2","ep11_reward_2d_envy_3"],persistent.art_unlocked_lvl1[2]])
        tmpList.append([["ep7_reward_2d_isabella","ep10_reward_2d_isabella_2",""],persistent.art_unlocked_lvl1[3]])
        tmpList.append([["ep7_reward_2d_jade","ep9_reward_2d_jade_2",""],persistent.art_unlocked_lvl1[4]])
        tmpList.append([["ep7_reward_2d_jill","ep10_reward_2d_jill_2",""],persistent.art_unlocked_lvl1[5]])
        tmpList.append([["ep7_reward_2d_josy","ep10_reward_2d_josy_2",""],persistent.art_unlocked_lvl1[6]])
        tmpList.append([["ep7_reward_2d_lily","ep8_reward_2d_lily_2","ep11_reward_2d_lily_3"],persistent.art_unlocked_lvl1[7]])
        tmpList.append([["ep7_reward_2d_maya","ep9_reward_2d_maya_2",""],persistent.art_unlocked_lvl1[8]])
        tmpList.append([["ep7_reward_2d_melanie","ep9_reward_2d_melanie_2","ep12_reward_2d_melanie_3"],persistent.art_unlocked_lvl1[9]])
        tmpList.append([["ep9_reward_2d_nora","ep11_reward_2d_nora_2",""],persistent.art_unlocked_lvl1[10]])
        tmpList.append([["ep7_reward_2d_quinn","ep8_reward_2d_quinn_2",""],persistent.art_unlocked_lvl1[11]])
        tmpList.append([["ep7_reward_2d_riona","ep8_reward_2d_riona_2",""],persistent.art_unlocked_lvl1[12]])
        tmpList.append([["ep7_reward_2d_sage","ep10_reward_2d_sage_2",""],persistent.art_unlocked_lvl1[13]])
        tmpList.append([["ep7_reward_2d_sarah","ep8_reward_2d_sarah_2","ep12_reward_2d_sarah_3"],persistent.art_unlocked_lvl1[14]])
        tmpList.append([["ep9_reward_2d_zoey","ep12_reward_2d_zoey_2",""],persistent.art_unlocked_lvl1[15]])
        
        tmpList.append(["ep7_wallpaper_isabella_1a",persistent.ep7_wpi1])
        tmpList.append(["ep7_wallpaper_isabella_2a",persistent.ep7_wpi2])
        tmpList.append(["ep7_wallpaper_jill_1a",persistent.ep7_wpj1])
        tmpList.append(["ep7_wallpaper_jill_2a",persistent.ep7_wpj2])
        tmpList.append(["ep7_wallpaper_josy_1a",persistent.ep7_wpjo1])
        tmpList.append(["ep7_wallpaper_josy_2a",persistent.ep7_wpjo2])
        tmpList.append(["ep7_wallpaper_maya_1a",persistent.ep7_wpm1])
        tmpList.append(["ep7_wallpaper_maya_2a",persistent.ep7_wpm2])
        tmpList.append(["ep7_wallpaper_sage_1a",persistent.ep7_wps1])
        tmpList.append(["ep7_wallpaper_sage_2a",persistent.ep7_wps2])
        tmpList.append(["ep8_wallpaper_isabella_1a",persistent.ep8_wpi1])
        tmpList.append(["ep8_wallpaper_jill_1a",persistent.ep8_wpj1])
        tmpList.append(["ep8_wallpaper_josy_1a",persistent.ep8_wpjo1])
        tmpList.append(["ep8_wallpaper_maya_1a",persistent.ep8_wpm1])
        tmpList.append(["ep8_wallpaper_quinn_1a",persistent.ep8_wpq1])
        tmpList.append(["ep8_wallpaper_sage_1a",persistent.ep8_wps1])
        tmpList.append(["ep8_wallpaper_envy_1a",persistent.ep8_wpe1])
        tmpList.append(["ep8_wallpaper_jade_1a",persistent.ep8_wpjade1])
        tmpList.append(["ep8_wallpaper_madame_1a",persistent.ep8_wpmad1])
        
        tmpList.append(["epi_wallpaper_zoey_1a",persistent.epi_card1])
        tmpList.append(["epi_wallpaper_zoey_2a",persistent.epi_card2])
        tmpList.append(["epi_wallpaper_zoey_3",persistent.epi_card3])
        tmpList.append(["epi_wallpaper_zoey_4",persistent.epi_card4])
        
        tmpList.append(["ep9_wallpaper_camila_1a",persistent.ep9_card1])
        tmpList.append(["ep9_wallpaper_jill_1a",persistent.ep9_card2])
        tmpList.append(["ep9_wallpaper_jill_2",persistent.ep9_card3])
        tmpList.append(["ep9_wallpaper_josy_1a",persistent.ep9_card4])
        tmpList.append(["ep9_wallpaper_josy_2",persistent.ep9_card5])
        tmpList.append(["ep9_wallpaper_maya_1a",persistent.ep9_card6])
        tmpList.append(["ep9_wallpaper_maya_2",persistent.ep9_card7])
        tmpList.append(["ep9_wallpaper_riona_1a",persistent.ep9_card8])
        
        tmpList.append(["ep9_wallpaper_riona_2",persistent.ep9_card17])
        tmpList.append(["ep9_wallpaper_riona_3a",persistent.ep9_card18])
        tmpList.append(["ep9_wallpaper_lily_1",persistent.ep9_card19])
        tmpList.append(["ep9_wallpaper_lily_2a",persistent.ep9_card20])
        
        tmpList.append(["ep10_wallpaper_cathy_1a",persistent.ep10_card13])
        tmpList.append(["ep10_wallpaper_cathy_2",persistent.ep10_card14])
        tmpList.append(["ep10_wallpaper_envy_1a",persistent.ep10_card15])
        tmpList.append(["ep10_wallpaper_envy_2",persistent.ep10_card16])
        tmpList.append(["ep10_wallpaper_quinn_1a",persistent.ep10_card11])
        tmpList.append(["ep10_wallpaper_quinn_2",persistent.ep10_card12])
        tmpList.append(["ep10_wallpaper_nora_1a",persistent.ep10_card9])
        tmpList.append(["ep10_wallpaper_nora_2",persistent.ep10_card10])
        
        tmpList.append(["ep11_wallpaper_isabella_2",persistent.ep11_card9])
        tmpList.append(["ep11_wallpaper_isabella_1a",persistent.ep11_card10])
        tmpList.append(["ep11_wallpaper_sage_2",persistent.ep11_card11])
        tmpList.append(["ep11_wallpaper_sage_1a",persistent.ep11_card12])
        
        tmpList.append(["ep12_wallpaper_josy_2",persistent.ep12_card15])
        tmpList.append(["ep12_wallpaper_josy_1a",persistent.ep12_card16])
        tmpList.append(["ep12_wallpaper_maya_2",persistent.ep12_card17])
        tmpList.append(["ep12_wallpaper_maya_1a",persistent.ep12_card18])
        tmpList.append(["2d_jb_elena1",persistent.ep12_card19])
        
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep10_reward_sage1",persistent.ep10_cardsa1])
        tmpList.append(["ep10_reward_sage2",persistent.ep10_cardsa2])
        tmpList.append(["ep10_reward_sage3",persistent.ep10_cardsa3])
        tmpList.append(["ep10_reward_sage4",persistent.ep10_cardsa4])
        tmpList.append(["ep10_reward_sage5",persistent.ep10_cardsa5])
        tmpList.append(["ep10_reward_sage6",persistent.ep10_cardsa6])
        tmpList.append(["ep10_reward_sage7",persistent.ep10_cardsa7])
        tmpList.append(["ep10_reward_sage8",persistent.ep10_cardsa8])
        tmpList.append(["ep10_reward_sage9",persistent.ep10_cardsa9])
        tmpList.append(["ep10_reward_sage10",persistent.ep10_cardsa10])
        tmpList.append(["ep10_reward_sage11",persistent.ep10_cardsa11])
        tmpList.append(["ep10_reward_sage12",persistent.ep10_cardsa12])
        tmpList.append(["ep10_reward_sage13",persistent.ep10_cardsa13])
        tmpList.append(["ep10_reward_sage14",persistent.ep10_cardsa14])
        tmpList.append(["ep10_reward_sage15",persistent.ep10_cardsa15])
        tmpList.append(["ep10_reward_sage16",persistent.ep10_cardsa16])
        tmpList.append(["ep10_reward_sage17",persistent.ep10_cardsa17])
        tmpList.append(["ep10_reward_sage18",persistent.ep10_cardsa18])
        tmpList.append(["ep10_reward_sage19",persistent.ep10_cardsa19])
        tmpList.append(["ep10_reward_sage20",persistent.ep10_cardsa20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep10_reward_zoey1",persistent.ep10_cardzo1])
        tmpList.append(["ep10_reward_zoey2",persistent.ep10_cardzo2])
        tmpList.append(["ep10_reward_zoey3",persistent.ep10_cardzo3])
        tmpList.append(["ep10_reward_zoey4",persistent.ep10_cardzo4])
        tmpList.append(["ep10_reward_zoey5",persistent.ep10_cardzo5])
        tmpList.append(["ep10_reward_zoey6",persistent.ep10_cardzo6])
        tmpList.append(["ep10_reward_zoey7",persistent.ep10_cardzo7])
        tmpList.append(["ep10_reward_zoey8",persistent.ep10_cardzo8])
        tmpList.append(["ep10_reward_zoey9",persistent.ep10_cardzo9])
        tmpList.append(["ep10_reward_zoey10",persistent.ep10_cardzo10])
        tmpList.append(["ep10_reward_zoey11",persistent.ep10_cardzo11])
        tmpList.append(["ep10_reward_zoey12",persistent.ep10_cardzo12])
        tmpList.append(["ep10_reward_zoey13",persistent.ep10_cardzo13])
        tmpList.append(["ep10_reward_zoey14",persistent.ep10_cardzo14])
        tmpList.append(["ep10_reward_zoey15",persistent.ep10_cardzo15])
        tmpList.append(["ep10_reward_zoey16",persistent.ep10_cardzo16])
        tmpList.append(["ep10_reward_zoey17",persistent.ep10_cardzo17])
        tmpList.append(["ep10_reward_zoey18",persistent.ep10_cardzo18])
        tmpList.append(["ep10_reward_zoey19",persistent.ep10_cardzo19])
        tmpList.append(["ep10_reward_zoey20",persistent.ep10_cardzo20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep11_reward_lily1",persistent.ep11_cardly1])
        tmpList.append(["ep11_reward_lily2",persistent.ep11_cardly2])
        tmpList.append(["ep11_reward_lily3",persistent.ep11_cardly3])
        tmpList.append(["ep11_reward_lily4",persistent.ep11_cardly4])
        tmpList.append(["ep11_reward_lily5",persistent.ep11_cardly5])
        tmpList.append(["ep11_reward_lily6",persistent.ep11_cardly6])
        tmpList.append(["ep11_reward_lily7",persistent.ep11_cardly7])
        tmpList.append(["ep11_reward_lily8",persistent.ep11_cardly8])
        tmpList.append(["ep11_reward_lily9",persistent.ep11_cardly9])
        tmpList.append(["ep11_reward_lily10",persistent.ep11_cardly10])
        tmpList.append(["ep11_reward_lily11",persistent.ep11_cardly11])
        tmpList.append(["ep11_reward_lily12",persistent.ep11_cardly12])
        tmpList.append(["ep11_reward_lily13",persistent.ep11_cardly13])
        tmpList.append(["ep11_reward_lily14",persistent.ep11_cardly14])
        tmpList.append(["ep11_reward_lily15",persistent.ep11_cardly15])
        tmpList.append(["ep11_reward_lily16",persistent.ep11_cardly16])
        tmpList.append(["ep11_reward_lily17",persistent.ep11_cardly17])
        tmpList.append(["ep11_reward_lily18",persistent.ep11_cardly18])
        tmpList.append(["ep11_reward_lily19",persistent.ep11_cardly19])
        tmpList.append(["ep11_reward_lily20",persistent.ep11_cardly20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["ep12_reward_camila1",persistent.ep12_cardcam1])
        tmpList.append(["ep12_reward_camila2",persistent.ep12_cardcam2])
        tmpList.append(["ep12_reward_camila3",persistent.ep12_cardcam3])
        tmpList.append(["ep12_reward_camila4",persistent.ep12_cardcam4])
        tmpList.append(["ep12_reward_camila5",persistent.ep12_cardcam5])
        tmpList.append(["ep12_reward_camila6",persistent.ep12_cardcam6])
        tmpList.append(["ep12_reward_camila7",persistent.ep12_cardcam7])
        tmpList.append(["ep12_reward_camila8",persistent.ep12_cardcam8])
        tmpList.append(["ep12_reward_camila9",persistent.ep12_cardcam9])
        tmpList.append(["ep12_reward_camila10",persistent.ep12_cardcam10])
        tmpList.append(["ep12_reward_camila11",persistent.ep12_cardcam11])
        tmpList.append(["ep12_reward_camila12",persistent.ep12_cardcam12])
        tmpList.append(["ep12_reward_camila13",persistent.ep12_cardcam13])
        tmpList.append(["ep12_reward_camila14",persistent.ep12_cardcam14])
        tmpList.append(["ep12_reward_camila15",persistent.ep12_cardcam15])
        tmpList.append(["ep12_reward_camila16",persistent.ep12_cardcam16])
        tmpList.append(["ep12_reward_camila17",persistent.ep12_cardcam17])
        tmpList.append(["ep12_reward_camila18",persistent.ep12_cardcam18])
        tmpList.append(["ep12_reward_camila19",persistent.ep12_cardcam19])
        tmpList.append(["ep12_reward_camila20",persistent.ep12_cardcam20])
        rewards_renders_list.append(tmpList)
        
        tmpList = []
        tmpList.append(["epi_reward_cr_1",persistent.epi_card5])
        tmpList.append(["epi_reward_cr_2",persistent.epi_card6])
        tmpList.append(["epi_reward_cr_3",persistent.epi_card7])
        tmpList.append(["epi_reward_cr_4",persistent.epi_card8])
        tmpList.append(["epi_reward_cr_5",persistent.epi_card9])
        tmpList.append(["epi_reward_cr_6",persistent.epi_card10])
        tmpList.append(["epi_reward_cr_7",persistent.epi_card11])
        tmpList.append(["epi_reward_cr_8",persistent.epi_card12])
        
        tmpList.append(["ep9_reward_cr_1",persistent.ep9_card9])
        tmpList.append(["ep9_reward_cr_2",persistent.ep9_card10])
        tmpList.append(["ep9_reward_cr_3",persistent.ep9_card11])
        tmpList.append(["ep9_reward_cr_4",persistent.ep9_card12])
        tmpList.append(["ep9_reward_cr_5",persistent.ep9_card13])
        tmpList.append(["ep9_reward_cr_6",persistent.ep9_card14])
        tmpList.append(["ep9_reward_cr_7",persistent.ep9_card15])
        tmpList.append(["ep9_reward_cr_8",persistent.ep9_card16])
        
        tmpList.append(["ep10_reward_cr_1",persistent.ep10_card1])
        tmpList.append(["ep10_reward_cr_2",persistent.ep10_card2])
        tmpList.append(["ep10_reward_cr_3",persistent.ep10_card3])
        tmpList.append(["ep10_reward_cr_4",persistent.ep10_card4])
        tmpList.append(["ep10_reward_cr_5",persistent.ep10_card5])
        tmpList.append(["ep10_reward_cr_6",persistent.ep10_card6])
        tmpList.append(["ep10_reward_cr_7",persistent.ep10_card7])
        tmpList.append(["ep10_reward_cr_8",persistent.ep10_card8])
        
        tmpList.append(["ep11_reward_cr_1",persistent.ep11_card1])
        tmpList.append(["ep11_reward_cr_2",persistent.ep11_card2])
        tmpList.append(["ep11_reward_cr_3",persistent.ep11_card3])
        tmpList.append(["ep11_reward_cr_4",persistent.ep11_card4])
        tmpList.append(["ep11_reward_cr_5",persistent.ep11_card5])
        tmpList.append(["ep11_reward_cr_6",persistent.ep11_card6])
        tmpList.append(["ep11_reward_cr_7",persistent.ep11_card7])
        tmpList.append(["ep11_reward_cr_8",persistent.ep11_card8])
        tmpList.append(["ep11_reward_cr_9",persistent.ep11_card9b])
        tmpList.append(["ep11_reward_cr_10",persistent.ep11_card10b])
        tmpList.append(["ep11_reward_cr_11",persistent.ep11_card11b])
        tmpList.append(["ep11_reward_cr_12",persistent.ep11_card12b])
        
        tmpList.append(["ep12_reward_cr_1",persistent.ep12_card1])
        tmpList.append(["ep12_reward_cr_2",persistent.ep12_card2])
        tmpList.append(["ep12_reward_cr_3",persistent.ep12_card3])
        tmpList.append(["ep12_reward_cr_4",persistent.ep12_card4])
        tmpList.append(["ep12_reward_cr_5",persistent.ep12_card5])
        tmpList.append(["ep12_reward_cr_6",persistent.ep12_card6])
        tmpList.append(["ep12_reward_cr_7",persistent.ep12_card7])
        tmpList.append(["ep12_reward_cr_8",persistent.ep12_card8])
        tmpList.append(["ep12_reward_cr_9",persistent.ep12_card9])
        tmpList.append(["ep12_reward_cr_10",persistent.ep12_card10])
        tmpList.append(["ep12_reward_cr_11",persistent.ep12_card11])
        tmpList.append(["ep12_reward_cr_12",persistent.ep12_card12])
        tmpList.append(["ep12_reward_cr_13",persistent.ep12_card13])
        tmpList.append(["ep12_reward_cr_14",persistent.ep12_card14])
        rewards_renders_list.append(tmpList)
        return

init python:
    def rewards_mark_seen(x, y, z):
        global new_art_girl_name_list
        
        if x == 4 and y < len(new_art_girl_name_list):
            if z == 1:
                persistent.rewards_seen_list[x][y][0] = False
            elif z == 2:
                persistent.rewards_seen_list[x][y][1] = False
            else:
                persistent.rewards_seen_list[x][y][2] = False
        else:
            persistent.rewards_seen_list[x][y] = False
        return

style reward_new_style:
    font "fonts/cabin-regular.ttf"
    color "#ffed00"
    size 30 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]
    xoffset 120 * persistent.scale_factor
    yoffset -150 * persistent.scale_factor
    xalign 0.5
    yalign 0.5
    ypos 0.5
    yminimum 100 * persistent.scale_factor

style reward_locked_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    size 30 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]
    xalign 0.5
    yalign 0.5
    ypos 0.5
    yminimum 100 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

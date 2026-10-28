label ep9_freeroam_diks_ph2_label:
$ freeRoamID = "ep9_2"
show screen wt_tasks_shown
$ roosterState = "ep9_2"
$ tmpInt = 0
$ guideSuggestedPage = 63

$ found_money = False
$ found_money2 = False
$ studied = False

$ disabled_apps = []
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

$ rooster_jump_label = "ep9_diks_ph2_main_label"

$ map_system_list = []
$ map_system_list.append(["ep9_diks_ph1_lib_mid","ep9_diks_ph2_lib_mid_label","Your room"])
$ map_system_list.append(["ep9_diks_ph2_derek","ep9_diks_ph2_derek_label","Derek's room"])
$ map_system_list.append(["ep9_diks_ph2_dining","ep9_diks_ph2_dining_label","Dining room"])
$ map_system_list.append(["ep9_diks_ph2_jacob","ep9_diks_ph2_jacob_label","Jacob's room"])
$ map_system_list.append(["ep9_diks_ph1_jamie","ep9_diks_ph2_jamie_label","Jamie's room"])
$ map_system_list.append(["ep9_diks_ph1_jb","ep9_diks_ph2_jb_label","John Boy's room"])
$ map_system_list.append(["ep9_diks_ph1_leon_room","ep9_diks_ph2_leon_room_label","Leon's room"])
if branchJill:
    $ map_system_list.append(["ep9_diks_ph2_mainjsb","ep9_diks_ph2_main_label","Main party room"])
else:
    $ map_system_list.append(["ep9_diks_ph2_mainjse","ep9_diks_ph2_main_label","Main party room"])
$ map_system_list.append(["ep9_diks_ph1_nick","ep9_diks_ph2_nick_label","Nick's room"])
$ map_system_list.append(["ep9_diks_ph2_right_hall","ep9_diks_ph2_right_hall_label","Right hallway"])
$ map_system_list.append(["ep9_diks_ph2_left_hall2","ep9_diks_ph2_left_hall2_label","Left hallway"])
$ map_system_list.append(["ep9_diks_ph1_rusty_room","ep9_diks_ph2_rusty_room_label","Rusty's room"])
$ map_system_list.append(["ep9_diks_ph2_tommy_room","ep9_diks_ph2_tommy_label","Tommy's room"])
$ map_system_list.append(["ep9_diks_ph2_uaae","ep9_diks_ph2_ua_label","Upper main room"])

jump initRoosterLabel
label ep9_diks_ph2_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_lib_mid_label"
if "ep9_diks_ph2_piss_event_label" in event_list and "ep9_diks_ph2_ssolo_event_label" in event_list:
    if renpy.random.randint(0, 5) == 3:
        $ currentEvent = "ep9_diks_ph2_piss_event_label"
        jump startEvent

if "ep9_diks_ph2_riona_event_label" in event_list or "ep9_diks_ph2_riona_event2_label" in event_list:
    scene ep9_diks_ph1_lib_mid_ri with dissolve
else:
    scene ep9_diks_ph1_lib_mid with dissolve

if "ep9_diks_ph2_riona_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_lib_mid_riona_idle", "ep9_diks_ph1_lib_mid_riona_hover", clicked=ui.returns("riona"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph2_lib_left_label
elif result == "go_right":
    jump ep9_diks_ph2_lib_right_label
elif result == "riona":
    $ currentEvent = "ep9_diks_ph2_riona_event_label"
    jump startEvent

label ep9_diks_ph2_lib_left_label:
scene ep9_diks_ph1_lib_left with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_lib_left_label"

$ ui.imagebutton("ep9_diks_ph1_lib_desk_idle", "ep9_diks_ph1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep9_diks_ph2_lib_mid_label
elif result == "desk":
    jump ep9_final_diks2_library_desk_label

label ep9_diks_ph2_lib_right_label:
scene ep9_diks_ph1_lib_right with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_lib_right_label"

$ ui.imagebutton("ep9_diks_ph1_lib_right_camera_idle", "ep9_diks_ph1_lib_right_camera_hover", clicked=ui.returns("camera"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph2_lib_mid_label
elif result == "camera":
    mc "(I should ask if people want their picture taken.)"
    jump ep9_diks_ph2_lib_right_label
elif result == "go_down":
    jump ep9_diks_ph2_right_hall_label

label ep9_diks_ph2_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_main_label"
if not firstTimeFreeRoam:
    if "ep9_diks_ph2_riona_event_label" not in event_list and not "ep9_jill_tour_label" in event_list:
        if not "ep9_diks_ph2_jsolo_event_label" in event_list and not "ep9_diks_ph2_zoey_event_label" in event_list and "ep9_diks_ph2_scary_intro_event_label" in event_list:
            $ currentEvent = "ep9_diks_ph2_scary_intro_event_label"
            jump startEvent
        elif not "ep9_diks_ph2_jsolo_event_label" in event_list and not "ep9_diks_ph2_zoey_event_label" in event_list and "ep9_diks_ph2_haunted_event_label" in event_list:
            $ currentEvent = "ep9_diks_ph2_haunted_event_label"
            jump startEvent
        elif not "ep9_diks_ph2_jsolo_event_label" in event_list and not "ep9_diks_ph2_zoey_event_label" in event_list and "ep9_diks_ph2_no_event_label" in event_list:
            $ currentEvent = "ep9_diks_ph2_no_event_label"
            jump startEvent

    if not "ep9_ssolo_label" in event_list and not "ep9_jsolo_label" in event_list and not "ep9_msolo_label" in event_list:
        if "ep9_diks_ph2_bmains_event_label" in event_list or "ep9_diks_ph2_mains_event_label" in event_list:
            if not "ep9_diks_ph2_dcam_event_label" in event_list and not "ep9_diks_ph2_no_event_label" in event_list and not "ep9_diks_ph2_haunted_event_label" in event_list and not "ep9_diks_ph2_scary_intro_event_label" in event_list and not "ep9_diks_ph2_ssolo_event_label" in event_list and not "ep9_diks_ph2_jmtalk_event_label" in event_list and not "ep9_diks_ph2_jsolo_event_label" in event_list:
                if "ep9_ph2_josy_event_label" in event_list:
                    $ currentEvent = "ep9_ph2_josy_event_label"
                    jump startEvent
                else:
                    if not "ep9_diks_ph2_rusty_event_label" in event_list and not "ep9_msolo_lewd_label" in event_list and not "ep9_diks_ph2_end_event_label" in event_list:
                        if branchJill and not "ep9_jill_tour_label" in event_list and not "ep9_jill_test_label" in event_list and not "ep9_jill_dance_label" in event_list:
                            $ currentEvent = "ep9_diks_ph2_bmains_event_label"
                            jump startEvent
                        elif branchMayaJosy and not "ep9_jm_dance_label" in event_list:
                            $ currentEvent = "ep9_diks_ph2_bmains_event_label"
                            jump startEvent
                        elif branchSage and not "ep9_sage_dance_label" in event_list:
                            $ currentEvent = "ep9_diks_ph2_bmains_event_label"
                            jump startEvent
                        elif branchIsabella and not "ep9_diks_ph2_photo_bella_event_label" in event_list and not "ep9_ph2_bella_jill_event_label" in event_list and not "ep9_isabella_dance_label" in event_list:
                            $ currentEvent = "ep9_diks_ph2_mains_event_label"
                            jump startEvent
                        elif branchAlone:
                            $ currentEvent = "ep9_diks_ph2_bmains_event_label"
                            jump startEvent
if firstTimeFreeRoam:
    if branchJill:
        scene ep9_diks_ph2_mainjsb with dissolve
    else:
        scene ep9_diks_ph2_mainjse with dissolve
elif "ep9_diks_ph2_riona_event_label" not in event_list and "ep9_diks_ph2_riona_event2_label" not in event_list and "oscar_block" not in event_list:
    if "ep9_diks_ph2_jamie_event_label" in event_list:
        if "ep9_diks_ph2_ssolo_event_label" in event_list or "ep9_quinn_talk_label" in event_list:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainjsb with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainjse with dissolve
            else:
                scene ep9_diks_ph2_mainjs with dissolve
        else:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainjbq with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainjeq with dissolve
            else:
                scene ep9_diks_ph2_mainjq with dissolve
    else:
        if "ep9_diks_ph2_ssolo_event_label" in event_list or "ep9_quinn_talk_label" in event_list:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainsb with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainse with dissolve
            else:
                scene ep9_diks_ph2_mains with dissolve
        else:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainbq with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_maineq with dissolve
            else:
                scene ep9_diks_ph2_mainq with dissolve
else:
    if "ep9_diks_ph2_jamie_event_label" in event_list:
        if "ep9_diks_ph2_ssolo_event_label" in event_list or "ep9_quinn_talk_label" in event_list:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainjsbr with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainjser with dissolve
            else:
                scene ep9_diks_ph2_mainjsr with dissolve
        else:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainjbqr with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainjeqr with dissolve
            else:
                scene ep9_diks_ph2_mainjqr with dissolve
    else:
        if "ep9_diks_ph2_ssolo_event_label" in event_list or "ep9_quinn_talk_label" in event_list:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainsbr with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_mainser with dissolve
            else:
                scene ep9_diks_ph2_mainsr with dissolve
        else:
            if "ep9_jill_tour_label" in event_list:
                scene ep9_diks_ph2_mainbqr with dissolve
            elif "ep9_jill_talk_label" in event_list:
                scene ep9_diks_ph2_maineqr with dissolve
            else:
                scene ep9_diks_ph2_mainqr with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    if persistent.mod_wtenabled:
        $ task_list = ["Talk to Sage (Main party room)","","Talk to Jamie (Main Party room upstairs)","","Talk to Josy (Right Hallway)","","","","Talk to Quinn (Right Hallway)","","","","","","","Talk to Derek (Upper Main Room)",""]
    else:
        $ task_list = ["Talk to Sage","","Talk to Jamie","","Talk to Josy","","","","Talk to Quinn","","","","","","","Talk to Derek",""]
    if persistent.mod_wtenabled:
        $ optional_task_list = ["","","Take picture with Riona (Main party room)","","Talk to Sarah (Upper Main Room)","Restock cakes (Right Hallway)"]
    else:
        $ optional_task_list = ["","","Take picture with Riona","","Talk to Sarah","Restock cakes"]

    $ chat_new_tasks = True
    $ event_list = []
    $ event_list.append("ep9_diks_ph2_ssolo_event_label")
    if branchJill:
        $ event_list.append("ep9_jill_tour_label")
        $ event_list.append("ep9_jill_test_label")
        if persistent.mod_wtenabled:
            $ task_list[3] = "Give Jill a tour (Main Party room)"
        else:
            $ task_list[3] = "Give Jill a tour"
        $ task_list[16] = "Check the dining room"
    else:
        $ event_list.append("ep9_jill_talk_label")
        $ task_list[7] = "Talk to Jill (Main party room)"
    $ event_list.append("ep9_diks_ph2_photo_riona_event_label")
    $ event_list.append("ep9_diks_ph2_jamie_event_label")
    $ event_list.append("ep9_diks_ph2_sarah_event_label")
    $ event_list.append("ep9_diks_ph2_dcam_event_label")
    $ event_list.append("ep9_diks_ph2_piss_event_label")
    if branchSage:
        $ event_list.append("ep9_sage_dance_label")
        if persistent.mod_wtenabled:
            if branchJill:
                $ task_list[3] = "Give Jill a tour (Main Party room)\n Dance with Sage (Tommy's room)"
            else:
                $ task_list[3] = "Dance with Sage (Tommy's room)"
        else:
            if branchJill:
                $ task_list[3] = "Give Jill a tour\n Dance with Sage"
            else:
                $ task_list[3] = "Dance with Sage"
            
    if branchMayaJosy:
        
        $ event_list.append("ep9_jm_dance_label")
        if persistent.mod_wtenabled:
            
            $ task_list[3] = "Dance with Josy & Maya (Tommy's room)"
            if branchSage and branchJill:
               $task_list[3]=" Give Jill a tour (Main Party room)\n Dance with Sage (Tommy's room)\n Dance with Josy & Maya (Tommy's room)"
            elif branchJill and not branchSage:
               $task_list[3]="Give Jill a tour (Main Party room)\n Dance with Josy & Maya (Tommy's room)"
            elif branchSage and not branchJill:
               $task_list[3]="Dance with Sage (Tommy's room)\n Dance with Josy & Maya (Tommy's room)"
                
             
        else:
            $ task_list[3] = "Dance with Josy & Maya"
            if branchSage and branchJill:
               $task_list[3]="Give Jill a tour\n Dance with Sage\n Dance with Josy & Maya"
            elif branchJill and not branchSage:
               $task_list[3]="Give Jill a tour\n Dance with Josy & Maya"
            elif branchSage and not branchJill:
               $task_list[3]="Dance with Sage\n Dance with Josy & Maya"
        
    if branchIsabella:
        $ event_list.append("ep9_diks_ph2_photo_bella_event_label")
        $ event_list.append("ep9_ph2_bella_jill_event_label")
        if persistent.mod_wtenabled:
            $ task_list[11] = "Take picture with Bella (Upper Main Room)"
        else:
            $ task_list[11] = "Take picture with Bella (Upper Main Room)"
        if branchJill:
            $ task_list[12] = ""
        else:
            $ task_list[12] = "Have Bella talk to Jill"
    $ event_list.append("ep9_diks_ph2_food_event_label")
    $ event_list.append("ep9_diks_ph2_jsolo_event_label")
    $ event_list.append("ep9_quinn_talk_label")
    if branchAlone:
        $ event_list.append("ep9_diks_ph2_camila_dance_event_label")
        if persistent.mod_wtenabled:
            $ optional_task_list[0] = "Dance with Camila (Tommy's room)"
        else:
            $ optional_task_list[0] = "Dance with Camila"
    if ep9_scary_stories:
        $ event_list.append("ep9_diks_ph2_scary_intro_event_label")
        $ task_list[14] = "Attend scary stories"
    elif ep9_haunted_mansion:
        $ event_list.append("ep9_diks_ph2_haunted_event_label")
        $ task_list[14] = "Try the Haunted Mansion"
    else:
        $ event_list.append("ep9_diks_ph2_no_event_label")
        $ task_list[14] = "Pass time"
    $ event_list.append("ep9_diks_ph2_heather_event_label")
    $ event_list.append("ep9_diks_ph2_l_event_label")
    if branchIsabella:
        $ event_list.append("ep9_diks_ph2_mains_event_label")
    else:
        $ event_list.append("ep9_diks_ph2_bmains_event_label")
    show screen freeroam_intro_screen(" ")
    $ updateTaskList()
    $ updateDikScore()
    show screen scoremsg
    $ renpy.pause(2)
    hide screen scoremsg
    show screen new_phone_screen
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        $ ui.imagebutton("mphone_btn_alert_golden", "mphone_btn_alert_golden", clicked=ui.returns("OK"), xalign=0.02, yalign=0.0198)
    else:
        $ ui.imagebutton("mphone_btn_alert", "mphone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.0198)
    if notifications:
        play sound mphone_notifications[current_notification_sound][1]
    $ renpy.pause(2)
    show screen map_screen_notification
    $ renpy.pause(1)
    show screen map_screen
    hide screen freeroam_intro_screen

$ ui.imagebutton("ep9_diks_ph2_main_stairs_idle", "ep9_diks_ph2_main_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_main_door_idle", "ep9_diks_ph2_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if not "ep9_diks_ph2_ssolo_event_label" in event_list and "ep9_diks_ph2_qpic_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_main_quinn_idle", "ep9_diks_ph2_main_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
if "ep9_jill_tour_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_main_jill_idle", "ep9_diks_ph2_main_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
elif "ep9_jill_talk_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_main_jillb_idle", "ep9_diks_ph2_main_jillb_hover", clicked=ui.returns("jill2"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_ssolo_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_main_sage_idle", "ep9_diks_ph2_main_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_riona_event_label" not in event_list and "ep9_diks_ph2_riona_event2_label" not in event_list and "ep9_diks_ph2_photo_riona_event_label" in event_list and "oscar_block" not in event_list:
    $ ui.imagebutton("ep9_diks_ph2_main_riona_idle", "ep9_diks_ph2_main_riona_hover", clicked=ui.returns("riona"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "stairs":
    jump ep9_diks_ph2_mainup_label
elif result == "go_down":
    jump ep9_diks_ph2_right_hall_label
elif result == "door":
    jump ep9_diks_ph2_left_hall2_label
elif result == "sage":
    $ currentEvent = "ep9_diks_ph2_ssolo_event_label"
    jump startEvent
elif result == "jill":
    $ currentEvent = "ep9_jill_tour_label"
    jump startEvent
elif result == "jill2":
    $ currentEvent = "ep9_jill_talk_label"
    jump startEvent
elif result == "riona":
    $ currentEvent = "ep9_diks_ph2_photo_riona_event_label"
    jump startEvent
elif result == "quinn":
    $ currentEvent = "ep9_diks_ph2_qpic_event_label"
    jump startEvent

label ep9_diks_ph2_mainup_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_mainup_label"
if "ep9_diks_ph2_jamie_event_label" in event_list:
    scene ep9_diks_ph2_mainup_jamie with dissolve
else:
    scene ep9_diks_ph2_mainup with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph2_mainup_ldoor_idle", "ep9_diks_ph2_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_jamie_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_mainup_rdoor_idle", "ep9_diks_ph2_mainup_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph2_mainup_jamie_idle", "ep9_diks_ph2_mainup_jamie_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph2_mainup2_rdoor_idle", "ep9_diks_ph2_mainup2_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_main_label
elif result == "room":
    jump ep9_diks_ph2_ua_label
elif result == "leon":
    jump ep9_diks_ph2_leon_room_label
elif result == "jamie":
    $ currentEvent = "ep9_diks_ph2_jamie_event_label"
    jump startEvent

label ep9_diks_ph2_ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_ua_label"

if "ep9_diks_ph2_l_event_label" in event_list and "ep9_diks_ph2_jamie_event_label" not in event_list:
    $ currentEvent = "ep9_diks_ph2_l_event_label"
    jump startEvent

if "ep9_diks_ph2_end_event_label" in event_list and current_task == "Talk to Sage":
    scene ep9_diks_ph2_uaae with dissolve
else:
    if "ep9_diks_ph2_zoey_event_label" in event_list:
        if ep9_sarah_punch:
            scene ep9_diks_ph2_uaa with dissolve
        else:
            scene ep9_diks_ph2_uab with dissolve
    else:
        if ep9_sarah_punch:
            scene ep9_diks_ph2_uac with dissolve
        else:
            scene ep9_diks_ph2_uad with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1400 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=750 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
if not ("ep9_diks_ph2_end_event_label" in event_list and current_task == "Talk to Sage"):
    if "ep9_diks_ph2_zoey_event_label" in event_list:
        if "ep9_diks_ph2_sarah_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph2_ua_sarah_idle", "ep9_diks_ph2_ua_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)
        elif "ep9_diks_ph2_sarah3_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph2_ua_sarah_idle", "ep9_diks_ph2_ua_sarah_hover", clicked=ui.returns("sarah3"), xpos=0, ypos=0, focus_mask=True)
    else:
        if "ep9_diks_ph2_sarah_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph2_ua_sarahb_idle", "ep9_diks_ph2_ua_sarahb_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)
        elif "ep9_diks_ph2_sarah3_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph2_ua_sarahb_idle", "ep9_diks_ph2_ua_sarahb_hover", clicked=ui.returns("sarah3"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_mainup_label
elif result == "go_up":
    jump ep9_diks_ph2_1corr_label
elif result == "go_right":
    jump ep9_diks_ph2_2ua_label
elif result == "sarah":
    $ currentEvent = "ep9_diks_ph2_sarah_event_label"
    jump startEvent
elif result == "sarah3":
    $ currentEvent = "ep9_diks_ph2_sarah3_event_label"
    jump startEvent

label ep9_diks_ph2_2ua_label:
if "ep9_diks_ph2_end_event_label" in event_list and current_task == "Talk to Sage":
    if branchIsabella:
        scene ep9_diks_ph2_2ue with dissolve
    else:
        scene ep9_diks_ph2_2ue2 with dissolve
else:
    if "ep9_diks_ph2_dcam_event_label" in event_list:
        if "ep9_diks_ph2_photo_bella_event_label" in event_list:
            scene ep9_diks_ph2_2ua with dissolve
        else:
            scene ep9_diks_ph2_2uab with dissolve
    else:
        if "ep9_diks_ph2_photo_bella_event_label" in event_list:
            scene ep9_diks_ph2_2uac with dissolve
        else:
            scene ep9_diks_ph2_2uad with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_2ua_label"

if "ep9_diks_ph2_photo_bella_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_2ua_bella_idle", "ep9_diks_ph2_2ua_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_dcam_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_2ua_derek_idle", "ep9_diks_ph2_2ua_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_end_event_label" in event_list and current_task == "Talk to Sage":
    $ ui.imagebutton("ep9_diks_ph2_2ua_sage_idle", "ep9_diks_ph2_2ua_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_ua_label
elif result == "derek":
    $ currentEvent = "ep9_diks_ph2_dcam_event_label"
    jump startEvent
elif result == "bella":
    $ currentEvent = "ep9_diks_ph2_photo_bella_event_label"
    jump startEvent
elif result == "sage":
    $ currentEvent = "ep9_diks_ph2_end_event2_label"
    jump startEvent
    label ep9_diks_ph2_end_event2_label:
    menu:
        "End free roam":
            $ phone_clear_jump_label = "ep9_diks_ph2_mains2_event_label"
            jump end_freeroam
        "Not yet":
            $ renpy.pause(0.5)
    jump endEvent

label ep9_diks_ph2_1corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_1corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph2_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_1corr_ldoor_idle", "ep9_diks_ph1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_1corr_rdoor_idle", "ep9_diks_ph1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_2corr_label
elif result == "go_up":
    jump ep9_diks_ph2_toilet_2nd_label
elif result == "janitor":
    jump ep9_diks_ph2_derek_label
elif result == "go_left":
    jump ep9_diks_ph2_ua_label

label ep9_diks_ph2_2corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_2corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph2_2corr_label"
$ ui.imagebutton("ep9_diks_ph1_2corr_door_idle", "ep9_diks_ph1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_1corr_label
elif result == "go_up":
    jump ep9_diks_ph2_jb_label
elif result == "go_right":
    jump ep9_diks_ph2_ua_label

label ep9_diks_ph2_derek_label:
$ renpy.block_rollback()
if "ep9_jsolo_label" in event_list:
    $ currentEvent = "ep9_jsolo_label"
    jump startEvent
$ currentFreeRoamLabel = "ep9_diks_ph2_derek_label"
scene ep9_diks_ph2_derek with dissolve

$ ui.imagebutton("ep9_diks_ph2_guests_idle", "ep9_diks_ph2_guests_hover", clicked=ui.returns("guests"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_1corr_label
elif result == "guests":
    scene ep9_diks_ph2_derek1 with dissolve
    mc "(People seem to enjoy Derek's bar... Sadly, there is only room for {color=#00ff00}2{/color} bar stools in here.)"
    mc "(And what a funky smell... This room could use windows or ventilation.)"
    jump ep9_diks_ph2_derek_label

label ep9_diks_ph2_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_left_hall2_label"

if "ep9_diks_ph2_photo_camila_event_label" in event_list:
    if "ep9_diks_ph2_bmains_event_label" not in event_list and not branchIsabella:
        scene ep9_diks_ph2_left_hall2cb with dissolve
    else:
        scene ep9_diks_ph2_left_hall2c with dissolve
else:
    if "ep9_diks_ph2_bmains_event_label" not in event_list and not branchIsabella:
        scene ep9_diks_ph2_left_hall2d with dissolve
    else:
        scene ep9_diks_ph2_left_hall2 with dissolve


if "ep9_diks_ph2_photo_camila_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_left_hall2_door_idle", "ep9_diks_ph2_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph2_left_hall2_doorb_idle", "ep9_diks_ph2_left_hall2_doorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if "ep9_diks_ph2_photo_camila_event_label" in event_list:
    if "ep9_diks_ph2_bmains_event_label" not in event_list and not branchIsabella:
        $ ui.imagebutton("ep9_diks_ph2_left_camilab_idle", "ep9_diks_ph2_left_camilab_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep9_diks_ph2_left_camila_idle", "ep9_diks_ph2_left_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_left_hall2_stairs_idle", "ep9_diks_ph2_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep9_diks_ph2_main_label
elif result == "go_up":
    jump ep9_diks_ph2_left_hall_label
elif result == "stairs":
    jump ep9_diks_ph2_tommy_label
elif result == "door":
    mc "(We locked this door for the party. Jamie didn't want anyone to ruin his plants by pissing on them.)"
    jump ep9_diks_ph2_left_hall2_label
elif result == "camila":
    $ currentEvent = "ep9_diks_ph2_photo_camila_event_label"
    jump startEvent

label ep9_diks_ph2_left_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_left_hall_label"

scene ep9_diks_ph1_left_hall with dissolve
$ ui.imagebutton("ep9_diks_ph1_left_hall_jdoor_idle", "ep9_diks_ph1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_left_hall_rdoor_idle", "ep9_diks_ph1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_left_hall2_label
elif result == "jdoor":
    jump ep9_diks_ph2_jamie_label
elif result == "rdoor":
    jump ep9_diks_ph2_rusty_room_label

label ep9_diks_ph2_rusty_room_label:
scene ep9_diks_ph1_rusty_room with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_rusty_room_label"

$ ui.imagebutton("ep9_diks_ph1_rusty_room_door_idle", "ep9_diks_ph1_rusty_room_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_left_hall_label
elif result == "door":
    jump ep9_diks_ph2_dining_label

label ep9_diks_ph2_right_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_right_hall_label"

if "ep9_ph2_bella_jill_event_label" in event_list and not "ep9_diks_ph2_photo_bella_event_label" in event_list:
    $ currentEvent = "ep9_ph2_bella_jill_event_label"
    jump startEvent
elif "ep9_msolo_lewd_label" in event_list:
    $ currentEvent = "ep9_msolo_lewd_label"
    jump startEvent
elif "ep9_ssolo_label" in event_list:
    $ currentEvent = "ep9_ssolo_label"
    jump startEvent
elif "ep9_diks_ph2_sally_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph2_sally_event_label"
    jump startEvent
if "ep9_diks_ph2_jsolo_event_label" in event_list:
    scene ep9_diks_ph2_right_hall with dissolve
else:
    if "ep9_quinn_talk_label" in event_list:
        if ep9_restocked_food:
            scene ep9_diks_ph2_right_hall_foodq with dissolve
        else:
            scene ep9_diks_ph2_right_hall_q with dissolve
    else:
        if ep9_restocked_food:
            scene ep9_diks_ph2_right_hall_food with dissolve
        else:
            scene ep9_diks_ph2_right_hall2 with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if "ep9_diks_ph2_jsolo_event_label" not in event_list and "ep9_quinn_talk_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_right_hall_kitchenb_idle", "ep9_diks_ph2_right_hall_kitchenb_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph2_right_hall_kitchen_idle", "ep9_diks_ph2_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph2_jsolo_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_right_hall_josy_idle", "ep9_diks_ph2_right_hall_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
else:
    if ep9_restocked_food:
        $ ui.imagebutton("ep9_diks_ph2_right_hall_table_idle", "ep9_diks_ph2_right_hall_table_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep9_diks_ph2_right_hall_tableb_idle", "ep9_diks_ph2_right_hall_tableb_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph2_jsolo_event_label" not in event_list and "ep9_quinn_talk_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_right_hall_quinn_idle", "ep9_diks_ph2_right_hall_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_diks_ph2_right_hall_theater_idle", "ep9_diks_ph2_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_right_hall_library_idle", "ep9_diks_ph2_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_main_label
elif result == "theater":
    jump ep9_diks_ph2_theater_label
elif result == "library":
    jump ep9_diks_ph2_lib_right_label
elif result == "kitchen":
    jump ep9_diks_ph2_kitchen_label
elif result == "table":
    jump ep9_diks_ph2_table_label
elif result == "josy":
    $ currentEvent = "ep9_diks_ph2_jsolo_event_label"
    jump startEvent
elif result == "quinn":
    $ currentEvent = "ep9_quinn_talk_label"
    jump startEvent

label ep9_diks_ph2_table_label:
if not persistent.ep9_cardji3:
    if ep9_restocked_food:
        scene ep9_diks_ph2_table_card with dissolve
    else:
        scene ep9_diks_ph2_tableb_card with dissolve
else:
    if ep9_restocked_food:
        scene ep9_diks_ph2_table with dissolve
    else:
        scene ep9_diks_ph2_tableb with dissolve

label ep9_diks_ph2_table_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_table_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph2_table_punch_idle", "ep9_diks_ph2_table_punch_hover", clicked=ui.returns("punch"), xpos=0, ypos=0, focus_mask=True)
if ep9_restocked_food:
    $ ui.imagebutton("ep9_diks_ph2_table_food_idle", "ep9_diks_ph2_table_food_hover", clicked=ui.returns("food"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph2_tableb_food_idle", "ep9_diks_ph2_tableb_food_hover", clicked=ui.returns("food"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardji3:
    $ ui.imagebutton("ep9_diks_ph2_table_card_idle", "ep9_diks_ph2_table_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_right_hall_label
elif result == "food":
    if "ep9_diks_ph2_food_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph2_food_event_label"
        jump startEvent
    elif "ep9_diks_ph2_food3_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph2_food3_event_label"
        jump startEvent
    else:
        if ep9_restocked_food:
            mc "(Looks good.)"
        else:
            mc "(I should put out some more cakes.)"
        jump ep9_diks_ph2_table_label
elif result == "punch":
    if "ep9_diks_ph2_sarah2_event_label" in event_list and optional_task_list[4] != "":
        $ currentEvent = "ep9_diks_ph2_sarah2_event_label"
        jump startEvent
    else:
        mc "(We're not running out of punch so far.)"
        jump ep9_diks_ph2_table_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji3 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if ep9_restocked_food:
        scene ep9_diks_ph2_table with dissolve
    else:
        scene ep9_diks_ph2_tableb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph2_table_label_nofx

label ep9_diks_ph2_theater_label:
$ renpy.block_rollback()
if "ep9_diks_ph2_jmtalk_event_label" in event_list and not "ep9_jill_tour_label" in event_list:
    stop music fadeout 3
    $ currentEvent = "ep9_diks_ph2_jmtalk_event_label"
    jump startEvent

scene ep9_diks_ph2_theater with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph2_theater_label"

$ ui.imagebutton("ep9_diks_ph2_theater_beth_idle", "ep9_diks_ph2_theater_beth_hover", clicked=ui.returns("beth"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=200 * persistent.scale_factor, ypos=450 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph2_theater2_label
elif result == "go_down":
    jump ep9_diks_ph2_right_hall_label
elif result == "beth":
    mc "(I knew people wouldn't be watching movies in here... Oh, well. At least it's a good spot for making out.)"
    jump ep9_diks_ph2_theater_label

label ep9_diks_ph2_theater2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_theater2_label"

scene ep9_diks_ph1_theater2 with dissolve

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_left":
    jump ep9_diks_ph2_theater_label

label ep9_diks_ph2_leon_room_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_leon_room_label"
scene ep9_diks_ph1_leon_room with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_mainup_label

label ep9_diks_ph2_toilet_2nd_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_toilet_2nd_label"
scene ep9_diks_ph2_toilet_2nd with dissolve

$ ui.imagebutton("ep9_diks_ph2_toilet_2nd_idle", "ep9_diks_ph2_toilet_2nd_hover", clicked=ui.returns("bottle"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_1corr_label
elif result == "bottle":
    scene ep9_diks_ph2_toilet_2nd1 with dissolve
    mc "*{i}Sigh{/i}* (Ok... Who did this?)"
    jump ep9_diks_ph2_toilet_2nd_label

label ep9_diks_ph2_dining_label:
if "ep9_jill_test_label" in event_list:
    $ currentEvent = "ep9_jill_test_label"
    jump startEvent
if not persistent.ep9_cardji1:
    scene ep9_diks_ph2_dining_card with dissolve
else:
    scene ep9_diks_ph2_dining with dissolve
label ep9_diks_ph2_dining_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_dining_label"

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph2_dining_stairs_idle", "ep9_diks_ph2_dining_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_dining_rdoor_idle", "ep9_diks_ph2_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_dining_jdoor_idle", "ep9_diks_ph2_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_dining_chips_idle", "ep9_diks_ph2_dining_chips_hover", clicked=ui.returns("chips"), xpos=0, ypos=0, focus_mask=True)

if not persistent.ep9_cardji1:
    $ ui.imagebutton("ep9_diks_ph2_dining_card_idle", "ep9_diks_ph2_dining_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph2_kitchen_label
elif result == "stairs":
    jump ep9_diks_ph2_upper_2dining_label
elif result == "chips":
    mc "(We still have enough for the party... I think.)"
    jump ep9_diks_ph2_dining_label
elif result == "rusty":
    jump ep9_diks_ph2_rusty_room_label
elif result == "jamie":
    jump ep9_diks_ph2_jamie_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji1 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph2_dining with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph2_dining_label_nofx

label ep9_diks_ph2_upper_2dining_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_upper_2dining with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph2_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_jacob_idle", "ep9_diks_ph1_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_nick_idle", "ep9_diks_ph1_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_jb_label
elif result == "stairs":
    jump ep9_diks_ph2_dining_label
elif result == "nick":
    jump ep9_diks_ph2_nick_label
elif result == "jacob":
    jump ep9_diks_ph2_jacob_label

label ep9_diks_ph2_kitchen_label:
scene ep9_diks_ph2_kitchen with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_kitchen_label"

if "ep9_diks_ph2_food2_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_kitchen_fridge_idle", "ep9_diks_ph2_kitchen_fridge_hover", clicked=ui.returns("fridge"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_dining_label
elif result == "go_right":
    jump ep9_diks_ph2_right_hall_label
elif result == "fridge":
    $ currentEvent = "ep9_diks_ph2_food2_event_label"
    jump startEvent


label ep9_diks_ph2_jb_label:
scene ep9_diks_ph1_jb with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_jb_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_1corr_label
elif result == "go_up":
    jump ep9_diks_ph2_upper_2dining_label

label ep9_diks_ph2_nick_label:
scene ep9_diks_ph1_nick with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_nick_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep9_diks_ph2_upper_2dining_label

label ep9_diks_ph2_jacob_label:
if "ep9_diks_ph2_zoey_event_label" in event_list:
    scene ep9_diks_ph2_jacob with dissolve
else:
    if not persistent.ep9_cardji2:
        scene ep9_diks_ph2_jacobb_card with dissolve
    else:
        scene ep9_diks_ph2_jacobb with dissolve

label ep9_diks_ph2_jacob_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_jacob_label"

if "ep9_diks_ph2_zoey_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_jacob_idle", "ep9_diks_ph2_jacob_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

if not "ep9_diks_ph2_zoey_event_label" in event_list and not persistent.ep9_cardji2:
    $ ui.imagebutton("ep9_diks_ph2_jacobb_card_idle", "ep9_diks_ph2_jacobb_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_upper_2dining_label
elif result == "zoey":
    $ currentFreeRoamLabel = "ep9_diks_ph2_lib_right_label"
    $ currentEvent = "ep9_diks_ph2_zoey_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji2 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph2_jacobb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph2_jacob_label_nofx

label ep9_diks_ph2_tommy_label:
show screen dance_filter_screen
if "ep9_diks_ph2_rusty_event_label" in event_list:
    scene ep9_diks_ph2_tommy_roomb with dissolve
else:
    scene ep9_diks_ph2_tommy_room with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_tommy_label"

if "ep9_diks_ph2_camila_dance_event_label" in event_list or "ep9_jm_dance_label" in event_list or "ep9_jill_dance_label" in event_list or "ep9_sage_dance_label" in event_list or "ep9_isabella_dance_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_tommy_dance_idle", "ep9_diks_ph2_tommy_dance_hover", clicked=ui.returns("dance"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph2_rusty_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph2_tommy_rusty_idle", "ep9_diks_ph2_tommy_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph2_tommy_curtain_idle", "ep9_diks_ph2_tommy_curtain_hover", clicked=ui.returns("curtain"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    hide screen dance_filter_screen
    jump ep9_diks_ph2_left_hall2_label
elif result == "curtain":
    hide screen dance_filter_screen
    jump ep9_diks_ph2_tommy2_label
elif result == "rusty":
    $ currentEvent = "ep9_diks_ph2_rusty_event_label"
    jump startEvent
elif result == "dance":
    if "ep9_diks_ph2_camila_dance_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph2_camila_dance_event_label"
    elif "ep9_jm_dance_label" in event_list:
        $ currentEvent = "ep9_jm_dance_label"
    elif "ep9_jill_dance_label" in event_list:
        $ currentEvent = "ep9_jill_dance_label"
    elif "ep9_sage_dance_label" in event_list:
        $ currentEvent = "ep9_sage_dance_label"
    else:
        $ currentEvent = "ep9_isabella_dance_label"
    jump startEvent

label ep9_diks_ph2_tommy2_label:
if "ep9_diks_ph2_heather_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph2_heather_event_label"
    jump startEvent
if found_money:
    if not persistent.ep9_cardji4:
        scene ep9_diks_ph2_tommy2_card with dissolve
    else:
        scene ep9_diks_ph2_tommy2 with dissolve
else:
    if not persistent.ep9_cardji4:
        scene ep9_diks_ph2_tommy2_card_money with dissolve
    else:
        scene ep9_diks_ph2_tommy2_money with dissolve

label ep9_diks_ph2_tommy2_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_tommy2_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not persistent.ep9_cardji4:
    $ ui.imagebutton("ep9_diks_ph2_tommy2_card_idle", "ep9_diks_ph2_tommy2_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if not found_money:
    $ ui.imagebutton("ep9_diks_ph2_tommy2_money_idle", "ep9_diks_ph2_tommy2_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_tommy_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji4 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if found_money:
        scene ep9_diks_ph2_tommy2 with dissolve
    else:
        scene ep9_diks_ph2_tommy2_money with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph2_tommy2_label_nofx
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    if not persistent.ep9_cardji4:
        scene ep9_diks_ph2_tommy2_card with dissolve
    else:
        scene ep9_diks_ph2_tommy2 with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep9_diks_ph2_tommy2_label_nofx

label ep9_diks_ph2_jamie_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph2_jamie_label"

scene ep9_diks_ph1_jamie with dissolve
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_jamie_door_idle", "ep9_diks_ph1_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph2_left_hall_label
elif result == "door":
    jump ep9_diks_ph2_dining_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

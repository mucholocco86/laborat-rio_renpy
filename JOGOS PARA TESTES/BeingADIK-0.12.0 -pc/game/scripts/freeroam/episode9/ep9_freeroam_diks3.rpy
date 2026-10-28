label ep9_freeroam_diks_ph3_label:
$ freeRoamID = "ep9_4"
show screen wt_tasks_shown
$ roosterState = "ep9_4"
$ tmpInt = 0


$ found_money = False
$ found_money2 = False
$ studied = False

if art_unlock_orders():
    $ new_chat_msg("Jacob",True,7)

$ disabled_apps = []
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

if branchJill:
    $ rooster_jump_label = "ep9_diks_ph3_2ua_label"
else:
    $ rooster_jump_label = "ep9_diks_ph3_left_hall2_label"

$ map_system_list = []
$ map_system_list.append(["ep9_diks_ph3_derek_fr0","ep9_diks_ph3_derek_label","Derek's room"])
$ map_system_list.append(["ep9_diks_ph3_dining","ep9_diks_ph3_dining_label","Dining room"])
$ map_system_list.append(["ep9_diks_ph3_jacob","ep9_diks_ph3_jacob_label","Jacob's room"])
$ map_system_list.append(["ep9_diks_ph3_jamie","ep9_diks_ph3_jamie_label","Jamie's room"])
$ map_system_list.append(["ep9_diks_ph3_jb","ep9_diks_ph3_jb_label","John Boy's room"])
$ map_system_list.append(["ep9_diks_ph3_leon_room","ep9_diks_ph3_leon_room_label","Leon's room"])
if branchIsabella:
    $ map_system_list.append(["ep9_diks_ph3_mainb","ep9_diks_ph3_main_label","Main party room"])
else:
    $ map_system_list.append(["ep9_diks_ph3_mainb2","ep9_diks_ph3_main_label","Main party room"])
$ map_system_list.append(["ep9_diks_ph1_nick","ep9_diks_ph3_nick_label","Nick's room"])
$ map_system_list.append(["ep9_diks_ph3_right_hall","ep9_diks_ph3_right_hall_label","Right hallway"])
$ map_system_list.append(["ep9_diks_ph3_left_hall2","ep9_diks_ph3_left_hall2_label","Left hallway"])
$ map_system_list.append(["ep9_diks_ph1_rusty_room","ep9_diks_ph3_rusty_room_label","Rusty's room"])
$ map_system_list.append(["ep9_diks_ph3_tommy_room","ep9_diks_ph3_tommy_label","Tommy's room"])
$ map_system_list.append(["ep9_diks_ph3_ua","ep9_diks_ph3_ua_label","Upper main room"])

call mphone_check_pack_quest_available from _call_mphone_check_pack_quest_available

jump initRoosterLabel
label ep9_diks_ph3_left_hall_label:
if not persistent.ep9_cardji14:
    scene ep9_diks_ph1_left_hall_card with dissolve
else:
    scene ep9_diks_ph1_left_hall with dissolve
label ep9_diks_ph3_left_hall_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_left_hall_label"

$ ui.imagebutton("ep9_diks_ph1_left_hall_jdoor_idle", "ep9_diks_ph1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_left_hall_rdoor_idle", "ep9_diks_ph1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardji14:
    $ ui.imagebutton("ep9_diks_ph1_left_hall_card_idle", "ep9_diks_ph1_left_hall_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_left_hall2_label
elif result == "jdoor":
    jump ep9_diks_ph3_jamie_label
elif result == "rdoor":
    jump ep9_diks_ph3_rusty_room_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji14 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_left_hall with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph3_left_hall_label_nofx

label ep9_diks_ph3_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_lib_mid_label"
if "ep9_vinny_label" in event_list:
    $ currentEvent = "ep9_vinny_label"
    jump startEvent
scene ep9_diks_ph1_lib_mid with dissolve

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph3_lib_left_label
elif result == "go_right":
    jump ep9_diks_ph3_lib_right_label

label ep9_diks_ph3_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_lib_left_label"
scene ep9_diks_ph3_lib_left with dissolve
$ ui.imagebutton("ep9_diks_ph3_lib_desk_idle", "ep9_diks_ph3_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep9_diks_ph3_lib_mid_label
elif result == "desk":
    jump ep9_final_diks2_library_desk_label

label ep9_diks_ph3_lib_right_label:
scene ep9_diks_ph1_lib_right with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_lib_right_label"

$ ui.imagebutton("ep9_diks_ph1_lib_right_camera_idle", "ep9_diks_ph1_lib_right_camera_hover", clicked=ui.returns("camera"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph3_lib_mid_label
elif result == "camera":
    mc "(Most guests have likely already had their picture taken by now.)"
    jump ep9_diks_ph3_lib_right_label
elif result == "go_down":
    jump ep9_diks_ph3_right_hall_label

label ep9_diks_ph3_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_main_label"
if "ep9_diks_ph3_preps_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_preps_event_label"
    jump startEvent
elif "ep9_bsolo_label" in event_list:
    $ currentEvent = "ep9_bsolo_label"
    jump startEvent
elif "ep9_diks_ph3_jt_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_jt_event_label"
    jump startEvent
elif "ep9_diks_ph3_jamie_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_jamie_event_label"
    jump startEvent
elif "ep9_diks_ph3_dz_event_label" not in event_list and "ep9_diks_ph3_zoey_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_zoey_event_label"
    jump startEvent

if "early_freeroam_mutex" in event_list:
    if "ep9_diks_ph3_costume_sm_event_label" in event_list or "ep9_diks_ph3_costume_sm_eventb_label" in event_list:
        if branchIsabella:
            scene ep9_diks_ph3_main with dissolve
        else:
            scene ep9_diks_ph3_main2 with dissolve
    else:
        if branchIsabella:
            scene ep9_diks_ph3_mainb with dissolve
        else:
            scene ep9_diks_ph3_mainb2 with dissolve
else:
    if branchIsabella and wt_ep9_branch_numbers < 2:
        scene ep9_diks_ph3_main_emptyb with dissolve
    else:
        if "ep9_diks_ph3_ln_leaving_event2_label" in event_list or "ep9_diks_ph3_ln_leaving_event_label" in event_list:
            scene ep9_diks_ph3_main_empty2 with dissolve
        else:
            scene ep9_diks_ph3_main_empty with dissolve


if "early_freeroam_mutex" in event_list:
    if branchIsabella:
        if "ep9_diks_ph3_prg_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph3_mainb_mj_idle", "ep9_diks_ph3_mainb_mj_hover", clicked=ui.returns("mj"), xpos=0, ypos=0, focus_mask=True)
        elif "ep9_diks_ph3_costume_jm_event_label" in event_list or "ep9_diks_ph3_costume_jm_eventb_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph3_mainb_mj_idle", "ep9_diks_ph3_mainb_mj_hover", clicked=ui.returns("mjb"), xpos=0, ypos=0, focus_mask=True)
    else:
        if "ep9_diks_ph3_prg_event_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph3_mainb_mjb_idle", "ep9_diks_ph3_mainb_mjb_hover", clicked=ui.returns("mj"), xpos=0, ypos=0, focus_mask=True)
        elif "ep9_diks_ph3_costume_jm_event_label" in event_list or "ep9_diks_ph3_costume_jm_eventb_label" in event_list:
            $ ui.imagebutton("ep9_diks_ph3_mainb_mjb_idle", "ep9_diks_ph3_mainb_mjb_hover", clicked=ui.returns("mjb"), xpos=0, ypos=0, focus_mask=True)
    if "ep9_diks_ph3_cumpetition_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_main_tommy_idle", "ep9_diks_ph3_main_tommy_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)
    if "ep9_diks_ph3_costume_bella_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_main_bella_idle", "ep9_diks_ph3_main_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_main_door_idle", "ep9_diks_ph3_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_main_stairs_idle", "ep9_diks_ph3_main_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
else:
    if "End the night with someone" in current_task and ("ep9_diks_ph3_quinn_event_label" in event_list or "ep9_diks_ph3_quinn2_event_label" in event_list):
        $ ui.imagebutton("ep9_diks_ph3_main_quinn_idle", "ep9_diks_ph3_main_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
    if "End the night with someone" in current_task and ("ep9_diks_ph3_ln_leaving_event2_label" in event_list or "ep9_diks_ph3_ln_leaving_event_label" in event_list):
        $ ui.imagebutton("ep9_diks_ph3_main_lily_idle", "ep9_diks_ph3_main_lily_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)
    if "Talk to Bella" in current_task:
        $ ui.imagebutton("ep9_diks_ph3_main_bellab_idle", "ep9_diks_ph3_main_bellab_hover", clicked=ui.returns("bella2"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_main_doorb_idle", "ep9_diks_ph3_main_doorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_main_stairsb_idle", "ep9_diks_ph3_main_stairsb_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[0][1]:
    $ ui.imagebutton("ep9_packquest_btn0_idle", "ep9_packquest_btn0_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)


$ result = ui.interact()
if result == "stairs":
    jump ep9_diks_ph3_mainup_label
elif result == "go_down":
    jump ep9_diks_ph3_right_hall_label
elif result == "door":
    jump ep9_diks_ph3_left_hall2_label

elif result == "mj":
    $ currentEvent = "ep9_diks_ph3_prg_event_label"
    jump startEvent
elif result == "lily":
    if "ep9_diks_ph3_ln_leaving_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_ln_leaving_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_ln_leaving_event2_label"
    jump startEvent
elif result == "bella":
    $ currentEvent = "ep9_diks_ph3_costume_bella_event_label"
    jump startEvent
elif result == "bella2":
    menu:
        "End free roam":
            $ phone_clear_jump_label = "ep9_bella_lewd2_label"
            stop music fadeout 3
            jump end_freeroam
        "Not yet":
            jump ep9_diks_ph3_main_label
elif result == "mjb":
    if "ep9_diks_ph3_costume_jm_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_jm_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_jm_eventb_label"
    jump startEvent
elif result == "tommy":
    $ currentEvent = "ep9_diks_ph3_cumpetition_event_label"
    jump startEvent
elif result == "quinn":
    if "ep9_diks_ph3_quinn_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_quinn_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_quinn2b_event_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[0][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_mainup_label:
if "early_freeroam_mutex" in event_list:
    scene ep9_diks_ph3_mainup with dissolve
else:
    if found_money:
        scene ep9_diks_ph3_mainupb with dissolve
    else:
        scene ep9_diks_ph3_mainupb_money with dissolve
label ep9_diks_ph3_mainup_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_mainup_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not found_money and "early_freeroam_mutex" not in event_list:
    $ ui.imagebutton("ep9_diks_ph3_mainupb_money_idle", "ep9_diks_ph3_mainupb_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if "early_freeroam_mutex" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_mainup_ldoor_idle", "ep9_diks_ph3_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_mainup_rdoor_idle", "ep9_diks_ph3_mainup_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph3_mainup_ldoorb_idle", "ep9_diks_ph3_mainup_ldoorb_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_mainup_rdoorb_idle", "ep9_diks_ph3_mainup_rdoorb_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_main_label
elif result == "room":
    jump ep9_diks_ph3_ua_label
elif result == "leon":
    jump ep9_diks_ph3_leon_room_label
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep9_diks_ph3_mainupb with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep9_diks_ph3_mainup_label_nofx

label ep9_diks_ph3_ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_ua_label"

if "ep9_diks_ph3_qv_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_qv_event_label"
    jump startEvent

if "ep9_diks_ph3_dz_event_label" in event_list:
    scene ep9_diks_ph3_uab with dissolve
elif "ep9_diks_ph3_costume_zoey_event_label" in event_list or "ep9_diks_ph3_costume_zoey_eventb_label" in event_list:
    scene ep9_diks_ph3_uac with dissolve
elif "Talk to Maya & Josy" in current_task:
    scene ep9_diks_ph3_ua_mj with dissolve
else:
    scene ep9_diks_ph3_ua with dissolve

if "ep9_diks_ph3_dz_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_ua_zoey_idle", "ep9_diks_ph3_ua_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
elif "ep9_diks_ph3_costume_zoey_event_label" in event_list or "ep9_diks_ph3_costume_zoey_eventb_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_ua2_zoey_idle", "ep9_diks_ph3_ua2_zoey_hover", clicked=ui.returns("zoey2"), xpos=0, ypos=0, focus_mask=True)
if "Talk to Maya & Josy" in current_task:
    $ ui.imagebutton("ep9_diks_ph3_main_mj_idle", "ep9_diks_ph3_main_mj_hover", clicked=ui.returns("mj2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1400 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=750 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_mainup_label
elif result == "go_up":
    jump ep9_diks_ph3_1corr_label
elif result == "go_right":
    jump ep9_diks_ph3_2ua_label
elif result == "zoey":
    $ currentEvent = "ep9_diks_ph3_dz_event_label"
    jump startEvent
elif result == "zoey2":
    if "ep9_diks_ph3_costume_zoey_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_zoey_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_zoey_eventb_label"
    jump startEvent
elif result == "mj2":
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if branchAlone and wt_ep9_branch_numbers < 2:
                             $mod_choices[10]="\n{size=-5}(End Night with Tara,Tiffani,Gina)"
                             $mod_choices[11]="(+2 Cheater)"
                        
    menu:
        "End freeroam [mod_gr][mod_choices[10]]":
            if branchMayaJosy:
                $ phone_clear_jump_label = "ep9_jm_committing_label"
            elif pathMayaJosy and (branchSage or branchJill or branchIsabella):
                $ phone_clear_jump_label = "ep9_jm_breakup_label"
            else:
                $ phone_clear_jump_label = "ep9_ending_others_label"
            if wt_ep9_branch_numbers > 1 and (branchJill or branchSage or branchMayaJosy or branchAlone):
                "End the night with?"
                menu:
                   "Maya & Josy" if branchMayaJosy:
                        $ phone_clear_jump_label = "ep9_jm_committing_label"
                        $ wt_ep9_end_pick="Maya"
                   "Sage" if branchSage:
                        $ phone_clear_jump_label = "ep9_jm_breakup_label"
                        $ wt_ep9_end_pick="Sage"
                        if branchMayaJosy:
                            $ phone_clear_jump_label="ep9_ending_others_label"
                   "Bella" if branchIsabella:
                        $ phone_clear_jump_label = "ep9_jm_breakup_label"
                        $ wt_ep9_end_pick="Bella"
                        if branchMayaJosy:
                            $ phone_clear_jump_label="ep9_ending_others_label"
                   "Jill" if branchJill:
                        $ phone_clear_jump_label = "ep9_jm_breakup_label"
                        $ wt_ep9_end_pick="Jill"
                        if branchMayaJosy:
                            $ phone_clear_jump_label="ep9_ending_others_label"
                   "Others \n{size=-5}(End Night with Tara,Tiffani,Gina)" if branchAlone:
                        $ phone_clear_jump_label = "ep9_ending_others_label"
                        $ wt_ep9_end_pick="Other"
            if wt_ep9_branch_numbers < 2:
               if branchAlone:
                $ wt_ep9_end_pick="Other"
               if branchJill:
                $ wt_ep9_end_pick="Jill"
               if branchSage:
                $ wt_ep9_end_pick="Sage"
               if branchMayaJosy:
                $ wt_ep9_end_pick="Maya"
               if branchIsabella:
                $ wt_ep9_end_pick="Bella"
               
            stop music fadeout 3
            jump end_freeroam
        "Not yet":
            jump ep9_diks_ph3_ua_label

label ep9_diks_ph3_2ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_2ua_label"
if firstTimeFreeRoam:
    scene ep9_diks_ph3_2uab2 with dissolve
    jump ep9_ph3_first_label
    label ep9_ph3_first2_label:
if "ep9_diks_ph3_costume_elena_event_label" in event_list or "ep9_diks_ph3_costume_elena_eventb_label" in event_list or not "early_freeroam_mutex" in event_list:
    if branchJill:
        scene ep9_diks_ph3_2uab with dissolve
    else:
        scene ep9_diks_ph3_2ua with dissolve
else:
    if branchJill:
        scene ep9_diks_ph3_2uab2 with dissolve
    else:
        scene ep9_diks_ph3_2ua2 with dissolve



if "ep9_diks_ph3_bj_event_label" in event_list and "ep9_diks_ph3_bm_event_label" not in event_list:
    $ ui.imagebutton("ep9_diks_ph3_2ua_jill_idle", "ep9_diks_ph3_2ua_jill_hover", clicked=ui.returns("jill3"), xpos=0, ypos=0, focus_mask=True)
elif "ep9_diks_ph3_costume_jill_event_label" in event_list or "ep9_diks_ph3_costume_jill_eventb_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_2ua_jill_idle", "ep9_diks_ph3_2ua_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph3_costume_elena_event_label" in event_list or "ep9_diks_ph3_costume_elena_eventb_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_2ua_jb_idle", "ep9_diks_ph3_2ua_jb_hover", clicked=ui.returns("jb"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[5][1]:
    $ ui.imagebutton("ep9_packquest_btn5_idle", "ep9_packquest_btn5_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_ua_label
elif result == "jill":
    if "ep9_diks_ph3_costume_jill_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_jill_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_jill_eventb_label"
    jump startEvent
elif result == "jill3":
    $ currentEvent = "ep9_diks_ph3_bj_event_label"
    jump startEvent
elif result == "jb":
    if "ep9_diks_ph3_costume_elena_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_elena_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_elena_eventb_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[5][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_1corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_1corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph3_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_1corr_ldoor_idle", "ep9_diks_ph1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_1corr_rdoor_idle", "ep9_diks_ph1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    if "ep9_diks_ph3_sally_eventb_label" in event_list and not "ep9_diks_ph3_sally_gone_event_label" in event_list:
        $ event_list.append("ep9_diks_ph3_sally_gone_event_label")
    jump ep9_diks_ph3_2corr_label
elif result == "go_up":
    if "ep9_diks_ph3_sally_event_label" in event_list or ep9_helped_sally or "ep9_diks_ph3_sally_gone_event_label" in event_list:
        jump ep9_diks_ph3_toilet_2nd_label
    else:
        play sound "sound_effects/door_knob.mp3"
        sy "OCCUPIED!!!"
        jump ep9_diks_ph3_1corr_label
elif result == "janitor":
    if "ep9_diks_ph3_sally_eventb_label" in event_list and not "ep9_diks_ph3_sally_gone_event_label" in event_list:
        $ event_list.append("ep9_diks_ph3_sally_gone_event_label")
    jump ep9_diks_ph3_derek_label
elif result == "go_left":
    if "ep9_diks_ph3_sally_eventb_label" in event_list and not "ep9_diks_ph3_sally_gone_event_label" in event_list:
        $ event_list.append("ep9_diks_ph3_sally_gone_event_label")
    jump ep9_diks_ph3_ua_label

label ep9_diks_ph3_2corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_2corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph3_2corr_label"
$ ui.imagebutton("ep9_diks_ph1_2corr_door_idle", "ep9_diks_ph1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_1corr_label
elif result == "go_up":
    jump ep9_diks_ph3_jb_label
elif result == "go_right":
    jump ep9_diks_ph3_ua_label

label ep9_diks_ph3_derek_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_derek_label"
scene ep9_diks_ph3_derek with dissolve

if pack_quest_active and not pack_quest_list[9][1]:
    $ ui.imagebutton("ep9_packquest_btn9_idle", "ep9_packquest_btn9_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph3_down_idle", "ep9_diks_ph3_down_hover", clicked=ui.returns("go_down2"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_1corr_label
elif result == "go_down2":
    jump ep9_diks_ph3_corr_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[9][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_left_hall2_label"
if not "early_freeroam_mutex" in event_list and "ep9_diks_ph3_sandy_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_sandy_event_label"
    jump startEvent

if "ep9_diks_ph3_prepsc_event_label" in event_list or ep9_prep_truce:
    if branchIsabella:
        scene ep9_diks_ph3_left_hall2p with dissolve
    else:
        scene ep9_diks_ph3_left_hall2bp with dissolve
else:
    if branchIsabella:
        scene ep9_diks_ph3_left_hall2 with dissolve
    else:
        scene ep9_diks_ph3_left_hall2b with dissolve
if firstTimeFreeRoam:
    label ep9_ph3_first_label:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    if persistent.mod_wtenabled:
        $ task_list = ["Check upstairs","","","","","Talk to Nicole (Right hallway)","","Find Becky (Jacob's room)","","Talk to Heather (Leon's room)","Talk to Josy & Maya (Main Party room)","Help John Boy","Find Sandy (Tommy's room)","","",""]
    else:
        $ task_list = ["Check upstairs","","","","","Talk to Nicole","","Find Becky","","Talk to Heather","Talk to Josy & Maya","Help John Boy","Find Sandy","","",""]
    $ optional_task_list = ["","","","Check Jamie's room","","","","","",""]

    $ chat_new_tasks = True
    $ event_list = []

    if ep9_riona_confided:
        if persistent.mod_wtenabled:
            $ task_list[15] = "Find Riona (Right hallway)"
        else:
            $ task_list[15] = "Find Riona"
        $ event_list.append("ep9_diks_ph3_riona_event_label")
    if branchJill:
        $ task_list[6] = "Check Rusty's room"
    else:
        $ optional_task_list[0] = "Check Rusty's room"

    if branchIsabella:
        if persistent.mod_wtenabled:
            $ task_list[6]="Talk to the ghost (Right hallway)"
            if branchJill:
                $ task_list[6]="Check Rusty's room\n Talk to the ghost (Right hallway)"
        else:
            $ task_list[6]="Talk to the ghost"
            if branchJill:
                $ task_list[6]="Check Rusty's room\n Talk to the ghost"
    else:
        if persistent.mod_wtenabled:
            $ optional_task_list[1] = "Talk to the ghost (Right hallway)"
        else:
            $ optional_task_list[1] = "Talk to the ghost"
    $ event_list.append("ep9_diks_ph3_rusty_event_label")
    $ event_list.append("ep9_diks_ph3_sm_event_label")
    $ event_list.append("ep9_diks_ph3_qv_event_label")
    $ event_list.append("ep9_diks_ph3_lily_event_label")
    $ event_list.append("ep9_diks_ph3_elena_event_label")
    $ event_list.append("ep9_diks_ph3_jt_event_label")
    $ event_list.append("ep9_diks_ph3_becky_event_label")
    $ event_list.append("ep9_diks_ph3_tara_event_label")
    $ event_list.append("ep9_diks_ph3_bm_event_label")
    $ event_list.append("ep9_diks_ph3_heather_event_label")
    $ event_list.append("ep9_diks_ph3_prg_event_label")
    $ event_list.append("ep9_diks_ph3_penny_event_label")
    $ event_list.append("ep9_diks_ph3_cari_event_label")
    $ event_list.append("ep9_diks_ph3_room_event_label")
    if branchJill:
        $ event_list.append("ep9_diks_ph3_bj_event_label")
    if branchIsabella:
        $ event_list.append("ep9_diks_ph3_db_event_label")

    if ep6_envy_lewd or ep8_sandy_lewd:
        $ event_list.append("ep9_diks_ph3_sandy_event_label")

    $ event_list.append("ep9_diks_ph3_preps_event_label")
    $ event_list.append("early_freeroam_mutex")

    $ updateTaskList()
    show screen freeroam_intro_screen(" ")
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
    if branchJill:
        jump ep9_ph3_first2_label

if "ep9_diks_ph3_prepsc_event_label" in event_list or ep9_prep_truce:
    $ ui.imagebutton("ep9_diks_ph3_left_hall2_stairs_idle", "ep9_diks_ph3_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_left_hall2b_door_idle", "ep9_diks_ph3_left_hall2b_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph3_left_hall2b_stairs_idle", "ep9_diks_ph3_left_hall2b_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_left_hall2_door_idle", "ep9_diks_ph3_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if "ep9_diks_ph3_prepsc_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_left_hall_christian_idle", "ep9_diks_ph3_left_hall_christian_hover", clicked=ui.returns("christian"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep9_diks_ph3_main_label
elif result == "go_up":
    jump ep9_diks_ph3_left_hall_label
elif result == "stairs":
    jump ep9_diks_ph3_tommy_label
elif result == "christian":
    $ currentEvent = "ep9_diks_ph3_prepsc_event_label"
    jump startEvent
elif result == "door":
    jump ep9_final_diks_porch_label

label ep9_final_diks_porch_label:
if not persistent.ep9_cardji13:
    if "ep9_diks_ph3_sage_event_label" in event_list or "ep9_diks_ph3_sage2_event_label" in event_list:
        scene ep9_fr_porch_card with dissolve
    else:
        scene ep9_fr_porchb_card with dissolve
else:
    if "ep9_diks_ph3_sage_event_label" in event_list or "ep9_diks_ph3_sage2_event_label" in event_list:
        scene ep9_fr_porch with dissolve
    else:
        scene ep9_fr_porchb with dissolve

label ep9_final_diks_porch_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_final_diks_porch_label"

if "ep9_diks_ph3_sage_event_label" in event_list:
    $ ui.imagebutton("ep9_fr_porch_sage_idle", "ep9_fr_porch_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
elif "ep9_diks_ph3_sage2_event_label" in event_list:
    $ ui.imagebutton("ep9_fr_porch_sage_idle", "ep9_fr_porch_sage_hover", clicked=ui.returns("sage2"), xpos=0, ypos=0, focus_mask=True)
elif pack_quest_active and not pack_quest_list[8][1]:
    $ ui.imagebutton("ep9_packquest_btn8_idle", "ep9_packquest_btn8_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)


if "ep9_diks_ph3_costume_riona_event_label" in event_list:
    $ ui.imagebutton("ep9_fr_porch_riona_idle", "ep9_fr_porch_riona_hover", clicked=ui.returns("riona"), xpos=0, ypos=0, focus_mask=True)
elif "ep9_diks_ph3_costume_riona_eventb_label" in event_list:
    $ ui.imagebutton("ep9_fr_porch_riona_idle", "ep9_fr_porch_riona_hover", clicked=ui.returns("rionab"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph3_costume_camila_event_label" in event_list:
    $ ui.imagebutton("ep9_fr_porch_camila_idle", "ep9_fr_porch_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

if not persistent.ep9_cardji13:
    $ ui.imagebutton("ep9_fr_porch_card_idle", "ep9_fr_porch_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_left_hall2_label
elif result == "sage":
    stop music fadeout 3
    $ currentEvent = "ep9_diks_ph3_sage_event_label"
    jump startEvent
elif result == "sage2":
    $ currentEvent = "ep9_diks_ph3_sage2_event_label"
    jump startEvent
elif result == "riona":
    $ currentEvent = "ep9_diks_ph3_costume_riona_event_label"
    jump startEvent
elif result == "rionab":
    $ currentEvent = "ep9_diks_ph3_costume_riona_eventb_label"
    jump startEvent
elif result == "camila":
    $ currentEvent = "ep9_diks_ph3_costume_camila_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji13 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep9_diks_ph3_sage_event_label" in event_list or "ep9_diks_ph3_sage2_event_label" in event_list:
        scene ep9_fr_porch with dissolve
    else:
        scene ep9_fr_porchb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_final_diks_porch_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[8][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_rusty_room_label:
$ renpy.block_rollback()
if "ep9_diks_ph3_bm_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_bm_event_label"
    jump startEvent

$ currentFreeRoamLabel = "ep9_diks_ph3_rusty_room_label"
if "ep9_diks_ph3_mj_event_label" in event_list:
    scene ep9_diks_ph3_rusty_room with dissolve
else:
    scene ep9_diks_ph1_rusty_room with dissolve

if "ep9_diks_ph3_mj_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_rusty_josy_idle", "ep9_diks_ph3_rusty_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)

if pack_quest_active and not pack_quest_list[3][1]:
    $ ui.imagebutton("ep9_packquest_btn3_idle", "ep9_packquest_btn3_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_door_idle", "ep9_diks_ph1_rusty_room_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_left_hall_label
elif result == "door":
    jump ep9_diks_ph3_dining_label
elif result == "josy":
    $ currentEvent = "ep9_diks_ph3_mj_event_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[3][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_right_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_right_hall_label"
if "ep9_diks_ph3_db_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_db_event_label"
    jump startEvent
elif "ep9_diks_ph3_riona_event_label" in event_list:
    $ currentFreeRoamLabel = "ep9_diks_ph3_theater_label"
    $ currentEvent = "ep9_diks_ph3_riona_event_label"
    jump startEvent

if "early_freeroam_mutex" in event_list:
    if "ep9_diks_ph3_tara_event_label" in event_list:
        scene ep9_diks_ph3_right_hall with dissolve
    else:
        scene ep9_diks_ph3_right_hall2 with dissolve
else:
    if "ep9_diks_ph3_cari_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_cari_event_label"
        jump startEvent

    if "ep9_diks_ph3_tara_event_label" in event_list:
        scene ep9_diks_ph3_right_hallb with dissolve
    else:
        scene ep9_diks_ph3_right_hall2b with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph3_right_hall_kitchen_idle", "ep9_diks_ph3_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph3_right_hall_bathroom_idle", "ep9_diks_ph3_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph3_tara_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_right_hall_tara_idle", "ep9_diks_ph3_right_hall_tara_hover", clicked=ui.returns("tara"), xpos=0, ypos=0, focus_mask=True)

if "early_freeroam_mutex" in event_list:
    if "ep9_diks_ph3_lily_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_right_hall_envy_idle", "ep9_diks_ph3_right_hall_envy_hover", clicked=ui.returns("nicole"), xpos=0, ypos=0, focus_mask=True)
    elif "ep9_diks_ph3_costume_nl_event_label" in event_list or "ep9_diks_ph3_costume_nl_eventb_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_right_hall_envy_idle", "ep9_diks_ph3_right_hall_envy_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_diks_ph3_right_hall_theater_idle", "ep9_diks_ph3_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph3_room_event_label" in event_list or (not "early_freeroam_mutex" in event_list and "ep9_diks_ph3_mj_event_label" not in event_list):
    $ ui.imagebutton("ep9_diks_ph3_right_hall_library_idle", "ep9_diks_ph3_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)


$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_main_label
elif result == "theater":
    jump ep9_diks_ph3_theater_label
elif result == "library":
    if "ep9_diks_ph3_room_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_room_event_label"
        jump startEvent
    else:
        jump ep9_diks_ph3_lib_right_label
elif result == "kitchen":
    jump ep9_diks_ph3_kitchen_label
elif result == "nicole":
    $ currentEvent = "ep9_diks_ph3_lily_event_label"
    jump startEvent
elif result == "tara":
    $ currentEvent = "ep9_diks_ph3_tara_event_label"
    jump startEvent
elif result == "lily":
    if "ep9_diks_ph3_costume_nl_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_nl_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_nl_eventb_label"
    jump startEvent
elif result == "bathroom":
    jump ep9_diks_ph3_bathroom_label

label ep9_diks_ph3_theater_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_theater_label"

if "ep9_diks_ph3_prepsg_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_prepsg_event_label"
    jump startEvent

if "ep9_diks_ph3_costume_derek_event_label" in event_list or "ep9_diks_ph3_costume_derek_eventb_label" in event_list:
    if "ep9_diks_ph3_prepsg_event_label" in event_list or "ep9_diks_ph3_preps_event_label" in event_list:
        scene ep9_diks_ph3_theater_both with dissolve
    else:
        scene ep9_diks_ph3_theater with dissolve
else:
    if "ep9_diks_ph3_prepsg_event_label" in event_list or "ep9_diks_ph3_preps_event_label" in event_list:
        scene ep9_diks_ph3_theater_empty with dissolve
    else:
        scene ep9_diks_ph3_theaterb with dissolve


if "ep9_diks_ph3_costume_derek_event_label" in event_list or "ep9_diks_ph3_costume_derek_eventb_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_derek_idle", "ep9_diks_ph3_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=200 * persistent.scale_factor, ypos=450 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph3_theater2_label
elif result == "go_down":
    jump ep9_diks_ph3_right_hall_label
elif result == "derek":
    if "ep9_diks_ph3_costume_derek_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_derek_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_derek_eventb_label"
    jump startEvent

label ep9_diks_ph3_theater2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_theater2_label"

scene ep9_diks_ph1_theater2 with dissolve
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_left":
    jump ep9_diks_ph3_theater_label

label ep9_diks_ph3_leon_room_label:
if not persistent.ep9_cardji15:
    if "ep9_diks_ph3_heather_event_label" in event_list:
        scene ep9_diks_ph3_leon_room_card with dissolve
    else:
        scene ep9_diks_ph3_leon_roomb_card with dissolve
else:
    if "ep9_diks_ph3_heather_event_label" in event_list:
        scene ep9_diks_ph3_leon_room with dissolve
    else:
        scene ep9_diks_ph3_leon_roomb with dissolve
label ep9_diks_ph3_leon_room_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_leon_room_label"

if "ep9_diks_ph3_heather_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_leon_heather_idle", "ep9_diks_ph3_leon_heather_hover", clicked=ui.returns("heather"), xpos=0, ypos=0, focus_mask=True)
elif pack_quest_active and not pack_quest_list[4][1]:
    $ ui.imagebutton("ep9_packquest_btn4_idle", "ep9_packquest_btn4_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardji15:
    $ ui.imagebutton("ep9_diks_ph3_leon_room_card_idle", "ep9_diks_ph3_leon_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=650 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_mainup_label
elif result == "heather":
    $ currentEvent = "ep9_diks_ph3_heather_event_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[4][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardji15 = True
    $ persistent.rew_jill_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep9_diks_ph3_heather_event_label" in event_list:
        scene ep9_diks_ph3_leon_room with dissolve
    else:
        scene ep9_diks_ph3_leon_roomb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph3_leon_room_label_nofx

label ep9_diks_ph3_toilet_2nd_label:
$ renpy.block_rollback()
if "ep9_diks_ph3_sally_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_sally_event_label"
    jump startEvent
$ currentFreeRoamLabel = "ep9_diks_ph3_toilet_2nd_label"
scene ep9_diks_ph3_toilet_2nd with dissolve

if pack_quest_active and not pack_quest_list[1][1]:
    $ ui.imagebutton("ep9_packquest_btn1_idle", "ep9_packquest_btn1_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_1corr_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[1][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_bathroom_label"
if "ep9_diks_ph3_elena_event_label" in event_list and not "early_freeroam_mutex" in event_list:
    $ currentEvent = "ep9_diks_ph3_elena_event_label"
    jump startEvent
scene ep9_diks_ph3_bathroom with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_right_hall_label

label ep9_diks_ph3_dining_label:
$ renpy.block_rollback()
if "ep9_diks_ph3_costume_sm_event_label" in event_list or "ep9_diks_ph3_costume_sm_eventb_label" in event_list:
    scene ep9_diks_ph3_dining_ml with dissolve
elif optional_task_list[8] == "Talk to Sarah & Melanie" or optional_task_list[8] == "Talk to Sarah & Melanie (Kitchen)":
    scene ep9_diks_ph3_dining_ml2 with dissolve
else:
    scene ep9_diks_ph3_dining with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph3_dining_label"

if "ep9_diks_ph3_costume_sm_event_label" in event_list or "ep9_diks_ph3_costume_sm_eventb_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_dining_sarah_idle", "ep9_diks_ph3_dining_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_dining_stairs2_idle", "ep9_diks_ph3_dining_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_diks_ph3_dining_stairs_idle", "ep9_diks_ph3_dining_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph3_dining_rdoor_idle", "ep9_diks_ph3_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph3_dining_jdoor_idle", "ep9_diks_ph3_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph3_kitchen_label
elif result == "stairs":
    jump ep9_diks_ph3_upper_2dining_label
elif result == "rusty":
    jump ep9_diks_ph3_rusty_room_label
elif result == "jamie":
    jump ep9_diks_ph3_jamie_label
elif result == "sarah":
    if "ep9_diks_ph3_costume_sm_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_sm_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_sm_eventb_label"
    jump startEvent

label ep9_diks_ph3_upper_2dining_label:
$ renpy.block_rollback()
scene ep9_diks_ph3_upper_2dining with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph3_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_jacob_idle", "ep9_diks_ph1_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_nick_idle", "ep9_diks_ph1_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_jb_label
elif result == "stairs":
    jump ep9_diks_ph3_dining_label
elif result == "nick":
    jump ep9_diks_ph3_nick_label
elif result == "jacob":
    jump ep9_diks_ph3_jacob_label

label ep9_diks_ph3_kitchen_label:
if optional_task_list[8] == "Talk to Sarah & Melanie" or optional_task_list[8] == "Talk to Sarah & Melanie (Kitchen)":
    scene ep9_diks_ph3_kitchen_sm with dissolve
else:
    scene ep9_diks_ph3_kitchen with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_kitchen_label"

if optional_task_list[8] == "Talk to Sarah & Melanie" or optional_task_list[8] == "Talk to Sarah & Melanie (Kitchen)":
    $ ui.imagebutton("ep9_diks_ph3_kitchen_sarah_idle", "ep9_diks_ph3_kitchen_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_dining_label
elif result == "go_right":
    jump ep9_diks_ph3_right_hall_label
elif result == "sarah":
    if "ep9_diks_ph3_sm_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_sm_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_sm_eventb_label"
    jump startEvent

label ep9_diks_ph3_jb_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_jb_label"
scene ep9_diks_ph3_jb with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_1corr_label
elif result == "go_up":
    jump ep9_diks_ph3_upper_2dining_label

label ep9_diks_ph3_nick_label:
scene ep9_diks_ph1_nick with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_nick_label"

if pack_quest_active and not pack_quest_list[7][1]:
    $ ui.imagebutton("ep9_packquest_btn7_idle", "ep9_packquest_btn7_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep9_diks_ph3_upper_2dining_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[7][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_jacob_label:
if "ep9_diks_ph3_becky_event_label" in event_list:
    scene ep9_diks_ph3_jacobb with dissolve
else:
    scene ep9_diks_ph3_jacob with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_jacob_label"

if "ep9_diks_ph3_becky_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_jacob_becky_idle", "ep9_diks_ph3_jacob_becky_hover", clicked=ui.returns("becky"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_upper_2dining_label
elif result == "becky":
    $ currentEvent = "ep9_diks_ph3_becky_event_label"
    jump startEvent


label ep9_diks_ph3_tommy_label:
show screen dance_filter_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_tommy_label"

if "ep9_diks_ph3_zoey2_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_zoey2_event_label"
    jump startEvent
elif "early_freeroam_mutex" in event_list:
    if "ep9_diks_ph3_jacob_event_label" in event_list or "ep9_diks_ph3_becky_event_label" in event_list:
        if "ep9_diks_ph3_prepsl_event_label" in event_list or ep9_prep_truce:
            scene ep9_diks_ph3_tommy_roomb with dissolve
        else:
            scene ep9_diks_ph3_tommy_roomb_noprep with dissolve
    else:
        if "ep9_diks_ph3_prepsl_event_label" in event_list or ep9_prep_truce:
            scene ep9_diks_ph3_tommy_room with dissolve
        else:
            scene ep9_diks_ph3_tommy_room_noprep with dissolve
else:
    if "ep9_diks_ph3_prepsl_event_label" in event_list or ep9_prep_truce:
        scene ep9_diks_ph3_tommy_roomc with dissolve
    else:
        scene ep9_diks_ph3_tommy_roomc_noprep with dissolve

if "ep9_diks_ph3_jacob_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph3_tommy_jacob_idle", "ep9_diks_ph3_tommy_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)

if "ep9_diks_ph3_jacob_event_label" in event_list or "ep9_diks_ph3_becky_event_label" in event_list:
    if "ep9_diks_ph3_costume_leon_event_label" in event_list or "ep9_diks_ph3_costume_leon_eventb_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_leonb_idle", "ep9_diks_ph3_tommy_leonb_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
    if "ep9_diks_ph3_rusty_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_sandyb_idle", "ep9_diks_ph3_tommy_sandyb_hover", clicked=ui.returns("sandy"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep9_diks_ph3_rusty_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_sandy_idle", "ep9_diks_ph3_tommy_sandy_hover", clicked=ui.returns("sandy"), xpos=0, ypos=0, focus_mask=True)
    if "ep9_diks_ph3_costume_leon_event_label" in event_list or "ep9_diks_ph3_costume_leon_eventb_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_leon_idle", "ep9_diks_ph3_tommy_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_diks_ph3_tommy_curtain_idle", "ep9_diks_ph3_tommy_curtain_hover", clicked=ui.returns("curtain"), xpos=0, ypos=0, focus_mask=True)

if "early_freeroam_mutex" in event_list:
    if "ep9_diks_ph3_prepsl_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_lucas2_idle", "ep9_diks_ph3_tommy_lucas2_hover", clicked=ui.returns("lucas"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep9_diks_ph3_prepsl_event_label" in event_list:
        $ ui.imagebutton("ep9_diks_ph3_tommy_lucas_idle", "ep9_diks_ph3_tommy_lucas_hover", clicked=ui.returns("lucas"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep9_diks_ph3_tommy_girls_idle", "ep9_diks_ph3_tommy_girls_hover", clicked=ui.returns("girls"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    hide screen dance_filter_screen
    jump ep9_diks_ph3_left_hall2_label
elif result == "curtain":
    hide screen dance_filter_screen
    jump ep9_diks_ph3_tommy2_label
elif result == "jacob":
    $ currentEvent = "ep9_diks_ph3_jacob_event_label"
    jump startEvent
elif result == "girls":
    mc "(It's getting late. Guests are either leaving or passing out, it seems. Just look at those {color=#00ff00}2{/color}.)"
    jump ep9_diks_ph3_tommy_label
elif result == "leon":
    if "ep9_diks_ph3_costume_leon_event_label" in event_list:
        $ currentEvent = "ep9_diks_ph3_costume_leon_event_label"
    else:
        $ currentEvent = "ep9_diks_ph3_costume_leon_eventb_label"
    jump startEvent
elif result == "sandy":
    $ currentEvent = "ep9_diks_ph3_rusty_event_label"
    jump startEvent
elif result == "lucas":
    $ currentEvent = "ep9_diks_ph3_prepsl_event_label"
    jump startEvent

label ep9_diks_ph3_tommy2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph3_tommy2_label"
scene ep9_diks_ph3_tommy2 with dissolve

if pack_quest_active and not pack_quest_list[2][1]:
    $ ui.imagebutton("ep9_packquest_btn2_idle", "ep9_packquest_btn2_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_tommy_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[2][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep9_diks_ph3_jamie_label:
$ renpy.block_rollback()
if "ep9_diks_ph3_penny_event_label" in event_list:
    $ currentEvent = "ep9_diks_ph3_penny_event_label"
    jump startEvent
$ currentFreeRoamLabel = "ep9_diks_ph3_jamie_label"
scene ep9_diks_ph3_jamie with dissolve
if pack_quest_active and not pack_quest_list[6][1]:
    $ ui.imagebutton("ep9_packquest_btn6_idle", "ep9_packquest_btn6_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_jamie_door_idle", "ep9_diks_ph1_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph3_left_hall_label
elif result == "door":
    jump ep9_diks_ph3_dining_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[6][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label ep12_freeroam_party_label:
$ freeRoamID = "ep12_3"
$ roosterState = "ep12_3"
$ tmpInt = 0
$ guideSuggestedPage = 258
$ found_money = False
$ found_money2 = False
$ bn_money_reward = True
show screen wt_tasks_shown
$ disabled_apps = ["brawler"]
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

call mphone_check_pack_quest_available from _call_mphone_check_pack_quest_available_3
$ rooster_jump_label = "ep12_np_dining_label"

$ map_system_list = []
$ map_system_list.append(["ep12_np_2f_corridor","ep12_np_2f_corridor_label","2F corridor"])
$ map_system_list.append(["ep12_np_corridor","ep12_np_corridor_label","3F corridor"])
$ map_system_list.append(["ep12_np_balcony","ep12_np_balcony_label","Balcony"])
$ map_system_list.append(["ep12_np_party_room","ep12_np_party_room_label","Dance floor"])
$ map_system_list.append(["ep12_np_dining","ep12_np_dining_label","Dining room"])
$ map_system_list.append(["ep12_np_outside","ep12_np_outside_label","Outside"])

jump initRoosterLabel

label ep12_np_dining_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_np_dining_label"
if "ep12_np_josy_label" in event_list:
    $ currentEvent = "ep12_np_josy_label"
    jump startEvent
if "ep12_np_zmc_label" in event_list:
    $ currentEvent = "ep12_np_zmc_label"
    jump startEvent
if "ep12_np2_mchen_label" in event_list:
    $ currentEvent = "ep12_np2_mchen_label"
    jump startEvent
if "part2" in event_list:
    if persistent.ep12_cardisa3:
        scene ep12_np_dining2
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_dining2_card
        hide screen dance_filter_screen
        with dissolve
else:
    if persistent.ep12_cardisa3:
        scene ep12_np_dining
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_dining_card
        hide screen dance_filter_screen
        with dissolve
label ep12_np_dining_label_nofx:

if firstTimeFreeRoam:
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ chat_new_tasks = True
    if "part2" in event_list:

        $ map_system_list = []
        $ map_system_list.append(["ep12_np_2f_corridor","ep12_np_2f_corridor_label","2F corridor"])
        $ map_system_list.append(["ep12_np_corridor2","ep12_np_corridor_label","3F corridor"])
        $ map_system_list.append(["ep12_np_balconyb","ep12_np_balcony_label","Balcony"])
        $ map_system_list.append(["ep12_np_party_roomb","ep12_np_party_room_label","Dance floor"])
        $ map_system_list.append(["ep12_np_dining2","ep12_np_dining_label","Dining room"])
        $ map_system_list.append(["ep12_np_outsideb","ep12_np_outside_label","Outside"])

        if persistent.mod_wtenabled:
            $ task_list = ["Talk to Rusty (Balcony)", "", "Find Anthony (Balcony)", "Find Riona (Balcony)","","Find Chad (2F corridor)", "Find Quinn (Dining room)", "Find Derek (Dance floor)","","","Find Heather (Dancefloor)","Talk to Sally (Dance floor)","",""]
        else:
            $ task_list = ["Talk to Rusty", "", "Find Anthony", "Find Riona","","Find Chad", "Find Quinn", "Find Derek","","","Find Heather","Talk to Sally","",""]
        if persistent.mod_wtenabled:
            $ optional_task_list = ["Talk to Jamie (3F corridor)", "Find Arieth (Dancefloor)", "Talk to Kylie and Penny (Balcony)", "Find Becky (3F corridor)"]
        else:
            $ optional_task_list = ["Talk to Jamie", "Find Arieth", "Talk to Kylie and Penny", "Find Becky"]
        $ event_list.append("ep12_np2_bc_label")
        $ event_list.append("ep12_np2_jaj_label")
        $ event_list.append("ep12_np2_rdm_label")
        $ event_list.append("ep12_np2_an_label")
        $ event_list.append("ep12_np2_rq_label")
        $ event_list.append("ep12_np2_tc_label")
        $ event_list.append("ep12_np2_ht_label")
        $ event_list.append("ep12_np2_qsm_label")
        $ event_list.append("ep12_np2_ad_label")
        $ event_list.append("ep12_np2_jsl_label")
        $ event_list.append("ep12_np2_had_label")
        $ event_list.append("ep12_np2_sally_label")
        $ event_list.append("ep12_np2_kp_label")
        if ep11_elena_lewd:
            $ event_list.append("ep12_np2_elena_label")
            if persistent.mod_wtenabled: 
                $ task_list[12] = "Talk to Elena (Balcony)"
            else:
                $ task_list[12] = "Talk to Elena"
        if not branchZoey:
            $ event_list.append("ep12_np2_zu_label")
            if persistent.mod_wtenabled:
                $ task_list[9] = "Talk to Zoey (Dance floor)"
            else:
                $ task_list[9] = "Talk to Zoey"
        if branchMayaJosy and not breakup:
            if persistent.mod_wtenabled:
                $ task_list[8] = "Find Josy and Maya (Dance floor)"
            else:
                $ task_list[8] = "Find Josy and Maya"
            $ event_list.append("ep12_np2_jmd_label")
        if branchJill and not breakup and (tc < 10 or persistent.no_cheater):
            if persistent.mod_wtenabled:
                if branchMayaJosy:
                    $ task_list[8] += "\nTalk to Jill (Dance floor)"
                else:
                    $ task_list[8] = "Talk to Jill (Dance floor)"
            else:
                 if branchMayaJosy:
                    $ task_list[8] += "\nTalk to Jill"
                 else:
                    $ task_list[8] = "Talk to Jill"
                
            $ event_list.append("ep12_np2_ji_label")

        if ep12_nikita:
            $ event_list.append("ep12_np2_nik_label")
            if persistent.mod_wtenabled:
                $ task_list[4] = "Talk to Nikita (Balcony)"
            else:
                $ task_list[4] = "Talk to Nikita"
        if breakup and not "Josy" in breakup:
            
            $ event_list.append("ep12_np2_jomc_label")
            if persistent.mod_wtenabled:
                if task_list[8] == "":
                    $ task_list[8] = "Talk to Josy (Dance floor)"
                else:
                    $ task_list[8] += "\nTalk to Josy (Dance floor)"
            else:
                if task_list[8] != "":
                    $ task_list[8] += "\nTalk to Josy"
                else:
                    $ task_list[8] = "Talk to Josy"
        if ep12_rolling:
            $ event_list.append("ep12_np2_lily_label")
            if persistent.mod_wtenabled:
                if task_list[8] != "":
                    $ task_list[8] += "\nFind Lily (Dance floor)"
                else:
                    $ task_list[8] = "Find Lily (Dance floor)"
            else:
              if task_list[8] != "":
                $ task_list[8] += "\nFind Lily"
              else:
                $ task_list[8] = "Find Lily"

        $ updateTaskList()
    else:
        hide screen new_phone_screen
        if persistent.mod_wtenabled:
            $ task_list = ["Talk to Leon (Bathroom)","","Talk to Derek (Dining room)", "Talk to Rusty (Dining room)", "","", "Go to the 3F corridor","Find Sarah (3F corridor)", "Talk to Jacob (Outside)", "Talk to Elena (Balcony)","Find Avery (Balcony)", "","","","","Talk to Chad (Dance floor)","","Find Josy and Bella (3F corridor)"]
        else:
            $ task_list = ["Talk to Leon","","Talk to Derek", "Talk to Rusty", "","", "Go to the 3F corridor","Find Sarah", "Talk to Jacob", "Talk to Elena","Find Avery", "","","","","Talk to Chad","","Find Josy and Bella"]
        if persistent.mod_wtenabled:
            $ optional_task_list = ["","", "Talk to Pink Rose girls (3F corridor)","Talk to Camila (Dance floor)","","",""]
        else:
            $ optional_task_list = ["","", "Talk to Pink Rose girls ","Talk to Camila ","","",""]

        $ event_list = []
        if ep11_tara_lewd and (not branchZoey or wt_ep11_zoey_kiss_others):
            $ event_list.append("ep12_np_tara_label")
            if persistent.mod_wtenabled:
                $ optional_task_list[6] = "Talk to Tara (Dance floor)"
            else:
                $ optional_task_list[6] = "Talk to Tara"
        if ep12_bianca_lewd or ep11_bianca_path:
            $ event_list.append("ep12_np_bianca_label")
            if persistent.mod_wtenabled:
                $ task_list[16] = "Talk to Bianca (Dance floor)"
            else:
                $ task_list[16] = "Talk to Bianca"
        if ep12_nicole_path and not ep12_nicole_breakup or ep12_nicole_breakup:
            if ep12_nicole_path and not ep12_nicole_breakup:
                if persistent.mod_wtenabled:
                    $ task_list[1] = "Talk to Nicole (Dining room)"
                else:
                    $ task_list[1] = "Talk to Nicole"
            $ event_list.append("ep12_np_nicmc_label")
        if ep11_jade_lewd:
            $ event_list.append("ep12_np_ja_label")
            if persistent.mod_wtenabled:
                $ optional_task_list[0] = "Find Jade (Dining room)"
            else:
                $ optional_task_list[0] = "Find Jade"
        if (ep8_jill_state == 1 and ep9_saw_matthew) or branchJill:
            $ event_list.append("ep12_np_om_label")
            if persistent.mod_wtenabled:
                $ task_list[11] = "Find Matthew (Balcony)"
            else:
                $ task_list[11] = "Find Matthew"

        if ep11_quinn_question[0] and ep11_quinn_question[1] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch and (not branchZoey or wt_ep11_zoey_kiss_others):
            $ event_list.append("ep12_np_qmc_label")
            if persistent.mod_wtenabled:
                $ task_list[14] = "Talk to Quinn (Dance floor)"
            else:
                $ task_list[14] = "Talk to Quinn"
        if ep12_nikita:
            $ event_list.append("ep12_np_nikita_label")
            if persistent.mod_wtenabled:
                $ optional_task_list[4] = "Find Nikita (Dance floor)"
            else:
                $ optional_task_list[4] = "Find Nikita"

        $ event_list.append("ep12_np_fem_label")
        $ event_list.append("ep12_np_rtb_label")
        $ event_list.append("ep12_np_bj_label")
        $ event_list.append("ep12_np_ca_label")

        $ event_list.append("ep12_np_mia_label")
        $ event_list.append("ep12_np_cf_label")
        $ event_list.append("ep12_np_de_label")
        $ event_list.append("ep12_np_rj_label")
        $ event_list.append("ep12_np_nick_label")
        $ event_list.append("ep12_np_beer_label")
        $ event_list.append("ep12_np_jj_label")
        $ event_list.append("ep12_np_he_label")
        $ event_list.append("ep12_np_cal_label")
        $ event_list.append("ep12_np_cam_label")
        $ event_list.append("ep12_np_mcc_label")
        $ event_list.append("ep12_np_dwa_label")
        $ event_list.append("ep12_np_dj_label")

        if ep12_rolling:
            $ event_list.append("ep12_np_ly_label")
        $ event_list.append("ep12_np_lmc_label")

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

if "part2" in event_list:
    $ ui.imagebutton("ep12_np_dining_door2_idle", "ep12_np_dining_door2_hover", clicked=ui.returns("corridor"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_dining_door_idle", "ep12_np_dining_door_hover", clicked=ui.returns("corridor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep12_np_dining_toilet_idle", "ep12_np_dining_toilet_hover", clicked=ui.returns("toilet"), xpos=0, ypos=0, focus_mask=True)
if "part2" in event_list:
    $ ui.imagebutton("ep12_np_dining_table2_idle", "ep12_np_dining_table2_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_dining_table_idle", "ep12_np_dining_table_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep12_cardisa3:
    $ ui.imagebutton("ep12_np_dining_card_idle", "ep12_np_dining_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_nicmc_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_nicole_idle", "ep12_np_dining_nicole_hover", clicked=ui.returns("nicole"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_cf_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_felicia_idle", "ep12_np_dining_felicia_hover", clicked=ui.returns("felicia"), xpos=0, ypos=0, focus_mask=True)

if not persistent.ep12_cardisa3:
    $ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"),xpos=160 * persistent.scale_factor, ypos=840 * persistent.scale_factor)
else:
    $ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "toilet":
    jump ep12_np_bathroom_label
elif result == "table":
    jump ep12_np_dining_table_label
elif result == "corridor":
    jump ep12_np_corridor_label
elif result == "go_down":
    jump ep12_np_dining_down_label
elif result == "nicole":
    $ currentEvent = "ep12_np_nicmc_label"
    jump startEvent
elif result == "felicia":
    $ currentEvent = "ep12_np_cf_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa3 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep12_np_dining2 with dissolve
    else:
        scene ep12_np_dining with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_dining_label_nofx

label ep12_np_dining_table_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_np_dining_table_label"
if "part2" in event_list:
    scene ep12_np_dining_tablec
    hide screen dance_filter_screen
    with dissolve
else:
    if "table" in event_list:
        scene ep12_np_dining_table
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_dining_tableb
        hide screen dance_filter_screen
        with dissolve

if "ep12_np_btable_label" in event_list:
    $ ui.imagebutton("ep12_np_btable_idle", "ep12_np_btable_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
if "part2" in event_list:
    $ ui.imagebutton("ep12_np_btable_drinks_idle", "ep12_np_btable_drinks_hover", clicked=ui.returns("drinks"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep12_np_dining_label
elif result == "table":
    $ currentEvent = "ep12_np_btable_label"
    jump startEvent
elif result == "drinks":
    mc "({color=00ff00}Five{/color} different types of liquor, yet people are mostly drinking sparkling wine and beer.)"
    jump ep12_np_dining_table_label

label ep12_np_dining_down_label:
$ currentFreeRoamLabel = "ep12_np_dining_down_label"
if "part2" in event_list:
    if "ep12_np2_cg_label" in event_list:
        $ currentEvent = "ep12_np2_cg_label"
        jump startEvent
    if freeRoamID == "ep12_3c":
        scene ep12_np_dining_down2b
        if "ACTIVE" in ep12_jewels and "blue" not in ep12_jewels and "BLUE" not in ep12_jewels:
            show ep12_blue_jewel_idle
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_dining_down2
        hide screen dance_filter_screen
        with dissolve
else:
    if maya_shiny_dress:
        scene ep12_np_dining_down
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_dining_downb
        hide screen dance_filter_screen
        with dissolve
$ renpy.block_rollback()

if "ep12_np2_qsm_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_quinn_idle", "ep12_np_dining_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_de_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_derek_idle", "ep12_np_dining_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_rj_label" in event_list or "ep12_np_rkey_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_rusty_idle", "ep12_np_dining_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_ly_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_lily_idle", "ep12_np_dining_lily_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_maya_label" in event_list:
    if maya_shiny_dress:
        $ ui.imagebutton("ep12_np_dining_maya_idle", "ep12_np_dining_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_dining_mayab_idle", "ep12_np_dining_mayab_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_jkey_label" in event_list or "ep12_np_ja_label" in event_list:
    $ ui.imagebutton("ep12_np_dining_jade_idle", "ep12_np_dining_jade_hover", clicked=ui.returns("jade"), xpos=0, ypos=0, focus_mask=True)
if "ACTIVE" in ep12_jewels and "blue" not in ep12_jewels and "BLUE" not in ep12_jewels:
    $ ui.imagebutton("ep12_blue_jewel_idle", "ep12_blue_jewel_idle", clicked=ui.returns("blue"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[0][1]:
    if "part2" in event_list:
        $ ui.imagebutton("ep12_packquest_btn0_idle", "ep12_packquest_btn0_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "derek":
    $ currentEvent = "ep12_np_de_label"
    jump startEvent
elif result == "rusty":
    if "ep12_np_rj_label" in event_list:
        $ currentEvent = "ep12_np_rj_label"
    else:
        $ currentEvent = "ep12_np_rkey_label"
    jump startEvent
elif result == "lily":
    $ currentEvent = "ep12_np_ly_label"
    jump startEvent
elif result == "blue":
    $ ep12_jewels.append("blue")
    jump ep12_np_dining_down_label
elif result == "quinn":
    $ currentEvent = "ep12_np2_qsm_label"
    jump startEvent
elif result == "maya":
    $ currentEvent = "ep12_np_maya_label"
    jump startEvent
elif result == "jade":
    if "ep12_np_ja_label" in event_list:
        $ currentEvent = "ep12_np_ja_label"
    else:
        $ currentEvent = "ep12_np_jkey_label"
    jump startEvent
elif result == "go_down":
    jump ep12_np_dining_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[0][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep12_np_bathroom_label:
if "ep12_np2_jd_label" in event_list:
    $ currentFreeRoamLabel = "ep12_np_bathroom_label"
    $ currentEvent = "ep12_np2_jd_label"
    jump startEvent
if "part2" in event_list:
    if persistent.ep12_cardisa2:
        scene ep12_np_bathroomb
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_bathroomb_card
        hide screen dance_filter_screen
        with dissolve
else:
    if persistent.ep12_cardisa2:
        scene ep12_np_bathroom
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_bathroom_card
        hide screen dance_filter_screen
        with dissolve
label ep12_np_bathroom_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_np_bathroom_label"

if not persistent.ep12_cardisa2:
    $ ui.imagebutton("ep12_np_bathroom_card_idle", "ep12_np_bathroom_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_lmc_label" in event_list:
    $ ui.imagebutton("ep12_np_bathroom_leon_idle", "ep12_np_bathroom_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)

if "part2" in event_list:
    $ ui.imagebutton("ep12_np_bathroom_stall2_idle", "ep12_np_bathroom_stall2_hover", clicked=ui.returns("stall"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_bathroom_stall_idle", "ep12_np_bathroom_stall_hover", clicked=ui.returns("stall"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep12_np_dining_label
elif result == "go_right":
    jump ep12_np_bathroom2_label
elif result == "stall":
    jump ep12_np_stall_label
elif result == "leon":
    $ currentEvent = "ep12_np_lmc_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa2 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep12_np_bathroomb with dissolve
    else:
        scene ep12_np_bathroom with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_bathroom_label_nofx

label ep12_np_bathroom2_label:
if persistent.ep12_cardisa20:
    if "part2" in event_list:
        scene ep12_np_bathroom2b
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_bathroom2
        hide screen dance_filter_screen
        with dissolve
else:
    if "part2" in event_list:
        scene ep12_np_bathroom2b_card
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_bathroom2_card
        hide screen dance_filter_screen
        with dissolve
label ep12_np_bathroom2_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_np_bathroom2_label"

if pack_quest_active and not pack_quest_list[3][1]:
    $ ui.imagebutton("ep12_packquest_btn3_idle", "ep12_packquest_btn3_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep12_cardisa20:
    $ ui.imagebutton("ep12_np_bathroom2_card_idle", "ep12_np_bathroom2_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep12_np_bathroom_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[3][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa20 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep12_np_bathroom2b with dissolve
    else:
        scene ep12_np_bathroom2 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_bathroom2_label_nofx

label ep12_np_stall_label:
if "part2" in event_list:
    if found_money2:
        scene ep12_np_stallb with dissolve
    else:
        scene ep12_np_stallb_money with dissolve
else:
    scene ep12_np_stall with dissolve

label ep12_np_stall_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_np_stall_label"

if pack_quest_active and not pack_quest_list[2][1]:
    if "part2" in event_list:
        $ ui.imagebutton("ep12_packquest_btn2_idle", "ep12_packquest_btn2_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if "part2" in event_list:
    if not found_money2:
        $ ui.imagebutton("ep12_np_stallb_money_idle", "ep12_np_stallb_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep12_np_bathroom_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[2][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep12_np_stallb with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep12_np_stall_label_nofx

label ep12_np_corridor_label:
$ currentFreeRoamLabel = "ep12_np_corridor_label"

if "ep12_np_nick_label" in event_list:
    $ currentEvent = "ep12_np_nick_label"
    jump startEvent
if "ep12_np2_bc_label" in event_list:
    $ currentEvent = "ep12_np2_bc_label"
    jump startEvent
if "ep12_np2_ari_label" in event_list:
    $ currentEvent = "ep12_np2_ari_label"
    jump startEvent

if "part2" in event_list:
    if "ep12_np2_dr_label" in event_list:
        if persistent.ep12_cardisa4:
            scene ep12_np_corridor2b
        else:
            scene ep12_np_corridor2b_card
        hide screen dance_filter_screen
        with dissolve
    else:
        if persistent.ep12_cardisa4:
            scene ep12_np_corridor2
        else:
            scene ep12_np_corridor2_card
        hide screen dance_filter_screen
        with dissolve
else:
    if current_task == "Greet Riona"  or current_task == "Greet Riona (3F corridor)":
        if persistent.ep12_cardisa4:
            scene ep12_np_corridorb
        else:
            scene ep12_np_corridorb_card
        hide screen dance_filter_screen
        with dissolve
    else:
        if persistent.ep12_cardisa4:
            scene ep12_np_corridor
        else:
            scene ep12_np_corridor_card
        hide screen dance_filter_screen
        with dissolve
$ renpy.block_rollback()
label ep12_np_corridor_label_nofx:
$ currentFreeRoamLabel = "ep12_np_corridor_label"

if "ep12_np2_ot_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor2_oscar_idle", "ep12_np_corridor2_oscar_hover", clicked=ui.returns("oscar"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_jaj_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor2_jaj_idle", "ep12_np_corridor2_jaj_hover", clicked=ui.returns("jaj"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_dr_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor2_dwy_idle", "ep12_np_corridor2_dwy_hover", clicked=ui.returns("dwyane"), xpos=0, ypos=0, focus_mask=True)

if current_task == "Greet Riona" or current_task == "Greet Riona (3F corridor)":
    $ ui.imagebutton("ep12_np_corridor_rio_idle", "ep12_np_corridor_rio_hover", clicked=ui.returns("riona"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_bj_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor_bj_idle", "ep12_np_corridor_bj_hover", clicked=ui.returns("bj"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_rtb_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor_pr_idle", "ep12_np_corridor_pr_hover", clicked=ui.returns("pr"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_ca_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor_caleb_idle", "ep12_np_corridor_caleb_hover", clicked=ui.returns("caleb"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_fem_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor_sarah_idle", "ep12_np_corridor_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)

if "part2" in event_list:
    $ ui.imagebutton("ep12_np_corridor_door2_idle", "ep12_np_corridor_door2_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_corridor_door_idle", "ep12_np_corridor_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

if "part2" in event_list:
    $ ui.imagebutton("ep12_np_corridor_balcony2_idle", "ep12_np_corridor_balcony2_hover", clicked=ui.returns("balcony"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_corridor_balcony_idle", "ep12_np_corridor_balcony_hover", clicked=ui.returns("balcony"), xpos=0, ypos=0, focus_mask=True)
if current_task == "Greet Riona" or current_task == "Greet Riona (3F corridor)":
    $ ui.imagebutton("ep12_np_corridor_stairs2_idle", "ep12_np_corridor_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_corridor_stairs_idle", "ep12_np_corridor_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

if not persistent.ep12_cardisa4:
    $ ui.imagebutton("ep12_np_corridor_card_idle", "ep12_np_corridor_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)


if "part2" in event_list:
    if "ep12_np2_dr_label" in event_list:
        $ ui.imagebutton("ep12_np_corridor_plana_idle", "ep12_np_corridor_plana_hover", clicked=ui.returns("plan"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_corridor_planb_idle", "ep12_np_corridor_planb_hover", clicked=ui.returns("plan"), xpos=0, ypos=0, focus_mask=True)
else:
    if current_task == "Greet Riona" or current_task == "Greet Riona (3F corridor)":
        $ ui.imagebutton("ep12_np_corridor_planc_idle", "ep12_np_corridor_planc_hover", clicked=ui.returns("plan"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_corridor_pland_idle", "ep12_np_corridor_pland_hover", clicked=ui.returns("plan"), xpos=0, ypos=0, focus_mask=True)

if pack_quest_active and not pack_quest_list[1][1]:
    if "part2" in event_list:
        if "ep12_np2_dr_label" in event_list:
            $ ui.imagebutton("ep12_packquest_btn1b_idle", "ep12_packquest_btn1b_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep12_packquest_btn1a_idle", "ep12_packquest_btn1a_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "balcony":
    jump ep12_np_balcony_label
elif result == "door":
    jump ep12_np_party_room_label
elif result == "plan":
    mc "(Those are the seating plans for the {color=00ff00}two{/color} dining halls. One for the DIKs and one for the jocks.)"
    jump ep12_np_corridor_label
elif result == "stairs":
    jump ep12_np_2f_corridor_label
elif result == "sarah":
    $ currentEvent = "ep12_np_fem_label"
    jump startEvent
elif result == "caleb":
    $ currentEvent = "ep12_np_ca_label"
    jump startEvent
elif result == "pr":
    $ currentEvent = "ep12_np_rtb_label"
    jump startEvent
elif result == "bj":
    $ currentEvent = "ep12_np_bj_label"
    jump startEvent
elif result == "jaj":
    $ currentEvent = "ep12_np2_jaj_label"
    jump startEvent
elif result == "oscar":
    $ currentEvent = "ep12_np2_ot_label"
    jump startEvent
elif result == "dwyane":
    $ currentEvent = "ep12_np2_dr_label"
    jump startEvent
elif result == "riona":
    menu:
        "Start dinner":
            $ currentEvent = "ep12_np_dinner_label"
            jump startEvent
        "Not yet":
            jump ep12_np_corridor_label
elif result == "go_down":
    jump ep12_np_dining_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[1][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa4 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

    if "part2" in event_list:
        if "ep12_np2_dr_label" in event_list:
            scene ep12_np_corridor2b
            hide screen dance_filter_screen
            with dissolve
        else:
            scene ep12_np_corridor2
            hide screen dance_filter_screen
            with dissolve
    else:
        if current_task == "Greet Riona" or current_task == "Greet Riona (3F corridor)":
            scene ep12_np_corridorb
            hide screen dance_filter_screen
            with dissolve
        else:
            scene ep12_np_corridor
            hide screen dance_filter_screen
            with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_corridor_label_nofx

label ep12_np_balcony_label:
$ currentFreeRoamLabel = "ep12_np_balcony_label"
if "ep12_np2_an_label" in event_list:
    $ currentEvent = "ep12_np2_an_label"
    jump startEvent
if "part2" in event_list:
    if "ep12_np_fem_event_label" in event_list:
        if renpy.random.randint(0, 20) > 19:
            $ currentEvent = "ep12_np_fem_event_label"
            jump startEvent
    if "ep12_np2_mjmc_label" in event_list and current_task == "Go to the balcony":
        if maya_shiny_dress:
            scene ep12_np_balconyb2
            hide screen dance_filter_screen
            with dissolve
        else:
            scene ep12_np_balconyb2b
            hide screen dance_filter_screen
            with dissolve
    elif current_task == "Go to the balcony":
        scene ep12_np_balcony2c
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_balconyb
        hide screen dance_filter_screen
        with dissolve
else:
    scene ep12_np_balcony
    hide screen dance_filter_screen
    with dissolve
$ renpy.block_rollback()

if current_task == "Go to the balcony":
    if "ep12_np2_mjmc_label" in event_list:
        if maya_shiny_dress:
            $ ui.imagebutton("ep12_np_balcony_jm_idle", "ep12_np_balcony_jm_hover", clicked=ui.returns("jm"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep12_np_balcony_jmb_idle", "ep12_np_balcony_jmb_hover", clicked=ui.returns("jm"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_balcony_mc_idle", "ep12_np_balcony_mc_hover", clicked=ui.returns("mc"), xpos=0, ypos=0, focus_mask=True)

if "ep12_np2_elena_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_elena2_idle", "ep12_np_balcony_elena2_hover", clicked=ui.returns("elena"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_mia_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_mia_idle", "ep12_np_balcony_mia_hover", clicked=ui.returns("mia"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_he_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_elena_idle", "ep12_np_balcony_elena_hover", clicked=ui.returns("elena2"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_cal_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_avery_idle", "ep12_np_balcony_avery_hover", clicked=ui.returns("avery"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_nik_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_nikita_idle", "ep12_np_balcony_nikita_hover", clicked=ui.returns("nikita"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_kp_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_kp_idle", "ep12_np_balcony_kp_hover", clicked=ui.returns("kp"), xpos=0, ypos=0, focus_mask=True)

if "part2" in event_list:
    if current_task == "Go to the balcony" and "ep12_np2_mjmc_label" in event_list:
        if maya_shiny_dress:
            $ ui.imagebutton("ep12_np_balcony_door2a_idle", "ep12_np_balcony_door2a_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep12_np_balcony_door2b_idle", "ep12_np_balcony_door2b_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    elif current_task == "Go to the balcony":
        $ ui.imagebutton("ep12_np_balcony_door2c_idle", "ep12_np_balcony_door2c_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_balcony_doorb_idle", "ep12_np_balcony_doorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_balcony_door_idle", "ep12_np_balcony_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "door":
    jump ep12_np_corridor_label
elif result == "go_left":
    jump ep12_np_balcony2_label
elif result == "mia":
    $ currentEvent = "ep12_np_mia_label"
    jump startEvent
elif result == "elena":
    $ currentEvent = "ep12_np2_elena_label"
    jump startEvent
elif result == "kp":
    $ currentEvent = "ep12_np2_kp_label"
    jump startEvent
elif result == "mc":
    $ currentEvent = "ep12_np_end_label"
    jump startEvent
    label ep12_np_end_label:
    if current_task == "Go to the balcony":
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep12_np2_fw_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(I still have things to do.)"
    jump endEvent
elif result == "jm":
    $ currentEvent = "ep12_np_endb_label"
    jump startEvent
    label ep12_np_endb_label:
    if current_task == "Go to the balcony":
        menu:
            "End free roam":
                stop music fadeout 3
                $ phone_clear_jump_label = "ep12_np2_mjmc_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(I still have things to do.)"
    jump endEvent
elif result == "elena2":
    $ currentEvent = "ep12_np_he_label"
    jump startEvent
elif result == "nikita":
    $ currentEvent = "ep12_np2_nik_label"
    jump startEvent
elif result == "avery":
    $ currentEvent = "ep12_np_cal_label"
    jump startEvent

label ep12_np_balcony2_label:
if "ep12_np2_rq_label" in event_list:
    $ currentFreeRoamLabel = "ep12_np_balcony2_label"
    $ currentEvent = "ep12_np2_rq_label"
    jump startEvent

if persistent.ep12_cardisa7:
    if "part2" in event_list:
        if "ep12_np2_rdm_label" in event_list:
            scene ep12_np_balcony2b2
        else:
            scene ep12_np_balcony2b
            if "ACTIVE" in ep12_jewels and "green" not in ep12_jewels and "GREEN" not in ep12_jewels:
                show ep12_green_jewel_idle
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_balcony2
        hide screen dance_filter_screen
        with dissolve
else:
    if "part2" in event_list:
        if "ep12_np2_rdm_label" in event_list:
            scene ep12_np_balcony2b2_card
        else:
            scene ep12_np_balcony2b_card
            if "ACTIVE" in ep12_jewels and "green" not in ep12_jewels and "GREEN" not in ep12_jewels:
                show ep12_green_jewel_idle
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_balcony2_card
        hide screen dance_filter_screen
        with dissolve
label ep12_np_balcony2_label_nofx:
$ currentFreeRoamLabel = "ep12_np_balcony2_label"

$ renpy.block_rollback()

if "ep12_np2_rio_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_rio_idle", "ep12_np_balcony_rio_hover", clicked=ui.returns("riona"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_rdm_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony_rusty_idle", "ep12_np_balcony_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_om_label" in event_list:
    $ ui.imagebutton("ep12_np_balcony2_matthew_idle", "ep12_np_balcony2_matthew_hover", clicked=ui.returns("matthew"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep12_cardisa7:
    $ ui.imagebutton("ep12_np_balcony2_card_idle", "ep12_np_balcony2_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ACTIVE" in ep12_jewels and "green" not in ep12_jewels and "GREEN" not in ep12_jewels:
    $ ui.imagebutton("ep12_green_jewel_idle", "ep12_green_jewel_idle", clicked=ui.returns("green"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_balcony_label
elif result == "matthew":
    $ currentEvent = "ep12_np_om_label"
    jump startEvent
elif result == "riona":
    $ currentEvent = "ep12_np2_rio_label"
    jump startEvent
elif result == "rusty":
    $ currentEvent = "ep12_np2_rdm_label"
    jump startEvent
elif result == "green":
    $ ep12_jewels.append("green")
    jump ep12_np_balcony2_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa7 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        if "ep12_np2_rdm_label" in event_list:
            scene ep12_np_balcony2b2 with dissolve
        else:
            scene ep12_np_balcony2b with dissolve
    else:
        scene ep12_np_balcony2 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_balcony2_label_nofx

label ep12_np_2f_corridor_label:
$ currentFreeRoamLabel = "ep12_np_2f_corridor_label"

if "part2" in event_list:
    if "ep12_np2_tc_label" in event_list:
        scene ep12_np_2fb_corridor
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_2f_corridor
        hide screen dance_filter_screen
        with dissolve
else:
    scene ep12_np_2f_corridor
    hide screen dance_filter_screen
    with dissolve
$ renpy.block_rollback()

if "ep12_np2_tc_label" in event_list:
    $ ui.imagebutton("ep12_np_corridor_chad_idle", "ep12_np_corridor_chad_hover", clicked=ui.returns("chad"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_tc_label" not in event_list:
    $ ui.imagebutton("ep12_np_2corridor_door_idle", "ep12_np_2corridor_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=630 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up2"), xpos=1000 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "door":
    if "ep12_np_storage_locked_label" in event_list:
        $ currentEvent = "ep12_np_storage_locked_label"
        jump startEvent
    elif not "key" in event_list:
        play sound "sound_effects/door_lock.mp3"
        mc "(It's locked...)"
        jump ep12_np_2f_corridor_label
    else:
        jump ep12_np_storage_label
elif result == "chad":
    $ currentEvent = "ep12_np2_tc_label"
    jump startEvent
elif result == "go_up":
    jump ep12_np_outside_label
elif result == "go_up2":
    if not "key" in event_list:
        play sound "sound_effects/door_lock.mp3"
        mc "(It's locked...)"
        jump ep12_np_2f_corridor_label
    else:
        jump ep12_np_locker_room_label
elif result == "go_down":
    jump ep12_np_corridor_label

label ep12_np_storage_label:
$ currentFreeRoamLabel = "ep12_np_storage_label"

scene ep12_np_storage
hide screen dance_filter_screen
with dissolve
$ renpy.block_rollback()

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[8][1]:
    $ ui.imagebutton("ep12_packquest_btn8_idle", "ep12_packquest_btn8_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_2f_corridor_label
elif result == "go_right":
    jump ep12_np_storage_right_label
elif result == "go_left":
    jump ep12_np_storage_left_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[8][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep12_np_storage_right_label:
if persistent.ep12_cardisa8:
    scene ep12_np_storage_right
    hide screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_storage_right_card
    hide screen dance_filter_screen
    with dissolve
label ep12_np_storage_right_label_nofx:
$ currentFreeRoamLabel = "ep12_np_storage_right_label"

$ renpy.block_rollback()

if pack_quest_active and not pack_quest_list[6][1]:
    $ ui.imagebutton("ep12_packquest_btn6_idle", "ep12_packquest_btn6_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep12_cardisa8:
    $ ui.imagebutton("ep12_np_storage_right_card_idle", "ep12_np_storage_right_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_storage_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[6][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa8 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep12_np_storage_right with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_storage_right_label_nofx

label ep12_np_storage_left_label:
if persistent.ep12_cardisa12:
    scene ep12_np_storage_left
    hide screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_storage_left_card
    hide screen dance_filter_screen
    with dissolve
label ep12_np_storage_left_label_nofx:
$ currentFreeRoamLabel = "ep12_np_storage_left_label"
$ renpy.block_rollback()

if not persistent.ep12_cardisa12:
    $ ui.imagebutton("ep12_np_storage_left_card_idle", "ep12_np_storage_left_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_beer_label" in event_list:
    $ ui.imagebutton("ep12_np_storage_beer_idle", "ep12_np_storage_beer_hover", clicked=ui.returns("beer"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_storage_label
elif result == "beer":
    $ currentEvent = "ep12_np_beer_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa12 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep12_np_storage_left with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_storage_left_label_nofx

label ep12_np_locker_room_label:
if found_money:
    if persistent.ep12_cardisa17:
        scene ep12_np_locker_room with dissolve
    else:
        scene ep12_np_locker_room_card with dissolve
else:
    if persistent.ep12_cardisa17:
        scene ep12_np_locker_room_money with dissolve
    else:
        scene ep12_np_locker_room_money_card with dissolve
label ep12_np_locker_room_label_nofx:
$ currentFreeRoamLabel = "ep12_np_locker_room_label"
$ renpy.block_rollback()

if not persistent.ep12_cardisa17:
    $ ui.imagebutton("ep12_np_locker_room_card_idle", "ep12_np_locker_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if not found_money:
    $ ui.imagebutton("ep12_np_locker_room_money_idle", "ep12_np_locker_room_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=400 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_2f_corridor_label
elif result == "go_right":
    jump ep12_np_locker_room_right_label
elif result == "go_up":
    jump ep12_np_locker_room_left_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa17 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if found_money:
        scene ep12_np_locker_room with dissolve
    else:
        scene ep12_np_locker_room_money with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_locker_room_label_nofx
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    if persistent.ep12_cardisa17:
        scene ep12_np_locker_room with dissolve
    else:
        scene ep12_np_locker_room_card with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep12_np_locker_room_label_nofx
label ep12_np_locker_room_right_label:
if persistent.ep12_cardisa19:
    scene ep12_np_locker_room_right
    hide screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_locker_room_right_card
    hide screen dance_filter_screen
    with dissolve
label ep12_np_locker_room_right_label_nofx:
$ currentFreeRoamLabel = "ep12_np_locker_room_right_label"
$ renpy.block_rollback()

if "ACTIVE" in ep12_jewels:
    $ ui.imagebutton("ep12_np_locker_room_right_l_idle", "ep12_np_locker_room_right_l_hover", clicked=ui.returns("locker"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[5][1]:
    $ ui.imagebutton("ep12_packquest_btn5_idle", "ep12_packquest_btn5_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep12_cardisa19:
    $ ui.imagebutton("ep12_np_locker_room_right_card_idle", "ep12_np_locker_room_right_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_locker_room_label
elif result == "locker":
    jump ep12_np_locker_room_right_l_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[5][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa19 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep12_np_locker_room_right with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_locker_room_right_label_nofx

label ep12_np_locker_room_right_l_label:
$ currentFreeRoamLabel = "ep12_np_locker_room_right_l_label"
$ renpy.block_rollback()
scene ep12_np_locker_room_right_l
if "ACTIVE" in ep12_jewels and "yellow" not in ep12_jewels and "YELLOW" not in ep12_jewels:
    show ep12_yellow_jewel_idle
hide screen dance_filter_screen
with dissolve

if "ACTIVE" in ep12_jewels and "yellow" not in ep12_jewels and "YELLOW" not in ep12_jewels:
    $ ui.imagebutton("ep12_yellow_jewel_idle", "ep12_yellow_jewel_idle", clicked=ui.returns("yellow"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_locker_room_right_label
elif result == "yellow":
    $ ep12_jewels.append("yellow")
    jump ep12_np_locker_room_right_l_label

label ep12_np_locker_room_left_label:
if persistent.ep12_cardisa18:
    scene ep12_np_locker_room_left
    hide screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_locker_room_left_card
    hide screen dance_filter_screen
    with dissolve
label ep12_np_locker_room_left_label_nofx:
$ currentFreeRoamLabel = "ep12_np_locker_room_left_label"
$ renpy.block_rollback()

if not persistent.ep12_cardisa18:
    $ ui.imagebutton("ep12_np_locker_room_left_card_idle", "ep12_np_locker_room_left_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep12_np_locker_room_left_locker_idle", "ep12_np_locker_room_left_locker_hover", clicked=ui.returns("locker"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_locker_room_label
elif result == "locker":
    play sound "sound_effects/door_lock.mp3"
    mc "(Hm... That locker is locked solid. What if I pull even harder?)"
    play sound "sound_effects/door_knob.mp3"
    scene ep12_np_locker_room_left1 with hpunch
    mc "(Nothing in here. Just a cardboard box, for some reason.)"
    jump ep12_np_locker_room_left_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa18 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep12_np_locker_room_left with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_locker_room_left_label_nofx

label ep12_np_outside_label:
$ currentFreeRoamLabel = "ep12_np_outside_label"

if "part2" in event_list:
    if ep11_jade_lewd and not "ep12_np2_an_label" in event_list:
        scene ep12_np_outsideb2
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_outsideb
        hide screen dance_filter_screen
        with dissolve
else:
    scene ep12_np_outside
    hide screen dance_filter_screen
    with dissolve

$ renpy.block_rollback()

if "ep12_np2_jade_label" in event_list:
    $ ui.imagebutton("ep12_np_outside_jade_idle", "ep12_np_outside_jade_hover", clicked=ui.returns("jade"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_jj_label" in event_list:
    $ ui.imagebutton("ep12_np_outside_jacob_idle", "ep12_np_outside_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
if "part2" in event_list:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1550 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
else:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1380 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

if current_task == "Go to the balcony":
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up2"), xpos=750 * persistent.scale_factor, ypos=150 * persistent.scale_factor)

if pack_quest_active and not pack_quest_list[7][1]:
    if "part2" in event_list:
        $ ui.imagebutton("ep12_packquest_btn7_idle", "ep12_packquest_btn7_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep12_np_2f_corridor_label
elif result == "go_up2":
    jump ep12_np_outsideb_label
elif result == "jacob":
    $ currentEvent = "ep12_np_jj_label"
    jump startEvent
elif result == "jade":
    $ currentEvent = "ep12_np2_jade_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[7][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep12_np_party_room_label:
$ currentFreeRoamLabel = "ep12_np_party_room_label"
if "ep12_np2_jmd_label" in event_list:
    $ currentEvent = "ep12_np2_jmd_label"
    jump startEvent
if "part2" in event_list:
    if ep12_zoey_friend or "ep12_np2_zu_label" in event_list or branchZoey:
        if "Jill" in breakup and "part3" in event_list:
            scene ep12_np_party_roombnj
        else:
            scene ep12_np_party_roomb
    else:
        if "Jill" in breakup and "part3" in event_list:
            scene ep12_np_party_roomb2nj
        else:
            scene ep12_np_party_roomb2
    show screen dance_filter_screen
    with dissolve
else:
    if "sage_gone" in event_list:
        scene ep12_np_party_room_ns
        show screen dance_filter_screen
        with dissolve
    else:
        scene ep12_np_party_room
        show screen dance_filter_screen
        with dissolve
$ renpy.block_rollback()

$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if "part2" in event_list:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1200 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
else:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1000 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
if "ep12_np_cam_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_camila_idle", "ep12_np_party_room_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_tm_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_tommy_idle", "ep12_np_party_room_tommy_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_jill_label" in event_list or "ep12_np_bujill_label" in event_list:
    if "sage_gone" in event_list:
        $ ui.imagebutton("ep12_np_party_room_jillb_idle", "ep12_np_party_room_jillb_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep12_np_party_room_jill_idle", "ep12_np_party_room_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_zu_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_zoey_idle", "ep12_np_party_room_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_bct_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_tiffani_idle", "ep12_np_party_room_tiffani_hover", clicked=ui.returns("tiffani"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_skey_label" in event_list or "ep12_np_smc_label" in event_list or "ep12_np_s2mc_label" in event_list or "ep12_np_s3mc_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_sage_idle", "ep12_np_party_room_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if current_task == "Talk to Nick" or current_task == "Talk to Nick (Dance floor)":
    $ ui.imagebutton("ep12_np_party_room_nick_idle", "ep12_np_party_room_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "sage":
    if "ep12_np_skey_label" in event_list:
        $ currentEvent = "ep12_np_skey_label"
    elif "ep12_np_smc_label" in event_list:
        $ currentEvent = "ep12_np_smc_label"
    elif "ep12_np_s2mc_label" in event_list:
        $ currentEvent = "ep12_np_s2mc_label"
    elif "ep12_np_s3mc_label" in event_list:
        $ currentEvent = "ep12_np_s3mc_label"
    jump startEvent
elif result == "tommy":
    $ currentEvent = "ep12_np_tm_label"
    jump startEvent
elif result == "nick":
    menu:
        "Pass time":
            $ currentEvent = "ep12_np2_nick_label"
            jump startEvent
        "Not yet":
            jump ep12_np_party_room_label
elif result == "camila":
    $ currentEvent = "ep12_np_cam_label"
    jump startEvent
elif result == "zoey":
    $ currentEvent = "ep12_np2_zu_label"
    jump startEvent
elif result == "jill":
    if "ep12_np_bujill_label" in event_list:
        $ currentEvent = "ep12_np_bujill_label"
    else:
        $ currentEvent = "ep12_np_jill_label"
    jump startEvent
elif result == "tiffani":
    $ currentEvent = "ep12_np_bct_label"
    jump startEvent
elif result == "go_up":
    jump ep12_np_party_room_up_label
elif result == "go_right":
    jump ep12_np_party_room_right_label
elif result == "go_down":
    jump ep12_np_corridor_label

label ep12_np_party_room_right_label:
$ currentFreeRoamLabel = "ep12_np_party_room_right_label"

if "part2" in event_list:
    scene ep12_np_party_room_rightb
    show screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_party_room_right
    show screen dance_filter_screen
    with dissolve
$ renpy.block_rollback()

if "ep12_np2_lily_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_lily_idle", "ep12_np_party_room_right_lily_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_jsl_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_jimmy_idle", "ep12_np_party_room_right_jimmy_hover", clicked=ui.returns("jimmy"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_ht_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_heather_idle", "ep12_np_party_room_right_heather_hover", clicked=ui.returns("heather"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_had_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_arieth_idle", "ep12_np_party_room_right_arieth_hover", clicked=ui.returns("arieth"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_mcc_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_chad_idle", "ep12_np_party_room_right_chad_hover", clicked=ui.returns("chad"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_dwa_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_anthony_idle", "ep12_np_party_room_right_anthony_hover", clicked=ui.returns("anthony"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_nikita_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_nikita_idle", "ep12_np_party_room_right_nikita_hover", clicked=ui.returns("nikita"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_tara_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_right_tara_idle", "ep12_np_party_room_right_tara_hover", clicked=ui.returns("tara"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "chad":
    $ currentEvent = "ep12_np_mcc_label"
    jump startEvent
elif result == "anthony":
    $ currentEvent = "ep12_np_dwa_label"
    jump startEvent
elif result == "lily":
    $ currentEvent = "ep12_np2_lily_label"
    jump startEvent
elif result == "jimmy":
    $ currentEvent = "ep12_np2_jsl_label"
    jump startEvent
elif result == "heather":
    $ currentEvent = "ep12_np2_ht_label"
    jump startEvent
elif result == "arieth":
    $ currentEvent = "ep12_np2_had_label"
    jump startEvent
elif result == "nikita":
    $ currentEvent = "ep12_np_nikita_label"
    jump startEvent
elif result == "tara":
    $ currentEvent = "ep12_np_tara_label"
    jump startEvent
elif result == "go_down":
    jump ep12_np_party_room_label

label ep12_np_party_room_up_label:
$ currentFreeRoamLabel = "ep12_np_party_room_up_label"

if "ep12_np2_jomc_label" in event_list:
    $ currentEvent = "ep12_np2_jomc_label"
    jump startEvent
if "ep12_np_bmc_label" in event_list:
    $ currentEvent = "ep12_np_bmc_label"
    jump startEvent

if "part2" in event_list:
    if "Jill" in breakup and "part3" in event_list:
        scene ep12_np_party_room_upbnj
    else:
        scene ep12_np_party_room_upb
    show screen dance_filter_screen
    with dissolve
else:
    scene ep12_np_party_room_up
    show screen dance_filter_screen
    with dissolve
$ renpy.block_rollback()

if "part2" in event_list:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1420 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
else:
    $ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1650 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
if "part2" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_doorb_idle", "ep12_np_party_room_up_doorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep12_np_party_room_up_door_idle", "ep12_np_party_room_up_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_sally_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_sally_idle", "ep12_np_party_room_up_sally_hover", clicked=ui.returns("sally"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_ji_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_jill_idle", "ep12_np_party_room_up_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_qmc_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_quinn_idle", "ep12_np_party_room_up_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np2_ad_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_derek_idle", "ep12_np_party_room_up_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_bianca_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_up_bianca_idle", "ep12_np_party_room_up_bianca_hover", clicked=ui.returns("bianca"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "quinn":
    $ currentEvent = "ep12_np_qmc_label"
    jump startEvent
elif result == "bianca":
    $ currentEvent = "ep12_np_bianca_label"
    jump startEvent
elif result == "sally":
    $ currentEvent = "ep12_np2_sally_label"
    jump startEvent
elif result == "jill":
    $ currentEvent = "ep12_np2_ji_label"
    jump startEvent
elif result == "derek":
    $ currentEvent = "ep12_np2_ad_label"
    jump startEvent
elif result == "go_up":
    jump ep12_np_party_room_dj_label
elif result == "door":
    jump ep12_np_party_balcony_label
elif result == "go_down":
    jump ep12_np_party_room_label

label ep12_np_party_room_dj_label:
if persistent.ep12_cardisa6:
    if "part2" in event_list:
        if "ep12_np2_q_lewd_label" in event_list:
            scene ep12_np_party_room_djb2
            show screen dance_filter_screen
            with dissolve
        else:
            if "Jill" in breakup and "part3" in event_list:
                scene ep12_np_party_room_djbnj
            else:
                scene ep12_np_party_room_djb
            show screen dance_filter_screen
            with dissolve
    else:
        scene ep12_np_party_room_dj
        show screen dance_filter_screen
        with dissolve
else:

    if "part2" in event_list:
        if "ep12_np2_q_lewd_label" in event_list:
            scene ep12_np_party_room_djb2_card
            show screen dance_filter_screen
            with dissolve
        else:
            if "Jill" in breakup and "part3" in event_list:
                scene ep12_np_party_room_djbnj_card
            else:
                scene ep12_np_party_room_djb_card
            show screen dance_filter_screen
            with dissolve
    else:
        scene ep12_np_party_room_dj_card
        show screen dance_filter_screen
        with dissolve

label ep12_np_party_room_dj_label_nofx:
$ currentFreeRoamLabel = "ep12_np_party_room_dj_label"
$ renpy.block_rollback()

if "ep12_np2_q_lewd_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_quinn_idle", "ep12_np_party_room_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
if "ep12_np_dj_label" in event_list:
    $ ui.imagebutton("ep12_np_party_room_dj_idle", "ep12_np_party_room_dj_hover", clicked=ui.returns("dj"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1600 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
if not persistent.ep12_cardisa6:
    $ ui.imagebutton("ep12_np_party_room_dj_card_idle", "ep12_np_party_room_dj_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[4][1]:
    if "part2" in event_list:
        $ ui.imagebutton("ep12_packquest_btn4_idle", "ep12_packquest_btn4_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "dj":
    $ currentEvent = "ep12_np_dj_label"
    jump startEvent
elif result == "quinn":
    $ currentEvent = "ep12_np2_q_lewd_label"
    jump startEvent
elif result == "go_up":
    jump ep12_np_party_room_up_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[4][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa6 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

    if "part2" in event_list:
        if "ep12_np2_q_lewd_label" in event_list:
            scene ep12_np_party_room_djb2 with dissolve
        else:
            if "Jill" in breakup and "part3" in event_list:
                scene ep12_np_party_room_djbnj with dissolve
            else:
                scene ep12_np_party_room_djb with dissolve
    else:
        scene ep12_np_party_room_dj with dissolve

    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_party_room_dj_label_nofx

label ep12_np_party_balcony_label:
if persistent.ep12_cardisa5:
    scene ep12_np_party_balcony
else:
    scene ep12_np_party_balcony_card
hide screen dance_filter_screen
if "ACTIVE" in ep12_jewels and "red" not in ep12_jewels and "RED" not in ep12_jewels:
    show ep12_red_jewel_idle
with dissolve
label ep12_np_party_balcony_label_nofx:
$ currentFreeRoamLabel = "ep12_np_party_balcony_label"
$ renpy.block_rollback()

if not persistent.ep12_cardisa5:
    $ ui.imagebutton("ep12_np_party_balcony_card_idle", "ep12_np_party_balcony_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[9][1]:
    $ ui.imagebutton("ep12_packquest_btn9_idle", "ep12_packquest_btn9_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

if "ACTIVE" in ep12_jewels and "red" not in ep12_jewels and "RED" not in ep12_jewels:
    $ ui.imagebutton("ep12_red_jewel_idle", "ep12_red_jewel_idle", clicked=ui.returns("red"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_party_room_up_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[9][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "red":
    $ ep12_jewels.append("red")
    jump ep12_np_party_balcony_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep12_cardisa5 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep12_np_party_balcony with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep12_np_party_balcony_label_nofx

label ep12_np_outsideb_label:
$ currentFreeRoamLabel = "ep12_np_outsideb_label"
$ renpy.block_rollback()
if "DONE" not in ep12_jewels:
    scene ep12_np_outsidebc
    if "RED" in ep12_jewels:
        show ep12_red_jewel
    if "GREEN" in ep12_jewels:
        show ep12_green_jewel
    if "BLUE" in ep12_jewels:
        show ep12_blue_jewel
    if "YELLOW" in ep12_jewels:
        show ep12_yellow_jewel
    with dissolve
else:
    scene ep12_np_outsidec with dissolve


if "DONE" not in ep12_jewels:
    $ ui.imagebutton("ep12_np_outsideb_door_idle", "ep12_np_outsideb_door_idle", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep12_np_outsideb_pillar_idle", "ep12_np_outsideb_pillar_idle", clicked=ui.returns("pillar"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_down":
    jump ep12_np_outside_label
elif result == "pillar":
    jump ep12_np_outsided_label
elif result == "door":
    if "START" in ep12_jewels:
        mc "(What a strange looking door... Something feels off about it.)"
        $ ep12_jewels = ["ACTIVE"]
    elif "RED" in ep12_jewels and "GREEN" in ep12_jewels and "BLUE" in ep12_jewels and "YELLOW" in ep12_jewels:
        stop music fadeout 3
        mc "(It's open...)"
        hide screen freeroam_help
        hide screen freeroam_wt_help
        $ currentEvent = "ep12_c_enter_event_label"
        jump startEvent
    elif "ACTIVE" in ep12_jewels and len(ep12_jewels) == 1:
        mc "(Nope. It doesn't open.)"
    else:
        mc "(Maybe the gems have something do to with the door.)"
    jump ep12_np_outsideb_label

label ep12_np_outsided_label:
$ currentFreeRoamLabel = "ep12_np_outsided_label"
$ renpy.block_rollback()

scene ep12_np_outsided
if "RED" in ep12_jewels:
    show ep12_red_jewel2
if "GREEN" in ep12_jewels:
    show ep12_green_jewel2
if "BLUE" in ep12_jewels:
    show ep12_blue_jewel2
if "YELLOW" in ep12_jewels:
    show ep12_yellow_jewel2
with dissolve

if "RED" not in ep12_jewels:
    $ ui.imagebutton("ep12_np_slot1_idle", "ep12_np_slot1_idle", clicked=ui.returns("slot1"), xpos=0, ypos=0, focus_mask=True)
if "GREEN" not in ep12_jewels:
    $ ui.imagebutton("ep12_np_slot2_idle", "ep12_np_slot2_idle", clicked=ui.returns("slot2"), xpos=0, ypos=0, focus_mask=True)
if "BLUE" not in ep12_jewels:
    $ ui.imagebutton("ep12_np_slot3_idle", "ep12_np_slot3_idle", clicked=ui.returns("slot3"), xpos=0, ypos=0, focus_mask=True)
if "YELLOW" not in ep12_jewels:
    $ ui.imagebutton("ep12_np_slot4_idle", "ep12_np_slot4_idle", clicked=ui.returns("slot4"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep12_np_outsideb_label
elif result == "slot1":
    if "red" in ep12_jewels:
        play sound "sound_effects/season3/jewel.mp3"
        $ ep12_jewels.append("RED")
        $ ep12_jewels.remove("red")
    else:
        mc "(What goes in here?)"
    jump ep12_np_outsided_label
elif result == "slot2":
    if "green" in ep12_jewels:
        play sound "sound_effects/season3/jewel.mp3"
        $ ep12_jewels.append("GREEN")
        $ ep12_jewels.remove("green")
    else:
        mc "(What goes in here?)"
    jump ep12_np_outsided_label
elif result == "slot3":
    if "blue" in ep12_jewels:
        play sound "sound_effects/season3/jewel.mp3"
        $ ep12_jewels.append("BLUE")
        $ ep12_jewels.remove("blue")
    else:
        mc "(What goes in here?)"
    jump ep12_np_outsided_label
elif result == "slot4":
    if "yellow" in ep12_jewels:
        play sound "sound_effects/season3/jewel.mp3"
        $ ep12_jewels.append("YELLOW")
        $ ep12_jewels.remove("yellow")
    else:
        mc "(What goes in here?)"
    jump ep12_np_outsided_label

label ep12_np_crypt_label:
$ currentFreeRoamLabel = "ep12_np_crypt_label"
$ renpy.block_rollback()
hide screen new_phone_screen
hide screen map_screen
scene ep12_np_crypt with dissolve

$ ui.imagebutton("ep12_np_mural_idle", "ep12_np_mural_idle", clicked=ui.returns("mural"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep12_np_mural_s_idle", "ep12_np_mural_s_idle", clicked=ui.returns("se"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep12_np_mural_cr_idle", "ep12_np_mural_cr_idle", clicked=ui.returns("cr"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep12_np_mural_et_idle", "ep12_np_mural_et_idle", clicked=ui.returns("et"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"),xpos=600 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    $ currentEvent = "ep12_c_event_label"
    jump startEvent
elif result == "se":
    $ currentEvent = "ep12_se_event_label"
    jump startEvent
elif result == "cr":
    $ currentEvent = "ep12_cr_event_label"
    jump startEvent
elif result == "et":
    $ currentEvent = "ep12_et_event_label"
    jump startEvent
elif result == "mural":
    $ currentEvent = "ep12_m_event_label"
    jump startEvent

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

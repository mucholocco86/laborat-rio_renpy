label ep10_freeroam_tg_label:
$ freeRoamID = "ep10_5"
$ roosterState = "ep10_5"
$ tmpInt = 0
show screen wt_tasks_shown
show screen freeroam_help
$ found_money = False
$ found_money2 = False
$ studied = False

$ disabled_apps = []
$ disabled_apps.append("brawler")
$ disabled_apps.append("music")
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True
call mphone_check_pack_quest_available from _call_mphone_check_pack_quest_available_1
$ rooster_jump_label = "ep10_fr_tg_main_hall_label"
jump initRoosterLabel

label ep10_fr_tg_main_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_main_hall_label"

if "tg_part2" in event_list:
    scene ep10_fr_tg_main_hall2 with dissolve
else:
    scene ep10_fr_tg_main_hall with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = [""]
    $ optional_task_list = [""]

    $ chat_new_tasks = True
    $ event_list = []

    $ event_list.append("ep10_tg_d_label")
    $ event_list.append("ep10_tg_mp_label")
    $ event_list.append("ep10_tg_helen_label")
    $ event_list.append("ep10_tg_pills_event_label")

    $ updateTaskList()

    show screen freeroam_intro_screen("Snoop around for the binder")
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
    hide screen freeroam_intro_screen


if "ep10_tg_hall_derek_label" in event_list:
    $ ui.imagebutton("ep10_fr_tg_main_hall_derek_idle", "ep10_fr_tg_main_hall_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_main_hall_cabinet_idle", "ep10_fr_tg_main_hall_cabinet_hover", clicked=ui.returns("cabinet"), xpos=0, ypos=0, focus_mask=True)
if not "tg_part2" in event_list:
    $ ui.imagebutton("ep10_fr_tg_main_hall_walker_idle", "ep10_fr_tg_main_hall_walker_hover", clicked=ui.returns("walker"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_main_hall_stairs_idle", "ep10_fr_tg_main_hall_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_main_hall_table_idle", "ep10_fr_tg_main_hall_table_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up2"), xpos=1100 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

if pack_quest_active and not pack_quest_list[1][1]:
    $ ui.imagebutton("ep10_packquest_btn1_idle", "ep10_packquest_btn1_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_up":
    jump ep10_fr_tg_left_hall_label
elif result == "go_up2":
    jump ep10_fr_tg_up_hall_label
elif result == "go_right":
    jump ep10_fr_tg_kitchen_label
elif result == "go_down":
    jump ep10_fr_tg_main_halld_label
elif result == "derek":
    $ currentEvent = "ep10_tg_hall_derek_label"
    jump startEvent
elif result == "stairs":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "walker":
    jump ep10_fr_tg_main_walker_label
elif result == "cabinet":
    jump ep10_fr_tg_main_cabinet_label
elif result == "table":
    jump ep10_fr_tg_main_table_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[1][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)



label ep10_fr_tg_main_halld_label:
if not persistent.ep10_cardsa10:
    scene ep10_fr_tg_main_halld_card with dissolve
else:
    scene ep10_fr_tg_main_halld with dissolve
label ep10_fr_tg_main_halld_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_main_halld_label"

if not persistent.ep10_cardsa10:
    $ ui.imagebutton("ep10_fr_tg_main_halld_card_idle", "ep10_fr_tg_main_halld_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa10 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_fr_tg_main_halld with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_main_halld_label_nofx

label ep10_fr_tg_main_walker_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_main_walker_label"
scene ep10_fr_tg_main_walker with dissolve

$ ui.imagebutton("ep10_fr_tg_main_walker_pills_idle", "ep10_fr_tg_main_walker_pills_hover", clicked=ui.returns("pills"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_main_walker_journal_idle", "ep10_fr_tg_main_walker_journal_hover", clicked=ui.returns("journal"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "pills":
    mc "(That's a lot of meds. Almost like a meal's worth of them.)"
    jump ep10_fr_tg_main_walker_label
elif result == "journal":
    if "ep10_tg_pills_event_label" in event_list:
        $ currentEvent = "ep10_tg_pills_event_label"
        jump startEvent
    else:
        if ep10_read_notepad:
            mc "(I regret reading that.)"
        else:
            mc "(I'm not reading that.)"
    jump ep10_fr_tg_main_walker_label

label ep10_fr_tg_main_table_label:
if not persistent.ep10_cardsa11:
    scene ep10_fr_tg_main_table_card with dissolve
else:
    scene ep10_fr_tg_main_table with dissolve
label ep10_fr_tg_main_table_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_main_table_label"

if not persistent.ep10_cardsa11:
    $ ui.imagebutton("ep10_fr_tg_main_table_card_idle", "ep10_fr_tg_main_table_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[6][1]:
    $ ui.imagebutton("ep10_packquest_btn6_idle", "ep10_packquest_btn6_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()


if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa11 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_fr_tg_main_table with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_main_table_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[6][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_main_cabinet_label:
if not persistent.ep10_cardsa12:
    if not found_money:
        scene ep10_fr_tg_main_cabinet_card_cash with dissolve
    else:
        scene ep10_fr_tg_main_cabinet_card with dissolve
else:
    if not found_money:
        scene ep10_fr_tg_main_cabinet_cash with dissolve
    else:
        scene ep10_fr_tg_main_cabinet with dissolve

label ep10_fr_tg_main_cabinet_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_main_cabinet_label"

if not persistent.ep10_cardsa12:
    $ ui.imagebutton("ep10_fr_tg_main_cabinet_card_idle", "ep10_fr_tg_main_cabinet_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if not found_money:
    $ ui.imagebutton("ep10_fr_tg_main_cabinet_cash_idle", "ep10_fr_tg_main_cabinet_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[8][1]:
    $ ui.imagebutton("ep10_packquest_btn8_idle", "ep10_packquest_btn8_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa12 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if not found_money:
        scene ep10_fr_tg_main_cabinet_cash with dissolve
    else:
        scene ep10_fr_tg_main_cabinet with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_main_cabinet_label_nofx
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    if not persistent.ep10_cardsa12:
        scene ep10_fr_tg_main_cabinet_card with dissolve
    else:
        scene ep10_fr_tg_main_cabinet with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_fr_tg_main_cabinet_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[8][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_left_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_left_hall_label"
scene ep10_fr_tg_left_hall with dissolve

$ ui.imagebutton("ep10_fr_tg_left_hall_ldoor_idle", "ep10_fr_tg_left_hall_ldoor_hover", clicked=ui.returns("ldoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_left_hall_rdoor_idle", "ep10_fr_tg_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_left_hall_cdoor_idle", "ep10_fr_tg_left_hall_cdoor_hover", clicked=ui.returns("cdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "ldoor":
    jump ep10_fr_tg_livingroom_label
elif result == "rdoor":
    jump ep10_fr_tg_dining_label
elif result == "cdoor":
    jump ep10_fr_tg_garage_label


label ep10_fr_tg_garage_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_garage_label"
scene ep10_fr_tg_garage with dissolve

if pack_quest_active and not pack_quest_list[0][1]:
    $ ui.imagebutton("ep10_packquest_btn0_idle", "ep10_packquest_btn0_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_garage_door_idle", "ep10_fr_tg_garage_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_garage_keys_idle", "ep10_fr_tg_garage_keys_hover", clicked=ui.returns("keys"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "door":
    jump ep10_fr_tg_left_hall_label
elif result == "keys":
    if "ep10_tg_keys_label" in event_list:
        $ currentEvent = "ep10_tg_keys_label"
        jump startEvent
    elif "tg_part2" in event_list:
        jump ep10_fr_tg_garage_keys_label
    else:
        mc "(It's locked.)"
        jump ep10_fr_tg_garage_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[0][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_garage_keys_label:
if "no_keys" in event_list:
    scene ep10_tg_keys3 with dissolve
else:
    scene ep10_tg_keys3b with dissolve
label ep10_fr_tg_garage_keys_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_garage_keys_label"

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if "no_keys" in event_list:
    $ ui.imagebutton("ep10_fr_tg_keys_idle", "ep10_fr_tg_keys_hover", clicked=ui.returns("keys"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_left":
    jump ep10_fr_tg_garage_label
elif result == "keys":
    if "no_keys" in event_list:
        $ event_list.remove("no_keys")
    play sound "sound_effects/season3/keys.mp3"
    scene ep10_tg_keys3b with dissolve
    mc "(House keys! Bingo!)"
    mc "(Ok... Time to get to the office unnoticed.)"
    jump ep10_fr_tg_garage_keys_label_nofx

label ep10_fr_tg_dining_label:
$ renpy.block_rollback()
if "ep10_tg_dinner_label" in event_list:
    $ currentEvent = "ep10_tg_dinner_label"
    jump startEvent
$ currentFreeRoamLabel = "ep10_fr_tg_dining_label"

if "tg_part2" in event_list:
    if ep8_told_josy_chad:
        scene ep10_fr_tg_dining2 with dissolve
    else:
        scene ep10_fr_tg_dining2b with dissolve
else:
    scene ep10_fr_tg_dining with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_left_hall_label


label ep10_fr_tg_livingroom_label:
if not persistent.ep10_cardzo12:
    scene ep10_fr_tg_livingroom_card with dissolve
else:
    scene ep10_fr_tg_livingroom with dissolve
label ep10_fr_tg_livingroom_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_livingroom_label"

if not persistent.ep10_cardzo12:
    $ ui.imagebutton("ep10_fr_tg_livingroom_card_idle", "ep10_fr_tg_livingroom_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[9][1]:
    $ ui.imagebutton("ep10_packquest_btn9_idle", "ep10_packquest_btn9_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_left_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardzo12 = True
    $ persistent.rew_zoey_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_fr_tg_livingroom with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_livingroom_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[9][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_up_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_up_hall_label"
scene ep10_fr_tg_up_hall with dissolve

$ ui.imagebutton("ep10_fr_tg_up_hall_ldoor_idle", "ep10_fr_tg_up_hall_ldoor_hover", clicked=ui.returns("ldoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_up_hall_cdoor_idle", "ep10_fr_tg_up_hall_cdoor_hover", clicked=ui.returns("cdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "ldoor":
    jump ep10_fr_tg_bedroom_label
elif result == "cdoor":
    jump ep10_fr_tg_bathroom_label


label ep10_fr_tg_kitchen_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_kitchen_label"

if "tg_part2" in event_list:
    scene ep10_fr_tg_kitchen2 with dissolve
else:
    if "tg_part1b" in event_list:
        scene ep10_fr_tg_kitchenb with dissolve
    else:
        scene ep10_fr_tg_kitchen with dissolve

if "ep10_tg_mp_label" in event_list or "ep10_tg2_mp_label" in event_list:
    $ ui.imagebutton("ep10_fr_tg_kitchen_maya_idle", "ep10_fr_tg_kitchen_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
if "tg_part1b" not in event_list and "tg_part2" not in event_list:
    $ ui.imagebutton("ep10_fr_tg_kitchen_patrick_idle", "ep10_fr_tg_kitchen_patrick_hover", clicked=ui.returns("patrick"), xpos=0, ypos=0, focus_mask=True)
if "tg_part2" not in event_list:
    $ ui.imagebutton("ep10_fr_tg_kitchen_turkey_idle", "ep10_fr_tg_kitchen_turkey_hover", clicked=ui.returns("turkey"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[7][1]:
    $ ui.imagebutton("ep10_packquest_btn7_idle", "ep10_packquest_btn7_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "maya":
    if "ep10_tg_mp_label" in event_list:
        $ currentEvent = "ep10_tg_mp_label"
    else:
        $ currentEvent = "ep10_tg2_mp_label"
    jump startEvent
elif result == "turkey":
    mc "(Ah, the turkey. The food looks and smells familiar.)"
    jump ep10_fr_tg_kitchen_label
elif result == "patrick":
    mc "(He's busy with the last preparations, it seems. This should buy me some time to snoop around. I gotta find that binder!)"
    jump ep10_fr_tg_kitchen_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[7][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_bedroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_bedroom_label"

if "tg_part2" in event_list:
    scene ep10_fr_tg_bedroomc with dissolve
elif "tg_part1b" in event_list:
    scene ep10_fr_tg_bedroomb with dissolve
else:
    scene ep10_fr_tg_bedroom with dissolve

if "ep10_tg_helen_label" in event_list:
    $ ui.imagebutton("ep10_fr_tg_bedroom_derek_idle", "ep10_fr_tg_bedroom_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)

if "tg_part2" in event_list and pack_quest_active and not pack_quest_list[4][1]:
    $ ui.imagebutton("ep10_packquest_btn4_idle", "ep10_packquest_btn4_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_up_hall_label
elif result == "derek":
    $ currentEvent = "ep10_tg_helen_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[4][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_bathroom_label"

scene ep10_fr_tg_bathroom with dissolve

$ ui.imagebutton("ep10_fr_tg_bathroom_laundry_idle", "ep10_fr_tg_bathroom_laundry_hover", clicked=ui.returns("laundry"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_bathroom_toilet_idle", "ep10_fr_tg_bathroom_toilet_hover", clicked=ui.returns("toilet"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[3][1]:
    $ ui.imagebutton("ep10_packquest_btn3_idle", "ep10_packquest_btn3_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_up_hall_label
elif result == "laundry":
    mc "(That's a lot of dirty laundry.)"
    jump ep10_fr_tg_bathroom_label
elif result == "toilet":
    mc "(Is it ok to use that toilet? I feel kinda weird about it.)"
    jump ep10_fr_tg_bathroom_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[3][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_up_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_up_bathroom_label"

scene ep10_fr_tg_up_bathroom with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_upstairs_hall_label


label ep10_fr_tg_maya_room_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_maya_room_label"

scene ep10_fr_tg_maya_room with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "go_right":
    jump ep10_fr_tg_maya_room_right_label
elif result == "go_left":
    jump ep10_fr_tg_maya_room_left_label

label ep10_fr_tg_derek_room_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_derek_room_label"

scene ep10_fr_tg_derek_room with dissolve

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "go_left":
    jump ep10_fr_tg_derek_room_left_label

label ep10_fr_tg_derek_room_left_label:
if not persistent.ep10_cardzo9:
    scene ep10_fr_tg_derek_room_left_card with dissolve
else:
    scene ep10_fr_tg_derek_room_left with dissolve
label ep10_fr_tg_derek_room_left_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_derek_room_left_label"

if not persistent.ep10_cardzo9:
    $ ui.imagebutton("ep10_fr_tg_derek_room_left_card_idle", "ep10_fr_tg_derek_room_left_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[5][1]:
    $ ui.imagebutton("ep10_packquest_btn5_idle", "ep10_packquest_btn5_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_derek_room_left_door_idle", "ep10_fr_tg_derek_room_left_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_derek_room_label
elif result == "door":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardzo9 = True
    $ persistent.rew_zoey_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_fr_tg_derek_room_left with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_derek_room_left_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[5][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_maya_room_right_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_maya_room_right_label"

scene ep10_fr_tg_maya_room_right with dissolve

if pack_quest_active and not pack_quest_list[2][1]:
    $ ui.imagebutton("ep10_packquest_btn2_idle", "ep10_packquest_btn2_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_maya_room_right_door_idle", "ep10_fr_tg_maya_room_right_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()


if result == "door":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "go_down":
    jump ep10_fr_tg_maya_room_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[2][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep10_fr_tg_maya_room_left_label:
if not found_money2:
    scene ep10_fr_tg_maya_room_left_cash with dissolve
else:
    scene ep10_fr_tg_maya_room_left with dissolve
label ep10_fr_tg_maya_room_left_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_maya_room_left_label"

$ ui.imagebutton("ep10_fr_tg_maya_room_left_door_idle", "ep10_fr_tg_maya_room_left_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if not found_money2:
    $ ui.imagebutton("ep10_fr_tg_maya_room_cash_idle", "ep10_fr_tg_maya_room_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()


if result == "door":
    jump ep10_fr_tg_upstairs_hall_label
elif result == "go_down":
    jump ep10_fr_tg_maya_room_label
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep10_fr_tg_maya_room_left with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_fr_tg_maya_room_left_label_nofx

label ep10_fr_tg_upstairs_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_upstairs_hall_label"
if ep8_told_josy_chad and "ep10_tg_d_label" in event_list:
    scene ep10_fr_tg_upstairs_hall_sage with dissolve
else:
    scene ep10_fr_tg_upstairs_hall with dissolve

$ ui.imagebutton("ep10_fr_tg_upstairs_hall_ldoor1_idle", "ep10_fr_tg_upstairs_hall_ldoor1_hover", clicked=ui.returns("ldoor1"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_upstairs_hall_rdoor1_idle", "ep10_fr_tg_upstairs_hall_rdoor1_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)

if ep8_told_josy_chad and "ep10_tg_d_label" in event_list:
    $ ui.imagebutton("ep10_fr_tg_upstairs_hall_cdoor2_idle", "ep10_fr_tg_upstairs_hall_cdoor2_hover", clicked=ui.returns("cdoor"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep10_fr_tg_upstairs_hall_cdoor_idle", "ep10_fr_tg_upstairs_hall_cdoor_hover", clicked=ui.returns("cdoor"), xpos=0, ypos=0, focus_mask=True)

if "ep10_tg_d_label" in event_list:
    if ep8_told_josy_chad:
        $ ui.imagebutton("ep10_fr_tg_upstairs_hall_sage_idle", "ep10_fr_tg_upstairs_hall_sage_hover", clicked=ui.returns("office_event"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep10_fr_tg_upstairs_hall_ldoor2_idle", "ep10_fr_tg_upstairs_hall_ldoor2_hover", clicked=ui.returns("office_event"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep10_fr_tg_upstairs_hall_ldoor2_idle", "ep10_fr_tg_upstairs_hall_ldoor2_hover", clicked=ui.returns("ldoor2"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_main_hall_label
elif result == "ldoor1":
    jump ep10_fr_tg_maya_room_label
elif result == "ldoor2":
    if "tg_part2" in event_list:
        if "no_keys" in event_list:
            mc "(The keys are in the garage. I need to hurry!)"
        else:
            stop music fadeout 3
            $ currentEvent = "ep10_tg_hide_event_label"
            jump startEvent
    else:
        mc "(The door is locked. I need to find the keys.)"
    jump ep10_fr_tg_upstairs_hall_label
elif result == "rdoor":
    jump ep10_fr_tg_up_bathroom_label
elif result == "cdoor":
    jump ep10_fr_tg_derek_room_label
elif result == "office_event":
    $ currentEvent = "ep10_tg_d_label"
    jump startEvent

label ep10_fr_tg_office_shelf_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_office_shelf_label"
scene ep10_fr_tg_office_shelf with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep10_fr_tg_office_car_idle", "ep10_fr_tg_office_car_hover", clicked=ui.returns("car"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_sbinders_idle", "ep10_fr_tg_office_sbinders_hover", clicked=ui.returns("binders"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer1_idle", "ep10_fr_tg_office_drawer1_hover", clicked=ui.returns("drawer1"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer2_idle", "ep10_fr_tg_office_drawer2_hover", clicked=ui.returns("drawer2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer3_idle", "ep10_fr_tg_office_drawer3_hover", clicked=ui.returns("drawer3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer4_idle", "ep10_fr_tg_office_drawer4_hover", clicked=ui.returns("drawer4"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer5_idle", "ep10_fr_tg_office_drawer5_hover", clicked=ui.returns("drawer5"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer6_idle", "ep10_fr_tg_office_drawer6_hover", clicked=ui.returns("drawer6"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_drawer7_idle", "ep10_fr_tg_office_drawer7_hover", clicked=ui.returns("drawer7"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "drawer1":
    play sound "sound_effects/season3/drawer_open.mp3"
    scene ep10_tg_drawer1 with dissolve
    mc "(No binders... This might not be the right place to look for it.)"
    play sound "sound_effects/season3/drawer_open.mp3"
    jump ep10_fr_tg_office_shelf_label
elif result == "drawer2":
    play sound "sound_effects/season3/drawer_open.mp3"
    scene ep10_tg_drawer2 with dissolve
    mc "(Nope. This isn't it.)"
    play sound "sound_effects/season3/drawer_open.mp3"
    jump ep10_fr_tg_office_shelf_label
elif result == "binders":
    mc "(Hm. Nope. These aren't what I'm looking for. Derek said the binder was white.)"
    jump ep10_fr_tg_office_shelf_label
elif result == "car":
    mc "(A toy car. Cute.)"
    jump ep10_fr_tg_office_shelf_label
elif result == "drawer3":
    play sound "sound_effects/season3/drawer_open.mp3"
    scene ep10_tg_drawer3 with dissolve
    mc "(That's a lot of papers...and some utility bills... This doesn't seem to be it.)"
    play sound "sound_effects/season3/drawer_open.mp3"
    jump ep10_fr_tg_office_shelf_label
elif result == "drawer4":
    play sound "sound_effects/season3/drawer_open.mp3"
    scene ep10_tg_drawer4 with dissolve
    mc "({color=#00ff00}3{/color} stacks of paper.)"
    play sound "sound_effects/season3/drawer_open.mp3"
    jump ep10_fr_tg_office_shelf_label
elif result == "drawer5":
    play sound "sound_effects/season3/drawer_locked.mp3"
    mc "(The drawer is jammed. I can't open it.)"
    jump ep10_fr_tg_office_shelf_label
elif result == "drawer6":
    play sound "sound_effects/season3/drawer_open.mp3"
    label ep10_fr_tg_office_shelf_6_label:
    if not persistent.ep10_cardzo10:
        scene ep10_tg_drawer6_card with dissolve
    else:
        scene ep10_tg_drawer6 with dissolve
    mc "(Huh? What are these? Dirty magazines... Very Christian.)"
    label ep10_fr_tg_office_shelf_6_label_nofx:
    $ renpy.block_rollback()
    $ currentFreeRoamLabel = "ep10_fr_tg_office_shelf_6_label"
    if not persistent.ep10_cardzo10:
        $ ui.imagebutton("ep10_tg_drawer6_card_idle", "ep10_tg_drawer6_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep10_tg_drawer6_drawer_idle", "ep10_tg_drawer6_drawer_hover", clicked=ui.returns("drawer"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep10_tg_drawer_idle", "ep10_tg_drawer_hover", clicked=ui.returns("go_down"), xpos=0, ypos=0, focus_mask=True)
    $ result = ui.interact()
    if result == "go_down":
        jump ep10_fr_office_shelf_label
    elif result == "drawer":
        play sound "sound_effects/season3/drawer_open.mp3"
        jump ep10_fr_tg_office_shelf_label
    elif result == "hidden_card":
        $ renpy.block_rollback()
        $ persistent.ep10_cardzo10 = True
        $ persistent.rew_zoey_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
        scene ep10_tg_drawer6 with dissolve
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
        jump ep10_fr_tg_office_shelf_6_label_nofx
elif result == "drawer7":
    play sound "sound_effects/season3/drawer_open.mp3"
    scene ep10_tg_drawer7 with dissolve
    mc "(Nothing...)"
    play sound "sound_effects/season3/drawer_open.mp3"
    jump ep10_fr_tg_office_shelf_label
elif result == "go_down":
    jump ep10_fr_tg_office_label

label ep10_fr_tg_office_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_office_label"
scene ep10_fr_tg_office with dissolve

$ ui.imagebutton("ep10_fr_tg_office_shelf_idle", "ep10_fr_tg_office_shelf_hover", clicked=ui.returns("shelf"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_desk_idle", "ep10_fr_tg_office_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "shelf":
    jump ep10_fr_tg_office_shelf_label
elif result == "go_left":
    jump ep10_fr_tg_office_left_label
elif result == "go_right":
    jump ep10_fr_tg_office_right_label
elif result == "desk":
    jump ep10_fr_tg_office_desk_label

label ep10_fr_tg_office_left_label:
if not persistent.ep10_cardzo11:
    scene ep10_fr_tg_office_left_card with dissolve
else:
    scene ep10_fr_tg_office_left with dissolve
label ep10_fr_tg_office_left_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_office_left_label"


if not persistent.ep10_cardzo11:
    $ ui.imagebutton("ep10_fr_tg_office_left_card_idle", "ep10_fr_tg_office_left_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_binder1_idle", "ep10_fr_tg_office_binder1_hover", clicked=ui.returns("binder1"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_binder2_idle", "ep10_fr_tg_office_binder2_hover", clicked=ui.returns("binder2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_binder3_idle", "ep10_fr_tg_office_binder3_hover", clicked=ui.returns("binder3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_binder4_idle", "ep10_fr_tg_office_binder4_hover", clicked=ui.returns("binder4"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "binder1":
    menu:
        "End free roam":
            mc "(\"Loans and personal documents\". Hm... This one could be worth a look.)"
            $ phone_clear_jump_label = "ep10_fr_tg_end_label"
            jump end_freeroam
        "Not yet":
            jump ep10_fr_tg_office_left_label
elif result == "binder2":
    mc "(The binder reads \"Work\". This isn't what I'm looking for.)"
    jump ep10_fr_tg_office_left_label
elif result == "binder3":
    mc "(The binder reads \"Travel\". Nope. Keep searching!)"
    jump ep10_fr_tg_office_left_label
elif result == "binder4":
    mc "(\"Insurance\". Yeah, it is not related to Maya.)"
    jump ep10_fr_tg_office_left_label
elif result == "go_right":
    jump ep10_fr_tg_office_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardzo11 = True
    $ persistent.rew_zoey_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_fr_tg_office_left with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_fr_tg_office_left_label_nofx

label ep10_fr_tg_office_right_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_office_right_label"
scene ep10_fr_tg_office_right with dissolve

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep10_fr_tg_office_wb_idle", "ep10_fr_tg_office_wb_hover", clicked=ui.returns("wb"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_left":
    jump ep10_fr_tg_office_label
elif result == "wb":
    if affinity == "DIK":
        mc "(Must resist the urge to draw a giant cock.)"
    else:
        mc "(I would be stupid to touch that whiteboard. He'd probably notice.)"
    jump ep10_fr_tg_office_right_label

label ep10_fr_tg_office_desk_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_fr_tg_office_desk_label"
scene ep10_fr_tg_office_desk with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep10_fr_tg_office_desk_printer_idle", "ep10_fr_tg_office_desk_printer_hover", clicked=ui.returns("printer"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_desk_calc_idle", "ep10_fr_tg_office_desk_calc_hover", clicked=ui.returns("calc"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_fr_tg_office_desk_pc_idle", "ep10_fr_tg_office_desk_pc_hover", clicked=ui.returns("pc"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_down":
    jump ep10_fr_tg_office_label
elif result == "printer":
    mc "(The paper in the printer is of no importance.)"
    jump ep10_fr_tg_office_desk_label
elif result == "calc":
    mc "(Just a calculator.)"
    jump ep10_fr_tg_office_desk_label
elif result == "pc":
    mc "(That's a pretty nice computer. I wish I could afford one... Well, I can, but I don't wanna waste my money on it.)"
    jump ep10_fr_tg_office_desk_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

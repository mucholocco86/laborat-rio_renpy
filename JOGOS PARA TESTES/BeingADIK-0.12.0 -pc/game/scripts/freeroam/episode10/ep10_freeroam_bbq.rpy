label ep10_freeroam_bbq_label:
$ freeRoamID = "ep10_3"
$ roosterState = "ep10_3"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 135
$ found_money = False
$ found_money2 = False
$ studied = False

$ disabled_apps = []
$ disabled_apps.append("brawler")
$ firstTimeFreeRoam = True
$ game_money_available = True
$ triple_tile_money_available = True

$ rooster_jump_label = "ep10_bbq_main_label"
jump initRoosterLabel


label ep10_bbq_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_main_label"

if "ep10_bbq_jacob_event_label" in event_list:
    $ currentEvent = "ep10_bbq_jacob_event_label"
    jump startEvent

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ current_task = ""
    if ep10_shroom_choice == "DIK":
        $ task_list = ["","","","Greet the blueberry","Talk to the nude man","","","","","","",""]
    else:
        $ task_list = ["","","","Greet Zoey","Talk to John Boy","","","","","","",""]
    $ optional_task_list = ["","",""]

    $ chat_new_tasks = True
    $ event_list = []

    if ep10_ufo == 51 and ep10_shroom_choice == "DIK":
        $ event_list.append("ep10_bbq_ufo_event_label")

    if ep10_shroom_choice == "DIK":
        $ event_list.append("ep10_bbq_santa_event_label")

    if ep10_pp_activity == 0:
        if ep10_shroom_choice == "DIK":
            $ task_list[11] = "Acquire floating sphere"
        else:
            $ task_list[11] = "Talk to Derek"
        $ event_list.append("ep10_bbq_dc_event_label")
    if branchIsabella:
        $ event_list.append("ep10_bbq_final_phase")
    if ep10_riona_date:
        $ event_list.append("ep10_bbq_rio_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[1] = "Find the shapeshifter"
        else:
            $ task_list[1] = "Find Riona"


    if branchSage and ep10_shroom_choice != "DIK":
        $ event_list.append("ep10_bbq_guitar_s_event_label")
        $ optional_task_list[0] = "Play guitar by the fire"
    if branchMayaJosy and ep10_shroom_choice != "DIK":
        $ event_list.append("ep10_bbq_guitar_jm_event_label")
        $ optional_task_list[0] = "Play guitar by the fire"
    if branchJill:
        if ep10_shroom_choice != "DIK":
            $ event_list.append("ep10_bbq_guitar_j_event_label")
            $ task_list[6] = "Play guitar by the fire"
        else:
            if ep10_pp_activity != 0:
                $ event_list.append("ep10_bbq_guitar_high_event_label")
                $ task_list[6] = "Play the Bard's song"
    if ep10_shroom_choice != "DIK" and branchAlone:
        $ event_list.append("ep10_bbq_guitar_others_event_label")
        $ optional_task_list[0] = "Play guitar by the fire"

    if not branchJill:
        if ep10_shroom_choice == "DIK":
            $ task_list[6] = "Talk to the elf"
        else:
            $ task_list[6] = "Talk to Jill"

    if not (branchAlone and ep8_quinn_lewd):
        $ event_list.append("ep10_bbq_q_pos")

    if branchAlone and ep8_quinn_lewd:
        $ event_list.append("ep10_bbq_q_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[7] = "Find the white-haired maiden"
        else:
            $ task_list[7] = "Talk to Quinn"
    elif ep10_rolling:
        if ep10_shroom_choice == "DIK":
            $ task_list[7] = "Find your queen"
        else:
            $ task_list[7] = "Find Lily"
        $ event_list.append("ep10_bbq_lroll_event_label")


    if branchMayaJosy:
        $ event_list.append("ep10_bbq_1dg_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[8] = "Inspect the rogue and the druid"
        else:
            $ task_list[8] = "Find Josy and Maya"
    else:
        $ event_list.append("ep10_bbq_msolo_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[8] = "Talk to the druid"
        else:
            $ task_list[8] = "Talk to Maya"

    if ep10_dating_nora:
        $ event_list.append("ep10_bbq_nora_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[10] = "Find the unicorn"
        else:
            $ task_list[10] = "Talk to Nora"

    if (ep10_jm_solo == "Josy" or ep10_jm_solo=="Maya Josy") and not branchMayaJosy:
        $ event_list.append("ep10_bbq_jsolo_event_label")

    $ event_list.append("jill_block")
    $ event_list.append("ep10_bbq_z_event_label")
    $ event_list.append("ep10_bbq_jb_event_label")
    $ event_list.append("ep10_bbq_eh_event_label")
    $ event_list.append("ep10_bbq_at_event_label")
    $ event_list.append("ep10_bbq_sy_event_label")

    if not branchJill:
        $ event_list.append("ep10_bbq_jillvar_event_label")

    if branchIsabella:
        $ event_list.append("ep10_bbq_bella_event_label")
        if ep10_shroom_choice == "DIK":
            $ task_list[0] = "Listen to the mermaid's song"
        else:
            $ task_list[0] = "Go to the lake"

    if ep10_shroom_choice == "DIK" and not branchJill:
        $ event_list.append("ep10_bbq_guitar_high_event_label")
        $ optional_task_list[0] = "Play the Bard's song"

    if ep10_shroom_choice == "DIK":
        $ optional_task_list[1] = "Find the lifeguard"
        $ optional_task_list[2] = "Find the village idiot"
        $ task_list[2] = "Talk to the wicked witch"
    else:
        $ optional_task_list[1] = "Find Heather"
        $ optional_task_list[2] = "Find Arieth"
        $ task_list[2] = "Talk to Sally"

    $ updateTaskList()

if ep10_pp_activity == 0:
    if "ep10_bbq_dc_event_label" in event_list:
        scene ep10_bbq_main with dissolve
    else:
        if "ep10_bbq_final_phase" in event_list:
            scene ep10_bbq_main_bp_final with dissolve
        else:
            scene ep10_bbq_main_bp_empty with dissolve
else:
    if "ep10_bbq_final_phase" in event_list:
        scene ep10_bbq_mainb_final with dissolve
    else:
        scene ep10_bbq_mainb with dissolve

if firstTimeFreeRoam:
    $ firstTimeFreeRoam = False
    if ep10_shroom_choice == "DIK":
        show screen freeroam_intro_screen("Explore the magic kingdom")
    else:
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
    hide screen freeroam_intro_screen

if "ep10_bbq_dc_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_main_derek_idle", "ep10_bbq_main_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
elif "ep10_bbq_bps_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_main_bp_idle", "ep10_bbq_main_bp_hover", clicked=ui.returns("bps"), xpos=0, ypos=0, focus_mask=True)
elif "ep10_bbq_bpj_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_main_bp_idle", "ep10_bbq_main_bp_hover", clicked=ui.returns("bpj"), xpos=0, ypos=0, focus_mask=True)
elif "ep10_bbq_bpjo_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_main_bp_idle", "ep10_bbq_main_bp_hover", clicked=ui.returns("bpjo"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1250 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_up":
    jump ep10_bbq_diks_fire_label
elif result == "go_down":
    jump ep10_bbq_diks_table_label
elif result == "bps":
    $ currentEvent = "ep10_bbq_bps_event_label"
    jump startEvent
elif result == "bpj":
    $ currentEvent = "ep10_bbq_bpj_event_label"
    jump startEvent
elif result == "bpjo":
    $ currentEvent = "ep10_bbq_bpjo_event_label"
    jump startEvent
elif result == "derek":
    $ currentEvent = "ep10_bbq_dc_event_label"
    jump startEvent

label ep10_bbq_diks_table_label:
if "ep10_bbq_z_event_label" in event_list:
    $ renpy.block_rollback()
    $ currentFreeRoamLabel = "ep10_bbq_diks_table_label"
    $ currentEvent = "ep10_bbq_z_event_label"
    jump startEvent

if found_money2:
    if "jacob_block" in event_list:
        scene ep10_bbq_diks_table with dissolve
    else:
        scene ep10_bbq_diks_table_z with dissolve
else:
    if "jacob_block" in event_list:
        scene ep10_bbq_diks_table_cash with dissolve
    else:
        scene ep10_bbq_diks_table_z_cash with dissolve

label ep10_bbq_diks_table_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_diks_table_label"

if not found_money2:
    $ ui.imagebutton("ep10_bbq_diks_table_cash_idle", "ep10_bbq_diks_table_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_jill2_event_label" in event_list and ep10_shroom_choice == "DIK" and "jacob_block" in event_list and not "jill_block" in event_list:
    $ ui.imagebutton("ep10_bbq_diks_table_rusty_idle", "ep10_bbq_diks_table_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_z2_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_diks_table_zoey_idle", "ep10_bbq_diks_table_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_nick_event_label" in event_list and "jacob_block" in event_list:
    $ ui.imagebutton("ep10_bbq_diks_table_nick_idle", "ep10_bbq_diks_table_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "nick":
    $ currentEvent = "ep10_bbq_nick_event_label"
    jump startEvent
elif result == "rusty":
    $ currentEvent = "ep10_bbq_jill2_event_label"
    jump startEvent
elif result == "zoey":
    $ currentEvent = "ep10_bbq_z2_event_label"
    jump startEvent
elif result == "go_down":
    jump ep10_bbq_main_label
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    if "jacob_block" in event_list:
        scene ep10_bbq_diks_table with dissolve
    else:
        scene ep10_bbq_diks_table_z with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_bbq_diks_table_label_nofx

label ep10_bbq_diks_fire_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_diks_fire_label"
$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)

if "sally_block" in event_list:
    scene ep10_bbq_diks_fire_nos with dissolve
elif "ep10_bbq_final_phase" in event_list:
    scene ep10_bbq_diks_fire_final with dissolve
else:
    scene ep10_bbq_diks_fire with dissolve

if "ep10_bbq_sy_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_diks_fire_sally_idle", "ep10_bbq_diks_fire_sally_hover", clicked=ui.returns("sally"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "sally":
    $ currentEvent = "ep10_bbq_sy_event_label"
    jump startEvent
elif result == "go_left":
    if "sally_block" in event_list:
        $ event_list.remove("sally_block")
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    jump ep10_bbq_tent_label
elif result == "go_right":
    if "sally_block" in event_list:
        $ event_list.remove("sally_block")
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    jump ep10_bbq_hots_label
elif result == "go_down":
    if "sally_block" in event_list:
        $ event_list.remove("sally_block")
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    jump ep10_bbq_main_label

label ep10_bbq_tent_label:
if found_money:
    scene ep10_bbq_tent with dissolve
else:
    scene ep10_bbq_tent_cash with dissolve
label ep10_bbq_tent_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_tent_label"

if not found_money:
    $ ui.imagebutton("ep10_bbq_tent_cash_idle", "ep10_bbq_tent_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if current_task == "Go to your tent":
    $ ui.imagebutton("ep10_bbq_tent_sleep_idle", "ep10_bbq_tent_sleep_hover", clicked=ui.returns("tent"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_guitar_s_event_label" in event_list or "ep10_bbq_guitar_jm_event_label" in event_list or "ep10_bbq_guitar_j_event_label" in event_list or "ep10_bbq_guitar_others_event_label" in event_list or "ep10_bbq_guitar_high_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_tent_guitar_idle", "ep10_bbq_tent_guitar_hover", clicked=ui.returns("guitar"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "guitar":
    if "ep10_bbq_guitar_s_event_label" in event_list:
        $ currentEvent = "ep10_bbq_guitar_s_event_label"
    elif "ep10_bbq_guitar_jm_event_label" in event_list:
        $ currentEvent = "ep10_bbq_guitar_jm_event_label"
    elif "ep10_bbq_guitar_j_event_label" in event_list:
        $ currentEvent = "ep10_bbq_guitar_j_event_label"
    elif "ep10_bbq_guitar_others_event_label" in event_list:
        $ currentEvent = "ep10_bbq_guitar_others_event_label"
    elif "ep10_bbq_guitar_high_event_label" in event_list:
        $ currentEvent = "ep10_bbq_guitar_high_event_label"
    jump startEvent
elif result == "go_right":
    jump ep10_bbq_diks_fire_label
elif result == "tent":
    $ currentEvent = "ep10_freeroam_bbq2_end_label"
    jump startEvent
    label ep10_freeroam_bbq2_end_label:
    menu:
        "End free roam":
            $ phone_clear_jump_label = "ep10_bbq_jz_event_label"
            jump end_freeroam
        "Not yet":
            $ renpy.pause(0.5)
    jump endEvent
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep10_bbq_tent with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_bbq_tent_label_nofx

label ep10_bbq_hots_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_hots_label"

if "ep10_bbq_lroll_event_label" in event_list:
    $ currentEvent = "ep10_bbq_lroll_event_label"
    jump startEvent

if not persistent.ep10_cardsa5:
    if "jill_block" in event_list:
        scene ep10_bbq_hots_card with dissolve
    else:
        if "ep10_bbq_jsolo_event_label" in event_list:
            scene ep10_bbq_hotsjjo_card with dissolve
        else:
            scene ep10_bbq_hotsj_card with dissolve
else:
    if "jill_block" in event_list:
        scene ep10_bbq_hots with dissolve
    else:
        if "ep10_bbq_jsolo_event_label" in event_list:
            scene ep10_bbq_hotsjjo with dissolve
        else:
            scene ep10_bbq_hotsj with dissolve

label ep10_bbq_hots_label_nofx:
if "ep10_bbq_eh_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_hots_heather_idle", "ep10_bbq_hots_heather_hover", clicked=ui.returns("heather"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_s_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_hots_sage_idle", "ep10_bbq_hots_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_msolo_event_label" in event_list:
    if "jill_block" in event_list:
        $ ui.imagebutton("ep10_bbq_hots_maya_idle", "ep10_bbq_hots_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep10_bbq_hots_maya2_idle", "ep10_bbq_hots_maya2_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_1dg_event_label" in event_list:
    if "jill_block" in event_list:
        $ ui.imagebutton("ep10_bbq_hots_maya_idle", "ep10_bbq_hots_maya_hover", clicked=ui.returns("maya2"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep10_bbq_hots_maya2_idle", "ep10_bbq_hots_maya2_hover", clicked=ui.returns("maya2"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_at_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_hots_arieth_idle", "ep10_bbq_hots_arieth_hover", clicked=ui.returns("arieth"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa5:
    $ ui.imagebutton("ep10_bbq_hots_card_idle", "ep10_bbq_hots_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_jill2_event_label" in event_list and ep10_shroom_choice != "DIK":
    $ ui.imagebutton("ep10_bbq_hots_jill_idle", "ep10_bbq_hots_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep10_bbq_hots_cups_idle", "ep10_bbq_hots_cups_hover", clicked=ui.returns("cups"), xpos=0, ypos=0, focus_mask=True)


$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep10_bbq_bathroom_label
elif result == "go_down":
    jump ep10_bbq_diks_fire_label
elif result == "heather":
    $ currentEvent = "ep10_bbq_eh_event_label"
    jump startEvent
elif result == "sage":
    $ currentEvent = "ep10_bbq_s_event_label"
    jump startEvent
elif result == "maya":
    $ currentEvent = "ep10_bbq_msolo_event_label"
    jump startEvent
elif result == "maya2":
    $ currentEvent = "ep10_bbq_1dg_event_label"
    jump startEvent
elif result == "arieth":
    $ currentEvent = "ep10_bbq_at_event_label"
    jump startEvent
elif result == "cups":
    mc "(Just {color=00ff00}3{/color} stacks of cups.)"
    jump ep10_bbq_hots_label
elif result == "jill":
    $ currentEvent = "ep10_bbq_jill2_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa5 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "jill_block" in event_list:
        scene ep10_bbq_hots with dissolve
    else:
        scene ep10_bbq_hotsj with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_bbq_hots_label_nofx

label ep10_bbq_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_bathroom_label"

if "ep10_bbq_jillvar_event_label" in event_list:
    $ currentFreeRoamLabel = "ep10_bbq_bathroom_label_nofx"
    $ currentEvent = "ep10_bbq_jillvar_event_label"
    jump startEvent
elif "ep10_bbq_jb_event_label" in event_list:
    $ currentEvent = "ep10_bbq_jb_event_label"
    jump startEvent

if "ep10_bbq_jsolo_event_label" in event_list and not "jill_block" in event_list:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_qj_card with dissolve
    else:
        scene ep10_bbq_bathroom_qj with dissolve
elif "ep10_bbq_q_event_label" in event_list or "ep10_bbq_q_pos" in event_list:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_q_card with dissolve
    else:
        scene ep10_bbq_bathroom_q with dissolve
else:
    if not persistent.ep10_cardsa6:
        scene ep10_bbq_bathroom_card with dissolve
    else:
        scene ep10_bbq_bathroom with dissolve
label ep10_bbq_bathroom_label_nofx:
$ currentFreeRoamLabel = "ep10_bbq_bathroom_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

if "ep10_bbq_jsolo_event_label" in event_list and not "jill_block" in event_list:
    $ ui.imagebutton("ep10_bbq_bathroom_josy_idle", "ep10_bbq_bathroom_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa6:
    $ ui.imagebutton("ep10_bbq_bathroom_card_idle", "ep10_bbq_bathroom_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep10_bbq_q_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_bathroom_q_idle", "ep10_bbq_bathroom_q_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_down":
    jump ep10_bbq_hots_label
elif result == "go_left":
    jump ep10_bbq_bench_label
elif result == "quinn":
    $ currentEvent = "ep10_bbq_q_event_label"
    jump startEvent
elif result == "josy":
    $ currentEvent = "ep10_bbq_jsolo_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa6 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep10_bbq_jsolo_event_label" in event_list and not "jill_block" in event_list:
        scene ep10_bbq_bathroom_qj with dissolve
    elif "ep10_bbq_q_event_label" in event_list or "ep10_bbq_q_pos" in event_list:
        scene ep10_bbq_bathroom_q with dissolve
    else:
        scene ep10_bbq_bathroom with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_bbq_bathroom_label_nofx


label ep10_bbq_bench_label:
$ renpy.block_rollback()
if "ep10_bbq_2dg_event_label" in event_list:
    $ currentEvent = "ep10_bbq_2dg_event_label"
    jump startEvent
$ currentFreeRoamLabel = "ep10_bbq_bench_label"
if ep10_shroom_choice == "DIK":
    if "ep10_bbq_rio_event_label" in event_list:
        scene ep10_bbq_benchb_rio with dissolve
    else:
        scene ep10_bbq_benchb with dissolve
else:
    if "ep10_bbq_rio_event_label" in event_list:
        scene ep10_bbq_bench_rio with dissolve
    else:
        scene ep10_bbq_bench with dissolve

if "ep10_bbq_rio_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_bench_rio_idle", "ep10_bbq_bench_rio_hover", clicked=ui.returns("rio"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep10_bbq_forest_label
elif result == "go_right":
    jump ep10_bbq_bathroom_label
elif result == "rio":
    $ currentEvent = "ep10_bbq_rio_event_label"
    jump startEvent

label ep10_bbq_forest_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_forest_label"
if "ep10_bbq_nora_event_label" in event_list:
    $ currentEvent = "ep10_bbq_nora_event_label"
    jump startEvent

if not persistent.ep10_cardsa7:
    scene ep10_bbq_forest_card with dissolve
else:
    scene ep10_bbq_forest with dissolve

label ep10_bbq_forest_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_forest_label"

if not persistent.ep10_cardsa7:
    $ ui.imagebutton("ep10_bbq_forest_card_idle", "ep10_bbq_forest_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=300 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_up":
    if "ep10_bbq_ufo_event_label" in event_list:
        $ currentEvent = "ep10_bbq_ufo_event_label"
        jump startEvent
    else:
        jump ep10_bbq_lake_label
elif result == "go_right":
    jump ep10_bbq_bench_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa7 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep10_bbq_forest with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_bbq_forest_label_nofx

label ep10_bbq_lake_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_bbq_lake_label"

if "ep10_bbq_bella_event_label" in event_list:
    $ currentEvent = "ep10_bbq_bella_event_label"
    jump startEvent

if ep10_shroom_choice == "DIK":
    if "ep10_bbq_santa_event_label" in event_list:
        scene ep10_bbq_lake with dissolve
    else:
        scene ep10_bbq_lakeb with dissolve
else:
    scene ep10_bbq_lake2 with dissolve

if "ep10_bbq_santa_event_label" in event_list:
    $ ui.imagebutton("ep10_bbq_lake_buoy_idle", "ep10_bbq_lake_buoy_hover", clicked=ui.returns("buoy"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep10_bbq_forest_label
elif result == "buoy":
    $ currentEvent = "ep10_bbq_santa_event_label"
    jump startEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

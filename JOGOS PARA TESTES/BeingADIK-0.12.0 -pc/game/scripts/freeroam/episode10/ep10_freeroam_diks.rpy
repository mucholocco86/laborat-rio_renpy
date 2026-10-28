label ep10_freeroam_diks:
$ freeRoamID = "ep10_1"
$ roosterState = "ep10_1"
$ tmpInt = 0
show screen wt_tasks_shown

$ mphone_music_genre = 3
$ mphone_next_song()

$ found_money = False
$ found_money2 = False
$ studied = False

$ disabled_apps = []
$ disabled_apps.append("brawler")
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

$ art_girl_lvl2_list[3] = branchIsabella
$ art_girl_crit2_list[3] = "- Played Isabella's branch"
$ art_girl_lvl2_list[5] = branchJill
$ art_girl_crit2_list[5] = "- Played Jill's branch"
$ art_girl_lvl2_list[6] = branchMayaJosy
$ art_girl_crit2_list[6] = "- Played Josy & Maya's branch"
$ art_girl_lvl2_list[13] = branchSage
$ art_girl_crit2_list[13] = "- Played Sage's branch"

if not persistent.art_unlocked_lvl2[3] or not persistent.art_unlocked_lvl2[5] or not persistent.art_unlocked_lvl2[6] or not persistent.art_unlocked_lvl2[13]:
    $ mphone_new_art_available = True
$ art_girl_new_icon[3] = not persistent.art_unlocked_lvl2[3]
$ art_girl_new_icon[5] = not persistent.art_unlocked_lvl2[5]
$ art_girl_new_icon[6] = not persistent.art_unlocked_lvl2[6]
$ art_girl_new_icon[13] = not persistent.art_unlocked_lvl2[13]

$ rooster_jump_label = "ep10_diks_fr1_lib_mid_label"

$ map_system_list = []
$ map_system_list.append(["ep10_diks_fr1_lib_mid","ep10_diks_fr1_lib_mid_label","Your room"])
$ map_system_list.append(["ep10_diks_fr1_derek","ep10_diks_fr1_derek_label","Derek's room"])
$ map_system_list.append(["ep10_diks_fr1_dining","ep10_diks_fr1_dining_label","Dining room"])
$ map_system_list.append(["ep10_diks_fr1_jacob","ep10_diks_fr1_jacob_label","Jacob's room"])
$ map_system_list.append(["ep10_diks_fr1_jamie","ep10_diks_fr1_jamie_label","Jamie's room"])
$ map_system_list.append(["ep10_diks_fr1_jb","ep10_diks_fr1_jb_label","John Boy's room"])
$ map_system_list.append(["ep10_diks_fr1_left_hall2","ep10_diks_fr1_left_hall2_label","Left hallway"])
$ map_system_list.append(["ep10_diks_fr1_leon_room","ep10_diks_fr1_leon_room_label","Leon's room"])
$ map_system_list.append(["ep10_diks_fr1_maind","ep10_diks_fr1_main_label","Main party room"])
$ map_system_list.append(["ep10_diks_fr1_nick","ep10_diks_fr1_nick_label","Nick's room"])
$ map_system_list.append(["ep10_diks_fr1_outdoorsb","ep10_diks_fr1_outdoors_label","Outside"])
$ map_system_list.append(["ep10_diks_fr1_right_hall","ep10_diks_fr1_right_hall_label","Right hallway"])
$ map_system_list.append(["ep10_diks_fr1_rusty_room","ep10_diks_fr1_rusty_room_label","Rusty's room"])
$ map_system_list.append(["ep10_diks_fr1_tommy_room","ep10_diks_fr1_tommy_label","Tommy's room"])
$ map_system_list.append(["ep10_diks_fr1_ua","ep10_diks_fr1_ua_label","Upper main room"])

$ mgallery_init_chat_album()
$ mphone_app_gallery_enabled = True

jump initRoosterLabel

label ep10_diks_fr1_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_lib_mid_label"
scene ep10_diks_fr1_lib_mid with dissolve

if firstTimeFreeRoam:
    label ep10_fr1_first_label:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    if persistent.mod_wt_enabled:
        $ task_list = ["Clean the mansion 0/5", "Talk to Josy (Main Party room)", "Talk to Nick (Upper Main room)", "Talk to Jacob (Main Party room)", "Talk to Quinn (Outside)", "","Check rooms for hidden cameras 0/5","Talk to Maya (Upper Main room)","Talk to Lily (Left Hallway)","Check your desk", "Talk to John Boy (Dining room)", "Talk to Jamie (Tommy's room)"]
    else:
        $ task_list = ["Clean the mansion 0/5", "Talk to Josy", "Talk to Nick", "Talk to Jacob", "Talk to Quinn", "","Check rooms for hidden cameras 0/5","Talk to Maya","Talk to Lily","Check your desk", "Talk to John Boy", "Talk to Jamie"]
    
    if persistent.mod_wt_enabled:
        $ optional_task_list = ["Talk to Leon (Leon's room)","","","Talk to Arieth (Right Hallway)","","Talk to Melanie (Upper main room)","","Talk to Rusty (Rusty's room)",""]
    else:
        $ optional_task_list = ["Talk to Leon","","","Talk to Arieth","","Talk to Melanie","","Talk to Rusty",""]

    $ chat_new_tasks = True
    $ event_list = []

    if branchMayaJosy:
        $ event_list.append("ep10_fr1_tommy_event_label")
    else:
        $ event_list.append("ep10_fr1_tommy_event2_label")
    $ event_list.append("ep10_fr1_jacob_event_label")
    $ event_list.append("ep10_fr1_josy_event_label")
    $ event_list.append("ep10_fr1_clean1_event_label")
    $ event_list.append("ep10_fr1_nick_event_label")
    $ event_list.append("ep10_fr1_maya_event_label")
    $ event_list.append("ep10_fr1_mel_event_label")
    $ event_list.append("ep10_fr1_clean2_event_label")
    if ep9_lily_nicole_lewd and not ep10_rolling:
        $ task_list[8] = ""
    else:
        $ event_list.append("ep10_fr1_lily_event_label")
    $ event_list.append("ep10_fr1_clean3_event_label")
    if ep8_elena_shot:
        $ event_list.append("ep10_fr1_elena_event_label")
        $ optional_task_list[4] = "Talk to Elena"
    if ep9_sarah_melanie_lewd:
        $ event_list.append("ep10_fr1_sarah_event_label")
        $ optional_task_list[8] = "Talk to Sarah"
    $ event_list.append("ep10_fr1_arieth_event_label")
    $ event_list.append("ep10_fr1_derek_event_label")
    $ event_list.append("ep10_fr1_clean5_event_label")
    $ event_list.append("ep10_fr1_leon_event_label")
    $ event_list.append("ep10_fr1_clean6_event_label")
    $ event_list.append("ep10_fr1_jb_event_label")
    $ event_list.append("ep10_fr1_clean7_event_label")
    $ event_list.append("ep10_fr1_clean8_event_label")
    $ event_list.append("ep10_fr1_jamie_event_label")
    $ event_list.append("ep10_fr1_clean4_event_label")
    $ event_list.append("ep10_fr1_clean9_event_label")
    $ event_list.append("ep10_fr1_clean10_event_label")
    $ event_list.append("ep10_fr1_desk_event_label")
    $ event_list.append("ep10_fr1_rusty_event_label")
    $ event_list.append("ep10_fr1_qc_event_label")
    if ep7_got_flower:
        $ optional_task_list[6] = "Water your flowers"
        if ep8_flower_water_level == 1:
            $ event_list.append("ep10_fr1_flower_event_label")
        else:
            $ event_list.append("ep10_fr1_flower_dead_event_label")

    $ event_list.append("ep10_fr1_camera1_event_label")
    $ event_list.append("ep10_fr1_camera2_event_label")
    $ event_list.append("ep10_fr1_camera3_event_label")
    $ event_list.append("ep10_fr1_camera4_event_label")
    $ event_list.append("ep10_fr1_camera5_event_label")
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

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep10_diks_fr1_lib_left_label
elif result == "go_right":
    jump ep10_diks_fr1_lib_right_label

label ep10_diks_fr1_left_hall_label:
$ currentFreeRoamLabel = "ep10_diks_fr1_left_hall_label"

scene ep10_diks_fr1_left_hall with dissolve

$ ui.imagebutton("ep10_diks_fr1_left_hall_jdoor_idle", "ep10_diks_fr1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_left_hall_rdoor_idle", "ep10_diks_fr1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep10_diks_fr1_left_hall2_label
elif result == "jdoor":
    jump ep10_diks_fr1_jamie_label
elif result == "rdoor":
    jump ep10_diks_fr1_rusty_room_label

label ep10_diks_fr1_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_lib_left_label"
scene ep10_diks_fr1_lib_left with dissolve
$ ui.imagebutton("ep10_diks_fr1_lib_desk_idle", "ep10_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep10_diks_fr1_lib_mid_label
elif result == "desk":
    jump ep10_library_desk_label

label ep10_library_desk_label:
image ep9_freeroam_diks_library_desk = "ep8_freeroam_diks_library_desk[ep7_current_desk_painting]"
image ep9_freeroam_diks_second_painting = "spr_second_painting[ep8_current_second_painting]"
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_library_desk_label"

if "ep10_fr1_desk_event_label" in event_list:
    $ currentEvent = "ep10_fr1_desk_event_label"
    jump startEvent

if ep7_current_desk_painting > 0:
    scene ep9_freeroam_diks_library_desk
else:
    scene ep9_freeroam_diks_library_desk0a
if branchJill:
    show ep7_polaroid_jill_spr
if ep6_fakeID:
    show ep7_fakeid_spr
if ep6_vipPass:
    show ep7_vip_spr
if ep5_dikWinner:
    show ep7_dik_helmet_spr
if persistent.triple_tile_challenge:
    show ep7_triple_tile_spr
show ep7_phone_spr
show ep7_wallet_spr

show spr_box_ep9
show ep8_gym_spr
show ep9_monkey_spr
if ep8_second_painting:
    if ep8_current_second_painting > 0:
        show ep9_freeroam_diks_second_painting
    else:
        show ep9_freeroam_diks_second_painting0
if not ep8_recital_failed:
    show ep8_concert_spr
if branchSage:
    show ep8_leaf_spr
if branchIsabella:
    show ep8_cork_spr
if branchMayaJosy:
    show spr_conch
show spr_sword
with dissolve

$ ui.imagebutton("ep9_monkey_spr", "ep9_monkey_spr", clicked=ui.returns("monkey"), xpos=0, ypos=0, focus_mask=True)
if branchJill:
    $ ui.imagebutton("ep7_polaroid_jill_spr", "ep7_polaroid_jill_spr", clicked=ui.returns("polaroid"), xpos=0, ypos=0, focus_mask=True)
if ep6_fakeID:
    $ ui.imagebutton("ep7_fakeid_spr", "ep7_fakeid_spr", clicked=ui.returns("fakeid"), xpos=0, ypos=0, focus_mask=True)
if ep6_vipPass:
    $ ui.imagebutton("ep7_vip_spr", "ep7_vip_spr", clicked=ui.returns("vip"), xpos=0, ypos=0, focus_mask=True)
if ep5_dikWinner:
    $ ui.imagebutton("ep7_dik_helmet_spr", "ep7_dik_helmet_spr", clicked=ui.returns("helmet"), xpos=0, ypos=0, focus_mask=True)
if persistent.triple_tile_challenge:
    $ ui.imagebutton("ep7_triple_tile_spr", "ep7_triple_tile_spr", clicked=ui.returns("triple_tile"), xpos=0, ypos=0, focus_mask=True)

if ep8_second_painting:
    if ep8_current_second_painting > 0:
        $ ui.imagebutton("spr_second_painting[ep8_current_second_painting]", "spr_second_painting_hover", clicked=ui.returns("second_painting"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep9_freeroam_diks_second_painting0", "spr_second_painting_hover", clicked=ui.returns("second_painting"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("spr_second_painting_buy_idle", "spr_second_painting_buy_hover", clicked=ui.returns("buy_second_painting"), xpos=0, ypos=0, focus_mask=True)
if not ep8_recital_failed:
    $ ui.imagebutton("ep8_concert_spr", "ep8_concert_spr", clicked=ui.returns("concert"), xpos=0, ypos=0, focus_mask=True)
if branchSage:
    $ ui.imagebutton("ep8_leaf_spr", "ep8_leaf_spr", clicked=ui.returns("leaf"), xpos=0, ypos=0, focus_mask=True)
if branchIsabella:
    $ ui.imagebutton("ep8_cork_spr", "ep8_cork_spr", clicked=ui.returns("cork"), xpos=0, ypos=0, focus_mask=True)
if branchMayaJosy:
    $ ui.imagebutton("spr_conch", "spr_conch", clicked=ui.returns("conch"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("spr_sword", "spr_sword", clicked=ui.returns("sword"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep8_gym_spr", "ep8_gym_spr", clicked=ui.returns("gym"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_wallet_spr", "ep7_wallet_spr_hover", clicked=ui.returns("wallet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_phone_spr2", "ep7_phone_spr2", clicked=ui.returns("phone"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_tabs_spr", "ep7_tabs_spr", clicked=ui.returns("tabs"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("spr_box_ep9", "spr_box_ep9_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library3_frame_idle", "ep7_freeroam_diks_library3_frame_hover", clicked=ui.returns("frame"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library_desk_study_idle", "ep7_freeroam_diks_library_desk_study_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep10_diks_fr1_lib_left_label
elif result == "box":
    if pb_3_lid_open[0]:
        mc "(I made some progress, but it was harder than I thought it would be. I'll play more with this box later. I need to solve it!)"
    else:
        $ qM = quick_menu
        $ quick_menu = 0
        hide screen new_phone_screen
        call screen puzzle_box_screen_ep10
        $ renpy.pause(0.5)
        show screen new_phone_screen
        $ quick_menu = qM
    jump ep10_library_desk_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep10_library_desk_label
elif result  == "second_painting":
    $ currentEvent = "ep10_choose_2nd_painting_label"
    jump startEvent
elif result  == "buy_second_painting":
    show screen newmoneymsg
    "{i}Buy a second photo frame?{/i}"
    menu:
        "Buy photo frame {color=#36ca2b}$8{/color}" if money > 7:
            hide screen newmoneymsg
            $ mny(-8)
            $ ep8_second_painting = True
        "Don't buy photo frame":
            hide screen newmoneymsg
    jump ep10_library_desk_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk_label
elif result  == "wallet":
    if wallet_lvl < 3:
        mc "(My wallet... Maybe I can afford to set aside some more money as pocket money?)"
        show screen newmoneymsg
        if wallet_lvl == 0:
            menu:
                "Upgrade wallet {color=#36ca2b}${/color}" if money > 0:
                    hide screen newmoneymsg
                    $ mny(-1)
                    $ wallet_lvl = 1
                    mc "(I think I can increase my pocket money budget to {color=#36ca2b}$6{/color}.)"
                "Don't upgrade your wallet":
                    hide screen newmoneymsg
        elif wallet_lvl == 1:
            menu:
                "Upgrade wallet {color=#36ca2b}$$${/color}" if money > 2:
                    hide screen newmoneymsg
                    $ mny(-3)
                    $ wallet_lvl = 2
                    mc "(I think I can increase my pocket money budget to {color=#36ca2b}$8{/color}.)"
                "Don't upgrade your wallet":
                    hide screen newmoneymsg
        else:
            menu:
                "Upgrade wallet {color=#36ca2b}$$$$${/color}" if money > 4:
                    hide screen newmoneymsg
                    $ mny(-5)
                    $ wallet_lvl = 3
                    mc "(I think I can increase my pocket money budget to {color=#36ca2b}$10{/color}.)"
                    mc "(But this is it... I can't afford to increase my pocket money budget further.)"
                    if steamAchievements and not config.console and not config.developer:
                        $ achievement.grant("ID_27")
                        init:
                            $ achievement.register("ID_27")
                        $ achievement.Sync()
                "Don't upgrade your wallet":
                    hide screen newmoneymsg
    else:
        mc "(My wallet... I can't afford to increase my pocket money budget further than this.)"
    jump ep10_library_desk_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep10_library_desk_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep10_library_desk_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep10_library_desk_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep10_library_desk_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep10_library_desk_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep10_library_desk_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep10_library_desk_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep10_library_desk_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep10_library_desk_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep10_library_desk_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep10_library_desk_label
elif result == "frame":
    $ currentEvent = "ep10_choose_painting_label"
    jump startEvent
elif result == "study":
    mc "(Classes start again tomorrow... It's been nice to have some time off from them.)"
    jump ep10_library_desk_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk_label

label ep10_choose_painting_label:
image ep7_freeroam_diks_library_painting = "ep7_freeroam_diks_library_painting[ep7_current_desk_painting]"
if ep7_current_desk_painting > 0:
    scene ep7_freeroam_diks_library_painting
else:
    scene ep9_freeroam_diks_library_desk0

$ ui.imagebutton("phone_arrow_right", "phone_arrow_right_hover", clicked=ui.returns("right"), xalign=0.8, yalign=0.5)
$ ui.imagebutton("phone_arrow_left", "phone_arrow_left_hover", clicked=ui.returns("left"), xalign=0.23, yalign=0.5)
$ ui.imagebutton("english_ok", "english_ok_hover", clicked=ui.returns("ok"), xalign=0.98, yalign=0.98)

$ result = ui.interact()
if result == "right":
    $ ep7_current_desk_painting += 1
    if ep7_current_desk_painting > 16:
        $ ep7_current_desk_painting = 0
    else:
        $ ep7_current_desk_painting = desk_check_unlocked_2d(ep7_current_desk_painting, True)
    jump ep10_choose_painting_label
elif result == "left":
    if ep7_current_desk_painting == 0:
        $ ep7_current_desk_painting = 16
    else:
        $ ep7_current_desk_painting -= 1
    if ep7_current_desk_painting != 0:
        $ ep7_current_desk_painting = desk_check_unlocked_2d(ep7_current_desk_painting, False)
    jump ep10_choose_painting_label
else:
    $ currentFreeRoamLabel = "ep10_library_desk_label"
    jump endEvent

label ep10_choose_2nd_painting_label:
image ep8_2nd_painting = "ep8_second_painting[ep8_current_second_painting]"
if ep8_current_second_painting > 0:
    scene ep8_2nd_painting
else:
    scene ep9_2nd_painting0

$ ui.imagebutton("phone_arrow_right", "phone_arrow_right_hover", clicked=ui.returns("right"), xalign=0.9, yalign=0.5)
$ ui.imagebutton("phone_arrow_left", "phone_arrow_left_hover", clicked=ui.returns("left"), xalign=0.1, yalign=0.5)
$ ui.imagebutton("english_ok", "english_ok_hover", clicked=ui.returns("ok"), xalign=0.98, yalign=0.98)

$ result = ui.interact()
if result == "right":
    $ ep8_current_second_painting += 1
    if ep8_current_second_painting > 19:
        $ ep8_current_second_painting = 0
    else:
        $ ep8_current_second_painting = desk_check_second_unlocked_2d(ep8_current_second_painting, True)
    jump ep10_choose_2nd_painting_label
elif result == "left":
    if ep8_current_second_painting == 0:
        $ ep8_current_second_painting = 19
    else:
        $ ep8_current_second_painting -= 1
    if ep8_current_second_painting != 0:
        $ ep8_current_second_painting = desk_check_second_unlocked_2d(ep8_current_second_painting, False)
    jump ep10_choose_2nd_painting_label
else:
    $ currentFreeRoamLabel = "ep10_library_desk_label"
    jump endEvent

label ep10_diks_fr1_lib_right_label:
scene ep10_diks_fr1_lib_right with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_lib_right_label"

$ ui.imagebutton("ep10_diks_fr1_lib_right_camera_idle", "ep10_diks_fr1_lib_right_camera_hover", clicked=ui.returns("camera"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep10_diks_fr1_lib_mid_label
elif result == "go_down":
    jump ep10_diks_fr1_right_hall_label
elif result == "camera":
    mc "(I'll ask Elena and Jacob to help me remove the camera equipment later.)"
    jump ep10_diks_fr1_lib_right_label

label ep10_diks_fr1_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_main_label"

if "ep10_fr1_sage_event_label" in event_list:
    if not "ep10_fr1_josy_event_label" in event_list and ep9_jm_sad:
        if "ep10_fr1_clean1_event_label" in event_list:
            scene ep10_diks_fr1_main_noj with dissolve
        else:
            scene ep10_diks_fr1_mainb_noj with dissolve
    else:
        if "ep10_fr1_clean1_event_label" in event_list:
            scene ep10_diks_fr1_main with dissolve
        else:
            scene ep10_diks_fr1_mainb with dissolve
    $ ui.imagebutton("ep10_diks_fr1_main_stairs_idle", "ep10_diks_fr1_main_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
else:
    if not "ep10_fr1_josy_event_label" in event_list and ep9_jm_sad:
        if "ep10_fr1_clean1_event_label" in event_list:
            scene ep10_diks_fr1_maind_noj with dissolve
        else:
            scene ep10_diks_fr1_mainc_noj with dissolve
    else:
        if "ep10_fr1_clean1_event_label" in event_list:
            scene ep10_diks_fr1_maind with dissolve
        else:
            scene ep10_diks_fr1_mainc with dissolve
    $ ui.imagebutton("ep10_diks_fr1_main_stairs2_idle", "ep10_diks_fr1_main_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

if "ep10_fr1_jacob_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_main_jacob_idle", "ep10_diks_fr1_main_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_sage_event_label" in event_list and current_task == "Talk to Sage":
    $ ui.imagebutton("ep10_diks_fr1_main_sage_idle", "ep10_diks_fr1_main_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_josy_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_main_josy_idle", "ep10_diks_fr1_main_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_clean1_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_main_clean_idle", "ep10_diks_fr1_main_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)

if "ep10_fr1_clean1_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_main_doorb_idle", "ep10_diks_fr1_main_doorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep10_diks_fr1_main_door_idle", "ep10_diks_fr1_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_main_door2_idle", "ep10_diks_fr1_main_door2_hover", clicked=ui.returns("door2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)


$ result = ui.interact()
if result == "stairs":
    jump ep10_diks_fr1_mainup_label
elif result == "go_down":
    jump ep10_diks_fr1_right_hall_label
elif result == "door":
    jump ep10_diks_fr1_left_hall2_label
elif result == "door2":
    jump ep10_diks_fr1_outdoors_label
elif result == "jacob":
    $ currentEvent = "ep10_fr1_jacob_event_label"
    jump startEvent
elif result == "sage":
    $ currentEvent = "ep10_diks_end_event2_label"
    jump startEvent
    label ep10_diks_end_event2_label:
    menu:
        "End free roam":
            $ phone_clear_jump_label = "ep10_fr1_sage_event_label"
            jump end_freeroam
        "Not yet":
            $ renpy.pause(0.5)
    jump endEvent
elif result == "josy":
    $ currentEvent = "ep10_fr1_josy_event_label"
    jump startEvent
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean1_event_label"
    jump startEvent

label ep10_diks_fr1_mainup_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_mainup_label"
scene ep10_diks_fr1_mainup with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_mainup_ldoor_idle", "ep10_diks_fr1_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_mainup_rdoor_idle", "ep10_diks_fr1_mainup_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_sarah_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_mainup_sarah_idle", "ep10_diks_fr1_mainup_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_main_label
elif result == "room":
    jump ep10_diks_fr1_ua_label
elif result == "sarah":
    $ currentEvent = "ep10_fr1_sarah_event_label"
    jump startEvent
elif result == "leon":
    jump ep10_diks_fr1_leon_room_label

label ep10_diks_fr1_ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_ua_label"

if "ep10_fr1_nick_event_label" in event_list:
    scene ep10_diks_fr1_ua with dissolve
else:
    scene ep10_diks_fr1_uab with dissolve

if "ep10_fr1_nick_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_ua_nick_idle", "ep10_diks_fr1_ua_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)
elif ep8_help_nick:
    $ ui.imagebutton("ep10_diks_fr1_ua_fish_idle", "ep10_diks_fr1_ua_fish_hover", clicked=ui.returns("fish_tank"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1200 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=650 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_ua_ladder_idle", "ep10_diks_fr1_ua_ladder_hover", clicked=ui.returns("go_up2"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_mainup_label
elif result == "go_up":
    jump ep10_diks_fr1_1corr_label
elif result == "go_right":
    jump ep10_diks_fr1_2ua_label
elif result == "nick":
    $ currentEvent = "ep10_fr1_nick_event_label"
    jump startEvent
elif result == "go_up2":
    jump ep10_diks_fr1_roof_label
elif result == "fish_tank":
    if minigames:
        $ quick_menu = False
        hide screen new_phone_screen
        call screen fish_tank_screen
        $ renpy.pause(0.5)
        $ quick_menu = True
        show screen new_phone_screen
    else:
        scene ep10_fr1_nick_event8 with dissolve
        $ jumpLabel = "ep10_ft_nm_return1b_label"
        jump ep10_ft_nm_label
        label ep10_ft_nm_return1b_label:
    jump ep10_diks_fr1_ua_label


label ep10_diks_fr1_2ua_label:
if persistent.ep10_cardsa3:
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_diks_fr1_2ua with dissolve
    else:
        scene ep10_diks_fr1_2uab with dissolve
else:
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_diks_fr1_2ua_card with dissolve
    else:
        scene ep10_diks_fr1_2uab_card with dissolve
label ep10_diks_fr1_2ua_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_2ua_label"

if "ep10_fr1_maya_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_2ua_maya_idle", "ep10_diks_fr1_2ua_maya_hover", clicked=ui.returns("maya"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_mel_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_2ua_mel_idle", "ep10_diks_fr1_2ua_mel_hover", clicked=ui.returns("mel"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_clean2_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_2ua_clean_idle", "ep10_diks_fr1_2ua_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa3:
    $ ui.imagebutton("ep10_diks_fr1_2ua_card_idle", "ep10_diks_fr1_2ua_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_ua_label
elif result == "maya":
    $ currentEvent = "ep10_fr1_maya_event_label"
    jump startEvent
elif result == "mel":
    $ currentEvent = "ep10_fr1_mel_event_label"
    jump startEvent
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean2_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa3 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_diks_fr1_2ua with dissolve
    else:
        scene ep10_diks_fr1_2uab with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_diks_fr1_2ua_label_nofx
label ep10_diks_fr1_1corr_label:
$ renpy.block_rollback()
scene ep10_diks_fr1_1corr with dissolve
$ currentFreeRoamLabel = "ep10_diks_fr1_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_1corr_ldoor_idle", "ep10_diks_fr1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_1corr_rdoor_idle", "ep10_diks_fr1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_2corr_label
elif result == "go_up":
    jump ep10_diks_fr1_toilet_2nd_label
elif result == "janitor":
    jump ep10_diks_fr1_derek_label
elif result == "go_left":
    jump ep10_diks_fr1_ua_label

label ep10_diks_fr1_2corr_label:
$ renpy.block_rollback()
scene ep10_diks_fr1_2corr with dissolve
$ currentFreeRoamLabel = "ep10_diks_fr1_2corr_label"
$ ui.imagebutton("ep10_diks_fr1_2corr_door_idle", "ep10_diks_fr1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_1corr_label
elif result == "go_up":
    jump ep10_diks_fr1_jb_label
elif result == "go_right":
    jump ep10_diks_fr1_ua_label

label ep10_diks_fr1_derek_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_derek_label"
scene ep10_diks_fr1_derek with dissolve

$ ui.imagebutton("ep10_diks_fr1_derek_drinks_idle", "ep10_diks_fr1_derek_drinks_hover", clicked=ui.returns("drinks"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_1corr_label
elif result == "drinks":
    mc "(He came up with {color=00ff00}8{/color} different Halloween-themed drinks. I wonder how many of them tasted good.)"
    jump ep10_diks_fr1_derek_label

label ep10_diks_fr1_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_left_hall2_label"
if "ep10_fr1_lily_event_label" in event_list or not ep10_rolling:
    scene ep10_diks_fr1_left_hall2 with dissolve
    $ ui.imagebutton("ep10_diks_fr1_left_hall2_door_idle", "ep10_diks_fr1_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    scene ep10_diks_fr1_left_hall2b with dissolve
    $ ui.imagebutton("ep10_diks_fr1_left_hall2_door2_idle", "ep10_diks_fr1_left_hall2_door2_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

if "ep10_fr1_lily_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_left_hall2_lily_idle", "ep10_diks_fr1_left_hall2_lily_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_left_hall2_stairs_idle", "ep10_diks_fr1_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep10_diks_fr1_main_label
elif result == "go_up":
    jump ep10_diks_fr1_left_hall_label
elif result == "stairs":
    jump ep10_diks_fr1_tommy_label
elif result == "door":
    jump ep10_final_diks_porch_label
elif result == "lily":
    $ currentEvent = "ep10_fr1_lily_event_label"
    jump startEvent

label ep10_final_diks_porch_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_final_diks_porch_label"
if ep8_flower_water_level > 0:
    scene ep10_fr_porch with dissolve
else:
    scene ep10_fr_porchb with dissolve

if ep7_got_flower and "ep10_fr1_flower_dead_event_label" in event_list:
    $ ui.imagebutton("ep10_fr_porch_flowerb_idle", "ep10_fr_porch_flowerb_hover", clicked=ui.returns("flower"), xpos=0, ypos=0, focus_mask=True)
elif ep7_got_flower and "ep10_fr1_flower_event_label" in event_list:
    $ ui.imagebutton("ep10_fr_porch_flower_idle", "ep10_fr_porch_flower_hover", clicked=ui.returns("flower"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_left_hall2_label
elif result == "flower":
    if ep8_flower_water_level > 0:
        $ currentEvent = "ep10_fr1_flower_event_label"
        jump startEvent
    else:
        $ currentEvent = "ep10_fr1_flower_dead_event_label"
        jump startEvent

label ep10_diks_fr1_rusty_room_label:
if not found_money2:
    if persistent.ep10_cardsa4:
        scene ep10_diks_fr1_rusty_room_cash with dissolve
    else:
        scene ep10_diks_fr1_rusty_room_cash_card with dissolve
else:
    if persistent.ep10_cardsa4:
        scene ep10_diks_fr1_rusty_room with dissolve
    else:
        scene ep10_diks_fr1_rusty_room_card with dissolve
label ep10_diks_fr1_rusty_room_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_rusty_room_label"


if not found_money2:
    $ ui.imagebutton("ep10_diks_fr1_rusty_room_cash_idle", "ep10_diks_fr1_rusty_room_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_rusty_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_rusty_room_rusty_idle", "ep10_diks_fr1_rusty_room_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_rusty_room_door_idle", "ep10_diks_fr1_rusty_room_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa4:
    $ ui.imagebutton("ep10_diks_fr1_rusty_card_idle", "ep10_diks_fr1_rusty_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_left_hall_label
elif result == "rusty":
    $ currentEvent = "ep10_fr1_rusty_event_label"
    jump startEvent
elif result == "door":
    jump ep10_diks_fr1_dining_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa4 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if not found_money2:
        scene ep10_diks_fr1_rusty_room_cash with dissolve
    else:
        scene ep10_diks_fr1_rusty_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_diks_fr1_rusty_room_label_nofx
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    if persistent.ep10_cardsa4:
        scene ep10_diks_fr1_rusty_room with dissolve
    else:
        scene ep10_diks_fr1_rusty_room_card with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_diks_fr1_rusty_room_label_nofx

label ep10_diks_fr1_right_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_right_hall_label"
if "ep10_fr1_clean3_event_label" in event_list:
    scene ep10_diks_fr1_right_hall with dissolve
else:
    scene ep10_diks_fr1_right_hallb with dissolve

if "ep10_fr1_clean3_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_right_hall_clean_idle", "ep10_diks_fr1_right_hall_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_elena_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_right_hall_elena_idle", "ep10_diks_fr1_right_hall_elena_hover", clicked=ui.returns("elena"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_arieth_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_arieth_idle", "ep10_diks_fr1_arieth_hover", clicked=ui.returns("arieth"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_right_hall_kitchen_idle", "ep10_diks_fr1_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_right_hall_bathroom_idle", "ep10_diks_fr1_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_right_hall_theater_idle", "ep10_diks_fr1_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_right_hall_library_idle", "ep10_diks_fr1_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_main_label
elif result == "theater":
    jump ep10_diks_fr1_theater_label
elif result == "library":
    jump ep10_diks_fr1_lib_right_label
elif result == "kitchen":
    jump ep10_diks_fr1_kitchen_label
elif result == "bathroom":
    jump ep10_diks_fr1_bathroom_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean3_event_label"
    jump startEvent
elif result == "elena":
    $ currentEvent = "ep10_fr1_elena_event_label"
    jump startEvent
elif result == "arieth":
    $ currentEvent = "ep10_fr1_arieth_event_label"
    jump startEvent

label ep10_diks_fr1_theater_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_theater_label"
if "ep10_fr1_clean5_event_label" in event_list:
    scene ep10_diks_fr1_theater with dissolve
else:
    scene ep10_diks_fr1_theaterb with dissolve

if "ep10_fr1_derek_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_theater_derek_idle", "ep10_diks_fr1_theater_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
elif "ep10_fr1_derek_event2_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_theater_derek_idle", "ep10_diks_fr1_theater_derek_hover", clicked=ui.returns("derek2"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_clean5_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_theater_clean_idle", "ep10_diks_fr1_theater_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_right_hall_label
elif result == "derek":
    $ currentEvent = "ep10_fr1_derek_event_label"
    jump startEvent
elif result == "derek2":
    $ currentEvent = "ep10_fr1_derek_event2_label"
    jump startEvent
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean5_event_label"
    jump startEvent

label ep10_diks_fr1_leon_room_label:
if ep9_winner == "Leon":
    scene ep10_diks_fr1_leon_room with dissolve
else:
    scene ep10_diks_fr1_leon_roomb with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_leon_room_label"

if "ep10_fr1_leon_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_leon_idle", "ep10_diks_fr1_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=650 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_mainup_label
elif result == "leon":
    $ currentEvent = "ep10_fr1_leon_event_label"
    jump startEvent

label ep10_diks_fr1_toilet_2nd_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_toilet_2nd_label"
if "ep10_fr1_camera1_event_label" in event_list:
    $ currentEvent = "ep10_fr1_camera1_event_label"
    jump startEvent

if "ep10_fr1_clean7_event_label" in event_list:
    scene ep10_diks_fr1_toilet_2nd with dissolve
else:
    scene ep10_diks_fr1_toilet_2ndb with dissolve

if "ep10_fr1_clean7_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_toilet_2nd_clean_idle", "ep10_diks_fr1_toilet_2nd_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_1corr_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean7_event_label"
    jump startEvent

label ep10_diks_fr1_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_bathroom_label"

if "ep10_fr1_clean6_event_label" in event_list:
    scene ep10_diks_fr1_bathroom with dissolve
else:
    scene ep10_diks_fr1_bathroomb with dissolve
if "ep10_fr1_camera4_event_label" in event_list:
    $ currentEvent = "ep10_fr1_camera4_event_label"
    jump startEvent

if "ep10_fr1_clean6_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_bathroom_cl_idle", "ep10_diks_fr1_bathroom_cl_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_right_hall_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean6_event_label"
    jump startEvent

label ep10_diks_fr1_dining_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_dining_label"
scene ep10_diks_fr1_dining with dissolve

$ ui.imagebutton("ep10_diks_fr1_dining_stairs2_idle", "ep10_diks_fr1_dining_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_dining_rdoor_idle", "ep10_diks_fr1_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_dining_jdoor_idle", "ep10_diks_fr1_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep10_diks_fr1_kitchen_label
elif result == "stairs":
    jump ep10_diks_fr1_upper_2dining_label
elif result == "rusty":
    jump ep10_diks_fr1_rusty_room_label
elif result == "jamie":
    jump ep10_diks_fr1_jamie_label


label ep10_diks_fr1_upper_2dining_label:
$ renpy.block_rollback()
scene ep10_diks_fr1_upper_2dining with dissolve
$ currentFreeRoamLabel = "ep10_diks_fr1_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_upper_2dining_jacob_idle", "ep10_diks_fr1_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_upper_2dining_nick_idle", "ep10_diks_fr1_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_jb_label
elif result == "stairs":
    jump ep10_diks_fr1_dining_label
elif result == "nick":
    jump ep10_diks_fr1_nick_label
elif result == "jacob":
    jump ep10_diks_fr1_jacob_label

label ep10_diks_fr1_kitchen_label:
scene ep10_diks_fr1_kitchen with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_kitchen_label"

if "ep10_fr1_jb_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_kitchen_jb_idle", "ep10_diks_fr1_kitchen_jb_hover", clicked=ui.returns("jb"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_dining_label
elif result == "go_right":
    jump ep10_diks_fr1_right_hall_label
elif result == "jb":
    $ currentEvent = "ep10_fr1_jb_event_label"
    jump startEvent

label ep10_diks_fr1_jb_label:
if found_money:
    scene ep10_diks_fr1_jb with dissolve
else:
    scene ep10_diks_fr1_jb_cash with dissolve
label ep10_diks_fr1_jb_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_jb_label"

if not found_money:
    $ ui.imagebutton("ep10_diks_fr1_jb_cash_idle", "ep10_diks_fr1_jb_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_1corr_label
elif result == "go_up":
    jump ep10_diks_fr1_upper_2dining_label
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep10_diks_fr1_jb with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_diks_fr1_jb_label_nofx

label ep10_diks_fr1_nick_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_nick_label"
scene ep10_diks_fr1_nick with dissolve
if "ep10_fr1_camera2_event_label" in event_list:
    $ currentEvent = "ep10_fr1_camera2_event_label"
    jump startEvent

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep10_diks_fr1_upper_2dining_label

label ep10_diks_fr1_jacob_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_jacob_label"
if "ep10_fr1_clean8_event_label" in event_list:
    scene ep10_diks_fr1_jacob with dissolve
else:
    scene ep10_diks_fr1_jacobb with dissolve

if "ep10_fr1_camera5_event_label" in event_list:
    $ currentEvent = "ep10_fr1_camera5_event_label"
    jump startEvent
if "ep10_fr1_clean8_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_jacob_clean_idle", "ep10_diks_fr1_jacob_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_upper_2dining_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean8_event_label"
    jump startEvent


label ep10_diks_fr1_tommy_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_tommy_label"

if "ep10_fr1_clean4_event_label" in event_list:
    scene ep10_diks_fr1_tommy_room with dissolve
else:
    scene ep10_diks_fr1_tommy_roomb with dissolve

if "ep10_fr1_clean4_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_tommy_clean_idle", "ep10_diks_fr1_tommy_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_jamie_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_tommy_jamie_idle", "ep10_diks_fr1_tommy_jamie_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_tommy_curtain_idle", "ep10_diks_fr1_tommy_curtain_hover", clicked=ui.returns("curtain"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_left_hall2_label
elif result == "curtain":
    if branchMayaJosy:
        if "ep10_fr1_tommy_event_label" in event_list:
            $ currentEvent = "ep10_fr1_tommy_event_label"
            jump startEvent
        else:
            mc "(I should let him be for now.)"
            jump ep10_diks_fr1_tommy_label
    else:
        jump ep10_diks_fr1_tommy2_label
elif result == "jamie":
    $ currentEvent = "ep10_fr1_jamie_event_label"
    jump startEvent
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean4_event_label"
    jump startEvent

label ep10_diks_fr1_tommy2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_tommy2_label"
scene ep10_diks_fr1_tommy2 with dissolve

if "ep10_fr1_tommy_event2_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_tommy2_idle", "ep10_diks_fr1_tommy2_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_tommy_label
elif result == "tommy":
    $ currentEvent = "ep10_fr1_tommy_event2_label"
    jump startEvent

label ep10_diks_fr1_jamie_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_jamie_label"
if "ep10_fr1_camera3_event_label" in event_list:
    $ currentEvent = "ep10_fr1_camera3_event_label"
    jump startEvent
scene ep10_diks_fr1_jamie with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep10_diks_fr1_jamie_door_idle", "ep10_diks_fr1_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_left_hall_label
elif result == "door":
    jump ep10_diks_fr1_dining_label

label ep10_diks_fr1_roof_label:
if persistent.ep10_cardsa1:
    if "ep10_fr1_clean9_event_label" in event_list:
        scene ep10_diks_fr1_roof with dissolve
    else:
        scene ep10_diks_fr1_roofb with dissolve
else:
    if "ep10_fr1_clean9_event_label" in event_list:
        scene ep10_diks_fr1_roof_card with dissolve
    else:
        scene ep10_diks_fr1_roofb_card with dissolve
label ep10_diks_fr1_roof_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_roof_label"

if "ep10_fr1_clean9_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_roof_clean_idle", "ep10_diks_fr1_roof_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa1:
    $ ui.imagebutton("ep10_diks_fr1_roof_card_idle", "ep10_diks_fr1_roof_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep10_diks_fr1_ua_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean9_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa1 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep10_fr1_clean9_event_label" in event_list:
        scene ep10_diks_fr1_roof with dissolve
    else:
        scene ep10_diks_fr1_roofb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_diks_fr1_roof_label_nofx

label ep10_diks_fr1_outdoors_label:
if persistent.ep10_cardsa2:
    if "ep10_fr1_clean10_event_label" in event_list:
        scene ep10_diks_fr1_outdoorsb with dissolve
    else:
        scene ep10_diks_fr1_outdoors with dissolve
else:
    if "ep10_fr1_clean10_event_label" in event_list:
        scene ep10_diks_fr1_outdoorsb_card with dissolve
    else:
        scene ep10_diks_fr1_outdoors_card with dissolve

label ep10_diks_fr1_outdoors_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr1_outdoors_label"

if "ep10_fr1_clean10_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_outdoors_clean_idle", "ep10_diks_fr1_outdoors_clean_hover", clicked=ui.returns("clean"), xpos=0, ypos=0, focus_mask=True)
if "ep10_fr1_qc_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr1_outdoors_quinn_idle", "ep10_diks_fr1_outdoors_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep10_diks_fr1_outdoors_door_idle", "ep10_diks_fr1_outdoors_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep10_cardsa2:
    $ ui.imagebutton("ep10_diks_fr1_outdoors_card_idle", "ep10_diks_fr1_outdoors_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "door":
    jump ep10_diks_fr1_main_label
elif result == "clean":
    $ currentEvent = "ep10_fr1_clean10_event_label"
    jump startEvent
elif result == "quinn":
    $ currentEvent = "ep10_fr1_qc_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep10_cardsa2 = True
    $ persistent.rew_sage_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep10_fr1_clean10_event_label" in event_list:
        scene ep10_diks_fr1_outdoorsb with dissolve
    else:
        scene ep10_diks_fr1_outdoors with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep10_diks_fr1_outdoors_label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

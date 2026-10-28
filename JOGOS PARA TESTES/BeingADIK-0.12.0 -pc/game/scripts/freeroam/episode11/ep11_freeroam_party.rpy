label ep11_freeroam_party_label:
$ freeRoamID = "ep11_4"
$ roosterState = "ep11_4"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 194
$ found_money = False
$ found_money2 = False
$ bn_money_reward = True

$ disabled_apps = ["brawler"]
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True
$ ep11_gift_opp = 1

call mphone_check_pack_quest_available from _call_mphone_check_pack_quest_available_2
$ rooster_jump_label = "ep11_diks_pp_main_label"

$ map_system_list = []
$ map_system_list.append(["ep11_diks_fr2_lib_mid","ep11_diks4_fr2_lib_mid_label","Your room"])
$ map_system_list.append(["ep11_diks_pp_derek","ep11_diks_pp_derek_label","Derek's room"])
$ map_system_list.append(["ep11_diks_pp_dining","ep11_diks_pp_dining_label","Dining room"])
$ map_system_list.append(["ep11_diks_fr1_jacob_no_box","ep11_diks_pp_jacob_label","Jacob's room"])
$ map_system_list.append(["ep11_diks_pp_jamie","ep11_diks_pp_jamie_label","Jamie's room"])
$ map_system_list.append(["ep11_diks_pp_jb","ep11_diks_pp_jb_label","John Boy's room"])
$ map_system_list.append(["ep11_diks_fr1_left_hall","ep11_diks_pp_left_hall_label","Left hallway"])
$ map_system_list.append(["ep11_diks_pp_main","ep11_diks_pp_main_label","Main party room"])
$ map_system_list.append(["ep11_diks_party_nick","ep11_diks_pp_nick_label","Nick's room"])
$ map_system_list.append(["ep11_diks3_pp_right_hall","ep11_diks_pp_right_hall_label","Right hallway"])
$ map_system_list.append(["ep11_diks_pp_tommy_room","ep11_diks_pp_tommy_label","Tommy's room"])
$ map_system_list.append(["ep11_diks_pp_ua","ep11_diks_pp_ua_label","Upper main room"])

jump initRoosterLabel

label ep11_diks4_fr2_lib_mid_label:
if persistent.ep11_cardmy20:
    scene ep11_diks_fr2_lib_mid with dissolve
else:
    scene ep11_diks_fr2_lib_mid_card with dissolve
label ep11_diks4_fr2_lib_mid_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks4_fr2_lib_mid_label"

if not persistent.ep11_cardmy20:
    $ ui.imagebutton("ep11_diks_fr2_lib_mid_card_idle", "ep11_diks_fr2_lib_mid_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep11_diks4_fr2_lib_left_label
elif result == "go_right":
    jump ep11_diks4_fr2_lib_right_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy20 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_fr2_lib_mid with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks4_fr2_lib_mid_label_nofx

label ep11_diks4_fr2_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks4_fr2_lib_left_label"
scene ep11_diks_fr1_lib_left with dissolve

$ ui.imagebutton("ep11_diks_fr1_lib_desk_idle", "ep11_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep11_diks4_fr2_lib_mid_label
elif result == "desk":
    jump ep11_library_desk2c_label

label ep11_library_desk2c_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_library_desk2c_label"

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
if ep5_dikWinner and not "part2_arieth" in event_list:
    show ep7_dik_helmet_spr
if persistent.triple_tile_challenge:
    show ep7_triple_tile_spr
show ep7_phone_spr
show ep7_wallet_spr

if ep11_flowers:
    show spr_flowers

show spr_box_ep9
show ep8_gym_spr
show ep9_monkey_spr

if ep10_quinn_photo == 1:
    show ep10_quinn_spr1
elif ep10_quinn_photo == 2:
    show ep10_quinn_spr2

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
if ep8_help_nick:
    show ep10_fish_spr
show spr_cups
show spr_gifts
with dissolve

if ep10_quinn_photo == 1:
    $ ui.imagebutton("ep10_quinn_spr1", "ep10_quinn_spr1", clicked=ui.returns("quinn_spr1"), xpos=0, ypos=0, focus_mask=True)
elif ep10_quinn_photo == 2:
    $ ui.imagebutton("ep10_quinn_spr2", "ep10_quinn_spr2", clicked=ui.returns("quinn_spr2"), xpos=0, ypos=0, focus_mask=True)
if ep8_help_nick:
    $ ui.imagebutton("ep10_fish_spr", "ep10_fish_spr_hover", clicked=ui.returns("fish_tank"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_monkey_spr", "ep9_monkey_spr", clicked=ui.returns("monkey"), xpos=0, ypos=0, focus_mask=True)
if branchJill:
    $ ui.imagebutton("ep7_polaroid_jill_spr", "ep7_polaroid_jill_spr", clicked=ui.returns("polaroid"), xpos=0, ypos=0, focus_mask=True)
if ep6_fakeID:
    $ ui.imagebutton("ep7_fakeid_spr", "ep7_fakeid_spr", clicked=ui.returns("fakeid"), xpos=0, ypos=0, focus_mask=True)
if ep6_vipPass:
    $ ui.imagebutton("ep7_vip_spr", "ep7_vip_spr", clicked=ui.returns("vip"), xpos=0, ypos=0, focus_mask=True)
if ep5_dikWinner and not "part2_arieth" in event_list:
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

if ep11_flowers:
    $ ui.imagebutton("spr_flowers", "spr_flowers", clicked=ui.returns("flowers"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_sword", "spr_sword", clicked=ui.returns("sword"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_gifts", "spr_gifts", clicked=ui.returns("piggy"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_cups", "spr_cups", clicked=ui.returns("cups"), xpos=0, ypos=0, focus_mask=True)
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
    jump ep11_diks4_fr2_lib_left_label
elif result == "box":
    if pb_completed:
        mc "(That box was tricky to solve, but I did it. Even if it was empty, it made me feel smart and confident. That's something, I guess.)"
    else:
        mc "(I don't have time to play with that tonight.)"
    jump ep11_library_desk2c_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep11_library_desk2c_label
elif result == "cups":
    if ep10_pp_activity == 0:
        mc "(DIKs' Thanksgiving was fun. I think people enjoyed playing Beer Pong.)"
    else:
        mc "(DIKs' Thanksgiving was fun. I kinda regret not having Beer Pong at the party.)"
    jump ep11_library_desk2c_label
elif result  == "second_painting":
    $ currentEvent = "ep11_choose_2nd_paintingb_label"
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
    jump ep11_library_desk2c_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2c_label
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
    jump ep11_library_desk2c_label
elif result  == "piggy":
    call screen giftMsgScreen
    $ renpy.pause(0.5)
    jump ep11_library_desk2c_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep11_library_desk2c_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep11_library_desk2c_label
elif result  == "flowers":
    mc "(Yep... I made that happen. I'll do my best to keep them alive for long.)"
    jump ep11_library_desk2c_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep11_library_desk2c_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep11_library_desk2c_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep11_library_desk2c_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep11_library_desk2c_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep11_library_desk2c_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep11_library_desk2c_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep11_library_desk2c_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep11_library_desk2c_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep11_library_desk2c_label
elif result == "frame":
    $ currentEvent = "ep11_choose_paintingb_label"
    jump startEvent
elif result == "study":
    $ renpy.block_rollback()
    mc "(I'm not gonna study tonight.)"
    jump ep11_library_desk2c_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2c_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2c_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2c_label
elif result == "fish_tank":
    mc "(No need for that tonight. It's party time!)"
    jump ep11_library_desk2c_label


label ep11_diks4_fr2_lib_right_label:
if persistent.ep11_cardly15:
    scene ep11_diks4_fr2_lib_right with dissolve
else:
    scene ep11_diks4_fr2_lib_right_card with dissolve
label ep11_diks4_fr2_lib_right_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks4_fr2_lib_right_label"

if not persistent.ep11_cardly15:
    $ ui.imagebutton("ep11_diks4_fr2_lib_right_card_idle", "ep11_diks4_fr2_lib_right_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

if pack_quest_active and not pack_quest_list[0][1]:
    $ ui.imagebutton("ep11_packquest_btn0_idle", "ep11_packquest_btn0_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_left":
    jump ep11_diks4_fr2_lib_mid_label
elif result == "go_down":
    jump ep11_diks_pp_right_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly15 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks4_fr2_lib_right with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks4_fr2_lib_right_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[0][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_left_hall_label:
$ currentFreeRoamLabel = "ep11_diks_pp_left_hall_label"

scene ep11_diks_fr1_left_hall with dissolve

$ ui.imagebutton("ep11_diks_fr1_left_hall_jdoor_idle", "ep11_diks_fr1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_left_hall_rdoor_idle", "ep11_diks_fr1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_diks_pp_left_hall2_label
elif result == "jdoor":
    jump ep11_diks_pp_jamie_label
elif result == "rdoor":
    jump ep11_diks_pp_rusty_room_label

label ep11_diks_pp_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_main_label"
if "ep11_pp_lily_event_label" in event_list and not "ep11_pp_nl_event_label" in event_list:
    $ currentEvent = "ep11_pp_lily_event_label"
    jump startEvent
if "ep11_pp_kp_event_label" in event_list:
    $ currentEvent = "ep11_pp_kp_event_label"
    jump startEvent
if "part2" in event_list:
    if "ep11_pp_tara_event_label" in event_list:
        $ currentEvent = "ep11_pp_tara_event_label"
        jump startEvent
    if "part2_lily" in event_list:
        if ep11_invited_tara:
            scene ep11_diks_pp2b2_main with dissolve
        else:
            scene ep11_diks_pp2b_main with dissolve
    else:
        if ep11_invited_tara:
            scene ep11_diks_pp2c2_main with dissolve
        else:
            scene ep11_diks_pp2c_main with dissolve
else:
    scene ep11_diks_pp_main with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""

    $ chat_new_tasks = True
    
    if persistent.mod_wtenabled:
    
        $ task_list = ["","Talk to Rusty (Tommy's room)","Talk to Elena (Derek's room)","Talk to Tommy (Tommy's room)","Talk to Sally (Tommy's room)", "Talk to Derek (Main Party room)","Talk to Ashley (Upper Main Room)", "Talk to Zoey (Right Hallway)", "Talk to Bianca (Main Party room)","Talk to Quinn and Lily (Main Party room)", "Talk to Camila (Tommy's room)","Talk to the group of girls (Upper Main Room)"]


        $ optional_task_list = ["","", "Talk to Chen (Upper Main Room)", "Talk to Tiffani (Main Party room)", "Talk to Becky (Main Party room)", "Talk to red-headed girls (Theater)","Talk to Arieth (Main party room upstairs)"]
    
    else:
        $ task_list = ["","Talk to Rusty","Talk to Elena","Talk to Tommy","Talk to Sally", "Talk to Derek","Talk to Ashley", "Talk to Zoey", "Talk to Bianca","Talk to Quinn and Lily", "Talk to Camila","Talk to the group of girls"]


    $ optional_task_list = ["","", "Talk to Chen", "Talk to Tiffani", "Talk to Becky", "Talk to red-headed girls","Talk to Arieth"]
    if ep11_db_mission:
        $ optional_task_list[0] = "Dirty Bowl Mission 0/5"
    $ event_list = []
    $ event_list.append("ep11_pp_arieth_event_label")
    $ event_list.append("ep11_pp_rusty_event_label")
    $ event_list.append("ep11_pp_elena_event_label")
    $ event_list.append("ep11_pp_tommy_event_label")
    $ event_list.append("ep11_pp_sally_event_label")
    $ event_list.append("ep11_pp_derek_event_label")
    $ event_list.append("ep11_pp_girls_event_label")
    $ event_list.append("ep11_pp_chen_event_label")
    $ event_list.append("ep11_pp_ashley_event_label")
    $ event_list.append("ep11_pp_zoey_event_label")
    $ event_list.append("ep11_pp_bianca_event_label")
    $ event_list.append("ep11_pp_tiffani_event_label")
    $ event_list.append("ep11_pp_becky_event_label")
    $ event_list.append("ep11_pp_quinn_event_label")
    $ event_list.append("ep11_pp_th_event_label")
    $ event_list.append("ep11_pp_group_event_label")
    $ event_list.append("ep11_pp_camila_event_label")
    if ep11_db_mission:
        $ event_list.append("ep11_pp_santa_event_label")

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
    if "ep11_pp_zoey2_event_label" in event_list or current_task == "Talk to Zoey":
        if "part2_lily" in event_list:
            $ ui.imagebutton("ep11_diks_pp2b_main_zoey_idle", "ep11_diks_pp2b_main_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_diks_pp2_main_zoey_idle", "ep11_diks_pp2_main_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_tiffani_event_label" in event_list:
        if ep11_invited_tara:
            $ ui.imagebutton("ep11_diks_pp2b_main_tiff_idle", "ep11_diks_pp2b_main_tiff_hover", clicked=ui.returns("tiffani2"), xpos=0, ypos=0, focus_mask=True)
        else:
            $ ui.imagebutton("ep11_diks_pp2_main_tiff_idle", "ep11_diks_pp2_main_tiff_hover", clicked=ui.returns("tiffani2"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_ctease_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp2_main_camila_idle", "ep11_diks_pp2_main_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_tara_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp2_main_tara_idle", "ep11_diks_pp2_main_tara_hover", clicked=ui.returns("tara"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp2_main_stairs2_idle", "ep11_diks_pp2_main_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp2_main_door_idle", "ep11_diks_pp2_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep11_diks_pp_main_stairs2_idle", "ep11_diks_pp_main_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp_main_door_idle", "ep11_diks_pp_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_derek_event_label" in event_list or current_task == "Talk to Derek":
        $ ui.imagebutton("ep11_diks_pp_main_derek_idle", "ep11_diks_pp_main_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_becky_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_main_becky_idle", "ep11_diks_pp_main_becky_hover", clicked=ui.returns("becky"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_tiffani_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_main_tiffani_idle", "ep11_diks_pp_main_tiffani_hover", clicked=ui.returns("tiffani"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[8][1]:
    $ ui.imagebutton("ep11_packquest_btn8_idle", "ep11_packquest_btn8_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "stairs":
    jump ep11_diks_pp_mainup_label
elif result == "go_right":
    jump ep11_diks_pp_mainb_label
elif result == "derek":
    if "ep11_pp_derek_event_label" in event_list:
        $ currentEvent = "ep11_pp_derek_event_label"
    else:
        $ currentEvent = "ep11_pp_d_start_event_label"
    jump startEvent
elif result == "tiffani":
    $ currentEvent = "ep11_pp_tiffani_event_label"
    jump startEvent
elif result == "tara":
    $ currentEvent = "ep11_tara_event_label"
    jump startEvent
elif result == "camila":
    $ currentEvent = "ep11_pp_ctease_event_label"
    jump startEvent
elif result == "tiffani2":
    $ currentEvent = "ep11_tiffani_event_label"
    jump startEvent
elif result == "zoey":
    if ep11_mg_party:
        $ currentEvent = "ep11_diks_pp_main_end_label"
        jump startEvent
        label ep11_diks_pp_main_end_label:
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep11_pp_zoey2_event_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
        jump endEvent
    else:
        if "ep11_pp_zoey2_event_label" in event_list:
            $ currentEvent = "ep11_pp_zoey2_event_label"
        else:
            $ currentEvent = "ep11_diks_pp_main_end2_label"
            jump startEvent
            label ep11_diks_pp_main_end2_label:
            menu:
                "End free roam":
                    $ phone_clear_jump_label = "ep11_pp_zoey_end_label"
                    jump end_freeroam
                "Not yet":
                    $ renpy.pause(0.5)
            jump endEvent
    jump startEvent
elif result == "becky":
    $ currentEvent = "ep11_pp_becky_event_label"
    jump startEvent
elif result == "door":
    jump ep11_diks_pp_left_hall2_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[8][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_mainb_label:
if "part2" in event_list:
    if not "part2_elena" in event_list and not "ep11_pp_elena_lewd_event_label" in event_list:
        if persistent.ep11_cardly19:
            scene ep11_diks_pp2_main with dissolve
        else:
            scene ep11_diks_pp2_main_card with dissolve
    else:
        if persistent.ep11_cardly19:
            scene ep11_diks_pp2_mainb with dissolve
        else:
            scene ep11_diks_pp2_mainb_card with dissolve
else:
    if "ep11_pp_quinn_event_label" in event_list:
        if persistent.ep11_cardly19:
            scene ep11_diks_pp_mainb with dissolve
        else:
            scene ep11_diks_pp_mainb_card with dissolve
    else:
        if persistent.ep11_cardly19:
            scene ep11_diks_pp_mainb2 with dissolve
        else:
            scene ep11_diks_pp_mainb2_card with dissolve
label ep11_diks_pp_mainb_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_mainb_label"

if "part2" in event_list:
    if "ep11_pp_nl_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp2_main_nic_idle", "ep11_diks_pp2_main_nic_hover", clicked=ui.returns("nicole"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep11_pp_bianca_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_main_bianca_idle", "ep11_diks_pp_main_bianca_hover", clicked=ui.returns("bianca"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_quinn_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_main_quinn_idle", "ep11_diks_pp_main_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
if "ep11_pp_santa_event_label" in event_list and ep11_db_mission_progress < 5:
    $ ui.imagebutton("ep11_diks_pp_main_santa_idle", "ep11_diks_pp_main_santa_hover", clicked=ui.returns("santa"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep11_cardly19:
    $ ui.imagebutton("ep11_diks_pp_mainb_card_idle", "ep11_diks_pp_mainb_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_left":
    jump ep11_diks_pp_main_label
elif result == "go_down":
    jump ep11_diks_pp_right_hall_label
elif result == "quinn":
    $ currentEvent = "ep11_pp_quinn_event_label"
    jump startEvent
elif result == "bianca":
    $ currentEvent = "ep11_pp_bianca_event_label"
    jump startEvent
elif result == "nicole":
    $ currentEvent = "ep11_pp_nl_event_label"
    jump startEvent
elif result == "santa":
    $ currentEvent = "ep11_pp_santa_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly19 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        if not "part2_elena" in event_list and not "ep11_pp_elena_lewd_event_label" in event_list:
            scene ep11_diks_pp2_main with dissolve
        else:
            scene ep11_diks_pp2_mainb with dissolve
    else:
        if "ep11_pp_quinn_event_label" in event_list:
            scene ep11_diks_pp_mainb with dissolve
        else:
            scene ep11_diks_pp_mainb2 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_mainb_label_nofx

label ep11_diks_pp_mainup_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_mainup_label"
if "part2" in event_list:
    scene ep11_diks_pp2b_mainup with dissolve
else:
    scene ep11_diks_pp_mainup with dissolve

if "part2" in event_list:
    $ ui.imagebutton("ep11_diks_pp2_mainup_ldoor_idle", "ep11_diks_pp2_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep11_diks_pp_mainup_ldoor_idle", "ep11_diks_pp_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_arieth_event_label" in event_list or "ep11_pp_dildo_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_mainup_arieth_idle", "ep11_diks_pp_mainup_arieth_hover", clicked=ui.returns("arieth"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_mainup_rdoor_idle", "ep11_diks_pp_mainup_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_main_label
elif result == "room":
    jump ep11_diks_pp_ua_label
elif result == "arieth":
    if "ep11_pp_arieth_event_label" in event_list:
        $ currentEvent = "ep11_pp_arieth_event_label"
    else:
        $ currentEvent = "ep11_pp_dildo_event_label"
    jump startEvent
elif result == "leon":
    jump ep11_diks_pp_leon_room_label

label ep11_diks_pp_ua_label:
if "part2" in event_list:
    if "ep11_pp_dm_event_label" in event_list:
        $ renpy.block_rollback()
        $ currentFreeRoamLabel = "ep11_diks_pp_ua_label"
        $ currentEvent = "ep11_pp_dm_event_label"
        jump startEvent
    if persistent.ep11_cardmy17:
        scene ep11_diks_pp2_ua with dissolve
    else:
        scene ep11_diks_pp2_ua_card with dissolve
else:
    if persistent.ep11_cardmy17:
        scene ep11_diks_pp_ua with dissolve
    else:
        scene ep11_diks_pp_ua_card with dissolve
label ep11_diks_pp_ua_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_ua_label"

if "part2" in event_list and pack_quest_active and not pack_quest_list[6][1]:
    $ ui.imagebutton("ep11_packquest_btn6_idle", "ep11_packquest_btn6_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep11_cardmy17:
    $ ui.imagebutton("ep11_diks_pp_ua_card_idle", "ep11_diks_pp_ua_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1600 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=800 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

if not "part2" in event_list:
    if "ep11_pp_girls_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_ua_girl_idle", "ep11_diks_pp_ua_girl_hover", clicked=ui.returns("girl"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_mainup_label
elif result == "go_up":
    jump ep11_diks_pp_1corr_label
elif result == "go_right":
    jump ep11_diks_pp_2ua_label
elif result == "girl":
    $ currentEvent = "ep11_pp_girls_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy17 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep11_diks_pp2_ua with dissolve
    else:
        scene ep11_diks_pp_ua with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_ua_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[6][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_2ua_label:
if not "part2" in event_list and not "ep11_pp_chen_event_label" in event_list and not "ep11_pp_drink1_event_label" in event_list and not "ep11_pp_drink2_event_label" in event_list and "ep11_pp_mt_event_label" in event_list:
    $ map_fast_travel_enabled = False
if "part2" in event_list:
    if not "part2_elena" in event_list and not "ep11_pp_elena_lewd_event_label" in event_list:
        scene ep11_diks_pp2_2ua with dissolve
    else:
        scene ep11_diks_pp2b_2ua with dissolve
else:
    if "ep11_pp_chen_event_label" in event_list:
        scene ep11_diks_pp_2ua with dissolve
    elif "ep11_pp_drink1_event_label" in event_list or "ep11_pp_drink2_event_label" in event_list or "ep11_pp_drink_skip_event_label" in event_list:
        scene ep11_diks_pp_2uab with dissolve
    else:
        if ep11_mistletoe == 0:
            scene ep11_diks_pp_2uac with dissolve
        else:
            scene ep11_diks_pp_2uacb with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_2ua_label"

if "part2" in event_list:
    if "ep11_pp_elena1_event_label" in event_list or "ep11_pp_elena2_event_label" in event_list or "ep11_pp_elena3_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_2ua_elena_idle", "ep11_diks_pp_2ua_elena_hover", clicked=ui.returns("elena"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_sk_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_2ua_sally_idle", "ep11_diks_pp_2ua_sally_hover", clicked=ui.returns("sally"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep11_pp_chen_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_2ua_chen_idle", "ep11_diks_pp_2ua_chen_hover", clicked=ui.returns("chen"), xpos=0, ypos=0, focus_mask=True)
    elif "ep11_pp_drink2_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_2ua_girl_idle", "ep11_diks_pp_2ua_girl_hover", clicked=ui.returns("girl"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_ashley_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_2ua_ashley_idle", "ep11_diks_pp_2ua_ashley_hover", clicked=ui.returns("ashley"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    if not "part2" in event_list and not "ep11_pp_chen_event_label" in event_list and not "ep11_pp_drink1_event_label" in event_list and not "ep11_pp_drink2_event_label" in event_list and "ep11_pp_mt_event_label" in event_list:
        $ currentEvent = "ep11_pp_mt_event_label"
        jump startEvent
    jump ep11_diks_pp_ua_label
elif result == "chen":
    $ currentEvent = "ep11_pp_chen_event_label"
    jump startEvent
elif result == "sally":
    $ currentEvent = "ep11_pp_sk_event_label"
    jump startEvent
elif result == "ashley":
    $ currentEvent = "ep11_pp_ashley_event_label"
    jump startEvent
elif result == "girl":
    $ currentEvent = "ep11_pp_drink2_event_label"
    jump startEvent
elif result == "elena":
    if "ep11_pp_elena1_event_label" in event_list:
        $ currentEvent = "ep11_pp_elena1_event_label"
    elif "ep11_pp_elena2_event_label" in event_list:
        $ currentEvent = "ep11_pp_elena2_event_label"
    else:
        $ currentEvent = "ep11_pp_elena3_event_label"
    jump startEvent

label ep11_diks_pp_1corr_label:
$ renpy.block_rollback()
scene ep11_diks_fr1_1corr with dissolve
$ currentFreeRoamLabel = "ep11_diks_pp_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_1corr_ldoor_idle", "ep11_diks_fr1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_1corr_rdoor_idle", "ep11_diks_fr1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_2corr_label
elif result == "go_up":
    jump ep11_diks_pp_toilet_2nd_label
elif result == "janitor":
    jump ep11_diks_pp_derek_label
elif result == "go_left":
    jump ep11_diks_pp_ua_label

label ep11_diks_pp_2corr_label:
$ renpy.block_rollback()
scene ep11_diks_fr1_2corr with dissolve
$ currentFreeRoamLabel = "ep11_diks_pp_2corr_label"
$ ui.imagebutton("ep11_diks_fr1_2corr_door_idle", "ep11_diks_fr1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_1corr_label
elif result == "go_up":
    jump ep11_diks_pp_jb_label
elif result == "go_right":
    jump ep11_diks_pp_ua_label

label ep11_diks_pp_derek_label:
if "part2" in event_list:
    if persistent.ep11_cardmy18:
        scene ep11_diks_pp2_derek with dissolve
    else:
        scene ep11_diks_pp2_derek_card with dissolve
else:
    if persistent.ep11_cardmy18:
        scene ep11_diks_pp_derek with dissolve
    else:
        scene ep11_diks_pp_derek_card with dissolve
label ep11_diks_pp_derek_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_derek_label"

if not persistent.ep11_cardmy18:
    $ ui.imagebutton("ep11_diks_pp_derek_card_idle", "ep11_diks_pp_derek_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if not "part2" in event_list:
    if "ep11_pp_elena_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_derek_elena_idle", "ep11_diks_pp_derek_elena_hover", clicked=ui.returns("elena"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_1corr_label
elif result == "elena":
    $ currentEvent = "ep11_pp_elena_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy18 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep11_diks_pp2_derek with dissolve
    else:
        scene ep11_diks_pp_derek with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_derek_label_nofx

label ep11_diks_pp_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_left_hall2_label"
if "part2" in event_list:
    if "part2_arieth" in event_list:
        scene ep11_diks_pp2_left_hall2
        hide screen dance_filter_screen
        with dissolve
    else:
        scene ep11_diks_pp2_left_hall2b
        hide screen dance_filter_screen
        with dissolve
else:
    scene ep11_diks_pp_left_hall2
    hide screen dance_filter_screen
    with dissolve

if "part2" in event_list:
    if "part2_arieth" in event_list:
        $ ui.imagebutton("ep11_diks_pp2_left_hall2_door_idle", "ep11_diks_pp2_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
        $ ui.imagebutton("ep11_diks_pp_left_hall2_stairs_idle", "ep11_diks_pp_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep11_diks_pp2_left_hall2b_door_idle", "ep11_diks_pp2_left_hall2b_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
        $ ui.imagebutton("ep11_diks_pp2_left_hall2_stairs_idle", "ep11_diks_pp2_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep11_diks_pp_left_hall2_door_idle", "ep11_diks_pp_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp_left_hall2_stairs_idle", "ep11_diks_pp_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_group_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_left_hall2_grp_idle", "ep11_diks_pp_left_hall2_grp_hover", clicked=ui.returns("group"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep11_diks_pp_main_label
elif result == "go_up":
    jump ep11_diks_pp_left_hall_label
elif result == "group":
    $ currentEvent = "ep11_pp_group_event_label"
    jump startEvent
elif result == "stairs":
    jump ep11_diks_pp_tommy_label
elif result == "door":
    jump ep11_diks_pp_porch_label

label ep11_diks_pp_porch_label:
if found_money2:
    scene ep11_fr_porch with dissolve
else:
    scene ep11_fr_porch_cash with dissolve
label ep11_diks_pp_porch_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_porch_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[2][1]:
    $ ui.imagebutton("ep11_packquest_btn2_idle", "ep11_packquest_btn2_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
if not found_money2:
    $ ui.imagebutton("ep11_fr_porch_cash_idle", "ep11_fr_porch_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_left_hall2_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[2][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep11_fr_porch with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_diks_pp_porch_label_nofx

label ep11_diks_pp_rusty_room_label:
if persistent.ep11_cardly20:
    scene ep11_diks_pp_rusty_room with dissolve
else:
    scene ep11_diks_pp_rusty_room_card with dissolve
label ep11_diks_pp_rusty_room_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_rusty_room_label"

if not persistent.ep11_cardly20:
    $ ui.imagebutton("ep11_diks_pp_rusty_room_card_idle", "ep11_diks_pp_rusty_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_rusty_room_door_idle", "ep11_diks_pp_rusty_room_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_left_hall_label
elif result == "door":
    jump ep11_diks_pp_dining_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly20 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_pp_rusty_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_rusty_room_label_nofx

label ep11_diks_pp_right_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_right_hall_label"
if "ep11_becky_event_label" in event_list:
    $ currentEvent = "ep11_becky_event_label"
    jump startEvent
if "part2" in event_list:
    scene ep11_diks3_pp2_right_hall with dissolve
else:
    scene ep11_diks3_pp_right_hall with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if "part2" in event_list:
    $ ui.imagebutton("ep11_diks_pp2_right_hall_kitchen_idle", "ep11_diks_pp2_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp2_right_hall_bathroom_idle", "ep11_diks_pp2_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp2_right_hall_theater_idle", "ep11_diks_pp2_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_dleave_event_label" in event_list or "ep11_pp_ad_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_right_hall_derek_idle", "ep11_diks_pp_right_hall_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep11_diks_pp_right_hall_kitchen_idle", "ep11_diks_pp_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp_right_hall_bathroom_idle", "ep11_diks_pp_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)
    $ ui.imagebutton("ep11_diks_pp_right_hall_theater_idle", "ep11_diks_pp_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_zoey_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_right_hall_zoey_idle", "ep11_diks_pp_right_hall_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep11_diks_pp_right_hall_library_idle", "ep11_diks_pp_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_right_hall_table_idle", "ep11_diks_pp_right_hall_table_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_mainb_label
elif result == "theater":
    jump ep11_diks_pp_theater_label
elif result == "library":
    jump ep11_diks4_fr2_lib_right_label
elif result == "table":
    jump ep11_diks3_fr2_table_label
elif result == "zoey":
    $ currentEvent = "ep11_pp_zoey_event_label"
    jump startEvent
elif result == "derek":
    if ep11_mg_party:
        $ currentEvent = "ep11_pp_dleave_event_label"
    else:
        $ currentEvent = "ep11_pp_ad_event_label"
    jump startEvent
elif result == "kitchen":
    jump ep11_diks_pp_kitchen_label
elif result == "bathroom":
    jump ep11_diks_pp_bathroom_label

label ep11_diks3_fr2_table_label:
$ renpy.block_rollback()
if "part2" in event_list:
    if "ep11_pp_mt2_event_label" in event_list:
        $ currentEvent = "ep11_pp_mt2_event_label"
        jump startEvent

scene ep11_diks3_fr2_table with dissolve
$ currentFreeRoamLabel = "ep11_diks3_fr2_table_label"

if "ep11_pp_drink1_event_label" in event_list:
    $ ui.imagebutton("ep11_diks3_fr2_punch_idle", "ep11_diks3_fr2_punch_hover", clicked=ui.returns("punch"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks3_fr2_cookies_idle", "ep11_diks3_fr2_cookies_hover", clicked=ui.returns("cookies"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks3_fr2_table_idle", "ep11_diks3_fr2_table_idle", clicked=ui.returns("go_down"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("arrow"), xpos=0, ypos=840 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[7][1]:
    $ ui.imagebutton("ep11_packquest_btn7_idle", "ep11_packquest_btn7_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "arrow":
    jump ep11_diks_pp_right_hall_label
elif result == "go_down":
    jump ep11_diks_pp_hall_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[7][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "cookies":
    mc "({color=00ff00}5{/color} stacks of cookies on all plates. Hm... It doesn't seem like people are eating a lot of them at this party. Probably because they're in their underwear and don't want to feel bloated.)"
    jump ep11_diks3_fr2_table_label
elif result == "punch":
    $ currentEvent = "ep11_pp_drink1_event_label"
    jump startEvent

label ep11_diks_pp_theater_label:
if "part2" in event_list:
    if "ep11_pp_quinn2_event_label" in event_list:
        if persistent.ep11_cardly16:
            scene ep11_diks_pp2_theaterq with dissolve
        else:
            scene ep11_diks_pp2_theaterq_card with dissolve
    else:
        if persistent.ep11_cardly16:
            scene ep11_diks_pp2_theater with dissolve
        else:
            scene ep11_diks_pp2_theater_card with dissolve
else:
    if persistent.ep11_cardly16:
        scene ep11_diks_pp_theater with dissolve
    else:
        scene ep11_diks_pp_theater_card with dissolve
label ep11_diks_pp_theater_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_theater_label"

if not persistent.ep11_cardly16:
    $ ui.imagebutton("ep11_diks_pp_theater_card_idle", "ep11_diks_pp_theater_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "part2" in event_list:
    if "ep11_pp_quinn2_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_theater_quinn_idle", "ep11_diks_pp_theater_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep11_pp_th_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_theater_girls_idle", "ep11_diks_pp_theater_girls_hover", clicked=ui.returns("girls"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_right_hall_label
elif result == "girls":
    $ currentEvent = "ep11_pp_th_event_label"
    jump startEvent
elif result == "quinn":
    $ currentEvent = "ep11_pp_quinn2_event_label"
    stop music fadeout 3
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly16 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2" in event_list:
        scene ep11_diks_pp2_theater with dissolve
    else:
        scene ep11_diks_pp_theater with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_theater_label_nofx

label ep11_diks_pp_leon_room_label:
if persistent.ep11_cardmy16:
    scene ep11_diks_pp_leon_room with dissolve
else:
    scene ep11_diks_pp_leon_room_card with dissolve
label ep11_diks_pp_leon_room_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_leon_room_label"

if not persistent.ep11_cardmy16:
    $ ui.imagebutton("ep11_diks_pp_leon_room_card_idle", "ep11_diks_pp_leon_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=650 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_mainup_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy16 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_pp_leon_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_leon_room_label_nofx

label ep11_diks_pp_toilet_2nd_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_toilet_2nd_label"

scene ep11_diks_pp_toilet_2nd with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[3][1]:
    $ ui.imagebutton("ep11_packquest_btn3_idle", "ep11_packquest_btn3_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_1corr_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[3][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_bathroom_label"

scene ep11_diks_party_bathroom with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[1][1]:
    $ ui.imagebutton("ep11_packquest_btn1_idle", "ep11_packquest_btn1_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_right_hall_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[1][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_dining_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_dining_label"
scene ep11_diks_pp_dining with dissolve

$ ui.imagebutton("ep11_diks_pp_dining_stairs2_idle", "ep11_diks_pp_dining_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_pp_dining_rdoor_idle", "ep11_diks_pp_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_dining_jdoor_idle", "ep11_diks_pp_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep11_diks_pp_kitchen_label
elif result == "stairs":
    jump ep11_diks_pp_upper_2dining_label
elif result == "rusty":
    jump ep11_diks_pp_rusty_room_label
elif result == "jamie":
    jump ep11_diks_pp_jamie_label


label ep11_diks_pp_upper_2dining_label:
$ renpy.block_rollback()
scene ep11_diks_pp_upper_2dining with dissolve
$ currentFreeRoamLabel = "ep11_diks_pp_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_pp_upper_2dining_jacob_idle", "ep11_diks_pp_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_upper_2dining_nick_idle", "ep11_diks_pp_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_jb_label
elif result == "stairs":
    jump ep11_diks_pp_dining_label
elif result == "nick":
    jump ep11_diks_pp_nick_label
elif result == "jacob":
    jump ep11_diks_pp_jacob_label

label ep11_diks_pp_kitchen_label:
if persistent.ep11_cardmy19:
    scene ep11_diks_pp_kitchen with dissolve
else:
    scene ep11_diks_pp_kitchen_card with dissolve
label ep11_diks_pp_kitchen_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_kitchen_label"

if not persistent.ep11_cardmy19:
    $ ui.imagebutton("ep11_diks_pp_kitchen_card_idle", "ep11_diks_pp_kitchen_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_dining_label
elif result == "go_right":
    jump ep11_diks_pp_right_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy19 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_pp_kitchen with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_kitchen_label_nofx

label ep11_diks_pp_jb_label:
if "ep11_pp_elena_lewd_event_label" in event_list:
    $ currentFreeRoamLabel = "ep11_diks_pp_jb_label"
    $ currentEvent = "ep11_pp_elena_lewd_event_label"
    jump startEvent

if "part2_elena" in event_list:
    if persistent.ep11_cardly18:
        scene ep11_diks_pp2_jb with dissolve
    else:
        scene ep11_diks_pp2_jb_card with dissolve
else:
    if persistent.ep11_cardly18:
        scene ep11_diks_pp_jb with dissolve
    else:
        scene ep11_diks_pp_jb_card with dissolve
label ep11_diks_pp_jb_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_jb_label"

if not persistent.ep11_cardly18:
    $ ui.imagebutton("ep11_diks_pp_jb_card_idle", "ep11_diks_pp_jb_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)
if pack_quest_active and not pack_quest_list[4][1]:
    $ ui.imagebutton("ep11_packquest_btn4_idle", "ep11_packquest_btn4_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_pp_jb_tree_idle", "ep11_diks_pp_jb_tree_hover", clicked=ui.returns("tree"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_1corr_label
elif result == "go_up":
    jump ep11_diks_pp_upper_2dining_label
elif result == "tree":
    mc "(That tree has {color=00ff00}8{/color} red balls on it. Ironically, I think there are more blue balls than that at this party, haha.)"
    jump ep11_diks_pp_jb_label_nofx
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[4][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly18 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "part2_elena" in event_list:
        scene ep11_diks_pp2_jb with dissolve
    else:
        scene ep11_diks_pp_jb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_jb_label_nofx

label ep11_diks_pp_nick_label:
if found_money:
    scene ep11_diks_party_nick with dissolve
else:
    scene ep11_diks_party_nick_cash with dissolve
label ep11_diks_pp_nick_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_nick_label"

if not found_money:
    $ ui.imagebutton("ep11_diks_party_nick_cash_idle", "ep11_diks_party_nick_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_diks_pp_upper_2dining_label
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep11_diks_party_nick with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_diks_pp_nick_label_nofx

label ep11_diks_pp_jacob_label:
if persistent.ep11_cardly17:
    scene ep11_diks_fr1_jacob_no_box with dissolve
else:
    scene ep11_diks_fr1_jacob_no_box_card with dissolve
label ep11_diks_pp_jacob_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_jacob_label"

if not persistent.ep11_cardly17:
    $ ui.imagebutton("ep11_diks_fr1_jacob_no_box_card_idle", "ep11_diks_fr1_jacob_no_box_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_upper_2dining_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardly17 = True
    $ persistent.rew_lily_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_fr1_jacob_no_box with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_pp_jacob_label_nofx

label ep11_diks_pp_tommy_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_tommy_label"
if "part2" in event_list:
    if current_task == "Go to Tommy's room":
        show screen dance_filter_screen
        $ currentEvent = "ep11_pp_act2_event_label"
        jump startEvent
    if "part2_kp" in event_list:
        scene ep11_diks_pp2b_tommy_room
        show screen dance_filter_screen
        with dissolve
    else:
        scene ep11_diks_pp2_tommy_room
        show screen dance_filter_screen
        with dissolve
else:
    if "ep11_pp_tommy_event_label" in event_list:
        scene ep11_diks_pp_tommy_room
        show screen dance_filter_screen
        with dissolve
    else:
        scene ep11_diks_pp_tommyb_room
        show screen dance_filter_screen
        with dissolve

if "part2" in event_list:
    if "ep11_pp_leon_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_leon_idle", "ep11_diks_pp_tommy_room_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_st_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_st_idle", "ep11_diks_pp_tommy_room_st_hover", clicked=ui.returns("st"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_bia_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_bia_idle", "ep11_diks_pp_tommy_room_bia_hover", clicked=ui.returns("bianca"), xpos=0, ypos=0, focus_mask=True)
else:
    if "ep11_pp_tommy_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_tommy_idle", "ep11_diks_pp_tommy_room_tommy_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_camila_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_camila_idle", "ep11_diks_pp_tommy_room_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_rusty_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_rusty_idle", "ep11_diks_pp_tommy_room_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
    if "ep11_pp_sally_event_label" in event_list:
        $ ui.imagebutton("ep11_diks_pp_tommy_room_sally_idle", "ep11_diks_pp_tommy_room_sally_hover", clicked=ui.returns("sally"), xpos=0, ypos=0, focus_mask=True)

if pack_quest_active and not pack_quest_list[9][1]:
    $ ui.imagebutton("ep11_packquest_btn9_idle", "ep11_packquest_btn9_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_left_hall2_label
elif result == "tommy":
    $ currentEvent = "ep11_pp_tommy_event_label"
    jump startEvent
elif result == "bianca":
    $ currentEvent = "ep11_pp_bia_event_label"
    jump startEvent
elif result == "st":
    $ currentEvent = "ep11_pp_st_event_label"
    jump startEvent
elif result == "leon":
    $ currentEvent = "ep11_pp_leon_event_label"
    jump startEvent
elif result == "sally":
    $ currentEvent = "ep11_pp_sally_event_label"
    jump startEvent
elif result == "camila":
    $ currentEvent = "ep11_pp_camila_event_label"
    jump startEvent
elif result == "rusty":
    $ currentEvent = "ep11_pp_rusty_event_label"
    jump startEvent
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[9][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)

label ep11_diks_pp_jamie_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_pp_jamie_label"
scene ep11_diks_pp_jamie with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_pp_jamie_door_idle", "ep11_diks_pp_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if pack_quest_active and not pack_quest_list[5][1]:
    $ ui.imagebutton("ep11_packquest_btn5_idle", "ep11_packquest_btn5_hover", clicked=ui.returns("pq"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_pp_left_hall_label
elif result == "door":
    jump ep11_diks_pp_dining_label
elif result == "pq":
    show screen packquest_button_found
    $ pack_quest_list[5][1] = True
    $ renpy.pause(3)
    $ renpy.jump(currentFreeRoamLabel)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

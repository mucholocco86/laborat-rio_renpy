label ep11_freeroam_diks_label:
$ freeRoamID = "ep11_2"
$ roosterState = "ep11_2"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 167
$ found_money = False
$ found_money2 = False
$ studied = False
$ tmpBool = False

if minigames:
    $ new_phone_call("Magnar","ep11_magnar_shop")

$ new_chat_msg("Sally",True,1)
$ new_chat_msg("Zoey",True,4)

$ disabled_apps = ["brawler","music"]
$ firstTimeFreeRoam = True
$ game_money_available = True
$ ep11_gift_opp = 2

$ triple_tile_money_available = True

if ep8_help_nick:
    $ jumpLabel = "ft_setup_round5_label"
    $ ft_round+= 1
    if minigames:
        label ft_round5_label:
        jump ft_setup_round_label
    else:
        $ ft_nm_new_round()
    label ft_setup_round5_label:

$ rooster_jump_label = "ep11_diks3_fr2_lib_mid_label"

$ map_system_list = []
$ map_system_list.append(["ep11_diks_fr2_lib_mid","ep11_diks3_fr2_lib_mid_label","Your room"])
$ map_system_list.append(["ep11_diks_fr1_derek","ep11_diks_fr1_derek_label","Derek's room"])
$ map_system_list.append(["ep11_diks_fr1_dining","ep11_diks_fr1_dining_label","Dining room"])
$ map_system_list.append(["ep11_hots_fr1_lobby","ep11_hots_fr1_lobby_label","HOTs' hallway"])
$ map_system_list.append(["ep11_diks_fr1_jacob","ep11_diks_fr1_jacob_label","Jacob's room"])
$ map_system_list.append(["ep11_diks_fr1_jamie","ep11_diks_fr1_jamie_label","Jamie's room"])
$ map_system_list.append(["ep11_diks_fr1_jb","ep11_diks_fr1_jb_label","John Boy's room"])
$ map_system_list.append(["ep11_diks_fr1_left_hall2","ep11_diks_fr1_left_hall2_label","Left hallway"])
$ map_system_list.append(["ep11_diks_fr1_mainb","ep11_diks_fr1_main_label","Main party room"])
$ map_system_list.append(["ep11_diks_party_nick","ep11_diks_fr1_nick_label","Nick's room"])
$ map_system_list.append(["ep11_diks_fr1_outdoors","ep11_diks_fr1_outdoors_label","Outside"])
$ map_system_list.append(["ep11_diks3_fr1_right_hall","ep11_diks_fr1_right_hall_label","Right hallway"])
$ map_system_list.append(["ep11_diks_fr1_tommy_room","ep11_diks_fr1_tommy_label","Tommy's room"])
$ map_system_list.append(["ep11_diks_fr1_ua","ep11_diks_fr1_ua_label","Upper main room"])

jump initRoosterLabel

label ep11_diks3_fr2_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks3_fr2_lib_mid_label"
scene ep11_diks_fr2_lib_mid with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    
    if persistent.mod_wtenabled:
    
        $ task_list = ["Talk to Melanie (Main Party Room)","","","","Talk to Rusty (Rusty's room)","","Talk to Sage (HOTS upstairs room)","","Find Derek (Upper Main Room)","","Talk to Camila (HOTS Camila's room)"]
        $ optional_task_list = ["","","","Talk to Leon (Right Hallway)","Talk to John Boy (HOTS upstairs)","","Help Sarah (HOTS upstairs room)","","","","Talk to Arieth (HOTS upstairs room)"]
    else:
        $ task_list = ["Talk to Melanie","","","","Talk to Rusty","","Talk to Sage","","Find Derek","","Talk to Camila"]
        $ optional_task_list = ["","","","Talk to Leon","Talk to John Boy","","Help Sarah","","","","Talk to Arieth"]

    $ chat_new_tasks = True
    $ event_list = []

    $ event_list.append("ep11_fr_deco_mem_event_label")
    $ event_list.append("ep11_fr_deco_sage_event_label")
    $ event_list.append("ep11_fr_deco_camila_event_label")
    $ event_list.append("ep11_fr_deco_ari_event_label")
    $ event_list.append("ep11_fr_deco_ari2_event_label")
    if branchJill:
        if persistent.mod_wtenabled:
            $ task_list[2] = "Talk to Jill (Main Party room)"
        else:
            $ task_list[2] = "Talk to Jill"
        $ event_list.append("ep11_fr_deco_ji_event_label")
    if branchAlone and ep8_quinn_lewd:
        if persistent.mod_wtenabled:
            $ task_list[9] = "Talk to Quinn (HOTS house)"
        else:
            $ task_list[9] = "Talk to Quinn"
            
    else:
        if persistent.mod_wtenabled:
            $ optional_task_list[9] = "Talk to Quinn (HOTS house)"
        else:
            $ optional_task_list[9] = "Talk to Quinn"
            

    $ event_list.append("ep11_fr_deco_q_event_label")

    if ep8_flower_water_level == 2:
        $ event_list.append("ep11_fr_deco_flower_event_label")
        $ optional_task_list[7] = "Check on your flowers"

    $ event_list.append("ep11_fr_deco_da_event_label")
    $ event_list.append("ep11_fr_deco_lc_event_label")
    $ event_list.append("ep11_fr_deco_rm_event_label")
    $ event_list.append("ep11_fr_deco_jb_event_label")
    $ event_list.append("ep11_fr_deco_sarah_event_label")

    if ep8_help_nick:
        $ optional_task_list[0] = "Take care of your fish"

    if minigames:
        $ optional_task_list[1] = "Study at your desk"
    if not pb_completed:
        $ optional_task_list[2] = "Solve the puzzle box"

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
    jump ep11_diks3_fr2_lib_left_label
elif result == "go_right":
    jump ep11_diks3_fr2_lib_right_label

label ep11_diks3_fr2_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks3_fr2_lib_left_label"
scene ep11_diks_fr1_lib_left with dissolve

$ ui.imagebutton("ep11_diks_fr1_lib_desk_idle", "ep11_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep11_diks3_fr2_lib_mid_label
elif result == "desk":
    jump ep11_library_desk2b_label

label ep11_library_desk2b_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_library_desk2b_label"

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

if ep10_quinn_photo == 1:
    show ep10_quinn_spr1
elif ep10_quinn_photo == 2:
    show ep10_quinn_spr2

if ep11_flowers:
    show spr_flowers

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
if ep5_dikWinner:
    $ ui.imagebutton("ep7_dik_helmet_spr", "ep7_dik_helmet_spr", clicked=ui.returns("helmet"), xpos=0, ypos=0, focus_mask=True)
if persistent.triple_tile_challenge:
    $ ui.imagebutton("ep7_triple_tile_spr", "ep7_triple_tile_spr", clicked=ui.returns("triple_tile"), xpos=0, ypos=0, focus_mask=True)
if ep11_flowers:
    $ ui.imagebutton("spr_flowers", "spr_flowers", clicked=ui.returns("flowers"), xpos=0, ypos=0, focus_mask=True)

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
    jump ep11_diks3_fr2_lib_left_label
elif result == "box":
    if pb_completed:
        mc "(That box was tricky to solve, but I did it. Even if it was empty, it made me feel smart and confident. That's something, I guess.)"
    else:
        $ qM = quick_menu
        $ quick_menu = 0
        hide screen new_phone_screen
        call screen puzzle_box_screen
        $ renpy.pause(0.5)
        if pb_completed:
            scene ep11_pb_done1b with dissolve
            if not persistent.ep11_cardmy13 or not persistent.ep11_cardmy14:
                if not persistent.ep11_cardmy14:
                    $ persistent.rew_maya_unlocked += 1
                    $ persistent.ep11_cardmy14 = True
                $ persistent.chat_new_rewards = True
                $ persistent.rew_maya_unlocked += 1
                $ persistent.ep11_cardmy13 = True
                $ calcRenders()
                show screen srmsg
                $ renpy.pause(3)
                hide screen srmsg
            if steamAchievements and not config.console and not config.developer:
                $ achievement.grant("IDS3_31")
                init:
                    $ achievement.register("IDS3_31")
            mc "(I did it! That's crazy. What a fun puzzle.)"
            scene ep11_pb_done2b with dissolve
            mc "(Um... Is there supposed to be something in here?)"
            mc "(It's empty... Damn. It felt like I had stumbled on a treasure box for a while.)"
            mc "(Oh, well... It was fun while it lasted. But all that for nothing...)"
            $ optional_task_list[2] = ""
            $ updateTaskList()
        show screen new_phone_screen
        $ quick_menu = qM
    jump ep11_library_desk2b_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep11_library_desk2b_label
elif result == "cups":
    if ep10_pp_activity == 0:
        mc "(DIKs' Thanksgiving was fun. I think people enjoyed playing Beer Pong.)"
    else:
        mc "(DIKs' Thanksgiving was fun. I kinda regret not having Beer Pong at the party.)"
    jump ep11_library_desk2b_label
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
    jump ep11_library_desk2b_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2b_label
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
    jump ep11_library_desk2b_label
elif result  == "piggy":
    call screen giftMsgScreen
    $ renpy.pause(0.5)
    jump ep11_library_desk2b_label
elif result  == "flowers":
    mc "(Yep... I made that happen. I'll do my best to keep them alive for long.)"
    jump ep11_library_desk2b_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep11_library_desk2b_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep11_library_desk2b_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep11_library_desk2b_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep11_library_desk2b_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep11_library_desk2b_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep11_library_desk2b_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep11_library_desk2b_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep11_library_desk2b_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep11_library_desk2b_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep11_library_desk2b_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep11_library_desk2b_label
elif result == "frame":
    $ currentEvent = "ep11_choose_paintingb_label"
    jump startEvent
elif result == "study":
    $ renpy.block_rollback()
    if minigames:
        if studied:
            mc "(I've studied enough for today.)"
        else:
            hide screen new_phone_screen
            $ studied = True
            $ optional_task_list[1] = ""
            $ updateTaskList()
            menu:
                "(What should I study?)"
                "Study English":
                    $ bonusPercentageEnglish += 10
                    "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
                "Study Math":
                    $ bonusPercentageMath += 10
                    "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
                "Study Science":
                    $ sm_studied += 1
                    $ tmpInt = sm_studied*5
                    "+5%% time on your next lab experiment.\nYour total bonus time for the next experiment is [tmpInt]%%."
                    $ tmpInt = 0
            mc "(That will do for now.)"
            show screen new_phone_screen
    else:
        mc "(I'm not gonna study today.)"
    jump ep11_library_desk2b_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2b_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2b_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2b_label
elif result == "fish_tank":
    if optional_task_list[0] != "":
        $ optional_task_list[0] = ""
        $ updateTaskList()
    if minigames:
        $ quick_menu = False
        hide screen new_phone_screen
        call screen fish_tank_screen
        $ renpy.pause(0.5)
        $ quick_menu = True
        show screen new_phone_screen
    else:
        if ft_fish_nm == 0:
            $ fish_label = "ep11_ft_nm_return5_label"
            jump nm_dead_fish_label
        else:
            scene ep11_fish1 with dissolve
            $ jumpLabel = "ep11_ft_nm_return5_label"
            jump ep10_ft_nm_label
            label ep11_ft_nm_return5_label:
    jump ep11_library_desk2b_label

label ep11_diks3_fr2_lib_right_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks3_fr2_lib_right_label"

scene ep11_diks3_fr2_lib_right with dissolve

if current_task == "Plan the party on your couch":
    $ ui.imagebutton("ep11_diks3_fr2_lib_sofa_idle", "ep11_diks3_fr2_lib_sofa_hover", clicked=ui.returns("sofa"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep11_diks3_fr2_lib_mid_label
elif result == "go_down":
    jump ep11_diks_fr1_right_hall_label
elif result == "sofa":
    $ currentEvent = "ep11_freeroam1b_room_end_label"
    jump startEvent
    label ep11_freeroam1b_room_end_label:
    if current_task == "Plan the party on your couch":
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep11_fr_deco_pp_event_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(I still have things to do.)"
    jump endEvent

label ep11_diks_fr1_left_hall_label:
$ currentFreeRoamLabel = "ep11_diks_fr1_left_hall_label"

if renpy.random.randint(0, 10) > 5 or tmpBool:
    scene ep11_diks_fr1_left_hall with dissolve
else:
    $ tmpBool = True
    scene ep11_diks_fr1_left_hallb with dissolve
label ep11_diks_fr1_left_hall_label_nofx:

$ ui.imagebutton("ep11_diks_fr1_left_hall_jdoor_idle", "ep11_diks_fr1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_left_hall_rdoor_idle", "ep11_diks_fr1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_diks_fr1_left_hall2_label
elif result == "jdoor":
    jump ep11_diks_fr1_jamie_label
elif result == "rdoor":
    if not "ep11_fr_deco_rm_event_label" in event_list:
        mc "(I'll let them be alone doing whatever they feel like doing in there.)"
        jump ep11_diks_fr1_left_hall_label_nofx
    else:
        jump ep11_diks_fr1_rusty_room_label

label ep11_diks_fr1_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_main_label"

if "ep11_fr_deco_nic_event_label" in event_list:
    $ currentEvent = "ep11_fr_deco_nic_event_label"
    jump startEvent

if "ep11_fr_deco_tj_event_label" in event_list:
    if branchJill:
        scene ep11_diks_fr1_main with dissolve
    else:
        scene ep11_diks_fr1_mainb with dissolve
else:
    if branchJill:
        scene ep11_diks_fr1_mainc with dissolve
    else:
        scene ep11_diks_fr1_maind with dissolve

$ ui.imagebutton("ep11_diks_fr1_main_stairs2_idle", "ep11_diks_fr1_main_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

if "ep11_fr_deco_mem_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_main_mel_idle", "ep11_diks_fr1_main_mel_hover", clicked=ui.returns("mel"), xpos=0, ypos=0, focus_mask=True)
elif "ep11_fr_mel_lewd_event_label" in event_list and (task_list[0] == "Talk to Melanie" or task_list[0] == "Talk to Melanie (Main Party Room)"):
    $ ui.imagebutton("ep11_diks_fr1_main_mel_idle", "ep11_diks_fr1_main_mel_hover", clicked=ui.returns("mel2"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_ji_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_main_jill_idle", "ep11_diks_fr1_main_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_tj_event_label" in event_list:
    if branchJill:
        $ ui.imagebutton("ep11_diks_fr1_main_tj2_idle", "ep11_diks_fr1_main_tj2_hover", clicked=ui.returns("tj"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep11_diks_fr1_main_tj2b_idle", "ep11_diks_fr1_main_tj2b_hover", clicked=ui.returns("tj"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep11_diks_fr1_main_door_idle", "ep11_diks_fr1_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_main_door2_idle", "ep11_diks_fr1_main_door2_hover", clicked=ui.returns("door2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)


$ result = ui.interact()
if result == "stairs":
    jump ep11_diks_fr1_mainup_label
elif result == "mel":
    $ currentEvent = "ep11_fr_deco_mem_event_label"
    jump startEvent
elif result == "mel2":
    $ currentEvent = "ep11_fr_mel_lewd_event_label"
    jump startEvent
elif result == "jill":
    $ currentEvent = "ep11_fr_deco_ji_event_label"
    jump startEvent
elif result == "tj":
    $ currentEvent = "ep11_fr_deco_tj_event_label"
    jump startEvent
elif result == "go_down":
    jump ep11_diks_fr1_right_hall_label
elif result == "door":
    jump ep11_diks_fr1_left_hall2_label
elif result == "door2":
    jump ep11_diks_fr1_outdoors_label

label ep11_diks_fr1_mainup_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_mainup_label"
scene ep11_diks_fr1_mainup with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_mainup_ldoor_idle", "ep11_diks_fr1_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_main_label
elif result == "room":
    jump ep11_diks_fr1_ua_label

label ep11_diks_fr1_ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_ua_label"

scene ep11_diks_fr1_ua with dissolve

if ep8_help_nick:
    $ ui.imagebutton("ep11_diks_fr1_ua_fish_idle", "ep11_diks_fr1_ua_fish_hover", clicked=ui.returns("fish_tank"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1200 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=650 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_mainup_label
elif result == "go_up":
    jump ep11_diks_fr1_1corr_label
elif result == "go_right":
    jump ep11_diks_fr1_2ua_label
elif result == "fish_tank":
    if optional_task_list[0] != "":
        $ optional_task_list[0] = ""
        $ updateTaskList()
    if minigames:
        $ quick_menu = False
        hide screen new_phone_screen
        call screen fish_tank_screen
        $ renpy.pause(0.5)
        $ quick_menu = True
        show screen new_phone_screen
    else:
        if ft_fish_nm == 0:
            $ fish_label = "ep11_ft_nm_return1b_label"
            jump nm_dead_fish_label
        else:
            scene ep10_fr1_nick_event8 with dissolve
            $ jumpLabel = "ep11_ft_nm_return1b_label"
            jump ep10_ft_nm_label
            label ep11_ft_nm_return1b_label:
    jump ep11_diks_fr1_ua_label


label ep11_diks_fr1_2ua_label:
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
if persistent.ep11_cardmy1:
    scene ep11_diks_fr1_2ua with dissolve
else:
    scene ep11_diks_fr1_2ua_card with dissolve
label ep11_diks_fr1_2ua_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_2ua_label"

if not persistent.ep11_cardmy1:
    $ ui.imagebutton("ep11_diks_fr1_2ua_card_idle", "ep11_diks_fr1_2ua_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_da_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_2ua_derek_idle", "ep11_diks_fr1_2ua_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    jump ep11_diks_fr1_ua_label
elif result == "derek":
    $ currentEvent = "ep11_fr_deco_da_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep11_cardmy1 = True
    $ persistent.rew_maya_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep11_diks_fr1_2ua with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep11_diks_fr1_2ua_label_nofx

label ep11_diks_fr1_1corr_label:
$ renpy.block_rollback()
scene ep11_diks_fr1_1corr with dissolve
$ currentFreeRoamLabel = "ep11_diks_fr1_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_1corr_ldoor_idle", "ep11_diks_fr1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_1corr_rdoor_idle", "ep11_diks_fr1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_2corr_label
elif result == "go_up":
    jump ep11_diks_fr1_toilet_2nd_label
elif result == "janitor":
    jump ep11_diks_fr1_derek_label
elif result == "go_left":
    jump ep11_diks_fr1_ua_label

label ep11_diks_fr1_2corr_label:
$ renpy.block_rollback()
scene ep11_diks_fr1_2corr with dissolve
$ currentFreeRoamLabel = "ep11_diks_fr1_2corr_label"
$ ui.imagebutton("ep11_diks_fr1_2corr_door_idle", "ep11_diks_fr1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_1corr_label
elif result == "go_up":
    jump ep11_diks_fr1_jb_label
elif result == "go_right":
    jump ep11_diks_fr1_ua_label

label ep11_diks_fr1_derek_label:
if found_money2:
    scene ep11_diks_fr1_derek with dissolve
else:
    scene ep11_diks_fr1_derek_cash with dissolve
label ep11_diks_fr1_derek_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_derek_label"

if not found_money2:
    $ ui.imagebutton("ep11_diks_fr1_derek_cash_idle", "ep11_diks_fr1_derek_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_derek_deer_idle", "ep11_diks_fr1_derek_deer_hover", clicked=ui.returns("deer"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_1corr_label
elif result == "deer":
    mc "(Ah, yes. Rudolph the red-nosed moose... Derek is such an ass.)"
    jump ep11_diks_fr1_derek_label
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep11_diks_fr1_derek with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_diks_fr1_derek_label_nofx

label ep11_diks_fr1_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_left_hall2_label"
if "ep11_fr_deco_mem_event_label" in event_list or "ep11_fr_deco_box1_event_label" in event_list:
    scene ep11_diks_fr1_left_hall2 with dissolve
else:
    scene ep11_diks_fr1_left_hall2_no_box with dissolve

$ ui.imagebutton("ep11_diks_fr1_left_hall2_door_idle", "ep11_diks_fr1_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_left_hall2_stairs_idle", "ep11_diks_fr1_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
if not "ep11_fr_deco_mem_event_label" in event_list and "ep11_fr_deco_box1_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_left_hall2_box_idle", "ep11_diks_fr1_left_hall2_box_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep11_diks_fr1_main_label
elif result == "go_up":
    jump ep11_diks_fr1_left_hall_label
elif result == "stairs":
    jump ep11_diks_fr1_tommy_label
elif result == "box":
    $ currentEvent = "ep11_fr_deco_box1_event_label"
    jump startEvent
elif result == "door":
    jump ep11_final_diks_porch_label

label ep11_final_diks_porch_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_final_diks_porch_label"
if "ep11_fr_deco_flower_event_label" in event_list:
    $ currentEvent = "ep11_fr_deco_flower_event_label"
    jump startEvent
scene ep11_fr_porch with dissolve
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_left_hall2_label

label ep11_diks_fr1_rusty_room_label:
$ renpy.block_rollback()
if "ep11_fr_deco_rm_event_label" in event_list:
    $ currentFreeRoamLabel = "ep11_diks_fr1_left_hall2_label"
    $ currentEvent = "ep11_fr_deco_rm_event_label"
    jump startEvent
else:
    mc "(I'll let them be alone in there doing whatever they feel like doing.)"
    $ renpy.jump(currentFreeRoamLabel)


label ep11_diks_fr1_right_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_right_hall_label"
scene ep11_diks3_fr1_right_hall with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if "ep11_fr_deco_lc_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_right_hall_leon_idle", "ep11_diks_fr1_right_hall_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_right_hall_kitchen_idle", "ep11_diks_fr1_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_right_hall_bathroom_idle", "ep11_diks_fr1_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_right_hall_theater_idle", "ep11_diks_fr1_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_right_hall_library_idle", "ep11_diks_fr1_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_main_label
elif result == "leon":
    $ currentEvent = "ep11_fr_deco_lc_event_label"
    jump startEvent
elif result == "theater":
    jump ep11_diks_fr1_theater_label
elif result == "library":
    jump ep11_diks3_fr2_lib_right_label
elif result == "kitchen":
    jump ep11_diks_fr1_kitchen_label
elif result == "bathroom":
    jump ep11_diks_fr1_bathroom_label

label ep11_diks_fr1_theater_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_theater_label"
scene ep11_diks_fr1_theater with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_right_hall_label

label ep11_diks_fr1_leon_room_label:
scene ep11_diks_fr1_leon_room with dissolve

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_leon_room_label"

$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=650 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_mainup_label

label ep11_diks_fr1_toilet_2nd_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_toilet_2nd_label"

scene ep11_diks_fr1_toilet_2nd with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_1corr_label

label ep11_diks_fr1_bathroom_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_bathroom_label"

scene ep11_diks_party_bathroom with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_right_hall_label

label ep11_diks_fr1_dining_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_dining_label"
if "ep11_fr_deco_mem_event_label" in event_list or "ep11_fr_deco_box2_event_label" in event_list:
    scene ep11_diks_fr1_dining with dissolve
else:
    scene ep11_diks_fr1_dining_no_box with dissolve

$ ui.imagebutton("ep11_diks_fr1_dining_stairs2_idle", "ep11_diks_fr1_dining_stairs2_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_dining_rdoor_idle", "ep11_diks_fr1_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_dining_jdoor_idle", "ep11_diks_fr1_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep11_diks_fr1_kitchen_label
elif result == "stairs":
    jump ep11_diks_fr1_upper_2dining_label
elif result == "rusty":
    jump ep11_diks_fr1_rusty_room_label
elif result == "jamie":
    jump ep11_diks_fr1_jamie_label


label ep11_diks_fr1_upper_2dining_label:
$ renpy.block_rollback()
scene ep11_diks_fr1_upper_2dining with dissolve
$ currentFreeRoamLabel = "ep11_diks_fr1_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_upper_2dining_jacob_idle", "ep11_diks_fr1_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_upper_2dining_nick_idle", "ep11_diks_fr1_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_jb_label
elif result == "stairs":
    jump ep11_diks_fr1_dining_label
elif result == "nick":
    jump ep11_diks_fr1_nick_label
elif result == "jacob":
    jump ep11_diks_fr1_jacob_label

label ep11_diks_fr1_kitchen_label:
if "ep11_fr_deco_mem_event_label" in event_list or "ep11_fr_deco_box2_event_label" in event_list:
    scene ep11_diks_fr1_kitchen with dissolve
else:
    scene ep11_diks_fr1_kitchen_no_box with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_kitchen_label"

if not "ep11_fr_deco_mem_event_label" in event_list and "ep11_fr_deco_box2_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_kitchen_box_idle", "ep11_diks_fr1_kitchen_box_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_dining_label
elif result == "go_right":
    jump ep11_diks_fr1_right_hall_label
elif result == "box":
    $ currentEvent = "ep11_fr_deco_box2_event_label"
    jump startEvent

label ep11_diks_fr1_jb_label:
scene ep11_diks_fr1_jb with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_jb_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_1corr_label
elif result == "go_up":
    jump ep11_diks_fr1_upper_2dining_label

label ep11_diks_fr1_nick_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_nick_label"
scene ep11_diks_party_nick with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_diks_fr1_upper_2dining_label

label ep11_diks_fr1_jacob_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_jacob_label"
if "ep11_fr_deco_mem_event_label" in event_list or "ep11_fr_deco_box3_event_label" in event_list:
    scene ep11_diks_fr1_jacob with dissolve
else:
    scene ep11_diks_fr1_jacob_no_box with dissolve

if not "ep11_fr_deco_mem_event_label" in event_list and "ep11_fr_deco_box3_event_label" in event_list:
    $ ui.imagebutton("ep11_diks_fr1_jacob_box_idle", "ep11_diks_fr1_jacob_box_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks_fr1_jacob_sheet_idle", "ep11_diks_fr1_jacob_sheet_hover", clicked=ui.returns("sheet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_upper_2dining_label
elif result == "sheet":
    mc "(I'm sure it's covered up for a reason...)"
    jump ep11_diks_fr1_jacob_label
elif result == "box":
    $ currentEvent = "ep11_fr_deco_box3_event_label"
    jump startEvent

label ep11_diks_fr1_tommy_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_tommy_label"

scene ep11_diks_fr1_tommy_room with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_left_hall2_label

label ep11_diks_fr1_jamie_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_jamie_label"
scene ep11_diks_fr1_jamie with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_jamie_door_idle", "ep11_diks_fr1_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep11_diks_fr1_left_hall_label
elif result == "door":
    jump ep11_diks_fr1_dining_label

label ep11_diks_fr1_outdoors_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks_fr1_outdoors_label"
scene ep11_diks_fr1_outdoors with dissolve

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep11_diks_fr1_outdoors_door_idle", "ep11_diks_fr1_outdoors_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "door":
    jump ep11_diks_fr1_main_label
elif result == "go_left":
    jump ep11_hots_fr1_lobby_label

label ep11_hots_fr1_lobby_label:
if found_money:
    scene ep11_hots_fr1_lobby with dissolve
else:
    scene ep11_hots_fr1_lobby_cash with dissolve
label ep11_hots_fr1_lobby_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_hots_fr1_lobby_label"

if not found_money:
    $ ui.imagebutton("ep11_hots_fr1_lobby_cash_idle", "ep11_hots_fr1_lobby_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_hots_fr1_lobby_door_idle", "ep11_hots_fr1_lobby_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=550 * persistent.scale_factor, ypos=430 * persistent.scale_factor)

$ result = ui.interact()

if result == "stairs":
    jump ep11_hots_fr1_upper_label
elif result == "door":
    jump ep11_diks_fr1_outdoors_label
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep11_hots_fr1_lobby with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_hots_fr1_lobby_label_nofx

label ep11_hots_fr1_upper_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_hots_fr1_upper_label"
if "ep11_fr_deco_box_event_label" in event_list:
    $ currentEvent = "ep11_fr_deco_box_event_label"
    jump startEvent

if "ep11_fr_deco_mem_event_label" in event_list or "ep11_fr_deco_box3_event_label" in event_list or "ep11_fr_deco_box2_event_label" in event_list or "ep11_fr_deco_box1_event_label" in event_list:
    scene ep11_hots_fr1_upper_no_boxes with dissolve
else:
    scene ep11_hots_fr1_upper with dissolve

if "ep11_fr_deco_jb_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_upper_jb_idle", "ep11_hots_fr1_upper_jb_hover", clicked=ui.returns("jb"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1120 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_hots_fr1_lobby_label
elif result == "jb":
    $ currentEvent = "ep11_fr_deco_jb_event_label"
    jump startEvent
elif result == "go_up":
    jump ep11_hots_fr1_upper2_label


label ep11_hots_fr1_upper2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_hots_fr1_upper2_label"

if "ep11_fr_deco_ari_event_label" in event_list:
    scene ep11_hots_fr2_upper with dissolve
else:
    scene ep11_hots_fr2_upperb with dissolve
if "ep11_fr_deco_q_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_upper3_quinn_idle", "ep11_hots_fr1_upper3_quinn_hover", clicked=ui.returns("quinn"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep11_hots_fr1_upper2_ldoor_idle", "ep11_hots_fr1_upper2_ldoor_hover", clicked=ui.returns("door_left"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=850 * persistent.scale_factor, ypos=420 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_up":
    jump ep11_hots_fr1_upper3_label
elif result == "quinn":
    $ currentEvent = "ep11_fr_deco_q_event_label"
    jump startEvent
elif result == "door_left":
    jump ep11_hots_fr1_el_label
elif result == "go_down":
    jump ep11_hots_fr1_upper_label

label ep11_hots_fr1_el_label:
$ renpy.block_rollback()

$ currentFreeRoamLabel = "ep11_hots_fr1_el_label"
scene ep11_hots_fr1_el with dissolve

$ ui.imagebutton("ep11_hots_fr1_el_boxes_idle", "ep11_hots_fr1_el_boxes_hover", clicked=ui.returns("boxes"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_hots_fr1_upper2_label
elif result == "boxes":
    mc "(I wonder what's inside those {color=00ff00}2{/color} boxes...)"
    jump ep11_hots_fr1_el_label

label ep11_hots_fr1_upper3_label:
$ renpy.block_rollback()

$ currentFreeRoamLabel = "ep11_hots_fr1_upper3_label"

if "ep11_fr_deco_ari_event_label" in event_list:
    scene ep11_hots_fr1_upper3 with dissolve
else:
    scene ep11_hots_fr1_upper3b with dissolve
    if "ep11_fr_deco_josy_event_label" in event_list:
        $ ui.imagebutton("ep11_hots_fr1_upper2_josy_idle", "ep11_hots_fr1_upper2_josy_hover", clicked=ui.returns("josy"), xpos=0, ypos=0, focus_mask=True)


if "ep11_fr_deco_ari_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_upper3_cdoor_idle", "ep11_hots_fr1_upper3_cdoor_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep11_hots_fr1_upper3_cdoorb_idle", "ep11_hots_fr1_upper3_cdoorb_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_hots_fr1_upper3_rdoor_idle", "ep11_hots_fr1_upper3_rdoor_hover", clicked=ui.returns("door_right"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "door":
    jump ep11_hots_fr1_lr_label
elif result == "josy":
    $ currentEvent = "ep11_fr_deco_josy_event_label"
    jump startEvent
elif result == "door_right":
    jump ep11_hots_fr1_rica_label
elif result == "go_down":
    jump ep11_hots_fr1_upper2_label

label ep11_hots_fr1_lr_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_hots_fr1_lr_label"
if "ep11_fr_deco_ari_event_label" in event_list:
    $ currentEvent = "ep11_fr_deco_ari_event_label"
    jump startEvent
if "ep11_fr_deco_sarah_event4_label" in event_list:
    scene ep11_hots_fr1_lrb with dissolve
else:
    scene ep11_hots_fr1_lr with dissolve

if "ep11_fr_deco_ari2_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_ari_idle", "ep11_hots_fr1_ari_hover", clicked=ui.returns("arieth"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_sage_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_sage_idle", "ep11_hots_fr1_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_sarah_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_sarah_idle", "ep11_hots_fr1_sarah_hover", clicked=ui.returns("sarah"), xpos=0, ypos=0, focus_mask=True)
if "ep11_fr_deco_sl_event_label" in event_list or "ep11_fr_deco_lily_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_lily_idle", "ep11_hots_fr1_lily_hover", clicked=ui.returns("lily"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_hots_fr1_upper3_label
elif result == "sarah":
    $ currentEvent = "ep11_fr_deco_sarah_event_label"
    jump startEvent
elif result == "arieth":
    $ currentEvent = "ep11_fr_deco_ari2_event_label"
    jump startEvent
elif result == "sage":
    $ currentEvent = "ep11_fr_deco_sage_event_label"
    jump startEvent
elif result == "lily":
    if "ep11_fr_deco_sl_event_label" in event_list:
        $ currentEvent = "ep11_fr_deco_sl_event_label"
    else:
        $ currentEvent = "ep11_fr_deco_lily_event_label"
    jump startEvent

label ep11_hots_fr1_rica_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_hots_fr1_rica_label"

scene ep11_hots_fr1_rica with dissolve

if "ep11_fr_deco_camila_event_label" in event_list:
    $ ui.imagebutton("ep11_hots_fr1_camila_idle", "ep11_hots_fr1_camila_hover", clicked=ui.returns("camila"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep11_hots_fr1_upper3_label
elif result == "camila":
    $ currentEvent = "ep11_fr_deco_camila_event_label"
    jump startEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

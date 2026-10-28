label ep11_freeroam_room2_label:
$ freeRoamID = "ep11_5"
$ roosterState = "ep11_5"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 225
$ found_money = False
$ found_money2 = False
$ bn_money_reward = True
$ studied = False

if art_unlock_orders():
    $ new_chat_msg("Jacob",True,11)

if ep7_accept_madame and branchAlone:
    $ new_phone_call("Madame Rose","ep11_madame_label_shop")
    $ new_chat_msg("Madame Rose",True,5)

if branchSage and (ep11_mg_party or wt_ep11_party_bella) and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ new_chat_msg("Sage",True,4)

$ new_chat_msg("Chad",True,2)

if ep11_camila_lewd:
    $ new_chat_msg("Camila",True,2)
if ep11_sarah_lewd and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ new_chat_msg("Sarah",False,1)
if ep11_mel_lewd and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ new_chat_msg("Melanie",False,1)
if ep11_nicole_dating and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ new_chat_msg("Nicole",False,3)

if branchJill and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ new_chat_msg("Jill",False,3)

$ new_chat_msg("Zoey",False,5)

if ep10_quinn_help:
    $ new_chat_msg("Riona",False,2)

if ep11_elena_lewd:
    $ new_chat_msg("Elena",True,4)

$ disabled_apps = []
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

if ep11_virus:
    $ settings_rooster_nickname = "FREE_RAM_2xE"
    $ roosterNickMCCustom = "FREE_RAM_2xE"
    $ rooster_nick_list[0][1] = "[name]@[roosterNickMCCustom]"

if ep8_help_nick:
    $ jumpLabel = "ft_setup_round6_label"
    $ ft_round+= 1
    if minigames:
        label ft_round6_label:
        jump ft_setup_round_label
    else:
        $ ft_nm_new_round()
    label ft_setup_round6_label:

$ rooster_jump_label = "ep11_diks5_fr2_lib_mid_label"
jump initRoosterLabel

label ep11_diks5_fr2_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks5_fr2_lib_mid_label"
if "ep11_zoey_joy_label" in event_list:
    $ currentEvent = "ep11_zoey_joy_label"
    jump startEvent
scene ep11_diks_fr5_lib_mid with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = ["","Talk to Zoey","","Talk to Chad"]
    $ optional_task_list = ["","","","","",""]

    $ chat_new_tasks = True
    $ event_list = []

    if ep11_elena_lewd:
        $ task_list[2] = "Talk to Elena"
    if ep10_quinn_help:
        $ optional_task_list[4] = "Talk to Riona"
    if ep8_help_nick and ((not ft_failed and minigames) or (not minigames and ft_fish_nm > 0)):
        $ optional_task_list[0] = "Take care of your fish"

    if minigames:
        $ optional_task_list[1] = "Study at your desk"
    if minigames:
        $ optional_task_list[2] = "Visit the gym (Brawler)"
    if not pb_completed:
        $ optional_task_list[3] = "Solve the puzzle box"

    if ep7_accept_madame and branchAlone:
        $ optional_task_list[5] = "Visit Madame Rose"

    if 1 in ep11_gift_list or 2 in ep11_gift_list:
        $ task_list[0] = "Wrap Christmas gifts"
        $ event_list.append("ep11_fr_gift_label")

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
    hide screen freeroam_intro_screen

$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep11_diks5_fr2_lib_left_label
elif result == "go_right":
    jump ep11_diks5_fr2_lib_right_label


label ep11_diks5_fr2_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks5_fr2_lib_left_label"
if "ep11_zoey_joy_label" in event_list:
    $ currentEvent = "ep11_zoey_joy_label"
    jump startEvent
scene ep11_diks_fr1_lib_left with dissolve

$ ui.imagebutton("ep11_diks_fr1_lib_desk_idle", "ep11_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep11_diks5_fr2_lib_mid_label
elif result == "desk":
    jump ep11_library_desk2d_label

label ep11_library_desk2d_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_library_desk2d_label"
if "ep11_zoey_joy_label" in event_list:
    $ currentEvent = "ep11_zoey_joy_label"
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
show spr_mask
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
$ ui.imagebutton("spr_cups", "spr_cups", clicked=ui.returns("cups"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_mask", "spr_mask", clicked=ui.returns("mask"), xpos=0, ypos=0, focus_mask=True)
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
    jump ep11_diks5_fr2_lib_left_label
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
            scene ep11_pb_done1c with dissolve
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
            scene ep11_pb_done2c with dissolve
            mc "(Um... Is there supposed to be something in here?)"
            mc "(It's empty... Damn. It felt like I had stumbled on a treasure box for a while.)"
            mc "(Oh, well... It was fun while it lasted. But all that for nothing...)"
            $ optional_task_list[3] = ""
            $ updateTaskList()
        show screen new_phone_screen
        $ quick_menu = qM
    jump ep11_library_desk2d_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep11_library_desk2d_label
elif result == "cups":
    if ep10_pp_activity == 0:
        mc "(DIKs' Thanksgiving was fun. I think people enjoyed playing Beer Pong.)"
    else:
        mc "(DIKs' Thanksgiving was fun. I kinda regret not having Beer Pong at the party.)"
    jump ep11_library_desk2d_label
elif result == "mask":
    mc "(The Christmas Panty party was all right, given the circumstances. I'm thankful that Derek helped out a lot.)"
    jump ep11_library_desk2d_label
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
    jump ep11_library_desk2d_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2d_label
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
    jump ep11_library_desk2d_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep11_library_desk2d_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep11_library_desk2d_label
elif result  == "flowers":
    mc "(Yep... I made that happen. I'll do my best to keep them alive for long.)"
    jump ep11_library_desk2d_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep11_library_desk2d_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep11_library_desk2d_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep11_library_desk2d_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep11_library_desk2d_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep11_library_desk2d_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep11_library_desk2d_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep11_library_desk2d_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep11_library_desk2d_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep11_library_desk2d_label
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
    jump ep11_library_desk2d_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2d_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2d_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2d_label
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
            $ fish_label = "ep11_ft_nm_return4b_label"
            jump nm_dead_fish_label
        else:
            scene ep11_fish1 with dissolve
            $ jumpLabel = "ep11_ft_nm_return4b_label"
            jump ep10_ft_nm_label
            label ep11_ft_nm_return4b_label:
    jump ep11_library_desk2d_label


label ep11_diks5_fr2_lib_right_label:
if "ep11_zoey_joy_label" in event_list:
    $ renpy.block_rollback()
    $ currentFreeRoamLabel = "ep11_diks5_fr2_lib_right_label"
    $ currentEvent = "ep11_zoey_joy_label"
    jump startEvent
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks5_fr2_lib_right_label"
if 1 in ep11_gift_list or 2 in ep11_gift_list:
    scene ep11_diks5_fr2_lib_rightb with dissolve
else:
    scene ep11_diks5_fr2_lib_right with dissolve

if "ep11_fr_gift_label" in event_list:
    $ ui.imagebutton("ep11_diks5_fr2_lib_right_gift_idle", "ep11_diks5_fr2_lib_right_gift_hover", clicked=ui.returns("gifts"), xpos=0, ypos=0, focus_mask=True)
if ep11_music:
    $ ui.imagebutton("ep11_diks5_fr2_guitar_idle", "ep11_diks5_fr2_guitar_hover", clicked=ui.returns("guitar"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep11_diks5_fr2_lib_mid_label
elif result == "go_down":
    $ currentEvent = "ep11_freeroam2_room_end_label"
    jump startEvent
    label ep11_freeroam2_room_end_label:
    if current_task == "Exit your room":
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep11_fr2_end_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(I still have things to do.)"
    jump endEvent
elif result == "gifts":
    $ currentEvent = "ep11_fr_gift_label"
    jump startEvent
elif result == "guitar":
    mc "(I need to practice a lot more for my performance... I will have to cram it like an exam.)"
    jump ep11_diks5_fr2_lib_right_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

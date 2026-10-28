label ep11_freeroam_room1_label:
$ freeRoamID = "ep11_1"
$ roosterState = "ep11_1"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 156
$ found_money = False
$ found_money2 = False
$ studied = False


$ bn_money_reward = True

$ bn_reward_available_list[0] = 14
$ bn_reward_available_list[1] = 2
$ bn_reward_available_list[2] = 4


$ new_phone_call("Sage","ep11_fr1_sage_call_label")
$ new_phone_call("Isabella","ep11_fr1_bella_call_label")

if ep7_accept_madame and branchAlone:
    $ new_phone_call("Madame Rose","ep11_madame_label_shop")
    $ new_chat_msg("Madame Rose",True,4)

if minigames:
    $ new_phone_call("Derek","ep11_derek_shop")
    $ new_phone_call("Magnar","ep11_magnar_shop")

if art_unlock_orders():
    $ new_chat_msg("Jacob",True,10)

if (ep10_rolling and not ep11_follow_quinn) or wt_ep11_quinn_lilly:
    $ new_chat_msg("Lily",True,2)
if ep11_camila_lewd:
    $ new_chat_msg("Camila",True,1)

$ art_girl_lvl2_list[1] = ep10_cathy_lewd
$ art_girl_crit2_list[1] = "- Got episode 10 lewd scene"
$ art_girl_lvl3_list[2] = (ep10_date_nicole and not ep10_cancel_date_nicole)
$ art_girl_crit3_list[2] = "- Got episode 10 lewd scene"
$ art_girl_lvl3_list[7] = ep10_rolling
$ art_girl_crit3_list[7] = "- Rolling with her"
$ art_girl_lvl2_list[10] = ep10_dating_nora
$ art_girl_crit2_list[10] = "- Got episode 10 lewd scene"


if not persistent.art_unlocked_lvl2[1] or not persistent.art_unlocked_lvl3[2] or not persistent.art_unlocked_lvl3[7] or not persistent.art_unlocked_lvl2[10]:
    $ mphone_new_art_available = True
$ art_girl_new_icon[1] = not persistent.art_unlocked_lvl2[1]
$ art_girl_new_icon[2] = not persistent.art_unlocked_lvl3[2]
$ art_girl_new_icon[7] = not persistent.art_unlocked_lvl3[7]
$ art_girl_new_icon[10] = not persistent.art_unlocked_lvl2[10]

$ disabled_apps = []
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

if ep8_help_nick:
    $ jumpLabel = "ft_setup_round4_label"
    $ ft_round+= 1
    if minigames:
        label ft_round4_label:
        jump ft_setup_round_label
    else:
        $ ft_nm_new_round()
    label ft_setup_round4_label:

$ rooster_jump_label = "ep11_diks2_fr2_lib_mid_label"
jump initRoosterLabel

label ep11_diks2_fr2_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks2_fr2_lib_mid_label"

scene anim_mid_lib_ep11 with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = ["Call Sage","Talk to Jacob","Inspect the notepad on your desk","Call Bella"]
    $ optional_task_list = ["","","","","",""]

    $ chat_new_tasks = True
    $ event_list = []

    $ event_list.append("ep11_gifts_label")
    $ event_list.append("ep11_fr_room_jacob_label")
    if ep8_help_nick and ((not ft_failed and minigames) or (not minigames and ft_fish_nm > 0)):
        $ event_list.append("ep11_fish_label")
        $ optional_task_list[0] = "Take care of your fish"

    if minigames:
        $ optional_task_list[1] = "Study at your desk"
    if minigames:
        $ optional_task_list[2] = "Visit the gym (Brawler)"
    $ optional_task_list[3] = "Solve the puzzle box"

    if ep7_accept_madame and branchAlone:
        $ optional_task_list[4] = "Visit Madame Rose"

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
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep11_diks2_fr2_lib_left_label
elif result == "go_right":
    jump ep11_diks2_fr2_lib_right_label
elif result == "go_down":
    jump ep11_diks2_fr2_lib_down_label


label ep11_diks2_fr2_lib_down_label:
if found_money2:
    scene ep11_diks2_fr2_lib_down with dissolve
else:
    scene ep11_diks2_fr2_lib_down_cash with dissolve
label ep11_diks2_fr2_lib_down_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks2_fr2_lib_down_label"

if not found_money2:
    $ ui.imagebutton("ep11_diks2_fr2_lib_down_cash_idle", "ep11_diks2_fr2_lib_down_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_diks2_fr2_lib_mid_label
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep11_diks2_fr2_lib_down with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_diks2_fr2_lib_down_label_nofx


label ep11_diks2_fr2_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks2_fr2_lib_left_label"
scene ep11_diks_fr1_lib_left with dissolve

$ ui.imagebutton("ep11_diks_fr1_lib_desk_idle", "ep11_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep11_diks2_fr2_lib_mid_label
elif result == "desk":
    jump ep11_library_desk2_label

label ep11_library_desk2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_library_desk2_label"

if "ep11_fish_label" in event_list:
    $ currentEvent = "ep11_fish_label"
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
$ ui.imagebutton("spr_gifts", "spr_gifts_hover", clicked=ui.returns("gifts"), xpos=0, ypos=0, focus_mask=True)
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
    jump ep11_diks2_fr2_lib_left_label
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
            scene ep11_pb_done1 with dissolve
            if not persistent.ep11_cardmy13 or not persistent.ep11_cardmy14:
                if not persistent.ep11_cardmy14:
                    $ persistent.rew_maya_unlocked += 1
                    $ persistent.ep11_cardmy14 = True
                if not persistent.ep11_cardmy13:
                    $ persistent.rew_maya_unlocked += 1
                    $ persistent.ep11_cardmy13 = True
                $ persistent.chat_new_rewards = True
                $ calcRenders()
                show screen srmsg
                $ renpy.pause(3)
                hide screen srmsg
            if steamAchievements and not config.console and not config.developer:
                $ achievement.grant("IDS3_31")
                init:
                    $ achievement.register("IDS3_31")
            mc "(No way! I did it! That's crazy. What a fun puzzle.)"
            scene ep11_pb_done2 with dissolve
            mc "(Um... Is there supposed to be something in here?)"
            mc "(It's empty... Damn. It felt like I had stumbled on a treasure box for a while.)"
            mc "(Oh, well... It was fun while it lasted. But all that for nothing...)"
            $ optional_task_list[3] = ""
            $ updateTaskList()
        show screen new_phone_screen
        $ quick_menu = qM
    jump ep11_library_desk2_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep11_library_desk2_label
elif result == "cups":
    if ep10_pp_activity == 0:
        mc "(DIKs' Thanksgiving was fun. I think people enjoyed playing Beer Pong.)"
    else:
        mc "(DIKs' Thanksgiving was fun. I kinda regret not having Beer Pong at the party.)"
    jump ep11_library_desk2_label
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
    jump ep11_library_desk2_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2_label
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
    jump ep11_library_desk2_label
elif result  == "gifts":
    if "ep11_gifts_label" in event_list:
        $ currentEvent = "ep11_gifts_label"
        jump startEvent
    else:
        call screen giftMsgScreen
        $ renpy.pause(0.5)
        jump ep11_library_desk2_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep11_library_desk2_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep11_library_desk2_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep11_library_desk2_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep11_library_desk2_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep11_library_desk2_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep11_library_desk2_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep11_library_desk2_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep11_library_desk2_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep11_library_desk2_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep11_library_desk2_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep11_library_desk2_label
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
    jump ep11_library_desk2_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep11_library_desk2_label
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
            $ fish_label = "ep11_ft_nm_return4_label"
            jump nm_dead_fish_label
        else:
            scene ep11_fish1 with dissolve
            $ jumpLabel = "ep11_ft_nm_return4_label"
            jump ep10_ft_nm_label
            label ep11_ft_nm_return4_label:
    jump ep11_library_desk2_label

label ep11_choose_paintingb_label:
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
    jump ep11_choose_paintingb_label
elif result == "left":
    if ep7_current_desk_painting == 0:
        $ ep7_current_desk_painting = 16
    else:
        $ ep7_current_desk_painting -= 1
    if ep7_current_desk_painting != 0:
        $ ep7_current_desk_painting = desk_check_unlocked_2d(ep7_current_desk_painting, False)
    jump ep11_choose_paintingb_label
else:
    if freeRoamID == "ep11_1":
        $ currentFreeRoamLabel = "ep11_library_desk2_label"
    elif freeRoamID == "ep11_2":
        $ currentFreeRoamLabel = "ep11_library_desk2b_label"
    elif freeRoamID == "ep11_4":
        $ currentFreeRoamLabel = "ep11_library_desk2c_label"
    elif freeRoamID == "ep11_5":
        $ currentFreeRoamLabel = "ep11_library_desk2d_label"
    jump endEvent

label ep11_choose_2nd_paintingb_label:
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
    jump ep11_choose_2nd_paintingb_label
elif result == "left":
    if ep8_current_second_painting == 0:
        $ ep8_current_second_painting = 19
    else:
        $ ep8_current_second_painting -= 1
    if ep8_current_second_painting != 0:
        $ ep8_current_second_painting = desk_check_second_unlocked_2d(ep8_current_second_painting, False)
    jump ep11_choose_2nd_paintingb_label
else:
    if freeRoamID == "ep11_1":
        $ currentFreeRoamLabel = "ep11_library_desk2_label"
    elif freeRoamID == "ep11_2":
        $ currentFreeRoamLabel = "ep11_library_desk2b_label"
    elif freeRoamID == "ep11_4":
        $ currentFreeRoamLabel = "ep11_library_desk2c_label"
    elif freeRoamID == "ep11_5":
        $ currentFreeRoamLabel = "ep11_library_desk2d_label"
    jump endEvent

label ep11_diks2_fr2_lib_right_label:
if "ep11_fr_room_jacob_label" in event_list:
    $ renpy.block_rollback()
    $ currentFreeRoamLabel = "ep11_diks2_fr2_lib_right_label"
    $ currentEvent = "ep11_fr_room_jacob_label"
    jump startEvent
if found_money:
    scene ep11_diks2_fr2_lib_right with dissolve
else:
    scene ep11_diks2_fr2_lib_right_cash with dissolve
label ep11_diks2_fr2_lib_right_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_diks2_fr2_lib_right_label"

if not found_money:
    $ ui.imagebutton("ep11_diks2_fr2_lib_right_cash_idle", "ep11_diks2_fr2_lib_right_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_diks2_fr2_lib_right_books_idle", "ep11_diks2_fr2_lib_right_books_hover", clicked=ui.returns("books"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep11_diks2_fr2_lib_mid_label
elif result == "books":
    mc "(I should read more, but with the class literature and all, it's hard to get motivated. I did read {color=00ff00}3{/color} of those books, though.)"
    jump ep11_diks2_fr2_lib_right_label_nofx
elif result == "go_down":
    $ currentEvent = "ep11_freeroam1_room_end_label"
    jump startEvent
    label ep11_freeroam1_room_end_label:
    if current_task == "Exit your room":
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep11_fr1_end_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(I still have things to do.)"
    jump endEvent
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep11_diks2_fr2_lib_right with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep11_diks2_fr2_lib_right_label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

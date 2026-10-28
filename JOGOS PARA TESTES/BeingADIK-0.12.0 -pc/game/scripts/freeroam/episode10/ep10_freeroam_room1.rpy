label ep10_freeroam_room1_label:
if branchSage:
    scene ep10_freeroam_room1b with Fade(2,2,2)
else:
    scene ep10_freeroam_room1 with Fade(2,2,2)
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep10/hollow_sky.mp3"])
$ renpy.pause()

if branchSage:
    scene ep10_freeroam_room2b with dissolve
    mc "*{i}Yawns{/i}*"
    scene ep10_freeroam_room3b with dissolve
    mc "(It feels nice to catch up on some sleep.)"
    scene ep10_freeroam_room4b with dissolve
    mc "(Seems like she needed it too.)"
    scene ep10_freeroam_room3b with dissolve
    mc "(I love these study days. No classes, just my conscience telling me how much I should study.)"
    scene ep10_freeroam_room5b with dissolve
    mc "*{i}Smack{/i}*"
    scene ep10_freeroam_room6b with dissolve
    sa "No... Is it morning already?"
    scene ep10_freeroam_room7b with dissolve
    mc "Yep. I've got a study day today, but you don't."
    scene ep10_freeroam_room6b with dissolve
    sa "Wanna trade?"
    scene ep10_freeroam_room7b with dissolve
    mc "Not at all. Stay in bed for a bit more if you want. I'll bring us breakfast."
else:
    scene ep10_freeroam_room2 with dissolve
    mc "*{i}Yawns{/i}*"
    scene ep10_freeroam_room3 with dissolve
    mc "(It feels nice to catch up on some sleep.)"
    mc "(I love these study days. No classes, just my conscience telling me how much I should study.)"


$ freeRoamID = "ep10_2"
$ roosterState = "ep10_2"
$ tmpInt = 0
show screen wt_tasks_shown
$ guideSuggestedPage = 120
$ found_money = False
$ found_money2 = False
$ studied = False

if art_unlock_orders():
    $ new_chat_msg("Jacob",True,8)

$ new_chat_msg("Elena",True,2)
$ new_chat_msg("Isabella",True,2)

if branchJill and ep9_told_jill:
    $ new_chat_msg("Jill",True,2)

$ new_chat_msg("Zoey",True,2)

$ new_phone_call("Dad","ep10_dad_phone_call_label")
if ep7_accept_madame and branchAlone:
    $ new_phone_call("Madame Rose","ep10_madame_label_shop")
    $ new_chat_msg("Madame Rose",True,3)

$ new_phone_call("Isabella","ep10_bella_phone_call_label")
if minigames:
    $ new_phone_call("Derek","ep10_derek_shop")
    $ new_phone_call("Magnar","ep10_magnar_shop")

$ disabled_apps = []
$ disabled_apps.append("brawler")
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

if ep8_help_nick:
    $ jumpLabel = "ft_setup_round2_label"
    $ ft_round+= 1
    if minigames:
        label ft_round2_label:
        jump ft_setup_round_label
    else:
        $ ft_nm_new_round()
    label ft_setup_round2_label:

$ rooster_jump_label = "ep10_diks_fr2_lib_mid_label"
jump initRoosterLabel

label ep10_diks_fr2_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr2_lib_mid_label"
scene ep10_diks_fr2_lib_mid with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = ["Call Isabella","Call your dad","Text Zoey","Text Elena","","","",""]
    $ optional_task_list = ["",""]

    $ chat_new_tasks = True
    $ event_list = []

    if branchJill and ep9_told_jill:
        $ task_list[7] = "Text Jill"
    if branchSage:
        $ task_list[6] = "Talk to Sage"
        $ event_list.append("ep10_fr2_sage_event_label")

    if ep8_help_nick:
        $ task_list[4] = "Check the bowl on your desk"
        $ event_list.append("ep10_fr2_desk_event_label")

    if not branchIsabella and minigames:
        $ optional_task_list[1] = "Study at your desk"


    if ep7_accept_madame and branchAlone:
        $ optional_task_list.append("Visit Madame Rose")

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

$ ui.imagebutton("fr_arrow_box", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_arrow_box", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep10_diks_fr2_lib_left_label
elif result == "go_right":
    jump ep10_diks_fr2_lib_right_label


label ep10_diks_fr2_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr2_lib_left_label"
scene ep10_diks_fr1_lib_left with dissolve
$ ui.imagebutton("ep10_diks_fr1_lib_desk_idle", "ep10_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_arrow_box", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep10_diks_fr2_lib_mid_label
elif result == "desk":
    jump ep10_library_desk2_label

label ep10_library_desk2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_library_desk2_label"

if "ep10_fr2_desk_event_label" in event_list:
    $ currentEvent = "ep10_fr2_desk_event_label"
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
$ ui.imagebutton("ep8_gym_spr", "ep8_gym_spr", clicked=ui.returns("gym"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_wallet_spr", "ep7_wallet_spr_hover", clicked=ui.returns("wallet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_phone_spr2", "ep7_phone_spr2", clicked=ui.returns("phone"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_tabs_spr", "ep7_tabs_spr", clicked=ui.returns("tabs"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("spr_box_ep9", "spr_box_ep9_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library3_frame_idle", "ep7_freeroam_diks_library3_frame_hover", clicked=ui.returns("frame"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library_desk_study_idle", "ep7_freeroam_diks_library_desk_study_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("arrow_invis_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep10_diks_fr2_lib_left_label
elif result == "box":
    if pb_3_lid_open[0]:
        mc "(I'll play more with this box later. I need to solve it!)"
    else:
        $ qM = quick_menu
        $ quick_menu = 0
        hide screen new_phone_screen
        call screen puzzle_box_screen_ep10
        hide screen puzzle_box_help
        hide screen puzzle_box_wt_help
        $ renpy.pause(0.5)
        show screen new_phone_screen
        $ quick_menu = qM
    jump ep10_library_desk2_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep10_library_desk2_label
elif result  == "second_painting":
    $ currentEvent = "ep10_choose_2nd_paintingb_label"
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
    jump ep10_library_desk2_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk2_label
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
    jump ep10_library_desk2_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep10_library_desk2_label
elif result  == "conch":
    mc "(Josy's belt buckle and one of Maya's flowers fell off when we had a threesome. They're nice mementos for my wall, I think.)"
    jump ep10_library_desk2_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep10_library_desk2_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep10_library_desk2_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep10_library_desk2_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep10_library_desk2_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep10_library_desk2_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep10_library_desk2_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep10_library_desk2_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep10_library_desk2_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep10_library_desk2_label
elif result == "frame":
    $ currentEvent = "ep10_choose_paintingb_label"
    jump startEvent
elif result == "study":
    $ renpy.block_rollback()
    if branchIsabella:
        mc "(I'll study at the library later. It will be nice seeing Bella today.)"
    else:
        if minigames:
            if studied:
                mc "(I've studied enough for now. I can study some more later.)"
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
            mc "(I'm gonna study later today.)"
    jump ep10_library_desk2_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk2_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk2_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep10_library_desk2_label
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
            $ fish_label = "ep10_ft_nm_return2_label"
            jump nm_dead_fish_label
        else:
            scene ep10_fr2_desk_event1 with dissolve
            $ jumpLabel = "ep10_ft_nm_return2_label"
            jump ep10_ft_nm_label
            label ep10_ft_nm_return2_label:

    jump ep10_library_desk2_label

label ep10_choose_paintingb_label:
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
    jump ep10_choose_paintingb_label
elif result == "left":
    if ep7_current_desk_painting == 0:
        $ ep7_current_desk_painting = 16
    else:
        $ ep7_current_desk_painting -= 1
    if ep7_current_desk_painting != 0:
        $ ep7_current_desk_painting = desk_check_unlocked_2d(ep7_current_desk_painting, False)
    jump ep10_choose_paintingb_label
else:
    $ currentFreeRoamLabel = "ep10_library_desk2_label"
    jump endEvent

label ep10_choose_2nd_paintingb_label:
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
    jump ep10_choose_2nd_paintingb_label
elif result == "left":
    if ep8_current_second_painting == 0:
        $ ep8_current_second_painting = 19
    else:
        $ ep8_current_second_painting -= 1
    if ep8_current_second_painting != 0:
        $ ep8_current_second_painting = desk_check_second_unlocked_2d(ep8_current_second_painting, False)
    jump ep10_choose_2nd_paintingb_label
else:
    $ currentFreeRoamLabel = "ep10_library_desk2_label"
    jump endEvent

label ep10_diks_fr2_lib_right_label:
if branchSage:
    if found_money:
        scene ep10_diks_fr2_lib_rights with dissolve
    else:
        scene ep10_diks_fr2_lib_rights_cash with dissolve
else:
    if found_money:
        scene ep10_diks_fr2_lib_right with dissolve
    else:
        scene ep10_diks_fr2_lib_right_cash with dissolve
label ep10_diks_fr2_lib_right_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep10_diks_fr2_lib_right_label"

if not found_money:
    $ ui.imagebutton("ep10_diks_fr2_lib_right_cash_idle", "ep10_diks_fr2_lib_right_cash_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
if branchSage and "ep10_fr2_sage_event_label" in event_list:
    $ ui.imagebutton("ep10_diks_fr2_lib_right_sage_idle", "ep10_diks_fr2_lib_right_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("arrow_invis", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_arrow_box", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep10_diks_fr2_lib_mid_label
elif result == "sage":
    $ currentEvent = "ep10_fr2_sage_event_label"
    jump startEvent
elif result == "go_down":
    $ currentEvent = "ep10_freeroam_room_end_label"
    jump startEvent
    label ep10_freeroam_room_end_label:
    if current_task == "Exit your room":
        menu:
            "End free roam":
                $ phone_clear_jump_label = "ep10_jm_plan_label"
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
    if branchSage:
        scene ep10_diks_fr2_lib_rights with dissolve
    else:
        scene ep10_diks_fr2_lib_right with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep10_diks_fr2_lib_right_label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

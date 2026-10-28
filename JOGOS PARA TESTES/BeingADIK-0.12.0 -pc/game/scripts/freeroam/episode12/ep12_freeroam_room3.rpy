label ep12_fr_room3_setup_label:
$ freeRoamID = "ep12_4"
$ roosterState = "ep12_4"
$ tmpInt = 0
$ guideSuggestedPage = 273
$ found_money = False
$ found_money2 = False
$ studied = False
show screen wt_tasks_shown
if art_unlock_orders():
    $ new_chat_msg("Jacob",True,13)

$ new_chat_msg("Dad",True,4)

$ disabled_apps = ["brawler"]
$ firstTimeFreeRoam = True
$ game_money_available = True

$ triple_tile_money_available = True

if ep8_help_nick:
    $ jumpLabel = "ft_setup_round9_label"
    $ ft_round+= 1
    if minigames:
        label ft_round9_label:
        jump ft_setup_round_label
    else:
        $ ft_nm_new_round()
    label ft_setup_round9_label:

$ rooster_jump_label = "ep12_diks2_fr3_lib_mid_label"
jump initRoosterLabel

label ep12_diks2_fr3_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_diks2_fr3_lib_mid_label"

if "trigger_active" in event_list:
    if "ep12_fr_jen_event_label" in event_list:
        $ currentEvent = "ep12_fr_jen_event_label"
        jump startEvent
    if "ep12_fr_dav_event_label" in event_list:
        $ currentEvent = "ep12_fr_dav_event_label"
        jump startEvent

if roadSage:
    scene ep12_diks2_fr3_lib_mids with dissolve
else:
    scene ep12_diks2_fr3_lib_mid with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = ["","","",""]
    $ optional_task_list = ["","",""]

    $ chat_new_tasks = True
    $ event_list = []

    if breakup:
        $ task_list[0] = "Check your desk"
        $ event_list.append("ep12_fr_remove_label")
    if ep11_music and not roadSage:
        $ task_list[1] = "Call David Cerus Baxter"
        $ event_list.append("ep12_fr_dav_event_label")
    if ep12_brawler_comp_won and not roadSage:
        $ task_list[1] = "Call Jen Byson"
        $ event_list.append("ep12_fr_jen_event_label")
    if roadSage:
        $ task_list[1] = "Talk to Sage"
        $ event_list.append("ep12_fr_sage_event_label")
    if ep8_help_nick and ((not ft_failed and minigames) or (not minigames and ft_fish_nm > 0)):
        $ optional_task_list[0] = "Take care of your fish"

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

$ ui.imagebutton("ep12_diks2_fr3_bed_idle", "ep12_diks2_fr3_bed_hover", clicked=ui.returns("bed"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep12_diks2_fr3_lib_left_label
elif result == "go_right":
    jump ep12_diks2_fr3_lib_right_label
elif result == "bed":
    $ currentEvent = "ep12_freeroam3_room_end_label"
    jump startEvent
    label ep12_freeroam3_room_end_label:
    if current_task == "Lie down on the bed":
        menu:
            "End free roam":
                if roadSage:
                    $ phone_clear_jump_label = "ep12_fr_sage_leave_label"
                else:
                    stop music fadeout 3
                    $ phone_clear_jump_label = "ep12_sally_end_label"
                jump end_freeroam
            "Not yet":
                $ renpy.pause(0.5)
    else:
        mc "(Not just quite yet...)"
    jump endEvent

label ep12_diks2_fr3_lib_left_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_diks2_fr3_lib_left_label"
if roadSage:
    scene ep12_diks_fr1_lib_left_s with dissolve
else:
    scene ep11_diks_fr1_lib_left with dissolve

$ ui.imagebutton("ep11_diks_fr1_lib_desk_idle", "ep11_diks_fr1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep12_diks2_fr3_lib_mid_label
elif result == "desk":
    jump ep12_library_desk3b_label

label ep12_library_desk3b_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_library_desk3b_label"

if "ep12_fr_remove_label" in event_list:
    $ currentEvent = "ep12_fr_remove_label"
    jump startEvent

if ep7_current_desk_painting > 0:
    scene ep9_freeroam_diks_library_desk
else:
    scene ep9_freeroam_diks_library_desk0a
if roadJill:
    show ep7_polaroid_jill_spr
if ep6_fakeID:
    show ep7_fakeid_spr
if ep6_vipPass:
    show ep7_vip_spr

if ep5_dikWinner:
    show spr_glasses_helmet
else:
    show spr_glasses

if persistent.triple_tile_challenge:
    show ep7_triple_tile_spr
show ep7_phone_spr
show ep7_wallet_spr

if ep11_flowers:
    show spr_flowers

show spr_box_ep9
show ep8_gym_spr
show ep9_monkey_spr

if roadQuinn:
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
if roadSage:
    show ep8_leaf_spr
if roadIsabella:
    show ep8_cork_spr
if roadMayaJosy:
    show spr_conch
show spr_sword
if ep8_help_nick:
    show ep10_fish_spr
show spr_cups
show spr_mask
show spr_candy
show spr_hello
if roadSage:
    show spr_calendar_december
if roadJill:
    show spr_poster
with dissolve

if ep10_quinn_photo == 1 and roadQuinn:
    $ ui.imagebutton("ep10_quinn_spr1", "ep10_quinn_spr1", clicked=ui.returns("quinn_spr1"), xpos=0, ypos=0, focus_mask=True)
elif ep10_quinn_photo == 2:
    $ ui.imagebutton("ep10_quinn_spr2", "ep10_quinn_spr2", clicked=ui.returns("quinn_spr2"), xpos=0, ypos=0, focus_mask=True)
if ep8_help_nick:
    $ ui.imagebutton("ep10_fish_spr", "ep10_fish_spr_hover", clicked=ui.returns("fish_tank"), xpos=0, ypos=0, focus_mask=True)
if roadSage:
    $ ui.imagebutton("spr_calendar_december", "spr_calendar_december", clicked=ui.returns("calendar_sage"), xpos=0, ypos=0, focus_mask=True)
if roadJill:
    $ ui.imagebutton("spr_poster", "spr_poster", clicked=ui.returns("poster"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_monkey_spr", "ep9_monkey_spr", clicked=ui.returns("monkey"), xpos=0, ypos=0, focus_mask=True)
if roadJill:
    $ ui.imagebutton("ep7_polaroid_jill_spr", "ep7_polaroid_jill_spr", clicked=ui.returns("polaroid"), xpos=0, ypos=0, focus_mask=True)
if ep6_fakeID:
    $ ui.imagebutton("ep7_fakeid_spr", "ep7_fakeid_spr", clicked=ui.returns("fakeid"), xpos=0, ypos=0, focus_mask=True)
if ep6_vipPass:
    $ ui.imagebutton("ep7_vip_spr", "ep7_vip_spr", clicked=ui.returns("vip"), xpos=0, ypos=0, focus_mask=True)
if persistent.triple_tile_challenge:
    $ ui.imagebutton("ep7_triple_tile_spr", "ep7_triple_tile_spr", clicked=ui.returns("triple_tile"), xpos=0, ypos=0, focus_mask=True)
if ep5_dikWinner:
    $ ui.imagebutton("spr_glasses_helmet", "spr_glasses_helmet", clicked=ui.returns("glasses"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("spr_glasses", "spr_glasses", clicked=ui.returns("glasses"), xpos=0, ypos=0, focus_mask=True)
if ep8_second_painting:
    if ep8_current_second_painting > 0:
        $ ui.imagebutton("spr_second_painting[ep8_current_second_painting]", "spr_second_painting_hover", clicked=ui.returns("second_painting"), xpos=0, ypos=0, focus_mask=True)
    else:
        $ ui.imagebutton("ep9_freeroam_diks_second_painting0", "spr_second_painting_hover", clicked=ui.returns("second_painting"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("spr_second_painting_buy_idle", "spr_second_painting_buy_hover", clicked=ui.returns("buy_second_painting"), xpos=0, ypos=0, focus_mask=True)
if not ep8_recital_failed:
    $ ui.imagebutton("ep8_concert_spr", "ep8_concert_spr", clicked=ui.returns("concert"), xpos=0, ypos=0, focus_mask=True)
if roadSage:
    $ ui.imagebutton("ep8_leaf_spr", "ep8_leaf_spr", clicked=ui.returns("leaf"), xpos=0, ypos=0, focus_mask=True)
if roadIsabella:
    $ ui.imagebutton("ep8_cork_spr", "ep8_cork_spr", clicked=ui.returns("cork"), xpos=0, ypos=0, focus_mask=True)
if roadMayaJosy:
    $ ui.imagebutton("spr_conch", "spr_conch", clicked=ui.returns("conch"), xpos=0, ypos=0, focus_mask=True)
if ep11_flowers:
    $ ui.imagebutton("spr_flowers", "spr_flowers", clicked=ui.returns("flowers"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_sword", "spr_sword", clicked=ui.returns("sword"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_cups", "spr_cups", clicked=ui.returns("cups"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_candy", "spr_candy", clicked=ui.returns("candy"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("spr_hello", "spr_hello", clicked=ui.returns("hello"), xpos=0, ypos=0, focus_mask=True)
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
    jump ep12_diks2_fr3_lib_left_label
elif result == "box":
    if pb_completed:
        mc "(That box was tricky to solve, but I did it. Even if it was empty, it made me feel smart and confident. That's something, I guess.)"
    else:
        mc "(Stupid puzzle box.)"
    jump ep12_library_desk3b_label
elif result == "glasses":
    mc "(I'm gonna hold on to these glasses until Derek pays me $1000.)"
    jump ep12_library_desk3b_label
elif result == "sword":
    mc "(My sword looks kinda cool on the wall. Something to remember my first party by.)"
    jump ep12_library_desk3b_label
elif result == "hello":
    mc "(HELLO!!! Haha.)"
    jump ep12_library_desk3b_label
elif result == "candy":
    $ ui.imagebutton("spr_candy_big", "spr_candy_big", clicked=ui.returns("spr_candy_big"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
elif result == "cups":
    if ep10_pp_activity == 0:
        mc "(DIKs' Thanksgiving was fun. I think people enjoyed playing Beer Pong.)"
    else:
        mc "(DIKs' Thanksgiving was fun. I kinda regret not having Beer Pong at the party.)"
    jump ep12_library_desk3b_label
elif result == "mask":
    mc "(The Christmas Panty party was all right, given the circumstances. I'm thankful that Derek helped out a lot.)"
    jump ep12_library_desk3b_label
elif result  == "second_painting":
    $ currentEvent = "ep12_choose_2nd_paintingb_label"
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
    jump ep12_library_desk3b_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
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
    jump ep12_library_desk3b_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep12_library_desk3b_label
elif result  == "conch":
    mc "(It makes me sad to look at those now...)"
    jump ep12_library_desk3b_label
elif result  == "flowers":
    mc "(Yep... I made that happen. I'll do my best to keep them alive for long.)"
    jump ep12_library_desk3b_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep12_library_desk3b_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep12_library_desk3b_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep12_library_desk3b_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep12_library_desk3b_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep12_library_desk3b_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep12_library_desk3b_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep12_library_desk3b_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep12_library_desk3b_label
elif result == "frame":
    $ currentEvent = "ep12_choose_paintingb_label"
    jump startEvent
elif result == "study":
    $ renpy.block_rollback()
    mc "(I've got nothing to study.)"
    jump ep12_library_desk3b_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
elif result == "calendar_sage":
    show calendar_sage_december
    mc "(Such a thoughtful and personal gift. When did she find the time to make this one?)"
    hide calendar_sage_december
    $ ui.imagebutton("calendar_sage_december", "calendar_sage_december", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
elif result == "poster":
    mc "(I love, love, love that album. And the poster too for that matter.)"
    jump ep12_library_desk3b_label
elif result == "poster":
    mc "(I love this poster.)"
    jump ep12_library_desk3b_label
elif result == "quinn_spr1":
    show quinn_spr1_big
    mc "(This is a hot photo. I fucking love it.)"
    hide quinn_spr1_big
    $ ui.imagebutton("quinn_spr1_big", "quinn_spr1_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
elif result == "quinn_spr2":
    show quinn_spr2_big
    mc "(Haha, I love this photo.)"
    hide quinn_spr2_big
    $ ui.imagebutton("quinn_spr2_big", "quinn_spr2_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep12_library_desk3b_label
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
            $ fish_label = "ep12_ft_nm_return3_label"
            jump nm_dead_fish_label
        else:
            scene ep12_fish1 with dissolve
            $ jumpLabel = "ep12_ft_nm_return3_label"
            jump ep10_ft_nm_label
            label ep12_ft_nm_return3_label:
    jump ep12_library_desk3b_label

label ep12_diks2_fr3_lib_right_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep12_diks2_fr3_lib_right_label"
if not roadSage and not "trigger_active" in event_list:
    $ event_list.append("trigger_active")
if branchJill:
    scene ep12_diks2_fr3_lib_right_j with dissolve
elif roadSage:
    scene ep12_diks2_fr3_lib_right_s with dissolve
else:
    scene ep12_diks2_fr3_lib_right with dissolve

if branchJill:
    $ ui.imagebutton("ep12_diks2_fr3_lib_right_g_idle", "ep12_diks2_fr3_lib_right_g_hover", clicked=ui.returns("guitar"), xpos=0, ypos=0, focus_mask=True)
if "ep12_fr_sage_event_label" in event_list:
    $ ui.imagebutton("ep12_diks2_fr3_lib_right_sage_idle", "ep12_diks2_fr3_lib_right_sage_hover", clicked=ui.returns("sage"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_left":
    jump ep12_diks2_fr3_lib_mid_label
elif result == "sage":
    $ currentEvent = "ep12_fr_sage_event_label"
    jump startEvent
elif result == "guitar":
    if roadJill:
        mc "(Man, I love my Strutter. I love Lana. That feels a bit weird to say, but it's a suitable name for it.)"
    else:
        mc "(I should return that guitar to Jill... It would feel wrong to keep it.)"
    jump ep12_diks2_fr3_lib_right_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

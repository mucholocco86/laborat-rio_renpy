label ep9_freeroam_diks_ph1_label:
$ freeRoamID = "ep9_1"
show screen wt_tasks_shown
$ roosterState = "ep9_1"
$ tmpInt = 0


$ found_money = False
$ found_money2 = False
$ studied = False

$ art_girl_lvl2_list[4] = ep8_jade_lewd
$ art_girl_crit2_list[4] = "- Got episode 8 lewd scene"
$ art_girl_lvl2_list[8] = ep8_maya_lewd
$ art_girl_crit2_list[8] = "- Got episode 8 solo lewd scene"
$ art_girl_lvl2_list[9] = ep8_melanie_lewd
$ art_girl_crit2_list[9] = "- Got episode 8 lewd scene"
$ art_girl_lvl1_list[10] = ep6_nora_lewd
$ art_girl_crit1_list[10] = "- Got episode 6 lewd scene"
$ art_girl_lvl1_list[15] = True
$ art_girl_crit1_list[15] = "- Played the Interlude"

if not persistent.art_unlocked_lvl2[4] or not persistent.art_unlocked_lvl2[8] or not persistent.art_unlocked_lvl2[9] or not persistent.art_unlocked_lvl1[15]:
    $ mphone_new_art_available = True
$ art_girl_new_icon[4] = not persistent.art_unlocked_lvl2[4]
$ art_girl_new_icon[8] = not persistent.art_unlocked_lvl2[8]
$ art_girl_new_icon[9] = not persistent.art_unlocked_lvl2[9]
$ art_girl_new_icon[10] = not persistent.art_unlocked_lvl1[10]
$ art_girl_new_icon[15] = not persistent.art_unlocked_lvl1[15]

$ mphone_contact_list.append(["Zoey","NONE",False])
$ mphone_chat_history_list.append(["Zoey",0,[],[]," ",0])

$ text_message_screen_list = []

$ text_message_screen_list.append(["Zoey","Hey, [name]. I got your new number from Neil. Hit me up when you have time for it. /Zoey",True])
$ text_message_screen_list.append(["%s" % name,"Hey. What's up?",False])
$ text_message_screen_list.append(["Zoey","Dude... Hey!!! mphone_emoji_smile",True])
$ text_message_screen_list.append(["Zoey","I don't wanna have this chat over text. Can we meet up somewhere? You know, when you got time to kill. When or where, that's up to ya.",True])
$ text_message_screen_list.append(["%s" % name,"Tomorrow afternoon, maybe? I don't know where, though.",False])
$ text_message_screen_list.append(["Zoey","Awesome! How about 2 p.m. at that park we used to go to? You know, the one on 5th?",True])
$ text_message_screen_list.append(["%s" % name,"Ok.",False])
$ text_message_screen_list.append(["Zoey","Great. Tomorrow, then. L8r Sk8r",True])

if zoey_dik:
    $ text_message_screen_list.append(["Zoey","Thanks for hearing me out today. I knew it was gonna be emotional and shit, but I didn't expect to cry that much.",True])
else:
    $ text_message_screen_list.append(["Zoey","Thanks for hearing me out today. I knew it was gonna be emotional, but I didn't expect to cry that much.",True])

if ep9_mad_at_zoey:
    $ text_message_screen_list.append(["%s" % name,"Yeah.",False])
else:
    $ text_message_screen_list.append(["%s" % name,"It felt good to finally say those things out loud to you. Don't worry about the crying. I know you only do that when things matter a lot to you.",False])

$ text_message_screen_list.append(["Zoey","Halloween's closing in. Were you serious about that invite?",True])
$ text_message_screen_list.append(["%s" % name,"Yeah, you're welcome to come if you want to.",False])
$ text_message_screen_list.append(["Zoey","I'm coming, for sure. Things are different in this town. It gets pretty boring when there aren't many left.",True])
$ text_message_screen_list.append(["%s" % name,"I felt the same this summer. So, no one's left?",False])
$ text_message_screen_list.append(["Zoey","Debbie's still around. But she's working full-time at Shoes and Laces these days.",True])
$ text_message_screen_list.append(["%s" % name,"Say hi from me the next time you see her.",False])
$ text_message_screen_list.append(["Zoey","Sure thing.",True])

$ text_message_screen_list.append(["Zoey","Dude! Did you see the news?",True])
$ text_message_screen_list.append(["%s" % name,"No?",False])
$ text_message_screen_list.append(["Zoey","ShitFaced are releasing a new album!",True])
$ text_message_screen_list.append(["%s" % name,"No way! It's been what? 6 years since their last one?",False])
$ text_message_screen_list.append(["Zoey","Yeah, this is amazing! There's a teaser video of it. I'll link you on Rooster!",True])
$ text_message_screen_list.append(["%s" % name,"Do you think this means they'll tour again?",False])
$ text_message_screen_list.append(["Zoey","If they do, I'm SO there! And you're coming too!",True])
if ep9_mad_at_zoey:
    $ text_message_screen_list.append(["%s" % name,"I gotta go. Talk another time.",False])
    $ text_message_screen_list.append(["Zoey","Sure! mphone_emoji_laugh",True])
else:
    $ text_message_screen_list.append(["%s" % name,"I'd love to see them live before I die.",False])
    $ text_message_screen_list.append(["Zoey","Before YOU die? Haha! I'm pretty sure they'll be dead a long time before you go. They're getting old. mphone_emoji_laugh",True])
    $ text_message_screen_list.append(["%s" % name,"Did you send the link?",False])

$ text_message_screen_list.append(["Zoey","So, Floyd's still a pain in the ass.",True])
$ text_message_screen_list.append(["%s" % name,"That doesn't surprise me. What's he up to now?",False])

$ text_message_screen_list.append(["Zoey","He fucking smirks and laughs every time Mom mentions I'm back to living at home. Almost as if he's telling me \"Told ya it wouldn't work\".",True])
$ text_message_screen_list.append(["%s" % name,"That's annoying. How are you handling it?",False])
if zoey_dik:
    $ text_message_screen_list.append(["Zoey","I tell him to go fuck himself. What else can I do?",True])
    if affinity == "DIK":
        $ text_message_screen_list.append(["%s" % name,"I'd probably do that too.",False])
        $ text_message_screen_list.append(["Zoey","Tell me about it...",True])
    else:
        $ text_message_screen_list.append(["%s" % name,"You could try to turn the other cheek, maybe?",False])
        $ text_message_screen_list.append(["Zoey","Nah. That wouldn't work.",True])
else:
    $ text_message_screen_list.append(["Zoey","I just ignore him. It still annoys me, but I'm not gonna show him that I care. That would just give him some weird satisfaction.",True])
    if affinity == "DIK":
        $ text_message_screen_list.append(["%s" % name,"Yeah. Fuck him.",False])
        $ text_message_screen_list.append(["Zoey","Meh.",True])
    else:
        $ text_message_screen_list.append(["%s" % name,"I think that's a smart way of handling him.",False])
        $ text_message_screen_list.append(["Zoey","Yeah. Me too.",True])

$ text_message_screen_list.append(["%s" % name,"Halloween's tomorrow. I sent you the directions on Rooster.",False])
$ text_message_screen_list.append(["Zoey","Thanks, I just saw it. Sorry for the radio silence today. I was busy.",True])
if ep9_mad_at_zoey:
    $ text_message_screen_list.append(["%s" % name,"I'm used to it.",False])
    $ text_message_screen_list.append(["Zoey","Yeah... Anyway, I can't wait for tomorrow!",True])
else:
    $ text_message_screen_list.append(["%s" % name,"No need to apologize. We don't have to talk every day. What did you do?",False])
    $ text_message_screen_list.append(["Zoey","Mom said she could get me a temp job at the makeup store. I went with her to work to see how it's done.",True])
    if affinity == "DIK":
        $ text_message_screen_list.append(["%s" % name,"The makeup store? You? Haha! mphone_emoji_laugh",False])
        if zoey_dik:
            $ text_message_screen_list.append(["Zoey","Parallel universe Zoey, checking in. Look, I need to do something aside from climbing the walls of my room, skating, and sketching. This is better than nothing.",True])
        else:
            $ text_message_screen_list.append(["Zoey","What? I might not be a girly girl, but I use makeup.",True])
    else:
        $ text_message_screen_list.append(["%s" % name,"No way? That's nice of Alison. Do you think it will be fun?",False])
        if zoey_dik:
            $ text_message_screen_list.append(["Zoey","Uh... No? Look, I need to do something aside from climbing the walls of my room, skating, and sketching. This is better than nothing.",True])
        else:
            $ text_message_screen_list.append(["Zoey","Not so much. Definitely not compared to Tattoos.",True])

    $ text_message_screen_list.append(["Zoey","It would be like working the reception, but there's a lot more to it than just that.",True])
    $ text_message_screen_list.append(["%s" % name,"Tell me more about it.",False])
    $ text_message_screen_list.append(["Zoey","Yeah, I can bore you with it tomorrow, maybe?",True])
$ text_message_screen_list.append(["%s" % name,"Call me if you can't find the place.",False])

$ mphone_scene_to_chat("Zoey",text_message_screen_list)

if art_unlock_orders():
    $ new_chat_msg("Jacob",True,6)

$ new_chat_msg("Zoey",True,1)
$ new_chat_msg("Dad",True,2)
$ new_chat_msg("Elena",True,1)

if branchMayaJosy:
    $ new_chat_msg("Josy",False,1)
    $ new_chat_msg("Maya",False,1)
if branchJill:
    $ new_chat_msg("Jill",False,1)

$ disabled_apps = []
$ firstTimeFreeRoam = True
$ game_money_available = True
$ triple_tile_money_available = True
$ rooster_jump_label = "ep9_diks_ph1_lib_mid_label"

$ map_system_list = []
$ map_system_list.append(["ep9_diks_ph1_lib_mid","ep9_diks_ph1_lib_mid_label","Your room"])
$ map_system_list.append(["ep9_diks_ph1_derek","ep9_diks_ph1_derek_label","Derek's room"])
$ map_system_list.append(["ep9_diks_ph1_dining","ep9_diks_ph1_dining_label","Dining room"])
$ map_system_list.append(["ep9_diks_ph1_jacob","ep9_diks_ph1_jacob_label","Jacob's room"])
$ map_system_list.append(["ep9_diks_ph1_jamie","ep9_diks_ph1_jamie_label","Jamie's room"])
$ map_system_list.append(["ep9_diks_ph1_jb","ep9_diks_ph1_jb_label","John Boy's room"])
$ map_system_list.append(["ep9_diks_ph1_leon_room","ep9_diks_ph1_leon_room_label","Leon's room"])
$ map_system_list.append(["ep9_diks_ph1_main","ep9_diks_ph1_main_label","Main party room"])
$ map_system_list.append(["ep9_diks_ph1_nick","ep9_diks_ph1_nick_label","Nick's room"])
$ map_system_list.append(["ep9_diks_ph1_right_hall","ep9_diks_ph1_right_hall_label","Right hallway"])
$ map_system_list.append(["ep9_diks_ph1_left_hall2","ep9_diks_ph1_left_hall2_label","Left hallway"])
$ map_system_list.append(["ep9_diks_ph1_rusty_room","ep9_diks_ph1_rusty_room_label","Rusty's room"])
$ map_system_list.append(["ep9_diks_ph1_tommy_room","ep9_diks_ph1_tommy_label","Tommy's room"])
$ map_system_list.append(["ep9_diks_ph1_ua","ep9_diks_ph1_ua_label","Upper main room"])

jump initRoosterLabel


label ep9_diks_ph1_lib_mid_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_lib_mid_label"
scene ep9_diks_ph1_lib_mid with dissolve
if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    if persistent.mod_wtenabled:
        $ task_list = ["Find your sword (Dining Room)","Talk to Jamie (Main Party room)","Talk to Sally (Derek's Room)","Talk to Rusty (Upper main room)","","","",""]
    else:
        $ task_list = ["Find your sword","Talk to Jamie","Talk to Sally","Talk to Rusty","","","",""]
    if swyper_rejected_by_ida:
        $ task_list[6] = "Talk to the group outside your room"

    if persistent.mod_wtenabled:
        $ optional_task_list = ["","","","Talk to Zoey (Main Party room)","Talk to Derek (Upper main room)","Talk to the girls (Main Party room upstairs)"]
    else:
        $ optional_task_list = ["","","","Talk to Zoey","Talk to Derek","Talk to the girls"]
    if branchMayaJosy:
        $ optional_task_list[0] = "Text Maya"
        $ optional_task_list[1] = "Text Josy"
    if branchJill:
        $ optional_task_list[2] = "Text Jill"

    $ updateTaskList()
    $ chat_new_tasks = True
    $ event_list = []
    $ event_list.append("ep9_diks_ph1_tommy_event_label")
    $ event_list.append("ep9_diks_ph1_jamie_event_label")
    $ event_list.append("ep9_diks_ph1_zoey_event_label")
    $ event_list.append("ep9_diks_ph1_dormies_event_label")
    $ event_list.append("ep9_diks_ph1_girls_event_label")
    $ event_list.append("ep9_diks_ph1_sally_event_label")
    $ event_list.append("ep9_diks_ph1_movie_event_label")
    $ event_list.append("ep9_diks_ph1_rusty_event_label")
    $ event_list.append("ep9_diks_ph1_derek_event_label")
    $ event_list.append("ep9_diks_ph1_sword_event_label")
    if swyper_rejected_by_ida:
        $ event_list.append("ep9_diks_ph1_santa_event_label")

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

$ ui.imagebutton("ep9_diks_ph1_lib_mid_pumpkin_idle", "ep9_diks_ph1_lib_mid_pumpkin_hover", clicked=ui.returns("pumpkin"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_bella_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_lib_mid_window_idle", "ep9_diks_ph1_lib_mid_window_hover", clicked=ui.returns("window"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph1_lib_left_label
elif result == "go_right":
    jump ep9_diks_ph1_lib_right_label
elif result == "pumpkin":
    mc "(Maybe I was a bit lazy with the decor in here, but it doesn't matter. The party's out there, and I did more than most DIKs with my room.)"
    jump ep9_diks_ph1_lib_mid_label
elif result == "window":
    if current_task != "Wait for Bella by your window" or ("ep9_diks_ph1_keg2_event_label" in event_list or "ep9_diks_ph1_tap_event_label" in event_list or "ep9_diks_ph1_keg_event_label" in event_list):
        mc "(She's not here yet. I have time to set up the keg Tommy asked me to.)"
        jump ep9_diks_ph1_lib_mid_label
    $ currentEvent = "ep9_diks_ph1_end_event_label"
    jump startEvent
    label ep9_diks_ph1_end_event_label:
    menu:
        "End free roam":
            $ phone_clear_jump_label = "ep9_bella_branch_label"
            stop music fadeout 3
            jump end_freeroam
        "Not yet":
            $ renpy.pause(0.5)
    jump endEvent

label ep9_diks_ph1_lib_left_label:
scene ep9_diks_ph1_lib_left with dissolve
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_lib_left_label"

$ ui.imagebutton("ep9_diks_ph1_lib_desk_idle", "ep9_diks_ph1_lib_desk_hover", clicked=ui.returns("desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_right":
    jump ep9_diks_ph1_lib_mid_label
elif result == "desk":
    jump ep9_final_diks2_library_desk_label

label ep9_final_diks2_library_desk_label:
image ep9_freeroam_diks_library_desk = "ep8_freeroam_diks_library_desk[ep7_current_desk_painting]"
image ep9_freeroam_diks_second_painting = "spr_second_painting[ep8_current_second_painting]"
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_final_diks2_library_desk_label"

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

if freeRoamID == "ep9_4":
    show spr_box_ep9
else:
    show ep8_box_spr
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

$ ui.imagebutton("ep8_gym_spr", "ep8_gym_spr", clicked=ui.returns("gym"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_wallet_spr", "ep7_wallet_spr_hover", clicked=ui.returns("wallet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_phone_spr2", "ep7_phone_spr2", clicked=ui.returns("phone"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_tabs_spr", "ep7_tabs_spr", clicked=ui.returns("tabs"), xpos=0, ypos=0, focus_mask=True)

if freeRoamID == "ep9_4":
    $ ui.imagebutton("spr_box_ep9", "spr_box_ep9", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep8_box_spr", "ep8_box_spr", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library3_frame_idle", "ep7_freeroam_diks_library3_frame_hover", clicked=ui.returns("frame"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep7_freeroam_diks_library_desk_study_idle", "ep7_freeroam_diks_library_desk_study_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down_short", "fr_go_down_short", clicked=ui.returns("go_down"), xpos=500 * persistent.scale_factor, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    if freeRoamID == "ep9_1":
        jump ep9_diks_ph1_lib_left_label
    elif freeRoamID == "ep9_2":
        jump ep9_diks_ph2_lib_left_label
    else:
        jump ep9_diks_ph3_lib_left_label
elif result == "box":
    mc "(I'll play with it some more later.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "second_painting":
    $ currentEvent = "ep9_choose_2nd_painting_label"
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
    jump ep9_final_diks2_library_desk_label
elif result  == "concert":
    show spr_concert_big
    $ ui.imagebutton("big_invis", "big_invis", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep9_final_diks2_library_desk_label
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
    jump ep9_final_diks2_library_desk_label
elif result  == "leaf":
    mc "(It's a bit dry, but it should last as long as I don't touch it.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "cork":
    mc "(The wine cork from the bottle Bella and I shared at her place.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "triple_tile":
    mc "(They sent me a trophy for reaching turn 100 on normal difficulty in Triple Tile. It was pretty hard... Still, I can't believe I'm the first to do it.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "gym":
    mc "(My gym card. Yep. I'm a Silver member. The Gold membership was a bit too expensive. Besides, I'm not interested in attending their classes.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "helmet":
    if ep5_derekPoints != ep5_mcPoints:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] to [ep5_derekPoints].)"
    else:
        mc "(Hell Week... A weird and fun week where I got to know Derek. I'll always remember how I won that competition. [ep5_mcPoints] - [ep5_derekPoints], but the tiebreaker was mine.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "polaroid":
    mc "(The picture I took of Jill during our date...)"
    jump ep9_final_diks2_library_desk_label
elif result  == "tabs":
    mc "(The tabs I transcribed from Jill's piano song.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "phone":
    mc "(My old phone. It's always good to have a spare, but I hope I never have to use that one again.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "fakeid":
    mc "(My fake ID... Guess I'm a Texan... Born and bred.)"
    jump ep9_final_diks2_library_desk_label
elif result  == "vip":
    mc "(Hell yeah. My VIP pass to The Pink Rose. I worked hard for that.)"
    jump ep9_final_diks2_library_desk_label
elif result == "frame":
    $ currentEvent = "ep9_choose_painting_label"
    jump startEvent
elif result == "study":
    mc "(No studying tonight; it's a party, and classes after midterms haven't started yet.)"
    jump ep9_final_diks2_library_desk_label
elif result == "monkey":
    show spr_monkey_big
    mc "(Mom's monkey pose is fantastic. It makes it even better that her friends are taking the picture seriously.)"
    hide spr_monkey_big
    $ ui.imagebutton("spr_monkey_big", "spr_monkey_big", clicked=ui.returns("big_invis"), xpos=0, ypos=0)
    $ result = ui.interact()
    jump ep9_final_diks2_library_desk_label

label ep9_choose_painting_label:
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
    jump ep9_choose_painting_label
elif result == "left":
    if ep7_current_desk_painting == 0:
        $ ep7_current_desk_painting = 16
    else:
        $ ep7_current_desk_painting -= 1
    if ep7_current_desk_painting != 0:
        $ ep7_current_desk_painting = desk_check_unlocked_2d(ep7_current_desk_painting, False)
    jump ep9_choose_painting_label
else:
    $ currentFreeRoamLabel = "ep9_final_diks2_library_desk_label"
    jump endEvent

label ep9_choose_2nd_painting_label:
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
    jump ep9_choose_2nd_painting_label
elif result == "left":
    if ep8_current_second_painting == 0:
        $ ep8_current_second_painting = 19
    else:
        $ ep8_current_second_painting -= 1
    if ep8_current_second_painting != 0:
        $ ep8_current_second_painting = desk_check_second_unlocked_2d(ep8_current_second_painting, False)
    jump ep9_choose_2nd_painting_label
else:
    $ currentFreeRoamLabel = "ep9_final_diks2_library_desk_label"
    jump endEvent


label ep9_diks_ph1_lib_right_label:
if not persistent.ep9_cardjo8:
    scene ep9_diks_ph1_lib_right_card with dissolve
else:
    scene ep9_diks_ph1_lib_right with dissolve
label ep9_diks_ph1_lib_right_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_lib_right_label"

$ ui.imagebutton("ep9_diks_ph1_lib_right_camera_idle", "ep9_diks_ph1_lib_right_camera_hover", clicked=ui.returns("camera"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
if not persistent.ep9_cardjo8:
    $ ui.imagebutton("ep9_diks_ph1_lib_right_card_idle", "ep9_diks_ph1_lib_right_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_left":
    jump ep9_diks_ph1_lib_mid_label
elif result == "camera":
    mc "(That's Elena's camera and some school equipment. The HOTs wanted a place to take pictures of the guests, and Jacob got excited.)"
    mc "(One thing led to another, and now I have a photo studio in my room.)"
    jump ep9_diks_ph1_lib_right_label
elif result == "go_down":
    jump ep9_diks_ph1_right_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo8 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_lib_right with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_lib_right_label_nofx

label ep9_diks_ph1_main_label:
if "ep9_diks_ph1_keg2_event_label" in event_list:
    $ renpy.block_rollback()
    $ currentFreeRoamLabel = "ep9_diks_ph1_main_label"
    $ currentEvent = "ep9_diks_ph1_keg2_event_label"
    jump startEvent
if found_money:
    scene ep9_diks_ph1_main with dissolve
else:
    scene ep9_diks_ph1_main_money with dissolve

label ep9_diks_ph1_main_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_main_label"

if not found_money:
    $ ui.imagebutton("ep9_diks_ph1_main_money_idle", "ep9_diks_ph1_main_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_main_stairs_idle", "ep9_diks_ph1_main_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_main_door_idle", "ep9_diks_ph1_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_tommy_event_label" in event_list and task_list[4] != "":
    $ ui.imagebutton("ep9_diks_ph1_main_tommy_idle", "ep9_diks_ph1_main_tommy_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_zoey_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_main_zoey_idle", "ep9_diks_ph1_main_zoey_hover", clicked=ui.returns("zoey"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_jamie_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_main_jamie_idle", "ep9_diks_ph1_main_jamie_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_dormies_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_main_becky_idle", "ep9_diks_ph1_main_becky_hover", clicked=ui.returns("becky"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)

$ result = ui.interact()
if result == "stairs":
    jump ep9_diks_ph1_mainup_label
elif result == "go_down":
    jump ep9_diks_ph1_right_hall_label
elif result == "door":
    jump ep9_diks_ph1_left_hall2_label
elif result == "tommy":
    $ currentEvent = "ep9_diks_ph1_tommy_event_label"
    jump startEvent
elif result == "zoey":
    $ currentEvent = "ep9_diks_ph1_zoey_event_label"
    jump startEvent
elif result == "jamie":
    $ currentEvent = "ep9_diks_ph1_jamie_event_label"
    jump startEvent
elif result == "becky":
    $ currentEvent = "ep9_diks_ph1_dormies_event_label"
    jump startEvent
elif result == "money":
    show screen newmoneymsg
    $ found_money = True
    $ mny(dollar)
    scene ep9_diks_ph1_main with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep9_diks_ph1_main_label_nofx

label ep9_diks_ph1_mainup_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_mainup with dissolve

$ currentFreeRoamLabel = "ep9_diks_ph1_mainup_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_mainup_ldoor_idle", "ep9_diks_ph1_mainup_ldoor_hover", clicked=ui.returns("room"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_mainup_rdoor_idle", "ep9_diks_ph1_mainup_rdoor_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_girls_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_mainup_girls_idle", "ep9_diks_ph1_mainup_girls_hover", clicked=ui.returns("girls"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_main_label
elif result == "room":
    jump ep9_diks_ph1_ua_label
elif result == "leon":
    jump ep9_diks_ph1_leon_room_label
elif result == "girls":
    $ currentEvent = "ep9_diks_ph1_girls_event_label"
    jump startEvent

label ep9_diks_ph1_ua_label:
if not persistent.ep9_cardjo15:
    scene ep9_diks_ph1_ua_card with dissolve
else:
    scene ep9_diks_ph1_ua with dissolve

label ep9_diks_ph1_ua_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_ua_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_right"), xpos=1400 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=750 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
if "ep9_diks_ph1_rusty_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_ua_rusty_idle", "ep9_diks_ph1_ua_rusty_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardjo15:
    $ ui.imagebutton("ep9_diks_ph1_ua_card_idle", "ep9_diks_ph1_ua_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_mainup_label
elif result == "go_up":
    jump ep9_diks_ph1_1corr_label
elif result == "go_right":
    jump ep9_diks_ph1_2ua_label
elif result == "rusty":
    $ currentEvent = "ep9_diks_ph1_rusty_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo15 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_ua with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_ua_label_nofx

label ep9_diks_ph1_2ua_label:
if not persistent.ep9_cardjo1:
    scene ep9_diks_ph1_2ua_card with dissolve
else:
    scene ep9_diks_ph1_2ua with dissolve
label ep9_diks_ph1_2ua_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_2ua_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if "ep9_diks_ph1_derek_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_2ua_derek_idle", "ep9_diks_ph1_2ua_derek_hover", clicked=ui.returns("derek"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_2ua_ghost_idle", "ep9_diks_ph1_2ua_ghost_hover", clicked=ui.returns("ghost"), xpos=0, ypos=0, focus_mask=True)

if not persistent.ep9_cardjo1:
    $ ui.imagebutton("ep9_diks_ph1_2ua_card_idle", "ep9_diks_ph1_2ua_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_ua_label
elif result == "derek":
    $ currentEvent = "ep9_diks_ph1_derek_event_label"
    jump startEvent
elif result == "ghost":
    mc "(A scarecrow and a ghost. Whoever that is just put a sheet over them and painted black eyes on it. It's not the worst costume here, but it probably won't win the costume contest.)"
    jump ep9_diks_ph1_2ua_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo1 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_2ua with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_2ua_label_nofx

label ep9_diks_ph1_1corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_1corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph1_1corr_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_1corr_ldoor_idle", "ep9_diks_ph1_1corr_ldoor_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_1corr_rdoor_idle", "ep9_diks_ph1_1corr_rdoor_hover", clicked=ui.returns("janitor"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_2corr_label
elif result == "go_up":
    jump ep9_diks_ph1_toilet_2nd_label
elif result == "janitor":
    jump ep9_diks_ph1_derek_label
elif result == "go_left":
    jump ep9_diks_ph1_ua_label

label ep9_diks_ph1_2corr_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_2corr with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph1_2corr_label"
$ ui.imagebutton("ep9_diks_ph1_2corr_door_idle", "ep9_diks_ph1_2corr_door_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_1corr_label
elif result == "go_up":
    jump ep9_diks_ph1_jb_label
elif result == "go_right":
    jump ep9_diks_ph1_ua_label

label ep9_diks_ph1_derek_label:
$ renpy.block_rollback()
if "ep9_diks_ph1_end_event_label" in event_list and current_task == "Go to Derek's closet":
    $ currentEvent = "ep9_diks_ph1_end_event2_label"
    jump startEvent
    label ep9_diks_ph1_end_event2_label:
    menu:
        "End free roam":
            if branchJill:
                $ phone_clear_jump_label = "ep9_jill_branch_label"
            elif branchMayaJosy:
                stop music fadeout 3
                $ phone_clear_jump_label = "ep9_jm_branch_label"
            elif branchAlone:
                stop music fadeout 3
                $ phone_clear_jump_label = "ep9_others_branch_label"
            else:
                stop music fadeout 3
                $ phone_clear_jump_label = "ep9_sage_branch_label"
            jump end_freeroam
        "Not yet":
            $ renpy.pause(0.5)
    jump endEvent

$ currentFreeRoamLabel = "ep9_diks_ph1_derek_label"

if "ep9_diks_ph1_sally_event_label" in event_list or "ep9_diks_ph1_sally_event_label_pass" in event_list:
    scene ep9_diks_ph1_derek with dissolve
else:
    scene ep9_diks_ph1_2derek with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900 * persistent.scale_factor)
if "ep9_diks_ph1_sally_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_sally_idle", "ep9_diks_ph1_sally_hover", clicked=ui.returns("sally"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_1corr_label
elif result == "sally":
    $ currentEvent = "ep9_diks_ph1_sally_event_label"
    jump startEvent


label ep9_diks_ph1_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_left_hall2_label"

scene ep9_diks_ph1_left_hall2 with dissolve
$ ui.imagebutton("ep9_diks_ph1_left_hall2_door_idle", "ep9_diks_ph1_left_hall2_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_left_hall2_stairs_idle", "ep9_diks_ph1_left_hall2_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_leon_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_left_hall2_leon_idle", "ep9_diks_ph1_left_hall2_leon_hover", clicked=ui.returns("leon"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1300 * persistent.scale_factor, ypos=450 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_right":
    jump ep9_diks_ph1_main_label
elif result == "go_up":
    jump ep9_diks_ph1_left_hall_label
elif result == "stairs":
    jump ep9_diks_ph1_tommy_label
elif result == "leon":
    $ currentEvent = "ep9_diks_ph1_leon_event_label"
    jump startEvent
elif result == "door":
    mc "(We locked this door for the party. Jamie didn't want anyone to ruin his plants by pissing on them.)"
    jump ep9_diks_ph1_left_hall2_label

label ep9_diks_ph1_left_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_left_hall_label"

scene ep9_diks_ph1_left_hall with dissolve
$ ui.imagebutton("ep9_diks_ph1_left_hall_jdoor_idle", "ep9_diks_ph1_left_hall_jdoor_hover", clicked=ui.returns("jdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_left_hall_rdoor_idle", "ep9_diks_ph1_left_hall_rdoor_hover", clicked=ui.returns("rdoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_left_skeleton_idle", "ep9_diks_ph1_left_skeleton_hover", clicked=ui.returns("skeleton"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_left_hall2_label
elif result == "jdoor":
    jump ep9_diks_ph1_jamie_label
elif result == "rdoor":
    jump ep9_diks_ph1_rusty_room_label
elif result == "skeleton":
    mc "(Spooky!)"
    jump ep9_diks_ph1_left_hall_label

label ep9_diks_ph1_rusty_room_label:
if not persistent.ep9_cardjo10:
    scene ep9_diks_ph1_rusty_room_card with dissolve
else:
    scene ep9_diks_ph1_rusty_room with dissolve

label ep9_diks_ph1_rusty_room_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_rusty_room_label"
if not persistent.ep9_cardjo10:
    $ ui.imagebutton("ep9_diks_ph1_rusty_room_card_idle", "ep9_diks_ph1_rusty_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_door_idle", "ep9_diks_ph1_rusty_room_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_1_idle", "ep9_diks_ph1_rusty_room_1_hover", clicked=ui.returns("1"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_2_idle", "ep9_diks_ph1_rusty_room_2_hover", clicked=ui.returns("2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_3_idle", "ep9_diks_ph1_rusty_room_3_hover", clicked=ui.returns("3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_rusty_room_4_idle", "ep9_diks_ph1_rusty_room_4_hover", clicked=ui.returns("4"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_left_hall_label
elif result == "door":
    jump ep9_diks_ph1_dining_label
elif result == "1":
    scene ep9_diks_ph1_rusty_room1 with dissolve
    mc "(A murder mystery, eh? Tommy had a good idea for these decorations.)"
    mc "(The victim seems to be a male with a huge cock. So... There are two of us? Haha! Well, not anymore.)"
    jump ep9_diks_ph1_rusty_room_label
elif result == "2":
    scene ep9_diks_ph1_rusty_room2 with dissolve
    mc "(A gun shell? The murder weapon must be a gun.)"
    jump ep9_diks_ph1_rusty_room_label
elif result == "3":
    scene ep9_diks_ph1_rusty_room3 with dissolve
    mc "(Lipstick on the glass... But the first piece of evidence shows that the victim is male. Is the killer a female?)"
    jump ep9_diks_ph1_rusty_room_label
elif result == "4":
    scene ep9_diks_ph1_rusty_room4 with dissolve
    mc "(Hm, where is evidence number {color=#00ff00}4{/color}?)"
    mc "(Oh! There's something behind the cushion. A gun! The murder weapon?)"
    jump ep9_diks_ph1_rusty_room_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo10 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_rusty_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_rusty_room_label_nofx

label ep9_diks_ph1_right_hall_label:
$ renpy.block_rollback()
scene ep9_diks_ph1_right_hall with dissolve

$ currentFreeRoamLabel = "ep9_diks_ph1_right_hall_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_right_hall_kitchen_idle", "ep9_diks_ph1_right_hall_kitchen_hover", clicked=ui.returns("kitchen"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_right_hall_bathroom_idle", "ep9_diks_ph1_right_hall_bathroom_hover", clicked=ui.returns("bathroom"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("ep9_diks_ph1_right_hall_table_idle", "ep9_diks_ph1_right_hall_table_hover", clicked=ui.returns("table"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_right_hall_noose_idle", "ep9_diks_ph1_right_hall_noose_hover", clicked=ui.returns("noose"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_right_hall_theater_idle", "ep9_diks_ph1_right_hall_theater_hover", clicked=ui.returns("theater"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_right_hall_library_idle", "ep9_diks_ph1_right_hall_library_hover", clicked=ui.returns("library"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_santa_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_right_hall_santa_idle", "ep9_diks_ph1_right_hall_santa_hover", clicked=ui.returns("santa"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_main_label
elif result == "theater":
    jump ep9_diks_ph1_theater_label
elif result == "library":
    jump ep9_diks_ph1_lib_right_label
elif result == "kitchen":
    jump ep9_diks_ph1_kitchen_label
elif result == "table":
    mc "(Eyeballs, severed fingers, and pumpkin muffins. It sounds like a winning combination. And I don't care what the others say; to me, that looks like a small Christmas tree.)"
    jump ep9_diks_ph1_right_hall_label
elif result == "noose":
    mc "(It's kind of ironic. On any other day than today, that noose would be terrifying. And on the day it's supposed to be scary, it's not.)"
    jump ep9_diks_ph1_right_hall_label
elif result == "bathroom":
    jump ep9_diks_ph1_bathroom_label
elif result == "santa":
    $ currentEvent = "ep9_diks_ph1_santa_event_label"
    jump startEvent

label ep9_diks_ph1_theater_label:
if not persistent.ep9_cardjo11:
    scene ep9_diks_ph1_theater_card with dissolve
else:
    scene ep9_diks_ph1_theater with dissolve
label ep9_diks_ph1_theater_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_theater_label"

if "ep9_diks_ph1_movie_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_theater_gina_idle", "ep9_diks_ph1_theater_gina_hover", clicked=ui.returns("gina"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=200 * persistent.scale_factor, ypos=450 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not persistent.ep9_cardjo11:
    $ ui.imagebutton("ep9_diks_ph1_theater_card_idle", "ep9_diks_ph1_theater_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph1_theater2_label
elif result == "go_down":
    jump ep9_diks_ph1_right_hall_label
elif result == "gina":
    $ currentEvent = "ep9_diks_ph1_movie_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo11 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_theater with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_theater_label_nofx

label ep9_diks_ph1_theater2_label:
if found_money2:
    scene ep9_diks_ph1_theater2 with dissolve
else:
    scene ep9_diks_ph1_theater2_money with dissolve
label ep9_diks_ph1_theater2_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_theater2_label"

if not found_money2:
    $ ui.imagebutton("ep9_diks_ph1_theater2_money_idle", "ep9_diks_ph1_theater2_money_hover", clicked=ui.returns("money"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_left":
    jump ep9_diks_ph1_theater_label
elif result == "money":
    show screen newmoneymsg
    $ found_money2 = True
    $ mny(dollar)
    scene ep9_diks_ph1_theater2 with dissolve
    $ renpy.pause(3)
    hide screen newmoneymsg
    jump ep9_diks_ph1_theater2_label_nofx

label ep9_diks_ph1_leon_room_label:
if not persistent.ep9_cardjo7:
    scene ep9_diks_ph1_leon_room_card with dissolve
else:
    scene ep9_diks_ph1_leon_room with dissolve

label ep9_diks_ph1_leon_room_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_leon_room_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_leon_spider_idle", "ep9_diks_ph1_leon_spider_hover", clicked=ui.returns("spider"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_leon_chains_idle", "ep9_diks_ph1_leon_chains_hover", clicked=ui.returns("chains"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardjo7:
    $ ui.imagebutton("ep9_diks_ph1_leon_room_card_idle", "ep9_diks_ph1_leon_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_mainup_label
elif result == "spider":
    mc "(I'm not scared of spiders, but I would be if that thing were real.)"
    jump ep9_diks_ph1_leon_room_label
elif result == "chains":
    mc "(Are those Halloween props or used for other purposes?)"
    jump ep9_diks_ph1_leon_room_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo7 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_leon_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_leon_room_label_nofx

label ep9_diks_ph1_toilet_2nd_label:
if not persistent.ep9_cardjo12:
    scene ep9_diks_ph1_toilet_2nd_card with dissolve
else:
    scene ep9_diks_ph1_toilet_2nd with dissolve
label ep9_diks_ph1_toilet_2nd_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_toilet_2nd_label"

$ ui.imagebutton("ep9_diks_ph1_toilet_2nd_tub_idle", "ep9_diks_ph1_toilet_2nd_tub_hover", clicked=ui.returns("tub"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not persistent.ep9_cardjo12:
    $ ui.imagebutton("ep9_diks_ph1_toilet_2nd_card_idle", "ep9_diks_ph1_toilet_2nd_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_1corr_label
elif result == "tub":
    mc "(Disgusting and cool at the same time. I hope it's easy to clean up.)"
    jump ep9_diks_ph1_toilet_2nd_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo12 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_toilet_2nd with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_toilet_2nd_label_nofx

label ep9_diks_ph1_bathroom_label:
if not persistent.ep9_cardjo2:
    scene ep9_diks_ph1_bathroom_card with dissolve
else:
    scene ep9_diks_ph1_bathroom with dissolve
label ep9_diks_ph1_bathroom_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_bathroom_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_bathroom_skeleton_idle", "ep9_diks_ph1_bathroom_skeleton_hover", clicked=ui.returns("skeleton"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardjo2:
    $ ui.imagebutton("ep9_diks_ph1_bathroom_card_idle", "ep9_diks_ph1_bathroom_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_right_hall_label
elif result == "skeleton":
    mc "(We wanted to make the bathrooms extra scary. You're already in a bathroom, so it doesn't matter if you shit yourself. Haha!)"
    jump ep9_diks_ph1_bathroom_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo2 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_bathroom with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_bathroom_label_nofx

label ep9_diks_ph1_dining_label:
$ renpy.block_rollback()
if "ep9_diks_ph1_sword_event_label" in event_list:
    scene ep9_diks_ph1_dining_sword with dissolve
else:
    scene ep9_diks_ph1_dining with dissolve
$ currentFreeRoamLabel = "ep9_diks_ph1_dining_label"

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=280 * persistent.scale_factor, ypos=250 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_dining_stairs_idle", "ep9_diks_ph1_dining_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_dining_rdoor_idle", "ep9_diks_ph1_dining_rdoor_hover", clicked=ui.returns("rusty"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_dining_jdoor_idle", "ep9_diks_ph1_dining_jdoor_hover", clicked=ui.returns("jamie"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_dining_chips_idle", "ep9_diks_ph1_dining_chips_hover", clicked=ui.returns("chips"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_dining_pumpkin_idle", "ep9_diks_ph1_dining_pumpkin_hover", clicked=ui.returns("pumpkin"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_sword_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_dining_sword_idle", "ep9_diks_ph1_dining_sword_hover", clicked=ui.returns("sword"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_up":
    jump ep9_diks_ph1_kitchen_label
elif result == "stairs":
    jump ep9_diks_ph1_upper_2dining_label
elif result == "chips":
    mc "(I hope we got enough chips... Who would have thought it would be this hard to estimate how much food you need for a guest list that seems to expand by the hour?)"
    jump ep9_diks_ph1_dining_label
elif result == "pumpkin":
    mc "(And this is where we stopped giving a fuck about the decorations. It's more of a staging area anyway.)"
    mc "(Also, limiting the party is better than having people running around in every room.)"
    jump ep9_diks_ph1_dining_label
elif result == "rusty":
    jump ep9_diks_ph1_rusty_room_label
elif result == "jamie":
    jump ep9_diks_ph1_jamie_label
elif result == "sword":
    $ currentEvent = "ep9_diks_ph1_sword_event_label"
    jump startEvent


label ep9_diks_ph1_upper_2dining_label:
if not persistent.ep9_cardjo16:
    scene ep9_diks_ph1_upper_2dining_card with dissolve
else:
    scene ep9_diks_ph1_upper_2dining with dissolve
label ep9_diks_ph1_upper_2dining_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_upper_2dining_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("stairs"), xpos=500 * persistent.scale_factor, ypos=750 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_jacob_idle", "ep9_diks_ph1_upper_2dining_jacob_hover", clicked=ui.returns("jacob"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_upper_2dining_nick_idle", "ep9_diks_ph1_upper_2dining_nick_hover", clicked=ui.returns("nick"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep9_cardjo16:
    $ ui.imagebutton("ep9_diks_ph1_upper_2dining_card_idle", "ep9_diks_ph1_upper_2dining_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_jb_label
elif result == "stairs":
    jump ep9_diks_ph1_dining_label
elif result == "nick":
    jump ep9_diks_ph1_nick_label
elif result == "jacob":
    jump ep9_diks_ph1_jacob_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo16 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_upper_2dining with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_upper_2dining_label_nofx

label ep9_diks_ph1_kitchen_label:
if not persistent.ep9_cardjo6:
    scene ep9_diks_ph1_kitchen_card with dissolve
else:
    scene ep9_diks_ph1_kitchen with dissolve
label ep9_diks_ph1_kitchen_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_kitchen_label"

$ ui.imagebutton("ep9_diks_ph1_kitchen_popcorn_idle", "ep9_diks_ph1_kitchen_popcorn_hover", clicked=ui.returns("popcorn"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_kitchen_beer_idle", "ep9_diks_ph1_kitchen_beer_hover", clicked=ui.returns("beer"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

if not persistent.ep9_cardjo6:
    $ ui.imagebutton("ep9_diks_ph1_kitchen_card_idle", "ep9_diks_ph1_kitchen_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_dining_label
elif result == "go_right":
    jump ep9_diks_ph1_right_hall_label
elif result == "popcorn":
    mc "(Every party needs food and snacks. Popcorn is both cheap and easy to make.)"
    mc "(Someone made the point it was healthy too, but if you're {b}that{/b} concerned about your health, you shouldn't even be drinking.)"
    jump ep9_diks_ph1_kitchen_label
elif result == "beer":
    mc "(We've ordered a lot of alcohol for tonight. At a glance, it seems like an excessive amount, but I trust that Rusty knows what he's doing by now.)"
    jump ep9_diks_ph1_kitchen_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo6 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_kitchen with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_kitchen_label_nofx

label ep9_diks_ph1_jb_label:
if not persistent.ep9_cardjo5:
    scene ep9_diks_ph1_jb_card with dissolve
else:
    scene ep9_diks_ph1_jb with dissolve

label ep9_diks_ph1_jb_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_jb_label"

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=500 * persistent.scale_factor, ypos=330 * persistent.scale_factor)
if not persistent.ep9_cardjo5:
    $ ui.imagebutton("ep9_diks_ph1_jb_card_idle", "ep9_diks_ph1_jb_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_1corr_label
elif result == "go_up":
    jump ep9_diks_ph1_upper_2dining_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo5 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_jb with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_jb_label_nofx

label ep9_diks_ph1_nick_label:
if not persistent.ep9_cardjo9:
    if "ep9_diks_ph1_tap_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_nick_tap_card with dissolve
    else:
        scene ep9_diks_ph1_nick_card with dissolve
else:
    if "ep9_diks_ph1_tap_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_nick_tap with dissolve
    else:
        scene ep9_diks_ph1_nick with dissolve

label ep9_diks_ph1_nick_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_nick_label"

$ ui.imagebutton("ep9_diks_ph1_nick_boxes_idle", "ep9_diks_ph1_nick_boxes_hover", clicked=ui.returns("box"), xpos=0, ypos=0, focus_mask=True)
if "ep9_diks_ph1_tap_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_nick_tap_idle", "ep9_diks_ph1_nick_tap_hover", clicked=ui.returns("tap"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_nick_boxes2_idle", "ep9_diks_ph1_nick_boxes2_hover", clicked=ui.returns("box2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

if not persistent.ep9_cardjo9:
    $ ui.imagebutton("ep9_diks_ph1_nick_card_idle", "ep9_diks_ph1_nick_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()

if result == "go_down":
    jump ep9_diks_ph1_upper_2dining_label
elif result == "box":
    mc "(The HOTs and the DIKs already had a lot of decorations from previous years, but most of them were ruined and ended up not being nearly enough for this party.)"
    jump ep9_diks_ph1_nick_label
elif result == "box2":
    mc "(We ended up renting plenty of props for the party. I think that was a good call.)"
    jump ep9_diks_ph1_nick_label
elif result == "tap":
    $ currentEvent = "ep9_diks_ph1_tap_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo9 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep9_diks_ph1_tap_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_nick_tap with dissolve
    else:
        scene ep9_diks_ph1_nick with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_nick_label_nofx

label ep9_diks_ph1_jacob_label:
if not persistent.ep9_cardjo3:
    scene ep9_diks_ph1_jacob_card with dissolve
else:
    scene ep9_diks_ph1_jacob with dissolve
label ep9_diks_ph1_jacob_label_nofx:

$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_jacob_label"

$ ui.imagebutton("ep9_diks_ph1_jacob_art_idle", "ep9_diks_ph1_jacob_art_hover", clicked=ui.returns("art"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

if not persistent.ep9_cardjo3:
    $ ui.imagebutton("ep9_diks_ph1_jacob_card_idle", "ep9_diks_ph1_jacob_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_upper_2dining_label
elif result == "art":
    mc "(Another painting in the works. But there are no Halloween decorations in here. Jacob's been helping out a lot with the party, though.)"
    jump ep9_diks_ph1_jacob_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo3 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_jacob with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_jacob_label_nofx

label ep9_diks_ph1_tommy_label:
if not persistent.ep9_cardjo13:
    scene ep9_diks_ph1_tommy_room_card with dissolve
else:
    scene ep9_diks_ph1_tommy_room with dissolve
label ep9_diks_ph1_tommy_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_tommy_label"

$ ui.imagebutton("ep9_diks_ph1_tommy_tape_idle", "ep9_diks_ph1_tommy_tape_hover", clicked=ui.returns("tape"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_tommy_coffin_idle", "ep9_diks_ph1_tommy_coffin_hover", clicked=ui.returns("coffin"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_tommy_curtain_idle", "ep9_diks_ph1_tommy_curtain_hover", clicked=ui.returns("curtain"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not persistent.ep9_cardjo13:
    $ ui.imagebutton("ep9_diks_ph1_tommy_room_card_idle", "ep9_diks_ph1_tommy_room_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_left_hall2_label
elif result == "curtain":
    jump ep9_diks_ph1_tommy2_label
elif result == "tape":
    mc "(I don't get the idea behind putting police tape around the dance floor, but Tommy wanted it.)"
    jump ep9_diks_ph1_tommy_label
elif result == "coffin":
    mc "(I wonder if Tommy's gonna sleep in that coffin tonight.)"
    jump ep9_diks_ph1_tommy_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo13 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_tommy_room with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_tommy_label_nofx

label ep9_diks_ph1_tommy2_label:
if not persistent.ep9_cardjo14:
    if "ep9_diks_ph1_keg_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_tommy2_card with dissolve
    else:
        scene ep9_diks_ph1_tommy2_keg_card with dissolve
else:
    if "ep9_diks_ph1_keg_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_tommy2 with dissolve
    else:
        scene ep9_diks_ph1_tommy2_keg with dissolve

label ep9_diks_ph1_tommy2_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_tommy2_label"


if "ep9_diks_ph1_keg_event_label" in event_list:
    $ ui.imagebutton("ep9_diks_ph1_tommy2_keg_idle", "ep9_diks_ph1_tommy2_keg_hover", clicked=ui.returns("keg"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
if not persistent.ep9_cardjo14:
    $ ui.imagebutton("ep9_diks_ph1_tommy2_card_idle", "ep9_diks_ph1_tommy2_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_tommy_label
elif result == "keg":
    $ currentEvent = "ep9_diks_ph1_keg_event_label"
    jump startEvent
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo14 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    if "ep9_diks_ph1_keg_event_label" in event_list or "ep9_diks_ph1_tommy_event_label" in event_list:
        scene ep9_diks_ph1_tommy2 with dissolve
    else:
        scene ep9_diks_ph1_tommy2_keg with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_tommy2_label_nofx

label ep9_diks_ph1_jamie_label:
if not persistent.ep9_cardjo4:
    scene ep9_diks_ph1_jamie_card with dissolve
else:
    scene ep9_diks_ph1_jamie with dissolve

label ep9_diks_ph1_jamie_label_nofx:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_diks_ph1_jamie_label"


$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("ep9_diks_ph1_jamie_pumpkin_idle", "ep9_diks_ph1_jamie_pumpkin_hover", clicked=ui.returns("pumpkin"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_diks_ph1_jamie_door_idle", "ep9_diks_ph1_jamie_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)

if not persistent.ep9_cardjo4:
    $ ui.imagebutton("ep9_diks_ph1_jamie_card_idle", "ep9_diks_ph1_jamie_card_hover", clicked=ui.returns("hidden_card"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "go_down":
    jump ep9_diks_ph1_left_hall_label
elif result == "pumpkin":
    mc "(I gotta hand it to Jamie. His room always feels cozy. It's probably because of the plants.)"
    jump ep9_diks_ph1_jamie_label
elif result == "door":
    jump ep9_diks_ph1_dining_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep9_cardjo4 = True
    $ persistent.rew_josy_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    scene ep9_diks_ph1_jamie with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep9_diks_ph1_jamie_label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label ep11_freeroam_cabin_label:
$ freeRoamID = "ep11_3"
$ roosterState = "ep11_3"
$ tmpInt = 0
$ guideSuggestedPage = 177

show screen wt_tasks_shown
$ disabled_apps = ["music","brawler","tripletile","shuffle","vault"]
$ firstTimeFreeRoam = True
$ game_money_available = True
$ triple_tile_money_available = True

$ rooster_jump_label = "ep11_fr_cabin_main_label"
jump initRoosterLabel

label ep11_fr_cabin_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_main_label"
if "ep11_cabin_sauna_event_label" in event_list:
    $ currentEvent = "ep11_cabin_sauna_event_label"
    jump startEvent
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
scene ep11_fr_cabin_main with dissolve

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False
    $ current_task = ""
    $ task_list = ["Talk to Bella","Talk to Jill","Talk to Bianca",""]
    $ optional_task_list = [""]

    $ chat_new_tasks = True
    $ event_list = []

    $ event_list.append("ep11_cabin_bella_event_label")
    $ event_list.append("ep11_cabin_jill_event_label")
    $ event_list.append("ep11_cabin_bianca_event_label")


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

if "ep11_cabin_jill_event_label" in event_list:
    $ ui.imagebutton("ep11_fr_cabin_main_jill_idle", "ep11_fr_cabin_main_jill_hover", clicked=ui.returns("jill"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    jump ep11_fr_cabin_hall_label
elif result == "jill":
    $ currentEvent = "ep11_cabin_jill_event_label"
    jump startEvent


label ep11_fr_cabin_kitchen_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_kitchen_label"
scene ep11_fr_cabin_kitchen with dissolve

if "ep11_cabin_bella_event_label" in event_list:
    $ ui.imagebutton("ep11_fr_cabin_main_bella_idle", "ep11_fr_cabin_main_bella_hover", clicked=ui.returns("bella"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_left", "fr_go_left", clicked=ui.returns("go_left"), xpos=20 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_left":
    jump ep11_fr_cabin_hall_label
elif result == "bella":
    $ currentEvent = "ep11_cabin_bella_event_label"
    jump startEvent

label ep11_fr_cabin_hall_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_hall_label"
scene ep11_fr_cabin_hall
hide screen ep10_snow_screen
with dissolve

$ ui.imagebutton("ep11_fr_cabin_stairs_idle", "ep11_fr_cabin_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=1000 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ ui.imagebutton("ep11_fr_cabin_ldoor_idle", "ep11_fr_cabin_ldoor_hover", clicked=ui.returns("ldoor"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ ui.imagebutton("fr_go_right", "fr_go_right", clicked=ui.returns("go_right"), xpos=1690 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_fr_cabin_outside1_label
elif result == "stairs":
    jump ep11_fr_cabin_br2_label
elif result == "go_up":
    jump ep11_fr_cabin_kitchen_label
elif result == "ldoor":
    jump ep11_fr_cabin_br1_label
elif result == "go_right":
    jump ep11_fr_cabin_main_label

label ep11_fr_cabin_br2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_br2_label"
scene ep11_fr_cabin_br2 with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_fr_cabin_hall_label


label ep11_fr_cabin_toilet_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_toilet_label"
scene ep11_fr_cabin_toilet with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_fr_cabin_hall_label

label ep11_fr_cabin_br1_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_br1_label"
scene ep11_fr_cabin_br1 with dissolve

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_fr_cabin_hall_label

label ep11_fr_cabin_outside1_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_outside1_label"

scene ep11_fr_cabin_outside1
show screen ep10_snow_screen
with dissolve

if "ep11_cabin_bianca_event_label" in event_list:
    $ ui.imagebutton("ep11_fr_cabin_main_bianca_idle", "ep11_fr_cabin_main_bianca_hover", clicked=ui.returns("bianca"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep11_fr_cabin_door_idle", "ep11_fr_cabin_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=420 * persistent.scale_factor, ypos=250 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_up":
    jump ep11_fr_cabin_outside2_label
elif result == "door":
    jump ep11_fr_cabin_hall_label
elif result == "bianca":
    $ currentEvent = "ep11_cabin_bianca_event_label"
    jump startEvent

label ep11_fr_cabin_outside2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep11_fr_cabin_outside2_label"

scene ep11_fr_cabin_outside2 with dissolve

$ ui.imagebutton("ep11_fr_cabin_pool_idle", "ep11_fr_cabin_pool_hover", clicked=ui.returns("pool"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)

$ result = ui.interact()

if result == "go_down":
    jump ep11_fr_cabin_outside1_label
elif result == "pool":
    mc "(A nice hot pool surrounded by freezing snow.)"
    jump ep11_fr_cabin_outside2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

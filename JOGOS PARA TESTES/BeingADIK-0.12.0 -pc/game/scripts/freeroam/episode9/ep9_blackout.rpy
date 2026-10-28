label ep9_blackout_label:
$ freeRoamID = "ep9_3"

$ roosterState = "ep9_3"
$ tmpInt = 0
$ guideSuggestedPage = 72

$ disabled_apps = []
$ firstTimeFreeRoam = True

$ rooster_jump_label = "ep9_bo_ua_label"

$ map_system_list = []

jump initRoosterLabel

label ep9_bo_ua_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_bo_ua_label"

if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True
scene ep9_bo_ua

if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
if not persistent.fx_tip:
    $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
    show screen specialmsg
    pause
    hide screen specialmsg
    $ persistent.fx_tip = True

if firstTimeFreeRoam:
    hide screen new_phone_screen
    $ firstTimeFreeRoam = False

    $ event_list = []

    show screen freeroam_intro_screen("Task: Investigate the blackout.")
    $ renpy.pause()
    hide text
    hide white_screen
    hide screen freeroam_intro_screen

$ ui.imagebutton("fr_go_up_small_idle", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=750 * persistent.scale_factor, ypos=370 * persistent.scale_factor)
$ result = ui.interact()
if result == "go_up":
    jump ep9_bo_mainup_label

label ep9_bo_mainup_label:
$ renpy.block_rollback()
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True
scene ep9_bo_mainup
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve

$ currentFreeRoamLabel = "ep9_bo_mainup_label"

$ ui.imagebutton("ep9_bo_mainup_tommy_idle", "ep9_bo_mainup_tommy_hover", clicked=ui.returns("tommy"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "tommy":
    jump ep9_bo_tommy_event_label

label ep9_bo_main_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_bo_main_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True
scene ep9_bo_main
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
uk "I can't see anything!"
uk "Take my hand!"
uk "Everyone, get in here and stay still!"
uk "Muhahaha!"
uk "Stop, you're scaring me!"
uk "What's going on? Whose leg is that?"
mc "Please, don't panic! Stay where you are, and I'll have the lights on soon."
mc "(I hope...)"

$ ui.imagebutton("fr_go_up_small_idle", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=750 * persistent.scale_factor, ypos=370 * persistent.scale_factor)

$ result = ui.interact()
if result == "go_up":
    jump ep9_bo_left_hall2_label

label ep9_bo_left_hall2_label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_bo_left_hall2_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True
if branchIsabella:
    scene ep9_bo_left_hall2b
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
else:
    scene ep9_bo_left_hall2
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
play sound "sound_effects/running.mp3"
mc "Whoever that is, don't panic! Stay put while we fix the problem."
$ ui.imagebutton("ep9_diks_bo_stairs_idle", "ep9_diks_bo_stairs_hover", clicked=ui.returns("stairs"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "stairs":
    $ phone_clear_jump_label = "ep9_blackout2_label"
    jump end_freeroam

label ep9_bo_tommy_event_label:
scene ep9_bo_tommy_event1
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
tm "[name]? Is that you?"
scene ep9_bo_tommy_event2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "Yeah. What the fuck is going on?"
scene ep9_bo_tommy_event1
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
tm "I thought it was something scary you came up with."
scene ep9_bo_tommy_event2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "It's not. I think a fuse might have blown."
scene ep9_bo_tommy_event1
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
tm "I think the fuse box is in the basement near my room."
scene ep9_bo_tommy_event2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "You're not sure about that?"
scene ep9_bo_tommy_event3
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
tm "I'm not a fucking electrician. We never had a power outage."
scene ep9_bo_tommy_event2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "I don't know if I can fix it, but I'll take a look."
scene ep9_bo_tommy_event1
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
tm "Watch your step."
jump ep9_bo_main_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

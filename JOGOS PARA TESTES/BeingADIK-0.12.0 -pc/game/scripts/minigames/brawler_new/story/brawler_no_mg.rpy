label brawler_story_alex_fight_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_alex_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_alex_cpu_block with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_mc_power2a with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_alex_cpu_block2 with vpunch
$ renpy.pause(0.5)
scene brawler_alex_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/hit.mp3"
    $ tmpInt -= 1
    scene brawler_alex_cpu_punch3 with vpunch
    mc "Hngh..."
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_alex_cpu_dodge2 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_alex_mc_kick1 with hpunch
$ renpy.pause(0.5)
scene brawler_alex_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_mc_power2b with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_mc_power3a with vpunch
else:
    $ tmpInt -= 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_alex_cpu_special with hpunch
$ renpy.pause(0.5)
scene brawler_alex_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_alex_mc_block1 with vpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_alex_mc_dodge2 with hpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_mc_power4c with vpunch
$ renpy.pause(0.5)
scene brawler_alex_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_alex_mc_power1 with hpunch
elif result == "up":
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_cpu_power3 with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_alex_mc_block3 with hpunch
$ renpy.pause(0.5)
scene brawler_alex_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt -= 1
elif result == "up":
    $ tmpInt += 1
else:
    $ tmpInt += 1
if tmpInt > 2:
    $ bn_mc_won = True
    play sound "sound_effects/season3/bn_flurry.mp3"
    scene brawler_alex_flurry
    $ renpy.pause(3.0)
    scene brawler_alex_mc_rage
    $ renpy.pause(4)
    scene brawler_alex_mc_win with dissolve
    mc "That's how you do it!"
else:
    $ bn_mc_won = False
    play sound "sound_effects/hit.mp3"
    scene brawler_alex_cpu_punch3 with vpunch
    $ renpy.pause(0.5)
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_alex_cpu_special with hpunch
    $ renpy.pause(1)

show screen new_phone_screen
if bn_mc_won:
    jump brawler_story_alex_after0_label
else:
    jump brawler_story_alex_after0b_label

label brawler_story_troy_fight_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_troy_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_troy_mc_punch1 with hpunch
elif result == "up":
    play sound "sound_effects/shove.mp3"
    scene brawler_troy_cpu_block with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_troy_mc_punch3 with vpunch
$ renpy.pause(0.5)
scene brawler_troy_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_troy_cpu_dodge with vpunch
elif result == "up":
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_troy_cpu_punch1 with vpunch
    mc "Hngh..."
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_troy_mc_power2 with hpunch
$ renpy.pause(0.5)
scene brawler_troy_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_troy_mc_block2 with vpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_troy_mc_dodge1 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_troy_mc_power1 with hpunch
$ renpy.pause(0.5)
scene brawler_troy_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_troy_mc_power3a with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_troy_mc_power3b with hpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_troy_mc_block3 with vpunch
$ renpy.pause(0.5)
scene brawler_troy_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt -= 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_troy_cpu_power1 with hpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_troy_cpu_dodge3 with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_troy_mc_block4 with hpunch
$ renpy.pause(0.5)
scene brawler_troy_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
elif result == "up":
    $ tmpInt -= 1
else:
    $ tmpInt += 1
if tmpInt > 2:
    $ bn_mc_won = True
    scene brawler_troy_mc_rage
    $ renpy.pause(3)
else:
    $ bn_mc_won = False
    scene brawler_troy_cpu_special
    $ renpy.pause(2)
show screen new_phone_screen
jump brawler_story_troy_after0_label

label brawler_story_dwyane_fight_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_dwyane_neutral with dissolve
$renpy.notify("UP")

$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_dwyane_cpu_block with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_dwyane_mc_punch2 with hpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_dwyane_mc_punch1 with vpunch
$ renpy.pause(0.5)
scene brawler_dwyane_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_dwyane_cpu_punch1 with vpunch
    mc "Hngh..."
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_dwyane_cpu_dodge3 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_dwyane_mc_power2 with hpunch
$ renpy.pause(0.5)
scene brawler_dwyane_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_dwyane_mc_block2 with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_dwyane_mc_power1 with hpunch
else:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_dwyane_mc_dodge1 with vpunch
$ renpy.pause(0.5)
scene brawler_dwyane_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_dwyane_mc_block3 with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_dwyane_mc_power4b with hpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_dwyane_mc_power3a with vpunch
$ renpy.pause(0.5)
scene brawler_dwyane_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_dwyane_cpu_dodge3 with vpunch
elif result == "up":
    $ tmpInt -= 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_dwyane_cpu_power1 with hpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_dwyane_mc_block4 with hpunch
$ renpy.pause(1)
scene brawler_dwyane_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
elif result == "up":
    $ tmpInt += 1
else:
    $ tmpInt -= 1
if tmpInt > 2:
    $ bn_mc_won = True
    scene brawler_dwyane_mc_rage
    $ renpy.pause(3)
else:
    $ bn_mc_won = False
    scene brawler_dwyane_cpu_special
    $ renpy.pause(2)
show screen new_phone_screen
jump brawler_story_dwyane_after1_label

label brawler_story_johnny_fight_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_johnny_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()

if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_cpu_block with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_punch1 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_punch2 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()

if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
elif result == "up":
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_cpu_punch1 with vpunch
    mc "Hngh..."
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power2 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()

if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block2 with vpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_mc_dodge1 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power1 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()

if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power4b with hpunch
elif result == "up":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block3 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_power3a with vpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt -= 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_johnny_cpu_power1 with hpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block4 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
elif result == "up":
    $ tmpInt += 1
else:
    $ tmpInt -= 1
if tmpInt > 2:
    $ bn_mc_won = True
    scene brawler_johnny_mc_rage
    $ renpy.pause(3)
else:
    $ bn_mc_won = False
    scene brawler_johnny_cpu_special
    $ renpy.pause(2)
show screen new_phone_screen
jump ep12_fcomp_round1_end_label

label brawler_story_johnny_fight2_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power2 with hpunch
elif result == "up":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_cpu_block with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_punch2 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power2 with hpunch
else:
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_cpu_punch1 with vpunch
    mc "Hngh..."
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power1 with hpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_mc_dodge1 with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block2 with vpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("UP")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block3 with vpunch
elif result == "up":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_power3a with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power4b with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
elif result == "up":
    $ tmpInt -= 1
    play sound "sound_effects/season3/kick_body.mp3"
    scene brawler_johnny_cpu_power1 with hpunch
else:
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_cpu_power2 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
elif result == "up":
    $ tmpInt -= 1
else:
    $ tmpInt -= 1
if tmpInt > 2:
    $ bn_mc_won = True
else:
    $ bn_mc_won = False
show screen new_phone_screen
jump ep12_fcomp_round2_end_label

label brawler_story_johnny_fight3_nomg_label:
hide screen new_phone_screen
$ tmpInt = 0
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_power3a with vpunch
elif result == "up":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_cpu_block with vpunch
else:
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_cpu_block with vpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power2 with hpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
else:
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_cpu_punch1 with vpunch
    mc "Hngh..."
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("RIGHT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block2 with vpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_mc_dodge1 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power1 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_mc_power3a with vpunch
elif result == "up":
    play sound "sound_effects/shove.mp3"
    scene brawler_johnny_mc_block3 with vpunch
else:
    $ tmpInt += 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene brawler_johnny_mc_power4b with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
elif result == "up":
    play sound "sound_effects/whoosh.mp3"
    scene brawler_johnny_cpu_dodge3 with vpunch
else:
    $ tmpInt -= 1
    play sound "sound_effects/hit.mp3"
    scene brawler_johnny_cpu_power2 with hpunch
$ renpy.pause(1)
scene brawler_johnny_neutral with dissolve
$renpy.notify("LEFT")
$ ui.imagebutton("brawler_sparr_left_idle", "brawler_sparr_left_hover", clicked=ui.returns("left"), xpos=70 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_up_idle", "brawler_sparr_up_hover", clicked=ui.returns("up"), xpos=830 * persistent.scale_factor, ypos=400 * persistent.scale_factor)
$ ui.imagebutton("brawler_sparr_right_idle", "brawler_sparr_right_hover", clicked=ui.returns("right"), xpos=1500 * persistent.scale_factor, ypos=350 * persistent.scale_factor)
$ result = ui.interact()
if result == "left":
    $ tmpInt += 1
elif result == "up":
    $ tmpInt -= 1
else:
    $ tmpInt += 1
if tmpInt > 2:
    $ bn_mc_won = True
else:
    $ bn_mc_won = False
show screen new_phone_screen
jump ep12_fcomp_round3_end_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

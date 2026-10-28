
label brawler_pov_nerd_neutral_label:
scene brawler_nerd_neutral
if pov_neutral_mode == 0:
    jump pov_neutral2_label
else:
    jump pov_block2_label

label brawler_pov_prep_neutral_label:
scene brawler_prep_neutral
if pov_neutral_mode == 0:
    jump pov_neutral2_label
else:
    jump pov_block2_label

label brawler_pov_jock_neutral_label:
scene brawler_jock_neutral
if pov_neutral_mode == 0:
    jump pov_neutral2_label
else:
    jump pov_block2_label



label brawler_nerd_win_label:
scene brawler_nerd_win
jump pov_fight_done2

label brawler_prep_win_label:
scene brawler_prep_win
jump pov_fight_done2

label brawler_jock_win_label:
scene brawler_jock_win
jump pov_fight_done2


label brawler_nerd_lose_label:
scene brawler_nerd_lose
jump pov_fight_done3

label brawler_prep_lose_label:
scene brawler_prep_lose
jump pov_fight_done3

label brawler_jock_lose_label:
scene brawler_jock_lose
jump pov_fight_done3



label brawler_pov_nerd_hits_you_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage == 0:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_kick1 with hpunch
elif randomImage == 1:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_kick2 with hpunch
elif randomImage == 2:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_punch1 with hpunch
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_punch2 with hpunch

jump pov_mc_got_hit2_label

label brawler_pov_prep_hits_you_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage == 0:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_kick1 with hpunch
elif randomImage == 1:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_kick2 with hpunch
elif randomImage == 2:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_punch1 with hpunch
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_punch2 with hpunch

jump pov_mc_got_hit2_label

label brawler_pov_jock_hits_you_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage == 0:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_kick1a with hpunch
    $ renpy.pause(1)
    scene brawler_jock_kick1b
elif randomImage == 1:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_kick2 with hpunch
elif randomImage == 2:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_punch1 with hpunch
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_punch2 with hpunch

jump pov_mc_got_hit2_label


label brawler_pov_nerd_dodged_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage > 0:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_nerd_dodge with hpunch
    $ renpy.pause(1.5)
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_block with hpunch
    $ renpy.pause(1.5)
    jump pov_mc_got_hit_label
jump pov_decide_turn_label

label brawler_pov_prep_dodged_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage > 2:
    play sound "sound_effects/whoosh.mp3"
    $ randomImage2 = renpy.random.randint(0, 1)
    if randomImage2 == 0:
        scene brawler_prep_dodge with hpunch
    else:
        scene brawler_prep_dodge2 with hpunch
    $ renpy.pause(1.5)
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_block with hpunch
    $ renpy.pause(1.5)
    jump pov_mc_got_hit_label
jump pov_decide_turn_label

label brawler_pov_jock_dodged_label:
$ randomImage = renpy.random.randint(0, 3)
if randomImage > 2:
    play sound "sound_effects/whoosh.mp3"
    $ randomImage2 = renpy.random.randint(0, 1)
    if randomImage2 == 0:
        scene brawler_jock_dodge with hpunch
    else:
        scene brawler_jock_dodge2 with hpunch
    $ renpy.pause(1.5)
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_block with hpunch
    $ renpy.pause(1.5)
    jump pov_mc_got_hit_label
jump pov_decide_turn_label



label brawler_pov_nerd_mc_hit_label:
play sound "sound_effects/hit.mp3"
if pov_attack_multiplier < 10:
    $ randomImage = renpy.random.randint(0, 1)
elif pov_attack_multiplier == 12:
    $ randomImage = 3
else:
    $ randomImage = renpy.random.randint(0, 2)

if randomImage == 0:
    scene brawler_nerd_mc_punch1 with hpunch
elif randomImage == 1:
    scene brawler_nerd_mc_punch2 with hpunch
elif randomImage == 2:
    scene brawler_nerd_mc_kick1a with hpunch
    $ renpy.pause(1)
    scene brawler_nerd_mc_kick1b
elif randomImage == 3:
    scene brawler_nerd_mc_kick2a with hpunch
    $ renpy.pause(1)
    scene brawler_nerd_mc_kick2b
jump pov_mc_hit2_label

label brawler_pov_prep_mc_hit_label:
play sound "sound_effects/hit.mp3"
if pov_attack_multiplier < 10:
    $ randomImage = renpy.random.randint(0, 1)
elif pov_attack_multiplier == 12:
    $ randomImage = 3
else:
    $ randomImage = renpy.random.randint(0, 2)

if randomImage == 0:
    scene brawler_prep_mc_punch1 with hpunch
elif randomImage == 1:
    scene brawler_prep_mc_punch2 with hpunch
elif randomImage == 2:
    scene brawler_prep_mc_kick1 with hpunch
elif randomImage == 3:
    scene brawler_prep_mc_kick2 with hpunch
jump pov_mc_hit2_label

label brawler_pov_jock_mc_hit_label:
play sound "sound_effects/hit.mp3"
if pov_attack_multiplier < 10:
    $ randomImage = renpy.random.randint(0, 1)
elif pov_attack_multiplier == 12:
    $ randomImage = 3
else:
    $ randomImage = renpy.random.randint(0, 2)

if randomImage == 0:
    scene brawler_jock_mc_punch1 with hpunch
elif randomImage == 1:
    scene brawler_jock_mc_punch2 with hpunch
elif randomImage == 2:
    scene brawler_jock_mc_kick2 with hpunch
elif randomImage == 3:
    scene brawler_jock_mc_kick1a with hpunch
    $ renpy.pause(1)
    scene brawler_jock_mc_kick1b
jump pov_mc_hit2_label



label brawler_pov_nerd_mc_dodged_label:
$ randomImage = renpy.random.randint(0, 2)
if randomImage < 2:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_nerd_mc_dodge with hpunch
else:
    play sound "sound_effects/hit.mp3"
    scene brawler_nerd_mc_block with hpunch
    if sports_counter_skill:
        $ renpy.pause(1.5)
        if pov_cpu_special != 0:
            $ pov_cpu_special = 0
        $ pov_cpu_special_counter -= 1
        $ pov_attack_multiplier = 8
        play sound "sound_effects/hit.mp3"
        scene brawler_nerd_mc_punch2
        jump pov_mc_hit2_label
jump pov_mc_dodged2_label


label brawler_pov_prep_mc_dodged_label:
$ randomImage = renpy.random.randint(0, 2)
if randomImage == 0:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_prep_mc_dodge1 with hpunch
elif randomImage == 1:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_prep_mc_dodge2 with hpunch
elif randomImage == 2:
    play sound "sound_effects/hit.mp3"
    scene brawler_prep_mc_block with hpunch
    if sports_counter_skill:
        $ renpy.pause(1.5)
        if pov_cpu_special != 0:
            $ pov_cpu_special = 0
        $ pov_cpu_special_counter -= 1
        $ pov_attack_multiplier = 8
        play sound "sound_effects/hit.mp3"
        scene brawler_prep_mc_punch2
        jump pov_mc_hit2_label
jump pov_mc_dodged2_label


label brawler_pov_jock_mc_dodged_label:
$ randomImage = renpy.random.randint(0, 2)
if randomImage == 0:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_jock_mc_dodge1 with hpunch
elif randomImage == 1:
    play sound "sound_effects/whoosh.mp3"
    scene brawler_jock_mc_dodge2 with hpunch
elif randomImage == 2:
    play sound "sound_effects/hit.mp3"
    scene brawler_jock_mc_block with hpunch
    if sports_counter_skill:
        $ renpy.pause(1.5)
        if pov_cpu_special != 0:
            $ pov_cpu_special = 0
        $ pov_cpu_special_counter -= 1
        $ pov_attack_multiplier = 8
        play sound "sound_effects/hit.mp3"
        scene brawler_jock_mc_punch1
        jump pov_mc_hit2_label
jump pov_mc_dodged2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

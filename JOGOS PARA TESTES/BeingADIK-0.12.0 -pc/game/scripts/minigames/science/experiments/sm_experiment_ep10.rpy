label sm_setup_experiment_ep10_label:

$ sm_experiment_list = []
if sm_hard_mode:
    $ ms_time = 200 * (1.0 + 0.1*sm_perk_time + 0.05*sm_studied)
else:
    $ ms_time = 400 * (1.0 + 0.1*sm_perk_time + 0.05*sm_studied)

$ sm_studied = 0
$ sm_notes = [False,False,False,False,False,False,False,False,False]


$ tmpInt = renpy.random.randint(1, 3)
$ tmpInt2 = renpy.random.randint(1, 10) * 10

if tmpInt == 1:
    $ sm_experiment_list.append(["red",tmpInt2])
elif tmpInt == 2:
    $ sm_experiment_list.append(["green",tmpInt2])
else:
    $ sm_experiment_list.append(["blue",tmpInt2])


$ tmpInt = renpy.random.randint(1, 2)
$ tmpInt2 = renpy.random.randint(1, 10) * 10
if tmpInt == 1:
    $ sm_experiment_list.append(["red",tmpInt2])
else:
    $ sm_experiment_list.append(["blue",tmpInt2])


$ tmpInt = renpy.random.randint(1, 3)
if tmpInt == 1:
    $ sm_experiment_list.append(["slow",0])
elif tmpInt == 2:
    $ sm_experiment_list.append(["medium",1])
else:
    $ sm_experiment_list.append(["fast",2])


$ tmpInt = renpy.random.randint(1, 10) * 10
$ tmpInt2 = renpy.random.randint(1, 10) * 10
$ sm_experiment_list.append(["clear","green",tmpInt])
if sm_experiment_list[0][0] == "red":
    $ sm_experiment_list.append(["green","red",tmpInt2])
else:
    $ sm_experiment_list.append(["red","blue",tmpInt2])


$ tmpInt = renpy.random.randint(1, 3)
if tmpInt == 1:
    $ sm_experiment_list.append(["slow",0])
elif tmpInt == 2:
    $ sm_experiment_list.append(["medium",1])
else:
    $ sm_experiment_list.append(["fast",2])


$ tmpInt = renpy.random.randint(1, 10) * 10
$ tmpInt2 = renpy.random.randint(1, 10) * 10
$ sm_experiment_list.append(["green",tmpInt2])
$ sm_experiment_list.append(["blue",tmpInt])

show screen science_screen
show screen sm_timer_screen
show screen wt_science_cheat
$ renpy.pause()
jump science_game_end_ep10_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

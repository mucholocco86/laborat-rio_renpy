init -1 python:
    def play_clap_ep10(trans, st, at):
        renpy.play("sound_effects/season3/clap.mp3", "sfx3")
    def play_slap_ep10(trans, st, at):
        renpy.play("sound_effects/season3/slap2.mp3", "sfx3")

image bg anim_quinn_clap_ep10 movie:
    "anim_quinn_clap_ep10"
    function play_clap_ep10
    pause 2
    repeat


image anim_zombie_die_ep10 = Movie(play="%s/movies/ep10/anim_zombie_die_ep10.webm" % persistent.img_dir, start_image="anim_zombie_die_ep10_start", channel = "sex1", loop=False)
image bg anim_zombie_die_ep10 movie:
    "anim_zombie_die_ep10"
    pause 1.67
    "anim_zombie_die_ep10_end"
image anim_boss_ep10 = Movie(play="%s/movies/ep10/anim_boss_ep10.webm" % persistent.img_dir, start_image="anim_boss_ep10_start", channel = "sex2", loop=False)
image bg anim_boss_ep10 movie:
    "anim_boss_ep10"
    pause 2.33
    "anim_boss_ep10_end"

image anim_boss_idle_ep10 = Movie(play="%s/movies/ep10/anim_boss_idle_ep10.webm" % persistent.img_dir, start_image="anim_boss_idle_ep10_start", channel = "sex3", loop=False)
image bg anim_boss_idle_ep10 movie:
    "anim_boss_idle_ep10"
    pause 3.33
    "anim_boss_idle_ep10_end"

image anim_zombie_idle_ep10 = Movie(play="%s/movies/ep10/anim_zombie_idle_ep10.webm" % persistent.img_dir, start_image="anim_zombie_idle_ep10_start", channel = "sex4", loop=False)
image bg anim_zombie_idle_ep10 movie:
    "anim_zombie_idle_ep10"
    pause 10
    "anim_zombie_idle_ep10_end"

image anim_zombie_run_ep10 = Movie(play="%s/movies/ep10/anim_zombie_run_ep10.webm" % persistent.img_dir, start_image="anim_zombie_run_ep10_start", channel = "sex5", loop=False)
image bg anim_zombie_run_ep10 movie:
    "anim_zombie_run_ep10"
    pause 1.167
    "anim_zombie_run_ep10_end"

image anim_civilian_dead_ep10 = Movie(play="%s/movies/ep10/anim_civilian_dead_ep10.webm" % persistent.img_dir, start_image="anim_civilian_dead_ep10_start", channel = "sex6", loop=False)
image bg anim_civilian_dead_ep10 movie:
    "anim_civilian_dead_ep10"
    pause 2
    "anim_civilian_dead_ep10_end"

image anim_civilian_ep10 = Movie(play="%s/movies/ep10/anim_civilian_ep10.webm" % persistent.img_dir, start_image="anim_civilian_ep10_start", channel = "sex7", loop=False)
image bg anim_civilian_ep10 movie:
    "anim_civilian_ep10"
    pause 4.5
    "anim_civilian_ep10_end"

image anim_bbq_intro_ep10 = Movie(play="%s/movies/ep10/anim_bbq_intro_ep10.webm" % persistent.img_dir, start_image="anim_bbq_intro_ep10_start", channel = "sex1")
image anim_derek_fluff_ep10 = Movie(play="%s/movies/ep10/anim_derek_fluff_ep10.webm" % persistent.img_dir, start_image="anim_derek_fluff_ep10_start", channel = "sex2")
image anim_derek_tg_ep10 = Movie(play="%s/movies/ep10/anim_derek_tg_ep10.webm" % persistent.img_dir, start_image="anim_derek_tg_ep10_start", channel = "sex3")
image anim_derek_trip_ep10 = Movie(play="%s/movies/ep10/anim_derek_trip_ep10.webm" % persistent.img_dir, start_image="anim_derek_trip_ep10_start", channel = "sex4")
image anim_sally_stroke_ep10 = Movie(play="%s/movies/ep10/anim_sally_stroke_ep10.webm" % persistent.img_dir, start_image="anim_sally_stroke_ep10_start", channel = "sex5")
image anim_vibrator_ep10 = Movie(play="%s/movies/ep10/anim_vibrator_ep10.webm" % persistent.img_dir, start_image="anim_vibrator_ep10_start", channel = "sex6")
image anim_quinn_clap_ep10 = Movie(play="%s/movies/ep10/anim_quinn_clap_ep10.webm" % persistent.img_dir, start_image="anim_quinn_clap_ep10_start", channel = "sex7")
image anim_josy_pull_ep10 = Movie(play="%s/movies/ep10/anim_josy_pull_ep10.webm" % persistent.img_dir, start_image="anim_josy_pull_ep10_start", channel = "sex8", loop=False)
image bg anim_josy_pull_ep10 movie:
    "anim_josy_pull_ep10"
    pause 5
    "anim_josy_pull_ep10_end"
image anim_plug_jiggle_ep10 = Movie(play="%s/movies/ep10/anim_plug_jiggle_ep10.webm" % persistent.img_dir, start_image="anim_plug_jiggle_ep10_start", channel = "sex1")
image anim_wheelchair_ep10 = Movie(play="%s/movies/ep10/anim_wheelchair_ep10.webm" % persistent.img_dir, start_image="anim_wheelchair_ep10_start", channel = "sex2", loop=False)
image bg anim_wheelchair_ep10 movie:
    "anim_wheelchair_ep10"
    pause 3
    "anim_wheelchair_ep10_end"
image anim_yoga1_ep10 = Movie(play="%s/movies/ep10/anim_yoga1_ep10.webm" % persistent.img_dir, start_image="anim_yoga1_ep10_start", channel = "sex1", loop=False)
image bg anim_yoga1_ep10 movie:
    "anim_yoga1_ep10"
    pause 3
    "anim_yoga1_ep10_end"
image anim_bella_smartass_ep10 = Movie(play="%s/movies/ep10/anim_bella_smartass_ep10.webm" % persistent.img_dir, start_image="anim_bella_smartass_ep10_start", channel = "sex2", loop=False)
image bg anim_bella_smartass_ep10 movie:
    "anim_bella_smartass_ep10"
    pause 3
    "anim_bella_smartass_ep10_end"
image anim_tractor_beam_ep10 = Movie(play="%s/movies/ep10/anim_tractor_beam_ep10.webm" % persistent.img_dir, start_image="anim_tractor_beam_ep10_start", channel = "sex3", loop=False)
image bg anim_tractor_beam_ep10 movie:
    "anim_tractor_beam_ep10"
    pause 9.33
    "anim_tractor_beam_ep10_end"
image anim_zoey_run_ep10 = Movie(play="%s/movies/ep10/anim_zoey_run_ep10.webm" % persistent.img_dir, start_image="anim_zoey_run_ep10_start", channel = "sex4", loop=False)
image bg anim_zoey_run_ep10 movie:
    "anim_zoey_run_ep10"
    pause 26
    "anim_zoey_run_ep10_end"
image anim_failed_grab_ep10 = Movie(play="%s/movies/ep10/anim_failed_grab_ep10.webm" % persistent.img_dir, start_image="anim_failed_grab_ep10_start", channel = "sex5", loop=False)
image bg anim_failed_grab_ep10 movie:
    "anim_failed_grab_ep10"
    pause 2
    "anim_failed_grab_ep10_end"
image anim_success_grab_ep10 = Movie(play="%s/movies/ep10/anim_success_grab_ep10.webm" % persistent.img_dir, start_image="anim_success_grab_ep10_start", channel = "sex6", loop=False)
image bg anim_success_grab_ep10 movie:
    "anim_success_grab_ep10"
    pause 3
    "anim_success_grab_ep10_end"


image anim_bella_porn1_ep10 = Movie(play="%s/movies/ep10/anim_bella_porn1_ep10.webm" % persistent.img_dir, start_image="anim_bella_porn1_ep10_start", channel = "sex1")
image anim_bella_porn2_ep10 = Movie(play="%s/movies/ep10/anim_bella_porn2_ep10.webm" % persistent.img_dir, start_image="anim_bella_porn2_ep10_start", channel = "sex2")
image anim_bella_arm_ep10 = Movie(play="%s/movies/ep10/anim_bella_arm_ep10.webm" % persistent.img_dir, start_image="anim_bella_arm_ep10_start", channel = "sex3")
image anim_bella_hj_ep10 = Movie(play="%s/movies/ep10/anim_bella_hj_ep10.webm" % persistent.img_dir, start_image="anim_bella_hj_ep10_start", channel = "sex4")
image anim_bella_pan_ep10 = Movie(play="%s/movies/ep10/anim_bella_pan_ep10.webm" % persistent.img_dir,start_image="anim_bella_pan_ep10_start", channel = "sex5", loop=False)
image bg anim_bella_pan_ep10 movie:
    "anim_bella_pan_ep10"
    pause 20.367
    "anim_bella_pan_ep10_end"

image anim_bella_hj2_ep10 = Movie(play="%s/movies/ep10/anim_bella_hj2_ep10.webm" % persistent.img_dir, start_image="anim_bella_hj2_ep10_start", channel = "sex6")
image anim_bella_rub_ep10 = Movie(play="%s/movies/ep10/anim_bella_rub_ep10.webm" % persistent.img_dir, start_image="anim_bella_rub_ep10_start", channel = "sex7")

image anim_bella_anal1_ep10 = Movie(play="%s/movies/ep10/anim_bella_anal1_ep10.webm" % persistent.img_dir, start_image="anim_bella_anal1_ep10_start", channel = "sex8")
image anim_bella_anal2_ep10 = Movie(play="%s/movies/ep10/anim_bella_anal2_ep10.webm" % persistent.img_dir, start_image="anim_bella_anal2_ep10_start", channel = "sex9")
image anim_bella_anal3_ep10 = Movie(play="%s/movies/ep10/anim_bella_anal3_ep10.webm" % persistent.img_dir, start_image="anim_bella_anal3_ep10_start", channel = "sex10")
image anim_bella_anal4_ep10 = Movie(play="%s/movies/ep10/anim_bella_anal4_ep10.webm" % persistent.img_dir, start_image="anim_bella_anal4_ep10_start", channel = "sex11")
image anim_bella_beads_ep10 = Movie(play="%s/movies/ep10/anim_bella_beads_ep10.webm" % persistent.img_dir, start_image="anim_bella_beads_ep10_start", channel = "sex12", loop=False)
image bg anim_bella_beads_ep10 movie:
    "anim_bella_beads_ep10"
    pause 10
    "anim_bella_beads_ep10_end"
image anim_bella_beads2_ep10 = Movie(play="%s/movies/ep10/anim_bella_beads2_ep10.webm" % persistent.img_dir, start_image="anim_bella_beads_ep10_end", channel = "sex13", loop=False)
image bg anim_bella_beads2_ep10 movie:
    "anim_bella_beads2_ep10"
    pause 10
    "anim_bella_beads_ep10_start"
image anim_bella_below_anal1_ep10 = Movie(play="%s/movies/ep10/anim_bella_below_anal1_ep10.webm" % persistent.img_dir, start_image="anim_bella_below_anal1_ep10_start", channel = "sex14")
image anim_bella_below_anal2_ep10 = Movie(play="%s/movies/ep10/anim_bella_below_anal2_ep10.webm" % persistent.img_dir, start_image="anim_bella_below_anal2_ep10_start", channel = "sex15")
image anim_bella_bj1_ep10 = Movie(play="%s/movies/ep10/anim_bella_bj1_ep10.webm" % persistent.img_dir, start_image="anim_bella_bj1_ep10_start", channel = "sex16")
image anim_bella_boobjob1_ep10 = Movie(play="%s/movies/ep10/anim_bella_boobjob1_ep10.webm" % persistent.img_dir, start_image="anim_bella_boobjob1_ep10_start", channel = "sex17")
image anim_bella_boobjob2_ep10 = Movie(play="%s/movies/ep10/anim_bella_boobjob2_ep10.webm" % persistent.img_dir, start_image="anim_bella_boobjob2_ep10_start", channel = "sex18")
image anim_bella_boobs1_ep10 = Movie(play="%s/movies/ep10/anim_bella_boobs1_ep10.webm" % persistent.img_dir, start_image="anim_bella_boobs1_ep10_start", channel = "sex19")
image anim_bella_boobs2_ep10 = Movie(play="%s/movies/ep10/anim_bella_boobs2_ep10.webm" % persistent.img_dir, start_image="anim_bella_boobs2_ep10_start", channel = "sex20")
image anim_bella_cock_slap_ep10 = Movie(play="%s/movies/ep10/anim_bella_cock_slap_ep10.webm" % persistent.img_dir, start_image="anim_bella_cock_slap_ep10_start", channel = "sex1", loop=False)
image bg anim_bella_cock_slap_ep10 movie:
    "anim_bella_cock_slap_ep10"
    pause 0.8
    function play_slap_ep10
    pause 1.2
    "anim_bella_cock_slap_ep10_end"
image anim_bella_cum1_ep10 = Movie(play="%s/movies/ep10/anim_bella_cum1_ep10.webm" % persistent.img_dir, start_image="anim_bella_cum1_ep10_start", channel = "sex2")
image anim_bella_cunn1_ep10 = Movie(play="%s/movies/ep10/anim_bella_cunn1_ep10.webm" % persistent.img_dir, start_image="anim_bella_cunn1_ep10_start", channel = "sex3")
image anim_bella_doggy1_anal_ep10 = Movie(play="%s/movies/ep10/anim_bella_doggy1_anal_ep10.webm" % persistent.img_dir, start_image="anim_bella_doggy1_anal_ep10_start", channel = "sex4")
image anim_bella_grind1_ep10 = Movie(play="%s/movies/ep10/anim_bella_grind1_ep10.webm" % persistent.img_dir, start_image="anim_bella_grind1_ep10_start", channel = "sex5")
image anim_bella_grind2_ep10 = Movie(play="%s/movies/ep10/anim_bella_grind2_ep10.webm" % persistent.img_dir, start_image="anim_bella_grind2_ep10_start", channel = "sex6")
image anim_bella_hj_ep10 = Movie(play="%s/movies/ep10/anim_bella_hj_ep10.webm" % persistent.img_dir, start_image="anim_bella_hj_ep10_start", channel = "sex7")
image anim_bella_insert_ep10 = Movie(play="%s/movies/ep10/anim_bella_insert_ep10.webm" % persistent.img_dir,start_image="anim_bella_insert_ep10_start", channel = "sex8", loop=False)
image bg anim_bella_insert_ep10 movie:
    "anim_bella_insert_ep10"
    pause 10
    "anim_bella_insert_ep10_end"
image anim_bella_kiss_ep10 = Movie(play="%s/movies/ep10/anim_bella_kiss_ep10.webm" % persistent.img_dir, start_image="anim_bella_kiss_ep10_start", channel = "sex9")
image anim_bella_pile1_ep10 = Movie(play="%s/movies/ep10/anim_bella_pile1_ep10.webm" % persistent.img_dir, start_image="anim_bella_pile1_ep10_start", channel = "sex10")
image anim_bella_pile2_ep10 = Movie(play="%s/movies/ep10/anim_bella_pile2_ep10.webm" % persistent.img_dir, start_image="anim_bella_pile2_ep10_start", channel = "sex11")
image anim_bella_prone_ep10 = Movie(play="%s/movies/ep10/anim_bella_prone_ep10.webm" % persistent.img_dir, start_image="anim_bella_prone_ep10_start", channel = "sex12")
image anim_bella_prone2_ep10 = Movie(play="%s/movies/ep10/anim_bella_prone2_ep10.webm" % persistent.img_dir, start_image="anim_bella_prone2_ep10_start", channel = "sex13")
image anim_bella_ride1_anal_ep10 = Movie(play="%s/movies/ep10/anim_bella_ride1_anal_ep10.webm" % persistent.img_dir, start_image="anim_bella_ride1_anal_ep10_start", channel = "sex14")
image anim_bella_ride2_anal_ep10 = Movie(play="%s/movies/ep10/anim_bella_ride2_anal_ep10.webm" % persistent.img_dir, start_image="anim_bella_ride2_anal_ep10_start", channel = "sex15")
image anim_bella_ride3_anal_ep10 = Movie(play="%s/movies/ep10/anim_bella_ride3_anal_ep10.webm" % persistent.img_dir, start_image="anim_bella_ride3_anal_ep10_start", channel = "sex16")
image anim_bella_side_anal1_ep10 = Movie(play="%s/movies/ep10/anim_bella_side_anal1_ep10.webm" % persistent.img_dir, start_image="anim_bella_side_anal1_ep10_start", channel = "sex17")
image anim_bella_stand1_ep10 = Movie(play="%s/movies/ep10/anim_bella_stand1_ep10.webm" % persistent.img_dir, start_image="anim_bella_stand1_ep10_start", channel = "sex18")
image anim_bella_stand2_ep10 = Movie(play="%s/movies/ep10/anim_bella_stand2_ep10.webm" % persistent.img_dir, start_image="anim_bella_stand2_ep10_start", channel = "sex19")


image anim_cathy_cunn1_ep10 = Movie(play="%s/movies/ep10/anim_cathy_cunn1_ep10.webm" % persistent.img_dir, start_image="anim_cathy_cunn1_ep10_start", channel = "sex1")
image anim_cathy_cunn2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_cunn2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_cunn2_ep10_start", channel = "sex2")
image anim_cathy_bj_ep10 = Movie(play="%s/movies/ep10/anim_cathy_bj_ep10.webm" % persistent.img_dir, start_image="anim_cathy_bj_ep10_start", channel = "sex3")
image anim_cathy_cum_ep10 = Movie(play="%s/movies/ep10/anim_cathy_cum_ep10.webm" % persistent.img_dir, start_image="anim_cathy_cum_ep10_start", channel = "sex4")
image anim_cathy_cum2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_cum2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_cum2_ep10_start", channel = "sex3")
image anim_cathy_chair_ep10 = Movie(play="%s/movies/ep10/anim_cathy_chair_ep10.webm" % persistent.img_dir, start_image="anim_cathy_chair_ep10_start", channel = "sex6")
image anim_cathy_chair2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_chair2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_chair2_ep10_start", channel = "sex7")
image anim_cathy_doggy_ep10 = Movie(play="%s/movies/ep10/anim_cathy_doggy_ep10.webm" % persistent.img_dir, start_image="anim_cathy_doggy_ep10_start", channel = "sex8")
image anim_cathy_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_doggy2_ep10_start", channel = "sex9")
image anim_cathy_doggy3_ep10 = Movie(play="%s/movies/ep10/anim_cathy_doggy3_ep10.webm" % persistent.img_dir, start_image="anim_cathy_doggy3_ep10_start", channel = "sex10")

image bg anim_cathy_doggy_ep10 movie:
    "anim_cathy_doggy_ep10"
    pause 4.0
    function play_slap_ep10
    pause 2.667
    repeat
image bg anim_cathy_doggy2_ep10 movie:
    "anim_cathy_doggy2_ep10"
    pause 4.0
    function play_slap_ep10
    pause 2.667
    repeat
image bg anim_cathy_doggy3_ep10 movie:
    "anim_cathy_doggy3_ep10"
    pause 4.0
    function play_slap_ep10
    pause 2.667
    repeat

image anim_cathy_mast_ep10 = Movie(play="%s/movies/ep10/anim_cathy_mast_ep10.webm" % persistent.img_dir, start_image="anim_cathy_mast_ep10_start", channel = "sex11")
image anim_cathy_miss_ep10 = Movie(play="%s/movies/ep10/anim_cathy_miss_ep10.webm" % persistent.img_dir, start_image="anim_cathy_miss_ep10_start", channel = "sex12")
image anim_cathy_miss2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_miss2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_miss2_ep10_start", channel = "sex13")
image anim_cathy_miss3_ep10 = Movie(play="%s/movies/ep10/anim_cathy_miss3_ep10.webm" % persistent.img_dir, start_image="anim_cathy_miss3_ep10_start", channel = "sex14")
image anim_cathy_miss4_ep10 = Movie(play="%s/movies/ep10/anim_cathy_miss4_ep10.webm" % persistent.img_dir, start_image="anim_cathy_miss4_ep10_start", channel = "sex15")
image anim_cathy_ride_ep10 = Movie(play="%s/movies/ep10/anim_cathy_ride_ep10.webm" % persistent.img_dir, start_image="anim_cathy_ride_ep10_start", channel = "sex16")
image anim_cathy_ride2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_ride2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_ride2_ep10_start", channel = "sex17")
image anim_cathy_ride3_ep10 = Movie(play="%s/movies/ep10/anim_cathy_ride3_ep10.webm" % persistent.img_dir, start_image="anim_cathy_ride3_ep10_start", channel = "sex18")
image anim_cathy_wall_ep10 = Movie(play="%s/movies/ep10/anim_cathy_wall_ep10.webm" % persistent.img_dir, start_image="anim_cathy_wall_ep10_start", channel = "sex19")
image anim_cathy_wall2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_wall2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_wall2_ep10_start", channel = "sex20")
image anim_cathy_wall3_ep10 = Movie(play="%s/movies/ep10/anim_cathy_wall3_ep10.webm" % persistent.img_dir, start_image="anim_cathy_wall3_ep10_start", channel = "sex1")
image anim_cathy_wall4_ep10 = Movie(play="%s/movies/ep10/anim_cathy_wall4_ep10.webm" % persistent.img_dir, start_image="anim_cathy_wall4_ep10_start", channel = "sex2")
image anim_cathy_wall5_ep10 = Movie(play="%s/movies/ep10/anim_cathy_wall5_ep10.webm" % persistent.img_dir, start_image="anim_cathy_wall5_ep10_start", channel = "sex3")
image anim_cathy_prone_ep10 = Movie(play="%s/movies/ep10/anim_cathy_prone_ep10.webm" % persistent.img_dir, start_image="anim_cathy_prone_ep10_start", channel = "sex4")
image anim_cathy_prone2_ep10 = Movie(play="%s/movies/ep10/anim_cathy_prone2_ep10.webm" % persistent.img_dir, start_image="anim_cathy_prone2_ep10_start", channel = "sex5")

image anim_envy_kiss_ep10 = Movie(play="%s/movies/ep10/anim_envy_kiss_ep10.webm" % persistent.img_dir, start_image="anim_envy_kiss_ep10_start", channel = "sex1")
image anim_envy_lick_ep10 = Movie(play="%s/movies/ep10/anim_envy_lick_ep10.webm" % persistent.img_dir, start_image="anim_envy_lick_ep10_start", channel = "sex2")
image anim_envy_lick2_ep10 = Movie(play="%s/movies/ep10/anim_envy_lick2_ep10.webm" % persistent.img_dir, start_image="anim_envy_lick2_ep10_start", channel = "sex3")
image anim_envy_lick3_ep10 = Movie(play="%s/movies/ep10/anim_envy_lick3_ep10.webm" % persistent.img_dir, start_image="anim_envy_lick3_ep10_start", channel = "sex4")
image anim_envy_lick4_ep10 = Movie(play="%s/movies/ep10/anim_envy_lick4_ep10.webm" % persistent.img_dir, start_image="anim_envy_lick4_ep10_start", channel = "sex5")
image anim_envy_bj_ep10 = Movie(play="%s/movies/ep10/anim_envy_bj_ep10.webm" % persistent.img_dir, start_image="anim_envy_bj_ep10_start", channel = "sex6")
image anim_envy_bj2_ep10 = Movie(play="%s/movies/ep10/anim_envy_bj2_ep10.webm" % persistent.img_dir, start_image="anim_envy_bj2_ep10_start", channel = "sex7")
image anim_envy_bj3_ep10 = Movie(play="%s/movies/ep10/anim_envy_bj3_ep10.webm" % persistent.img_dir, start_image="anim_envy_bj3_ep10_start", channel = "sex8")
image anim_envy_below_ep10 = Movie(play="%s/movies/ep10/anim_envy_below_ep10.webm" % persistent.img_dir, start_image="anim_envy_below_ep10_start", channel = "sex9")
image anim_envy_below2_ep10 = Movie(play="%s/movies/ep10/anim_envy_below2_ep10.webm" % persistent.img_dir, start_image="anim_envy_below2_ep10_start", channel = "sex10")
image anim_envy_doggy_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy_ep10_start", channel = "sex11")
image anim_envy_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy2_ep10_start", channel = "sex12")
image anim_envy_doggy_anal_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy_anal_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy_anal_ep10_start", channel = "sex13")
image anim_envy_doggy_anal2_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy_anal2_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy_anal2_ep10_start", channel = "sex14")
image anim_envy_doggy_anal3_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy_anal3_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy_anal3_ep10_start", channel = "sex15")
image anim_envy_doggy_anal4_ep10 = Movie(play="%s/movies/ep10/anim_envy_doggy_anal4_ep10.webm" % persistent.img_dir, start_image="anim_envy_doggy_anal4_ep10_start", channel = "sex16")
image anim_envy_hug_ep10 = Movie(play="%s/movies/ep10/anim_envy_hug_ep10.webm" % persistent.img_dir, start_image="anim_envy_hug_ep10_start", channel = "sex17")
image anim_envy_hug2_ep10 = Movie(play="%s/movies/ep10/anim_envy_hug2_ep10.webm" % persistent.img_dir, start_image="anim_envy_hug2_ep10_start", channel = "sex18")
image anim_envy_rev_anal_ep10 = Movie(play="%s/movies/ep10/anim_envy_rev_anal_ep10.webm" % persistent.img_dir, start_image="anim_envy_rev_anal_ep10_start", channel = "sex19")
image anim_envy_rev2_anal_ep10 = Movie(play="%s/movies/ep10/anim_envy_rev2_anal_ep10.webm" % persistent.img_dir, start_image="anim_envy_rev2_anal_ep10_start", channel = "sex20")
image anim_envy_rev_ep10 = Movie(play="%s/movies/ep10/anim_envy_rev_ep10.webm" % persistent.img_dir, start_image="anim_envy_rev_ep10_start", channel = "sex1")
image anim_envy_rev2_ep10 = Movie(play="%s/movies/ep10/anim_envy_rev2_ep10.webm" % persistent.img_dir, start_image="anim_envy_rev2_ep10_start", channel = "sex2")
image anim_envy_miss_ep10 = Movie(play="%s/movies/ep10/anim_envy_miss_ep10.webm" % persistent.img_dir, start_image="anim_envy_miss_ep10_start", channel = "sex3")
image anim_envy_miss2_ep10 = Movie(play="%s/movies/ep10/anim_envy_miss2_ep10.webm" % persistent.img_dir, start_image="anim_envy_miss2_ep10_start", channel = "sex4")
image anim_envy_cum_ep10 = Movie(play="%s/movies/ep10/anim_envy_cum_ep10.webm" % persistent.img_dir, start_image="anim_envy_cum_ep10_start", channel = "sex5")
image anim_envy_cum2_ep10 = Movie(play="%s/movies/ep10/anim_envy_cum2_ep10.webm" % persistent.img_dir, start_image="anim_envy_cum2_ep10_start", channel = "sex6")



image anim_jill_assjob_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob_ep10_start", channel = "sex1")
image anim_jill_assjobb_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjobb_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjobb_ep10_start", channel = "sex2")
image anim_jill_assjob2_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob2_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob2_ep10_start", channel = "sex3")
image anim_jill_assjob3_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob3_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob3_ep10_start", channel = "sex4")
image anim_jill_assjob4_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob4_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob4_ep10_start", channel = "sex5")
image anim_jill_assjob5_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob5_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob5_ep10_start", channel = "sex6")
image anim_jill_assjob6_ep10 = Movie(play="%s/movies/ep10/anim_jill_assjob6_ep10.webm" % persistent.img_dir, start_image="anim_jill_assjob6_ep10_start", channel = "sex7")
image anim_jill_bj_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj_ep10_start", channel = "sex8")
image anim_jill_bj2_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj2_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj2_ep10_start", channel = "sex9")
image anim_jill_bj3_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj3_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj3_ep10_start", channel = "sex10")
image anim_jill_bj4_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj4_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj4_ep10_start", channel = "sex11")
image anim_jill_bj5_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj5_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj5_ep10_start", channel = "sex12")
image anim_jill_bj6_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj6_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj6_ep10_start", channel = "sex13")
image anim_jill_bj7_ep10 = Movie(play="%s/movies/ep10/anim_jill_bj7_ep10.webm" % persistent.img_dir, start_image="anim_jill_bj7_ep10_start", channel = "sex14")
image anim_jill_boobjob_cum_ep10 = Movie(play="%s/movies/ep10/anim_jill_boobjob_cum_ep10.webm" % persistent.img_dir, start_image="anim_jill_boobjob_cum_ep10_start", channel = "sex15")
image anim_jill_boobjob_ep10 = Movie(play="%s/movies/ep10/anim_jill_boobjob_ep10.webm" % persistent.img_dir, start_image="anim_jill_boobjob_ep10_start", channel = "sex16")
image anim_jill_boobjob2_ep10 = Movie(play="%s/movies/ep10/anim_jill_boobjob2_ep10.webm" % persistent.img_dir, start_image="anim_jill_boobjob2_ep10_start", channel = "sex17")
image anim_jill_boobjob3_ep10 = Movie(play="%s/movies/ep10/anim_jill_boobjob3_ep10.webm" % persistent.img_dir, start_image="anim_jill_boobjob3_ep10_start", channel = "sex18")
image anim_jill_cum1_ep10 = Movie(play="%s/movies/ep10/anim_jill_cum1_ep10.webm" % persistent.img_dir, start_image="anim_jill_cum1_ep10_start", channel = "sex19")
image anim_jill_cum2_ep10 = Movie(play="%s/movies/ep10/anim_jill_cum2_ep10.webm" % persistent.img_dir, start_image="anim_jill_cum2_ep10_start", channel = "sex20")
image anim_jill_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_jill_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_jill_doggy1_ep10_start", channel = "sex1")
image anim_jill_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_jill_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_jill_doggy2_ep10_start", channel = "sex2")
image anim_jill_hj_ep10 = Movie(play="%s/movies/ep10/anim_jill_hj_ep10.webm" % persistent.img_dir, start_image="anim_jill_hj_ep10_start", channel = "sex3")
image anim_jill_hj2_ep10 = Movie(play="%s/movies/ep10/anim_jill_hj2_ep10.webm" % persistent.img_dir, start_image="anim_jill_hj2_ep10_start", channel = "sex4")
image anim_jill_hj3_ep10 = Movie(play="%s/movies/ep10/anim_jill_hj3_ep10.webm" % persistent.img_dir, start_image="anim_jill_hj3_ep10_start", channel = "sex5")
image anim_jill_miss1_ep10 = Movie(play="%s/movies/ep10/anim_jill_miss1_ep10.webm" % persistent.img_dir, start_image="anim_jill_miss1_ep10_start", channel = "sex6")
image anim_jill_miss2_ep10 = Movie(play="%s/movies/ep10/anim_jill_miss2_ep10.webm" % persistent.img_dir, start_image="anim_jill_miss2_ep10_start", channel = "sex7")
image anim_jill_ride1_ep10 = Movie(play="%s/movies/ep10/anim_jill_ride1_ep10.webm" % persistent.img_dir, start_image="anim_jill_ride1_ep10_start", channel = "sex8")
image anim_jill_ride2_ep10 = Movie(play="%s/movies/ep10/anim_jill_ride2_ep10.webm" % persistent.img_dir, start_image="anim_jill_ride2_ep10_start", channel = "sex9")
image anim_jill_rub_ep10 = Movie(play="%s/movies/ep10/anim_jill_rub_ep10.webm" % persistent.img_dir, start_image="anim_jill_rub_ep10_start", channel = "sex10")
image anim_jill_rub2_ep10 = Movie(play="%s/movies/ep10/anim_jill_rub2_ep10.webm" % persistent.img_dir, start_image="anim_jill_rub2_ep10_start", channel = "sex11")
image anim_jill_rub3_ep10 = Movie(play="%s/movies/ep10/anim_jill_rub3_ep10.webm" % persistent.img_dir, start_image="anim_jill_rub3_ep10_start", channel = "sex12")
image anim_jill_stand1_ep10 = Movie(play="%s/movies/ep10/anim_jill_stand1_ep10.webm" % persistent.img_dir, start_image="anim_jill_stand1_ep10_start", channel = "sex13")
image anim_jill_stand2_ep10 = Movie(play="%s/movies/ep10/anim_jill_stand2_ep10.webm" % persistent.img_dir, start_image="anim_jill_stand2_ep10_start", channel = "sex14")
image anim_jill_wash_ep10 = Movie(play="%s/movies/ep10/anim_jill_wash_ep10.webm" % persistent.img_dir, start_image="anim_jill_wash_ep10_start", channel = "sex15")
image anim_jill_wash2_ep10 = Movie(play="%s/movies/ep10/anim_jill_wash2_ep10.webm" % persistent.img_dir, start_image="anim_jill_wash2_ep10_start", channel = "sex16")
image anim_jill_wash3_ep10 = Movie(play="%s/movies/ep10/anim_jill_wash3_ep10.webm" % persistent.img_dir, start_image="anim_jill_wash3_ep10_start", channel = "sex17")

image anim_jill_strip_ep10 = Movie(play="%s/movies/ep10/anim_jill_strip_ep10.webm" % persistent.img_dir, start_image="anim_jill_strip_ep10_start", channel = "sex18", loop=False)
image bg anim_jill_strip_ep10 movie:
    "anim_jill_strip_ep10"
    pause 4
    "anim_jill_strip_ep10_end"
image anim_jill_insert_ep10 = Movie(play="%s/movies/ep10/anim_jill_insert_ep10.webm" % persistent.img_dir, start_image="anim_jill_insert_ep10_start", channel = "sex19", loop=False)
image bg anim_jill_insert_ep10 movie:
    "anim_jill_insert_ep10"
    pause 4
    "anim_jill_insert_ep10_end"
image anim_jill_insert2_ep10 = Movie(play="%s/movies/ep10/anim_jill_insert2_ep10.webm" % persistent.img_dir, start_image="anim_jill_insert2_ep10_start", channel = "sex20", loop=False)
image bg anim_jill_insert2_ep10 movie:
    "anim_jill_insert2_ep10"
    pause 4
    "anim_jill_insert2_ep10_end"


image anim_jm_bj1_ep10 = Movie(play="%s/movies/ep10/anim_jm_bj1_ep10.webm" % persistent.img_dir, start_image="anim_jm_bj1_ep10_start", channel = "sex1")
image anim_jm_bj2_ep10 = Movie(play="%s/movies/ep10/anim_jm_bj2_ep10.webm" % persistent.img_dir, start_image="anim_jm_bj2_ep10_start", channel = "sex2")
image anim_jm_bj3_ep10 = Movie(play="%s/movies/ep10/anim_jm_bj3_ep10.webm" % persistent.img_dir, start_image="anim_jm_bj3_ep10_start", channel = "sex3")
image anim_jm_bj4_ep10 = Movie(play="%s/movies/ep10/anim_jm_bj4_ep10.webm" % persistent.img_dir, start_image="anim_jm_bj4_ep10_start", channel = "sex4")
image anim_jm_bj5_ep10 = Movie(play="%s/movies/ep10/anim_jm_bj5_ep10.webm" % persistent.img_dir, start_image="anim_jm_bj5_ep10_start", channel = "sex5")
image anim_jm_miss1_ep10 = Movie(play="%s/movies/ep10/anim_jm_miss1_ep10.webm" % persistent.img_dir, start_image="anim_jm_miss1_ep10_start", channel = "sex6")
image anim_jm_miss2_ep10 = Movie(play="%s/movies/ep10/anim_jm_miss2_ep10.webm" % persistent.img_dir, start_image="anim_jm_miss2_ep10_start", channel = "sex7")
image anim_jm_miss3_ep10 = Movie(play="%s/movies/ep10/anim_jm_miss3_ep10.webm" % persistent.img_dir, start_image="anim_jm_miss3_ep10_start", channel = "sex8")
image anim_jm_miss4_ep10 = Movie(play="%s/movies/ep10/anim_jm_miss4_ep10.webm" % persistent.img_dir, start_image="anim_jm_miss4_ep10_start", channel = "sex9")
image anim_jm_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_jm_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_jm_doggy1_ep10_start", channel = "sex10")
image anim_jm_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_jm_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_jm_doggy2_ep10_start", channel = "sex11")
image anim_jm_doggy3_ep10 = Movie(play="%s/movies/ep10/anim_jm_doggy3_ep10.webm" % persistent.img_dir, start_image="anim_jm_doggy3_ep10_start", channel = "sex12")
image anim_jm_doggy4_ep10 = Movie(play="%s/movies/ep10/anim_jm_doggy4_ep10.webm" % persistent.img_dir, start_image="anim_jm_doggy4_ep10_start", channel = "sex13")
image anim_jm_doggy5_ep10 = Movie(play="%s/movies/ep10/anim_jm_doggy5_ep10.webm" % persistent.img_dir, start_image="anim_jm_doggy5_ep10_start", channel = "sex14")
image anim_jm_hj1_ep10 = Movie(play="%s/movies/ep10/anim_jm_hj1_ep10.webm" % persistent.img_dir, start_image="anim_jm_hj1_ep10_start", channel = "sex15")


image anim_josy_bj1_ep10 = Movie(play="%s/movies/ep10/anim_josy_bj1_ep10.webm" % persistent.img_dir, start_image="anim_josy_bj1_ep10_start", channel = "sex1")
image anim_josy_bj2_ep10 = Movie(play="%s/movies/ep10/anim_josy_bj2_ep10.webm" % persistent.img_dir, start_image="anim_josy_bj2_ep10_start", channel = "sex2")
image anim_josy_tits_ep10 = Movie(play="%s/movies/ep10/anim_josy_tits_ep10.webm" % persistent.img_dir, start_image="anim_josy_tits_ep10_start", channel = "sex3")
image anim_josy_lick1_ep10 = Movie(play="%s/movies/ep10/anim_josy_lick1_ep10.webm" % persistent.img_dir, start_image="anim_josy_lick1_ep10_start", channel = "sex4")
image anim_josy_lick2_ep10 = Movie(play="%s/movies/ep10/anim_josy_lick2_ep10.webm" % persistent.img_dir, start_image="anim_josy_lick2_ep10_start", channel = "sex5")
image anim_josy_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_josy_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_josy_doggy1_ep10_start", channel = "sex6")
image anim_josy_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_josy_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_josy_doggy2_ep10_start", channel = "sex7")
image anim_josy_ride1_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride1_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride1_ep10_start", channel = "sex8")
image anim_josy_ride1b_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride1b_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride1b_ep10_start", channel = "sex9")
image anim_josy_ride2_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride2_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride2_ep10_start", channel = "sex10")
image anim_josy_ride3_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride3_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride3_ep10_start", channel = "sex11")
image anim_josy_ride3b_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride3b_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride3b_ep10_start", channel = "sex12")
image anim_josy_ride4_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride4_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride4_ep10_start", channel = "sex13")
image anim_josy_ride4b_ep10 = Movie(play="%s/movies/ep10/anim_josy_ride4b_ep10.webm" % persistent.img_dir, start_image="anim_josy_ride4b_ep10_start", channel = "sex14")
image anim_josy_side1_ep10 = Movie(play="%s/movies/ep10/anim_josy_side1_ep10.webm" % persistent.img_dir, start_image="anim_josy_side1_ep10_start", channel = "sex15")
image anim_josy_side1b_ep10 = Movie(play="%s/movies/ep10/anim_josy_side1b_ep10.webm" % persistent.img_dir, start_image="anim_josy_side1b_ep10_start", channel = "sex16")
image anim_josy_side2_ep10 = Movie(play="%s/movies/ep10/anim_josy_side2_ep10.webm" % persistent.img_dir, start_image="anim_josy_side2_ep10_start", channel = "sex17")
image anim_josy_prone1_ep10 = Movie(play="%s/movies/ep10/anim_josy_prone1_ep10.webm" % persistent.img_dir, start_image="anim_josy_prone1_ep10_start", channel = "sex18")
image anim_josy_prone2_ep10 = Movie(play="%s/movies/ep10/anim_josy_prone2_ep10.webm" % persistent.img_dir, start_image="anim_josy_prone2_ep10_start", channel = "sex19")
image anim_josy_miss1_ep10 = Movie(play="%s/movies/ep10/anim_josy_miss1_ep10.webm" % persistent.img_dir, start_image="anim_josy_miss1_ep10_start", channel = "sex20")
image anim_josy_miss2_ep10 = Movie(play="%s/movies/ep10/anim_josy_miss2_ep10.webm" % persistent.img_dir, start_image="anim_josy_miss2_ep10_start", channel = "sex1")
image anim_josy_kiss_ep10 = Movie(play="%s/movies/ep10/anim_josy_kiss_ep10.webm" % persistent.img_dir, start_image="anim_josy_kiss_ep10_start", channel = "sex2")


image anim_lily_kiss_ep10 = Movie(play="%s/movies/ep10/anim_lily_kiss_ep10.webm" % persistent.img_dir, start_image="anim_lily_kiss_ep10_start", channel = "sex1")
image anim_lily_hj_ep10 = Movie(play="%s/movies/ep10/anim_lily_hj_ep10.webm" % persistent.img_dir, start_image="anim_lily_hj_ep10_start", channel = "sex2")
image anim_lily_bj1_ep10 = Movie(play="%s/movies/ep10/anim_lily_bj1_ep10.webm" % persistent.img_dir, start_image="anim_lily_bj1_ep10_start", channel = "sex3")
image anim_lily_bj2_ep10 = Movie(play="%s/movies/ep10/anim_lily_bj2_ep10.webm" % persistent.img_dir, start_image="anim_lily_bj2_ep10_start", channel = "sex4")
image anim_lily_bj3_ep10 = Movie(play="%s/movies/ep10/anim_lily_bj3_ep10.webm" % persistent.img_dir, start_image="anim_lily_bj3_ep10_start", channel = "sex5")
image anim_lily_bj4_ep10 = Movie(play="%s/movies/ep10/anim_lily_bj4_ep10.webm" % persistent.img_dir, start_image="anim_lily_bj4_ep10_start", channel = "sex6")
image anim_lily_bj5_ep10 = Movie(play="%s/movies/ep10/anim_lily_bj5_ep10.webm" % persistent.img_dir, start_image="anim_lily_bj5_ep10_start", channel = "sex7")
image anim_lily_cum_ep10 = Movie(play="%s/movies/ep10/anim_lily_cum_ep10.webm" % persistent.img_dir, start_image ="anim_lily_cum_ep10_start", channel = "sex8", loop=False)
image bg anim_lily_cum_ep10 movie:
    "anim_lily_cum_ep10"
    pause 7.33
    "anim_lily_cum_ep10_end"
image anim_lily_cum2_ep10 = Movie(play="%s/movies/ep10/anim_lily_cum2_ep10.webm" % persistent.img_dir, start_image="anim_lily_cum2_ep10_start", channel = "sex9")



image anim_madame_boobjob_cum_ep10 = Movie(play="%s/movies/ep10/anim_madame_boobjob_cum_ep10.webm" % persistent.img_dir, start_image="anim_madame_boobjob_cum_ep10_start", channel = "sex1")
image anim_madame_boobjob1_ep10 = Movie(play="%s/movies/ep10/anim_madame_boobjob1_ep10.webm" % persistent.img_dir, start_image="anim_madame_boobjob1_ep10_start", channel = "sex2")
image anim_madame_boobjob2_ep10 = Movie(play="%s/movies/ep10/anim_madame_boobjob2_ep10.webm" % persistent.img_dir, start_image="anim_madame_boobjob2_ep10_start", channel = "sex3")
image anim_madame_boobjob3_ep10 = Movie(play="%s/movies/ep10/anim_madame_boobjob3_ep10.webm" % persistent.img_dir, start_image="anim_madame_boobjob3_ep10_start", channel = "sex4")
image anim_madame_footjob1_ep10 = Movie(play="%s/movies/ep10/anim_madame_footjob1_ep10.webm" % persistent.img_dir, start_image="anim_madame_footjob1_ep10_start", channel = "sex5")
image anim_madame_footjob2_ep10 = Movie(play="%s/movies/ep10/anim_madame_footjob2_ep10.webm" % persistent.img_dir, start_image="anim_madame_footjob2_ep10_start", channel = "sex6")
image anim_madame_footjob3_ep10 = Movie(play="%s/movies/ep10/anim_madame_footjob3_ep10.webm" % persistent.img_dir, start_image="anim_madame_footjob3_ep10_start", channel = "sex7")
image anim_madame_miss1_ep10 = Movie(play="%s/movies/ep10/anim_madame_miss1_ep10.webm" % persistent.img_dir, start_image="anim_madame_miss1_ep10_start", channel = "sex8")
image anim_madame_miss2_ep10 = Movie(play="%s/movies/ep10/anim_madame_miss2_ep10.webm" % persistent.img_dir, start_image="anim_madame_miss2_ep10_start", channel = "sex9")
image anim_madame_miss3_ep10 = Movie(play="%s/movies/ep10/anim_madame_miss3_ep10.webm" % persistent.img_dir, start_image="anim_madame_miss3_ep10_start", channel = "sex10")
image anim_madame_ride1_ep10 = Movie(play="%s/movies/ep10/anim_madame_ride1_ep10.webm" % persistent.img_dir, start_image="anim_madame_ride1_ep10_start", channel = "sex11")
image anim_madame_ride2_ep10 = Movie(play="%s/movies/ep10/anim_madame_ride2_ep10.webm" % persistent.img_dir, start_image="anim_madame_ride2_ep10_start", channel = "sex12")
image anim_madame_ride3_ep10 = Movie(play="%s/movies/ep10/anim_madame_ride3_ep10.webm" % persistent.img_dir, start_image="anim_madame_ride3_ep10_start", channel = "sex13")


image anim_maya_hj_ep10 = Movie(play="%s/movies/ep10/anim_maya_hj_ep10.webm" % persistent.img_dir, start_image="anim_maya_hj_ep10_start", channel = "sex1")
image anim_maya_hj2_ep10 = Movie(play="%s/movies/ep10/anim_maya_hj2_ep10.webm" % persistent.img_dir, start_image="anim_maya_hj2_ep10_start", channel = "sex2")
image anim_maya_bj_ep10 = Movie(play="%s/movies/ep10/anim_maya_bj_ep10.webm" % persistent.img_dir, start_image="anim_maya_bj_ep10_start", channel = "sex3")
image anim_maya_bj2_ep10 = Movie(play="%s/movies/ep10/anim_maya_bj2_ep10.webm" % persistent.img_dir, start_image="anim_maya_bj2_ep10_start", channel = "sex4")
image anim_maya_bj3_ep10 = Movie(play="%s/movies/ep10/anim_maya_bj3_ep10.webm" % persistent.img_dir, start_image="anim_maya_bj3_ep10_start", channel = "sex5")
image anim_maya_lick_ep10 = Movie(play="%s/movies/ep10/anim_maya_lick_ep10.webm" % persistent.img_dir, start_image="anim_maya_lick_ep10_start", channel = "sex6")
image anim_maya_insert_ep10 = Movie(play="%s/movies/ep10/anim_maya_insert_ep10.webm" % persistent.img_dir, start_image="anim_maya_insert_ep10_start", channel = "sex7", loop=False)
image bg anim_maya_insert_ep10 movie:
    "anim_maya_insert_ep10"
    pause 4
    "anim_maya_insert_ep10_end"
image anim_maya_ride1_ep10 = Movie(play="%s/movies/ep10/anim_maya_ride1_ep10.webm" % persistent.img_dir, start_image="anim_maya_ride1_ep10_start", channel = "sex8")
image anim_maya_ride2_ep10 = Movie(play="%s/movies/ep10/anim_maya_ride2_ep10.webm" % persistent.img_dir, start_image="anim_maya_ride2_ep10_start", channel = "sex9")
image anim_maya_ride3_ep10 = Movie(play="%s/movies/ep10/anim_maya_ride3_ep10.webm" % persistent.img_dir, start_image="anim_maya_ride3_ep10_start", channel = "sex10")
image anim_maya_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_maya_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_maya_doggy1_ep10_start", channel = "sex11")
image anim_maya_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_maya_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_maya_doggy2_ep10_start", channel = "sex12")
image anim_maya_doggy3_ep10 = Movie(play="%s/movies/ep10/anim_maya_doggy3_ep10.webm" % persistent.img_dir, start_image="anim_maya_doggy3_ep10_start", channel = "sex13")
image anim_maya_side1_ep10 = Movie(play="%s/movies/ep10/anim_maya_side1_ep10.webm" % persistent.img_dir, start_image="anim_maya_side1_ep10_start", channel = "sex14")
image anim_maya_side2_ep10 = Movie(play="%s/movies/ep10/anim_maya_side2_ep10.webm" % persistent.img_dir, start_image="anim_maya_side2_ep10_start", channel = "sex15")
image anim_maya_stand1_ep10 = Movie(play="%s/movies/ep10/anim_maya_stand1_ep10.webm" % persistent.img_dir, start_image="anim_maya_stand1_ep10_start", channel = "sex16")
image anim_maya_stand2_ep10 = Movie(play="%s/movies/ep10/anim_maya_stand2_ep10.webm" % persistent.img_dir, start_image="anim_maya_stand2_ep10_start", channel = "sex17")
image anim_maya_cum_ep10 = Movie(play="%s/movies/ep10/anim_maya_cum_ep10.webm" % persistent.img_dir, start_image="anim_maya_cum_ep10_start", channel = "sex18")


image anim_nora_slap_ep10 = Movie(play="%s/movies/ep10/anim_nora_slap_ep10.webm" % persistent.img_dir, start_image="anim_nora_slap_ep10_start", channel = "sex1")
image bg anim_nora_slap_ep10 movie:
    "anim_nora_slap_ep10"
    pause 1.7
    function play_slap_ep10
    pause 2.3
    repeat
image anim_nora_boobjob1_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob1_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob1_ep10_start", channel = "sex2")
image anim_nora_boobjob2_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob2_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob2_ep10_start", channel = "sex3")
image anim_nora_boobjob3_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob3_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob3_ep10_start", channel = "sex4")
image anim_nora_boobjob3b_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob3b_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob3b_ep10_start", channel = "sex5")
image anim_nora_boobjob4_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob4_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob4_ep10_start", channel = "sex6")
image anim_nora_boobjob5_ep10 = Movie(play="%s/movies/ep10/anim_nora_boobjob5_ep10.webm" % persistent.img_dir, start_image="anim_nora_boobjob5_ep10_start", channel = "sex7")
image anim_nora_rub_ep10 = Movie(play="%s/movies/ep10/anim_nora_rub_ep10.webm" % persistent.img_dir, start_image="anim_nora_rub_ep10_start", channel = "sex8")
image anim_nora_rub2_ep10 = Movie(play="%s/movies/ep10/anim_nora_rub2_ep10.webm" % persistent.img_dir, start_image="anim_nora_rub2_ep10_start", channel = "sex9")
image anim_nora_bj1_ep10 = Movie(play="%s/movies/ep10/anim_nora_bj1_ep10.webm" % persistent.img_dir, start_image="anim_nora_bj1_ep10_start", channel = "sex10")
image anim_nora_bj2_ep10 = Movie(play="%s/movies/ep10/anim_nora_bj2_ep10.webm" % persistent.img_dir, start_image="anim_nora_bj2_ep10_start", channel = "sex11")
image anim_nora_bj3_ep10 = Movie(play="%s/movies/ep10/anim_nora_bj3_ep10.webm" % persistent.img_dir, start_image="anim_nora_bj3_ep10_start", channel = "sex12")
image anim_nora_bj3b_ep10 = Movie(play="%s/movies/ep10/anim_nora_bj3b_ep10.webm" % persistent.img_dir, start_image="anim_nora_bj3b_ep10_start", channel = "sex13")
image anim_nora_lick_ep10 = Movie(play="%s/movies/ep10/anim_nora_lick_ep10.webm" % persistent.img_dir, start_image="anim_nora_lick_ep10_start", channel = "sex14")
image anim_nora_lick2_ep10 = Movie(play="%s/movies/ep10/anim_nora_lick2_ep10.webm" % persistent.img_dir, start_image="anim_nora_lick2_ep10_start", channel = "sex15")
image anim_nora_assjob_ep10 = Movie(play="%s/movies/ep10/anim_nora_assjob_ep10.webm" % persistent.img_dir, start_image="anim_nora_assjob_ep10_start", channel = "sex16")
image anim_nora_assjob2_ep10 = Movie(play="%s/movies/ep10/anim_nora_assjob2_ep10.webm" % persistent.img_dir, start_image="anim_nora_assjob2_ep10_start", channel = "sex17")
image anim_nora_insert_ep10 = Movie(play="%s/movies/ep10/anim_nora_insert_ep10.webm" % persistent.img_dir, start_image = "anim_nora_insert_ep10_start", channel = "sex18", loop=False)
image bg anim_nora_insert_ep10 movie:
    "anim_nora_insert_ep10"
    pause 4
    "anim_nora_insert_ep10_end"
image anim_fluffy_ep10 = Movie(play="%s/movies/ep10/anim_fluffy_ep10.webm" % persistent.img_dir, start_image = "anim_fluffy_ep10_start", channel = "sex19", loop=False)
image bg anim_fluffy_ep10 movie:
    "anim_fluffy_ep10"
    pause 2
    "anim_fluffy_ep10_end"

image anim_nora_prone1_ep10 = Movie(play="%s/movies/ep10/anim_nora_prone1_ep10.webm" % persistent.img_dir, start_image="anim_nora_prone1_ep10_start", channel = "sex1")
image anim_nora_prone2_ep10 = Movie(play="%s/movies/ep10/anim_nora_prone2_ep10.webm" % persistent.img_dir, start_image="anim_nora_prone2_ep10_start", channel = "sex2")
image anim_nora_side1_ep10 = Movie(play="%s/movies/ep10/anim_nora_side1_ep10.webm" % persistent.img_dir, start_image="anim_nora_side1_ep10_start", channel = "sex3")
image anim_nora_side2_ep10 = Movie(play="%s/movies/ep10/anim_nora_side2_ep10.webm" % persistent.img_dir, start_image="anim_nora_side2_ep10_start", channel = "sex4")
image anim_nora_stand1_ep10 = Movie(play="%s/movies/ep10/anim_nora_stand1_ep10.webm" % persistent.img_dir, start_image="anim_nora_stand1_ep10_start", channel = "sex5")
image anim_nora_stand2_ep10 = Movie(play="%s/movies/ep10/anim_nora_stand2_ep10.webm" % persistent.img_dir, start_image="anim_nora_stand2_ep10_start", channel = "sex6")
image anim_nora_stand3_ep10 = Movie(play="%s/movies/ep10/anim_nora_stand3_ep10.webm" % persistent.img_dir, start_image="anim_nora_stand3_ep10_start", channel = "sex7")
image anim_nora_rev1_ep10 = Movie(play="%s/movies/ep10/anim_nora_rev1_ep10.webm" % persistent.img_dir, start_image="anim_nora_rev1_ep10_start", channel = "sex8")
image anim_nora_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_nora_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_nora_doggy1_ep10_start", channel = "sex9")
image anim_nora_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_nora_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_nora_doggy2_ep10_start", channel = "sex10")
image anim_nora_ride1_ep10 = Movie(play="%s/movies/ep10/anim_nora_ride1_ep10.webm" % persistent.img_dir, start_image="anim_nora_ride1_ep10_start", channel = "sex11")
image anim_nora_ride2_ep10 = Movie(play="%s/movies/ep10/anim_nora_ride2_ep10.webm" % persistent.img_dir, start_image="anim_nora_ride2_ep10_start", channel = "sex12")
image anim_nora_cum1_ep10 = Movie(play="%s/movies/ep10/anim_nora_cum1_ep10.webm" % persistent.img_dir, start_image="anim_nora_cum1_ep10_start", channel = "sex13", loop=False)
image anim_nora_cum2_ep10 = Movie(play="%s/movies/ep10/anim_nora_cum2_ep10.webm" % persistent.img_dir, start_image="anim_nora_cum2_ep10_start", channel = "sex14")

image bg anim_nora_cum1_ep10 movie:
    "anim_nora_cum1_ep10"
    pause 5.33
    "anim_nora_cum1_ep10_end"


image anim_quinn_hj_ep10 = Movie(play="%s/movies/ep10/anim_quinn_hj_ep10.webm" % persistent.img_dir, start_image="anim_quinn_hj_ep10_start", channel = "sex1")
image anim_quinn_bj_ep10 = Movie(play="%s/movies/ep10/anim_quinn_bj_ep10.webm" % persistent.img_dir, start_image="anim_quinn_bj_ep10_start", channel = "sex2")
image anim_quinn_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_quinn_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_quinn_doggy1_ep10_start", channel = "sex3")
image anim_quinn_miss1_ep10 = Movie(play="%s/movies/ep10/anim_quinn_miss1_ep10.webm" % persistent.img_dir, start_image="anim_quinn_miss1_ep10_start", channel = "sex4")
image anim_quinn_miss2_ep10 = Movie(play="%s/movies/ep10/anim_quinn_miss2_ep10.webm" % persistent.img_dir, start_image="anim_quinn_miss2_ep10_start", channel = "sex5")
image anim_quinn_miss3_ep10 = Movie(play="%s/movies/ep10/anim_quinn_miss3_ep10.webm" % persistent.img_dir, start_image="anim_quinn_miss3_ep10_start", channel = "sex6")
image anim_quinn_rev1_ep10 = Movie(play="%s/movies/ep10/anim_quinn_rev1_ep10.webm" % persistent.img_dir, start_image="anim_quinn_rev1_ep10_start", channel = "sex7")
image anim_quinn_rev2_ep10 = Movie(play="%s/movies/ep10/anim_quinn_rev2_ep10.webm" % persistent.img_dir, start_image="anim_quinn_rev2_ep10_start", channel = "sex8")
image anim_quinn_rev3_ep10 = Movie(play="%s/movies/ep10/anim_quinn_rev3_ep10.webm" % persistent.img_dir, start_image="anim_quinn_rev3_ep10_start", channel = "sex9")
image anim_quinn_ride1_ep10 = Movie(play="%s/movies/ep10/anim_quinn_ride1_ep10.webm" % persistent.img_dir, start_image="anim_quinn_ride1_ep10_start", channel = "sex10")
image anim_quinn_ride2_ep10 = Movie(play="%s/movies/ep10/anim_quinn_ride2_ep10.webm" % persistent.img_dir, start_image="anim_quinn_ride2_ep10_start", channel = "sex11")
image anim_quinn_cum_ep10 = Movie(play="%s/movies/ep10/anim_quinn_cum_ep10.webm" % persistent.img_dir, start_image="anim_quinn_cum_ep10_start", channel = "sex12")
image anim_quinn_car_ep10 = Movie(play="%s/movies/ep10/anim_quinn_car_ep10.webm" % persistent.img_dir, start_image="anim_quinn_car_ep10_start", channel = "sex13")


image anim_riona_cum_ep10 = Movie(play="%s/movies/ep10/anim_riona_cum_ep10.webm" % persistent.img_dir, start_image="anim_riona_cum_ep10_start", channel = "sex1")
image anim_riona_kiss_ep10 = Movie(play="%s/movies/ep10/anim_riona_kiss_ep10.webm" % persistent.img_dir, start_image="anim_riona_kiss_ep10_start", channel = "sex2")
image anim_riona_hj1_ep10 = Movie(play="%s/movies/ep10/anim_riona_hj1_ep10.webm" % persistent.img_dir, start_image="anim_riona_hj1_ep10_start", channel = "sex3")
image anim_riona_bj1_ep10 = Movie(play="%s/movies/ep10/anim_riona_bj1_ep10.webm" % persistent.img_dir, start_image="anim_riona_bj1_ep10_start", channel = "sex4")
image anim_riona_bj1b_ep10 = Movie(play="%s/movies/ep10/anim_riona_bj1b_ep10.webm" % persistent.img_dir, start_image="anim_riona_bj1b_ep10_start", channel = "sex5")
image anim_riona_bj2_ep10 = Movie(play="%s/movies/ep10/anim_riona_bj2_ep10.webm" % persistent.img_dir, start_image="anim_riona_bj2_ep10_start", channel = "sex6")
image anim_riona_cunn1_ep10 = Movie(play="%s/movies/ep10/anim_riona_cunn1_ep10.webm" % persistent.img_dir, start_image="anim_riona_cunn1_ep10_start", channel = "sex7")
image anim_riona_cunn2_ep10 = Movie(play="%s/movies/ep10/anim_riona_cunn2_ep10.webm" % persistent.img_dir, start_image="anim_riona_cunn2_ep10_start", channel = "sex8")
image anim_riona_cunn3_ep10 = Movie(play="%s/movies/ep10/anim_riona_cunn3_ep10.webm" % persistent.img_dir, start_image="anim_riona_cunn3_ep10_start", channel = "sex9")
image anim_riona_finger1_ep10 = Movie(play="%s/movies/ep10/anim_riona_finger1_ep10.webm" % persistent.img_dir, start_image="anim_riona_finger1_ep10_start", channel = "sex10")
image anim_riona_finger2_ep10 = Movie(play="%s/movies/ep10/anim_riona_finger2_ep10.webm" % persistent.img_dir, start_image="anim_riona_finger2_ep10_start", channel = "sex11")
image anim_riona_finger3_ep10 = Movie(play="%s/movies/ep10/anim_riona_finger3_ep10.webm" % persistent.img_dir, start_image="anim_riona_finger3_ep10_start", channel = "sex12")
image anim_riona_doggy1_anal_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy1_anal_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy1_anal_ep10_start", channel = "sex13")
image anim_riona_doggy2_anal_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy2_anal_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy2_anal_ep10_start", channel = "sex14")
image anim_riona_doggy3_anal_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy3_anal_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy3_anal_ep10_start", channel = "sex15")
image anim_riona_doggy4_anal_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy4_anal_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy4_anal_ep10_start", channel = "sex16")
image anim_riona_rev1_ep10 = Movie(play="%s/movies/ep10/anim_riona_rev1_ep10.webm" % persistent.img_dir, start_image="anim_riona_rev1_ep10_start", channel = "sex17")
image anim_riona_rev2_ep10 = Movie(play="%s/movies/ep10/anim_riona_rev2_ep10.webm" % persistent.img_dir, start_image="anim_riona_rev2_ep10_start", channel = "sex18")
image anim_riona_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy1_ep10_start", channel = "sex19")
image anim_riona_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_riona_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_riona_doggy2_ep10_start", channel = "sex20")
image anim_riona_stand1_ep10 = Movie(play="%s/movies/ep10/anim_riona_stand1_ep10.webm" % persistent.img_dir, start_image="anim_riona_stand1_ep10_start", channel = "sex1")
image anim_riona_stand2_ep10 = Movie(play="%s/movies/ep10/anim_riona_stand2_ep10.webm" % persistent.img_dir, start_image="anim_riona_stand2_ep10_start", channel = "sex2")
image anim_riona_stand3_ep10 = Movie(play="%s/movies/ep10/anim_riona_stand3_ep10.webm" % persistent.img_dir, start_image="anim_riona_stand3_ep10_start", channel = "sex3")
image anim_riona_miss1_ep10 = Movie(play="%s/movies/ep10/anim_riona_miss1_ep10.webm" % persistent.img_dir, start_image="anim_riona_miss1_ep10_start", channel = "sex4")
image anim_riona_miss2_ep10 = Movie(play="%s/movies/ep10/anim_riona_miss2_ep10.webm" % persistent.img_dir, start_image="anim_riona_miss2_ep10_start", channel = "sex5")
image anim_riona_miss3_ep10 = Movie(play="%s/movies/ep10/anim_riona_miss3_ep10.webm" % persistent.img_dir, start_image="anim_riona_miss3_ep10_start", channel = "sex6")


image anim_sage_pan_ep10 = Movie(play="%s/movies/ep10/anim_sage_pan_ep10.webm" % persistent.img_dir, start_image ="anim_sage_pan_ep10_start", channel = "sex1", loop=False)
image anim_dots_ep10 = Movie(play="%s/movies/ep10/anim_dots_ep10.webm" % persistent.img_dir, start_image="anim_dots_ep10_start", channel = "sex2")
image anim_sage_69_ep10 = Movie(play="%s/movies/ep10/anim_sage_69_ep10.webm" % persistent.img_dir, start_image="anim_sage_69_ep10_start", channel = "sex3")
image anim_sage_69b_ep10 = Movie(play="%s/movies/ep10/anim_sage_69b_ep10.webm" % persistent.img_dir, start_image="anim_sage_69b_ep10_start", channel = "sex4")
image anim_sage_bj_cum_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj_cum_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj_cum_ep10_start", channel = "sex5")
image anim_sage_bj1_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj1_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj1_ep10_start", channel = "sex6")
image anim_sage_bj2_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj2_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj2_ep10_start", channel = "sex7")
image anim_sage_bj3_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj3_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj3_ep10_start", channel = "sex8")
image anim_sage_bj4_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj4_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj4_ep10_start", channel = "sex9")
image anim_sage_bj5_ep10 = Movie(play="%s/movies/ep10/anim_sage_bj5_ep10.webm" % persistent.img_dir, start_image="anim_sage_bj5_ep10_start", channel = "sex10")
image anim_sage_boobjob1_ep10 = Movie(play="%s/movies/ep10/anim_sage_boobjob1_ep10.webm" % persistent.img_dir, start_image="anim_sage_boobjob1_ep10_start", channel = "sex11")
image anim_sage_boobjob2_ep10 = Movie(play="%s/movies/ep10/anim_sage_boobjob2_ep10.webm" % persistent.img_dir, start_image="anim_sage_boobjob2_ep10_start", channel = "sex12")
image anim_sage_cum1_ep10 = Movie(play="%s/movies/ep10/anim_sage_cum1_ep10.webm" % persistent.img_dir, start_image="anim_sage_cum1_ep10_start", channel = "sex13")
image anim_sage_doggy1_anal_ep10 = Movie(play="%s/movies/ep10/anim_sage_doggy1_anal_ep10.webm" % persistent.img_dir, start_image="anim_sage_doggy1_anal_ep10_start", channel = "sex14")
image anim_sage_doggy1_ep10 = Movie(play="%s/movies/ep10/anim_sage_doggy1_ep10.webm" % persistent.img_dir, start_image="anim_sage_doggy1_ep10_start", channel = "sex15")
image anim_sage_doggy2_anal_ep10 = Movie(play="%s/movies/ep10/anim_sage_doggy2_anal_ep10.webm" % persistent.img_dir, start_image="anim_sage_doggy2_anal_ep10_start", channel = "sex16")
image anim_sage_doggy2_ep10 = Movie(play="%s/movies/ep10/anim_sage_doggy2_ep10.webm" % persistent.img_dir, start_image="anim_sage_doggy2_ep10_start", channel = "sex17")
image anim_sage_ride1_ep10 = Movie(play="%s/movies/ep10/anim_sage_ride1_ep10.webm" % persistent.img_dir, start_image="anim_sage_ride1_ep10_start", channel = "sex18")
image anim_sage_ride2_ep10 = Movie(play="%s/movies/ep10/anim_sage_ride2_ep10.webm" % persistent.img_dir, start_image="anim_sage_ride2_ep10_start", channel = "sex19")
image anim_sage_miss1_ep10 = Movie(play="%s/movies/ep10/anim_sage_miss1_ep10.webm" % persistent.img_dir, start_image="anim_sage_miss1_ep10_start", channel = "sex20")
image anim_sage_miss2_ep10 = Movie(play="%s/movies/ep10/anim_sage_miss2_ep10.webm" % persistent.img_dir, start_image="anim_sage_miss2_ep10_start", channel = "sex1")
image anim_sage_miss2b_ep10 = Movie(play="%s/movies/ep10/anim_sage_miss2b_ep10.webm" % persistent.img_dir, start_image="anim_sage_miss2_ep10_start", channel = "sex2")
image anim_sage_miss3_ep10 = Movie(play="%s/movies/ep10/anim_sage_miss3_ep10.webm" % persistent.img_dir, start_image="anim_sage_miss3_ep10_start", channel = "sex3")
image anim_sage_miss4_ep10 = Movie(play="%s/movies/ep10/anim_sage_miss4_ep10.webm" % persistent.img_dir, start_image="anim_sage_miss4_ep10_start", channel = "sex4")


image bg anim_sage_pan_ep10 movie:
    "anim_sage_pan_ep10"
    pause 13.267
    "anim_sage_pan_ep10_end"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

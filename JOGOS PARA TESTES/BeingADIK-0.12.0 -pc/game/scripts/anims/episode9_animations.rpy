init -1 python:
    def play_wave3_footsteps(trans, st, at):
        renpy.play("sound_effects/footsteps_outside.mp3","sfx1")
    def play_wave3_car_pass(trans, st, at):
        renpy.play("sound_effects/season3/car_pass.mp3","sfx1")
    def play_wave3_car_hit(trans, st, at):
        renpy.play("sound_effects/season3/car_hit.mp3","sfx1")
    def play_wave3_squirt(trans, st, at):
        renpy.play("sound_effects/season3/squirt.mp3","sfx1")
    def play_wave3_car_whoosh(trans, st, at):
        renpy.play("sound_effects/whoosh.mp3","sfx1")
    def play_wave3_car_shove(trans, st, at):
        renpy.play("sound_effects/shove.mp3","sfx1")
    def play_coin_ep9(trans, st, at):
        renpy.play("sound_effects/coin.mp3","sfx1")

    def play_jumpscare_ep9(trans, st, at):
        renpy.play("sound_effects/season3/jumpscare.mp3","sfx1")
    def play_slap_ep9(trans, st, at):
        renpy.play("sound_effects/slap.mp3","sfx1")
    def play_intro_ep9(trans, st, at):
        renpy.play("music/ep9/licensed_music/track114.mp3","music")
    def play_scary_intro_ep9(trans, st, at):
        renpy.music.stop(fadeout=10)
        renpy.play("<from 44.7>music/ep9/licensed_music/track116.mp3", fadein=10, channel="music2")
    def play_hit_ep5r(trans, st, at):
        renpy.play("sound_effects/season2/tybalt_punch.mp3", "sfx1")
    def play_hit_ep7r(trans, st, at):
        renpy.play("sound_effects/whoosh.mp3", "sfx1")
    def play_hit2_ep7r(trans, st, at):
        renpy.play("sound_effects/hit.mp3", "sfx2")
    def play_lightning_ep9():
        renpy.play("sound_effects/season2/thunder2.mp3", "sfx3")

image anim_punch_ep5r = Movie(play="%s/ep9/recap/anim_punch_ep5.webm" % persistent.img_dir, channel = "sex1", loop=False)
image bg anim_punch_ep5r movie:
    "anim_punch_ep5r"
    function play_hit_ep5r
    pause 3.50
    "ep5_tybalt_punch"
image anim_tybalt_smash3_ep7r = Movie(play="%s/ep9/recap/anim_tybalt_smash3_ep7.webm" % persistent.img_dir, channel = "sex2", loop=False)
image bg anim_tybalt_smash3_ep7r movie:
    "anim_tybalt_smash3_ep7r"
    function play_hit_ep7r
    pause 0.5
    function play_hit2_ep7r
    pause 1.5
    "anim_tybalt_smash3_ep7_end"

image anim_coin_flip_ep9 = Movie(play="%s/movies/ep9/anim_coin_flip_ep9.webm" % persistent.img_dir, start_image="anim_coin_flip_ep9_start", channel = "sex3", loop=False)
image anim_eyes_scared_ep9 = Movie(play="%s/movies/ep9/anim_eyes_scared_ep9.webm" % persistent.img_dir, start_image="anim_eyes_scared_ep9_start", channel = "sex4")
image anim_eyes_scared2_ep9 = Movie(play="%s/movies/ep9/anim_eyes_scared2_ep9.webm" % persistent.img_dir, start_image="anim_eyes_scared2_ep9_start", channel = "sex5")
image anim_eyes_scared3_ep9 = Movie(play="%s/movies/ep9/anim_eyes_scared3_ep9.webm" % persistent.img_dir, start_image="anim_eyes_scared3_ep9_start", channel = "sex6", loop=False)
image bg anim_eyes_scared3_ep9 movie:
    function play_jumpscare_ep9
    "anim_eyes_scared3_ep9"
    pause 2
    "anim_eyes_scared3_ep9_end"
image bg anim_coin_flip_ep9 movie:
    function play_coin_ep9
    "anim_coin_flip_ep9"
    pause 2
    "anim_coin_flip_ep9_end"

image anim_rain_ep9 = Movie(play="%s/movies/ep9/anim_rain_ep9.webm" % persistent.img_dir, start_image="anim_rain_ep9_start", channel = "sex7")

image anim_intro_ep9 = Movie(play="%s/movies/ep9/anim_intro_ep9.webm" % persistent.img_dir, start_image="anim_intro_ep9_start", channel = "sex8", loop=False)
image bg anim_intro_ep9 movie:
    "anim_intro_ep9"
    function play_intro_ep9
    pause 35
    function play_scary_intro_ep9
    pause 29.67
    "anim_intro_ep9_end"

image anim_halloween_ep9 = Movie(play="%s/movies/ep9/anim_halloween_ep9.webm" % persistent.img_dir, start_image="anim_halloween_ep9_start", channel = "sex9", loop=False)
image bg anim_halloween_ep9 movie:
    "anim_halloween_ep9"
    pause 65.33
    "anim_halloween_ep9_end"

image anim_pan_leon_ep9 = Movie(play="%s/movies/ep9/anim_pan_leon_ep9.webm" % persistent.img_dir, start_image="anim_pan_leon_ep9_start", channel = "sex10", loop=False)
image bg anim_pan_leon_ep9 movie:
    "anim_pan_leon_ep9"
    pause 5
    "anim_pan_leon_ep9_end"

image anim_jamie_trick_ep9 = Movie(play="%s/movies/ep9/anim_jamie_trick_ep9.webm" % persistent.img_dir, start_image="anim_jamie_trick_ep9_start", channel = "sex11", loop=False)
image bg anim_jamie_trick_ep9 movie:
    "anim_jamie_trick_ep9"
    pause 4
    "anim_jamie_trick_ep9_end"

image anim_haunted_hand_ep9 = Movie(play="%s/movies/ep9/anim_haunted_hand_ep9.webm" % persistent.img_dir, start_image="anim_haunted_hand_ep9_start", channel = "sex12", loop=False)
image bg anim_haunted_hand_ep9 movie:
    "anim_haunted_hand_ep9"
    pause 4
    "anim_haunted_hand_ep9_end"

image anim_camila_dance_ep9 = Movie(play="%s/movies/ep9/anim_camila_dance_ep9.webm" % persistent.img_dir, start_image="anim_camila_dance_ep9_start", channel = "sex1")
image anim_camila_dance2_ep9 = Movie(play="%s/movies/ep9/anim_camila_dance2_ep9.webm" % persistent.img_dir, start_image="anim_camila_dance2_ep9_start", channel = "sex2")
image anim_camila_dance3_ep9 = Movie(play="%s/movies/ep9/anim_camila_dance3_ep9.webm" % persistent.img_dir, start_image="anim_camila_dance3_ep9_start", channel = "sex3")
image anim_camila_dance4_ep9 = Movie(play="%s/movies/ep9/anim_camila_dance4_ep9.webm" % persistent.img_dir, start_image="anim_camila_dance4_ep9_start", channel = "sex4")
image anim_camila_dance5_ep9 = Movie(play="%s/movies/ep9/anim_camila_dance5_ep9.webm" % persistent.img_dir, start_image="anim_camila_dance5_ep9_start", channel = "sex5")

image anim_heather_idle_ep9 = Movie(play="%s/movies/ep9/anim_heather_idle_ep9.webm" % persistent.img_dir, start_image = "anim_heather_idle_ep9_start", channel = "sex1")
image anim_heather_idle2_ep9 = Movie(play="%s/movies/ep9/anim_heather_idle2_ep9.webm" % persistent.img_dir, start_image="anim_heather_idle2_ep9_start", channel = "sex2")
image anim_heather_bj_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj_ep9_start", channel = "sex3")
image anim_heather_bj2_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj2_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj2_ep9_start", channel = "sex4")
image anim_heather_bj3_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj3_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj3_ep9_start", channel = "sex5")
image anim_heather_bj4_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj4_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj4_ep9_start", channel = "sex6")
image anim_heather_bj5_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj5_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj5_ep9_start", channel = "sex7")
image anim_heather_bj6_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj6_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj6_ep9_start", channel = "sex8")
image anim_heather_bj7_ep9 = Movie(play="%s/movies/ep9/anim_heather_bj7_ep9.webm" % persistent.img_dir, start_image="anim_heather_bj7_ep9_start", channel = "sex9")
image anim_heather_boobjob_ep9 = Movie(play="%s/movies/ep9/anim_heather_boobjob_ep9.webm" % persistent.img_dir, start_image="anim_heather_boobjob_ep9_start", channel = "sex10")
image anim_heather_boobjob2_ep9 = Movie(play="%s/movies/ep9/anim_heather_boobjob2_ep9.webm" % persistent.img_dir, start_image="anim_heather_boobjob2_ep9_start", channel = "sex11")
image anim_heather_boobjob3_ep9 = Movie(play="%s/movies/ep9/anim_heather_boobjob3_ep9.webm" % persistent.img_dir, start_image="anim_heather_boobjob3_ep9_start", channel = "sex12")
image anim_heather_boobjob4_ep9 = Movie(play="%s/movies/ep9/anim_heather_boobjob4_ep9.webm" % persistent.img_dir, start_image="anim_heather_boobjob4_ep9_start", channel = "sex13")
image anim_heather_boobjob5_ep9 = Movie(play="%s/movies/ep9/anim_heather_boobjob5_ep9.webm" % persistent.img_dir, start_image="anim_heather_boobjob5_ep9_start", channel = "sex14")

image anim_bella_tits_ep9 = Movie(play="%s/movies/ep9/anim_bella_tits_ep9.webm" % persistent.img_dir, start_image="anim_bella_tits_ep9_start", channel = "sex1")
image anim_bella_tits2_ep9 = Movie(play="%s/movies/ep9/anim_bella_tits2_ep9.webm" % persistent.img_dir, start_image="anim_bella_tits2_ep9_start", channel = "sex2")
image anim_bella_tits3_ep9 = Movie(play="%s/movies/ep9/anim_bella_tits3_ep9.webm" % persistent.img_dir, start_image="anim_bella_tits3_ep9_start", channel = "sex3")
image anim_bella_kiss_ep9 = Movie(play="%s/movies/ep9/anim_bella_kiss1_ep9.webm" % persistent.img_dir, start_image="anim_bella_kiss_ep9_start", channel = "sex4")
image anim_bella_kiss2_ep9 = Movie(play="%s/movies/ep9/anim_bella_kiss2_ep9.webm" % persistent.img_dir, start_image="anim_bella_kiss2_ep9_start", channel = "sex5")
image anim_bella_kiss3_ep9 = Movie(play="%s/movies/ep9/anim_bella_kiss3_ep9.webm" % persistent.img_dir, start_image="anim_bella_kiss3_ep9_start", channel = "sex6")
image anim_bella_dance_ep9 = Movie(play="%s/movies/ep9/anim_bella_dance_ep9.webm" % persistent.img_dir, start_image="anim_bella_dance_ep9_start", channel = "sex7")
image anim_bella_dance2_ep9 = Movie(play="%s/movies/ep9/anim_bella_dance2_ep9.webm" % persistent.img_dir, start_image="anim_bella_dance2_ep9_start", channel = "sex8")
image anim_bella_lick_ep9 = Movie(play="%s/movies/ep9/anim_bella_lick_ep9.webm" % persistent.img_dir, start_image="anim_bella_lick_ep9_start", channel = "sex9")
image anim_bella_finger_ep9 = Movie(play="%s/movies/ep9/anim_bella_finger_ep9.webm" % persistent.img_dir, start_image="anim_bella_finger_ep9_start", channel = "sex10")
image anim_bella_footjob_ep9 = Movie(play="%s/movies/ep9/anim_bella_footjob_ep9.webm" % persistent.img_dir, start_image="anim_bella_footjob_ep9_start", channel = "sex11")
image anim_bella_hj_ep9 = Movie(play="%s/movies/ep9/anim_bella_hj_ep9.webm" % persistent.img_dir, start_image="anim_bella_hj_ep9_start", channel = "sex12")
image anim_bella_hj2_ep9 = Movie(play="%s/movies/ep9/anim_bella_hj2_ep9.webm" % persistent.img_dir, start_image="anim_bella_hj2_ep9_start", channel = "sex13")
image anim_bella_hj3_ep9 = Movie(play="%s/movies/ep9/anim_bella_hj3_ep9.webm" % persistent.img_dir, start_image="anim_bella_hj3_ep9_start", channel = "sex14")
image anim_bella_bj1_ep9 = Movie(play="%s/movies/ep9/anim_bella_bj1_ep9.webm" % persistent.img_dir, start_image="anim_bella_bj1_ep9_start", channel = "sex15")
image anim_bella_bj2_ep9 = Movie(play="%s/movies/ep9/anim_bella_bj2_ep9.webm" % persistent.img_dir, start_image="anim_bella_bj2_ep9_start", channel = "sex16")
image anim_bella_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_bella_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_bella_doggy1_ep9_start", channel = "sex17")
image anim_bella_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_bella_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_bella_doggy2_ep9_start", channel = "sex18")
image anim_bella_side_ep9 = Movie(play="%s/movies/ep9/anim_bella_side_ep9.webm" % persistent.img_dir, start_image="anim_bella_side_ep9_start", channel = "sex19")
image anim_bella_side2_ep9 = Movie(play="%s/movies/ep9/anim_bella_side2_ep9.webm" % persistent.img_dir, start_image="anim_bella_side2_ep9_start", channel = "sex20")
image anim_bella_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_bella_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_bella_doggy3_ep9_start", channel = "sex1")
image anim_bella_doggy4_ep9 = Movie(play="%s/movies/ep9/anim_bella_doggy4_ep9.webm" % persistent.img_dir, start_image="anim_bella_doggy4_ep9_start", channel = "sex2")
image anim_bella_rev1_ep9 = Movie(play="%s/movies/ep9/anim_bella_rev1_ep9.webm" % persistent.img_dir, start_image="anim_bella_rev1_ep9_start", channel = "sex3")
image anim_bella_rev2_ep9 = Movie(play="%s/movies/ep9/anim_bella_rev2_ep9.webm" % persistent.img_dir, start_image="anim_bella_rev2_ep9_start", channel = "sex4")
image anim_bella_slip_ep9 = Movie(play="%s/movies/ep9/anim_bella_slip_ep9.webm" % persistent.img_dir, start_image="anim_bella_slip_ep9_start", channel = "sex5", loop=False)
image anim_bella_bj_cum_ep9 = Movie(play="%s/movies/ep9/anim_bella_bj_cum_ep9.webm" % persistent.img_dir, start_image="anim_bella_bj_cum_ep9_start", channel = "sex6")
image anim_bella_cum_ep9 = Movie(play="%s/movies/ep9/anim_bella_cum_ep9.webm" % persistent.img_dir, start_image="anim_bella_cum_ep9_start", channel = "sex7")
image bg anim_bella_slip_ep9 movie:
    "anim_bella_slip_ep9"
    pause 4
    "anim_bella_slip_ep9_end"

image anim_bella_ride1_ep9 = Movie(play="%s/movies/ep9/anim_bella_ride1_ep9.webm" % persistent.img_dir, start_image="anim_bella_ride1_ep9_start", channel = "sex1")
image anim_bella_ride2_ep9 = Movie(play="%s/movies/ep9/anim_bella_ride2_ep9.webm" % persistent.img_dir, start_image="anim_bella_ride2_ep9_start", channel = "sex2")
image anim_bella_ride3_ep9 = Movie(play="%s/movies/ep9/anim_bella_ride3_ep9.webm" % persistent.img_dir, start_image="anim_bella_ride3_ep9_start", channel = "sex3")
image anim_bella_ride4_ep9 = Movie(play="%s/movies/ep9/anim_bella_ride4_ep9.webm" % persistent.img_dir, start_image="anim_bella_ride4_ep9_start", channel = "sex4")

image anim_jill_branch_ep9 = Movie(play="%s/movies/ep9/anim_jill_branch_ep9.webm" % persistent.img_dir, start_image = "anim_jill_branch_ep9_start", channel = "sex1")
image anim_jill_kiss_ep9 = Movie(play="%s/movies/ep9/anim_jill_kiss_ep9.webm" % persistent.img_dir, start_image="anim_jill_kiss_ep9_start", channel = "sex2")
image anim_jill_tits_ep9 = Movie(play="%s/movies/ep9/anim_jill_tits_ep9.webm" % persistent.img_dir, start_image="anim_jill_tits_ep9_start", channel = "sex3")
image anim_jill_thigh_ep9 = Movie(play="%s/movies/ep9/anim_jill_thigh_ep9.webm" % persistent.img_dir, start_image="anim_jill_thigh_ep9_start", channel = "sex4")
image anim_jill_thigh4_ep9 = Movie(play="%s/movies/ep9/anim_jill_thigh4_ep9.webm" % persistent.img_dir, start_image="anim_jill_thigh4_ep9_start", channel = "sex5")
image anim_jill_thigh2_ep9 = Movie(play="%s/movies/ep9/anim_jill_thigh2_ep9.webm" % persistent.img_dir, start_image="anim_jill_thigh2_ep9_start", channel = "sex6")
image anim_jill_thigh3_ep9 = Movie(play="%s/movies/ep9/anim_jill_thigh3_ep9.webm" % persistent.img_dir, start_image="anim_jill_thigh3_ep9_start", channel = "sex7")
image anim_jill_thigh_cum_ep9 = Movie(play="%s/movies/ep9/anim_jill_thigh_cum_ep9.webm" % persistent.img_dir, start_image = "anim_jill_thigh_cum_ep9_start", channel = "sex8")
image anim_jill_asscheeks_ep9 = Movie(play="%s/movies/ep9/anim_jill_asscheeks_ep9.webm" % persistent.img_dir, start_image="anim_jill_asscheeks_ep9_start", channel = "sex9")
image anim_jill_asscheeks2_ep9 = Movie(play="%s/movies/ep9/anim_jill_asscheeks2_ep9.webm" % persistent.img_dir, start_image="anim_jill_asscheeks2_ep9_start", channel = "sex10")
image anim_jill_asscheeks3_ep9 = Movie(play="%s/movies/ep9/anim_jill_asscheeks3_ep9.webm" % persistent.img_dir, start_image="anim_jill_asscheeks3_ep9_start", channel = "sex11")
image anim_jill_lick_ep9 = Movie(play="%s/movies/ep9/anim_jill_lick_ep9.webm" % persistent.img_dir, start_image="anim_jill_lick_ep9_start", channel = "sex12")
image anim_jill_lick2_ep9 = Movie(play="%s/movies/ep9/anim_jill_lick2_ep9.webm" % persistent.img_dir, start_image="anim_jill_lick2_ep9_start", channel = "sex13")
image anim_jill_lick3_ep9 = Movie(play="%s/movies/ep9/anim_jill_lick3_ep9.webm" % persistent.img_dir, start_image="anim_jill_lick3_ep9_start", channel = "sex14")
image anim_jill_rub_ep9 = Movie(play="%s/movies/ep9/anim_jill_rub_ep9.webm" % persistent.img_dir, start_image="anim_jill_rub_ep9_start", channel = "sex15")
image anim_jill_rub2_ep9 = Movie(play="%s/movies/ep9/anim_jill_rub2_ep9.webm" % persistent.img_dir, start_image="anim_jill_rub2_ep9_start", channel = "sex16")
image anim_jill_feet_ep9 = Movie(play="%s/movies/ep9/anim_jill_feet_ep9.webm" % persistent.img_dir, start_image="anim_jill_feet_ep9_start", channel = "sex17")
image anim_jill_hj1_ep9 = Movie(play="%s/movies/ep9/anim_jill_hj1_ep9.webm" % persistent.img_dir, start_image="anim_jill_hj1_ep9_start", channel = "sex18")
image anim_jill_boobjob1_ep9 = Movie(play="%s/movies/ep9/anim_jill_boobjob1_ep9.webm" % persistent.img_dir, start_image="anim_jill_boobjob1_ep9_start", channel = "sex19")
image anim_jill_boobjob2_ep9 = Movie(play="%s/movies/ep9/anim_jill_boobjob2_ep9.webm" % persistent.img_dir, start_image="anim_jill_boobjob2_ep9_start", channel = "sex20")
image anim_jill_mouth2_ep9 = Movie(play="%s/movies/ep9/anim_jill_mouth2_ep9.webm" % persistent.img_dir, start_image="anim_jill_mouth2_ep9_start", channel = "sex1")
image anim_jill_mouth_ep9 = Movie(play="%s/movies/ep9/anim_jill_mouth_ep9.webm" % persistent.img_dir, start_image="anim_jill_mouth_ep9_start", channel = "sex2")
image anim_jill_insert_ep9 = Movie(play="%s/movies/ep9/anim_jill_insert_ep9.webm" % persistent.img_dir, start_image="anim_jill_insert_ep9_start", channel = "sex3", loop=False)
image bg anim_jill_insert_ep9 movie:
    "anim_jill_insert_ep9"
    pause 4
    "anim_jill_insert_ep9_end"
image anim_jill_miss_ep9 = Movie(play="%s/movies/ep9/anim_jill_miss_ep9.webm" % persistent.img_dir, start_image="anim_jill_miss_ep9_start", channel = "sex4")
image anim_jill_doggy_ep9 = Movie(play="%s/movies/ep9/anim_jill_doggy_ep9.webm" % persistent.img_dir, start_image="anim_jill_doggy_ep9_start", channel = "sex5")
image anim_jill_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_jill_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_jill_doggy2_ep9_start", channel = "sex6")
image anim_jill_standing_ep9 = Movie(play="%s/movies/ep9/anim_jill_standing_ep9.webm" % persistent.img_dir, start_image="anim_jill_standing_ep9_start", channel = "sex7")
image anim_jill_standing2_ep9 = Movie(play="%s/movies/ep9/anim_jill_standing2_ep9.webm" % persistent.img_dir, start_image="anim_jill_standing2_ep9_start", channel = "sex8")
image anim_jill_rev_ep9 = Movie(play="%s/movies/ep9/anim_jill_rev_ep9.webm" % persistent.img_dir, start_image="anim_jill_rev_ep9_start", channel = "sex9")
image anim_jill_rev2_ep9 = Movie(play="%s/movies/ep9/anim_jill_rev2_ep9.webm" % persistent.img_dir, start_image="anim_jill_rev2_ep9_start", channel = "sex10")
image anim_jill_cum_tits_ep9 = Movie(play="%s/movies/ep9/anim_jill_cum_tits_ep9.webm" % persistent.img_dir, start_image="anim_jill_cum_tits_ep9_start", channel = "sex11")

image anim_sage_wakeup_ep9 = Movie(play="%s/movies/ep9/anim_sage_wakeup_ep9.webm" % persistent.img_dir, start_image="anim_sage_wakeup_ep9_start", channel = "sex1")
image anim_sage_grab_ep9 = Movie(play="%s/movies/ep9/anim_sage_grab_ep9.webm" % persistent.img_dir, start_image="anim_sage_grab_ep9_start", channel = "sex2")
image anim_sage_branch_miss_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_miss_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_miss_ep9_start", channel = "sex3")
image anim_sage_branch_miss2_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_miss2_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_miss2_ep9_start", channel = "sex4")
image anim_sage_branch_miss3_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_miss3_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_miss3_ep9_start", channel = "sex5")
image anim_sage_branch_ride1_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_ride1_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_ride1_ep9_start", channel = "sex6")
image anim_sage_branch_ride2_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_ride2_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_ride2_ep9_start", channel = "sex7")
image anim_sage_branch_ride3_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_ride3_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_ride3_ep9_start", channel = "sex8")
image anim_sage_branch_ride4_ep9 = Movie(play="%s/movies/ep9/anim_sage_branch_ride4_ep9.webm" % persistent.img_dir, start_image="anim_sage_branch_ride4_ep9_start", channel = "sex9")
image anim_sage_lap_ep9 = Movie(play="%s/movies/ep9/anim_sage_lap_ep9.webm" % persistent.img_dir, start_image="anim_sage_lap_ep9_start", channel = "sex10")
image anim_sage_lap2_ep9 = Movie(play="%s/movies/ep9/anim_sage_lap2_ep9.webm" % persistent.img_dir, start_image="anim_sage_lap2_ep9_start", channel = "sex11")
image anim_sage_lap3_ep9 = Movie(play="%s/movies/ep9/anim_sage_lap3_ep9.webm" % persistent.img_dir, start_image="anim_sage_lap3_ep9_start", channel = "sex12")
image anim_jade_ride_ep9 = Movie(play="%s/movies/ep9/anim_jade_ride_ep9.webm" % persistent.img_dir, start_image="anim_jade_ride_ep9_start", channel = "sex13")
image anim_sage_talk_ep9 = Movie(play="%s/movies/ep9/anim_sage_talk_ep9.webm" % persistent.img_dir, start_image="anim_sage_talk_ep9_start", channel = "sex14")
image anim_sage_talk2_ep9 = Movie(play="%s/movies/ep9/anim_sage_talk2_ep9.webm" % persistent.img_dir, start_image="anim_sage_talk2_ep9_start", channel = "sex15", loop=False)
image bg anim_sage_talk2_ep9 movie:
    "anim_sage_talk2_ep9"
    pause 1
    "anim_sage_talk2_ep9_end"
image anim_sage_hm_bj_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_bj_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_bj_ep9_start", channel = "sex16")
image anim_sage_hm_bj2_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_bj2_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_bj2_ep9_start", channel = "sex17")
image anim_sage_hm_bj3_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_bj3_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_bj3_ep9_start", channel = "sex18")
image anim_sage_hm_spank_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_spank_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_spank_ep9_start", channel = "sex19")
image bg anim_sage_hm_spank_ep9 movie:
    "anim_sage_hm_spank_ep9"
    pause 0.5
    function play_slap_ep9
    pause 1.75
    repeat
image anim_sage_hm_fuck1_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_fuck1_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_fuck1_ep9_start", channel = "sex1")
image anim_sage_hm_fuck2_ep9 = Movie(play="%s/movies/ep9/anim_sage_hm_fuck2_ep9.webm" % persistent.img_dir, start_image="anim_sage_hm_fuck2_ep9_start", channel = "sex2")
image anim_sage_lewd_plug_ep9 = Movie(play="%s/movies/ep9/anim_sage_lewd_plug_ep9.webm" % persistent.img_dir, start_image="anim_sage_lewd_plug_ep9_start", channel = "sex3", loop=False)
image bg anim_sage_lewd_plug_ep9 movie:
    "anim_sage_lewd_plug_ep9"
    pause 4
    "anim_sage_lewd_plug_ep9_end"
image bg anim_sage_lewd_plug3_ep9 movie:
    "anim_sage_lewd_plug3_ep9"
    pause 4
    "anim_sage_lewd_plug3_ep9_end"
image anim_sage_lewd_plug2_ep9 = Movie(play="%s/movies/ep9/anim_sage_lewd_plug2_ep9.webm" % persistent.img_dir, start_image="anim_sage_lewd_plug2_ep9_start", channel = "sex4")
image anim_sage_lewd_plug3_ep9 = Movie(play="%s/movies/ep9/anim_sage_lewd_plug3_ep9.webm" % persistent.img_dir, start_image="anim_sage_lewd_plug3_ep9_start", channel = "sex5", loop=False)
image anim_anal_sage_bj_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_bj_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_bj_ep9_start", channel = "sex6")
image anim_anal_sage_mast_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_mast_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_mast_ep9_start", channel = "sex7")
image anim_anal_sage_mast2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_mast2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_mast2_ep9_start", channel = "sex8")
image anim_anal_sage_finger1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_finger1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_finger1_ep9_start", channel = "sex9")
image anim_anal_sage_finger2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_finger2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_finger2_ep9_start", channel = "sex10")
image anim_anal_sage_finger3_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_finger3_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_finger3_ep9_start", channel = "sex11")
image anim_anal_sage_spank1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_spank1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_spank1_ep9_start", channel = "sex12")
image anim_anal_sage_spank2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_spank2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_spank2_ep9_start", channel = "sex13")
image bg anim_anal_sage_spank1_ep9 movie:
    "anim_anal_sage_spank1_ep9"
    pause 1.9
    function play_slap_ep9
    pause 2.1
    repeat
image bg anim_anal_sage_spank2_ep9 movie:
    "anim_anal_sage_spank2_ep9"
    pause 1.9
    function play_slap_ep9
    pause 2.1
    repeat

image anim_anal_sage_rub_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rub_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rub_ep9_start", channel = "sex14")
image anim_anal_sage_tease_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_tease_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_tease_ep9_start", channel = "sex15")
image anim_anal_sage_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_doggy1_ep9_start", channel = "sex16")
image anim_anal_sage_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_doggy2_ep9_start", channel = "sex17")
image anim_anal_sage_side1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_side1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_side1_ep9_start", channel = "sex18")
image anim_anal_sage_side2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_side2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_side2_ep9_start", channel = "sex19")
image anim_anal_sage_side3_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_side3_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_side3_ep9_start", channel = "sex20")
image anim_anal_sage_cg1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_cg1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_cg1_ep9_start", channel = "sex1")
image anim_anal_sage_cg2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_cg2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_cg2_ep9_start", channel = "sex2")
image anim_anal_sage_cg3_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_cg3_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_cg3_ep9_start", channel = "sex3")
image anim_anal_sage_rev1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rev1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rev1_ep9_start", channel = "sex4")
image anim_anal_sage_rev2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rev2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rev2_ep9_start", channel = "sex5")
image anim_anal_sage_rev3_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rev3_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rev3_ep9_start", channel = "sex6")
image anim_anal_sage_rev4_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rev4_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rev4_ep9_start", channel = "sex7")
image anim_anal_sage_rev5_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_rev5_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_rev5_ep9_start", channel = "sex8")
image anim_anal_sage_ride1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_ride1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_ride1_ep9_start", channel = "sex9")
image anim_anal_sage_ride2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_ride2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_ride2_ep9_start", channel = "sex10")
image anim_anal_sage_stand1_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_stand1_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_stand1_ep9_start", channel = "sex11")
image anim_anal_sage_stand2_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_stand2_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_stand2_ep9_start", channel = "sex12")
image anim_anal_sage_stand3_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_stand3_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_stand3_ep9_start", channel = "sex13")
image anim_anal_sage_cum_ep9 = Movie(play="%s/movies/ep9/anim_anal_sage_cum_ep9.webm" % persistent.img_dir, start_image="anim_anal_sage_cum_ep9_start", channel = "sex14", loop=False)
image bg anim_anal_sage_cum_ep9 movie:
    "anim_anal_sage_cum_ep9"
    pause 16.67
    "anim_anal_sage_cum_ep9_end"

image anim_jade_finger_ep9 = Movie(play="%s/movies/ep9/anim_jade_finger_ep9.webm" % persistent.img_dir, start_image="anim_jade_finger_ep9_start", channel = "sex1")
image anim_jade_finger_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_finger_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_finger_ass_ep9_start", channel = "sex2")
image anim_jade_finger2_ep9 = Movie(play="%s/movies/ep9/anim_jade_finger2_ep9.webm" % persistent.img_dir, start_image="anim_jade_finger2_ep9_start", channel = "sex3")
image anim_jade_finger2_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_finger2_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_finger2_ass_ep9_start", channel = "sex4")
image anim_jade_insert_ep9 = Movie(play="%s/movies/ep9/anim_jade_insert_ep9.webm" % persistent.img_dir, start_image="anim_jade_insert_ep9_start", channel = "sex5", loop=False)
image anim_jade_insert_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_insert_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_insert_ass_ep9_start", channel = "sex6", loop=False)
image bg anim_jade_insert_ep9 movie:
    "anim_jade_insert_ep9"
    pause 4
    "anim_jade_insert_ep9_end"
image bg anim_jade_insert_ass_ep9 movie:
    "anim_jade_insert_ass_ep9"
    pause 4
    "anim_jade_insert_ass_ep9_end"
image anim_jade_doggy_ep9 = Movie(play="%s/movies/ep9/anim_jade_doggy_ep9.webm" % persistent.img_dir, start_image="anim_jade_doggy_ep9_start", channel = "sex7")
image anim_jade_doggy_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_doggy_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_doggy_ass_ep9_start", channel = "sex8")
image anim_jade_doggy2_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_doggy2_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_doggy2_ass_ep9_start", channel = "sex9")
image anim_jade_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_jade_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_jade_doggy3_ep9_start", channel = "sex10")
image anim_jade_doggy3_ass_ep9 = Movie(play="%s/movies/ep9/anim_jade_doggy3_ass_ep9.webm" % persistent.img_dir, start_image="anim_jade_doggy3_ass_ep9_start", channel = "sex11")

image anim_nora_idle_ep9 = Movie(play="%s/movies/ep9/anim_nora_idle_ep9.webm" % persistent.img_dir, start_image="anim_nora_idle_ep9_start", channel = "sex1")

image anim_quinn_finger_ep9 = Movie(play="%s/movies/ep9/anim_quinn_finger_ep9.webm" % persistent.img_dir, start_image="anim_quinn_finger_ep9_start", channel = "sex1")
image anim_quinn_finger2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_finger2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_finger2_ep9_start", channel = "sex2")
image anim_quinn_finger_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_finger_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_finger_anal_ep9_start", channel = "sex3")
image anim_quinn_spank_ep9 = Movie(play="%s/movies/ep9/anim_quinn_spank_ep9.webm" % persistent.img_dir, start_image="anim_quinn_spank_ep9_start", channel = "sex4")
image anim_quinn_spank2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_spank2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_spank2_ep9_start", channel = "sex5")
image anim_quinn_spank3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_spank3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_spank3_ep9_start", channel = "sex6")
image bg anim_quinn_spank_ep9 movie:
    "anim_quinn_spank_ep9"
    pause 2.7
    function play_slap_ep9
    pause 1.3
    repeat
image bg anim_quinn_spank2_ep9 movie:
    "anim_quinn_spank2_ep9"
    pause 2.7
    function play_slap_ep9
    pause 1.3
    repeat
image bg anim_quinn_spank3_ep9 movie:
    "anim_quinn_spank3_ep9"
    pause 2.7
    function play_slap_ep9
    pause 1.3
    repeat
image anim_quinn_doggy_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_doggy_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_doggy_anal_ep9_start", channel = "sex7")
image anim_quinn_doggy_anal2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_doggy_anal2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_doggy_anal2_ep9_start", channel = "sex8")
image anim_quinn_doggy_anal3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_doggy_anal3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_doggy_anal3_ep9_start", channel = "sex9")
image anim_quinn_doggy_ep9 = Movie(play="%s/movies/ep9/anim_quinn_doggy_ep9.webm" % persistent.img_dir, start_image="anim_quinn_doggy_ep9_start", channel = "sex10")
image anim_quinn_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_doggy2_ep9_start", channel = "sex11")
image anim_quinn_miss_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_ep9_start", channel = "sex12")
image anim_quinn_miss2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss2_ep9_start", channel = "sex13")
image anim_quinn_miss3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss3_ep9_start", channel = "sex14")
image anim_quinn_miss_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_anal_ep9_start", channel = "sex15")
image anim_quinn_miss_anal2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_anal2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_anal2_ep9_start", channel = "sex16")
image anim_quinn_miss_anal3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_anal3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_anal3_ep9_start", channel = "sex17")
image anim_quinn_stand_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand_ep9_start", channel = "sex18")
image anim_quinn_stand2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand2_ep9_start", channel = "sex19")
image anim_quinn_stand3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand3_ep9_start", channel = "sex20")
image anim_quinn_stand_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand_anal_ep9_start", channel = "sex1")
image anim_quinn_stand_anal2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand_anal2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand_anal2_ep9_start", channel = "sex2")
image anim_quinn_ride_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride_anal_ep9_start", channel = "sex3")
image anim_quinn_ride2_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride2_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride2_anal_ep9_start", channel = "sex4")
image anim_quinn_ride3_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride3_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride3_anal_ep9_start", channel = "sex5")
image anim_quinn_ride_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride_ep9_start", channel = "sex6")
image anim_quinn_ride2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride2_ep9_start", channel = "sex7")
image anim_quinn_ride3_ep9 = Movie(play="%s/movies/ep9/anim_quinn_ride3_ep9.webm" % persistent.img_dir, start_image="anim_quinn_ride3_ep9_start", channel = "sex8")
image anim_quinn_behind_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_behind_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_behind_anal_ep9_start", channel = "sex9")
image anim_quinn_behind_anal2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_behind_anal2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_behind_anal2_ep9_start", channel = "sex10")
image anim_quinn_behind_ep9 = Movie(play="%s/movies/ep9/anim_quinn_behind_ep9.webm" % persistent.img_dir, start_image="anim_quinn_behind_ep9_start", channel = "sex11")
image anim_quinn_behind2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_behind2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_behind2_ep9_start", channel = "sex12")
image anim_quinn_miss_sub_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_sub_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_sub_ep9_start", channel = "sex13")
image anim_quinn_miss_sub2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_miss_sub2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_miss_sub2_ep9_start", channel = "sex14")
image anim_quinn_stand_sub_anal_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand_sub_anal_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand_sub_anal_ep9_start", channel = "sex15")
image anim_quinn_stand_sub_anal2_ep9 = Movie(play="%s/movies/ep9/anim_quinn_stand_sub_anal2_ep9.webm" % persistent.img_dir, start_image="anim_quinn_stand_sub_anal2_ep9_start", channel = "sex16")
image anim_quinn_bj_sub_ep9 = Movie(play="%s/movies/ep9/anim_quinn_bj_sub_ep9.webm" % persistent.img_dir, start_image="anim_quinn_bj_sub_ep9_start", channel = "sex17")
image anim_quinn_bj_ep9 = Movie(play="%s/movies/ep9/anim_quinn_bj_ep9.webm" % persistent.img_dir, start_image="anim_quinn_bj_ep9_start", channel = "sex18")

image anim_lily_finger_ep9 = Movie(play="%s/movies/ep9/anim_lily_finger_ep9.webm" % persistent.img_dir, start_image="anim_lily_finger_ep9_start", channel = "sex1")
image anim_lily_finger_ass_ep9 = Movie(play="%s/movies/ep9/anim_lily_finger_ass_ep9.webm" % persistent.img_dir, start_image="anim_lily_finger_ass_ep9_start", channel = "sex2")
image anim_lily_dildo_ass_ep9 = Movie(play="%s/movies/ep9/anim_lily_dildo_ass_ep9.webm" % persistent.img_dir, start_image="anim_lily_dildo_ass_ep9_start", channel = "sex3")
image anim_lily_dildo_ep9 = Movie(play="%s/movies/ep9/anim_lily_dildo_ep9.webm" % persistent.img_dir, start_image="anim_lily_dildo_ep9_start", channel = "sex4")
image anim_lily_idle_ep9 = Movie(play="%s/movies/ep9/anim_lily_idle_ep9.webm" % persistent.img_dir, start_image="anim_lily_idle_ep9_start", channel = "sex5")

image anim_mel_sarah_squeeze1_ep9 = Movie(play="%s/movies/ep9/anim_mel_sarah_squeeze1_ep9.webm" % persistent.img_dir, start_image="anim_mel_sarah_squeeze1_ep9_start", channel = "sex1")
image anim_mel_sarah_squeeze2_ep9 = Movie(play="%s/movies/ep9/anim_mel_sarah_squeeze2_ep9.webm" % persistent.img_dir, start_image="anim_mel_sarah_squeeze2_ep9_start", channel = "sex2")
image anim_mel_sarah_squeeze3_ep9 = Movie(play="%s/movies/ep9/anim_mel_sarah_squeeze3_ep9.webm" % persistent.img_dir, start_image="anim_mel_sarah_squeeze3_ep9_start", channel = "sex3")
image anim_mel_sarah_squeeze4_ep9 = Movie(play="%s/movies/ep9/anim_mel_sarah_squeeze4_ep9.webm" % persistent.img_dir, start_image="anim_mel_sarah_squeeze4_ep9_start", channel = "sex4")
image anim_sarah_anal_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_sarah_anal_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_sarah_anal_doggy1_ep9_start", channel = "sex1")
image anim_sarah_anal_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_sarah_anal_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_sarah_anal_doggy2_ep9_start", channel = "sex2")
image anim_sarah_anal_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_sarah_anal_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_sarah_anal_doggy3_ep9_start", channel = "sex3")
image anim_sarah_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_sarah_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_sarah_doggy1_ep9_start", channel = "sex4")
image anim_sarah_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_sarah_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_sarah_doggy2_ep9_start", channel = "sex5")
image anim_sarah_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_sarah_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_sarah_doggy3_ep9_start", channel = "sex6")
image anim_melanie_anal_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_melanie_anal_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_melanie_anal_doggy1_ep9_start", channel = "sex7")
image anim_melanie_anal_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_melanie_anal_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_melanie_anal_doggy2_ep9_start", channel = "sex8")
image anim_mel_anal_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_mel_anal_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_mel_anal_doggy3_ep9_start", channel = "sex9")
image anim_mel_doggy3b_ep9 = Movie(play="%s/movies/ep9/anim_mel_doggy3b_ep9.webm" % persistent.img_dir, start_image="anim_mel_doggy3b_ep9_start", channel = "sex10")
image anim_mel_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_mel_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_mel_doggy3_ep9_start", channel = "sex11")
image anim_melanie_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_melanie_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_melanie_doggy1_ep9_start", channel = "sex12")
image anim_melanie_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_melanie_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_melanie_doggy2_ep9_start", channel = "sex13")
image anim_sm_bj1_ep9 = Movie(play="%s/movies/ep9/anim_sm_bj1_ep9.webm" % persistent.img_dir, start_image="anim_sm_bj1_ep9_start", channel = "sex14")
image anim_sm_bj2_ep9 = Movie(play="%s/movies/ep9/anim_sm_bj2_ep9.webm" % persistent.img_dir, start_image="anim_sm_bj2_ep9_start", channel = "sex15")
image anim_sm_bj3_ep9 = Movie(play="%s/movies/ep9/anim_sm_bj3_ep9.webm" % persistent.img_dir, start_image="anim_sm_bj3_ep9_start", channel = "sex16")
image anim_sm_bj4_ep9 = Movie(play="%s/movies/ep9/anim_sm_bj4_ep9.webm" % persistent.img_dir, start_image="anim_sm_bj4_ep9_start", channel = "sex17")
image anim_cum1_ep9 = Movie(play="%s/movies/ep9/anim_cum1_ep9.webm" % persistent.img_dir, start_image="anim_cum1_ep9_start", channel = "sex18")
image anim_cum2_ep9 = Movie(play="%s/movies/ep9/anim_cum2_ep9.webm" % persistent.img_dir, start_image="anim_cum2_ep9_start", channel = "sex19")
image anim_sarah_anal_rev_ep9 = Movie(play="%s/movies/ep9/anim_sarah_anal_rev_ep9.webm" % persistent.img_dir, start_image="anim_sarah_anal_rev_ep9_start", channel = "sex20")
image anim_sarah_rev_ep9 = Movie(play="%s/movies/ep9/anim_sarah_rev_ep9.webm" % persistent.img_dir, start_image="anim_sarah_rev_ep9_start", channel = "sex1")
image anim_mel_anal_rev_ep9 = Movie(play="%s/movies/ep9/anim_mel_anal_rev_ep9.webm" % persistent.img_dir, start_image="anim_mel_anal_rev_ep9_start", channel = "sex2")
image anim_mel_rev_ep9 = Movie(play="%s/movies/ep9/anim_mel_rev_ep9.webm" % persistent.img_dir, start_image="anim_mel_rev_ep9_start", channel = "sex3")
image anim_sm_ending_ep9 = Movie(play="%s/movies/ep9/anim_sm_ending_ep9.webm" % persistent.img_dir, start_image="anim_sm_ending_ep9_start", channel = "sex4", loop=False)
image bg anim_sm_ending_ep9 movie:
    "anim_sm_ending_ep9"
    pause 4
    "anim_sm_ending_ep9_end"

image anim_cumpetition_1_ep9 = Movie(play="%s/movies/ep9/anim_cumpetition_1_ep9.webm" % persistent.img_dir, start_image="anim_cumpetition_1_ep9_start", channel = "sex1")
image anim_cumpetition_2_ep9 = Movie(play="%s/movies/ep9/anim_cumpetition_2_ep9.webm" % persistent.img_dir, start_image="anim_cumpetition_2_ep9_start", channel = "sex2")
image anim_cumpetition_3_ep9 = Movie(play="%s/movies/ep9/anim_cumpetition_3_ep9.webm" % persistent.img_dir, start_image="anim_cumpetition_3_ep9_start", channel = "sex3")
image anim_cumpetition_4_ep9 = Movie(play="%s/movies/ep9/anim_cumpetition_4_ep9.webm" % persistent.img_dir, start_image="anim_cumpetition_4_ep9_start", channel = "sex4")
image anim_cumpetition_5_ep9 = Movie(play="%s/movies/ep9/anim_cumpetition_5_ep9.webm" % persistent.img_dir, start_image="anim_cumpetition_5_ep9_start", channel = "sex5")
image anim_ln_bj_ep9 = Movie(play="%s/movies/ep9/anim_ln_bj_ep9.webm" % persistent.img_dir, start_image="anim_ln_bj_ep9_start", channel = "sex1")
image anim_ln_bj2_ep9 = Movie(play="%s/movies/ep9/anim_ln_bj2_ep9.webm" % persistent.img_dir, start_image="anim_ln_bj2_ep9_start", channel = "sex2")
image anim_ln_bj3_ep9 = Movie(play="%s/movies/ep9/anim_ln_bj3_ep9.webm" % persistent.img_dir, start_image="anim_ln_bj3_ep9_start", channel = "sex3")
image anim_ln_bj4_ep9 = Movie(play="%s/movies/ep9/anim_ln_bj4_ep9.webm" % persistent.img_dir, start_image="anim_ln_bj4_ep9_start", channel = "sex4")
image anim_ln_bj5_ep9 = Movie(play="%s/movies/ep9/anim_ln_bj5_ep9.webm" % persistent.img_dir, start_image="anim_ln_bj5_ep9_start", channel = "sex5")
image anim_ln_miss1_ep9 = Movie(play="%s/movies/ep9/anim_ln_miss1_ep9.webm" % persistent.img_dir, start_image="anim_ln_miss1_ep9_start", channel = "sex6")
image anim_ln_miss2_ep9 = Movie(play="%s/movies/ep9/anim_ln_miss2_ep9.webm" % persistent.img_dir, start_image="anim_ln_miss2_ep9_start", channel = "sex7")
image anim_ln_miss3_ep9 = Movie(play="%s/movies/ep9/anim_ln_miss3_ep9.webm" % persistent.img_dir, start_image="anim_ln_miss3_ep9_start", channel = "sex8")
image anim_ln_miss4_ep9 = Movie(play="%s/movies/ep9/anim_ln_miss4_ep9.webm" % persistent.img_dir, start_image="anim_ln_miss4_ep9_start", channel = "sex9")
image anim_ln_doggy_ep9 = Movie(play="%s/movies/ep9/anim_ln_doggy_ep9.webm" % persistent.img_dir, start_image="anim_ln_doggy_ep9_start", channel = "sex10")
image anim_ln_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_ln_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_ln_doggy2_ep9_start", channel = "sex11")
image anim_ln_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_ln_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_ln_doggy3_ep9_start", channel = "sex12")
image anim_ln_doggy4_ep9 = Movie(play="%s/movies/ep9/anim_ln_doggy4_ep9.webm" % persistent.img_dir, start_image="anim_ln_doggy4_ep9_start", channel = "sex13")
image anim_ln_side1_ep9 = Movie(play="%s/movies/ep9/anim_ln_side1_ep9.webm" % persistent.img_dir, start_image="anim_ln_side1_ep9_start", channel = "sex14")
image anim_ln_side2_ep9 = Movie(play="%s/movies/ep9/anim_ln_side2_ep9.webm" % persistent.img_dir, start_image="anim_ln_side2_ep9_start", channel = "sex15")
image anim_ln_ride1_ep9 = Movie(play="%s/movies/ep9/anim_ln_ride1_ep9.webm" % persistent.img_dir, start_image="anim_ln_ride1_ep9_start", channel = "sex16")
image anim_ln_ride2_ep9 = Movie(play="%s/movies/ep9/anim_ln_ride2_ep9.webm" % persistent.img_dir, start_image="anim_ln_ride2_ep9_start", channel = "sex17")
image anim_ln_ride3_ep9 = Movie(play="%s/movies/ep9/anim_ln_ride3_ep9.webm" % persistent.img_dir, start_image="anim_ln_ride3_ep9_start", channel = "sex18")
image anim_ln_cum_ep9 = Movie(play="%s/movies/ep9/anim_ln_cum_ep9.webm" % persistent.img_dir, start_image="anim_ln_cum_ep9_start", channel = "sex19")

image anim_ln_hit_ep9 = Movie(play="%s/movies/ep9/anim_ln_hit_ep9.webm" % persistent.img_dir, start_image="anim_ln_hit_ep9_start", channel = "sex20", loop=False)
image bg anim_ln_hit_ep9 movie:
    "anim_ln_hit_ep9"
    pause 4
    "anim_ln_hit_ep9_end"
image anim_wave3_ep9 = Movie(play="%s/movies/ep9/anim_wave3_ep9.webm" % persistent.img_dir, start_image="anim_wave3_ep9_start", channel = "sex1", loop=False)
image bg anim_wave3_ep9 movie:
    "anim_wave3_ep9"
    function play_wave3_footsteps
    pause 54.24
    function play_wave3_car_pass
    pause 7.04
    function play_wave3_car_hit
    pause 4.5
    function play_wave3_squirt
    pause 8.32
    function play_wave3_car_whoosh
    pause 1.01
    function play_wave3_car_whoosh
    pause 1.03
    function play_wave3_car_shove
    pause 6.99
    "anim_wave3_ep9_end"

image anim_riona_kiss_ep9 = Movie(play="%s/movies/ep9/anim_riona_kiss_ep9.webm" % persistent.img_dir, start_image="anim_riona_kiss_ep9_start", channel = "sex1")
image anim_jm_rim_ep9 = Movie(play="%s/movies/ep9/anim_jm_rim_ep9.webm" % persistent.img_dir, start_image="anim_jm_rim_ep9_start", channel = "sex1")
image anim_jm_rim2_ep9 = Movie(play="%s/movies/ep9/anim_jm_rim2_ep9.webm" % persistent.img_dir, start_image="anim_jm_rim2_ep9_start", channel = "sex2")
image anim_jm_asshole_ep9 = Movie(play="%s/movies/ep9/anim_jm_asshole_ep9.webm" % persistent.img_dir, start_image="anim_jm_asshole_ep9_start", channel = "sex3")
image anim_jm_finger_ep9 = Movie(play="%s/movies/ep9/anim_jm_finger_ep9.webm" % persistent.img_dir, start_image="anim_jm_finger_ep9_start", channel = "sex4")
image anim_jm_pussy_ep9 = Movie(play="%s/movies/ep9/anim_jm_pussy_ep9.webm" % persistent.img_dir, start_image="anim_jm_pussy_ep9_start", channel = "sex5")
image anim_jm_pussy2_ep9 = Movie(play="%s/movies/ep9/anim_jm_pussy2_ep9.webm" % persistent.img_dir, start_image="anim_jm_pussy2_ep9_start", channel = "sex6")
image anim_maya_hj_ep9 = Movie(play="%s/movies/ep9/anim_maya_hj_ep9.webm" % persistent.img_dir, start_image="anim_maya_hj_ep9_start", channel = "sex7")
image anim_maya_hj2_ep9 = Movie(play="%s/movies/ep9/anim_maya_hj2_ep9.webm" % persistent.img_dir, start_image="anim_maya_hj2_ep9_start", channel = "sex8")
image anim_maya_boobjob1_ep9 = Movie(play="%s/movies/ep9/anim_maya_boobjob1_ep9.webm" % persistent.img_dir, start_image="anim_maya_boobjob1_ep9_start", channel = "sex9")
image anim_maya_finger_ep9 = Movie(play="%s/movies/ep9/anim_maya_finger_ep9.webm" % persistent.img_dir, start_image="anim_maya_finger_ep9_start", channel = "sex10")
image anim_maya_finger2_ep9 = Movie(play="%s/movies/ep9/anim_maya_finger2_ep9.webm" % persistent.img_dir, start_image="anim_maya_finger2_ep9_start", channel = "sex11")
image anim_maya_panties_lick_ep9 = Movie(play="%s/movies/ep9/anim_maya_panties_lick_ep9.webm" % persistent.img_dir, start_image="anim_maya_panties_lick_ep9_start", channel = "sex12")
image anim_josy_suck_ep9 = Movie(play="%s/movies/ep9/anim_josy_suck_ep9.webm" % persistent.img_dir, start_image="anim_josy_suck_ep9_start", channel = "sex13")
image anim_josy_shake_ep9 = Movie(play="%s/movies/ep9/anim_josy_shake_ep9.webm" % persistent.img_dir, start_image="anim_josy_shake_ep9_start", channel = "sex14")
image anim_josy_squeeze_ep9 = Movie(play="%s/movies/ep9/anim_josy_squeeze_ep9.webm" % persistent.img_dir, start_image="anim_josy_squeeze_ep9_start", channel = "sex15")
image anim_jm_lick1_ep9 = Movie(play="%s/movies/ep9/anim_jm_lick1_ep9.webm" % persistent.img_dir, start_image="anim_jm_lick1_ep9_start", channel = "sex16")
image anim_jm_lick2_ep9 = Movie(play="%s/movies/ep9/anim_jm_lick2_ep9.webm" % persistent.img_dir, start_image="anim_jm_lick2_ep9_start", channel = "sex17")
image anim_jm_bj1_ep9 = Movie(play="%s/movies/ep9/anim_jm_bj1_ep9.webm" % persistent.img_dir, start_image="anim_jm_bj1_ep9_start", channel = "sex18")
image anim_jm_bj2_ep9 = Movie(play="%s/movies/ep9/anim_jm_bj2_ep9.webm" % persistent.img_dir, start_image="anim_jm_bj2_ep9_start", channel = "sex19")
image anim_jm_hj1_ep9 = Movie(play="%s/movies/ep9/anim_jm_hj1_ep9.webm" % persistent.img_dir, start_image="anim_jm_hj1_ep9_start", channel = "sex20")
image anim_jm_hj2_ep9 = Movie(play="%s/movies/ep9/anim_jm_hj2_ep9.webm" % persistent.img_dir, start_image="anim_jm_hj2_ep9_start", channel = "sex1")
image anim_jm_hj3_ep9 = Movie(play="%s/movies/ep9/anim_jm_hj3_ep9.webm" % persistent.img_dir, start_image="anim_jm_hj3_ep9_start", channel = "sex2")
image anim_jm_hj4_ep9 = Movie(play="%s/movies/ep9/anim_jm_hj4_ep9.webm" % persistent.img_dir, start_image="anim_jm_hj4_ep9_start", channel = "sex3")
image anim_jm_hj5_ep9 = Movie(play="%s/movies/ep9/anim_jm_hj5_ep9.webm" % persistent.img_dir, start_image="anim_jm_hj5_ep9_start", channel = "sex4")
image anim_mj_panty_grind_ep9 = Movie(play="%s/movies/ep9/anim_mj_panty_grind_ep9.webm" % persistent.img_dir, start_image="anim_mj_panty_grind_ep9_start", channel = "sex5")
image anim_mj_panty_grind2_ep9 = Movie(play="%s/movies/ep9/anim_mj_panty_grind2_ep9.webm" % persistent.img_dir, start_image="anim_mj_panty_grind2_ep9_start", channel = "sex6")
image anim_jm_doggy1_ep9 = Movie(play="%s/movies/ep9/anim_jm_doggy1_ep9.webm" % persistent.img_dir, start_image="anim_jm_doggy1_ep9_start", channel = "sex7")
image anim_jm_doggy2_ep9 = Movie(play="%s/movies/ep9/anim_jm_doggy2_ep9.webm" % persistent.img_dir, start_image="anim_jm_doggy2_ep9_start", channel = "sex8")
image anim_jm_doggy3_ep9 = Movie(play="%s/movies/ep9/anim_jm_doggy3_ep9.webm" % persistent.img_dir, start_image="anim_jm_doggy3_ep9_start", channel = "sex9")
image anim_jm_doggy4_ep9 = Movie(play="%s/movies/ep9/anim_jm_doggy4_ep9.webm" % persistent.img_dir, start_image="anim_jm_doggy4_ep9_start", channel = "sex10")
image anim_jm_doggy5_ep9 = Movie(play="%s/movies/ep9/anim_jm_doggy5_ep9.webm" % persistent.img_dir, start_image="anim_jm_doggy5_ep9_start", channel = "sex11")
image anim_jm_miss1_ep9 = Movie(play="%s/movies/ep9/anim_jm_miss1_ep9.webm" % persistent.img_dir, start_image="anim_jm_miss1_ep9_start", channel = "sex11")
image anim_jm_miss2_ep9 = Movie(play="%s/movies/ep9/anim_jm_miss2_ep9.webm" % persistent.img_dir, start_image="anim_jm_miss2_ep9_start", channel = "sex12")
image anim_jm_miss3_ep9 = Movie(play="%s/movies/ep9/anim_jm_miss3_ep9.webm" % persistent.img_dir, start_image="anim_jm_miss3_ep9_start", channel = "sex13")
image anim_jm_rev1_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev1_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev1_ep9_start", channel = "sex14")
image anim_jm_rev2_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev2_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev2_ep9_start", channel = "sex15")
image anim_jm_rev3_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev3_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev3_ep9_start", channel = "sex16")
image anim_jm_rev4_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev4_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev4_ep9_start", channel = "sex17")
image anim_jm_rev5_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev5_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev5_ep9_start", channel = "sex18")
image anim_jm_rev6_ep9 = Movie(play="%s/movies/ep9/anim_jm_rev6_ep9.webm" % persistent.img_dir, start_image="anim_jm_rev6_ep9_start", channel = "sex19")
image anim_jm_double1_ep9 = Movie(play="%s/movies/ep9/anim_jm_double1_ep9.webm" % persistent.img_dir, start_image="anim_jm_double1_ep9_start", channel = "sex20")
image anim_jm_double2_ep9 = Movie(play="%s/movies/ep9/anim_jm_double2_ep9.webm" % persistent.img_dir, start_image="anim_jm_double2_ep9_start", channel = "sex1")
image anim_jm_ride1_ep9 = Movie(play="%s/movies/ep9/anim_jm_ride1_ep9.webm" % persistent.img_dir, start_image="anim_jm_ride1_ep9_start", channel = "sex2")
image anim_jm_stand1_ep9 = Movie(play="%s/movies/ep9/anim_jm_stand1_ep9.webm" % persistent.img_dir, start_image="anim_jm_stand1_ep9_start", channel = "sex3")
image anim_jm_stand2_ep9 = Movie(play="%s/movies/ep9/anim_jm_stand2_ep9.webm" % persistent.img_dir, start_image="anim_jm_stand2_ep9_start", channel = "sex4")
image anim_jm_stand3_ep9 = Movie(play="%s/movies/ep9/anim_jm_stand3_ep9.webm" % persistent.img_dir, start_image="anim_jm_stand3_ep9_start", channel = "sex5")
image anim_jm_tease_ep9 = Movie(play="%s/movies/ep9/anim_jm_tease_ep9.webm" % persistent.img_dir, start_image="anim_jm_tease_ep9_start", channel = "sex6")
image anim_jm_cum_ep9 = Movie(play="%s/movies/ep9/anim_jm_cum_ep9.webm" % persistent.img_dir, start_image="anim_jm_cum_ep9_start", channel = "sex7")
image anim_jm_cum2_ep9 = Movie(play="%s/movies/ep9/anim_jm_cum2_ep9.webm" % persistent.img_dir, start_image="anim_jm_cum2_ep9_start", channel = "sex8")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

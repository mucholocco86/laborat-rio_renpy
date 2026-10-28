image anim_brawler_movie = Movie(play="%s/minigames/brawler/displayables/anim_brawler_movie.webm" % persistent.img_dir, start_image="anim_brawler_movie_start", channel = "sex1")
image bg anim_brawler_movie movie:
    "anim_brawler_movie"
    pause 5
    function play_bn_main
    pause 18
    repeat





image brawler_alex_neutral = Movie(play="%s/ep10/brawler/alex/brawler_alex_neutral.webm" % persistent.img_dir, start_image = "brawler_alex_neutral_start", channel = "sex1")
image brawler_alex_flurry_init = Movie(play="%s/ep10/brawler/alex/brawler_alex_flurry.webm" % persistent.img_dir, start_image = "brawler_alex_flurry_start", channel = "sex2")
image brawler_alex_crippling_init = Movie(play="%s/movies/ep11/brawler_alex_crippling.webm" % persistent.img_dir, start_image = "brawler_alex_crippling_start", channel = "sex3")
image brawler_alex_highkick = Movie(play="%s/movies/ep12/brawler_alex_highkick.webm" % persistent.img_dir, start_image = "brawler_alex_highkick_start", channel = "sex4")

image brawler_alex_flurry:
    "brawler_alex_flurry_init"
    pause 1.0
    "brawler_alex_flurry_end"
    "brawler_dwyane_watch1"

image brawler_alex_crippling:
    "brawler_alex_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_alex_crippling_end"
    "brawler_dwyane_watch1"

image brawler_alex_highkick:
    "brawler_alex_highkick_init"
    pause 2.0
    "brawler_alex_highkick_end"
    "brawler_dwyane_watch2"


image brawler_alex_mc_power2:
    function bn_play_punch
    "brawler_alex_mc_power2a" with vpunch
    pause 0.5
    choice:
        function bn_play_kick_slap2
        "brawler_alex_mc_power2b" with hpunch
    choice:
        function bn_play_punch
        "brawler_alex_mc_power2c" with hpunch

image brawler_alex_mc_power3:
    function bn_play_punch
    "brawler_alex_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_alex_mc_power3b" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_alex_mc_power3c" with hpunch
    pause 0.5
    choice:
        "brawler_alex_mc_power3d" with dissolve
    choice:
        "brawler_alex_mc_power3d" with dissolve
    choice:
        "brawler_alex_mc_power3d" with dissolve
    choice:
        "brawler_dwyane_watch1"

image brawler_alex_mc_power4:
    function bn_play_punch
    "brawler_alex_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_alex_mc_power4b" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_alex_mc_power4c" with vpunch
    pause 0.5

image brawler_alex_mc_rage:
    function bn_play_punch
    "brawler_alex_mc_rage1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_alex_mc_rage2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_alex_mc_rage3" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_alex_mc_rage4" with hpunch
    pause 0.5
    "brawler_dwyane_watch2"





image brawler_chao_neutral = Movie(play="%s/ep10/brawler/chao/brawler_chao_neutral.webm" % persistent.img_dir, start_image = "brawler_chao_neutral_start", channel = "sex1")
image brawler_chao_flurry_init = Movie(play="%s/ep10/brawler/chao/brawler_chao_flurry.webm" % persistent.img_dir, start_image = "brawler_chao_flurry_start", channel = "sex2")
image brawler_chao_crippling_init = Movie(play="%s/movies/ep11/brawler_chao_crippling.webm" % persistent.img_dir, start_image = "brawler_chao_crippling_start", channel = "sex3")
image brawler_chao_highkick = Movie(play="%s/movies/ep12/brawler_chao_highkick.webm" % persistent.img_dir, start_image = "brawler_chao_highkick_start", channel = "sex4")

image brawler_chao_flurry:
    "brawler_chao_flurry_init"
    pause 1.0
    "brawler_chao_flurry_end"
    "brawler_dwyane_watch2"

image brawler_chao_crippling:
    "brawler_chao_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_chao_crippling_end"
    "brawler_dwyane_watch2"

image brawler_chao_highkick:
    "brawler_chao_highkick_init"
    pause 2.0
    "brawler_chao_highkick_end"
    "brawler_dwyane_watch2"


image brawler_chao_cpu_special1:
    function bn_play_kick
    "brawler_chao_cpu_special" with vpunch
    pause 1
    "brawler_chao_cpu_special2" with dissolve

image brawler_chao_mc_rage:
    function bn_play_punch
    "brawler_chao_mc_punch1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_chao_mc_punch2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_chao_mc_punch3" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_chao_mc_kick1" with hpunch
    pause 0.5
    "brawler_dwyane_watch2"

image brawler_chao_mc_power3:
    function bn_play_kick_slap
    "brawler_chao_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_chao_mc_power3b" with hpunch

image brawler_chao_mc_power4:
    function bn_play_kick_slap2
    "brawler_chao_mc_power4a" with hpunch
    pause 0.5
    "brawler_chao_mc_power4b" with dissolve





image brawler_dwyane_neutral = Movie(play="%s/ep10/brawler/dwyane/brawler_dwyane_neutral.webm" % persistent.img_dir, start_image = "brawler_dwyane_neutral_start", channel = "sex1")
image brawler_dwyane_flurry_init = Movie(play="%s/ep10/brawler/dwyane/brawler_dwyane_flurry.webm" % persistent.img_dir, start_image = "brawler_dwyane_flurry_start", channel = "sex2")
image brawler_dwyane_crippling_init = Movie(play="%s/movies/ep11/brawler_dwyane_crippling.webm" % persistent.img_dir, start_image = "brawler_dwyane_crippling_start", channel = "sex3")
image brawler_dwyane_highkick = Movie(play="%s/movies/ep12/brawler_dwyane_highkick.webm" % persistent.img_dir, start_image = "brawler_dwyane_highkick_start", channel = "sex4")

image brawler_dwyane_flurry:
    "brawler_dwyane_flurry_init"
    pause 1.0
    "brawler_dwyane_flurry_end"

image brawler_dwyane_crippling:
    "brawler_dwyane_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_dwyane_crippling_end"

image brawler_dwyane_highkick:
    "brawler_dwyane_highkick_init"
    pause 2.0
    "brawler_dwyane_highkick_end"


image brawler_dwyane_cpu_special1:
    function bn_play_punch
    "brawler_dwyane_cpu_power3" with vpunch
    pause 0.5
    function bn_play_kick
    "brawler_dwyane_cpu_special" with vpunch

image brawler_dwyane_mc_rage:
    function bn_play_punch
    "brawler_dwyane_mc_punch1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dwyane_mc_punch2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dwyane_mc_power4a" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_dwyane_mc_power4b" with hpunch

image brawler_dwyane_mc_power3:
    function bn_play_punch
    "brawler_dwyane_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dwyane_mc_power3b" with hpunch

image brawler_dwyane_mc_power4:
    function bn_play_punch
    "brawler_dwyane_mc_power4a" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_dwyane_mc_power4b" with dissolve





image brawler_tate_neutral = Movie(play="%s/ep10/brawler/tate/brawler_tate_neutral.webm" % persistent.img_dir, start_image = "brawler_tate_neutral_start", channel = "sex1")
image brawler_tate_flurry_init = Movie(play="%s/ep10/brawler/tate/brawler_tate_flurry.webm" % persistent.img_dir, start_image = "brawler_tate_flurry_start", channel = "sex2")
image brawler_tate_crippling_init = Movie(play="%s/movies/ep11/brawler_tate_crippling.webm" % persistent.img_dir, start_image = "brawler_tate_crippling_start", channel = "sex3")
image brawler_tate_highkick = Movie(play="%s/movies/ep12/brawler_tate_highkick.webm" % persistent.img_dir, start_image = "brawler_tate_highkick_start", channel = "sex4")

image brawler_tate_flurry:
    "brawler_tate_flurry_init"
    pause 1.0
    "brawler_tate_flurry_end"
    "brawler_dwyane_watch2" with dissolve

image brawler_tate_crippling:
    "brawler_tate_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_tate_crippling_end"
    "brawler_dwyane_watch2" with dissolve

image brawler_tate_highkick:
    "brawler_tate_highkick_init"
    pause 2.0
    "brawler_tate_highkick_end"
    "brawler_dwyane_watch2" with dissolve


image brawler_tate_cpu_special1:
    function bn_play_punch
    "brawler_tate_cpu_special" with vpunch
    pause 0.5
    function bn_play_kick_slap2
    "brawler_tate_cpu_special2" with hpunch

image brawler_tate_mc_rage:
    function bn_play_punch
    "brawler_tate_mc_punch1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_tate_mc_punch2" with hpunch
    pause 0.5
    function bn_play_kick_slap2
    "brawler_tate_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_tate_mc_power5" with hpunch

image brawler_tate_mc_power3:
    function bn_play_punch
    "brawler_tate_mc_power3a" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_tate_mc_power3b" with hpunch

image brawler_tate_mc_power4:
    function bn_play_kick_slap2
    "brawler_tate_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_tate_mc_power4b" with hpunch





image brawler_troy_neutral = Movie(play="%s/ep10/brawler/troy/brawler_troy_neutral.webm" % persistent.img_dir, start_image = "brawler_troy_neutral_start", channel = "sex1")
image brawler_troy_flurry_init = Movie(play="%s/ep10/brawler/troy/brawler_troy_flurry.webm" % persistent.img_dir, start_image = "brawler_troy_flurry_start", channel = "sex2")
image brawler_troy_crippling_init = Movie(play="%s/movies/ep11/brawler_troy_crippling.webm" % persistent.img_dir, start_image = "brawler_troy_crippling_start", channel = "sex3")
image brawler_troy_highkick = Movie(play="%s/movies/ep12/brawler_troy_highkick.webm" % persistent.img_dir, start_image = "brawler_troy_highkick_start", channel = "sex4")

image brawler_troy_flurry:
    "brawler_troy_flurry_init"
    pause 1.0
    "brawler_troy_flurry_end"
    "brawler_dwyane_watch2" with dissolve

image brawler_troy_crippling:
    "brawler_troy_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_troy_crippling_end"
    "brawler_dwyane_watch2" with dissolve

image brawler_troy_highkick:
    "brawler_troy_highkick_init"
    pause 2.0
    "brawler_troy_highkick_end"
    "brawler_dwyane_watch2" with dissolve


image brawler_troy_cpu_special:
    function bn_play_punch
    "brawler_troy_cpu_power3" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_troy_cpu_special1" with vpunch

image brawler_troy_mc_rage:
    function bn_play_punch
    "brawler_troy_mc_punch1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_troy_mc_punch2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_troy_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_troy_mc_power4b" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_troy_mc_power5" with vpunch

image brawler_troy_mc_power3:
    function bn_play_punch
    "brawler_troy_mc_power3a" with hpunch
    pause 0.5
    function bn_play_kick_slap2
    "brawler_troy_mc_power3b" with hpunch

image brawler_troy_mc_power4:
    function bn_play_punch
    "brawler_troy_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_troy_mc_power4b" with hpunch





image brawler_dawe_neutral = Movie(play="%s/movies/ep11/brawler_dawe_neutral.webm" % persistent.img_dir, start_image = "brawler_dawe_neutral_start", channel = "sex1")
image brawler_dawe_flurry_init = Movie(play="%s/movies/ep11/brawler_dawe_flurry.webm" % persistent.img_dir, start_image = "brawler_dawe_flurry_start", channel = "sex2")
image brawler_dawe_crippling_init = Movie(play="%s/movies/ep11/brawler_dawe_crippling.webm" % persistent.img_dir, start_image = "brawler_dawe_crippling_start", channel = "sex3")
image brawler_dawe_highkick = Movie(play="%s/movies/ep12/brawler_dawe_highkick.webm" % persistent.img_dir, start_image = "brawler_dawe_highkick_start", channel = "sex4")

image brawler_dawe_flurry:
    "brawler_dawe_flurry_init"
    pause 1.0
    "brawler_dawe_flurry_end"

image brawler_dawe_crippling:
    "brawler_dawe_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_dawe_crippling_end"

image brawler_dawe_highkick:
    "brawler_dawe_highkick_init"
    pause 2.0
    "brawler_dawe_highkick_end"


image brawler_dawe_mc_power2:
    function bn_play_punch
    "brawler_dawe_mc_power2a" with vpunch
    pause 0.5
    choice:
        function bn_play_kick_slap2
        "brawler_dawe_mc_power2b" with hpunch
    choice:
        function bn_play_punch
        "brawler_dawe_mc_power2c" with hpunch

image brawler_dawe_mc_power3:
    function bn_play_punch
    "brawler_dawe_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dawe_mc_power3b" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_dawe_mc_power3c" with hpunch
    pause 0.5
    choice:
        "brawler_dawe_mc_power3d" with dissolve
    choice:
        "brawler_dawe_mc_power3d" with dissolve
    choice:
        "brawler_dawe_mc_power3d" with dissolve
    choice:
        "brawler_tate_watch1"

image brawler_dawe_mc_power4:
    function bn_play_punch
    "brawler_dawe_mc_power4a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dawe_mc_power4b" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_dawe_mc_power4c" with vpunch
    pause 0.5

image brawler_dawe_mc_rage:
    function bn_play_punch
    "brawler_dawe_mc_rage1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dawe_mc_rage2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dawe_mc_rage3" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_dawe_mc_rage4" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_dawe_mc_rage5" with vpunch
    pause 0.5
    "brawler_tate_watch2"






image brawler_johnny_neutral = Movie(play="%s/movies/ep12/brawler_johnny_neutral.webm" % persistent.img_dir, start_image = "brawler_johnny_neutral_start", channel = "sex1")
image brawler_johnny_flurry_init = Movie(play="%s/movies/ep12/brawler_johnny_flurry.webm" % persistent.img_dir, start_image = "brawler_johnny_flurry_start", channel = "sex2")
image brawler_johnny_crippling_init = Movie(play="%s/movies/ep12/brawler_johnny_crippling.webm" % persistent.img_dir, start_image = "brawler_johnny_crippling_start", channel = "sex3")
image brawler_johnny_highkick_init = Movie(play="%s/movies/ep12/brawler_johnny_highkick.webm" % persistent.img_dir, start_image = "brawler_johnny_highkick_start", channel = "sex4")

image brawler_johnny_flurry:
    function fight_cheers
    "brawler_johnny_flurry_init"
    pause 1.0
    "brawler_johnny_flurry_end"
    choice:
        "brawler_johnny_watch1"
    choice:
        "brawler_johnny_watch2"
    choice:
        "brawler_johnny_watch3"

image brawler_johnny_crippling:
    function fight_cheers
    "brawler_johnny_crippling_init"
    pause 0.1
    function bn_play_kick_slap
    pause 0.75
    function bn_play_punch
    pause 0.15
    "brawler_johnny_crippling_end"
    choice:
        "brawler_johnny_watch1"
    choice:
        "brawler_johnny_watch2"
    choice:
        "brawler_johnny_watch3"

image brawler_johnny_highkick:
    function fight_cheers
    "brawler_johnny_highkick_init"
    pause 2.0
    "brawler_johnny_highkick_end"
    choice:
        "brawler_johnny_watch1"
    choice:
        "brawler_johnny_watch2"
    choice:
        "brawler_johnny_watch3"


image brawler_johnny_mc_power2:
    function bn_play_punch
    "brawler_johnny_mc_power2a" with vpunch
    pause 0.5
    choice:
        function bn_play_punch
        "brawler_johnny_mc_power2b" with hpunch
    choice:
        function bn_play_kick_body
        "brawler_johnny_mc_power2c" with hpunch

image brawler_johnny_mc_power3:
    function fight_cheers
    function bn_play_kick_slap
    "brawler_johnny_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3b" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3c" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3d" with hpunch
    pause 0.5
    choice:
        "brawler_johnny_watch1"
    choice:
        "brawler_johnny_watch2"
    choice:
        "brawler_johnny_watch3"

image brawler_johnny_mc_power4:
    function bn_play_punch
    "brawler_johnny_mc_power4a" with hpunch
    pause 0.5
    function bn_play_kick
    "brawler_johnny_mc_power4b" with hpunch
    pause 0.5
    function bn_play_kick_slap
    "brawler_johnny_mc_power4c" with vpunch
    pause 0.5

image brawler_johnny_mc_power4jms:
    function fight_cheers
    function bn_play_kick_slap
    "brawler_johnny_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3b" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3c" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3d" with hpunch
    pause 0.5
    "brawler_johnny_watch4"

image brawler_johnny_mc_power4z:
    function fight_cheers
    function bn_play_kick_slap
    "brawler_johnny_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3b" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3c" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3d" with hpunch
    pause 0.5
    "brawler_johnny_watch4b"

image brawler_johnny_mc_power4n:
    function fight_cheers
    function bn_play_kick_slap
    "brawler_johnny_mc_power3a" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3b" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3c" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_power3d" with hpunch
    pause 0.5
    "brawler_johnny_watch4c"

image brawler_johnny_mc_rage:
    function fight_cheers
    function bn_play_punch
    "brawler_johnny_mc_rage1" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_rage2" with hpunch
    pause 0.5
    function bn_play_punch
    "brawler_johnny_mc_rage3" with hpunch
    pause 0.5
    function bn_play_kick_slap2
    "brawler_johnny_mc_rage4" with hpunch
    pause 0.5
    choice:
        "brawler_johnny_watch1"
    choice:
        "brawler_johnny_watch2"
    choice:
        "brawler_johnny_watch3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label epi_drawing_game3_label:
$ drw_timer = 0
$ drw_fail = 0
$ renpy.block_rollback()
call screen epi_drawing_game_ready_screen

$ ztime = time.time()
$ drw_pos = []
$ drw_pos.append([200,200])
$ renpy.block_rollback()
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1300,300])
$ drw_pos.append([1200,300])
$ drw_pos.append([1400,300])
$ drw_pos.append([1300,400])
$ drw_pos.append([1300,200])
$ drw_pos.append([1500,200])
$ drw_pos.append([1100,200])
$ drw_pos.append([1200,100])
$ drw_pos.append([1400,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([300,700])
$ drw_pos.append([300,500])
$ drw_pos.append([400,400])
$ drw_pos.append([400,600])
$ drw_pos.append([400,800])
$ drw_pos.append([500,500])
$ drw_pos.append([500,700])
$ drw_pos.append([600,600])
$ drw_pos.append([600,800])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([900,100])
$ drw_pos.append([700,200])
$ drw_pos.append([700,300])
$ drw_pos.append([800,100])
$ drw_pos.append([800,400])
$ drw_pos.append([900,200])
$ drw_pos.append([900,400])
$ drw_pos.append([1000,100])
$ drw_pos.append([1000,300])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1800,900])
$ drw_pos.append([1400,500])
$ drw_pos.append([1400,900])
$ drw_pos.append([1500,600])
$ drw_pos.append([1500,800])
$ drw_pos.append([1600,700])
$ drw_pos.append([1700,600])
$ drw_pos.append([1700,800])
$ drw_pos.append([1800,500])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([400,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([900,800])
$ drw_pos.append([600,600])
$ drw_pos.append([600,800])
$ drw_pos.append([700,700])
$ drw_pos.append([800,400])
$ drw_pos.append([800,600])
$ drw_pos.append([900,500])
$ drw_pos.append([1000,400])
$ drw_pos.append([1100,500])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([400,100])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([1200,400])
$ drw_pos.append([1100,300])
$ drw_pos.append([1100,400])
$ drw_pos.append([1100,500])
$ drw_pos.append([1100,600])
$ drw_pos.append([1100,200])
$ drw_pos.append([1200,600])
$ drw_pos.append([1200,200])
$ drw_pos.append([1300,200])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
$ drw_pos = []
$ drw_pos.append([200,400])
$ renpy.block_rollback()
play sound "sound_effects/interlude/sketch.mp3"
call screen epi_drawing_game_screen
play sound "sound_effects/interlude/sketch.mp3"

$ ztime = time.time() - ztime
$ tmpInt = max(100-drw_fail*10-ztime*1,0)
if tmpInt > 90.0 and drw_fail == 0:
    $ epi_draw_scores.append("s")
elif tmpInt > 80.0 and drw_fail == 0:
    $ epi_draw_scores.append("a")
elif tmpInt > 70.0:
    $ epi_draw_scores.append("b")
elif tmpInt > 60.0:
    $ epi_draw_scores.append("c")
elif tmpInt > 50.0:
    $ epi_draw_scores.append("d")
elif tmpInt > 40.0:
    $ epi_draw_scores.append("e")
else:
    $ epi_draw_scores.append("f")
$ renpy.block_rollback()
call screen drawing_screen_rank(0.05,0.9)

if epi_draw_scores[-1] == "s":
    if not persistent.epi_card7:
        $ unlock_epi_render(7)
    jump epi_after_drawing3_label

call screen zoey_choice_screen("Retry",300,100, "Continue",1400,100)
if tmp_choice == 1:
    $ epi_draw_scores.pop()
    scene epi_summer2 with dissolve
    jump epi_drawing_game3_label
else:
    jump epi_after_drawing3_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
